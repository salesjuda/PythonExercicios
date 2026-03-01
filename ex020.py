# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Leia o nome dos quartro alunos e mostre a ordem sorteada
import random
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Ditite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quardo aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)

print(f"A ordem de apresentação do trabalho, vai ser: {alunos}")
