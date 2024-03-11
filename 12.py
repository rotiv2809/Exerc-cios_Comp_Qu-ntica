import matplotlib.pyplot as plt

c = input("Digite um numero complexo (no formato a+bj): ")
c = complex(c)

vector = []
x_axis = []
y_axis = []

# Inicializando as listas
for _ in range(11):
    vector.append(None)
    x_axis.append(None)
    y_axis.append(None)

for i in range(1, 11):
    vector[i] = c**i

for i in range(1, 11):
    x_axis[i] = vector[i].real

for i in range(1, 11):
    y_axis[i] = vector[i].imag

for i in range(1, 11):
    plt.plot([0, x_axis[i]], [0, y_axis[i]], label=f"c**{i}")

plt.title("Reta representando número complexo")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")
plt.legend()  # Adiciona uma legenda para indicar qual linha representa qual número

plt.tight_layout()

plt.show()
