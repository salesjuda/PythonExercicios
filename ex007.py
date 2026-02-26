#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.
nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("informe a segunda nota do aluno: "))

print("Nota total {:.1f}, a média é: {:.1f}".format(nota1 + nota2, (nota1+nota2)/2))