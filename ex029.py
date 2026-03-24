#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 50KM/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

km = float(input("Digite o valor do Km/h: "))

if(km >80):
    print(f"Você fui multado e vai pagar: R${(km-80)*7:.2f} Reais")
else:
    print("Você não foi multado!")
print("Tenha um ótimo dia, diriga com segurança.")