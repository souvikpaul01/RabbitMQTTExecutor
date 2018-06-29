#!/usr/bin/env node

var amqp = require('amqplib/callback_api');
var q = 'task_queue';
var input_topic = 'input';
var host = 'amqp://guest:guest@172.17.124.22';
var output_topic = 'output';


function udf(msg){

	//Do something:
	result = msg;

	console.log(" [x] Computed %s", result);
	return result;
}


amqp.connect(host, function(err, conn) {
  conn.createChannel(function(err, ch) {
    ch.assertQueue(q, {durable: true});
    ch.prefetch(1);
    ch.bindQueue(q, 'amq.topic', input_topic);
    console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", q);

    ch.consume(q, function(msg) {
	data = msg.content.toString()
	console.log(" [x] Received %s", data);
	result = udf(data);
	ch.publish('amq.topic', output_topic, new Buffer(result));
	console.log(" [x] Done");
        ch.ack(msg);
    }, {noAck: false});
  });
});
