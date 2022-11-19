"""Main module."""
from typing import Dict
from warrant.aws_srp import AWSSRP
import boto3

USERNAME='joey'
PASSWORD='Password123.'
POOL_ID='us-east-1_XHw9hobXn'
CLIENT_ID = '3jjg56h79h3lrje33r7g406iuo'

def auth_user(username: str, password: str, pool_id: str, client_id: str) -> Dict:
    aws = AWSSRP(username=username, password=password, pool_id=pool_id, client_id=client_id)
    tokens = aws.authenticate_user()
    return tokens

def get_access_token(username: str, password: str, pool_id: str, client_id: str) -> str:
    tokens = auth_user(username, password, pool_id, client_id)
    id_token = tokens['AuthenticationResult']['IdToken']
    refresh_token = tokens['AuthenticationResult']['RefreshToken']
    access_token = tokens['AuthenticationResult']['AccessToken']
    token_type = tokens['AuthenticationResult']['TokenType']
    return access_token

def get_user_info(access_token: str) -> Dict:
    client = boto3.client('cognito-idp')
    return client.get_user(AccessToken=access_token)
