from itertools import permutations

def permutAtions(stri):
   
    permuted = permutations(stri)
    for perm in permuted:
        print(''.join(perm))


inputl = input("string: ")
print("Permutations:")
permutAtions(inputl)
