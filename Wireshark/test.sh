echo "------script start-------"

sleep 1
s="`python3 test.py`"
if [ $s = "hello" ]; then
	echo "success return python's string"
fi