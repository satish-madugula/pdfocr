import os
from pytesseract import pytesseract
from datetime import datetime
from pdf2image import convert_from_path

"""
As "pytesseract" works on images, we need to convert the pdfs to images before using pytesseract for extracting the text
"""  
try:
    imgs_path = "/Users/satishmadgula/Desktop/pdfocr/jpgs"
    src_file = "/Users/satishmadgula/Desktop/pdfocr/TL/TL ABUDHABI FREELANCE.PDF"
    filename = os.path.basename(src_file)

    file_name_without_ext = filename[:len(filename)-4]

    pages = convert_from_path(src_file)
    for i,page in enumerate(pages):
        image_name = file_name_without_ext + "_" + str(i)
        full_image_name = os.path.join(imgs_path, image_name+".jpg")
        page.save(full_image_name, "JPEG")
        output_filename = filename + '_' + datetime.now().strftime("%d-%m-%Y%H-%M-%S")
        dest_file = os.path.join(os.getcwd(), output_filename)
        custom_config = r'--oem 3 --psm 6 hocr'

        pytesseract.run_tesseract(full_image_name, dest_file, lang='eng+ara', extension=None, config=custom_config)
        print(f"hocr file saved at: {os.getcwd()}; Filename: {output_filename}.hocr")
    
except Exception as e:
    print("Exception Occured: " ,e.message)