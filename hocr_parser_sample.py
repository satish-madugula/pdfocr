import bs4
import pprint


xml_input = open("text_hocr14-02-202315:30:02.hocr","r",encoding="utf-8")
soup = bs4.BeautifulSoup(xml_input,'xml')
ocr_lines = soup.findAll("span", {"class": "ocr_line"})#We will save coordinates of line and the text contained in the line in lines_structure list
lines_structure = []
for line in ocr_lines:
    line_text = line.text.replace("\n"," ").strip()
    title = line['title']
    #The coordinates of the bounding box
    x1,y1,x2,y2 = map(int, title[5:title.find(";")].split())
    lines_structure.append({"text": line_text})

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(lines_structure)
