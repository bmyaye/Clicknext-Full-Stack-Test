# no.2 check two words

# s = input("Enter two words: ").split()
# s1 = s[0].lower()
# s2 = s[1].lower()

s1 = input("Enter the first word: ").lower()
s2 = input("Enter the second word: ").lower()

word1 = {}
word2 = {}

for letter in s1:
    if letter in word1:
        word1[letter] += 1
    else:
        word1[letter] = 1

for letter in s2:
    if letter in word2:
        word2[letter] += 1
    else:
        word2[letter] = 1

if word1 == word2:
    print('true')
else:
    print('false')
