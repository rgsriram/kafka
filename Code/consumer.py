from kafka import KafkaConsumer

BROKER_HOST = '127.0.0.1'
PORT = 9092
TOPIC = 'test_topic'


class Consumer(object):
    def __init__(self, broker_host, port):
        self.bootstrap_server = "%s:%s" % (broker_host, port)

        # Group ID for the consumers. If you launch multiple instance of this \
        #       program all will fall under this group id.
        self.group_id = "test_group"

        # Automatically commits the offsets consumed. 
        # But we can handle it on our own also.
        self.enable_auto_commit = True
        self.auto_commit_interval_ms = 1000

        # earliest = will move to the oldest available message
        # latest = will move to the most recent
        self.auto_offset_reset = 'earliest'

    def run(self, topics):
        consumer = KafkaConsumer(
            bootstrap_servers=self.bootstrap_server,
            group_id=self.group_id,
            enable_auto_commit=self.enable_auto_commit,
            auto_commit_interval_ms=self.auto_commit_interval_ms,
            auto_offset_reset=self.auto_offset_reset,
            key_deserializer=str.encode,
            value_deserializer=str.encode
        )

        consumer.subscribe(topics)

        while True:
            messages = consumer.poll(100)

            for key, values in messages.items():
                for message in values:
                    print("Partiton: %s, Offset: %s, Key: %s, Value: %s, Timestamp: %s" % (
                        message.partition,
                        message.offset,
                        message.key,
                        message.value,
                        message.timestamp
                    ))


if __name__ == '__main__':
    consumer = Consumer(broker_host=BROKER_HOST, port=PORT)
    consumer.run([TOPIC])
