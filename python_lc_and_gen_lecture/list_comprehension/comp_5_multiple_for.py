"""
not only can we use multiple ifs, but also multiple fors:
[expr for i_1 in it_1 ... for i_n in it_n if c_1 ... if c_k]
where each following for is nested in the previous one
"""

a = [(x,y) for x in range(1,4) for y in range(4,7)]
print(a)

"""
shall produce the same results as:
"""

a = []
for x in range(1, 4):
    for y in range(4, 7):
            a.append((x, y))
print(a)

"""
omitting the brackets when the expression is a tuple shall produce an error
"""
#a = [x, y for x in range(1, 4) for y in range(4, 7)]
