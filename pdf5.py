# Count unique values inside a list.
# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 #because [1,2,5,8,4] are unique values.
list = [1, 2, 2, 5, 8, 4, 4, 8]
list.sort()
i=0
a=[]
while i<len(list):
    b=list[i]
    if b not in a:
        a.append(b)
    else:
        pass    
        i+=1
print('There are',len(a),'unique values in the list')