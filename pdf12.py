# You will be given a number and you need to return it as a string in Expanded Form. 
# For example:
# 12 # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304 # Should return '70000 + 300 + 4'
a="12"
b=len(a)
# i=0
# while i<b:
if b==1:
    print(b)
elif b==2:
    print(a[0]+'0 +',a[1]) 
elif b==3:
    print(a[0]+"00 +",a[1]+"0 +",a[2])       
else:
    pass    