# List product excluding duplicates.
# List = [6,1,3,5,6,3,1]
# Output: 60
list = [6,1,3,5,6,3,1]
i=0
a=[]
p=1
while i<len(list):
    b=list[i]
    if b not in a:
        a.append(b)
        i=i+1
        p=p*b
        print(p)