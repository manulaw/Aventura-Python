'''
 controller.py : Message processor; When listener receives a message, it invokes Controller.
 Author : Manula Waidyanatha <mwaidyanatha@gmail.com>
'''

import threading
from sender import send


class Controller(threading.Thread):
    
    version = ''
    address = ''
    message = ''
    
    def __init__(self, version, address, message):
        threading.Thread.__init__(self)
        self.version = version
        self.address = address
        self.message = message
        
    def run(self):               
        #Logging the phone number(Address) and the message
        log = open("log.txt", "a")
        log.write(self.address + " " + self.message + "\n")
        log.close()
        
	#Send SMS
        send(self.version, self.address, "Hello")
