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


img = cv2.imread("img.jpg")
plt.imshow(img)
plt.show()
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


