# Convert Character Matrix to single String;
# The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest
list=[['g','f','g'],['i', 's'],['b', 'e', 's', 't']]
list_1=['g','f','g']
list_2=['i', 's']
list_3=['b', 'e', 's', 't']
list_1.extend(list_2)
list_1.extend(list_3)
i=0
j=("")
while i<len(list_1):
    a=list_1[i]
    i+=1
    j=j+a
print(j)