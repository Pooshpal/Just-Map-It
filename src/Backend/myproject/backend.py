import cv2
import base64
import json
from navigation import getDirection
def getMap():
    try:
        image = cv2.imread("./assets/map.png")
        if image is not None:
            # Encode the image as base64
            _, encoded_image = cv2.imencode('.png', image)
            base64_image = base64.b64encode(encoded_image.tobytes()).decode()
            return {"msg": base64_image}
        else:
            return {"error": "Failed to load the map image"}

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def getMetadata():
    try:
        f = open('./assets/metadata.json')
        data = json.load(f)
        return data
    except FileNotFoundError:
        return {"error": "Metadata file not found"}
    except json.JSONDecodeError as e:
        return {"error": f"Error decoding metadata: {str(e)}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

def getDirections(itemList: list):
    try:
        return getDirection(itemList)
    except Exception as e:
        return {"error": str(e)}