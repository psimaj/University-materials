"""
instead of first receiving a value from yield inside and then yielding something to the oustide, we can do it in just one expression
note that like in every assignment, the right-hand side is evaluated first, which means that the value yielded outside shall use the old value of 'x', and only then will 'x' be assigned a new value
"""

def natural_convolution():
    i = 0
    x = 1
    while True:
        x = yield i * x

        """
        yield yields the value outside first
        and returns a value inside
        """

        i += 1

a = natural_convolution()

"""
the generator needs to be started before being sent anything
"""

next(a)

"""
after calling next, the generator waits on the first yield
"""

for i in range(1, 10):
    print(a.send(i))

    """
    the generator immediately yields the next value after receiving send
    there's only one yield, so no need to call next
    """
