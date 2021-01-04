sleep_sec=$(($1 + 2))

for i in $(seq 1 $2);
do
    sleep $1
    cd data_test
        arr=(*.pcap)
        echo "Files done: ${arr[$i]}"
    cd ../
    temp=`source pcap2csv.sh ${arr[$i]}`
    num=$((temp / $1))
    if [ $num -ge 10000 ]; then
    	echo "test success!!!!"
    	echo "test success!!!!"
    	echo "test success!!!!"
    	echo "test success!!!!"
    	echo "test success!!!!"
    	echo "test success!!!!"
    	echo "test success!!!!"
    	echo "test success!!!!"
    	echo "test success!!!!"
    	echo "test success!!!!"
    fi
done
