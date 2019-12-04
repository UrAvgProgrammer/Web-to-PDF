#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fpdf import FPDF
from PIL import Image
import os
import uuid

# chrome_path = r"D:\Projects\chromedriver\chromedriver.exe"
chrome_path = r"D:\Work\Selenium Scraper\chromedriver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.implicitly_wait(15)

if not os.path.exists('pdf'):
	os.makedirs('pdf')

if not os.path.exists('img'):
	os.makedirs('img')

def automation(url):
	driver.get(url)
	original_size = driver.get_window_size()
	required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
	required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
	driver.set_window_size(required_width, required_height)
	# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	file_name = str(uuid.uuid4().hex)
	driver.find_element_by_tag_name('body').screenshot('./img/{}.png'.format(file_name))
	img_pdf(file_name)
	# img_pdf_imgsize(file_name)
	driver.quit()

def img_pdf(file_name):
	#NOTE: Better result if page size is equal to image size.
	# set image directory
	image_directory = './img/{}.png'.format(file_name)

	print(image_directory)
	#margin
	margin = 0

	screenshot = Image.open(image_directory)

	width, height = screenshot.size

 	# convert pixel in mm with 1px=0.264583 mm
	width, height = float(width * 0.264583), float(height * 0.264583)

	pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}
	orientation = 'P' if width < height else 'L'
    #  make sure image size is not greater than the pdf format size
	width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
	height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']

	pdf = FPDF()

	pdf.add_page(orientation=orientation)
	
	pdf.image(image_directory, margin, margin, width, height)

	pdf.output("./pdf/" + file_name + ".pdf", "F")

def img_pdf_imgsize(file_name):
	#NOTE: Better result if page size is equal to image size.
	# set image directory
	image_directory = './img/{}.png'.format(file_name)

	print(image_directory)
	#margin
	margin = 0

	screenshot = Image.open(image_directory)

	width, height = screenshot.size

	pdf = FPDF(unit="pt", format=[width, height])

	pdf.add_page()
	
	pdf.image(image_directory, margin, margin)

	pdf.output("./pdf/" + file_name + ".pdf", "F")

if __name__ == '__main__':
	automation('https://webscraper.io/test-sites/e-commerce/scroll/phones/touch')