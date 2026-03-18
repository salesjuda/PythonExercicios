#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A" em que posição ela aparece a primeira vez. Em que posição ela aparece a ultima vez
frase = str(input("Digite uma frase: ")).lower().strip()

print(f"a letra A apareceu {frase.count('a')} vezes. Começando na posição: {frase.find('a')+1} Terminando na posição: {frase.rfind('a')+1} vezes.")