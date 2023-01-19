import string
print("inserte la primera plabra a comparar")
anagrama1=input()
print("inserte la segunda plabra a comparar")
anagrama2=input()

if anagrama1==anagrama2:
    print("las palabras iguales no son un anagrama")

string1= list(anagrama1)
string2= list(anagrama2)
y = 0
if len(string1)==len(string2):

    for i in range(0,len(string1),1):

        for x in range(0,len(string1),1):
            if string1[i]== string2[x]:
                y=y+1
                break
                print(y)

if y == len(string1):
    print("son anagramas")
else:
    print("no son anagramas")    
print(string1)
print(string2)
  