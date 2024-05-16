def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count


string = "Hello, World!"
vowel_count = count_vowels(string)
print(f"Number of vowels: {vowel_count}")