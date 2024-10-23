import re
def reverse(word):
    reversed_word = ''
    symbols_dict = {}
    symbols = re.compile(r"\W+")
    symbols_list = symbols.findall(word)
    for letter in range(len(word)-1, -1, -1):
        if word[letter] in symbols_list:
            symbols_dict[letter] = word[letter]
            reversed_word += ' '
            continue 
        reversed_word += word[letter]
    reversed_list = list(reversed_word)
    for index, item in symbols_dict.items():
        reversed_list[index] = item

    reversed_word = ''.join(reversed_list)

    print(reversed_word)

word = "A-Br=CD=E+F"


reverse(word)        
