def stone_piles(n):
    # If n is even, start from 2 and increment by 2
    # If n is odd, start from 1 and increment by 2
    stones = []
    start = 2 if n % 2 == 0 else 1
    for i in range(start, n, 2):
        stones.append(i)
    return stones

n = 7
result = stone_piles(n)
print(f"Stones in each pile = {result}")

n = 8
result = stone_piles(n)
print(f"Stones in each pile = {result}")
