for i in `seq 71 90` 
do
    #ssh root@150.89.223.$i /bin/LSS/students/init.sh
    #ssh root@150.89.223.$i /bin/LSS/students/ctrl.sh
    ssh root@150.89.223.$i crontab -r
    scp crontab root@150.89.223.$i:/etc/
    ssh root@150.89.223.$i crontab -u root /etc/crontab
    #ssh root@150.89.223.$i rm -rf /var/test
    #scp file.sh root@150.89.223.$i:/bin/LSS/students/file/
done
