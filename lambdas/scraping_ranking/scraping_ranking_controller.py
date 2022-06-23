import json
import requests
from bs4 import BeautifulSoup
import boto3
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from boto3.dynamodb.conditions import Key
from tools.http_error import HTTPError
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all, patch

patch_all()
patch(['boto3'])


aws_region = os.environ.get('AWS_REGION')

sns_arn = os.environ.get('SNS_SCRAPING_ARN')

sns_client = boto3.client('sns', region_name=aws_region)


def scraping_ranking(data):
    try:
        options = Options()
        options.binary_location = '/opt/headless-chromium'
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('/opt/chromedriver',chrome_options=options)
        driver.get("https://www.worldpadeltour.com/jugadores/?ranking=masculino")
        SCROLL_PAUSE_TIME = 0.5
        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")        
        for x in range(5):
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")        
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        driver.execute_script("window.scrollTo(0, 0);")
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        ranking_list = []

        for player_card in soup.find_all('li', class_="c-player-card__item"):
            #Get player route
            player_route = player_card.find('a', class_="c-trigger", href=True)['href']
            ranking_list.append(player_route)

        #FAN-OUT
        for player_url in ranking_list[0:50]:
            sns_client.publish(
                TargetArn=sns_arn,
                Message=json.dumps({'default': json.dumps({'url':player_url})}),
                MessageStructure='json'
            )

        response = {"Ranking_Scrapped": True, "Ranking":json.dumps(ranking_list)}
        return response

    except Exception as e:
        raise HTTPError(500, "Internal Error: %s" % e)