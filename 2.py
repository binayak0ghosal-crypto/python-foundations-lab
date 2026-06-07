def analyze_string(s):
    vowels = 'aeiouAEIOU'
    alphabet_count = 0
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    space_count = 0
    other_count = 0

    for char in s:
        if char.isalpha():
            alphabet_count += 1
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1

    print("\nString Analysis:")
    print("Alphabets     :", alphabet_count)
    print("  Vowels      :", vowel_count)
    print("  Consonants  :", consonant_count)
    print("Digits        :", digit_count)
    print("Spaces        :", space_count)
    print("Other Characters:", other_count)

# Get string input from user
input_string = input("Enter a string: ")
analyze_string(input_string)
