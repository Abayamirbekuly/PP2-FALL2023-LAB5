def chick(numheads, numlegs):
   
    chickens = 0
    rabbits = 0

    
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits

    
    return None


numheads = 35
numlegs = 94
solution = chick(numheads, numlegs)

if solution is not None:
    chickens, rabbits = solution
    print(chickens)
    print(rabbits)
else:
    print("No solution found.")
