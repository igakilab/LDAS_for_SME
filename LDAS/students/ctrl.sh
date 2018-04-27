#!/bin/bash

#コマンド実行履歴とファイル編集履歴の記録先
cmd_path='/bin/LSS/students/cmd'
file_path='/bin/LSS/students/file'

#学生を特定するためのIDを設定
#今回はIDをipアドレスの末尾の値とする
id=ip_address

#ファイル編集履歴収集用スクリプトの実行
$file_path/file.sh $id

#コマンド実行履歴収集用スクリプトの実行
$cmd_path/cast_data3.py $id
