#!/usr/bin/env python
# coding:utf-8

import pymongo
import sys
import commands

#dbの設定
# host = 'ip_address'
# port = 'port_num'
# db_name = 'db'
# collection = 'status'

#ユーザ/パスワード
# user = 'Read and write User'
# pwd = 'write'

#サーバ状況確認コマンド
server_status_commands = ["service httpd status","","",""]

#DBへの接続
client = pymongo.MongoClient(host, port)
client[db].authenticate(user, pwd)
col = client[db_name][collection]

#収集するログ情報
id = "status"
date = commands.getoutput("date")
dir = ""
cmd = commands.getoutput("service httpd status")
res = []
flag = 0
cnt = 0

for i in range(71, 91):
    for s in server_status_commands:
		#print date
                #print dir
                #print cmd
                #print res
col.update_many({'id': id, 'date': date, 'dir': dir, 'cmd': cmd, 'res': res}, {
                '$setOnInsert': {'id': id, 'date': date, 'dir': dir, 'cmd': cmd, 'res': res}}, upsert=True)
                res = []
		s_split = string.split(" ", 3)
               	date = mat.group()
               	dir = s_split[2]
               	cmd = s_split[3]
		mat2 = re.search(r'vi ', cmd)
		if mat2:
			flag = 1
		else:
			flag = 0
	else:
		for p in pat2:
			string = re.sub(p, '', string)	
		if not flag:
			res.append(string)
	string = file.readline()
