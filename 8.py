import matplotlib.pyplot as plt
num1 = complex(2, -1)
num2 = complex(1, 1)
soma = num1 + num2
subtracao = num1 - num2
plt.figure(figsize=(8, 4))
plt.plot(num1.real, num1.imag, 'ro', label='(2, -1)')
plt.plot(num2.real, num2.imag, 'bo', label='(1, 1)')
plt.plot(soma.real, soma.imag, 'go', label='(3, 0)')
plt.plot(subtracao.real, subtracao.imag, 'yo', label='(1, -2)')
plt.xlim(-3, 4)
plt.ylim(-3, 3)
plt.grid(True)
plt.legend()
plt.show()