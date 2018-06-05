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
- rsync 3.0.6
- cron


## インストールが必要なソフト
- python 2.6.6
- pip 7.1.0
- lsyncd 2.1.4
- inotify
- Apache 2.2.15
- tomcat 7.0.85

## インストールコマンド一覧

Python

    $ yum -y install python  

pip

    $ yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm $ 

lsyncd

    $ lsyncd --version  

rsync

    $ rsync --version  

cron

    $ whereis -b crontab | cut -d' ' -f2 | xargs rpm -qf  

inotify

    $   

Apache

    $ httpd -v

Tomcat

    $ tomcat version



## バージョン確認コマンド一覧

CentOS  

    $ cat /etc/redhat-release  

Python

    $ python -V  

pip

    $ pip -V  

lsyncd

    $ lsyncd --version  

rsync

    $ rsync --version  

cron

    $ whereis -b crontab | cut -d' ' -f2 | xargs rpm -qf  

inotify

    $   

Apache

    $ httpd -v

Tomcat

    $ tomcat version



# セットアップ方法

Githubのリポジトリからクローン
その中にあるsetup.shを実行する．

授業で利用するマシンのipアドレスを把握する

    $ ifconfig

学生演習用サーバに対して，LDASディレクトリ以下のstudentsディレクトリのみを送る

下記コマンドを実行する

    $ ./setup.sh



## 学生用

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


### gitコマンド
### よく使うコマンド
Initialize commit

    $ git init
    $ git add .
    $ git commit -m "コメント"

Clone command

    $ git clone git@


Add commit

    $ git add .
    $ git commit -m "コメント"

Delete commit

    $ git rm $(git ls-files --deleted)
    $ git commit -m "コメント"

Show log

    $ git log

Status git

    $ git status

Diff git

    $ git diff



### lsyncd
### インストール方法

    $ yum -y install lsyncd

### 設定ファイルの編集

    $ cp -p /usr/share/doc/lsyncd-2.1.4/examples/lrsync.lua /etc/lsyncd.conf
    $ vi /etc/lsyncd.conf
    $ vi /etc/rsyncd.conf

### python
### インストール方法

    $ yum -y install python

pythonのバージョン確認コマンド

    $ python -V

上記コマンドを実行して，pythonのバージョンが表示されたらインストール完了．

### pip
### インストール方法

pyinotifyをインストールするためには，pipが必要になる．
しかし，大学の環境ではpipはインストールされていない．
そこで，pipをインストールする


一番簡単な方法

    $ 





### lsyncdのデーモン登録

    $ chkconfig --add lsyncd


## 教員用
- サーバ状況確認履歴
- DB
