#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date #Metodo para pegar o ano atual do computador
ano = int(input("Digite o Ano dessejado, ou 0 para verificar o ano atual: "))
if ano == 0:
    ano = date.today().year # Pegando o ano atual do computador.
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O Ano {ano} é Bissexto!")
else:
    print(f"O Ano {ano} não é Bisexto!")