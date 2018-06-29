# RabbitMQTTExecutor - Distributed data processing for MQTT data streams. 


Allows to easily create a cluster of docker containers that:
1. listen to MQTT messages on a specific topic in the RabbitMQ broker 
2. execute user defined function (UDF) to process each message 
3. write result back as an MQTT message to another topic


## rabbitMQTTBroker

Docker image for setting up RabbitMQ broker with MQTT plugin enabled. 

**Docker commands:**

```
docker build -t rabbitmqtt .
docker run --name rabbitmqtt -d -p 15672:15672 -p 1883:1883 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest rabbitmqtt 
```


## PythonScriptExecutor

Docker image for executing Python UDF on MQTT messages in RabbitMQ broker.

**rabbitMQWorkerTaskQueue.py**

This Python script sets up and subscribes to a RabbitMQ work queue and executes a Python function for every task. 
It also sets up a binding to route messages from a MQTT topic into the work queue and publishes results back into another MQTT topic. 
Any number of task executors can subscribe to the same work queue and RabbitMQ will automatically distribute the work tasks between them. 

**Arguments should be:** 

- **task_queue_host** - IP or hostname of the RabbitMQ broker. MQTT plugin must be activated
- **task_queue** -  Name for the task queue (will be created if does not exist)
- **input_mqtt_topic** - Input MQTT topic to listen to
- **output_mqtt_topic** - Output MQTT topic to publish results to


**userDefinedFunction.py**

Implement call(data) function. This is called for every MQTT message. Results are published to output_mqtt_topic MQTT topic. 


**Docker commands**


```
docker build -t rabbitmqttexecutor .
docker run -d -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest  -e TASK_QUEUE_HOST=172.17.124.22  -e TASK_QUEUE=task_queue_json  -e INPUT_MQTT_TOPIC=input  -e OUTPUT_MQTT_TOPIC=output rabbitmqttexecutor 
```



## JSScriptExecutor 

Java script example for executing JS UDF on MQTT messages in RabbitMQ broker.


