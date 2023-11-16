import cv2
import base64
import json
from navigation import getDirection
import ast
def getMap():
    image = cv2.imread("./assets/map.png")
     # Encode the image as base64
    _, encoded_image = cv2.imencode('.png', image)
    base64_image = base64.b64encode(encoded_image.tobytes()).decode()
    return {"msg":base64_image}

def getMetadata():
    f = open('./assets/metadata.json')
    data = json.load(f)
    return data


def getDirections(itemList:list):
    return getDirection(itemList)

def getImage(path:list):
    img = cv2.imread('./assets/store.png')
    for i in range(len(path)-1):
        cv2.line(img,(int(path[i][0]),int(path[i][1])),(int(path[i+1][0]),int(path[i+1][1])),(0, 0, 255), 2)
    # cv2.imwrite("./assets/final_path.png",img)
     # Encode the image as base64
    _, encoded_image = cv2.imencode('.png', img)
    base64_image = base64.b64encode(encoded_image.tobytes()).decode()
    return {"msg":base64_image}


import numpy as np
from pyzbar.pyzbar import decode
def getQR(base64__in_image):
    # Decode the base64 image and convert it back to bytes
    decoded_image = base64.b64decode(base64__in_image)

    # Read the decoded image
    image_from_bytes = cv2.imdecode(np.frombuffer(decoded_image, np.uint8), cv2.IMREAD_COLOR)

    # Decode the QR code from the image
    decoded_objects = decode(image_from_bytes)

    
    

    if decoded_objects:
        # Extract the data from the decoded QR code
        decoded_data = decoded_objects[0].data.decode("utf-8")
        image = cv2.imread("./assets/store.png")
        decoded_data=ast.literal_eval(decoded_data)
        print(decoded_data[2])
        image=cv2.circle(image, (int(decoded_data[2][0]),int(decoded_data[2][1])), 5, (0, 0,255) , 5)
        # Encode the image as base64
        _, encoded_image = cv2.imencode('.png', image)
        base64_image = base64.b64encode(encoded_image.tobytes()).decode()

        # Print the decoded data
        return decoded_data,base64_image
    else:
        return "No QR code found in the image or it couldn't be decoded."