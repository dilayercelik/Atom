# demo.py

import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)

curved = uf.add_five(scores) #new list where each element is the element in the same index in the scores list, with 5 added added to its value
mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

#what is __name__ ?
print(__name__) #so you see this file is the '__main__' file (that's its 'name')
print(uf.__name__) #and the name of the imported script is useful_functions (which is not the main)

#import module 'math'
import math

print(math.factorial(4))    #output = should print 24 (in gith bash or terminal below)
