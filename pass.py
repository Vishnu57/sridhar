password = raw_input("enter a password")
c=0
for i in password:
    if (i=='1' or i=='2' or i=='3'):
        c=c+1
if (c>=2 and i=='@'):
        print " password is valid "
else:
    print "password is not valid"