# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input("Digite o seu nome completo: "))
print(f"O seu nome completo é: {nome}")
print(f"Nome com letras Maiusculas: {nome.upper()}")
print(f"Nome com letras Minusculas: {nome.lower()}")
print(f"Possui {len(''.join(nome.split()))} Caracteres nessa frase.")
print(f"{len(nome.split()[0])}")
