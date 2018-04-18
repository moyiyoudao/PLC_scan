from socket import *
from time import ctime,sleep

import os

HOST = ''
PORT = 21567
buff_size = 65500
ADDR = (HOST, PORT)
tcp_sock = socket(AF_INET, SOCK_STREAM)
tcp_sock.bind(ADDR)
tcp_sock.listen(5)
while True:
    print('Waiting for connection...')
    tcp_clisock,addr_cli =tcp_sock.accept()
    print('Connect from', addr_cli)
    while True:
        data = tcp_clisock.recv(buff_size)
        if not data:
            break
        print(data)
        data = str(data, encoding = "utf-8")
        if data == 'read_results':
            process = os.popen('python parse_xml.py')
            out = process.read()
            process.close()
            #print(out)
            tcp_clisock.send(bytes(out, 'utf-8'))
        elif data == 'ip_show':
            process = os.popen('ipconfig /all')
            out = process.read()
            process.close()
            #print(out)
            tcp_clisock.send(bytes(out, 'utf-8'))
        elif data.split(" ")[0] =='ip_set':
            process = os.popen('netsh interface ip set address name="本地连接" source= static addr = '+data.split(" ")[1])
            out = process.read()
            process.close()
            tcp_clisock.send(bytes('\n[%s] %s' % (ctime(), data), 'utf-8'))
        elif data.split(" ")[0] == 'scan' and (data.split(" ")[1] == '-p') :
            process = os.popen('nmap -sS ' + data.split(" ")[2])
            out = process.read()
            process.close()
            # print(out)
            tcp_clisock.send(bytes(out, 'utf-8'))
        elif  data.split(" ")[0] == 'scan' and data.split(" ")[1] != '-p':
            data ='python plc_scan.py '+data.split(" ")[1]
            os.system(data)
            tcp_clisock.send(bytes('\n[%s] %s' % (ctime(), data), 'utf-8'))

        elif data =='file_transfer':
            process = os.popen("more out.xml")
            out = process.read()
            process.close()
            #print(out)
            tcp_clisock.send(bytes(out, 'utf-8'))
            sleep(3)

            process = os.popen("more ItInfo.xml")
            out = process.read()
            process.close()
            #print(out)
            tcp_clisock.send(bytes(out, 'utf-8')) 
            

        else:
            print('resume load ')
            tcp_clisock.send(bytes('resume load ', 'utf-8'))





    tcp_clisock.close()
tcp_sock.close()