from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

#this is all pretty standard
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
#until here

share = "RDF"

#get the website
driver.get("https://www.google.com/")

search = driver.find_element_by_name("q")
search.send_keys("JSE", share)
search.send_keys(Keys.RETURN)

text = driver.find_element_by_class_name("NprOob")

print(text.text)


proceed = False
now = datetime.now()

while int(now.strftime("%H")) < 20:
	now = datetime.now()
	seconds = now.strftime("%S")
	if(proceed == False and seconds[-1] != "0"):
		time.sleep(0.5)
		print("miss", seconds)
	if(proceed == False and seconds[-1] == "0"):
		proceed = True
		print("HIT")

	if proceed:
		now = datetime.now()
		print(now.strftime("%S"))
		driver.refresh()

		price = driver.find_element_by_class_name("NprOob")		
		currentPrice = price.text
		file = open("prices.txt", "a")
		file.write(currentPrice);
		file.write("\n");
		file.close()
		secs = str(now.strftime("%S"))[-1]
		time.sleep(30 - int(secs))

i = 0 
while i < 31:

	driver.refresh();

	price = driver.find_element_by_class_name("NprOob")		
	currentPrice = price.text
	file = open("prices.txt", "a")
	file.write(currentPrice);
	file.write("\n");
	file.close()
	secs = str(now.strftime("%S"))[-1]
	print("wrote")
	time.sleep(30 - int(secs))

	i = i +1