#-*-coding: UTF-8-*-
import csv
import numpy as np
import cv2
from matplotlib import pyplot as plt
import img2pdf 
from PIL import ImageFont, ImageDraw, Image
import os 


def convertToPdf(filename):
    img = Image.open(filename + ".jpg") 
    pdf_bytes = img2pdf.convert(img.filename) 
    file = open("pdf/" + filename + ".pdf", "wb") 
    file.write(pdf_bytes) 
    img.close() 
    file.close() 


def writeToImg(img, line):
    '''
    fontScale              = 0.85
    fontColor              = (0,0,0)
    lineType               = 2
    font                   = cv2.FONT_HERSHEY_COMPLEX

    ctr = 0
    '''
    line[2] = line[2] + " " + line[3]
    line.pop(3)
    line.pop(4)
    line.pop(7)
    #['Sıra No', 'Sicil No', 'Vatandaşlık No', 'Ad', 'Soyad', 'Başvuru Alanı', '']
    #['Vatandaşlık no', 'Sicil No','Ad Soyad', 'Başvuru Alanı', 'Salon Adı','Sıra No']
    # Vatandaşlık No;Sicil No;Ad;Sınıf;Kat;Salon Adı;Sıra No;Yer

    #cornerArray = [(908,717), (340,566), (324,513), (286,479), (286 + len(line[3])*16,479), (346,579), (0,0), (344,716)]
    cornerArray = [(324,513), (341,545), (286,479), (346,579),(906,684),(344,716), (908,717)]
    b,g,r,a = 0,0,0,0
    fontpath = "OpenSans-Regular.ttf"
    font = ImageFont.truetype(fontpath, 24)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
   
    # 286,502 AD Soyad  289 484
    # 324 533 Tc Kimlik No  323 516
    #  340 569 Sicil no 341 551
    # 346 603 Başvuru alanı 345 585
    #  344 740 Salon  345 722
    #  908 705 Kat 906 684
    #  908 741 Sıra no 909 720
   
    print("-----")
    for i in range(7):

        draw.text(cornerArray[i],  line[i], font = font, fill = (b, g, r, a))
        img = np.array(img_pil)
 
    return img










store = []
with open('liste3.csv', 'r') as csvFile:
    img = cv2.imread("image.jpg")

    reader = csv.reader(csvFile)
    for row in reader:
        store = row[0].split(";")
        
 #      plt.imshow(img)
 #      plt.show()
        print(store)
        newImg = writeToImg(img, store)
        
        cv2.imwrite(store[0] + ".jpg",newImg)
        convertToPdf(store[0])
        os.remove(store[0] + ".jpg")
csvFile.close()
