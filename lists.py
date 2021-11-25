intlist = [1,2,3,4]
strlist = ['test','test2','test3']
print(intlist)
print(strlist)

#Accessing and Traversing
print(strlist[-1])

#traversing for strings
for i in strlist:
    print(i)

for i in range(len(strlist)):
    strlist[i] = strlist[i]+"+"
    print(strlist[i])


intlist.insert(0,11)

print(intlist)

intlist.append(44)
print(intlist)

intlist.extend([20,30,40,50])
print(intlist)

charlist = ['a','b','c','d','e','f']
#slicing - goes from 0 till the nth index but doesn't include it
print(charlist[:])
charlist[0:2] = ['x','y']
print(charlist[:])

#deleting elements in list -> provide index to delete the index element you want
charlist.pop()

# if we don't need removed value then we can just use delete()
del charlist[0]
print(charlist)
del charlist[0:2]
print(charlist)

#remove element using remove() directly
charlist.remove('d')
print(charlist)

# Searching for an element in the list -> in operator and linear search/searching algorithms
slist = [10,20,30,40,50,60,70,80,90]

if 0 in slist:
    print(slist.index(20))
else:
    print("Does not exist")

#Linear Search
def searchlist(list, val):
    for i in list:
        if i == val:
            return list.index(val)
    return 'No value'

print(searchlist(slist, 30))        


"""
List Operations / Functions
+ operator : concat lists
* operator : self-reptitive list 
len() to count elements in list -> gives total number of elements
max() to get max element in the list (int only)
min() to get min element in the list (int only)
sum() to get sum of elements in the list

to calculate avg() -> sum(list)/len(list)   
"""

# list() to convert strings to lists
a = 'spam'
b = list(a)
print(b)

#can use delimiter = '' with str.split(delimiter) to create a list
c = 'spam spam spam'
d = c.split()
print(d)

# to join list to string -> join()
e = 'spam-spam1-spam2'
delimiter = '-'
f = e.split(delimiter)
print(f)
print(delimiter.join(f))

myList = [2,4,3,1,5,7]

#common pitfall 1 - most list methods return none
#make copies of original list before running mylist.sort() since the original list is lost post sort - use sorted() for handling this
# myList = myList.sort()
myList.sort()
print(myList)