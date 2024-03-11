def comparar_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return False

    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            if matriz1[i][j] != matriz2[i][j]:
                return False
    
    return True

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
    
if(comparar_matrizes(conjugada(matriz),transposta(matriz))):
    print("a matriz é hermitiana")
else:
    print("a matriz não é hermitiana")
