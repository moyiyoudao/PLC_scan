"""
Usage:
    scan <scan_ip>
    scan -p <scan_ip>
    ip_show  Show the tool ip information
    ip_set   Set the tool IP
    read_results   read scans results
    file_transfer   transfer result files
Options:

Example:
    scan 192.168.100.100-120         scan ip 192.168.100.100 - 192.168.100.120
    scan -p 192.168.100.100-120        scan ip 192.168.100.100 - 192.168.100.120 opened ports
"""
from socket import *
from time import sleep
import sys
import os
import optparse
from docopt import docopt
def main():
    HOST = sys.argv[1]
    PORT = 21567
    buff_size =65500
    ADDR = (HOST,PORT)

    tcp_cli_sock = socket(AF_INET,SOCK_STREAM)
    tcp_cli_sock.connect(ADDR)

    while True:
        data = input('> ')
        if not data:
            break

        else:
            tcp_cli_sock.send(bytes(data, 'utf-8'))
            if data =='file_transfer':
                data = tcp_cli_sock.recv(buff_size)
                try:
                    with open('out.xml','w') as fs:
                        fs.write(data.decode('utf-8'))
                except IOError as erro:
                    print('File error'+str(erro))
                sleep(1)
                data = tcp_cli_sock.recv(buff_size)
                try:
                    with open('HostInfo.xml','w') as fs:
                        fs.write(data.decode('utf-8'))
                except IOError as erro:
                    print('File error'+str(erro))

            else:
                data = tcp_cli_sock.recv(buff_size)
                if not data:
                    break
                print(data.decode('utf-8'))
    tcp_cli_sock.close()
if __name__ == '__main__':
    args = docopt(__doc__)
    print(__doc__)

    main()