def filterUniqueItems(l1 : list):
    l2 = []
    for i in l1:
        if i not in l2:
            l2.append(i)
    
    return l2


list1 = [1, 2, 2, 3, 4, 4, 5, 5]
list2 = filterUniqueItems(list1)

print(f"List with unique elements: {list2}")