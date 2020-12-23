
#TO imporve (Make wait times satndard by minusing the fetch time, what if low volume does mean a move,) 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


fileName = 'RDF-12Dec.txt'
file = open(fileName, "r")
rawList = file.read().split()
file.close()
normalList = []
tenList = []
for x in rawList:
	normalList.append(float(x))
lenNormal = len(normalList)
for x in range(int(lenNormal/10)):
	tenList.append(normalList[x*10])
lenTen = len(tenList)


#End
List = []

avgPrice = 0
watching = False

isInvested = False
dipped = False

newHigh = 0


totalShares = 0
totalCash = 10000

doubleDrop = False

current = 0
#Start

#Stuff to play with
watchLimSet = 40
priceTrail = 0.99
initalSteps = 2
preStartSteps = 10

watchingLim = watchLimSet




def testPoint(value):
	global avgPrice, watching
	if(value == List[len(List)-1] and  value == List[len(List)-2] and value == List[len(List)-3] \
	and value == List[len(List)-4] and value == List[len(List)-5] and value == List[len(List)-6] ):
		# Lets add on Or to grab other variations of patterns like from the jaggled lines or :
		if(value == List[len(List)-7]):
			#do nothing 
			print("Test ends on: Left")
		else:
			avgPrice = value
			watching = True
			print("Test end on: Watching")

def watchPoint(value):
	global dipped, avgPrice, isInvested, watching, newHigh,totalCash,totalShares, watchingLim, doubleDrop

	if(watchingLim == 0):
		Watching = False
		dipped = False
		watchingLim = watchLimSet
		doubleDrop = False
	else:

		if(dipped):
			if(value > avgPrice):
				#Buy
				watchingLim = watchLimSet

				isInvested = True
				watching = False
				dipped = False
				doubleDrop = False
				newHigh = avgPrice
				totalShares = (totalCash/value)
				totalCash = totalCash - (totalCash/value)*value
				print("Buy at:",value)
			else:
				watchingLim = watchingLim - 1
		else:
			if(value < avgPrice - avgPrice*0.0025 ):
				if doubleDrop:
					dipped = True
					print("Dipped moved to True")
					watchingLim = watchingLim - 1
					doubleDrop = False
				else:
					doubleDrop = True

			if(value > avgPrice):
				watching = False
				watchingLim = watchLimSet
				doubleDrop = False
				print("Wrong Trend")

def sellWatch(value):
	global newHigh, priceTrail, isInvested,watching,totalShares,totalCash
	if(newHigh * priceTrail > value):
		#sell
		
		isInvested = False
		totalCash = totalCash + totalShares*value
		totalShares = 0
		print("Sell at:", value)
	if(value > newHigh):
		newHigh = value
		print("New High Reached!")

def grabPoint():
	
	return(normalList[current])

		
now = datetime.now()
formatted = int(now.strftime("%H"))*60 + int(now.strftime("%M"))

List.append(grabPoint())
current = current + preStartSteps
List.append(grabPoint())
current = current + preStartSteps
List.append(grabPoint())
current = current + preStartSteps


while current < lenNormal:#formatted > 554 and formatted < 1035:
	value = (grabPoint())
	if(isInvested == False):
		if(watching == False):
			current = current+initalSteps
			testPoint(value) 

			print("P1 - waited 250")
		else:
			current = current + 1 
			watchPoint(value)
			print("P2 - waited 20")
	else:
		current = current + 1
		sellWatch(value)
		print("P3 - waited 10")

	now = datetime.now()
	formatted = int(now.strftime("%H"))*60 + int(now.strftime("%M"))	
	List.append(value)

print("Total Cash:",totalCash)
print("Total shares:",totalShares)
print("closes at", List[len(List)-1])
