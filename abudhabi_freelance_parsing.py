import os
import json
from bs4 import BeautifulSoup
import cv2
import pandas as pd


res = {}

hocr_path = (
    "/home/satish/Desktop/tonewlaptop/hocr_mod/hocrs/TL ABUDHABI FREELANCE.PDF_24-02-202322-22-46.hocr"
)


boundingbox_images_path = "/home/satish/Desktop/tonewlaptop/hocr_mod/boundingbox_images"


xml_input = open(hocr_path, "r", encoding="utf-8")

key_list = [
    "certificate no",
    "issue date",
    "license no",
    "adcci no",
    "license type",
    "legal form",
    "trade name",
    "establishment date",
    "expiry date",
    "mohre",
    "gdrfa",
]


def ifKeyPresent(lst, fieldName):
    count = 0
    for ele in lst:
        if ele in fieldName.lower():
            count = count + 1
    if count > 0:
        return True
    else:
        return False

def genBoundingBox(img_path,lines):
    title = lines['title']
    img_path = img_path.replace('"','')
    filename = os.path.basename(img_path)
    if os.path.exists(os.path.join(boundingbox_images_path,filename)):
        img = cv2.imread(os.path.join(boundingbox_images_path,filename))
    elif os.path.exists(img_path):
        img = cv2.imread(img_path)
    
    x1,y1,x2,y2 = map(int, title[5:title.find(";")].split())
    cv2.rectangle(img, (x1,y1),(x2,y2), (0,255,0), 1)
    cv2.imwrite(os.path.join(boundingbox_images_path,filename),img)



def getAllDetails(soup, elemid, fieldName,ocr_image_path):
    if ifKeyPresent(key_list, fieldName):
        lines = soup.find("span", attrs={"id": elemid})
        eng_span = lines.findAll("span", {"lang": "eng"})
        ara_span = lines.findAll("span", {"dir": "rtl"})
        eng_words = ""
        ara_words = ""
        for word in eng_span:
            eng_words += word.text.replace(":", "") + " "
        for word in ara_span:
            ara_words += word.text.replace(":", "") + " "

        if "certificate no" in fieldName.lower():
            genBoundingBox(ocr_image_path,lines)
            eng_words = eng_words.lower().replace("certificate no", "")
            res["certificate_no"] = eng_words.strip()
            res["certificate_no_ara "] = ara_words.strip()

        elif "issue date" in fieldName.lower():
            genBoundingBox(ocr_image_path,lines)
            eng_words = eng_words.lower().replace("issue date", "")
            res["issue_date"] = eng_words.strip()
            res["issue_date_ara "] = ara_words.strip()

        elif "license no" in fieldName.lower():
            genBoundingBox(ocr_image_path,lines)
            eng_words = eng_words.lower().replace("license no", "")
            res["license_no"] = eng_words.strip()
            res["license_no_ara "] = ara_words.strip()

        elif "adcci no" in fieldName.lower():
            genBoundingBox(ocr_image_path,lines)
            eng_words = eng_words.lower().replace("adcci no", "")
            res["adcci_no"] = eng_words.strip()
            res["adcci_no_ara "] = ara_words.strip()

        elif "license type" in fieldName.lower():
            genBoundingBox(ocr_image_path,lines)
            eng_words = eng_words.lower().replace("license type", "")
            res["license_type"] = eng_words.strip()
            res["license_type_ara "] = ara_words.strip()

        elif "legal form" in fieldName.lower():
            genBoundingBox(ocr_image_path,lines)
            eng_words = eng_words.lower().replace("legal form", "")
            res["legal_form"] = eng_words.strip()
            res["legal_form_ara "] = ara_words.strip()

        elif "trade name" in fieldName.lower():
            genBoundingBox(ocr_image_path,lines)
            eng_words = eng_words.lower().replace("trade name", "")
            res["trade_name"] = eng_words.strip()
            res["trade_name_ara "] = ara_words.strip()

        elif "establishment date" in fieldName.lower():
            genBoundingBox(ocr_image_path,lines)
            eng_words = eng_words.lower().replace("establishment date", "")
            res["establishment_date"] = eng_words.strip()
            res["establishment_date_ara "] = ara_words.strip()

        elif "expiry date" in fieldName.lower():
            genBoundingBox(ocr_image_path,lines)
            eng_words = eng_words.lower().replace("expiry date", "")
            res["expiry_date"] = eng_words.strip()
            res["expiry_date_ara "] = ara_words.strip()

        elif "mohre" in fieldName.lower():
            genBoundingBox(ocr_image_path,lines)
            eng_words = eng_words.lower().replace("mohre", "")
            res["mohre"] = eng_words.strip()
            res["mohre_ara"] = ara_words.strip()

        elif "gdrfa" in fieldName.lower():
            genBoundingBox(ocr_image_path,lines)
            eng_words = eng_words.lower().replace("gdrfa", "")
            res["gdrfa"] = eng_words.strip()
            res["gdrfa_ara "] = ara_words.strip()


soup = BeautifulSoup(xml_input, "xml")
# to get the image path of the hocr file
ocr_page = soup.find_all("div",{"id":"page_1"})
ocr_page_title = ocr_page[0]['title'].split(";")
ocr_image_path = ocr_page_title[0][6:]


ocr_lines = soup.findAll("span", {"class": "ocr_line"})
lines = ""
for line in ocr_lines:
    texts = line.findAll("span", {"class": "ocrx_word"})
    getAllDetails(soup, line.get("id"), line.text.replace("\n", " ").strip(),ocr_image_path)

print(res)

# df = pd.DataFrame(res,index=[0])
# print(df.head())
