def find(alist, item):
	if len(alist) == 0:
		return "Your number is not in my list"
	else:
		mid = len(alist)//2
		if item == alist[mid]:
			return "Your number is in my list"
		else:
			if item < alist[mid]:
				return find(alist[:mid], item)
			else:
				return find(alist[mid+1:], item)

testlist = list(range(0,100,3))

#get input from and convert to integer
item = int(input("Enter your number: "))

print(find(testlist, item))
