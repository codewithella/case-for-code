#  Questão 5
def encontrar_colunas_poderosas(matriz):
    if not matriz or not matriz[0]:  # Verifica se a matriz é vazia
        return ([], [])
    
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    
    # Inicializa listas para soma e multiplicação
    soma = [0] * num_colunas
    mul = [1] * num_colunas
    
    # Calcula soma e multiplicação para cada coluna
    for j in range(num_colunas):
        for i in range(num_linhas):
            soma[j] += matriz[i][j]
            mul[j] *= matriz[i][j]
    
    # Encontra os valores máximos
    max_soma = max(soma)
    max_mul = max(mul)
    
    # Encontra os índices das colunas com soma e multiplicação máximas
    indices_soma = [i for i in range(num_colunas) if soma[i] == max_soma]
    indices_mul = [i for i in range(num_colunas) if mul[i] == max_mul]
    
    # Exibe os resultados
    print(f"Índice da coluna com maior soma: {indices_soma}")
    print(f"Índice da coluna com maior multiplicação: {indices_mul}")
    
    return (indices_soma, indices_mul)

# Exemplo de uso
matriz = [
    [1, 2, 3, 3],
    [4, 5, 6, 6],
    [7, 8, 9, 9]
]

resultado = encontrar_colunas_poderosas(matriz)
print("Saída:", resultado)
