import pyshark
import time, os, sys
import pprint


# only for testing
# if you do "source run.sh 1 <stop time>"
# you can igore below
index, test_flag = 1, False
if len(sys.argv) > 1:
	index, test_flag = int(sys.argv[1]), True

# just for clearly read
f1 = open('outputtxt/files-done.txt', 'w')
f2 = open('outputtxt/conversations.txt', 'w')

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
  except AttributeError as e:
    pass

path = 'data_test'
for i in range(index):
	if test_flag:
		time.sleep(1)
	filelist = os.listdir(path)
	filelist = sorted(filelist, key=lambda x: x[8:13])

	cap = pyshark.FileCapture(path+'/'+filelist[i])
	conversations = [] # only contain TCP/UDP packets
	# you can check the conversations type
	# you can also use "dir(<packet>)" to check options of packet

	for pkt in cap:
		results = network_conversation(pkt)
		if results != None:
			conversations.append(results)
	# i think conversations is the data we need

	f1.write("files done: %d \tTCP/UDP capture size: %d\n" % (i+1, len(conversations)))
	f2.write("%s\n" % (str(conversations)))
f1.close()
f2.close()

