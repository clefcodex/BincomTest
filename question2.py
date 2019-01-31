#import necessary moduluses
import urllib.request as ul
import re
from collections import Counter

# extract and read file
extract = ul.urlopen('file:///home/clefcodex/Desktop/BincomTest/Materials/python_class_test.html').read()


#use regex to find all contents in <td> tag
contents = re.findall(r'<td>(.*?)</td>', str(extract))
 
#create list to days and colors
days = []
colors = []

for i in range(len(contents)):
	if i % 2 == 0:
		days.append(contents[i])
	else:
		colors.append(contents[i])


colorindexZero = colors[0].split(', ') #put all monday colors into a single list
colorindexZero[-1] = colorindexZero[-1].strip(',')
colorindexOne = colors[1].split(', ') #put all tuesday colors into a single list
colorindexTwo = colors[2].split(', ') #put all wednesday colors into a single list
colorindexThree = colors[3].split(', ') #put all thursday colors into a single list
colorindexFour = colors[4].split(', ') #put all friday colors into a single list

#put all lists monday through friday in a single list totalColor
totalColor = colorindexZero + colorindexOne + colorindexTwo + colorindexThree + colorindexFour


#put colors in dictionary colorCounts
colorCounts = Counter(totalColor)

#mostly worn throughout the week
mostlyWorn = colorCounts.most_common(1)

print(mostlyWorn)