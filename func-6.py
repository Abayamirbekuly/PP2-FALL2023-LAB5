def reverse(string):
    
    words = string.split()

  
    reversedg = ' '.join(reversed(words))
    return reversedg


inputu = input(" sentence: ")
reversedg = reverse(inputu)
print("Reversed sentence:", reversedg)
