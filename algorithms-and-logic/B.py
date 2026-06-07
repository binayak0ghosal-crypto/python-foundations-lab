def d_C(user_input,character):
    return user_input.replace(character,'')

user_input=input("Enter a string")
character=input("Which character do u wanna delete?")
new_string= d_C(user_input,character)
print(new_string)
