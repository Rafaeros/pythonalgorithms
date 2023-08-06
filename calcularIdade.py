"""
Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
A idade dessa pessoa;
Sua idade em 2030
"""
import datetime as dt
data_hoje = dt.datetime.today()
ano_hoje = data_hoje.year


print("-------------------------")
ano_nascimento = float(input("Insira o ano do seu nascimento: "))
idade = ano_hoje-ano_nascimento
print("Idade: ", idade)
print("Idade em 2030: ", 2030-ano_nascimento)
print("-------------------------")
