# Mqtt Client for Alarm GSM Menager
from threading import Thread, Lock
from queue import Queue
from time import sleep          # this lets us have a time delay
import paho.mqtt.client as mqtt
import json 

class MqttClient():

    def __init__(self, name, server, port, login, passw):
        self.name = name
        self.server = server
        self.port = port
        self.login = login
        self.passw = passw
        self.client = mqtt.Client(self.name) 
        self.client.username_pw_set(username=self.login, password=self.passw) 
        self.client.will_set(topic=f'{self.name}/status', payload="Offline")
        self.client.on_connect = self.onConnect
        self.client.on_disconnect = self.onDisconnect
        self.client.on_subscribe = self.onSubscribe
        self.client.on_message = self.onMessage
        
        print(f'Init client param:'
            f'\nName: \t {self.name}'
            f'\nSrv: \t {self.server}'
            f'\nPort: \t {self.port}'
            f'\nLogin: \t {self.login}'
            f'\nPassw: \t {self.passw}')

    def onConnect(self, client, userdata, flags, rc):
        print("Mqtt Connected with result code " + str(rc))
        self.client.publish(topic=f'{self.name}/status', payload="Online")
        self.subscribe()
        
    def onDisconnect(self, client, userdata, rc = 0):
        print(f'DisConnected result code {str(rc)}')
     
    # The callback for when a PUBLISH message is received from the server.
    def onMessage(self, ckient, userdata, msg):
        print(f'"Recive: \ntopic:{msg.topic}') 
        print(f'msg:{str(msg.payload.decode("utf-8"))}') 
        
    def onSubscribe(self, client, userdata, mid, granted_qos):
        print(  f'Subscribe: \nmid: {str(mid)}'
                f'\ngranted_qos: {str(granted_qos)}')    
        
    def subscribe(self):
         self.client.subscribe(f'Alarm-GSM/+/system')
         self.client.subscribe(f'Alarm-GSM/+/jsonData')
        
    def process(self):    
        couter = 0

        result = self.client.connect(self.server, self.port, 15)
        print(f'Connect in process result = {result}')
        self.client.loop_start()
        try:        
            while(True):
                sleep(5)
                print(f'Counter loop {couter}')
                couter += 1
                
        except KeyboardInterrupt:
                print ("exiting")
                self.client.disconnect()
                self.client.loop_stop()                 
            
    def startProcess(self):
        # ThrClient = Thread(target=self.process, args=(client,))
        Thread(target=self.process).start()
        
alrmGsmMan = MqttClient("AlarmGsmMenager", "194.87.82.22", 1883, "vdsuser", "11101987")       
alrmGsmMan.startProcess()