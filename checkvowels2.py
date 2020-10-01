#compare the inputed word to the vowel set to get the vowels in the word
vowel = set(('a,e,i,o,u'))
word = input('enter a word ')

intersect = vowel.intersection(set(word))
print(intersect)