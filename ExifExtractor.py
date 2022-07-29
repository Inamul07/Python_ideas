import urllib.request
import os
from PIL import Image
from PIL.ExifTags import TAGS

def dl_jpg(url, full_path):
    urllib.request.urlretrieve(url, full_path)

url = input("Image URL: ")
file_name = input("Enter file name to save as: ")

path = "/Users/mohamedinamulhassan/Desktop/DrugEx-Files/images/"
full_path = path + file_name + '.jpg'
dl_jpg(url, full_path)

image = Image.open(full_path)

exif = {}
for tag, value in image._getexif().items():
    if tag in TAGS:
        exif[TAGS[tag]] = value

if 'GPSInfo' in exif:
    lat = exif['GPSInfo'][2][0] + (exif['GPSInfo'][2][1] / 60) + (exif['GPSInfo'][2][2] / 3600)
    lon = exif['GPSInfo'][4][0] + (exif['GPSInfo'][4][1] / 60) + (exif['GPSInfo'][4][2] / 3600)

print(str(float(lat)) + "," + str(float(lon)))
