# if you use google colab & you didn't install openai, use this to do it 
!pip install openai

import urllib.request
from PIL import Image
import cv2
from google.colab.patches import cv2_imshow

import os 
import openai 

# you can get your secret key from openAI.api, don't share it with anyone :)
openai.api_key = 'here add your API secret key' 
openai.Model.list()

image_result = openai.Image.create(
    prompt = 'scotch cat sitting in the table eating date', # here type the discriptive text you want the model to generate
    n = 1,  # you can type the number of images you want the model to show
    size = '512x512', # you can choose the size of the image as you prefer but there is some limit if you exceeded it they charge you
)
image_result ['data'][0]['url']
img_url = image_result['data'][0]['url']
urllib.request.urlretrieve(img_url, 'img.png')

img = cv2.imread("img.png")

cv2_imshow(img)
