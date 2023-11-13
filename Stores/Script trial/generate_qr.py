import qrcode
import os
#sections = ["Fresh Produce - 1","Fresh Produce - 2","Fresh Produce - 3","Fresh Produce - 4","Fresh Produce - 5","Meat - 1","Meat - 2","Meat - 3","Dairy - 1","Dairy - 2","Bakery - 1","Bakery - 2","Frozen Foods - 1","Beauty & Health - 1","Beauty & Health - 2","Beauty & Health - 3","Beauty & Health - 4","Beauty & Health - 5","Candy - 1","Stationary - 1","Stationary - 2","Stationary - 3","Stationary - 4","Stationary - 5","Grocery - 1","Grocery - 2","Grocery - 3","Grocery - 4","Grocery - 5","Grocery - 6","Grocery - 7","Beverages - 1","Snacks & Packaged products - 1","Snacks & Packaged products - 2","Snacks & Packaged products - 3","Snacks & Packaged products - 4","Snacks & Packaged products - 5","Snacks & Packaged products - 5","Household and Cleaning - 1","Household and Cleaning - 2","Pet - 1","Pet - 2","Pet - 3"]
access_nodes = {"Fresh Produce - 1":84,"Fresh Produce - 2":83,"Fresh Produce - 3":82,"Fresh Produce - 4":94,"Fresh Produce - 5":96,"Meat - 1":86,"Meat - 2":87,"Meat - 3":99,"Dairy - 1":72,"Dairy - 2":76,"Bakery - 1":69,"Bakery - 2":79,"Frozen Foods - 1":85,"Beauty & Health - 1":29,"Beauty & Health - 2":40,"Beauty & Health - 3":53,"Beauty & Health - 4":60,"Beauty & Health - 5":51,"Candy - 1":89,"Candy - 2":88,"Stationary - 1":47,"Stationary - 2":48,"Stationary - 3":49,"Stationary - 4":50,"Stationary - 5":63,"Grocery - 1":7,"Grocery - 2":15,"Grocery - 3":16,"Grocery - 4":36,"Grocery - 5":37,"Grocery - 6":38,"Grocery - 7":44,"Beverages - 1":26,"Snacks & Packaged products - 1":11,"Snacks & Packaged products - 2":19,"Snacks & Packaged products - 3":29,"Snacks & Packaged products - 4":13,"Snacks & Packaged products - 5":21,"Snacks & Packaged products - 6":33,"Household and Cleaning - 1":2,"Household and Cleaning - 2":4,"Pet - 1":56,"Pet - 2":66,"Pet - 3":58}
coord_dict = {"1": [34, 46], "2": [219, 46], "3": [410, 46], "4": [578, 46], "5": [726, 46], "6": [801, 46], "7": [878, 46], "8": [955, 46], "9": [34, 125], "10": [66, 125], "11": [243, 125], "12": [410, 125], "13": [576, 125], "14": [726, 125], "15": [801, 125], "16": [955, 125], "17": [64, 166], "18": [65, 204], "19": [242, 204], "20": [410, 204], "21": [576, 204], "22": [726, 204], "23": [801, 204], "24": [879, 204], "25": [955, 204], "26": [726, 246], "27": [41, 321], "28": [65, 321], "29": [224, 321], "30": [410, 321], "31": [488, 321], "32": [565, 321], "33": [576, 321], "34": [670, 321], "35": [726, 321], "36": [801, 321], "37": [878, 321], "38": [955, 321], "39": [41, 435], "40": [224, 435], "41": [410, 435], "42": [670, 439], "43": [802, 439], "44": [828, 439], "45": [879, 439], "46": [955, 439], "47": [410, 472], "48": [487, 472], "49": [565, 472], "50": [670, 472], "51": [41, 489], "52": [41, 510], "53": [223, 510], "54": [410, 510], "55": [670, 510], "56": [828, 510], "57": [955, 510], "58": [955, 545], "59": [41, 584], "60": [223, 584], "61": [410, 584], "62": [488, 584], "63": [509, 584], "64": [565, 584], "65": [670, 584], "66": [829, 584], "67": [955, 584], "68": [22, 664], "69": [133, 664], "70": [243, 664], "71": [385, 664], "72": [448, 664], "73": [514, 664], "74": [670, 664], "75": [828, 664], "76": [868, 664], "77": [959, 664], "78": [22, 744], "79": [133, 744], "80": [144, 744], "81": [243, 744], "82": [242, 804], "83": [385, 804], "84": [514, 804], "85": [670, 804], "86": [829, 804], "87": [960, 804], "88": [144, 835], "89": [243, 851], "90": [144, 880], "91": [144, 955], "92": [243, 955], "93": [384, 955], "94": [415, 955], "95": [514, 955], "96": [654, 955], "97": [670, 955], "98": [827, 955], "99": [895, 955], "100": [959, 955]}


# Create a directory to store the QR code images
output_directory = "qr_codes"
os.makedirs(output_directory, exist_ok=True)

# Generate QR codes and save them as image files
for key, value in access_nodes.items():
    # Combine the key, value from access_nodes, and value from coord_dict
    qr_data = f"['{key}', {value}, {coord_dict[str(value)]}]"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image with a file name based on the key
    filename = os.path.join(output_directory, f"{key}.png")
    img.save(filename)

    print(f"QR code for '{key}' saved as '{filename}'")
