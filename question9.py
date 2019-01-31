#0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def fibonacci(n):
	alist = []
	n1 = 0
	n2 = 1
	count = 0
	if n <= 0:
		print("Invalid entry!, Enter a positive integer")
	elif (n == 1):
		alist.append(n1)
	else:
		while count < n:
			alist.append(n1)
			nth = n1 + n2

			# updating n1 and n2
			n1 = n2
			n2 = nth
			count += 1
	return alist

print("Fibonacci series upto 50 terms: ", fibonacci(50))
print('\n')
print("sum of the first 50 Fibonacci sequence: ", sum(fibonacci(50)) )