import cv2
import base64
import json
from navigation import getDirection
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