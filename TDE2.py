"""
#1
dados = (19, 1.70, "Peter Parker", True)

print(dados[1])
print(dados[3])
dados[0] = 30
#TypeError: 'tuple' object does not support item assignment
#Explicação: tuplas em python depois de criadas, não podem ser alterados
"""
"""
#2
tupla = (1, 2, 2, 3, 2)
def contar_ocorrencias(t, valor):
    return t.count(valor)
  
print("Qtd de 2:", contar_ocorrencias(tupla, 2))
"""
"""
#3
numeros = [10, 20, 30, 40, 50]
numeros.append(100)
numeros.pop(2)
numeros[0] = 500

print(numeros)
"""
"""
#4
notas = [7.5, 8.0, 6.5, 9.0, 10.0]
soma = sum(notas)
media = soma / len(notas)

print("Soma das notas:", soma)
print("Média das notas:", media)
"""
"""
#5
num = [15, 3, 22, 8, 45, 6, 11, 2]
cre = sorted(num)
decre = sorted(num, reverse=True)
mq10 = [n for n in num if n > 10]

print("Ordem crescente:", cre)
print("Ordem decrescente:", decre)
print("Números maiores que 10:", maq10)
"""
"""
#6
notas = [[7, 8, 9, 6], [6, 5, 8, 7], [10, 9, 8, 9]]
print("Nota do 2º aluno na 3ª disciplina:", notas[1][2])
medias = []

for i, notas_aluno in enumerate(notas):
    media = sum(notas_aluno) / len(notas_aluno)
    medias.append(media)
    print(f"Média do aluno {i+1}: {media:.2f}")
  
maior_media = max(medias)
aluno_maior_media = medias.index(maior_media) + 1
print(f"O aluno {aluno_maior_media} teve a maior média ({maior_media:.2f})")
"""
"""
#7
vals = []

for i in range(4):
    val = int(input(f"Digite o {i+1}º valor: "))
    vals.append(val)

qtd_nove = vals.count(9)
print("Quantidade de vezes que apareceu o 9:", qtd_nove)

if 3 in vals:
    posicao = vals.index(3)
    print("O primeiro valor 3 foi digitado na posição:", posicao)
else:
    print("O valor 3 não foi digitado")

pares = [v for v in vals if v % 2 == 0]
print("Números pares digitados:", pares)
"""
"""
#8
import random

dado = [random.randint(1, 6) for _ in range(50)]
qtd6 = dado.count(6)
percentual = (qtd6 / 50) * 100

print("Lançamentos:", dado)
print(f"A face 6 saiu {qtd6} vezes")
print(f"Percentual de ocorrências da face 6: {percentual:.2f}%")
""""
