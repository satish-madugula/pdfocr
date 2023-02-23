from bs4 import BeautifulSoup
import json

hocr_file = "/home/satish/hocr_mod/ServeS - Trade License0.jpgtext_hocr21-02-202309:57:52.hocr"
with open(hocr_file, 'r') as f:
    hocr = f.read()

soup = BeautifulSoup(hocr, 'html.parser')

pages = []
for page in soup.find_all('div', class_='ocr_page'):
    page_data = {
        'id': page['id'],
        #'width': int(page['data-image-width']),
        #'height': int(page['data-image-height']),
        'lines': []
    }

    for line in page.find_all('span', class_='ocr_line'):
        line_data = {
            'text': line.text.replace("\n", " "),
            'bbox': [int(x) for x in line['title'].split(';')[0].split(' ')[1:]]
        }
        page_data['lines'].append(line_data)

    pages.append(page_data)

json_data = json.dumps(pages, indent=2,ensure_ascii=False)
print(json_data)