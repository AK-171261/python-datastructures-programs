'''
Ways to sort list of dictionaries by values in Python – Using lambda function/Using itemgetter
'''

lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

# Method-1
for obj in sorted(lis, key=lambda x: (x["age"], x["name"])):
    print(obj)
# {'name': 'Nikhil', 'age': 19}
# {'name': 'Manjeet', 'age': 20}
# {'name': 'Nandini', 'age': 20}

# Method-2
res = sorted(lis, key=lambda x: (x["age"], x["name"]))
print(res)
# [{'name': 'Nikhil', 'age': 19}, {'name': 'Manjeet', 'age': 20}, {'name': 'Nandini', 'age': 20}]

# Method-3
from operator import itemgetter

res = sorted(lis, key=itemgetter('age', 'name'), reverse=True)
print(res)
# [{'name': 'Nandini', 'age': 20}, {'name': 'Manjeet', 'age': 20}, {'name': 'Nikhil', 'age': 19}]


'''
Ways to sort dictionaries by values in Python – Using lambda function
'''
dict1 = {1: 1, 2: 9, 3: 4}
res = sorted(dict1.items(), key=lambda x: x[1])
print(res)
# [(1, 1), (3, 4), (2, 9)]
