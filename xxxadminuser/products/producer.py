import pika
import json

params = pika.URLParameters("amqps://eyfccuct:2msDlzGcil6LwCVEbOkDmq-FXDQbkqRh@mustang.rmq.cloudamqp.com/eyfccuct")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="main", body=json.dumps(body), properties=properties)
