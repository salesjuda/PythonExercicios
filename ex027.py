#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
nome = str(input("Digite o nome completo de uma pessoa: ")).strip().split()
print(f"{nome[0]}")
print(f"{nome[len(nome)-1]}")