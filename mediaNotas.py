"""Faça um algoritmo que leia o nome da disciplina e três notas, para um único aluno. Calcule a média aritmética das notas e, ao final, escreva o nome da disciplina, sua média e se ele foi aprovado ou reprovado. A média para aprovação é 70."""

disciplina = input("Digite o nnome da disciplina: ")
nota1 = float(input("Digite o valor da nota 1: "))
nota2 = float(input("Digite o valor da nota 2: "))
nota3 = float(input("Digite o valor da nota 3: "))

media = (nota1+nota2+nota3)/3

if (media > 70):
    print(disciplina)
    print(media)
    print("Aluno aprovado!")
else:
    print(disciplina)
    print(media)
    print("Aluno reprovado!")
