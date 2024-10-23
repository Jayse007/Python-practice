import re

vowels = re.compile(r'[^aeiouAEIOU\s\n]')
consonants = vowels.findall("I hate futminna so much and do not see how I could have made such a mistake")
print(len(consonants))