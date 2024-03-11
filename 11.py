import matplotlib.pyplot as plt

def multiplicacao_real(c, r):
    return c * r

c = input("Digite um numero complexo (no formato a+bj): ")
r = float(input("Digite um numero real: "))
c = complex(c)
m = multiplicacao_real(c, r)

# Extrair as partes real e imaginária dos números complexos
x1, y1 = c.real, c.imag
x2, y2 = m.real, m.imag

# Define os pontos para a primeira reta
x1_points = [0, x1]
y1_points = [0, y1]

# Define os pontos para a segunda reta
x2_points = [0, x2]
y2_points = [0, y2]


plt.plot(x2_points, y2_points, 'r-', label='número c*r')  # Plota a segunda reta em vermelho
plt.plot(x1_points, y1_points, 'b-', label='número c')  # Plota a primeira reta em azul

plt.title("Reta representando número complexo e sua multiplicação por um número real")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")
plt.legend()  # Adiciona uma legenda para indicar qual linha representa qual número

plt.tight_layout()

plt.show()
