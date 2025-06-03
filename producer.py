import pika, json, time, random
from config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASS

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
params = pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, '/', credentials)

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

operations = ['add', 'sub', 'mul', 'div', 'all']

def generate_task():
    return {
        'n1': random.randint(1, 100),
        'n2': random.randint(1, 100),
        'op': random.choice(operations)
    }

while True:
    task = generate_task()
    message = json.dumps(task)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2)
    )
    print(f"Envoyé : {message}")
    time.sleep(random.randint(2, 5))
