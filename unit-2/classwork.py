classmates = ["Ross", "Marcus", "Flavio", "Joseph",
            "Maham", "Vinay", "Gungeet", "Faris"]

'''
#print number of items in list
print(len(classmates))

#print the first item in list
print(classmates[0])

#starts from 0 from beginning or -1 from behind

#print the last element in list
print(classmates[-1])

#adds element to list
#classmates.append("John")
#print(classmates[-1])

#inserts element in list
#classmates.insert(1, "Jane")
#print(classmates[1])

#remove element from end of list
classmates.pop()

#remove element somewhere in list
classmates.pop(2)

#remove element form end of list
#classmates.pop(-1)
'''

#print all elements in list
for name in classmates:
    print(name)

'''
#search for an item in list
for name in classmates:
    if name == "Faris":
        print("Faris found in list")

#or

if "Faris" in classmates:
    print("Found Faris in list")
'''

#using indices in for loop
for idx, name in enumerate(classmates):
    print(idx, name)

name = "Princeton"

'''
#print name in reverse
for x in range(len(name)- 1, -1, -1):
    print(name[x])
'''
#or shortest way :)
print(name[::-1])
print(name[1:3:2])