for (( i=0; i<60; i++ )){
	namedate=`(date +"%H:%M:%S")`
	wget -q -O $namedate.html http://www.wsj.com/mdc/public/page/2_3021-activnyse-actives.html
    ./hw9.py $namedate.html
 	sleep 1m   

}
