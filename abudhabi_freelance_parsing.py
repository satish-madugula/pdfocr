from distutils.command.clean import clean
import os
import json
import pprint
from bs4 import BeautifulSoup
from lxml.html import fromstring
from lxml import etree
import pandas as pd



res = {}

# def hocr_to_dataframe(fp):
#     doc = etree.parse(fp)
#     words = []
#     langs = []
#     for path in doc.xpath('//*'):
#         if 'ocrx_word' in path.values():
#             if 'eng' in path.values():
#                 langs.append('eng')
#             else:
#                 langs.append('ara')
#             words.append(path.text)

#     dfReturn = pd.DataFrame({'word' : words,'language' : langs})

#     return dfReturn

hocr_path = "/Users/satishmadgula/Desktop/pdfocr/TL ABUDHABI FREELANCE.PDF_24-02-202322-22-46.hocr"
xml_input = open(hocr_path,"r",encoding="utf-8")

# df_data = hocr_to_dataframe(hocr_path)
# df_data.to_csv("abudhabi_freelance.txt",header=False)
key_list = ["certificate no","issue date","license no","adcci no","license type" ,"legal form","trade name","establishment date","expiry date","mohre","gdrfa"]
def ifKeyPresent(lst, fieldName):
    count = 0
    for ele in lst:
        if (ele in fieldName.lower()):
            count = count + 1
    if count >0:
        return True
    else:
         return False

def getAllCertificateDetails(soup,elemid,fieldName):
    if ifKeyPresent(key_list,fieldName):
        lines = soup.find('span', attrs={'id':elemid})
        eng_span =  lines.findAll("span",{"lang":"eng"})
        ara_span = lines.findAll("span",{"dir":"rtl"})
        eng_words = ""
        ara_words = ""
        for word in eng_span:
            eng_words += word.text.replace(":","") + " "
        for word in ara_span:
            ara_words += word.text.replace(":","") + " "
        

        if 'certificate no' in fieldName.lower():
            eng_words = eng_words.lower().replace("certificate no", "")
            res["certificate no"] = eng_words
            res["certificate no ara "] = ara_words
        
        if 'issue date' in fieldName.lower():
            eng_words = eng_words.lower().replace("issue date", "")
            res["issue date"] = eng_words
            res["issue date ara "] = ara_words

        if 'license no' in fieldName.lower():
            eng_words = eng_words.lower().replace("license no", "")
            res["license no"] = eng_words
            res["license no ara "] = ara_words

        if 'adcci no' in fieldName.lower():
            eng_words = eng_words.lower().replace("adcci no", "")
            res["adcci no"] = eng_words
            res["adcci no ara "] = ara_words
        
        if 'license type' in fieldName.lower():
            eng_words = eng_words.lower().replace("license type", "")
            res["license type"] = eng_words
            res["license type ara "] = ara_words

        if 'legal form' in fieldName.lower():
            eng_words = eng_words.lower().replace("legal form", "")
            res["legal form"] = eng_words
            res["legal form ara "] = ara_words

        if 'trade name' in fieldName.lower():
            eng_words = eng_words.lower().replace("trade name", "")
            res["trade name"] = eng_words
            res["trade name ara "] = ara_words

        if 'establishment date' in fieldName.lower():
            eng_words = eng_words.lower().replace("establishment date", "")
            res["establishment date"] = eng_words
            res["establishment date ara "] = ara_words

        if 'expiry date' in fieldName.lower():
            eng_words = eng_words.lower().replace("expiry date", "")
            res["expiry date"] = eng_words
            res["expiry date ara "] = ara_words
        
        if 'mohre' in fieldName.lower():
            eng_words = eng_words.lower().replace("mohre", "")
            res["mohre"] = eng_words
            res["mohre ara "] = ara_words

        if 'gdrfa' in fieldName.lower():
            eng_words = eng_words.lower().replace("gdrfa", "")
            res["gdrfa"] = eng_words
            res["gdrfa ara "] = ara_words

 

# def getAllIssueDateDetails(soup,elemid):
#     certificate_lines = soup.find('span', attrs={'id':elemid})
#     #print(certificate_lines.text.replace("\n"," ")
#     eng_span =  certificate_lines.findAll("span",{"lang":"eng"})
#     ara_span = certificate_lines.findAll("span",{"dir":"rtl"})
#     eng_words = ""
#     ara_words = ""
#     for word in eng_span:
#         eng_words += word.text + " "
#     for word in ara_span:
#         ara_words += word.text + " "
#     eng_words = eng_words.replace("Issue Date ", "")
#     res["Issue Date"] = eng_words
#     res["Issue Date ara "] = ara_words
#     print(res)


soup = BeautifulSoup(xml_input,'xml')
ocr_lines = soup.findAll("span", {"class": "ocr_line"})
lines = ''
for line in ocr_lines:
    texts = line.findAll("span",{"class":"ocrx_word"})
    getAllCertificateDetails(soup, line.get('id'),line.text.replace("\n"," ").strip())
    #print(line.text.replace("\n"," "))
    # line_text = ""
    # for idx,word in enumerate(texts):
    #     line_text += word.text + " "
    #     #if line_text.strip() == 'Certificate No':
    #     getAllCertificateDetails(soup, line.get('id'),line_text.strip())
        
        # if line_text.strip() == 'Issue Date':
        #     getAllIssueDateDetails(soup, line.get('id'))

        # if line_text.strip() == 'License No':
        #     getAllLicenseNumberDetails(soup, line.get('id'))
        
        # if line_text.strip() == 'ADCCI NO':
        #     getAllAdcciNoDetails(soup, line.get('id'))
        
    #lines += line_text + "\n"

#print(lines)

print(res)

"""
ocr_lines = soup.findAll("span", {"class": "ocr_line"})
lines= []
for line in ocr_lines:
    read_dir = line.find(attrs={"dir":"rtl"})
    if read_dir is not None:
        lang = 'ara'
    else:
        lang = 'eng'
    line_text = line.text.replace("\n"," ").strip()
    #print(line_text)
    if 'certificate no' in line_text.lower():
        words = line_text.split(" ")
        certificate_number_val = words[3] # from the line the value of the certificate is 4 
        res['certificate no'] = certificate_number_val
        res['certificate_no_ara'] = words[5] + " " + words[6]
    
    elif 'issue date' in line_text.lower():
        words = line_text.split(":")
        if len(words)>=3:
            issue_date_val = words[1] # from the line the value of the certificate is 4 
            res['Issue Date'] = issue_date_val
            res['issue_date_ara'] = words[2]

    elif 'license no' in line_text.lower():
        words = line_text.split(":")
        if len(words)>=3:
            licenseno_val = words[1] # from the line the value of the certificate is 4 
            res['License No'] = licenseno_val
            res['License No_ara'] = words[2]
    
    elif 'adcci no' in line_text.lower():
        words = line_text.split(":")
        if len(words) >= 3:
            adccino_val = words[1] # from the line the value of the certificate is 4 
            res['ADCCI No'] = adccino_val
            res['ADCCI No_ara'] = words[2]

    elif 'license type' in line_text.lower():
        words = line_text.split(":")
        print(words)
        # licensetype_val = words[3] # from the line the value of the certificate is 4 
        # res['ADCCI No'] = adccino_val
        # res['ADCCI No_ara'] = words[5] + " " + words[6]
    

#print(res)

"""