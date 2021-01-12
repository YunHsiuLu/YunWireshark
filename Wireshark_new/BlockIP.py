import csv
import os
import sys
import time
import threading
from telnetlib import Telnet

def check_ip(dic, ip):
    for i in list(dic.keys()):
        if i == ip:
            return True
        else:
            return False

def blockIP(block_ip, blocked_ip_list, punishment_time):
    try:
    	print(block_ip + " has been blocked")
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
    
    	t=threading.Thread(target = unblock, args=(block_ip, blocked_ip_list, punishment_time,))
    	t.start()
    except:
    	pass
    
def unblock(block_ip, blocked_ip_list, punishment_time):
    try:
    	time.sleep(punishment_time)
    
    	tn = Telnet('140.168.0.1')
        tn.read_until(b'Username')
        tn.write('root'.encode('ascii')+b'\n')
        tn.read_until(b'Password')
        tn.write('123456'.encode('ascii')+b'\n')
        tn.write('show access-list 10'.encode('ascii')+b'\r\n')
        op = tn.read_until(block_ip.encode('ascii'))

        l = len(block_ip)

        for i in range(1, 10000):
            if str(op)[-(l+9+i)] == ' ':
                print(i - 1)
                break
        # for testing
        print(str(op)[-(l+9+i-1):-(l+9)])
        iplistnum = str(op)[-(l+9+i-1):-(l+9)]
        tn.write('conf t'.encode('ascii')+b'\n')
        tn.write('ip access-list standard 10'.encode('ascii')+b'\n')
        tn.write('no '.encode('ascii'))
        tn.write(iplistnum.encode('ascii')+b'\n')
        tn.write('exit'.encode('ascii')+b'\n')
        tn.write('exit'.encode('ascii')+b'\n')
        tn.write('exit'.encode('ascii')+b'\n')
        tn.read_all()
    
    	blocked_ip_list.remove(block_ip)
    	print(block_ip + " has been unblocked")
    except:
    	pass

def test():
    print("testing......")
    
