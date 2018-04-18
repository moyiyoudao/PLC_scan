#-*- coding:utf-8 -*-
import sys
import os
import time
def main():
#while True:
	#Mitsubishi_cmd='nmap --script Mitsubishi_melsoft_tcp_p_5007.nse '+ sys.argv[1]+' -p 5007' #linux 构造shell/CMD命令
	Mitsubishi_cmd='nmap --unprivileged --script Mitsubishi_melsoft_tcp_p_5007.nse '+ sys.argv[1]+' -p 5007' #windows 构造shell/CMD命令
	#print Mitsubishi_cmd #python 2.7.6
	print(Mitsubishi_cmd) #python 3.x
	process = os.popen(Mitsubishi_cmd) #开辟进程执行shell/CMD命令,将结果输出到process中
	output = process.read() #读取shell/CMD命令的输出
	process.close() #关闭进程
	if '5007/tcp open' in output:
		process = os.popen(Mitsubishi_cmd+' -oX out.xml') #将扫描到的设备信息写到out.xml
		process.close()
	else:
		#Mitsubishi_cmd='nmap --script Mitsubishi_melsoft_udp_p_5006.nse '+ sys.argv[1]+' -p 5006' #linux
		Mitsubishi_cmd='nmap --unprivileged --script Mitsubishi_melsoft_udp_p_5006.nse '+ sys.argv[1]+' -p 5006' #windows 
		#print Mitsubishi_cmd #python 2.7.6
		print(Mitsubishi_cmd) #python 3.x
		process = os.popen(Mitsubishi_cmd)
		output = process.read()
		process.close()
		if '5006/udp open' in output:
			process = os.popen(Mitsubishi_cmd+' -oX out.xml')
			process.close()
		else:
			#Siemense_cmd='nmap --script s7.nse '+ sys.argv[1]+' -p 102' #linux
			Siemense_cmd='nmap --unprivileged --script s7.nse '+ sys.argv[1]+' -p 102' #windows 
			#print Siemense_cmd #python 2.7.6
			print(Siemense_cmd) #python 3.x
			process = os.popen(Siemense_cmd)
			output = process.read()
			process.close()
			if '102/tcp open' in output:
				process = os.popen(Siemense_cmd+' -oX out.xml')
				process.close()
			else:
				#Modbus_cmd='nmap --script modbus-discover.nse '+ sys.argv[1]+' -p 502' #linux
				Modbus_cmd='nmap --unprivileged --script modbus-discover.nse '+ sys.argv[1]+' -p 502' #windows
				#print Modbus_cmd #python 2.7.6
				print(Modbus_cmd) #python 3.x
				process = os.popen(Modbus_cmd)
				output = process.read()
				process.close()
				if '502/tcp open' in output:
					process = os.popen(Modbus_cmd+' -oX out.xml')
					process.close()
				else:
					#rockwell_enip_cmd='nmap --script rockwell_enip.nse '+ sys.argv[1]+' -p 44818' 
					rockwell_enip_cmd='nmap --unprivileged --script rockwell_enip.nse '+ sys.argv[1]+' -p 44818' #windows
					#print rockwell_enip_cmd #python 2.7.6
					print(rockwell_enip_cmd) #python 3.x
					process = os.popen(rockwell_enip_cmd)
					process.close()
					if '44818/tcp open' in output and 'Yokogawa' not in output:
						process = os.popen(rockwell_enip_cmd+' -oX out.xml')
						output = process.read()
						process.close()
					else:
						#yokogawa_enip_cmd='nmap --script yokogawa_enip.nse '+ sys.argv[1]+' -p 44818' #linux
						yokogawa_enip_cmd='nmap --unprivileged --script yokogawa_enip.nse '+ sys.argv[1]+' -p 44818' #windows
						#print yokogawa_enip_cmd #python 2.7.6
						print(yokogawa_enip_cmd) #python 3.x
						process = os.popen(yokogawa_enip_cmd)
						output = process.read()
						process.close()
						if '44818/tcp open' in output:
							process = os.popen(yokogawa_enip_cmd+' -oX out.xml')
							process.close()

	cmd = 'nmap -O -sS -sU -F ' + sys.argv[1] + ' -oX ItInfo.xml'  # windows 构造shell/CMD命令
	print(cmd)  # python 3.x
	process = os.popen(cmd)  # 开辟进程执行shell/CMD命令,将结果输出到process中
	output = process.read()  # 读取shell/CMD命令的输出
	process.close()  # 关闭进程
if __name__ == '__main__':
    main()
'''
如果后期需要添加其他协议识别，在该程序结尾添加以下语句（注意python中的缩进格式）
else:
	cmd='nmap --script yokogawa_enip.nse '+ sys.argv[1]+' -p 44818'#yokogawa_enip.nse这个脚本名称改为新协议脚本名称，-p 44818中的44818改为新协议的端口号
	print cmd #不改
	process = os.popen(cmd) #不改
	output = process.read() #不改
	process.close() #不改
	if '44818/tcp open' in output: #其中44818改为新协议端口号
		process = os.popen(cmd+' -oX out.xml') #不改
		process.close() #不改
'''