#import necessary moduluses
import urllib.request as ul
import re
from collections import Counter
import psycopg2

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

#generating colorList and freqList
colorList = []
for key in colorCounts.keys():
	colorList.append(key)

freqList = []
for value in colorCounts.values():
	freqList.append(value)

#connection to database
conn = psycopg2.connect(database = "assignment", user = "postgres", password = "gospel1759", host = "127.0.0.1", port = "5432")

cu = conn.cursor()

#iterate through the colorlist and freqlist and populate the table
for x in range(len(colorList)):

	cu.execute("INSERT INTO colortable (color, frequency) \
	VALUES (%s, %s)", (colorList[x], freqList[x]) );	

conn.commit()

print("Data succesfully inserted")

conn.close()
