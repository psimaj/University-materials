"""
it's important to note that while the result of a list comprehension and a semantically equivalent for loop might be indentical, they aren't fully quivalent pieces of code
"""

a = [i for i in range(10)]

"""
name 'i' is not defined in the global scope referencing it shall produce an error
"""
#print(i)


a = []
for i in range(10):
    a.append(i)

print(i)

"""
name 'i' will be defined which is just one of the differences
the following also doesn't work:
"""
#b = [0 if i == 0 else b[i-1] for i in range(10)]
"""
the list is first fully evaluated and the name 'b' starts referencing it after it's fully built, while we can do the following using a normal for loop:
"""

b = []
for i in range(10):
    b.append(0 if i == 0 else b[i-1])
