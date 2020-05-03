f = open('C:/Users/Dilay Ercelik/Udacity/python/some_file.txt', 'r')
file_data = f.read()
f.close()

###

#files = []
#for i in range(10000):
    #files.append(open('some_file.txt', 'r'))
    #print(i) #output = 8188 -> max opening of files supported by my operating system

####

with open('C:/Users/Dilay Ercelik/Udacity/python/some_file.txt', 'r') as f:  #as 'string f'
    file_data = f.read()       #using the string method '.read()' on the STRING f
                              #no need to f.close() with the 'with' statement
print(file_data)

###

with open('C:/Users/Dilay Ercelik/Udacity/python/camelot.txt', 'r') as song:
    print(song.read(3))
    print(song.read(7))
    print(song.read())
