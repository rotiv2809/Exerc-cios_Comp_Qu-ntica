c1 = input("Forneça o primeiro número complexo: ")
c1 = complex(c1)
c2 = input("Forneça o segundo número complexo: ")
c2 = complex(c2)

if(c1.conjugate()+c2.conjugate() == (c1+c2).conjugate()):
    print("A soma dos conjugados é o conjugado da soma")
if(c1.conjugate()*c2.conjugate() == (c1*c2).conjugate()):
    print("O produto dos conjugados é o conjugado dos produtos")
