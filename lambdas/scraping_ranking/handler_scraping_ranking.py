import json
import logging
import os
import time
import uuid
import boto3

from lambdas.scraping_ranking.scraping_ranking_controller import (
    scraping_ranking,
)


def h_scraping_ranking(event, context):

    response = {
        "headers": {"Access-Control-Allow-Origin": "*"},
        "statusCode": 200,
        "body": None,
    }

    try:
        headers = event["headers"] if "headers" in event else None

        #data = event["body"] if "body" in event else None
        data = event["body"] if "body" in event else None
        data = json.loads(data) if data else None
        #data = event["pathParameters"] if "pathParameters" in event else None


        result = scraping_ranking(data)

        response.update({"body": json.dumps(result)})

    except Exception as e:
        print("> Error: %s" % e)
        response.update({"statusCode": 500, "body": "Internal Error: %s" % e})

    return response