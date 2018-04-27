#!/usr/bin/env python 
# coding:utf-8

import pymongo
import sys
import re
import ConfigParser

#学生IDの設定を行う.
#仮想マシンごとに異なるidを設定する必要がある
#コマンドライン引数で指定する
args=sys.argv

#コマンドライン引数のエラー処理
if len(args) == 1 :
    print "指定された引数は0です。"
    print "実行するにはipアドレスの末尾の引数が必要です。"
    quit()

#コマンド実行履歴で記録するデータ変数
id="cmd"+args[1]
date=""
dir=""
cmd=""
res=[]

#コマンド実行履歴用ディレクトリ
path = '/bin/LSS/students/cmd'

#デバッグ用変数
flag=0
cnt=0

#正規表現
#ログファイル成形用変数 pat
#r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}' で年月日と時刻を取得
pat = [r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}']

#ログファイルのカラーコード削除用変数 pat2
pat2 = [r'\x1b', r'\[0m', r'\[[\d{1,2};\d{1,2};\d{1,2}]*m']

#DBに接続
def connect_db():
    #Config設定を読み込み
    config = ConfigParser.ConfigParser()
    config.read('config/setting.ini')
    #mongodbの情報
    host = config.get('mongodb', 'host')
    port = config.get('mongodb', 'port')
    user = config.get('mongopass', 'user')
    passwd = config.get('mongopass', 'passwd')
    #使用するdbの名前とコレクション
    db_name = config.get('mongodb', 'db_name')
    db_coll = config.get('mongodb', 'db_coll')
    
    #接続
    client = pymongo.MongoClient( host, port )
    client[db_name].authenticate(user, passwd)
    db = client[db_name]
    coll = db[db_coll]
    return coll 

#DBに保存
def save_db(coll):
    col.update_many(
            {'id': id, 'date': date, 'dir': dir, 'cmd': cmd, 'res': res },
            {'$setOnInsert':
                {'id': id, 'date': date, 'dir': dir, 'cmd': cmd, 'res': res }
            },upsert=True)

#ログファイル読み込み
def file_read():
    file = open( path + '/log/data.log', 'r') 
    string = file.readline() 

#デバッグ用関数
def debug():
    print id
    print date
    print dir
    print cmd
    print res

#コマンド実行履歴収集モジュール
def cmd_exe_his():
    connect_db()
    string = file_read()
    while string:
    	mat = re.search(pat[0], string)
	if mat:
            #debug()
            save_db()
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

#main
if __name__ == '__main__':
    cmd_exe_his()
