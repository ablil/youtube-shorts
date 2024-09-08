#!/usr/bin/env python3
from ytb import extract_info

def extract_query_param(event, param):
    query_params = event.get('queryStringParameters')
    if query_params and param in query_params:
        return query_params[param]
    return None

def lambda_handler(event, context):
    url = extract_query_param(event, 'url')
    if url:
        info = extract_info(url)
        return {
            'statusCode': 302,
            'headers': {
                'Location': info['url']
            }
        }

    return {
        "statusCode": 204
    }