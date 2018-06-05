# LDAS_for_SME
Learning Data Analysis System for Server Management Exervise

# Description
LDAS_for_SMEでは, 授業の基礎演習環境にインストールする事を前提にしている. 
このシステムでは, 3つのログを収集している.  

## コマンド実行履歴
学生が入力したコマンドのログ情報を収集している.

## ファイル編集履歴
学生が編集したファイルの情報を収集している.

### サーバ状況確認履歴
サーバ演習課題に応じた



# 全体のディレクトリ構成

LDAS/  
　 ├─ students/  
　 └─ teacher/  

teacher/  




# セットアップ方法



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



## 教員用
- サーバ状況確認履歴
- DB