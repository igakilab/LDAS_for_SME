for i in `seq 74 80` 
do
    #ssh root@150.89.223.$i /bin/LSS/students/init.sh
    #ssh root@150.89.223.$i /bin/LSS/students/ctrl.sh
    #ssh root@150.89.223.$i crontab -r
    #scp crontab root@150.89.223.$i:/etc/
    #ssh root@150.89.223.$i crontab -u root /etc/crontab
    #ssh root@150.89.223.$i rm -rf /var/test
    #scp file.sh root@150.89.223.$i:/bin/LSS/students/file/

    #ssh root@150.89.223.$i yum -y install epel-release
    #ssh root@150.89.223.$i yum -y install lsyncd
    #ssh root@150.89.223.$i yum -y erase epel-release

    #scp lsyncd.conf root@150.89.223.$i:/etc/
    #scp file_edit_init.sh root@150.89.223.$i:/bin/LSS/students/file/
    #scp file.sh root@150.89.223.$i:/bin/LSS/students/file/
    #scp ctrl.sh root@150.89.223.$i:/bin/LSS/students/

    #ssh root@150.89.223.$i rm -rf ~/.ssh/known_hosts 

    #ssh root@150.89.223.$i cd /bin/LSS/students/file/ #&& git clone ssh://root@150.89.223.120:2020/root/file'$i'.git repo'
    #ssh root@150.89.223.$i 'cd repo && mkdir etc'
    #ssh root@150.89.223.$i 'cd repo && mkdir var'

    #ssh root@150.89.223.$i service lsyncd start
    #ssh root@150.89.223.$i chkconfig --add lsyncd
    #ssh root@150.89.223.$i chkconfig lsyncd on

    #ssh root@150.89.223.$i 'echo test >> /etc/a'
    #ssh root@150.89.223.$i 'echo test >> /var/a'
    #ssh root@150.89.223.$i 'rm -rf /etc/a'
    #ssh root@150.89.223.$i 'rm -rf /var/a'
    #ssh root@150.89.223.$i 'cd /bin/LSS/students/file/repo && git log' 

    #ssh root@150.89.223.$i rm -rf /bin/LSS/students/file/repo
    #ssh root@150.89.223.$i service lsyncd restart

    #ssh root@150.89.223.$i /bin/LSS/students/file/file.sh

done
