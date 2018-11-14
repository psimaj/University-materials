"""
contrary to how return behaves in function, one may have multiple consecutive yields
the following example is equivalent to big_powers(5) from the previous example
"""

def why_loop():
    yield 1
    yield 1
    yield 4
    yield 27
    yield 256

print(*why_loop())
