#pip install matplotlib


import matplotlib.pyplot as plt 

fileName = 'prices.txt'
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

xVal = []
for x in range(lenTen):
	xVal.append(x)

# line 1 points 

# plotting the line 1 points 
x1 = xVal
y1 = tenList
plt.plot(x1, y1, label = "RDF Ten") 
#plt.scatter(x1, y1, label= "stars", color= "green",  
 #           marker= "|", s=30)

# naming the x axis 
plt.xlabel('Time (s)') 
# naming the y axis 
plt.ylabel('Price (centes)') 
# giving a title to my graph 
plt.title('Comparing srcs!') 

# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 
