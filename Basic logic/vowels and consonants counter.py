vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

words = input("Please type in a phrase\n")

vowel_count = 0 

for letter in words:
    if letter in vowel:
        vowel_count += 1

print(vowel_count)