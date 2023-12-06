# Crie uma função que recebe um número e retorna se ele é positivo, negativo ou zero.
# def verifica_num(numero):
#   if numero > 0:
#       print('O número é positivo')
#   elif numero < 0:
#       print('O número é negativo')
#   else:
#       print('O número é zero')

# numero = int(input('Digite um número: '))
# verifica_num(numero)

# Crie uma função que recebe a idade de uma pessoa e retorna se ela é maior de idade ou menor.
# def verifica_idade(idade):
#     if idade < 18:
#         print('Você é menor de idade')
#     elif idade >= 18:
#         print('Você é maior de idade')

# idade = int(input('Digite sua idade: '))
# verifica_idade(idade)

# Crie uma função que recebe três números e retorna o maior deles.
# def maior_numero(num, num2, num3):
#     if num > num2 and num > num3:
#         print(f'O número {num} é maior')
#     elif num2 > num and num2 > num3:
#         print(f'O número {num2} é maior')
#     elif num3 > num and num3 > num2:
#         print(f'O número {num3} é maior')

# num = int(input('Digite um número: '))
# num2 = int(input('Digite outro número: '))
# num3 = int(input('Digite mais outro número: '))
# maior_numero(num, num2, num3)

# Crie uma função que recebe um número e retorna se ele é par ou ímpar.
# def impar_par(num):
#     if num % 2 == 0:
#       print('O número é par')
#     else:
#       print('O número é ímpar')

# num = int(input('Digite um número: '))
# impar_par(num)

# Crie uma função que recebe um mês (em número) e retorna a estação do ano correspondente.
# janeiro = 1
# fevereiro = 2
# marco = 3
# abril = 4
# maio = 5
# junho = 6
# julho = 7
# agosto = 8
# setembro = 9
# outubro = 10
# novembro = 11
# dezembro = 12
# def recebe_mes(mes):
#   if mes == dezembro or mes == janeiro or mes == fevereiro or mes == marco:
#     print('Verão')
#   elif mes == abril or mes == maio or mes == junho or mes == julho:
#     print('Outono')
#   elif mes == agosto or mes == setembro or mes == outubro or mes == novembro:
#     print('Inverno')

# mes = int(input('Digite um número de um mês:'))
# recebe_mes(mes)

# Crie uma função que recebe a nota de um aluno e retorna se ele foi aprovado (nota maior ou igual a 7), está de recuperação (nota maior ou igual a 5 e menor que 7) ou foi reprovado (nota menor que 5).
# def recebe_notas(nota, nota2, nota3, nota4):
#   if media >= 7:
#     print('Aprovado!')
#   elif media >= 5 and media < 7:
#     print('Está de recuperação')
#   elif media < 5:
#     print('Reprovado')

# nota = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# nota3 = float(input('Digite a terceira nota: '))
# nota4 = float(input('Digite a quarta nota: '))
# media = (nota + nota2 + nota3 + nota4) / 4
# recebe_notas(nota, nota2, nota3, nota4)

# Crie uma função que recebe o peso e a altura de uma pessoa e calcula o seu IMC (Índice de Massa Corporal), retornando se a pessoa está abaixo do peso, com peso normal, com sobrepeso ou obesa.
# def calcula_imc(peso, altura):
#   imc = peso / altura ** 2
#   if imc <= 16 and imc >= 18.5:
#     print('Você está abaixo do peso')
#   elif imc >= 18.6 and imc <= 24.9:
#     print('Seu peso está normal')
#   elif imc >= 25 and imc <= 29.9:
#     print('Você está em sobrepeso')
#   elif imc >= 30:
#     print('Você está em estado de obesidade')
#   else:
#     print('O programa foi encerrado')
# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))
# calcula_imc(peso, altura)

# Crie uma função que recebe um ano e retorna se ele é bissexto ou não.
# def bissexto (ano):
#   if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print('Este ano é bissexto')
#   else:
#     print('O ano não é bissexto')

# ano = int(input('Digite um ano:'))
# bissexto(ano)

# Crie uma função que recebe um caractere e retorna se ele é uma vogal, uma consoante ou um número.
def verificator(digito):
    if digito in consoante or digito in vogal:
        if digito in vogal:
            info = (f'A letra {digito} é vogal')
            return info
        elif digito in consoante:
            info = 'O caractere digitado é uma consoante'
            return info

    elif digito.isdigit():
        info = (f'O caractere {digito} é um número')
        return info

    else:
        info = 'O caractere é um símbolo'
        return info
        
        

vogal = ['a','e','i','o','u','A','E','I','O','U']
consoante = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']

caractere = input('Digite um caractere:')

print(verificator(caractere))
# Crie uma função que recebe um número e retorna se ele é um número primo ou não.
# def verifica_primo(num):
#   if num % num == 0 or num % 1 == num:
#     print('O numéro é primo')
#   else:
#     print('O número não é primo')
# num = int(input('Envie um número: '))
# verifica_primo(num)
