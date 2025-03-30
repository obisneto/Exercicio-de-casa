# 1. Escreva um programa que peça dois números do usuário e exiba a soma deles.
# (Saída deve ser “A soma é _____”).
numero1 = float(input("digite um numero: "))
numero2 = float(input("digite outro numero: "))
print(f"a soma é {numero1 + numero2}")

# 2. Escreva um programa que leia três números do usuário e exiba a média deles
# (Saída deve ser “A média é _____”).
numero1 = float(input("digite um numero: "))
numero2 = float(input("digite outro numero: "))
numero3 = float(input("digite o terceiro numero: "))
media = (numero1 + numero2 + numero3) / 3
print(f"a media é {media}")

# 3. Escreva um programa que leia o raio de um círculo e calcule sua área (Saída deve
# ser “A área é _____”).
raio_circulo = float(input("digite o raio do circulo: "))
area_circulo = 3.14 * raio_circulo ** 2
print(f"a area é {area_circulo:.2f}")

# 4. Escreva um programa que leia a largura e a altura de um retângulo e calcule seu
# perímetro (Saída deve ser “O perímetro é _____”).
altura_retangulo = float(input("digite a altura do seu retangulo: "))
largura_retangulo = float(input("digite a largura do seu retangulo: "))
perimetro_retangulo = altura_retangulo + altura_retangulo + largura_retangulo + largura_retangulo
print(f"o perimetro é {perimetro_retangulo}")

# 5. Escreva um programa que leia a largura e altura de um retângulo e calcule sua
# área (Saída deve ser “A área é _____”).
altura_retangulo = float(input("digite a altura do seu retangulo: "))
largura_retangulo = float(input("digite a largura do seu retangulo: "))
area_retangulo = altura_retangulo * largura_retangulo
print(f"A area é {area_retangulo}")

# 6. Escreva um programa que solicite do usuário a distância em km e o consumo de
# gasolina (em km/litro) e informe a quantidade de litros que ele utilizará para
# percorrer essa distância (Saída deve ser “Serão utilizados _____ litros”).
distancia_km = float(input("digite a distancia em km que sera percorrida: "))
consumo_gasolina = float(input("digite o consumo da gasolina: "))
quantidade_gasolina_utilizada = distancia_km / consumo_gasolina
print(f"serao utilizados {quantidade_gasolina_utilizada} litros")

# 7. Escreva um programa que leia um número de horas e converta para minutos
# (Saída deve ser “____ horas equivale a _____ minutos”).
numero_horas = float(input("digite o numero de horas: "))
minutos = numero_horas * 60
print(f"{numero_horas} hora(s) equivale a {minutos} minuto(s)")

# 8. Escreva um programa que leia um número de dias e converta para horas (Saída
# deve ser “___ dias equivale a _____ horas”).
dias = float(input("digite o numero de dias: "))
horas = dias * 24
print(f"{dias} dia(s) equivale a {horas} hora(s)")

# 9. Escreva um programa que leia uma distância de quilômetros e a converta para
# milhas. (1 quilômetro = 0.621371 milhas) (Saída deve ser “___ km equivale a
# _____ milhas”).
quilometros = float(input("digite a quantidade de quilometros: "))
milhas = quilometros * 0.621371
print(f"{quilometros} km equivale a {milhas:.2f} milhas")

# 10. Escreva um programa que leia um valor e um percentual de aumento e exiba o
# novo valor após o aumento(Saída deve ser “o salário antes do aumento era de
# _____, após o aumento de ____ resultou no salário final de ____”).
valor = float(input("digite o seu salario: "))
percentual = float(input("digite um percentual para aumentar o seu salario anterior: "))
calculo_percentual = valor * percentual
numero_apos_percentual = valor + calculo_percentual
print(f"o salario antes do aumento era de {valor}, apos o aumento de {percentual:.2%} resultou no salario final de {numero_apos_percentual}")

# 11. Escreva um programa que leia um valor e um percentual de desconto e exiba o
# valor após aplicar o desconto (Saída deve ser “o valor antes do aumento era de
# _____, após o desconto de ____ resultou no valor final de ____”).
valor = float(input("digite um valor: "))
desconto = float(input("digite o desconto: "))
calculo_desconto = valor * desconto 
valor_apos_desconto = valor - calculo_desconto
print(f"o valor antes do aumento era de {valor}, apos o desconto de {calculo_desconto}% resultou no valor final de {valor_apos_desconto}")

# 12. Escreva um programa que leia a largura de um cubo (em metros) e calcule qual
# a sua capacidade de volume (Saída deve ser “o cubo possui ___ metros de
# comprimento e tem uma capacidade de ___ metros cúbicos” ).
largura_cubo = float(input(" digite a largura em metros do cubo: "))
volume_cubo = largura_cubo * largura_cubo * largura_cubo
print(f"o cubo possui {largura_cubo} metros de comprimento e tem uma capacidade de {volume_cubo} metros³")

# 13. Escreva um programa que leia o salário mensal de um usuário e calcule o salário
# anual (A saída deve ser “o salário mensal é de ___ e o anual é ___”).
salario_mensal = float(input("digite o seu salario mensal: "))
salario_anual = salario_mensal * 12
print(f"o seu salario mensal é de {salario_mensal} e o anual é {salario_anual}")

