print("Item a:")
print(1j**2)
print(1j**3)
print(1j**4)
print(1j**5)

def j_equivalente(a):
    if(a%4 == 0):
        return 1
    elif(a%4 == 1):
        return 1j
    elif(a%4 == 2):
        return -1
    elif(a%4 == 3):
        return -1j

print("Item b")
a = input("Escreva a potência de j: ")
a = int(a)
print(f"j^^{a} é equivalente a {j_equivalente(a)}")
