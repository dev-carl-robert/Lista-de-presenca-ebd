import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent


nome = input("Qual o nome do aluno? ")
sobrenome = input("Qual o sobrenome do aluno? ")
idade = input("Qual a idade do aluno? ")
data_de_nascimento = input("Qual a data de nascimento do aluno? ")
sexo = input("Qual o sexo do aluno? ")
telefone = input("Qual o telefone do aluno? ")
classe = input("Qual a classe do aluno? ")
professorResponsavel = input("Qual professor responsavel do aluno? ")

with open(ROOT_PATH / "alunos.csv", "a", encoding="utf-8", newline="") as arquivoAluno:
    indice = 00 
    escritorAluno = csv.writer(arquivoAluno)
    escritorAluno.writerow([(indice + 1), nome, sobrenome, idade, data_de_nascimento, sexo, telefone, classe, professorResponsavel])


