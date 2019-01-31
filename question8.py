import random


def randonNum():
	numlist = []
	for x in range(4):
	  numlist.append(random.randint(0,1))
	for i in numlist:
		print(i, end="")
	base10 = numlist[0]*8 + numlist[1]*4 + numlist[2]*2 + numlist[3]*1
	print(" to base10 is: ", base10)

randonNum()