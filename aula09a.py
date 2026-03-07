# Manipulando Cadeias de Texto

# Fatiamento
frase = ["Curso em Video Python"]

frase[9:21] # Vai da posição 9 até a 21, lembrando que exibe 1 a menos do final, ou seja, vai exibir de 9 até 20.

frase[9:21:2] # Vai da posição 9 até a 21 pulando de 2 em 2, exibindo sempre 1 a menos.

frase[:5] # sempre que vc não define o inicio do fatiamento, ele vai do inicio ou seja, posição zero da cadeia.

frase[15:] # Fatia da posição 15 até o final completo, já que vc não definiu o final.

frase[9::3] # Percorre do 9 até o final, pulando de 3 em 3 caracteres.

# Análise

len(frase) # Análisa a quantidade de caracteres

frase.count('o') # Vai contar quantas vezes aparece a letra 'o' Minuscula.

frase.count('o', 0, 13) # Vai contas quantas vezes a letra o apareceu entre o caractere 0 até o 13.

frase.find('deo') # Vai dizer qual a posição que começou a palavra.



