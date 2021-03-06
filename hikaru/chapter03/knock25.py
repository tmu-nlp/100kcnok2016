#-*-coding: utf-8-*-
import json, re
f = open('jawiki-country.json','r')
for line in f:
    jsonData = json.loads(line)
    if jsonData['title'] == "イギリス":
        break 

UK_text = jsonData['text'].strip() 
find_list = re.findall('==+(.*?)==+', UK_text)# + 直前の正規表現の1回以上の繰り返し
#print (find_list)

UK_dict = {}
UK_list = jsonData['text'].splitlines()
for (i, line) in enumerate(UK_list):
    if line.count('='):
        field = re.search('\|(.*?)=', line)
        value = re.search('=(.*)', line)
        if field != None and value != None:
            UK_dict[field.group(1).strip()] = value.group(1).strip()
    if line == '}}':
        break
print (UK_dict.items())
