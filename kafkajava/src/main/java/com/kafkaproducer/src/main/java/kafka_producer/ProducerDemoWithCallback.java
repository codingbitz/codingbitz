package com.kafkaproducer.src.main.java.kafka_producer;

import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.StringSerializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Properties;

public class ProducerDemoWithCallback {
	public static void main(String[] args) {
		Logger logger = LoggerFactory.getLogger(ProducerDemoWithCallback.class);
		String bootstrap_servers = "127.0.0.1:9092";
		// Create Producer Property
		Properties properties = new Properties();
		properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrap_servers);
		properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

		// Create Producer
		KafkaProducer<String, String> producer = new KafkaProducer<String, String>(properties);
		for (int i = 0; i < 10; i++) {
			// Create Producer Record
			ProducerRecord<String, String> record = new ProducerRecord<>("first_topic", "Checks & balances" + Integer.toString(i));
			//Send message
			producer.send(record, new Callback() {
				@Override
				public void onCompletion(RecordMetadata recordMetadata, Exception e) {
					if (e != null) {
						logger.info("new record metadata rx: \n" +
								"topic:" + recordMetadata.topic() + "\n" +
								"partition: " + recordMetadata.partition() + "\n" +
								"offset: " + recordMetadata.offset() + "\n" +
								"timestamp: " + recordMetadata.timestamp());
					} else {
						logger.error("error while producing topic");
					}
				}
			});
			producer.flush();
		}
		producer.close();
	}
	}