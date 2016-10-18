#list=['one.py','two.py','three.py']
#output would be list=a1=['one.py','three.py']

list=['one.py','two.py','three.py']
a1=[]
for i in list:
	if i==list[0]:
		a1.append(i)
	if i==list[2]:
		a1.append(i)
print a1
		
