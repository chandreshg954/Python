lookup=[0]*100
def initialize():
	for i in range(100):
		lookup[i] = -1
def fib(n) :
	if lookup[n] == -1:
		if n<=1:
			lookup[n] = n
		else:
			lookup[n] = fib(n-1) + fib(n-2)
	return lookup[n]
a = int(input("Enter the number for finding fibonacci : "))
initialize()
b = fib(a) 
print "Fibonacci of given number is : " , b

