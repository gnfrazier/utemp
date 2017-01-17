from umqtt.simple import MQTTClient


def message(**kwargs, server="localhost", topic="MQTT", subject="empty message"):
    c = MQTTClient("umqtt_client", server)
    c.connect()
    c.publish(bytes(topic, 'UTF-8'), bytes(subject, 'UTF-8'))
    c.disconnect()


def main():
    message()

if __name__ == "__main__":
    main()
