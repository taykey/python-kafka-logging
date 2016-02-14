from kafka.client import KafkaClient
from kafka.producer import SimpleProducer, KeyedProducer
from kafka.conn import DEFAULT_SOCKET_TIMEOUT_SECONDS
import logging


class KafkaLoggingHandler(logging.Handler):

    def __init__(self, hosts_list, topic, timeout_secs=DEFAULT_SOCKET_TIMEOUT_SECONDS, **kwargs):
        logging.Handler.__init__(self)

        self.kafka_client = KafkaClient(hosts_list, timeout=timeout_secs)
        self.key = kwargs.get("key", None)
        self.kafka_topic_name = topic

        if not self.key:
            self.producer = SimpleProducer(self.kafka_client, **kwargs)
        else:
            self.producer = KeyedProducer(self.kafka_client, **kwargs)

    def emit(self, record):
        # drop kafka logging to avoid infinite recursion
        if record.name == 'kafka':
            return
        try:
            # use default formatting
            msg = self.format(record)
            if isinstance(msg, unicode):
                msg = msg.encode("utf-8")

            # produce message
            if not self.key:
                self.producer.send_messages(self.kafka_topic_name, msg)
            else:
                self.producer.send_messages(self.kafka_topic_name, self.key, msg)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def close(self):
        if self.producer is not None:
            self.producer.stop()
        logging.Handler.close(self)
