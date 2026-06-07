
vowels = consonants = uppercase = lowercase = 0


with open('PARA.txt', 'r')as file:
    for line in file:
        for char in line:
            if char.isalpha():

                if char.isupper():
                    uppercase += 1
                else:
                    lowercase += 1


                if char.lower() in 'aeiou':
                    vowels += 1
                else:
                    consonants += 1

print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
print(f"Number of uppercase letters: {uppercase}")
print(f"Number of lowercase letters: {lowercase}")
