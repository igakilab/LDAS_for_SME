ip=`hostname -I`
ip=${ip:11:2}
repository=ssh://root@150.89.223.120:2020/root/file$ip.git

rm -rf /root/.ssh/known_hosts
cd /bin/LSS/students/file/ && git clone repository repo 
cd repo && mkdir etc && mkdir var

service lsyncd start
chkconfig --add lsyncd
chkconfig lsyncd on

echo test >> /etc/a
echo test >> /var/a
rm -rf /etc/a
rm -rf /var/a
cd /bin/LSS/students/file/repo && git log -u 
