import re

sub_test = re.compile(r'Mr\.(\w)(\w*)')
sub_output = sub_test.sub(r'\1','Mr.James and his friend Teddy have been having an argument that has not ended since the beginning of the year. Mr.Joshua who thought he could settle their dispute just became a casualty.')
print(sub_output)


test = re.compile(r'Bat(man|woman)')
search = test.search('The Batwoman has been causing us trouble')
print(search.group())

vowel = re.compile(r'[aeiou]{3}')
search = vowel.findall('this is to test whether there are vowels in a row with one character class. Haier is good isn\'t it')
print(search)