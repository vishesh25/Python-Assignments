arr = [1, 2, 3, 4, 5]
k = 6

def find_pairs_with_sum(num, key):
    pairs = []
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == key:
                pairs.append((num[i], num[j]))
    return pairs

result = find_pairs_with_sum(arr, k)
count = len(result)
print("Count of pairs with sum equal to", k, ":", count)