import time
from binary_search_tree import BSTNode
from lru_cache import LRUCache
import functools

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
#
duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# ORIGINAL runtime: 12.141798257827759 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# BINARY SEARCH TREE
bst = BSTNode(" ")
for name in names_1:  # O(n)
    bst.insert(name)  # O(n log n)

for name in names_2:   # O(n)
    if bst.contains(name):  # O(n log n)
        duplicates.append(name)  # O(1)
# New runtime: 0.26656484603881836 seconds
# O(n log n)
#
# for name in names_1:
#     LRUCache.put(key=1, value=0)
# for name in names_2:
#     if LRUCache.get:
#         LRUCache.put(key=2, value=0)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# PYTHON BUILT IN LIST FUNCTION
# list() Returns a list;  set()	Returns a new set object
STRETCH = list(set(names_1) & (set(names_2)))
# runtime: 0.010425090789794922 seconds

end_time = time.time()
print (f"{len(STRETCH)} STRETCH:\n\n{', '.join(STRETCH)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
