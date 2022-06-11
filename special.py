# a=[4,8,17,8,19,23,19]
# >find the average of the odd numbers
# >find the sum of the even numbers
# >remove the duplicates
a=[4,8,17,8,19,23,19]
i=0
c=[]
while i<len(a):
    b=a[i]
    if b%2==0:
        c.append(b)
    else:
        pass    
        i=i+1
    # d=b/(len(c))
        print(c)