from kafka.client import KafkaClient
from kafka.producer import SimpleProducer, KeyedProducer
import logging
import traceback
import sys


class KafkaLoggingHandler(logging.Handler):

    def __init__(self, hosts_list, topic, key=None):
        logging.Handler.__init__(self)
        self.kafka_client = KafkaClient(hosts_list)
        self.key = key
        self.kafka_topic_name = topic
        if not key:
            self.producer = SimpleProducer(self.kafka_client)
        else:
            self.producer = KeyedProducer(self.kafka_client)

    def emit(self, record):
        # drop kafka logging to avoid infinite recursion
        if record.name == 'kafka':
            return
        try:
            # use default formatting
            msg = self.format(record)
            # produce message
            if not self.key:
                self.producer.send_messages(self.kafka_topic_name, msg)
            else:
                self.producer.send(self.kafka_topic_name, self.key, msg)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def close(self):
        self.producer.stop()
        logging.Handler.close(self)
