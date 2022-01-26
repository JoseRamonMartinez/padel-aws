import json
import requests
from bs4 import BeautifulSoup
import re
import boto3
import os
import time
import unicodedata
from datetime import datetime, timedelta
from boto3.dynamodb.conditions import Key
from tools.http_error import HTTPError

aws_region = os.environ.get('AWS_REGION')
sns_arn = os.environ.get('SNS_POST_PLAYER_ARN')

sns_client = boto3.client('sns', region_name=aws_region)

def scraping_player(data):
    try:
        agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        result = requests.get(data["url"], headers=agent)
        src = result.content
        soup = BeautifulSoup(src, 'html.parser')
        player_data_list = []
        player_data_list.append(re.sub(r'.*jugadores/(.*)/.*', r'\1', data["url"]))

        for player_data in soup.find_all('p', class_="c-ranking-header__data"):
            player_data_list.append( player_data.get_text())

        for player_data in soup.find_all('li', class_="c-player__data-item"):
            player_data_list.append(''.join((c for c in unicodedata.normalize('NFD', player_data.find('p').getText()) if unicodedata.category(c) != 'Mn')))

        response = {
                'name': player_data_list[0],
                'position':player_data_list[1],
                'data':{
                    'score':player_data_list[2],
                    'played_matches':player_data_list[3],
                    'won_matches':player_data_list[4],
                    'lost_matches':player_data_list[5],
                    'effectiveness':player_data_list[6],
                    'winning_streak':player_data_list[7],
                    'partner':player_data_list[8],
                    'side':player_data_list[9],
                    'born_place':player_data_list[10],
                    'born_date':player_data_list[11],
                    'height':player_data_list[12],
                    'home_place':player_data_list[13]  
                }
        }

        #Post player on DDBB
        sns_client.publish(
            TargetArn=sns_arn,
            Message=json.dumps({'default': json.dumps(response)}),
            MessageStructure='json'
        )

        return json.dumps(response)

    except Exception as e:
        raise HTTPError(500, "Internal Error: %s" % e)