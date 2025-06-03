import pika, json
from config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASS

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
params = pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, '/', credentials)

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='result_queue', durable=True)

def callback(ch, method, properties, body):
    result = json.loads(body)
    print(f"Résultat reçu : {result}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='result_queue', on_message_callback=callback)
print("En attente de résultats...")
channel.start_consuming()
