#identify the lis in question
# Simple_logic = ['logic1', 'logic2', 'logic3', 'logic4']

# print(Simple_logic[:3])

'''  
this should return the following
['logic1', 'logic2', 'logic3']

'''
# print(Simple_logic[0:3])

'''  
this should return the following
['logic1', 'logic2', 'logic3']

'''

# print(Simple_logic[:-2])

'''  
this should return the following
['logic1', 'logic2']

'''

# *******************
'''
* Lists are used to store multiple items in a single variable and are created using square brackets.
* List items are ordered, changeable, and allow duplicate values.

* List items are indexed, the first item has index [0], the second item has index [1] etc.
* When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

* If you add new items to a list, the new items will be placed at the end of the list
* The list is changeable, meaning that we can change, add, and remove items in a list after it has been created
* Since lists are indexed, lists can have items with the same value
* To determine how many items a list has, use the len() function e.g print(len(Simple_logic))

* List items can be of any data type
* Negative indexing means start from the end

* You can specify a range of indexes by specifying where to start and where to end the range.

* When specifying a range, the return value will be a new list with the specified items.  e.g print(Simple_logic[2:3]) The search will start at index 2 (included) and end at index 3 (not included) By leaving out the end value, the range will go on to the end of the list.
* Remember that the first item has index 0 
* Specify negative indexes if you want to start the search from the end of the list 
* print(Simple_logic[-1:-2]) This example returns the items from  (-2) to the end, but NOT including (-1)
'''
'''Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
'''

'''
**** A billion dollar question.****

Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list


list1 = [54, 44, 27, 79, 91, 41]


'''

'''
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)


'''

''' 
Slice list into 3 equal chunks and reverse each chunk


sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]


# your answer should look like this

Chunk  1 [11, 45, 8]
After reversing it  [8, 45, 11]
Chunk  2 [23, 14, 12]
After reversing it  [12, 14, 23]
Chunk  3 [78, 45, 89]
After reversing it  [89, 45, 78]
'''

'''


'''



sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sample_list)

length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times
for i in range(3):
    # get indexes
    indexes = slice(start, end)
    
    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)
    
    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size


