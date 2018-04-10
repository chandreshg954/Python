for _ in range(int(input())):
	m = 1000000007
	n,w = [int(x) for x in input().split()]
	if w>8 or w<-9 :
		print(0)
	else :
		if w>=0 :
			p = 9-w
		else :
			p = 10+w
		print((p*pow(10 , n-2 , m))%m)
