from kafka import KafkaProducer

BROKER_HOST = '127.0.0.1'
PORT = 9092
TOPIC = 'test'


class Producer(object):
    def __init__(self, broker_host, port):
        # 0 - No waiting for ack
        # 1 - Waiting only for leader
        # 2 - Waiting for leader and replicas
        self.ack = 1

        # No of retries
        self.retries = 3

        # Time gap between data push
        self.linger_ms = 1

        self.bootstrap_server = "%s:%s" % (broker_host, port)

    def run(self, topic_name):
        data = [
            "Hi",
            "Hello",
            "How are you?",
            "Where are you"
        ]

        producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_server,
            acks=self.ack,
            retries=self.retries,
            linger_ms=self.linger_ms,
            key_serializer=str.encode,
            value_serializer=str.encode
        )

        key = 1
        for each in data:
            # Since we specified 'key' here value will be written in that key.
            print producer.send(topic_name, key=str(key), value=each)
            key += 1

        producer.close()


if __name__ == '__main__':
    producer = Producer(broker_host=BROKER_HOST, port=PORT)
    producer.run(topic_name=TOPIC)
