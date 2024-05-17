def read_even_length_strings(filename):
    with open(filename, 'r') as file:
        line = file.read()
        lines = line.split()
        even_length_strings = [line.strip() for line in lines if len(line.strip()) % 2 == 0]
    return even_length_strings


even_strings = read_even_length_strings('/doc.txt')
for string in even_strings:
    print(string)
