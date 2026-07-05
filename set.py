set={1,2,3,4,5}
set.add(6)
print(set)
set.remove(3)
print(set)
set.discard(10)  # does not raise an error if the element is not found
print(set)
set.clear()
print(set)
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

