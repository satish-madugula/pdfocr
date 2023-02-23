import os
from pytesseract import pytesseract
from datetime import datetime

"""
As "pytesseract" works on images, we need to convert the pdfs to images before using pytesseract for extracting the text

"""  



src_file = "Ziina - Trade License0.jpg"
filename = os.path.basename(src_file)
print(filename)
output_filename = filename + 'text_hocr' + datetime.now().strftime("%d-%m-%Y%H:%M:%S")
dest_file = os.path.join(os.getcwd(), output_filename)

try:
    pytesseract.run_tesseract(src_file, dest_file, lang='ara+eng', extension=None, config="hocr")
    print(f"hocr file saved at: {os.getcwd()}; Filename: {output_filename}.hocr")
    
except Exception as e:
    print("Exception Occured: " ,e.message)

