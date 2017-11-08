# encoding:utf-8

import urllib, urllib2, sys
import ssl
import json
scene_id = 13473
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&' \
       'client_id=q7xymNXWnMQtAAV0hp9eY9zS' \
       '&client_secret=VhYRXUsMvxamZCad7g5Gq205vubwSDcr '
token=""
def auth():
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    res = response.read()
    if (res):
        connect = json.loads(res)
        return connect['access_token']

def chat(req):
    global token

    _url="https://aip.baidubce.com/rpc/2.0/solution/v1/unit_utterance?access_token="
    _url+=token

    post_data={"scene_id":scene_id,"query":req,"session_id":""}

    request = urllib2.Request(_url, json.dumps(post_data))
    request.add_header('Content-Type', 'application/json')
    try:
        response = urllib2.urlopen(request)
    except Exception as e:
        print e
    content = response.read()
    if (content):
        con=json.loads(content)
        print con['result']['session_id']
        print con['result']['qu_res']['raw_query']
        return con['result']['action_list'][0]['say']

#        for key in content:
#            print key,":",json.dumps(con[key], sort_keys=True, indent=4, separators=(',', ': '))

def run():
    global token
    token=auth()


run()
