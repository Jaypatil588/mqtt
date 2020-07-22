import paho.mqtt.client as mqttClient
import time

broker_address= "15.206.119.242"  #Broker address
port = 1883                         #Broker port
topic1 = "set"
instance = "local sub"
print( "topic :",topic1)
print( "IP:",broker_address)
print( "Instance:",instance)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
#        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    print ("Received Message: "  + message.payload)

Connected = False   #global variable for the state of the connection
client = mqttClient.Client(instance)               #create new instance
#client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback

client.connect(broker_address, port=port)          #connect to broker

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)

client.subscribe(topic1)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print( "exiting")
    client.disconnect()
    client.loop_stop()
