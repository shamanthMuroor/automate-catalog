import os
import requests

images = []
dir = "D:\\Python Project Files\\Capstone Final Project\\supplier-data\\images\\"
for image in os.listdir(dir):
    imagefullpath = os.path.join(dir, image)
    images.append(imagefullpath)

url = "http://localhost/upload/"
for upload_image in images:
    with open(upload_image, 'rb') as opened:
        res = requests.post(url, files={'file':opened})
