c1 = input("Forneça o primeiro número complexo: ")
c1 = complex(c1)
c2 = input("Forneça o segundo número complexo: ")
c2 = complex(c2)
c3 = input("Forneça o terceiro número complexo: ")
c3 = complex(c3)

print("Item a")
if(c1 + c2 == c2 + c1):
    print("Ocorre a comutatividade")
if(c1 * c2 == c2 * c1):
    print("Ocorre a comutatividade")
print("Item b")
if((c1+c2)+c3 == c1+(c2+c3)):
    print("Ocorre a comutatividade")
if((c1*c2)*c3 == c1*(c2*c3)):
    print("Ocorre a comutatividade")
print("Item c")
if(c1 * (c2+c3) == (c1*c2) + (c1*c3)):
    print("Ocorre a distributividade")