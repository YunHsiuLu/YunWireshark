import pyshark
import time, os, sys
import pprint
import BlockIP


# only for testing
# if you do "source run.sh 1 <stop time>"
# you can igore below
index, test_flag = 1, False
if len(sys.argv) > 1:
	index, test_flag = int(sys.argv[1]), True


# store the TCP/UDP packets
def network_conversation(packet):
  try:
    protocol = packet.transport_layer
    source_address = packet.ip.src
    #source_port = packet[packet.transport_layer].srcport
    destination_address = packet.ip.dst
    #destination_port = packet[packet.transport_layer].dstport
    pkt_length = packet.length
    #return (f'{protocol} {source_address}:{source_port} --> {destination_address}:{destination_port}')
    return [protocol, source_address, destination_address, pkt_length]
  except:
    pass

_dic = {}
blocked_ip_list = []
my_host = '140.168.0.3' 
path = 'data_test'
try:
	i = 0
	while True:
		# just for clearly read
		f1 = open('outputtxt/files-done%d.txt' % ((i+1)%(index+1)), 'w')
		f2 = open('outputtxt/conversations%d.txt'  % ((i+1)%(index+1)), 'w')
		if test_flag:
			time.sleep(1)
		filelist = os.listdir(path)
		filelist = sorted(filelist, key=lambda x: x[8:13])

		cap = pyshark.FileCapture(path+'/'+filelist[i])
		conversations = [] # only contain TCP/UDP packets
	# you can check the conversations type
	# you can also use "dir(<packet>)" to check options of packet

		for pkt in cap:
			conversations.append(network_conversation(pkt))
			if network_conversation(pkt) != None and network_conversation(pkt)[1] != my_host:
				_dic[network_conversation(pkt)[1]] = _dic.get(network_conversation(pkt)[1], 0) + 1
				if _dic[network_conversation(pkt)[1]] / (i+1) > 15 and network_conversation(pkt)[1] not in blocked_ip_list:		
					blocked_ip_list.append(network_conversation(pkt)[1])
					BlockIP.blockIP(network_conversation(pkt)[1], blocked_ip_list, 5)
		#if results != None:
	# i think conversations is the data we need
		print("Time:" + str(i+1), _dic)
		f1.write("files done: %d \tTCP/UDP capture size: %d\n" % (i+1, len(conversations)))
		f2.write("%s\n" % (str(conversations)))
		i += 1
	f1.close()
	f2.close()

	while True:
		if len(blocked_ip_list) == 0:
			sys.exit(0)
		else:
			print(len(blocked_ip_list))
			time.sleep(1)
except:
	pass

