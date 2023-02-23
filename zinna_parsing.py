import os
import json
import pprint
from bs4 import BeautifulSoup
from lxml.html import fromstring
import pandas as pd


xml_input = open("Ziina - Trade License0.jpgtext_hocr22-02-202314:50:19.hocr","r",encoding="utf-8")
soup = BeautifulSoup(xml_input,'xml')
ocr_lines = soup.findAll("span", {"class": "ocr_line"})#We will save coordinates of line and the text contained in the line in lines_structure list
lines_structure = []
y_coord = []
text = []
for line in ocr_lines:
    line_text = line.text.replace("\n"," ").strip()
    title = line['title']
    x1,y1,x2,y2 = map(int, title[5:title.find(";")].split())
    lines_structure.append({"text": line_text,"boxes":(x1,y1,x2,y2)})
    y_coord.append(y1)
    text.append(line_text)
    
zipped = zip(text,y_coord)

zipped = list(zipped)
# Using sorted and lambda
sorted_on_ycord = sorted(zipped, key = lambda x: x[1])

#read json 
json_file_path = "/home/satish/hocr_mod/zinna_structure.json"

with open(json_file_path, 'r') as j:
     contents = json.loads(j.read())

keys = list(contents.keys())

arranged_by_lines = []

for idx,data in enumerate(sorted_on_ycord):
    if idx == 0:
        line_number = sorted_on_ycord[idx][1]
    else:
        if sorted_on_ycord[idx][1]-sorted_on_ycord[idx-1][1] <= 3:
            line_number = sorted_on_ycord[idx-1][1]
        else:
            line_number = sorted_on_ycord[idx][1]
    text = sorted_on_ycord[idx][0]
    arranged_by_lines.append((text,line_number))
    

print(arranged_by_lines)

df = pd.DataFrame(arranged_by_lines  , columns =['text', 'y_coord'])
out = df.groupby(['y_coord'],sort=True).apply(lambda x: ' '.join(x['text'])) # list
print(type(out))
output = list(out)

