dur_b=$1
cycle=$2
echo "round: $dur_b s, stop: $dur_a s, files: $files"

rm -rf data_test/*
echo ""
source runtshark.sh $dur_b $cycle &> tshark_output.out &
#source countfiles.sh $dur_b $files &
python3 CapRead.py $cycle