"""Main module."""
from typing import Dict, Optional
from warrant.aws_srp import AWSSRP
import boto3


def auth_user(username: str, password: str, pool_id: str, client_id: str, pool_region: Optional[str]=None) -> Dict:
    aws = AWSSRP(username=username, password=password, pool_id=pool_id, client_id=client_id, pool_region=pool_region)
    tokens = aws.authenticate_user()
    return tokens

def get_access_token(username: str, password: str, pool_id: str, client_id: str, pool_region: Optional[str]=None) -> str:
    tokens = auth_user(username, password, pool_id, client_id, pool_region)
    id_token = tokens['AuthenticationResult']['IdToken']
    refresh_token = tokens['AuthenticationResult']['RefreshToken']
    access_token = tokens['AuthenticationResult']['AccessToken']
    token_type = tokens['AuthenticationResult']['TokenType']
    return access_token

def get_user_info(access_token: str) -> Dict:
    client = boto3.client('cognito-idp')
    return client.get_user(AccessToken=access_token)
