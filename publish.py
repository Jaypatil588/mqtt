import paho.mqtt.client as mqtt #import the client1
import time

broker_address= "15.206.119.242"  #Broker addre$

port = 1883
instance = "Pub"
topic = "set"

client = mqtt.Client(instance) #create new instance
client.connect(broker_address, port=port) #connect to broker

time.sleep(1)
msg="a"
while msg !="end":
        msg=raw_input("Type something : ")
        client.publish(topic,msg) #publish
time.sleep(1)
