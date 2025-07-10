#Sets

my_set = {1, 2, 3, 4, 5}

print(my_set)

# Adding an item to the set
my_set.add(6)
print(my_set)

# Removing an item from the set
my_set.remove(3)
print(my_set)

# adding multiple items to the set

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
union_set = set1.union(set2)
print(union_set)

# Intersection 
inter_set = set1.intersection(set2)
print(inter_set)

# Difference
diff_set = set1.difference(set2)
print(diff_set)