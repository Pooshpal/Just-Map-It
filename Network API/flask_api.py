from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def get_json():
    data = request.get_json()  # Retrieve JSON payload from client
    return jsonify(data)  # Return contents of JSON payload as a JSON response

if __name__ == '__main__':
    app.run()
