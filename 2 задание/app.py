from flask import Flask, request, jsonify
from kafka import KafkaProducer

app = Flask(__name__)
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: str(v).encode('utf-8')
)

kafka_topic = 'your_kafka_topic'

@app.route('/api/data', methods=['POST'])
def send_to_kafka():
    try:
        data = request.get_json()
        producer.send(kafka_topic, value=data)
        return jsonify({"status": "success", "message": "Data sent to Kafka"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
