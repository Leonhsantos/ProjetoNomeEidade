# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


nome = str(input("Qual seu nome completo ? "))
print("Seu nome é :", nome)


data_Nascimento = int(input("Digite sua data de nascimento:"))
ano = 2022
idade = ano - data_Nascimento
while data_Nascimento < 1922 or data_Nascimento > 2021: 
    print("Data de nascimento fora do intervalo permitido (1922 - 2021). ")
    data_Nascimento = int(input("digite a data de nascimento correta:"))
    idade = ano - data_Nascimento
print("Sua idade é: ", idade)








