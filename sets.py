vowel = {'a', 'e', 'i', 'o', 'u'}

word = 'hello'


# union

u = vowel.union(set(word))
print(sorted(u))
# difference
d = vowel.difference(set(word))
print(sorted(d))
# intersect
i = vowel.intersection(set(word))
print(sorted(i))


