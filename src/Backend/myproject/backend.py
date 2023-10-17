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

def getImage(path:list):
    img = cv2.imread('./assets/floor_blueprint.png')
    for i in range(len(path)-1):
        cv2.line(img,(int(path[i][0]),int(path[i][1])),(int(path[i+1][0]),int(path[i+1][1])),(0, 0, 255), 2)
    #cv2.imwrite("./assets/final_path.png",img)
     # Encode the image as base64
    _, encoded_image = cv2.imencode('.png', img)
    base64_image = base64.b64encode(encoded_image.tobytes()).decode()
    return {"msg":base64_image}

