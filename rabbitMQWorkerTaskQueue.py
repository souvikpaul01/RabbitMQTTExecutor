#!/usr/bin/env python
import pika
import sys
import userDefinedFunction as udf
import traceback
import os

def callback(ch, method, properties, body):
    global output_mqtt_topic
    #print("Received object of size: %r" % sys.getsizeof(body))

    #execute User defined function:
    result = udf.call(body)

    #publish result back to MQTT
    ch.basic_publish(exchange='amq.topic', routing_key=output_mqtt_topic, body=result)

    #print("A Task Completed")

    #Confirm that task was completed
    ch.basic_ack(delivery_tag = method.delivery_tag)


if __name__ == '__main__':
    args = sys.argv[1:]
    if(len(args) != 4):
        print("Arguments should be:")
        print("task_queue_host task_queue input_mqtt_topic output_mqtt_topic ")
        print("Example: 172.17.125.11 json_queue json_output ")
        sys.exit(0)

    try:
        #Ip or hostname of the RabbitMQ broker. MQTT plugin must be activated
        task_queue_host = args[0] #'leader'

        #Name for the task queue (will be created if does not exist)
        task_queue = args[1] #'task_queue_json'

        #Input MQTT topic to listen to
        input_mqtt_topic = args[2] #"input"

        #Output MQTT topic to publis results to
        output_mqtt_topic = args[3]  # "output"

        #Specify connection credentials

        username = "quest"
        if 'RABBITMQ_DEFAULT_USER' in os.environ:
            username = os.environ['RABBITMQ_DEFAULT_USER']

        password = "quest"
        if 'RABBITMQ_DEFAULT_PASS' in os.environ:
            password = os.environ['RABBITMQ_DEFAULT_PASS']

            credentials = pika.PlainCredentials(os.environ['RABBITMQ_DEFAULT_PASS'], os.environ['RABBITMQ_DEFAULT_PASS'])

            # Connect to task queue
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=task_queue_host, credentials=credentials))
            channel = connection.channel()

            #Declare "new" task queue (create only if one does not exist)
            channel.queue_declare(queue=task_queue, durable=True)

            #Bind the task queue to the input MQTT topic (input_routing_key)
            channel.queue_bind(exchange='amq.topic', queue=task_queue, routing_key=input_mqtt_topic)

            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.basic_qos(prefetch_count=1)

            # Define function to be executed on each MQTT message
            channel.basic_consume(callback, queue=task_queue)

            # Start listening to task queue
            channel.start_consuming()

    except:
        print("Error occured")
        traceback.print_exc(file=sys.stdout)




