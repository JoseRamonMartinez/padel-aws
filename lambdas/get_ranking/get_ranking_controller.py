import json
import boto3
import os
from datetime import datetime, timedelta
from boto3.dynamodb.conditions import Key
from tools.http_error import HTTPError
from tools.decimalencoder import DecimalEncoder

aws_region = os.environ.get('AWS_REGION')
players_table = os.environ['PLAYERS_TABLE']

dynamodb = boto3.resource('dynamodb', region_name=aws_region)

dybamodb_players_table = dynamodb.Table(players_table)


def get_ranking(data):
    try:
        response = dybamodb_players_table.scan()
        return response["Items"]
    except Exception as e:
        raise HTTPError(500, 'Internal Error: %s' % e)