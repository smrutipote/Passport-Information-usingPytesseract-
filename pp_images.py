import os
import pytesseract
import re
import pandas as pd
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


folder_path='pp_images'
image_list = os.listdir(folder_path)
print(image_list)

Names =[]
Date_passport=[]
for image in image_list:
    image_path = os.path.join(folder_path,image)
    image_text= pytesseract.image_to_string(image_path)
    image_text= re.sub('\n+','\n', image_text)
    raw =re.sub('[^a-zA-Z0-9.@/,]+',' ',image_text.strip())
    #print(raw)
    name = re.findall('\s[A-Z]{3,10}\s[A-Z]{3,20}\s', raw)
    dates = re.findall('[0-9]{2}/[0-9]{2}/[0-9]{4}', raw)
    if name:
        Names.append(name[-1])
    else:
        Names.append(' ')
    if dates:
        Date_passport.append(dates[-1])
    else:
        Date_passport.append(' ')
        
    
print(Names)
print(Date_passport)

dict1 = {'Names':Names,'Pasport Date': Date_passport}

df= pd.DataFrame(dict1, columns= dict1.keys())

df.to_csv('Passport.csv',index= False)