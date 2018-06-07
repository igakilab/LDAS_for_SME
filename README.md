# LDAS_for_SME
Learning Data Analysis System for Server Management Exervise

# Description
LDAS_for_SMEでは, 授業の基礎演習環境にインストールする事を前提にしている. 
このシステムでは, 3つのログを収集している.  



## コマンド実行履歴
学生が入力したコマンドのログ情報を収集している.
.bash_profileにscriptコマンドを追記しておく

## ファイル編集履歴
学生が編集したファイルの情報を収集している.

### サーバ状況確認履歴
サーバ演習課題に応じたshellscriptを実行して，実行結果をデータベースに保存している．

# 全体のディレクトリ構成

LDAS/  
　 ├─ students/ //学生用  
　 └─ teacher/ //教員用 

students/  
　 ├─ cmd/ //コマンド実行履歴  
　 |　 　 ├─ cast_data3.py //コマンド実行履歴収集プログラム  
　 |　 　 └─ log/ //scriptコマンドで収集したログファイルを保存    
　 └─ file/ //ファイル編集履歴  
　 　 　 ├─ file.sh //ファイル編集履歴収集プログラム  
        └─ file(ipアドレス下2桁)/ プログラムにより収集したgitのログ   

teacher/  
   ├─ status/ //サーバ状況確認履歴  
   |　 　 └─ cast_data3.py //サーバ状況確認履歴収集プログラムファイルを保存  
   ├─ db/  
   └─ web/  


## 想定している環境
- CentOS 6.7  
- script 
- cron


## インストールが必要なソフト(Know-how.mdで解説)
- python 2.6.6 -> python2.7.13に変更が必要と判明
- pip 7.1.0 -> pip 8.1.2に変更が必要と判明
- pymongo 3.6.1
- pyinotify 0.9.6
- GitPython 2.1.10
- rsync 3.0.6  
- lsyncd 2.1.4
- Apache 2.2.15
- Tomcat 7.0.85å

# セットアップ方法

Githubのリポジトリからクローン
その中にあるsetup.shを実行する．

授業で利用するマシンのipアドレスを把握する

    $ ifconfig

学生演習用サーバに対して，LDASディレクトリ以下のstudentsディレクトリのみを送る

下記コマンドを実行する

    $ ./setup.sh



# 学生用


    $ scp   

### コマンド実行履歴
### Installation

    $ student/init.sh

### cron登録方法

    $ crontab -e  

crontabを以下の用に編集する.   

    */5 * * * * /bin/LSS/students/ctrl.sh
    */5 13-17 * * 1 /bin/LSS/students/ctrl.sh

crontabファイルを読み込む

    $ crontab -u root /etc/crontab 


### ファイル編集履歴


# 教員用
- サーバ状況確認履歴
- DB
