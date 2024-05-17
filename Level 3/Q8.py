def parse_encoded_string(encoded):
    import re
    parts = re.split('0+', encoded)
    return {"first_name": parts[0], "last_name": parts[1], "id": parts[2]}

encoded_str = "Robert000Smith000123"
print(parse_encoded_string(encoded_str))
