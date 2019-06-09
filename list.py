#!/usr/bin/python3

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
c=iter(adhoc)
a=[]
b=[]
for i in c :
	if (i>5) :
		a.append(i)
	elif (i<=2) :
		b.append(i)
else :
	print(a)
	print(b)
	



