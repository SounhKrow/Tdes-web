"""
#1
def soma_lista(lista):
    return sum(lista)
"""
"""
#2
def maior_valor(lista):
    return max(lista)
"""
"""
#3
def media(lista):
    return sum(lista) / len(lista)
num = []
qtd = int(input("Quantos números deseja digitar? "))
for i in range(qtd):
    valor = float(input(f"Digite o {i+1}º número: "))
    num.append(valor)

print("Lista digitada:", num)
print("Média:", media(num))
"""
"""
#4
def numeros_pares(lista):
    return [n for n in lista if n % 2 == 0]
"""
"""
#5
def contar_elementos(lista):
    print("Quantidade total de elementos:", len(lista))
    print("Maior valor:", max(lista))
    print("Menor valor:", min(lista))
"""
"""
#6
aluno = {
    "nome": "Kaleo Lemos",
    "idade": 20,
    "curso": "Ciência da Computação",
    "nota_final": 10 #;) 
}

print("Dados do aluno:")
print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Curso:", aluno["curso"])
print("Nota final:", aluno["nota_final"])
"""
"""
#7
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 7.0},
    {"nome": "Carla", "nota": 9.2}
]

print("Alunos cadastrados:")
for aluno in alunos:
    print(f"Nome: {aluno['nome']} - Nota: {aluno['nota']}")
"""
"""
#8
def media_turma(alunos):
    soma_notas = sum(aluno["nota"] for aluno in alunos)
    return soma_notas / len(alunos)

alunos = [
    {"nome": "Kaleo", "nota": 7.6},
    {"nome": "Rafael", "nota": 8.9},
    {"nome": "Julia", "nota": 5.1}
]

print("Média da turma:", media_turma(alunos))
"""
"""
#9
def prodmcaro(produtos):
    maiscaro = max(produtos, key=produtos.get)
    print(f"O produto mais caro é '{maiscaro}' custando R$ {produtos[maiscaro]}")

produtos = {
    "arroz": 25,
    "feijão": 10,
    "macarrão": 8
}

prodmcaro(produtos)
"""
"""
#10
def estoque(produtos):
    for produto, quantidade in produtos.items():
        print(f"Produto: {produto} - Quantidade: {quantidade}")

produtos = {
    "caneta": 10,
    "caderno": 5,
    "borracha": 7
}

estoque(produtos)
"""
"""
#11
def maior_numero(*args):
    return max(args)
"""
"""
#12
def mostrar_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
"""
