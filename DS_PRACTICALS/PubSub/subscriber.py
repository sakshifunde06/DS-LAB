import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPIC = "example/pubsub"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to broker {BROKER}")
        client.subscribe(TOPIC)
        print("Subscribed to topic:", TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

def subscribe_messages():
    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(BROKER, 1883, 60)
        client.loop_forever()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":  # Corrected here
    subscribe_messages()


'''
   pip install paho-mqtt
   
   python subscriber.py  
   (after this command open another terminal and run command python publisher.py) 
   Received message: HI
'''
'''
   pip install paho-mqtt
   
   python subscriber.py  
   (after this command open another terminal and run command python publisher.py) 
   Received message: HI
'''
