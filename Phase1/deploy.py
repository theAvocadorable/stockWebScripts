import os
from selenium import webdriver
import time
from datetime import datetime

share = "RDF"

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

driver.get("https://www.google.com/search?q=jse%3Ardf&rlz=1C1CHZL_enZA765ZA765&oq=jse%3Ardf&aqs=chrome.0.69i59j69i61j69i58j69i61.2148j0j7&sourceid=chrome&ie=UTF-8")

now = datetime.now()
currentTime = int(now.strftime("%H"))*60 + int(now.strftime("%M"))

valuesRDF = []
valuesSOL = []
valuesSNH = []
valuesRMBH = []
valuesDRD = []

valuesNPN = []
valuesSBK = []
valuesPPC = []
valuesIMP = []

print("Session Begins")
firstShot = True

def getIt(name):
	driver.get(name)
	price = driver.find_element_by_class_name("NprOob")	
	currentPrice = price.text
	return currentPrice

#while (currentTime > 435 and currentTime < 1251) or currentTime == 1253:#915:
def job():
	global valuesRDF, valuesSOL, valuesSNH, valuesRMBH, valuesDRD, valuesNPN, valuesSBK, valuesPPC, valuesIMP
	
	valuesRDF.append(getIt("https://www.google.com/search?q=jse%3Ardf&rlz=1C1CHZL_enZA765ZA765&oq=jse%3Ardf&aqs=chrome.0.69i59j69i61j69i58j69i61.2148j0j7&sourceid=chrome&ie=UTF-8"))
	valuesSOL.append(getIt("https://www.google.com/search?rlz=1C1CHZL_enZA765ZA765&sxsrf=ALeKk00c4fVC6wPjXojIaRa2Otkl93xArg%3A1608632523634&ei=y8jhX-CdJqeDhbIPi6y2iAk&q=jse%3Asol&oq=jse%3Asol&gs_lcp=CgZwc3ktYWIQAzoECAAQRzoHCAAQyQMQQzoKCAAQsQMQgwEQQzoLCAAQsQMQgwEQkQI6BAgAEEM6CAgAELEDEIMBUNOfG1imrBtg2a0baABwAngAgAGUAogBmgmSAQMyLTWYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwigr5SRr-HtAhWnQUEAHQuWDZEQ4dUDCA0&uact=5"))
	valuesSNH.append(getIt("https://www.google.com/search?rlz=1C1CHZL_enZA765ZA765&sxsrf=ALeKk01ebBFUjjt0aqNAaki174jpK5-BmA%3A1608634393683&ei=GdDhX4iaKeK21fAPsaKSqAE&q=jse%3Asnh&oq=jse%3Asnh&gs_lcp=CgZwc3ktYWIQAzoECAAQRzoECCMQJzoECAAQQzoFCAAQkQI6DQgAELEDEIMBEMkDEEM6CggAELEDEIMBEEM6BwgAELEDEEM6CAgAELEDEIMBUKXhA1i96wNgou0DaABwBXgAgAGnAogBzg2SAQMyLTeYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwjIiu-MtuHtAhViWxUIHTGRBBUQ4dUDCA0&uact=5"))
	valuesRMBH.append(getIt("https://www.google.com/search?rlz=1C1CHZL_enZA765ZA765&sxsrf=ALeKk03aBh1LVN_KXFdR3OjKVEuyIRa3eg%3A1608634458033&ei=WtDhX5nNAdem1fAPxZ29yAw&q=jse%3Armbh&oq=jse%3Brm&gs_lcp=CgZwc3ktYWIQAxgAMgQIIxAnMggIABDJAxCRAjICCAAyAggAMgcIABAUEIcCMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoECAAQRzoFCAAQkQI6CAgAELEDEIMBOgUILhCxAzoOCAAQsQMQgwEQyQMQkQI6CggAELEDEBQQhwI6BQgAELEDOg0IABCxAxCDARAUEIcCOg0IABCxAxCDARDJAxBDOgoIABCxAxCDARBDOgQIABBDOhAIABCxAxCDARDJAxAUEIcCOgQIABAKOggIABDJAxDEAjoHCAAQyQMQDVDB3gNY1f8DYLaPBGgEcAN4AIABkgKIAZETkgEEMi0xMJgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab"))
	valuesDRD.append(getIt("https://www.google.com/search?rlz=1C1CHZL_enZA765ZA765&sxsrf=ALeKk03VpYsavHXnUoPeJ-u7nUpxPOSjpQ%3A1608635572061&ei=tNThX9-ZA8CU1fAPr9e10AI&q=JSE%3ADRD&oq=JSE%3ADRD&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABgujBoAHACeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwjfw-G-uuHtAhVAShUIHa9rDSoQ4dUDCA0&uact=5"))

	valuesNPN.append(getIt("https://www.google.com/search?rlz=1C1CHZL_enZA765ZA765&ei=HAHiX8fSO_Ke1fAPnqiv0AQ&q=jse%3Anpn&oq=jse%3Anpn&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1DhKVjhKWC9LWgAcAJ4AIABAIgBAJIBAJgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwjH0PHr5OHtAhVyTxUIHR7UC0oQ4dUDCA0&uact=5"))
	valuesSBK.append(getIt("https://www.google.com/search?rlz=1C1CHZL_enZA765ZA765&sxsrf=ALeKk009KOKFVYrF5GUCk10Tue19yKAr3w%3A1608646721594&ei=QQDiX5ruI_HIxgOE3ZugAQ&q=jse%3Asbk&oq=jse%3Asbk&gs_lcp=CgZwc3ktYWIQAzoECAAQRzoECCMQJzoNCAAQsQMQgwEQyQMQQzoKCAAQsQMQgwEQQzoFCAAQkQI6BAgAEEM6CAgAELEDEIMBUNKxD1jlvA9gsb4PaABwAXgAgAGTA4gB7wqSAQcyLTQuMC4xmAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwjakqOD5OHtAhVxpHEKHYTuBhQQ4dUDCA0&uact=5"))
	valuesPPC.append(getIt("https://www.google.com/search?rlz=1C1CHZL_enZA765ZA765&sxsrf=ALeKk00OAU0RXGPaGzkcQgcRIiCXEMp9Gw%3A1608646976684&ei=QAHiX4KmKYOU1fAP2o-ysAQ&q=jse%3Appc&oq=jse%3Appc&gs_lcp=CgZwc3ktYWIQAzoECAAQRzoECCMQJzoHCAAQyQMQQzoKCAAQsQMQgwEQQzoFCAAQkQI6BAgAEENQor4BWIHLAWDWywFoAHAEeACAAaMDiAGpCZIBBzItMi4xLjGYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwiCxvT85OHtAhUDShUIHdqHDEYQ4dUDCA0&uact=5"))	
	valuesIMP.append(getIt("https://www.google.com/search?rlz=1C1CHZL_enZA765ZA765&sxsrf=ALeKk01KA1LIX0MkY3frQNgien44tGp6iQ%3A1608647003808&ei=WwHiX_DuMOXJxgOksI6QCQ&q=jse%3Aimp&oq=jse%3Aimp&gs_lcp=CgZwc3ktYWIQAzoECAAQRzoECCMQJzoFCAAQkQI6BAgAEEM6CAgAELEDEIMBOgIILjoOCAAQsQMQgwEQyQMQkQI6CggAELEDEIMBEEM6BwgAELEDEEM6BQgAELEDOgIIADoNCAAQsQMQgwEQyQMQQ1C4tAFYg8kBYKfKAWgAcAN4AIAB-AKIAfcMkgEFMi00LjKYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwiwiOyJ5eHtAhXlpHEKHSSYA5IQ4dUDCA0&uact=5"))

	firstShot = True

	



