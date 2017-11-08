# encoding:utf-8

import itchat
from itchat.content import *
import smartchat

itchat.auto_login(hotReload=True)
#itchat.send("有人找你",'filehelper')
def printlist():
    sex = ['', '男', '女']
    users=itchat.get_friends()
    for user in users:
        print "微信名:",user['NickName']," 备注名：",user['RemarkName']," 性别",sex[user['Sex']]

@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=False,isMpChat=False)
def text_reply(msg):

#    for key in msg:
#        print key,":",msg[key]
    print msg['FromUserName']
    msg.user.send(smartchat.chat(msg['Text']))

itchat.run()
