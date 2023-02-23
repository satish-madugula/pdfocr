import difflib
import os
import bs4
from lxml.html import fromstring


trade_hocr = 'TradeLicense_10.jpgtext_hocr21-02-202309:58:17.hocr'
serve_hocr = 'ServeS - Trade License0.jpgtext_hocr21-02-202309:57:52.hocr'
# dubai_hocr = 'DUBAI CIVIL TL_0.hocr'

# Load the first HTML file
with open(trade_hocr, 'r') as trade_file:
    #html1 = trade_file.readlines()
    html1 = trade_file.read()

# Load the second HTML file
with open(serve_hocr, 'r') as serve_file:
    #html2 = serve_file.readlines()
    html2 = serve_file.read()



with open(dubai_hocr, 'r') as dubai_file:
    #html2 = serve_file.readlines()
    html3 = dubai_file.read()

# Find the differences between the two HTML files
#diff = difflib.unified_diff(html1, html2)

# Print the differences
#for line in diff:
#    print(line)



print("*"*50)


#print(html1)
parserObj = fromstring(html1)
outputString = str(parserObj.text_content())
with open('trade.txt','a+') as f:
    f.write(outputString)



parserObj1 = fromstring(html2)
outputString_1 = str(parserObj1.text_content())
with open('serve.txt','a+') as f:
    f.write(outputString_1)

# parserObj2 = fromstring(html3)
# outputString_2 = str(parserObj2.text_content())
# with open('dubai.txt','a+') as f:
#     f.write(outputString_2)

serve_file_content = open('serve.txt','r')
s_lines = serve_file_content.read().replace("\n", "")
serve_file_content.close()

trade_file_content = open('trade.txt','r')
t_lines = trade_file_content.read().replace("\n", " ").split(" ")
trade_file_content.close()

