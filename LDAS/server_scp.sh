for i in `seq 92` 
do
    #ssh root@150.89.223.$i /bin/LSS/students/init.sh
    #ssh root@150.89.223.$i /bin/LSS/students/ctrl.sh
    ssh root@150.89.223.$i crontab -r
    scp root root@150.89.223.$i:/var/spool/root 
    scp file.sh root@150.89.223.$i:/bin/LSS/students/file/
done
