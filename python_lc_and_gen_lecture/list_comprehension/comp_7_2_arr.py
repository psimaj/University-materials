"""
since the expression in list comprehension syntax can be nearly anything it can also be an another list, maybe created using a list comprehension which allows us to create a 2-dimensional list in just one simple line
"""

a = [[i for i in range(j)] for j in range(4)]
print(a)
