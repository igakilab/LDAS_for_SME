# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

#------- コマンド実行履歴収取用設定 -------
#プロンプトの表示変更
PS1='[\D{%FT%T} \u@\h \w]\$ '

