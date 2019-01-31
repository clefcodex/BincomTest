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

#number of red in the list
redNumber = colorCounts['RED']

#total frequency of colors
totalFreq = 0
for count, freq in colorCounts.most_common():
	totalFreq += freq

#probability function
def prob(event, sample_size):
	if isinstance(event, (list, tuple)):
		count = len(event)

	else:
		count = 1

	return count/sample_size

#probability of choosing a red color
print(prob(redNumber, totalFreq))