#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

a=range(1501,2701)
b=[]
for i in a:
	if (i%7==0)and (i%5==0):
		b.append(i)
print b