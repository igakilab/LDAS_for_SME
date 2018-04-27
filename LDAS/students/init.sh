#!/bin/bash

#コマンド実行履歴とファイル編集履歴の記録先
cmd_path='/bin/LSS/students/cmd'
file_path='/bin/LSS/students/file'

#学生を特定するためのIDを設定
#今回はIDをipアドレスの末尾の値とする
#コマンドライン引数を使ってipアドレスを設定
#id

#コマンド実行履歴収集用のプロンプト変更
cp -f $cmd_path/.bash_profile ~/
cp -f $cmd_path/.bashrc ~/

#コマンド実行履歴収集用コマンドのインストール
yum -y install python-setuptools
easy_install pymongo

#ファイル編集履歴収集用コマンドのインストール
yum -y install rsync
yum -y install git

#ファイル編集履歴収集用スクリプトの実行
#$file_path/file.sh $id

#コマンド実行履歴収集用スクリプトの実行
#$cmd_path/cast_data3.py $id
