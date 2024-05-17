def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return len(lines)

line_count = count_lines('C:/Workspace/Python Assignments/Level 3/demo.txt')
print("Number of lines:", line_count)
