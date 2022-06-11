# Binary to Decimal
bin=[1,0,0,1,1,0,1,1]
i=-1
j=0
b=0
sum=0
while i>(-len(bin)-1):
    a=bin[i]
    b=(a*(2**j))
    i=i-1
    j=j+1
    sum=sum+b
print(sum)
    