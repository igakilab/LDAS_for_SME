#!/usr/bin/env python 
# coding:utf-8

import pymongo
import sys
import re

#DB情報
host = host_ipaddress
port = port_num
db = 'db'
user = 'Read and write User'
pwd = 'write'

#コマンド実行履歴用ディレクトリ
path = '/bin/LSS/students/cmd'

client = pymongo.MongoClient(host, port)
client[db].authenticate(user, pwd)
col = client[db]['cmds']

#学生IDの設定を行う.
#仮想マシンごとに異なるidを設定する必要がある
args=sys.argv

#コマンドライン引数のエラー処理
if len(args) == 1 : 
    print "指定された引数は0です。"
    print "実行するにはipアドレスの末尾の引数が必要です。"
    quit()

id="cmd"+args[1]
date=""
dir=""
cmd=""
res=[]
flag=0
cnt=0

#ログファイルのデータを成形するために必要な正規表現の変数 pat
#r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}' で年月日と時刻を取得
pat = [r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}']

#ログファイルのカラーコード削除用の正規表現の変数 pat2
pat2 = [r'\x1b', r'\[0m', r'\[[\d{1,2};\d{1,2};\d{1,2}]*m']
 
file = open( path + '/log/data.log', 'r') 
string = file.readline() 
while string:
	mat = re.search(pat[0], string)
	if mat:
		#print date
                #print dir
                #print cmd
                #print res
		col.update_many({'id': id, 'date': date, 'dir': dir, 'cmd': cmd, 'res': res },{'$setOnInsert':{'id': id, 'date': date, 'dir': dir, 'cmd': cmd, 'res': res }},upsert=True)
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
