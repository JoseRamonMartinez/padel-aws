import json
import boto3
import os
import time
from datetime import datetime, timedelta
from boto3.dynamodb.conditions import Key
from tools.http_error import HTTPError
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()
patch(['boto3'])

aws_region = os.environ.get('AWS_REGION')
players_table = os.environ['PLAYERS_TABLE']

dynamodb = boto3.resource('dynamodb', region_name=aws_region)

dybamodb_players_table = dynamodb.Table(players_table)

def post_player(data):
    try:
        player = {
            "name": data["name"],
            "position": int(data["position"]),
            "ttl": int(time.time() + (86400*31)),
            "data":data["data"]
        }
        # write the user to the database
        dybamodb_players_table.put_item(Item=player)

        response = {"Create": True}
        return response

    except Exception as e:
        raise HTTPError(500, "Internal Error: %s" % e)