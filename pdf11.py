# For example, if we give 9119 the function should return 811181, 
# as the square of 9 is 81 and square of 1 is 1.
a='9119'
b=list(a)
i=0
d=0
while i<len(b):
    c=b[i]
    e=int(c)
    d=(e**2)
    i=i+1
    print(d,end="")