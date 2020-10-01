vowels = tuple('aeiou')

word = input("provide a word to check for vowels  ")


found = {}


for letter in word:
    if letter in vowels:
        #initalize letter in found
        found.setdefault(letter, 0)
        found[letter] += 1


for k,v in sorted(found.items()):
    print(f"{k} is found {v} times")

print(found)