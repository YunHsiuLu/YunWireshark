sleep_sec=$(($1 + 2))

for i in $(seq 1 $2);
do
    sleep $1
    cd data_test
        arr=(*.pcap)
        echo "Files done: ${arr[$i]}"
    cd ../
    c=$(($i-1))
    temp=`source pcap2csv.sh ${arr[$c]}`
    python3 BlockIP.py $temp
done
