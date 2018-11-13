def why_loop():
    yield 1
    yield 1
    yield 4
    yield 27
    yield 256

print(*why_loop())
