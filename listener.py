'''
 listener.py : This is the SMS Receiver (MO); This listens for the request by aventura platform
 Author : Manula Waidyanatha <mwaidyanatha@gmail.com>
'''
import SocketServer
import re
from controller import Controller
from config import HOST_ADDR, HOST_PORT

class Listener(SocketServer.BaseRequestHandler):

    def handle(self):
        #self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        
        #Get the message in to an array. 
        msg_lines = self.data.split("\n")
        
        #Get the message content from array.
        sms = msg_lines[-1]
        
        input_vars = re.split(r'[=&]', sms)
        
        version = input_vars[input_vars.index('version') + 1]
        address = input_vars[input_vars.index('address') + 1]
        message = input_vars[input_vars.index('message') + 1]
        #correlator = input_vars[input_vars.index('correlator') + 1]

        #Send "Success" Message                
        output = '''HTTP/1.1 200 OK\nContent-type: text/xml\n\n<status_code>SBL-SMS-MT-2000</status_code><status_message>Success</status_message>'''
        self.request.send(output)
        self.finish()
        
        #Send the received message to controller
        Controller(version, address, message).start()        
        
        
if __name__ == "__main__":    
    # Create the server
    server = SocketServer.TCPServer((HOST_ADDR, HOST_PORT), Listener)
    print '###MO Listner####'
    print 'Receiver URL: http://'+HOST_ADDR+":"+str(HOST_PORT)
    
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
