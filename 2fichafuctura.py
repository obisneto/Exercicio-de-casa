# 1. Desenvolva um programa que solicite que um usuário informe o número de
# votos brancos, nulos e válidos de uma eleição e exiba o percentual que cada um
# representa em relação ao total de eleitores.
votos_brancos = int(input("digite quantos votos brancos tiveram: "))
votos_nulos = int(input("digite quantos votos nulos tiveram: "))
votos_validos = int(input("digite a quantidade de votos validos: "))

porcentagem_brancos = (votos_brancos /(votos_brancos + votos_nulos + votos_validos))
porcentagem_nulos = (votos_nulos /(votos_brancos + votos_nulos + votos_validos))
porcentagem_validos = (votos_validos /(votos_brancos + votos_nulos + votos_validos))

print(f"{porcentagem_brancos:.2%} foram votos brancos, {porcentagem_nulos:.2%} foram votos nulos e {porcentagem_validos:.2%} dos votos foram validos ")


# 2. Escreva um programa que verifica se uma pessoa é maior de idade (18 anos ou
# mais). E imprima se ela é ou não maior de idade.
idade = int(input("digite a sua idade: "))

if idade >= 18:
    print("voce é maior de idade")
else:
    print("voce é menor de idade")


# 3. Escreva um programa que verifique se um número é par ou ímpar. E imprima
# essa informação.
numero = float(input("digite um numero: "))

if numero % 2 == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é impar")


# 4. Escreva um programa que peça o salário de 2 pessoas e informe qual dos dois é
# o maior.
salario1 = float(input("digite o primeiro salario: "))
salario2 = float(input("digite o segundo salario: "))

if salario1 > salario2:
    print(f"o primeiro salario é maior que o segundo")
elif salario1 == salario2:
    print("os dois salarrios sao iguais")
else:
    print(f"o segundo salario é maior que o primeiro")


# 5. Escreva um programa que verifica se uma palavra inserida pelo usuário é
# "Python". E imprima se é ou não.
palavra = input("digite uma palavra: ")

if palavra == "Python":
    print("palavra correta")
else:
    print("palavra incorreta")


# 6. Escreva um programa que verifica se um número é positivo, negativo ou zero.
numero = float(input("digite um numero: "))

if numero > 0:
    print(f"{numero} é positivo")
elif numero == 0:
    print("voce digitou 0(zero)")
else:
    print(f"{numero} é negativo ")