while True:
	now = datetime.now()
	currentTime = int(now.strftime("%H"))*60 + int(now.strftime("%M"))
	if currentTime > 435 and currentTime < 915:
		job()
		time.sleep(24)	
	elif firstShot:
		print("Moved one")
		firstShot = False	
		print("RDF") 
		print(valuesRDF) 
		print("SOL") 
		print(valuesSOL)
		print("SNH") 
		print(valuesSNH)
		print("RMBH")  
		print(valuesRMBH)
		print("DRD") 
		print(valuesDRD) 
		print("NPN") 
		print(valuesNPN)
		print("SBK") 
		print(valuesSBK)
		print("PPC")  
		print(valuesPPC)
		print("IMP")  
		print(valuesIMP)
		valuesRDF = [] 
		valuesSOL = [] 
		valuesSNH = [] 
		valuesRMBH = []  
		valuesDRD = [] 		
		valuesNPN = [] 
		valuesSBK = [] 
		valuesPPC = []
		valuesIMP = []
	
	elif int(now.strftime("%H")) > 15 or int(now.strftime("%H")) < 6:
		print("moved 2")
		time.sleep(3600)
		

	else:
		time.sleep(60)
	

#heroku run python deploy.py
#heroku ps:scale worker=1, heroku logs --tail
#git push heroku master