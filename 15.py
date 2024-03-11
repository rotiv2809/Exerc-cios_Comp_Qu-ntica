def soma(vetor_1=[], vetor_2=[]):
    vetor_soma = []
    for i in range(len(vetor_1)):
        vetor_soma.append(vetor_1[i] + vetor_2[i])
    return vetor_soma

def inversa(vetor = []):
    vetor_inverso = []
    for i in range(len(vetor)):
        vetor_inverso.append(1/int(vetor[i]))
    return vetor_inverso

def escalar(vetor_1=[], vetor_2=[]):
    soma = 0
    for i in range(len(vetor_1)):
        soma += (vetor_1[i]*vetor_2[i])
    return soma





n = int(input("n = "))  # Convertendo para um número inteiro

vector = []
vector_2 = []

print("Digite os elementos do primeiro vetor:")
for _ in range(n):
    vector.append(int(input()))

print("\nDigite os elementos do segundo vetor:")
for _ in range(n):
    vector_2.append(int(input()))

print(f"soma = {soma(vector, vector_2)}")
print(f"inversa = {inversa(vector)}")
print(f"escalar = {escalar(vector, vector_2)}")
