import os
import pytesseract
from PIL import Image
from datetime import datetime

# Specify the path to the Tesseract executable (if not in the system PATH)
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\Asus\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"  # Windows
)
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Linux

# Open the image
img_path = "inputs/"
file_name = input("Enter the image file name: ")
# image = Image.open(img_path + file_name)
try:
    image = Image.open(img_path + file_name)
except FileNotFoundError:
    print("Error : File not found")
    exit()
except Exception as e:
    print(e)
    exit()

# Perform OCR and extract text from the image
text = pytesseract.image_to_string(image)

# Save the extracted text to a file
now = datetime.now()
current_time = now.strftime("%H-%M-%S")

if os.path.exists("outputs") == False:
    os.mkdir("outputs")
    
with open(f"outputs/{file_name}.txt", "w+") as file:
    file.write(text)
    print("-" * 80)
    print(text)
    print("-" * 80)
    print(f"Text extracted from the image has been saved to outputs/{file_name}.txt")
