#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fpdf import FPDF
from PIL import Image
import glob
import os

chrome_path = r"D:\Projects\chromedriver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.wait(15)

def automation(url):
	driver.get(url)
	original_size = driver.get_window_size()
	required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
	required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
	driver.set_window_size(required_width, required_height)


# def img_pdf():
# 	# set here
# 	image_directory = '/path/to/imageDir'
# 	extensions = ('*.jpg','*.png','*.gif') #add your image extentions
# 	# set 0 if you want to fit pdf to image
# 	# unit : pt
# 	margin = 10

# 	imagelist=[]
# 	for ext in extensions:
# 	    imagelist.extend(glob.glob(os.path.join(image_directory,ext)))

# 	for imagePath in imagelist:
# 	    cover = Image.open(imagePath)
# 	    width, height = cover.size

# 	pdf = FPDF(unit="pt", format=[width + 2*margin, height + 2*margin])
# 	pdf.add_page()

# 	pdf.image(imagePath, margin, margin)

# 	destination = os.path.splitext(imagePath)[0]
# 	pdf.output(destination + ".pdf", "F")