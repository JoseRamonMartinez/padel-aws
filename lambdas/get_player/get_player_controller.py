import json
import boto3
import os
from datetime import datetime, timedelta
from boto3.dynamodb.conditions import Key
from tools.http_error import HTTPError
from tools.decimalencoder import DecimalEncoder
from aws_xray_sdk.core import patch

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch

libraries = (['boto3'])
patch(libraries)


aws_region = os.environ.get('AWS_REGION')
players_table = os.environ['PLAYERS_TABLE']

dynamodb = boto3.resource('dynamodb', region_name=aws_region)

dybamodb_players_table = dynamodb.Table(players_table)


def get_player_by_name(data):
    try:
        # response = dybamodb_players_table.query(
        #     KeyConditionExpression=Key('name').eq(data["name"])
        # )
        # get response from dynamodb for player with name contains data["name"] using scan
        response = dybamodb_players_table.scan()
        response = [x for x in response["Items"] if data["name"] in x['name']]
        return response[0]
    except Exception as e:
        raise HTTPError(500, 'Internal Error: %s' % e)

def get_player_by_position(data):
    try:
        response = dybamodb_players_table.query(
            IndexName='PositionIndex',
            KeyConditionExpression=Key('position').eq(int(data["position"]))
        )
        return response["Items"]
    except Exception as e:
        raise HTTPError(500, 'Internal Error: %s' % e)