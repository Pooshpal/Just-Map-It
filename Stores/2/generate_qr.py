import qrcode
import os
sections = ["Fresh Produce - 1","Fresh Produce - 2","Fresh Produce - 3","Fresh Produce - 4","Fresh Produce - 5","Meat - 1","Meat - 2","Meat - 3","Dairy - 1","Dairy - 2","Bakery - 1","Bakery - 2","Frozen Foods - 1","Beauty & Health - 1","Beauty & Health - 2","Beauty & Health - 3","Beauty & Health - 4","Beauty & Health - 5","Candy - 1","Stationary - 1","Stationary - 2","Stationary - 3","Stationary - 4","Stationary - 5","Grocery - 1","Grocery - 2","Grocery - 3","Grocery - 4","Grocery - 5","Grocery - 6","Grocery - 7","Beverages - 1","Snacks & Packaged products - 1","Snacks & Packaged products - 2","Snacks & Packaged products - 3","Snacks & Packaged products - 4","Snacks & Packaged products - 5","Snacks & Packaged products - 5","Household and Cleaning - 1","Household and Cleaning - 2","Pet - 1","Pet - 2","Pet - 3"]

# Create a directory to store the QR code images
output_directory = "qr_codes"
os.makedirs(output_directory, exist_ok=True)

# Generate QR codes and save them as image files
for i in sections:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(i)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image with a file name based on the key
    filename = os.path.join(output_directory, f"{i}.png")
    img.save(filename)

    print(f"QR code for '{i}' saved as '{filename}'")
