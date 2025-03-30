# # nivel 1
# # questao 1
# print("Alo mundo")
# # qustao 2
# numero = float(input("digite um numero: "))
# print("o numero informado foi:", numero)
# # questao 3
# segundo_numero = float(input("digite outro numero: "))
# print(" o segundo numero informado foi:", segundo_numero)
# print(numero + segundo_numero)
# # questao 4
# primeira_nota = float(input("digite a primeira nota: "))
# segunda_nota = float(input("digite a segunda nota: "))
# terceita_nota = float(input("digite a terceira nota: "))
# quarta_nota = float(input("digite a quarta nota: "))
# media = (primeira_nota + segunda_nota + terceita_nota + quarta_nota) / 4
# print("sua media foi de:", media)
# # questao 5
# quantidade_metros = float(input("digite a quantidade de metros: "))
# centimetros = quantidade_metros * 100
# print(quantidade_metros, "metro(s) é igual a:", centimetros, "centimetros")
# # questao 6
# raio_circulo = float(input("digite o raio do circulo em centimetros: "))
# area_circulop1 = raio_circulo ** 2
# area_circulop2 = 3.14159265358979323846 * area_circulop1
# print("a area do circulo é de: ", area_circulop2, "centimetros ao quadrado")
# # questao 7
# lado_quadrado = float(input("digite o lado do seu quadrado em cm: "))
# area_quadrado = lado_quadrado ** 2
# print("o dobro da area do seu quadrado é de:", area_quadrado * 2, "cm ao quadrado")
# # questao 8
# dinheiro_hora = float(input("digite quanto voce ganha a hora trabalhada: "))
# horas_mes = float(input("digite quantas horas voce trabalha no mes: "))
# salario_mes = dinheiro_hora * horas_mes
# print("voce ganha R$", salario_mes, "ao mes")
# # questao 9
# fireheint = int(input("digite a temperatura em fahrenheit: "))
# celcios = 5 / 9 * (fireheint - 32)
# print("a temperatura é igual a:", celcios, "Grau Ceucius")
# # questao 10
# ceucius = int(input("digite a temperatura em celcius: "))
# fahrenheit = ceucius * 1.8 + 32
# print("a temperatura é igual a:", fahrenheit, "Grau Fahrenheit")
# # questao 11
# primeiro_numero_inteiro = int(input("digite um numero inteiro: "))
# segundo_numero_inteiro = int(input("digite outro numero inteiro: "))
# numero_real = float(input("digite um numero real: "))
# print("o dobro do primeiro numero + a metade do segundo numero é igual a:", (primeiro_numero_inteiro * 2) + (segundo_numero_inteiro / 2))
# print("(o primeiro numero x 3) + o terceiro numero é igual a:", (primeiro_numero_inteiro * 3) + numero_real)
# print("o terceiro numero ao cubo é igual a:", numero_real ** 3)
# # questao 12
# altura = float(input("diga sua altura em metros: "))
# print("seu peso ideal é de", (72.7 * altura) - 58, "kg")
# # questao 13
# Altura = float(input("diga sua altura em metros: "))
# print("se voce for homem seu peso ideal é de", (72.7 * Altura) - 58, "kg")
# print("se voce for mulher seu peso ideal é de", (62.1 * Altura) - 44.7, "kg")
# # questao 14
# peso = int(input("digite o peso dos peixes em kg: "))
# limite = 50
# peso_mais = peso - limite

# if peso_mais >= 1:
#     print("você passou do limite de", limite, "kg")
#     print("sua multa foi de R$", peso_mais * 4)
# else:
#     print("você não passou do limite de", limite, "kg")
#     print("não tera multa")
#     # questao 15
# salario_hora = float(input("digite quanto voce ganha por hora trabalhada: "))
# horas_no_mes = float(input("digite horas trabalhadas no mes: "))
# salario_bruto = salario_hora * horas_no_mes
# inss = salario_bruto * 0.08
# sindicato = salario_bruto * 0.05
# imposto_renda = salario_bruto * 0.11
# salario_liquido = salario_bruto - inss - sindicato - imposto_renda
# descontos = inss + sindicato + imposto_renda
# print(f"seu salario bruto foi de R$ {salario_bruto:.2f}")
# print(f"seu INSS foi de R$ {inss:.2f}")
# print(f"seu sindicato foi de R$ {sindicato:.2f}")
# print(f"seu Imposto De Renda foi de R$ {imposto_renda:.2f}")
# print(f"seu salario liquido foi de R$ {salario_liquido:.2f}")
# print(f"seu desconto foi de R$ {descontos:.2f}")
# # exercicio 16

tamanho_metros_quadrados = float(input("digite a area em metros quadrados: "))
tinta_litro = 3
lata_tinta = 18 ** 2
preco_lata_tinta = 80




# exercicio 17

# exercicio 18


# ************************************************************************************************

# anotacoes

# idade = int(input("digite sua idade: ")) # ctrl ; tudo que voce selecionar vira comentario
# maioridade = 18
# maior_de_idade = idade >= maioridade
# print(maior_de_idade)

# valor1 = int(input("digite um valor:"))
# valor2 = int(input("digite outro valor:"))

# print("valor1 é maior que valor2?", (valor1 > valor2))

# # == -> igual a
# print("valor1 é maior que valor2?", (valor1 > valor2))
# # >= -> maior ou igual
# print("valor1 é maior que valor2?", (valor1 > valor2))
# # > -> maior que
# print("valor1 é maior que valor2?", (valor1 > valor2))
# # < -> menor que
# print("valor1 é maior que valor2?", (valor1 > valor2))
# # <= -> menor ou igual a
# print("valor1 é maior que valor2?", (valor1 > valor2))
# # != -> diferente de
# print("valor1 é maior que valor2?", (valor1 > valor2))




# faturamento = 1000 
# custo = 700

# novas_vendas = 300

# faturamento = faturamento + novas_vendas # somar
# imposto = faturamento * 0.1 # multiplicar
# lucro = faturamento - custo  - imposto # subtrair
# print(faturamento)
# print(lucro)
# margem_lucro  = lucro / faturamento # dividir
# print(margem_lucro)

# restituicao = imposto * 0.1
# print(restituicao)

# # Mod resto da divisao
# # 10 % 3
# print (10 % 3)

# tempo_em_meses = 160
# tempo_em_anos = int(tempo_em_meses / 12) # deixa inteiro 
# print(tempo_em_anos)
# print(tempo_em_meses % 12)
# print(tempo_em_anos, "anos e", tempo_em_meses % 12, "meses" )

# numero = 123.57

# print(round(numero)) # arredonda o numero

# Faturamento = 139_018_182 # _  é uma ediçao visual para facilitar
