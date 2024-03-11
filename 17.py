def produto_cartesiano(matriz_1, matriz_2):
    linhas = len(matriz_1)
    linhas_m_2 = len(matriz_2)
    colunas = len(matriz_2[0])
    if (len(matriz_1[0]) != len(matriz_2)):
        return "não é possivel operar o produto"
    else:
        produto_cartesiano = []
        for i in range(linhas):
            linha = []
            for j in range(linhas_m_2):
                elemento = 0
                for k in range(colunas):
                    elemento += matriz_1[i][k]*matriz_2[j][k]
                linha.append(elemento)
            produto_cartesiano.append(linha)
        return produto_cartesiano

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

linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz_2 = []

print("Digite os elementos da linha")
for i in range (linhas):
    linha = []
    for j in range (colunas):
        elemento = int(input(f"Insira o elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz_2.append(linha)
    
print("O produto cartesiano será:")
for linha in produto_cartesiano(matriz_1, matriz_2):
    print(linha)
