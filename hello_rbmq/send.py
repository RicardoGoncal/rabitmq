#!/usr/bin/env python

import pika


# Executando a conexão 
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Criação da lista
channel.queue_declare(queue='hello')

# Usando o Exchange para determinar as config de envio
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

print("[x] Sent 'Hello World!'")

connection.close()