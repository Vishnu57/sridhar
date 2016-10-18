list=['a.txt','b.py','c.txt','d.mp3','e.py','f.mp3']
l1=[]
l2=[]
l3=[]
for i in list:
	if i.endswith('.txt'):
		l1.append(i)
	elif i.endswith(".py"):
		l2.append(i)
	elif i.endswith(".mp3"):
		l3.append(i)
print "l1 %s "%l1
print "l2 %s "%l2
print "l3 %s "%l3
