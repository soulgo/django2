#!/usr/bin/env python
#encoding:UTF-8
from PIL import Image
import subprocess
def cleanFile(filePath,newFilePath):
    image = Image.open(filePath)

    image = image.point(lambda x:0 if x<143 else 255)
    image.save(newFilePath)

    subprocess.call(["tesseract",newFilePath,"output"])

    file = open("out.txt",'r')
    print (file.read())
    file.close()

cleanFile("captcha.jpg","ca.png")