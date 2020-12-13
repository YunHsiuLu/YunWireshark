# step for running
==========================
First check you have pyshark, tshark package.  
pyshark => python3 -m pip install pyshark  
tshark  =>   
*   sudo apt-get update
*   sudo apt-get install tshark
==========================
To check the network interface, you need to install net-tools:  
*   sudo apt-get update
*   sudo apt-get install net-tools
Make sure you have the net-tools, then:  
# ifconfig
and correct the arguement in runtshark.sh:  
*   tshark -i {your interface} ......
==========================
Before running run.sh:  
if you are ubuntu user, correct the index in countfiles.sh:  
*   just below cd ../, add the line: c=$(($i - 1))
*   then change the next line index in arr => source pcap2csv.sh ${arr[$c]}
For running run.sh:
*   source run.sh [round time] [stop rime]  
==========================
**NOTE** for each run, files in data_test and date_testcsn will be removed.  