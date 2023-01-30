# Mqtt Client for Alarm GSM Menager

from threading import Thread, Lock
from queue import Queue
from time import sleep          # this lets us have a time delay
import paho.mqtt.client as mqtt
import subprocess as ioControl
import json 

class MqttClient():

    def __init__(self, name, server, port, login, passw):
        self.name = name
        self.server = server
        self.port = port
        self.login = login
        self.passw = passw
        self.client = mqtt.Client(name) 
        self.client.username_pw_set(username=self.login, password=self.passw) 
        self.client.will_set(topic=f'{self.name}/status', payload="Offline")
        self.client.on_connect = self.onConnect
        self.client.on_disconnect = self.onDisconnect
        self.client.on_messagedisconnect = self.onMessage
        
        print(f'Init client param:'
            f'\nName: \t {self.name}'
            f'\nServer: \t {self.server}'
            f'\nPort: \t {self.port}'
            f'\nLogin: \t {self.login}'
            f'\nPassw: \t {self.passw}')

    def onConnect(self, userdata, flags, rc):
        # print(f'Mqtt Connected with result code {str(rc)}')
        self.client.publish(f'{self.name}/status','Online')
        
    def onDisconnect(self, userdata, rc = 0):
        print(f'DisConnected result code {str(rc)}')
     
    # The callback for when a PUBLISH message is received from the server.
    def onMessage(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))   
        
    def process(self):    
        couter = 0
        
        result = self.client.connect(self.server, self.port, 15)
        print(f'Connect in process result = {result}')
        
        while(True):
            sleep(5)
            print(f'Counter loop {couter}')
            couter += 1
            
            
    def startProcess(self):
        # ThrClient = Thread(target=self.process, args=(client,))
        Thread(target=self.process).start()
        
alrmGsmMan = MqttClient("AlarmGsmMenager", "194.87.82.22", 1883, "vdsuser", "11101987")       

alrmGsmMan.startProcess()