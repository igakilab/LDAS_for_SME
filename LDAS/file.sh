#/bin/bash

#監視対象ディレクトリ
monitor_dir=("etc" "var" )

current_dir=`pwd`

# ログ収集ディレクトリ
log_dir=/bin/LSS/students/file

#ファイル編集履歴を保存するリモートリポジトリ名を記述 
#コマンドライン引数のエラー処理
if [ $# -ne 1 ]; then
  echo "指定された引数は$#です。" 1>&2
  echo "実行するにはipアドレスの末尾の引数が必要です。" 1>&2
  exit 1
fi

#ipアドレスとポート番号の設定必須
host=ip_address
port=port_num

repo_name=file$1
repo=ssh://file@$host:$port/file/$repo_name.git

# ディレクトリの有無を確認 なければ作成
if [ ! -d $log_dir ]; then
    mkdir -p $log_dir/log
fi

cd $log_dir

# Gitリポジトリの有無を確認 なければ作成
if [ ! -d ./$repo_name/.git ]; then
    git clone $repo >& /dev/null
fi

cd $repo_name

# 監視しているディレクトリの同期をとる
for d in ${monitor_dir[@]}; 
do
   rsync -av --exclude='var/log' /${d} . >& /dev/null
   rsync -av --exclude='var/log' --delete /${d} . >& /dev/null
done

# 変更された差分をコミットする
git add * >& /dev/null
git commit -m 'commit' >& /dev/null

#変更された差分をpushする
git pull >& /dev/null
git push >& /dev/null

cd "$current_dir"
