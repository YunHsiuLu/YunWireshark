dur_b=$1
dur_a=$2
files=$((dur_a / dur_b))
echo "round: $dur_b s, stop: $dur_a s, files: $files"

rm -rf data_test/*
echo ""
source runtshark.sh $dur_b $dur_a &> tshark_output.out &
#source countfiles.sh $dur_b $files &
python3 CapRead.py $files