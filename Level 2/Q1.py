l1 = [1, 2, 3, 4, 5] 
l2 =  [4, 5, 6, 7, 8]

l3 = []

for i in l1:
    if i in l2:
        l3.append(i)

print(f"Common items: {l3}")