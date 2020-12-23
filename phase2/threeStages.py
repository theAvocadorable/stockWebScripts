#Properly declare all needed varible
fileName = 'pricesG.txt'
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
# Dont touch them, mainly 

#More used varibles

totalShares = 0
totalCash = 10000 

closingPrice = 0
#Functions
def detBuy(List, smList):
	global totalShares
	global totalCash 
	global closingPrice

	avgPrice = 0
	watching = False
	dipped = False

	isInvested = False
	newHigh = 0
	priceTrail = 0.995 # This is to be changed all the time!! 995 for RDF and closer to 97 for SOL

	for x in range(len(List)-1):
		if isInvested == False:	
			if watching == False:
				if(List[x] == List[x+1]) :
					print("Xs of ", x)
					if(List[x] == List[x+2]):
						#do nothing 
						print("Left")
					else:
						avgPrice = List[x]
						watching = True
			else:
				if(dipped == False):
					if(List[x] < avgPrice):
						dipped = True
					if(List[x] > avgPrice):
						watching = False
				else:
					for y in range(10):
						print("Big is ", List[x])

						small = (x-1)*10 + 1 + y
						print("Small is ", smList[small])
						
						if(smList[small] > avgPrice):
							#buy here
							isInvested = True
							newHigh = smList[small]
							totalShares = int(	totalCash/smList[small])
							totalCash = totalCash - int(totalCash/smList[small])*smList[small]
							print("Buying at ", smList[small], ":", x)
							break

		else:
			for y in range(10):
				small = (x-1)*10 + 1 + y
				if(smList[small] > newHigh):
					newHigh = smList[small]

				if(newHigh * priceTrail > smList[small]):
					#sell
					isInvested = False
					watching = False
					totalCash = totalCash + totalShares*smList[small]
					totalShares = 0
					print("I sell at ", smList[small])
					break

	closingPrice = 	List[len(List)-1]



detBuy(tenList,normalList)
Assets = 0.0
Assets = float(totalShares*closingPrice + totalCash)/totalCash -1

print("CASH: ", totalCash)
print("SHARES ", totalShares)
print(Assets)