# 7. Escreva um programa que encontra o maior de três números.
numero1 = float(input("digite o primeiro numero: "))
numero2 = float(input("digite o segundo numero: "))
numero3 = float(input("digite o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print("o primeiro numero é maior")
elif numero2 > numero1 and numero2 > numero3:
    print("o segundo numero é o maior")
elif numero3 > numero1 and numero3 > numero2:
    print("o terceiro numero é o maior")
else:
    print("tem numero repetido")


# 8. Escreva um programa que verifica se um número é divisível por 5.
numero = float(input("digite um numero: "))

if numero % 5 == 0:
    print(f"{numero} é divisivel por 5")
else:
    print(f"{numero} nao é divisivel por 5")


# 9. Escreva um programa que solicita a nota 3 provas, faz a média e informa se o
# aluno foi aprovado (nota maior ou igual a 7).
nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
nota3 = float(input("digite sua terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"voce foi aprovado com {media} de media")
else:
    print("voce foi reprovado")


# 10. Escreva um programa que verifica se um número é divisível por 3 e por 5.
numero = float(input("digite um numero: "))

if numero % 3 == 0 and numero % 5 ==0:
    print(f"esse numero é divisivel por 3 e por 5")
else:
    print(f"esse numero nao é divisivel por 3 e por 5")


# 11. Desenvolva um programa que determine o módulo de um número inteiro (se o
# número for negativo ele deve ser transformado em positivo).
numero = float(input("digite um numero: "))

if numero < 0:
    print(f"{numero} positivo fica assim {-(numero)}")
elif numero == 0:
    print(f"Voce digitou zero")
else:
    print(f"{numero} ja é positivo")


# 12. Escreva um programa que peça a velocidade do motorista e a velocidade máxima
# em uma determinada avenida, e calcule a multa (se houver), sabendo que
# são pagos:

# a) 50 reais se o motorista ultrapassar em até 10km/h a velocidade permitida (ex.:
# velocidade máxima: 50km/h; motorista a 60km/h ou a56km/h);

# b) 100 reais, se o motorista ultrapassar de 11 a 30 km/h a velocidade permitida.

# c) 200 reais, se estiver acima de 31km/h da velocidade permitida.
velocidade_motorista = float(input("digite a sua velocidade em km: "))
velocidade_maxima = float(input("digite a velocidade maxima do local em km: "))

if velocidade_motorista <= velocidade_maxima:
    print(f"Parabens não houve multa!")
elif velocidade_motorista - velocidade_maxima >= 1 and velocidade_motorista - velocidade_maxima <= 10:
    print(f" Voce tera que pagar uma multa de R$ 50,00")
elif velocidade_motorista - velocidade_maxima >= 11 and velocidade_motorista - velocidade_maxima <= 30:
    print(f"Voce tera que pagar uma multa de R$ 100,00")
else:
    print(f"Voce tera que pagar uma multa de R$ 200,00")


# 13. Em uma determinada faculdade, dado que um estudante não atingiu a média
# 7,0, este precisará fazer uma prova final. A nota mínima na avaliação final para
# que este estudante seja aprovado é dada pela seguinte fórmula: NF = (50 - Média
# x 6) ÷ 4. Assim, com base nessa informação desenvolva um programa que solicite
# três notas e caso esteja abaixo da média, calcule qual a nota mínima que o
# estudante precisa tirar na avaliação final para passar.
nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
nota3 = float(input("digite sua terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
nf = (50 - media * 6) / 4

if media >= 7:
    print(f"Parabens voce passou!!!")
else:
    print(f"Infelizmente voce não passou porque sua media foi de: {media} e a media minima era de 7,\n mas se voce tirar {nf} na final voce passa")

# 14. Um hotel cobra R$ 50,00 por diária acrescida de uma taxa de serviços. A taxa de
# serviços é de:
# R$ 4,00 por diária, se o número de diárias for menor que 5;
# R$ 3,60 por diária, caso contrário. De posse destas informações, construa um
# programa que solicite o número de diárias e informe o quanto deverá ser pago
# pelo hóspede.
diaria = int(input("digite a quantidade de dias que voce passara no hotel: "))
valor_uma_diaria = 50
if diaria <= 5:
    taxa_servicos = 4
    total_servicos = diaria * taxa_servicos
    print(f"o valor da(s) diaria(s) incluindo a taxa de serviço ficara R$ {(diaria * valor_uma_diaria) + total_servicos}")
else:
    taxa_servicos = 3.6
    total_servicos = diaria * taxa_servicos
    print(f"o valor da(s) diaria(s) incluindo a taxa de serviço ficara R$ {(diaria * valor_uma_diaria) + total_servicos}")


# 15. No bairro do Janga existe uma lei que toda vez que um pescador traz um peso
# de peixes maior que o estabelecido pelo regulamento de pesca (50 quilos) deve
# pagar uma multa de R$4,00 por quilo excedente. A prefeitura precisa que você
# faça um programa que solicite o peso de certa quantidade de peixes e caso haja
# excesso de peso, mostre qual é este peso (em quilos) e quanto de multa deverá
# ser paga. Caso não haja excesso, deverá ser mostrada a mensagem “Parabéns
# por não ultrapassar o limite”.

peso = int(input("digite o peso dos peixes em kg: "))
limite = 50
peso_mais = peso - limite

if peso_mais >= 1:
    print("você passou do limite de", limite, "kg")
    print("sua multa foi de R$", peso_mais * 4)
else:
    print(f"parabens por nao ultrapassar o limite")


# 16. Escreva um programa que implemente uma calculadora básica que realiza
# adição, subtração, multiplicação e divisão com base na escolha do usuário
# (solicita valor1, valor2, e operação).

while True:
    print(f"Escreva dois numeros e depois diga qual operação ira utilizar.")
    numero1 = float(input("digite o primeiro numero: "))
    numero2 = float(input("digite o segundo numero: "))
    operacao = input("diigte a operação(*, /, +, -, ** ou //): ")

    if operacao == "*":
        print(f"{numero1} vezes {numero2} é igual a {numero1 * numero2}")
    elif operacao == "/":
        print(f"{numero1} dividido por {numero2} é igual a {numero1 / numero2}")
    elif operacao == "+":
        print(f"{numero1} mais {numero2} é igual a {numero1 + numero2}")
    elif operacao == "-":
        print(f"{numero1} menos {numero2} é igual a {numero1 - numero2}")
    elif operacao == "**":
        print(f"{numero1} elevado a {numero2} é igual a {numero1 ** numero2}")
    elif operacao == "//":
        print(f"{numero1} divido(divisão inteira) {numero2} é igual a {numero1 // numero2}")
    else:
        print(f"operação indisponivel")
    
    repetir = input("voce quer repetir(sim ou nao): ")
    if repetir == "nao":
        print()
        break
    elif repetir == "sim":
        print()
    else:
        print(f"comando invalido. vou considerar como um sim")
        print()


# 17. Escreva um programa que solicita ao usuário um número e analise se o número
# é divisível por 2, por 3 e por 5. Imprima “O número é divisível por _”.
numero = float(input("digite um numero: "))

if numero % 2 == 0:
    print(f"{numero} é divisivel por 2")
else:
    print(f"{numero} não é divisiveel por 2")
if numero % 3 == 0:
    print(f"{numero} é divisivel por 3")
else:
    print(f"{numero} não é divisivel por 3")
if numero % 5 == 0:
    print(f"{numero} é divisivel por 5")
else:
    print(f"{numero} não é divisivel por 5")