# 14. Você foi contratado por uma loja para criar um programa que calcula o preço
# final de um produto após um desconto. O programa deve ler o preço original do
# produto (reais e centavos) e a porcentagem de desconto.
produto = float(input("digite o valor do produto: "))
desconto = float(input("digite o valor do desconto: "))
calculo_desconto = produto * desconto
produto_apos_desconto = produto - calculo_desconto
print(f"antes o valor do produto era de {produto} depois do desconto de {desconto * 100}% ficou por {produto_apos_desconto}")

# 15. Você foi contratado por um banco para criar um programa que converte um
# valor em reais para dólares. O programa deve ler o valor em reais e a cotação do
# dólar no momento.4
reais = float(input("digite o valor em reais: "))
dolar = reais / 5.7156
print(f"{reais} reais é igual a {dolar} dolar/dolares hoje")

# 16. Você foi contratado por uma empresa de nutrição para criar um programa que
# calcula o Índice de Massa Corporal (IMC) de uma pessoa. O programa deve ler o
# peso (em kg) e a altura (em metros) da pessoa. O IMC é dado pelo peso dividido
# pela altura ao quadrado peso / (altura **2).
peso = float(input("digite seu peso em kg: "))
altura = float(input("digite seu peso em metros: "))
imc = peso / (altura ** 2)
print(f"seu imc é de {imc:.2f}")

# 17. Você foi contratado por uma escola para criar um programa que calcula a média
# aritmética de 3 notas fornecidas pelo usuário.
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"sua media foi de {media}")

# 18. Você foi contratado por um banco para realizar um sistema de saque onde o
# usuário deve digitar o saldo inicial e em seguida o valor a ser sacado. O programa
# deve retornar o saldo final.
saldo_inicial = float(input("digite o seu saldo inicial: "))
valor_sacado = float(input("digite o valor que vai ser sacado: "))
saldo_final = saldo_inicial - valor_sacado
print(f"seu saldo final foi de {saldo_final}")

# 19. Uma concessionária de motos revende uma moto acrescidos 26% referidos a
# impostos, 2% referente ao seguro, 8% do lucro da revendedora e 1% da comissão
# do vendedor. Sabendo-se que estas porcentagens são calculadas com relação ao
# preço de fábrica (preço que a revendedora compra a moto), desenvolva um
# programa que calcule o preço de venda desta moto na concessionária.
moto = float(input("digite o valor inicial da moto: "))
imposto = moto * 0.26
seguro = moto * 0.02
lucro_revendedora = moto * 0.08
comissao = moto * 0.01
print(f"voce vai revender por {moto + imposto + seguro + lucro_revendedora + comissao}")

# 20. No bairro do Janga-PE existe uma empresa que fabrica tonéis cilíndricos de aço
# que são utilizados para armazenar água. Cada tonel produzido possui uma tampa
# lisa feita do mesmo material do tonel. Sabendo que a empresa gasta R$ 2,50 para
# pintar um m2 desta tampa com um tipo especial de tinta, desenvolva um
# programa que solicite as medidas desta tampa e a quantidade de tampas a serem
# pintadas e informe ao usuário quanto a empresa irá gastar para pintá-las.
raio_tampa = float(input("digite o raio da tampa em metros: "))
quantidade_tampas = int(input("digite a quantidade de tampa(s): "))
area_tampa = (raio_tampa ** 2) * 3.14
preco_metro = 2.50
quanto_empresa_gastara = (area_tampa * preco_metro) * quantidade_tampas
print(f"o valor para pintar {quantidade_tampas:.2f} é {quanto_empresa_gastara}")

# 21. Desenvolva um programa que calcule os gastos com combustível em uma
# viagem. O programa deve solicitar ao usuário a distância a ser percorrida em
# km, o consumo do carro em km/litro e o preço do litro do combustível. Como
# resposta o programa deverá informar qual o valor em R$ a ser gasto com
# combustível na viagem.
distancia_pecorrida = float(input("digite a distancia pecorrida em km: "))
km_litro = float(input("digite quantos km por litro o seu carro faz: "))
litro_combustivel = float(input("digite o preço do litro do combustivel: "))
valor_gasto = (litro_combustivel * km_litro) * distancia_pecorrida 
print(f"o valor gasto vai ser de {valor_gasto}")

# 22. Para se produzir um determinado tipo de fertilizante, uma fábrica precisa
# misturar três partes de Nitrogênio (N), duas partes de Potássio (K) e uma parte
# de Fósforo (P). De posse dessa informação, desenvolva um programa que
# solicite como informação uma determinada quantidade (em Kg) deste
# fertilizante e informe ao usuário a quantidade (em Kg) necessária de Nitrogênio,
# Potássio e Fósforo para a mistura.


# nao consegui porque nao fala quanto faz tres prtes de... duas de... e uma de... 



# 23. Faça um programa que calcule o volume de água em metros cúbicos de
# piscinas retangulares. Solicite do usuário os valores de comprimento, altura e
# largura e retorne o volume. (Volume= comprimento * largura * altura).
altura_piscina = float(input("digite a altura em cm da piscina: "))
comprimento_piscina = float(input("digite o comprimento em cm da piscina: "))
largura_piscina = float(input("digite a largura em cm da piscina: "))
volume_piscina = altura_piscina * largura_piscina * altura_piscina
print(f"o volume da sua piscina é de {volume_piscina} cm³")
