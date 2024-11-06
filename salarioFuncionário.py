"""
Faça um algoritmo que receba o salário base de um funcionário e calcule o valor a receber, sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% sobre o salário + gratificação. Mostre o salário base, o valor da gratificação, o valor do imposto e o salário a receber
"""


salarioBruto = float(input("Digite o salário do funcionário: "))
gratificacao = 0.05
imposto = 0.07

valorGratificacao = salarioBruto*gratificacao
valorImposto = salarioBruto*imposto

salarioLiquido = (salarioBruto + valorGratificacao) - valorImposto

print("--------------------------------")
print("Salário Bruto: ", salarioBruto)
print("Valor gratificacao: ", valorGratificacao)
print("Valor imposto: ", valorImposto)
print("Salário a receber: ", salarioLiquido)
print("--------------------------------")
