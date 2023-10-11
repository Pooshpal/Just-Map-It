import cv2
import base64
def getMap():
    image = cv2.imread("D:/Projects/Just-Map-It/Backend/myproject/assets/map.png")
     # Encode the image as base64
    _, encoded_image = cv2.imencode('.png', image)
    base64_image = base64.b64encode(encoded_image.tobytes()).decode()
    return {"msg":base64_image}

def getMetadata():
    pass

def getItems():
    pass

def getDirections():
    pass