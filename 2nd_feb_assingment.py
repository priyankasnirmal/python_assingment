A = (1,2,3,4,5)
print(A.count(1))
print(A.count(2))

print(A.index(3))

#Python Tuple is a collection of objects separated by commas. In some ways, a tuple is similar to a list in terms of indexing, nested objects, and repetition but a tuple is immutable, unlike lists which are mutable.


List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
print(set(List))
A1 = {1,2,3,4}
A2 = {4,5,6,7}
A3 = {1,2,5,6}

print(A1.union(A2))

print(A1.union(A2,A3))

print(A1.union(A2).union(A3))

print(A1.union(A2.union(A3)))

A4 = A1.union(A2.union(A3))
print(A4)

A5 = {67}
A4.update(A5)
print(A4)
print(A5)

d={}
d["F"] = "fish"
d["F"] = "fish"
d["D"] = "dog"
d["A"] = "apple"
d["C"] = "cat"
d["P"] = "pen"
 
print(d)
# The dictionary is an unordered collection that contains key:value pairs separated by commas inside curly brackets. Dictionaries are optimized to retrieve values when the key is known.

d1 = {i:i*3 for i in range(1,5)}
  
print(d1)
  

dict1 = {'Sport': 'Cricket', 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}

keys_view = dict1.keys()
values_view = dict1.values()
items_view = dict1.items()

print("Keys view:", keys_view)
print("Values view:", values_view)
print("Items view:", items_view)

###
dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}
dict1.setdefault('topic',['Python', 'Machine Learning','Deep Learning'])
print(dict1)
