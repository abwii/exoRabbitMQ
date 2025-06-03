from flask import Flask, render_template
import threading, pika, json
from config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASS

app = Flask(__name__)
results = []

def consume():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    params = pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, '/', credentials)

    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='result_queue', durable=True)

    def callback(ch, method, properties, body):
        data = json.loads(body)
        results.append(data)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='result_queue', on_message_callback=callback)
    channel.start_consuming()

@app.route('/')
def index():
    return render_template('index.html', results=results)

if __name__ == '__main__':
    threading.Thread(target=consume, daemon=True).start()
    app.run(debug=True)
