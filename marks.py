#examination marks Telugu=54,English=12, science=65, fail marks are 30
#subject wise pass or not
a=input("enter the telugu marks:")
b=input("enter the english marks:")
c=input("enter the science marks:")
for i in a,b,c:
	if i>30:
		print "pass"
	elif i<30:
		print "fail"
print "telugu %s"%a
print "english %s"%b
print "science %s"%c
if (a+b+c>=60):
	print "pass"
else:
	print "fail"