#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fpdf import FPDF
from PIL import Image
import glob
import os
import uuid

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
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	if not os.path.exists('img'):
    	os.makedirs('img')

    file_name = str(uuid.uuid4().hex)
	driver.find_element_by_tag_name('body').screenshot('/img/{}.png'.format(file_name))
	
	driver.quit()

def img_pdf(file_name):
	if not os.path.exists('pdf'):
    	os.makedirs('pdf')
	# set here
	image_directory = '/img/{}.png'.format(file_name)
	 #add your image extentions
	# set 0 if you want to fit pdf to image
	# unit : pt
	margin = 10

    screenshot = Image.open(image_directory)
    width, height = screenshot.size

	pdf = FPDF(unit="pt", format=[width + 2*margin, height + 2*margin], 'A4')

	pdf.add_page()
	
	pdf.image(image_directory, margin, margin)


	pdf.output("/pdf/" + filename + ".pdf", "F")