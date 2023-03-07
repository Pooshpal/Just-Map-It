import requests
import json

class Client:
    def __init__(self, host, port,storeID,purpose = 'Test'):
        self.request_url = 'http://'+str(host)+':'+str(port)+'/'+purpose
        self.purpose = purpose
        self.storeID = storeID
        self.run()

    def getMap(self,url,storeID):
        payload = {'storeID': storeID}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            image_data = response.content
            with open('./temp/received_map.jpg', 'wb') as f:
                f.write(image_data)
            return "Success"
        else:
            return "Failed to retrieve image. Status code: {response.status_code}"

    def getMetadata(self,url,storeID):
        payload = {'storeID': storeID}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            with open("./temp/metadata.json", "w") as outfile:
                outfile.write(json.dumps(response))
            return "Success"
        else:
            return "Failed to retrieve metadata. Status code: {response.status_code}"
    
    def getDirections(self,url,storeID):
        items = input("Enter items seperated by a space : ")
        payload = {'storeID': storeID,'itemList':items.split()}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            with open("./temp/Directions.json", "w") as outfile:
                outfile.write(json.dumps(response))
            return "Success"
        else:
            return "Failed to retrieve Directions. Status code: {response.status_code}"
    
    def getLocation(self,url,storeID):
        item = input("Enter the item you see around you : ")
        payload = {'storeID': storeID,'item':item}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            with open("./temp/CurrentLocation.json", "w") as outfile:
                outfile.write(json.dumps(response))
            return "Success"
        else:
            return "Failed to retrieve Current Location. Status code: {response.status_code}"
    
    def test(self,url,storeID):
        payload = {'storeID': storeID}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return "Success"
        else:
            return "Failed to Test. Status code: {response.status_code}"
    
    def run(self):
        if self.purpose == 'getMap':print(self.getMap(self.request_url,self.storeID))
        if self.purpose == 'getMetadata':print(self.getMetadata(self.request_url,self.storeID))
        if self.purpose == 'getDirections':print(self.getDirections(self.request_url,self.storeID))
        if self.purpose == 'getLocation':print(self.getLocation(self.request_url,self.storeID))
        else:print(self.test(self.request_url,self.storeID))