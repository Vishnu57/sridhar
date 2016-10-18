str=["i am an indian", "this is an apple", "how do you kno that", "i am an indo", "i know that", "this is vishnu"]
l1=[]
l2=[]
for i in str:
	if i.startswith("i"):
		l1.append(i)
	if i.endswith("that"):
		l2.append(i)
print l1
print l2
		
