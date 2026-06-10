import itertools
letters = ['A', 'B', 'C']

# Permutations (Order matters)
print(list(itertools.permutations(letters, 2))) # in place of 2 you replace with 3 then o/p [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
# itertool method make list or tuple then call into list() or tupple method
# Output: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# Combinations (Order doesn't matter)
print(list(itertools.combinations(letters, 2)))# same 2 replace 3 then change behaviour
# Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]
#=====================

# chain(): Combine multiple collections seamlessly
numbers = [1, 2]
words = ['x', 'y']
print(list(itertools.chain(numbers, words)))
# Output: [1, 2, 'x', 'y']

# accumulate(): Running totals
print(list(itertools.accumulate([1, 2, 3, 4])))
# Output: [1, 3, 6, 10] # (1, 1+2, 1+2+3, 1+2+3+4) we can make it

#==========================
# count(): Endless counter
for i in itertools.count(start=10, step=5):
    if i > 25:
        break
    print(i, end=" ")
# Output: 10 15 20 25
