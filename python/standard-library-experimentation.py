#experimentation with some modules of the standard library (basics)

#"math" module: exp() function

#print e to the power of 3 using the math module
import math

answer = math.exp(3)

print(answer)       #prints e**3

###################

#"random" module: choice() function

#generate a random password
# Use an import statement at the top
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces
def generate_password():
    password = random.choice(word_list) + random.choice(word_list) + random.choice(word_list) #using 3 times the function choice() from the random module to choose randomly 3 words from the list of words 'word_list'
    return password

# test your function
print(generate_password())
