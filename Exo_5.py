n = int(input("Donner la valeur de n : "))
def factorielle(a):
    if a == 1 or a == 0:
        return 1
    else: 
         return a * factorielle(a-1)
print(factorielle(n))
