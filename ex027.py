#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
nome = input("Digite o nome completo de uma pessoa: ")

separado = nome.split()
cont = len(separado) -1
print(f"{cont}")
print(f"{separado[0]}")
print(f"{separado[cont]}")