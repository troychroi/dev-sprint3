# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name:

# ex. 8.1

def bkwd(word):
	index = len(word) - 1
	while index >= 0:
		letter = word[index]
		print letter
		index = index - 1
bkwd('love')
print '  '

# page 72 example
def fruite(word):
	for char in word:
		print char 
fruite('banana')

# ex. 8.2
def names():
	prefixes = 'JKLMNOPQ'
	suffix1 = 'ack'
	suffix2 = 'uack'
	for letter in prefixes:
		if (letter != 'O') and (letter != 'Q'):
			print letter + suffix1
		else:
			print letter + suffix2
names()



# ex. 8.5 

def count(word, char):
	count = 0
	for c in word:
		if char == c:
			count += 1
	return count
print count('plappy', 'p') 

# ex. 8.7

word = 'banana'
count = word.count('a')
print count 

# ex 8.8
word = 'kremey'
sans_k = word.strip('krem')
print sans_k
# what? I want it to print 'and' but instead it takes off the first 'a' as well as 'ale'. I tried several variations. nothing is consistent or predictable. 


# ex. 8.12
# self-created: 
def rotate_letter(letter, i):
	letter = ord(letter) + i
	letter_shift = chr(letter)
	letter = letter_shift
	return letter
print rotate_letter('c', 7)


# mimic solution from book: 
def rotate_word(word, i):
	res = ''
	for letter in word:
		res += rotate_letter(letter, i)
	return res
print rotate_word('cheer', 7)

# explain please? -- delete if you figure it out YOU













