import json
import logging
import os
import time
import uuid
from tools.decimalencoder import DecimalEncoder
import boto3

from lambdas.get_ranking.get_ranking_controller import (
    get_ranking
)

def h_get_ranking(event, context):

    response = {
        "headers": {"Access-Control-Allow-Origin": "*"},
        "statusCode": 200,
        "body": None,
    }

    try:
        headers = event["headers"] if "headers" in event else None

        data = event["pathParameters"] if "pathParameters" in event else None

        result = get_ranking(data)

        response.update({"body": json.dumps(result, cls=DecimalEncoder)})

    except Exception as e:
        print("> Error: %s" % e)
        response.update({"statusCode": 500, "body": "Internal Error: %s" % e})

    return response