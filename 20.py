def is_identity(matriz1):
    if (len(matriz1) != len(matriz1[0])):
        return False

    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            if (i == j):
                if matriz1[i][j] != 1:
                    return False
            else:
                if matriz1[i][j] != 0:
                    return False
    
    return True

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

matriz_1 = []

print("Digite os elementos da linha")
for i in range (linhas):
    linha = []
    for j in range (colunas):
        elemento = int(input(f"Insira o elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz_1.append(linha)
    
if is_identity(produto_cartesiano(matriz_1,transposta(conjugada(matriz_1)))) and is_identity(produto_cartesiano(transposta(conjugada(matriz_1)),matriz_1)):
    print("É unitária")
else:
    print("Não é unitária")
