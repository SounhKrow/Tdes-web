"""
#1
num = float(input("Digite um número: "))

if num > 0:
    print("O número é Positivo")
elif num < 0:
    print("O número é Negativo")
else:
    print("O número é Zero")
"""
"""
#2
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite o último número: "))
maiornum = 0

if num1 >= num2 and num1 > num3:
    maiornum = num1
elif num2 >= num1 and num2 > num3:
    maiornum = num2
else:
    maiornum = num3
print(f"O maior número é: {maiornum}")
"""
"""
#3
ano = int(input("Digite um ano: "))
biano = 0

if ano % 4 == 0 and ano % 100 != 0:
    biano = ano
    print(f"O ano {biano} é bisexto")
elif ano %400 == 0:
    biano = ano
    print(f"O ano {biano} é bisexto")
else:
    print("Isso não é um ano bisexto")
"""
"""
#4
valorP = float(input("Digite o valor do produto: "))
valorD = float

if valorP > 100:
    valorD = (valorP - (valorP * 0.10))
    print(f"O valor {valorP} recebe 10% de desconto: {valorD:.2f}")
elif 100 > valorP > 50:
    valorD = (valorP - (valorP * 0.05))
    print(f"O valor {valorP} recebe 5% de desconto: {valorD:.2f}")
else:
    print("Não tem desconto.")
"""
"""
#5
num = int(input("Digite um número: "))

if num > 0:
    print("O número é positivo")
if num % 2 == 0 or num == 0:
    print("O número é par")
"""
"""
#6
l1 = int(input("Digite o primeiro lado: "))
l2 = int(input("Digite o segundo lado: "))
l3 = int(input("Digite o terceiro lado: "))

if l1 == l2 and l2 == l3 and l1 == l3:
    print("Esse triangulo é Equilátero")
elif l1 == l2 and l1 != l3 and l2 != l3 or l1 == l3 and l1 != l2 and l2 != l3 or l2 == l3 and l1 != l2 and l1 != l3:
    print("Esse triangulo é Isósceles")
elif l1 != l2 and l1 != l3 and l2 != l3:
    print("Esse triangulo é Escaleno")
else:
    print("Erro")
"""
"""
#7
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+,-,/,*): ")

if op == "+":
    R = n1 + n2
    print(f"Resultado: {R}")
elif op == "-":
    R = n1 - n2
    print(f"Resultado: {R}")
elif op == "/":
    if n2 == 0:
        print("Erro, não pode dividir por 0")
    else:
        R = n1 / n2
        print(f"Resultado: {R}")
elif op == "*":
    R = n1 * n2
    print(f"Resultado: {R}")
else:
    print("Erro")
"""
"""
#8
nota = float(input("Digite uma nota (0 - 10): "))

while nota > 10 or nota < 0:
    print("Inválido, digite uma nota válida: ")
    nota = float(input("Digite uma nota (0 - 10): "))

if nota >= 7:
    print(f"Aprovado, nota: {nota:.1f}")
elif nota >= 5 and nota <= 6.9:
    print(f"Recuperação, nota: {nota:.1f}")
elif nota < 5:
    print(f"Reprovado, nota: {nota:.1f}")
else:
    print("Erro")
"""
"""
#9
sal = float(input("Digite seu salário: "))
par = float(input("Digite a parcela: "))
P = sal * 0.30

if par <= P:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")
"""
"""
#10
id1 = int(input("Digite a idade 1: "))
id2 = int(input("Digite a idade 2: "))

if id1 > id2:
    print("A primeira pessoa é mais velha!")
elif id2 > id1:
    print("A segunda pessoa é mais velha!")
elif id1 == id2:
    print("Mesma idade!")
else:
    print("Erro")
"""