# RabbitMQTTExecutor 

Distributed Python Task Executor for:
1. listening to MQTT messages in the RabbitMQ broker on a specific topic
2. executing Python UDF to process each message 
3. writing results back as MQTT messages to another topic


rabbitMQTTBroker

For setting up RabbitMQ broker as a Docker container with MQTT enabled. 

Docker commands:
docker build -t rabbitmqtt .
docker run --name rabbitmqtt -d -p 15672:15672 -p 1883:1883 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest rabbitmqtt 


PythonScriptExecutor


rabbitMQWorkerTaskQueue.py

This Python script sets up and subscribes to a RabbitMQ work queue and executes a Python function for every task. 
It also sets up a binding to route messages from a MQTT topic into the work queue and publishes results back into another MQTT topic. 

Any number of task executors can subscribe to the same work queue and RAbbitMQ will distribute the work tasks between them. 

Arguments should be: task_queue_host task_queue input_routing_key output_routing_key


task_queue_host - Ip or hostname of the RabbitMQ broker. MQTT plugin must be activated
task_queue -  Name for the task queue (will be created if does not exist)
input_mqtt_topic - Input MQTT topic to listen to
output_mqtt_topic - Output MQTT topic to publis results to


userDefinedFunction.py

implement call(data) function. This is called for every MQTT message. Results are published to output_mqtt_topic MQTT topic. 





Docker commands:


docker build -t rabbitmqttexecutor .
docker run -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest  -e TASK_QUEUE_HOST=172.17.124.22  -e TASK_QUEUE=task_queue_json  -e INPUT_MQTT_TOPIC=input  -e OUTPUT_MQTT_TOPIC=output rabbitmqttexecutor 



