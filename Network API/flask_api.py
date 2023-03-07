from flask import Flask, request, send_file,jsonify
from threading import Semaphore, Thread

app = Flask(__name__)
semaphore = Semaphore(5)  # Maximum of 5 clients at once

@app.route('/api', methods=['POST'])
def get_image():
    data = request.get_json()  # Retrieve JSON payload from client
    image_path = data['image_path']  # Get image path from JSON payload

    with semaphore:  # Acquire semaphore lock to limit maximum clients
        client_address = request.remote_addr  # Get client IP address
        client_user_agent = request.user_agent.string  # Get client user agent
        print(f'Request received from {client_address} with user agent {client_user_agent}')

        return send_file(image_path, mimetype='image/jpeg')  # Return image file as a response

if __name__ == '__main__':
    app.run()




