c1 = input("Forneça o primeiro número complexo: ")
c1 = complex(c1)
c2 = input("Forneça o segundo número complexo: ")
c2 = complex(c2)

def modulo_complexos(a,b):
    return (a**2 +b**2)**0.5

mod_c1 = modulo_complexos(c1.real,c1.imag)
mod_c2 = modulo_complexos(c2.real,c2.imag)
mod_c1_c2 = modulo_complexos((c1*c2).real, (c1*c2).imag)
mod_c1_mais_c2 = modulo_complexos((c1+c2).real, (c1+c2).imag)

if(round(mod_c1*mod_c2,3) == round(mod_c1_c2,3)):
    print("O produto dos módulos e o módulo dos produtos")
if(mod_c1_mais_c2 <= mod_c1 + mod_c2):
    print("A desigualdade triangular foi obedecida")
