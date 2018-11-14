"""
return is equivalent to raising StopIteration
return value is the message carried by the exception
"""

def why_loop():
    yield 1
    yield 1
    yield 4
    return 'MPZS'
    yield 27
    yield 256

a = why_loop()
for i in range(5):
    print(next(a))
