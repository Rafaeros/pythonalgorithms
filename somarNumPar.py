print("Somar numeros pares")
valorMaximo = int(input("Digite o valor maximo:"))
cont=0
somaPar = 0
while(cont<=valorMaximo):
    if(cont%2==0):
        somaPar = somaPar + cont
    cont+=1

print("A Soma dos pares é: ", somaPar)