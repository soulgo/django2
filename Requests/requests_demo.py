#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET = 'http://127.0.0.1:8000/get'
def use_simple_requests():
    response = requests.get(URL_IP)
    print '>>>>>>Response Headders'
    print response.headers
    print '>>>>>>Response Body'
    # print ''.join([line for line in response.readlines()])
    print response.text


def use_parms_requests():
    parms = {'param1':'hello','param2':'world'}
    print 'Request Params'
    print parms
    response = requests.get(URL_IP,params=parms)
    print '>>>>>>Status Code'
    print response.status_code
    print response.reason
    print '>>>>>>Response Body'
    print response.json()



if __name__ == '__main__':
    print '>>>Use simple requests'
    use_simple_requests()
    print '>>>Use Params requests'
    use_parms_requests()