import cv2
import qrcode
from pyzbar.pyzbar import decode

access_nodes = {"Fresh Produce - 1":84,"Fresh Produce - 2":83,"Fresh Produce - 3":82,"Fresh Produce - 4":94,"Fresh Produce - 5":96,"Meat - 1":86,"Meat - 2":87,"Meat - 3":99,"Dairy - 1":72,"Dairy - 2":76,"Bakery - 1":69,"Bakery - 2":79,"Frozen Foods - 1":85,"Beauty & Health - 1":29,"Beauty & Health - 2":40,"Beauty & Health - 3":53,"Beauty & Health - 4":60,"Beauty & Health - 5":51,"Candy - 1":89,"Candy - 2":88,"Stationary - 1":47,"Stationary - 2":48,"Stationary - 3":49,"Stationary - 4":50,"Stationary - 5":63,"Grocery - 1":7,"Grocery - 2":15,"Grocery - 3":16,"Grocery - 4":36,"Grocery - 5":37,"Grocery - 6":38,"Grocery - 7":44,"Beverages - 1":26,"Snacks & Packaged products - 1":11,"Snacks & Packaged products - 2":19,"Snacks & Packaged products - 3":29,"Snacks & Packaged products - 4":13,"Snacks & Packaged products - 5":21,"Snacks & Packaged products - 6":33,"Household and Cleaning - 1":2,"Household and Cleaning - 2":4,"Pet - 1":56,"Pet - 2":66,"Pet - 3":58}

# Define the path to the QR code image
qr_code_image_path = "./qr_codes/Beauty & Health - 3.png"

# Load the QR code image using OpenCV
qr_code_image = cv2.imread(qr_code_image_path)

# Decode the QR code
decoded_objects = decode(qr_code_image)

if decoded_objects:
    # Extract the data from the decoded QR code
    decoded_data = decoded_objects[0].data.decode("utf-8")

    # Print the decoded data
    print(f"Decoded data: {decoded_data}")
else:
    print("No QR code found in the image or it couldn't be decoded.")

access_point = access_nodes[decoded_data]

print(f"Access point: {access_point}")