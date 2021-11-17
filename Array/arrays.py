from array import *
# array('type', [initialization])
arr1 = array('i', [1,2,3,4,5])

print(arr1)

# insert -> (index,val)
arr1.insert(5,7)
arr1.insert(0,0)
print(arr1)


#Traversal function -> O(N) complexity 
def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)

#Array element access
def accessElement(array, index):
    if index >= len(array):
        print('There is no element in this index')
    else:
        print(array[index])

accessElement(arr1, 6)

#Searching for an element in an Array -> Use array.index(value) to return index

def arraySearch(array, val):
    for i in array:
        if i == val:
            return print('Exists at the index =', array.index(val))

arraySearch(arr1, 7)

# Deleting an element from an array -> use array.remove(val)

arr1.remove(7)

print(arr1)

# 2D Array

import numpy as np

twoD = np.array([[11,15,20,24],[23,4,55,33],[2,66,42,76],[23,64,22,78]])
print(twoD)