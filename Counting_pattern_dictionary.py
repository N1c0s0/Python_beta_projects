counts = dict()
##Se crea el diccionario counts
print("Enter a line of text: ")
line = input("")
words = line.split()
##se crea la lista words dividiendo el texto con espacios
print("words: ", words)
print("Counting... ")
for word in words:
    ##se recorre la lista words, el contador es word
    counts[word] = counts.get(word,0) + 1
    ##get checks if a key is already in a dictionary with default value 0
print("Counts",counts)    
