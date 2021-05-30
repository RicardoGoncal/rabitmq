#!/usr/bin/env python

import sys
import pika

message = ' '.join(sys.argv[1:]) or "Hello World"

# Executando conexão
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Criação da lista
channel.queue_declare(queue='task_queue', durable=True)

# Usando o Exchange para determinar as configs de envio
channel.basic_publish(exchange='', routing_key='task_queue', body=message, properties=pika.BasicProperties(delivery_mode=2))

print(" [x] Sent %r" %message)
connection.close()
