a = [(x,y) for x in range(1,4) if x != 2 for y in range(4,7) if x + y != 7 if y != 2*x]
print(a)

#this is effectively equivalent to:

a = []
for x in range(1, 4):
    if x != 2:
        for y in range(4, 7):
            if x + y != 7 and y != 2*x:
                a.append((x, y))

print(a)
#omitting the brackets shall produce an error
#a = [x, y for x in range(1, 4) for y in range(4, 7)]
