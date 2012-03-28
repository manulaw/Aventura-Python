'''
 sender.py : This is the SMS Sender (MT)
 Author : Manula Waidyanatha <mwaidyanatha@gmail.com>
'''

import socket
import base64
import urllib
from config import CLIENT_ADDR, CLIENT_PORT, USERNAME, PASSWORD, SERVICE_URI

   
def send(version, address, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((CLIENT_ADDR, CLIENT_PORT))
    
    
    auth = base64.b64encode(USERNAME + ':' + PASSWORD)    
    message = urllib.quote(message)
    content = '''version=''' + version + '''&address=tel:''' + address + '''&message=''' + message
    data = '''POST /''' + SERVICE_URI + ''' HTTP/1.1\nHost: localhost:5000\nAccept: */*\nProxy-Connection: Keep-Alive\nAuthorization: Basic ''' + auth + '''\nContent-length: ''' + str(len(content)) + '''\nContent-Type: application/x-www-form-urlencoded\n\n''' + content
    
    client_socket.send(data)
    client_socket.close()
        
        
