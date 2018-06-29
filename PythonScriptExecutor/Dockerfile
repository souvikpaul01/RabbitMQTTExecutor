FROM python:alpine

RUN pip3 install pika

WORKDIR /app
COPY . /app

CMD ["sh", "-c", "python3 rabbitMQWorkerTaskQueue.py $TASK_QUEUE_HOST $TASK_QUEUE $INPUT_MQTT_TOPIC $OUTPUT_MQTT_TOPIC"]
