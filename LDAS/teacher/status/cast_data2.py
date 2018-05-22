#!/usr/bin/env python
# coding:utf-8

import pymongo
import sys
import commands

#dbの設定
host = "150.89.223.120"
port = 27017
db_name = 'db'
collection = 'status'

#ユーザ/パスワード
user = 'Read and write User'
pwd = 'write'

#サーバ状況確認コマンド
server_status_commands = ["service httpd status"]

#ssh関数 引数ipアドレスを変更


#DBへの接続
client = pymongo.MongoClient(host, port)
client[db_name].authenticate(user, pwd)
col = client[db_name][collection]

# for i in range(71, 91):

for s in server_status_commands:
    #収集するログ情報
	id = "status92"
	date = commands.getoutput("date")
	dir = ""
	cmd = s
	res = commands.getoutput("ssh root@150.89.223.92 " + s)
	flag = 0
	cnt = 0
	print date
	print dir
	print cmd
	print res
	col.update_many({'id': id, 'date': date, 'dir': dir, 'cmd': cmd, 'res': res}, {
	'$setOnInsert': {'id': id, 'date': date, 'dir': dir, 'cmd': cmd, 'res': res}}, upsert=True)