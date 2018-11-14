"""
using nearly the same syntax as in list comprehension (the only difference is the type of brackets), one may create generator expressions
"""

def simple_gen(n):
    for i in range(1, n+1):
        yield i**3

n = 6

simple_gen_comp = (i**3 for i in range(1, n+1))
simple_list_comp = [i**3 for i in range(1, n+1)]

"""
in comparison to list comprehension, generator expressions are lazy which makes them considerably more memory efficient
one may access their elements in the same ways as normal generators
"""

simple_gen_inst = simple_gen(n)

print(type(simple_gen_comp))
print(*simple_gen_comp)

"""
we can see that according to the type, simple_gen_comp is simply a generator
"""

print(type(simple_list_comp))
print(*simple_list_comp)

print(type(simple_gen_inst))
print(*simple_gen_inst)
