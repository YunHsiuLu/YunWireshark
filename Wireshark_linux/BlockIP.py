import csv
import os
import sys
from telnetlib import Telnet

def check_ip(dic, ip):
    for i in list(dic.keys()):
        if i == ip:
            return True
        else:
            return False

def blockIP():
    filename = sys.argv[1]
    
    packets_list =[]
    path = 'data_testcsv/' + filename
    with open(path, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            packets_list.append(row)
    
    ip = {}
    for i in range(len(packets_list)):
        if i == 0:
            continue
        #print (packets_list[i][3])
        if packets_list[i][3] != "140.168.0.3":
            if check_ip(ip, packets_list[i][3]):
                ip[packets_list[i][3]] += 1
            else:
                ip[packets_list[i][3]] = 1
    
    block_ip = ""
    # how to block ip below


    # block in router
    tn=Telnet("140.168.0.1")
    tn.read_until(b"Username")
    tn.write("root".encode('ascii')+b"\r\n")
    tn.read_until(b"Password:")
    tn.write("123456".encode('ascii')+b"\r\n")
    tn.write("conf t".encode('ascii')+b"\r\n")
    tn.write("access-list 10 deny ".encode('ascii'))
    
    # for loop ip block
    tn.write(block_ip.encode('ascii')+b"\r\n")

    tn.write("access-list 10 permit any".encode('ascii')+b"\r\n")
    tn.write("interface f0/0".encode('ascii')+b"\r\n")
    tn.write("ip access-group 10 in".encode('ascii')+b"\r\n")
    tn.write("exit".encode('ascii')+b"\r\n")
    tn.write("exit".encode('ascii')+b"\r\n")
    tn.write("exit".encode('ascii')+b"\r\n")
    tn.read_all()

def unblockIP():
    print("hello")


#blockIP()
print(sys.argv[1])
