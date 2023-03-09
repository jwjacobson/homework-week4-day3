#!/usr/bin/python
# Exercise 1: reverse the list
test = ['this' , 'is', 'a', 'sentence', '.']

def swap(arr, a, b, c, d):
    arr[a], arr[d] = arr[d], arr[a]
    arr[b], arr[c] = arr[c], arr[b]
    return arr

print(swap(test, 0, 1, 3, 4))

# Exercise 2: count the words, store in dict with frequencies as values
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

words = []
counts = []

for word in a_text.split():
    if word not in words:
        words.append(word)
        counts.append(a_text.split().count(word))
answer_dict = dict(zip(words, counts))
print(answer_dict)

# Exercise 3: implement a linear search algorithm
nums_list = [10,23,45,70,11,15]
nums_list2 = [10,23,45,11,1510,23,70,45,11,15]

def linear_search(arr, target):
    for element in arr:
        if element == target:
            return arr.index(element)
    return -1                            

print(linear_search(nums_list, 70))
print(linear_search(nums_list2, 80))    # example where target is not in list

