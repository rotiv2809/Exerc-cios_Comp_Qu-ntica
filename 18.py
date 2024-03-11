def traco(matriz):
    linhas = len(matriz)
    if (matriz == [] or len(matriz) != len(matriz[0])):
        return 0
    else:
        elemento = 0
        for i in range(linhas):
            elemento += matriz[i][i]
        return elemento

linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz_1 = []

print("Digite os elementos da linha")
for i in range (linhas):
    linha = []
    for j in range (colunas):
        elemento = int(input(f"Insira o elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz_1.append(linha)
    
print(f"O traço será: {traco(matriz_1)}")
