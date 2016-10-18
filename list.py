#we have one list and output would be single[1,5,6,8] double[23,34,46]
list=[1,342,23,6,324,98734,8,765,46,5]
single=[]
double=[]
triple=[]
for i in list:
	if i<10:
		single.append(i)
	elif i<99:
		double.append(i)
	elif i<999:
		triple.append(i)
print "Single %s"%single
print "double %s"%double
print "triple %s"%triple
	