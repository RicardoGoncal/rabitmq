# Work Queues no RabbitMQ

O objetivo deste estudo é ajudar os estudantes da área de tecnologia com o uso do software
de mensageria chamado **RabbitMQ**.

O estudo aplicado no momento é o segundo tutorial apresentado no próprio site do **RabbitMQ** e
será todo estruturado na linguagem de programação Python.

[link para o site do RabbitMQ](https://www.rabbitmq.com/)

## Requisitos

- Ter o Python 3.6+ instalado em sua máquina
- Instalar o Docker
- Uma IDE de preferência
- Realizar a instalação do pacote descrito abaixo

```bash
python -m pip install pika --upgrade
```

## Como funciona o código


### new_task.py



### worker.py



## Como executar o envio da mensagem

Após escrever os dois códigos, precisamos executar algumas etapas para que o processo seja
executado.

1. Com o Docker instalado execute o seguinte comando `sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management`
![Execução do comando Docker]()
