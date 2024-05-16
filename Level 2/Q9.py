def access_element_at_index(lst, index):
    try:
        element = lst[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print(f"Index {index} is out of range.")

my_list = [10, 20, 30, 40, 50]

access_element_at_index(my_list, 2) 
access_element_at_index(my_list, 10)