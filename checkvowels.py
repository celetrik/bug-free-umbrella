vowels = list('aeiou')

word = input("provide a word to check for vowels  ")


found = {}


for letter in word:
    if letter in vowels:
        if letter not in found:
            #initalize letter in found dict
            found[letter] = 0
            #increase count of letter in dict
            found[letter] += 1
        else:
            # increase count only if letter already exists in found
            found[letter] += 1

for k,v in sorted(found.items()):
    print(f"{k} is found {v} times")

print(found)