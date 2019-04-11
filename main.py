import csv
import numpy as np
import cv2
from matplotlib import pyplot as plt
import img2pdf 
from PIL import Image 
import os 


def convertToPdf(img):
    pdf_bytes = img2pdf.convert(img.filename) 
    file = open("denemeeee.pdf", "wb") 
    file.write(pdf_bytes) 
    img.close() 
    file.close() 


def writeToImg(img, line):
    font                   = cv2.FONT_HERSHEY_COMPLEX
    bottomLeftCornerOfText = (324,470)
    fontScale              = 0.85
    fontColor              = (0,0,0)
    lineType               = 2

    cv2.putText(img,'Hello World!', 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)




img = cv2.imread("image.jpg")
'''
plt.imshow(img)
plt.show()
'''
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (324,470)
fontScale              = 0.85
fontColor              = (0,0,0)
lineType               = 2

cv2.putText(img,'Hello World!', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)

cv2.imshow("image", img)







cv2.waitKey(0)
cv2.destroyAllWindows()

'''
print("df")
store = []
with open('ex.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    print(reader)
    for row in reader:
        store = row[0].split(";")
csvFile.close()

'''


