import os
import pytesseract
# from PIL import Image # Uncomment this line if you are using PIL
from datetime import datetime
import cv2 # Uncomment this line if you are using OpenCV

# Specify the path to the Tesseract executable (if not in the system PATH)
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\Asus\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"  # Windows
)
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Linux

# Open the image
img_path = "inputs/"
file_name = input("Enter the image file name: ")

try:
    # Remove noise from the image, resize it, grayscale it, and display it
    image = cv2.imread(img_path + file_name)
    # Resize the image to a reduced size for better performance but original orientation if size is large
    # image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR) # Uncomment this line if you want to resize the image
    # image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15) # Uncomment this line if you want to remove noise
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
except FileNotFoundError:
    print("Error : File not found")
    exit()
except Exception as e:
    print(e)
    exit()

# Perform OCR and extract text from the image
text = pytesseract.image_to_string(image)

# Save the extracted text to a file
if os.path.exists("outputs") == False:
    os.mkdir("outputs")
    
with open(f"outputs/{file_name}.txt", "w+") as file:
    file.write(text)
    print("Content of the image:")
    print("-" * 80)
    print(text)
    print("-" * 80)
    print(f"Text extracted from the image has been saved to outputs/{file_name}.txt")
