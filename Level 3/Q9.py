def run_length_encode(input_string):
    if not input_string:
        return ""
    result = []
    last_char = input_string[0]
    count = 0
    for char in input_string:
        if char == last_char:
            count += 1
        else:
            result.append(f"{last_char}{count}")
            last_char = char
            count = 1
    result.append(f"{last_char}{count}") 
    return ''.join(result)


encoded_str = run_length_encode("wwwwaaadebbbbbw")
print(encoded_str)
