FROM python:alpine

RUN pip3 install pika

WORKDIR /app
COPY . /app

CMD ["python3", "script.py",  "$TASK_QUEUE_HOST", "$TASK_QUEUE", "$INPUT_MQTT_TOPIC", "$OUTPUT_MQTT_TOPIC"] 
