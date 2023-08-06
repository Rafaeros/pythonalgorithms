# Faça um algoritmo que leia três valores inteiros, e em seguida, mostre os três valores ordenados de forma crescente.

nums = [0,0,0]

nums[0] = int(input("Digite o valor 1: "))
nums[1] = int(input("Digite o valor 2: "))
nums[2] = int(input("Digite o valor 3: "))

nums.sort()

print(nums)