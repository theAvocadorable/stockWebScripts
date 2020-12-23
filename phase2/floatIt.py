fileName = "RDF-22Dec.txt"
file = open(fileName, "r")
li = file.read().split('/n')

lent = len(li)

for x in range(lent):
	li[x] = li[x].replace(',', '.')
	li[x] = li[x].replace(' ', '')

file = open(fileName, "w")
file.write('');
file.close()

for x in li:
	file = open(fileName, "a")
	file.write(x);
	file.write("\n");
	file.close()

print("Success")