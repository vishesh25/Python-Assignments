def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return len(lines)

line_count = count_lines('/demo.txt')
print("Number of lines:", line_count)
