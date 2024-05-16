def find_median(number_list):
    number_list.sort()
    n = len(number_list)
    mid = n // 2

    if n % 2 == 0:
        median = (number_list[mid - 1] + number_list[mid]) / 2
    else:
        median = number_list[mid]

    return median

number_list = [7, 2, 5, 1, 9, 3]
median = find_median(number_list)
print(f"Median: {median}")