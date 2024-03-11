def transposta(matriz):
    if not matriz:
        return []
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    transposta = []
    
    for j in range(colunas):
        linha = []
        for i in range(linhas):
            elemento = matriz[i][j]
            linha.append(elemento)
        transposta.append(linha)
    
    return transposta

def conjugada(matriz):
    if not matriz:
        return []
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    conjugada = []
    
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elemento = matriz[i][j].conjugate()
            linha.append(elemento)
        conjugada.append(linha)
    return conjugada    

linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz = []

print("Digite os elementos da linha")
for i in range (linhas):
    linha = []
    for j in range (colunas):
        elemento = complex(input(f"Insira o elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)
    
print("A matriz transposta será:")

for i in range(len(transposta(matriz))):
    print(transposta(matriz)[i])

print("A matriz conjugada será:")
for linha in conjugada(matriz):
    print(linha)
    
print("A matriz dagger será:")
for linha in transposta(conjugada(matriz)):
    print(linha)
