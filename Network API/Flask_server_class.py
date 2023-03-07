from flask import Flask, request, jsonify, send_file
import threading

app = Flask(__name__)

class Server_Logs:
    def __init__(self):
        self.lock = threading.Lock()
        self.clients = set()

    def add_client(self, client_ip):
        with self.lock:
            self.clients.add(client_ip)
            print(f"New client connected: {client_ip}")

    def remove_client(self, client_ip):
        with self.lock:
            self.clients.remove(client_ip)
            print(f"Client disconnected: {client_ip}")

    def get_clients(self):
        with self.lock:
            return list(self.clients)

    def serve_image(self, image_path):
        return send_file(image_path, mimetype='image/jpeg')

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_log = Server_Logs()

    @app.route('/getMap', methods=['POST'])
    def getMap(self):
        client_ip = request.remote_addr

        # Add client to list of connected clients
        self.server_log.add_client(client_ip)
        
        # Parse JSON data from client
        data = request.get_json()
        image_path = '../Stores/'+str(data['storeID'])+'/map.png'

        # Serve the image
        image = self.server_log.serve_image(image_path)

        # Remove client from list of connected clients
        self.server_log.remove_client(client_ip)

        return image

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
