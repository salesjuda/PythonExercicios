#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input("Digite a quantidade de Dias: "))
km = float(input("Digite quantos km o carro rodou: "))
print(f"Você percorreu {km:.2f} vai pagar {km*0.15 + 60*dias:.2f}")