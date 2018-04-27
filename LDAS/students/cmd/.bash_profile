# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin

export PATH

#------- コマンド実行履歴収取用設定 -------
#ログを記録するディレクトリのパス
log_dir='/bin/LSS/students/cmd'

#コマンド実行履歴のログを記録する
#cmdディレクトリを作成
if [ ! -d $log_dir ]; then
        mkdir -p $log_dir/log
fi

#ログイン時にscriptコマンドを実行
#取得した操作ログを/bin/LSS/cmd/log/以下に記録
script -fq $log_dir/log/data.log

