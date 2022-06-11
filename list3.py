marks = [23, 45, 89, 90, 56, 80] 
#length = len(marks)
i= 0
total= 0
while i< len(marks):
    total= marks[i] + total
    i = i + 1
    print("Total Marks: "+str(total))