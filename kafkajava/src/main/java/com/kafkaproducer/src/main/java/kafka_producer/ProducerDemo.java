package com.kafkaproducer.src.main.java.kafka_producer;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Properties;

public class ProducerDemo{
	public static void main(String[] args) {
		String bootstrap_servers = "127.0.0.1:9092";
		// Create Producer Property
		Properties properties = new Properties();
		properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,bootstrap_servers);
		properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG,StringSerializer.class.getName());

		// Create Producer
		KafkaProducer<String,String> producer = new KafkaProducer<>(properties);
		// Create Producer Record
		ProducerRecord<String,String> record = new ProducerRecord<>("first_topic", "Hello World");
		//Send message
		producer.send(record); //async
		producer.flush();
		producer.close();
	}
}