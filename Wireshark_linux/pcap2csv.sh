filename=$1
str="test${filename:8:5}.csv"
tshark -r "data_test"/$filename -T fields -e frame.number -e eth.src -e eth.dst -e ip.src -e ip.dst -e frame.len -E header=y -E separator=, > "data_testcsv"/$str
echo "`python3 CsvRealtimeRead.py $str`"

