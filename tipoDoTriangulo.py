"""Faça um algoritmo que dados 3 valores, X, Y, Z, verifique se esses valores formam um triângulo. Em caso afirmativo, descubra o tipo do triângulo (equilátero, isósceles ou escaleno). Em caso negativo, escreva uma mensagem informando que os 3 valores não formam um triângulo."""

A = int(input("Digite o valor A: "))
B = int(input("Digite o valor B: "))
C = int(input("Digite o valor C: "))

if (A == B and B == C):
    print("O triângulo é equilátero")
elif (A != B and A != C and B != C):
    print("O triângulo é Escaleno")
elif (A == B or A == C or B == C):
    print("O triângulo é Isósceles")
