import json
import logging
import os
import time
import uuid
import boto3

from lambdas.post_player.post_player_controller import (
    post_player,
)


def h_post_player(event, context):

    response = {
        "headers": {"Access-Control-Allow-Origin": "*"},
        "statusCode": 200,
        "body": None,
    }

    try:
        headers = event["headers"] if "headers" in event else None

        data = event["body"] if "body" in event else None
        data = event["body"] if "body" in event else None

        for sqs_record in event["Records"]:
            data = json.loads(sqs_record["body"])
        
        data = json.loads(data) if data else None

        result = post_player(data)

        response.update({"body": json.dumps(result)})

    except Exception as e:
        print("> Error: %s" % e)
        response.update({"statusCode": 500, "body": "Internal Error: %s" % e})

    return response