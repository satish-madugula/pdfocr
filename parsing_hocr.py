# %%
import re
import bs4
import pprint

                
                
pat = "\w[par]\w[_]\d{1,3}[_]\d{1,3}"

my_regex = re.compile(pat)

# matched_strings = soup.find_all(text=my_regex)
# print(matched_strings)
                
# %%
xml_input = open("text_hocr14-02-202315:30:02.hocr","r",encoding="utf-8")
soup = bs4.BeautifulSoup(xml_input,'xml')

p_elems = soup.find_all('p',id=my_regex)
#print(len(p_elems))

for p in p_elems:
    p_lines = p.find_all("span",{"class": "ocr_line"})
    lines= []
    for line in ocr_lines:
        line_text = line.text.replace("\n"," ").strip()
        title = line['title']
        #The coordinates of the bounding box
        x1,y1,x2,y2 = map(int, title[5:title.find(";")].split())
        lines.append({"text": line_text})

# %%    

# needs to be itreated on all p_elems

p_lines = p_elems[12].find_all("span",{"class":"ocr_line"})
l = p_lines[0] #
l = l.text.replace("\n"," ") # gives the text in that line...