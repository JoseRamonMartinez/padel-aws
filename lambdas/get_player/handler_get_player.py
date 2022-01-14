import json
import logging
import os
import time
import uuid
import boto3

from lambdas.get_player.get_player_controller import (
    get_player_by_name,get_player_by_position
)

def h_get_player_by_name(event, context):

    response = {
        "headers": {"Access-Control-Allow-Origin": "*"},
        "statusCode": 200,
        "body": None,
    }

    try:
        headers = event["headers"] if "headers" in event else None

        data = event["pathParameters"] if "pathParameters" in event else None

        result = get_player(data)

        response.update({"body": json.dumps(result)})

    except Exception as e:
        print("> Error: %s" % e)
        response.update({"statusCode": 500, "body": "Internal Error: %s" % e})

    return response

def h_get_player_by_position(event, context):

    response = {
        "headers": {"Access-Control-Allow-Origin": "*"},
        "statusCode": 200,
        "body": None,
    }

    try:
        headers = event["headers"] if "headers" in event else None

        data = event["pathParameters"] if "pathParameters" in event else None

        result = get_player(data)

        response.update({"body": json.dumps(result)})

    except Exception as e:
        print("> Error: %s" % e)
        response.update({"statusCode": 500, "body": "Internal Error: %s" % e})

    return response