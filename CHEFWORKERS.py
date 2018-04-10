from sys import stdin
n = int(input().strip())
coin = [int(x) for x in stdin.readline().split()]
worker = [int(x) for x in stdin.readline().split()]
ls1 = []
ls2 = []
ls3 = []
for i in range(n):
	if worker[i] == 3 :
		ls3.append(coin[i])
	elif worker[i] == 2:
		ls2.append(coin[i])
	else:
		ls1.append(coin[i])
if(len(ls1)!=0 and len(ls2)!=0 and len(ls3)!=0):
	l1 = min(ls1)
	l2 = min(ls2)
	l3 = min(ls3)
	if l3 >= l2 + l1:
		print(l2+l1)
	else :
		print(l3)
elif(len(ls1) == 0 or len(ls2) == 0) and (len(ls3)!= 0):
	print(min(ls3))
elif len(ls3) == 0:
	print(min(ls1) + min(ls2))