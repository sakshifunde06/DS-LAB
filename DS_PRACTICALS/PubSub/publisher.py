import paho.mqtt.client as mqtt
import time

BROKER = "test.mosquitto.org"  # Public broker for testing
TOPIC = "example/pubsub"

def publish_message():
    try:
        client = mqtt.Client()
        client.connect(BROKER, 1883, 60)
        print(f"Connected to broker {BROKER}")
        while True:
            message = input("Enter a message to publish: ")
            client.publish(TOPIC, message)
            print(f"Published: {message}")
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":  # Corrected here
    publish_message()
