for i in `seq 1` 
do
    #ssh root@150.89.223.$i /bin/LSS/students/init.sh
    #ssh root@150.89.223.$i /bin/LSS/students/ctrl.sh
    ssh root@150.89.223.92 crontab -r
    scp  crontab root@150.89.223.92:/etc/
    ssh root@150.89.223.92 crontab -u root /etc/crontab
    scp file.sh root@150.89.223.92:/bin/LSS/students/file/
done
