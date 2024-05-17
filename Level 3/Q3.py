def JtoI(filename):
    with open(filename, 'r') as file:
        content = file.read()
    corrected_content = content.replace('J', 'I').lower()
    print(corrected_content)

JtoI('/words.txt')
