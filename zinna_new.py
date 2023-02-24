import os
import json
import pprint
from bs4 import BeautifulSoup
from lxml.html import fromstring
from lxml import etree
import pandas as pd

# def hocr_to_dataframe(fp):
#     doc = etree.parse(fp)
#     words = []
#     langs = []
#     for path in doc.xpath('//*'):
#         if 'ocrx_word' in path.values():
#             if 'ara' in path.values():
#                 langs.append('ara')
#             else:
#                 langs.append('eng')
#             words.append(path.text)

#     dfReturn = pd.DataFrame({'word' : words,'language' : langs})

#     return dfReturn

hocr_path = "/home/satish/hocr_mod/hocrs/Ziina - Trade License_0.hocr"
xml_input = open(hocr_path,"r",encoding="utf-8")

#df_data = hocr_to_dataframe(hocr_path)
#df_data.to_csv("MyZinna.txt",header=False)

soup = BeautifulSoup(xml_input,'xml')
ocr_lines = soup.findAll("span", {"class": "ocr_line"})#We will save coordinates of line and the text contained in the line in lines_structure list

for line in ocr_lines:
    texts = line.findAll("span",{"class":"ocrx_word"})
    for text in texts:
        w = text.find(attrs={"lang":"ara"})
        if w is not None and w == 'ara':
            

    





