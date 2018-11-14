"""
in its full glory, the list comprehension syntax also allows ifs in between the fors:
[expr for i_1 in it_1 if c_11 ... if c_k1 ... for i_n in it_n if c_1n ... if c_kn]
where the i-th set of ifs is nested between the i-th and (i+1)-th for
"""

a = [(x,y) for x in range(1,4) if x != 2 for y in range(4,7) if x + y != 7 if y != 2*x]
print(a)

"""
shall produce the same results as:
"""

a = []
for x in range(1, 4):
    if x != 2:
        for y in range(4, 7):
            if x + y != 7 and y != 2*x:
                a.append((x, y))
print(a)
