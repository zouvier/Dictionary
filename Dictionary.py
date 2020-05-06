# needed Modules. must pip install spellchecker
import json
import sys
from spellchecker import SpellChecker

# initialized dictionary data file  into dictionary, along with the spell check module
dictionary = json.load(open("data.json"))
spelling = SpellChecker()
# keeps track of the dictionary number
definition_number = 1

# main search function

def search(word):
	global definition_number
	# checks to see if the word is in the dictionary, if not it uses spell check to find a better fit ~
	# ~ recursion is then used to return values and ask if the user wants to continue
	if word.upper() in dictionary:
		for item in dictionary[word]:
			print('definition ' + str(definition_number) + ': '+item)
			definition_number += 1
		definition_number = 1
		question = input('Would you like to enter another word? \n Y/N: ')
		if question.lower() == 'y':
			return beginning()
		else:
			sys.exit('Exiting Program')
	word = word.lower()
	if word in dictionary:
		print(word + ': ')
		for item in dictionary[word]:
			print('definition ' + str(definition_number) + ': '+item)
			definition_number += 1
		definition_number = 1
		question = input('Would you like to enter another word? \n Y/N: ')
		if question.lower() == 'y':
			return beginning()
		else:
			sys.exit('Exiting Program')
	elif word not in dictionary:
		word = spelling.correction(word)
		print("This word does not exist, did you mean: " + word)
		question = input('Y/N: ')
		if question.lower() == 'y':
			return search(word)
		else:
			question = input('Would you like to continue? Y/N: ')
			if question.lower() == 'y':
				return beginning()
			else:
				sys.exit('Exiting program')

# beginning function
def beginning():
	user_word = input("Enter a word: ")

	print(search(user_word))

# calls the function and executes the code
beginning()
