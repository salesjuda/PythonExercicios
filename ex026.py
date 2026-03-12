#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A" em que posição ela aparece a primeira vez. Em que posição ela aparece a ultima vez
frase = input("Digite uma frase: ")

frase = frase.lower()
print(f"a letra A apareceu {frase.count('a')} vezes. Começand na posição: {frase.find('a')} Terminando na posição: {frase.rfind('a')} vezes.")