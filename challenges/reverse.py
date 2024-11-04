import re


#The code is intended to take in a string as an argument
# reverse the order of the input string and at the same time 
# not affect the position of any symbol from the original string

def reverse(word: str) -> str: 
    reversed_word = ''
    symbols_dict = {}
    symbols = re.compile(r"\W+")
    symbols_list = symbols.findall(word)
    for letter in range(len(word)-1, -1, -1):
        if word[letter] in symbols_list:
            symbols_dict[letter] = word[letter]
            continue 
        reversed_word += word[letter]
    reversed_list = list(reversed_word)
    order = dict(sorted(symbols_dict.items()))

    for index, item in order.items():
        reversed_list.insert(index, item)

    reversed_word = ''.join(reversed_list)

    print(reversed_word)

word = "A-Br=CD=E+F"


reverse(word)        

#This was a question on turing platform.