#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
a = float(input("Digite o tamanho da primeira reta: "))
b = float(input("Digite o tamanho da segunda reta: "))
c = float(input("Digite o tamanho da terceira reta: "))
if(a + b > c and a + c > b and b + c > a):
    print("Pode ser um triângulo!")
else:
    print("Não pode ser um triângulo!")