# 1. Create an array and traverse
from array import *

def createArray(type, list):
    arr1 = array(type, list)
    return(arr1)

testarray = createArray('i',[2,4,6,8,10])

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(testarray)


# 2. Access individual elements through indexes
def indexElement(array,index):
    print(array[index])

indexElement(testarray, 3)

# 3. Append any value to the array using append() method
testarray.append(12)
print(testarray)

# 4. Insert value in an array using insert() method
testarray.insert(0,0)
print(testarray)

# 5. Extend python array using extend() method
testarray.extend([14,16,18,20])
print(testarray)

# 6. Add items from list into array using fromlist() method
testlist = [22,24,26,28,30]
testarray.fromlist(testlist)
print(testarray)

# 7. Remove any array element using remove() method
testarray.remove(0)
print(testarray)

# 8. Remove last array element using pop() method

#popping last element
testarray.pop()
print(testarray)

#popping ith element
testarray.pop(10)
print(testarray)

# 9. Fetch any element through its index using index() method
print(array.index(testarray, 20))

# 10. Reverse a python array using reverse() method
testarray.reverse()
print(testarray)

# 11. Get array buffer information through buffer_info() method
print(testarray.buffer_info())

# 12. Check for number of occurrences of an element using count() method
print(testarray.count(18))

# 13. Convert array to string using tostring() method
print(testarray.tobytes())

# 14. Convert array to a python list with same elements using tolist() method
print(testarray.tolist())

# 15. Append a string to char array using fromstring() method
# print(testarray.frombytes())
# 16. Slice Elements from an array
print(testarray[:6])