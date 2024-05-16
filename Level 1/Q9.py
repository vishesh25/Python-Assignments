input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]

freq = {}

for i in input_list:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

print(f"Frequency count: {freq}")