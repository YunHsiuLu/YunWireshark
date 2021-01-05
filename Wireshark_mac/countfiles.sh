sleep_sec=$(($1 + 2))

for i in $(seq 1 $2);
do
    sleep $1
    cd data_test
        arr=(*.pcap)
        echo "Files done: ${arr[$i]}"
    cd ../
    temp=`source pcap2csv.sh ${arr[$i]}`
    str=$(echo $temp | awk -F' ' '{print $1}')
    str2=$(echo $temp | awk -F' ' '{print $2}')
    num=$((str / $1))
    echo "$num , $str"
    if [ $num -ge 1000 ]; then
	echo "more than 1000!!!!!!!"
	python3 BlockIP.py $str2
    fi
done
