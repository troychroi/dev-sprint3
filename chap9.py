# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: 
 
# ex. 9.1

words = open('words.txt')
line = words.readline()

def long_words():
	for line in words:
		word = line.strip()
		if len(word) > 20:
			print word
long_words()
# ex. 9.2

def has_no_e(word):
	for letter in word:
		if letter == 'e':
			return False
	return True
print has_no_e('words')

# ex. 9.3

def avoids(word, forbidden):
	for letter in word:
		if letter in forbidden:
			return False
	return True
print avoids('love', 'h')

# ex 9.4

def use_only(word, available):
	for letter in word:
		if letter not in available:
			return False
	return True
print use_only('love', 'love')


