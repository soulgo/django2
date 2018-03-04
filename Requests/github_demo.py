#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
from requests import exceptions
URL = "https://api.github.com"

def build_url(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    #username
    response = requests.get(build_url('users/luojunquan'))
    #email
    # response = requests.get(build_url('user/emails'),auth=('用户名','密码'))
    print better_print(response.text)

def params_request():
    response = requests.get(build_url('users'),params={'since':11})
    print better_print(response.text)
    print '-------------->>>>'
    print response.request.headers
    print '-------------->>>>'
    print response.url

def timeout_request():
    try:
        response = requests.get(build_url('user/emails'),timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e:
        print e.message
    else:
        print response.text
        print response.status_code


if __name__ == "__main__":
    timeout_request()
