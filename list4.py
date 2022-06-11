marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
#list_length = len(student_marks)
i= 0
less_than50 = 0
while i < len(marks):
    mark = marks[i]
    if mark < 50:
        less_than50 = less_than50 + 1
    i = i+ 1
print("Marks less than 50: " + str(less_than50))