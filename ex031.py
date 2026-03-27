#Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas
km = float(input("Digite a distancia da viagem em Km: "))
if(km <= 200):
    total = km * 0.5
    print(f"o Preço da passagem é de R${total:.2f} Reais de acordo com a distância")
else:
    total = km * 0.45
    print(f"O preço da passagem é de R${total:.2f} Reais de acordo com a distância.")