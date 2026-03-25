# Manipulando Cadeias de Texto

# FATIAMENTO
frase = ["Curso em Video Python"]

frase[9:21] # Vai da posição 9 até a 21, lembrando que exibe 1 a menos do final, ou seja, vai exibir de 9 até 20.

frase[9:21:2] # Vai da posição 9 até a 21 pulando de 2 em 2, exibindo sempre 1 a menos.

frase[:5] # sempre que vc não define o inicio do fatiamento, ele vai do inicio ou seja, posição zero da cadeia.

frase[15:] # Fatia da posição 15 até o final completo, já que vc não definiu o final.

frase[9::3] # Percorre do 9 até o final, pulando de 3 em 3 caracteres.

# ANÁLISE
len(frase) # Análisa a quantidade de caracteres

frase.count('o') # Vai contar quantas vezes aparece a letra 'o' Minuscula.

frase.count('o', 0, 13) # Vai contar quantas vezes a letra o apareceu entre o caractere 0 até o 13.

frase.find('deo') # Vai dizer qual a posição que começou a palavra.
frase.find('android') # Se vc define uma palavra ou letra que não existe em nenhuma posição, o python vai te retornar o valor de -1 da posição.

'Curso' in frase # Ele vai verificar se existe a palavra Curso dentro de frase retornando True ou False

# TRANSFORMAÇÃO
frase.replace('Python', 'Android') # Vai encontrar a palavra 'Python' e vai substituir por 'Android'.
frase.upper() # É um metodo que Transforma as letras em maiusculo.
frase.lower() # É um metodo que transforma as letras em minusculo.
frase.capitalize() # Transforma todas as letras em minusculo deixando apenas a primeira da frase em Maiusculo.
frase.title() # Transforma as letras em minusculo deixando apenas a primeira de cadas palavra em maiusculo.
frase.strip() # Remove todos os espaços inuteis do inicio e do final da frase.
frase.rstrip() # Remove todos os espaços inuteis do final da frase a direita.
frase.lstrip() # Remove todos os espaços inuteis do inicio da frase a esquerda.

# DIVISÃO
frase.split() # Divide a string em uma lista de substring feita por cada palavra que fazia parte da frase.

# JUNÇÃO
'-'.join(frase) # Junta todos os elementos de uma frase separando cada palavra por um caractere delimitado que nesse exemplo seria '-'.
