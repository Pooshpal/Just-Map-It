from flask import Flask, request, jsonify, send_file
import threading


app = Flask(__name__)
class Server_Logs:
    def __init__(self):
        self.lock = threading.Lock()
        self.clients = set()

    def add_client(self, client_ip, purpose):
        with self.lock:
            self.clients.add(client_ip)
            print(f"**        New client connected: {client_ip} for : {purpose}       **")

    def remove_client(self, client_ip,purpose):
        with self.lock:
            self.clients.remove(client_ip)
            print(f"**        Client disconnected: {client_ip} for : {purpose}        **")

    def get_clients(self):
        with self.lock:
            return list(self.clients)

    def serve_image(self, image_path):
        return send_file(image_path, mimetype='image/jpeg')

server_log = Server_Logs()
class Server:

    @app.route('/getMap', methods=['POST'])
    def getMap():
        client_ip = request.remote_addr
        # Add client to list of connected clients
        server_log.add_client(client_ip,"Fetching Map")
        # Parse JSON data from client
        data = request.get_json()
        image_path = '../Stores/'+str(data['storeID'])+'/map.png'
        # Serve the image
        image = server_log.serve_image(image_path)
        # Remove client from list of connected clients
        server_log.remove_client(client_ip,"Fetching Map")
        return image
    
    @app.route('/getMetadata', methods=['POST'])
    def getMetadata(): 
        client_ip = request.remote_addr
        server_log.add_client(client_ip,"Fetching Metadata")
        data = request.get_json()
        # Metadata has to contain : a catalog of all items present section wise in the store and a list of all items present. 
        # { 'all_items' : [] , section_wise_items : {'section_name' : [],}}
        # load this metadata into variable json
        json_path = './Store/'+str(data['storeID'])+'/metadata.json'
        json = {'Metadata':'Yes'}
        server_log.remove_client(client_ip,"Fetching Metadata")
        return jsonify(json)
    
    @app.route('/getDirections', methods=['POST'])
    def getDirections():
        client_ip = request.remote_addr
        server_log.add_client(client_ip,"Fetching Directions")
        data = request.get_json()
        #call function and send it data['itemList'] and startNode as default. store returned json as variable
        # returned json should be :
        # {destination_1:{items:['apple','banana'],path:[1,2,3,4]},destination_2:... ,billing:{items:None,path:[]}}
        # The path shd be : the previous destination to this one. for destination_1 , it shd be start to destination_1
        # the path shd als have the last destination to billing as last entry.
        json = {'Directions':'Yes'}
        server_log.remove_client(client_ip,"Fetching Directions")
        return jsonify(json)
    
    @app.route('/getLocation', methods=['POST'])
    def getLocation():
        client_ip = request.remote_addr
        server_log.add_client(client_ip,"Fetching Location")
        data = request.get_json()
        #call function and send it data['item'] store returned json as variable
        json = {'Location':'Yes'}
        server_log.remove_client(client_ip,"Fetching Location")
        return jsonify(json)
    
    @app.route('/Test', methods=['POST'])
    def getTest():
        client_ip = request.remote_addr
        server_log.add_client(client_ip,"Testing")
        data = request.get_json()
        json = {'status':200}
        server_log.remove_client(client_ip,"Testing")
        return jsonify(json)


app.run(host='0.0.0.0', port=5000, threaded=True)
server = Server()