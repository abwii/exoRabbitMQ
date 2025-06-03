import pika, json, time, sys, random
from config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASS

operation = sys.argv[1]

def compute(op, n1, n2):
    time.sleep(random.randint(5, 15))
    if op == "add": return n1 + n2
    elif op == "sub": return n1 - n2
    elif op == "mul": return n1 * n2
    elif op == "div": return n1 / n2 if n2 != 0 else None

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
params = pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, '/', credentials)

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_declare(queue='result_queue', durable=True)

def callback(ch, method, properties, body):
    data = json.loads(body)
    n1, n2, op = data["n1"], data["n2"], data["op"]

    if op == operation or op == "all":
        result = compute(operation, n1, n2)
        output = {"n1": n1, "n2": n2, "op": operation, "result": result}
        channel.basic_publish(exchange='', routing_key='result_queue', body=json.dumps(output))
        print(f"[{operation}] Résultat envoyé : {output}")

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
print(f"[{operation}] Worker prêt...")
channel.start_consuming()
