def rotate_right(arr, D):
    N = len(arr)
    D = D % N
    return arr[-D:] + arr[:-D]

arr = [1, 2, 3, 4, 5]
D = 2
rotated_arr = rotate_right(arr, D)
print("arr after rotation =", rotated_arr)