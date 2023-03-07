import requests
import json

image_url = 'http://127.0.0.1:5000/getMap'

# Specify the path to the image file you want to request
storeID = 1

# Create a JSON payload with the image path
payload = {'storeID': storeID}

# Send a POST request to the server to retrieve the image
response = requests.post(image_url, json=payload)

# Check that the response was successful
if response.status_code == 200:
    # Get the contents of the image from the response
    image_data = response.content

    # Save the image to a file
    with open('received_map.jpg', 'wb') as f:
        f.write(image_data)
else:
    print(f"Failed to retrieve image. Status code: {response.status_code}")