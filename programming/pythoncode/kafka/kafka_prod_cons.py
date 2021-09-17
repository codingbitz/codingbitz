import threading, logging, time, json, sys
from kafka import KafkaConsumer, KafkaProducer, TopicPartition

class Producer(threading.Thread):
    daemon = False

    def run(self):
        prod = KafkaProducer(bootstrap_servers='localhost:9092',
                                 key_serializer=str.encode,
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                 compression_type='gzip')

        while True:
            try:
                tpc_nm ='tpc-pykafjson'
                prd_msg1 ={'name':'first_record','age':25}
                prd_msg2 ={'name':'second_record','age':45}
                prod.send(tpc_nm, key=prd_msg1["name"],value=prd_msg1)
                prod.send(tpc_nm, key=prd_msg2["name"],value=prd_msg2)
                time.sleep(1)
                prod.flush()
                prod.close()
            except(AssertionError) as assErr:
                print(assErr)
                break
            
class Consumer(threading.Thread):
    daemon = False

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 group_id='grp-pykafjson',
                                 max_poll_records=10,
                                 auto_commit_interval_ms= 5,
                                 enable_auto_commit=True,
                                 session_timeout_ms=30000,
                                 auto_offset_reset='earliest',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        consumer.subscribe(['tpc-pykafjson'])
        ps = [TopicPartition('tpc-pykafjson', p) for p in consumer.partitions_for_topic('tpc-pykafjson')]
        print("beginning:", consumer.end_offsets(ps))

        for msg in enumerate(consumer):
            print("Consumer records:\n")
            print(f'MessageKey: {msg[0]}')
            print (f'topic name: {msg[1][0]},name: {msg[1][6]["name"]},age: {msg[1][6]["age"]}')
            ###consumer.close()
            ###sys.exit()

def main():
    threads = [
        Producer(),
        Consumer()
    ]

    for t in threads:
        t.start()

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:' +
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.ERROR
    )

main()