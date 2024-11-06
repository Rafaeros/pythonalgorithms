from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def hello():
    return jsonify(message="pong")

@app.route('/soma', methods=['POST'])
def soma():
    data = request.get_json()
    result = data['num1'] + data['num2']
    return jsonify(result=result)

@app.route('/subtracao', methods=['POST'])
def subtracao():
    data = request.get_json()
    result = data['num1'] - data['num2']
    return jsonify(result=result)

@app.route('/multiplicacao', methods=['POST'])
def multiplicacao():
    data = request.get_json()
    result = data['num1'] * data['num2']
    return jsonify(result=result)

@app.route('/divisao', methods=['POST'])
def divisao():
    data = request.get_json()
    if data['num2'] == 0:
        return jsonify(error="Division by zero is not allowed"), 400
    result = data['num1'] / data['num2']
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)