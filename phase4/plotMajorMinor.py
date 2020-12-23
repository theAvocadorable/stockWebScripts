#pip install matplotlib


import matplotlib.pyplot as plt 

file = open("pricesG.txt", "r")
li = file.read().split()
file.close()
listSmall = []

for x in li:
	listSmall.append(float(x))



lent = len(listSmall)

xVal = []

for x in range(lent):
	xVal.append(x)

# plotting the line 1 points 
x1 = xVal
y1 = listSmall
# plotting the line 2 points 
plt.plot(x1, y1, label = "SmallerInt") 

bigX = []
for x in range(int(lent/10)):
	bigX.append(x*10)

bigY = []
for x in range(int(lent/10)):
	bigY.append(listSmall[x*10])

# line 2 points 
x2 = bigX
y2 = bigY
# plotting the line 2 points 
plt.plot(x2, y2, label = "ten times") 

#range it

#plt.ylim(360,390) 

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
