a = [(x,y) for x in range(1,4) for y in range(4,7)]
print(a)

#this is effectively equivalent to:

a = []
for x in range(1, 4):
    for y in range(4, 7):
            a.append((x, y))

print(a)
#omitting the brackets shall produce an error
#a = [x, y for x in range(1, 4) for y in range(4, 7)]
