import csv
from pathlib import Path
import pandas as pd

ROOT_PATH = Path(__file__).parent
caminho_csv = ROOT_PATH / "alunos.csv"


# nome = input("Qual o nome do aluno? ")
# sobrenome = input("Qual o sobrenome do aluno? ")
# idade = input("Qual a idade do aluno? ")
# data_de_nascimento = input("Qual a data de nascimento do aluno? ")
# sexo = input("Qual o sexo do aluno? ")
# telefone = input("Qual o telefone do aluno? ")
# classe = input("Qual a classe do aluno? ")
# professorResponsavel = input("Qual professor responsavel do aluno? ")

# if caminho_csv.exists():
#     Alunos_df = pd.read_csv(caminho_csv)
#     indice = Alunos_df.index.max() + 1
# else:
#     indice = 0
    
# with open(caminho_csv, "a", encoding="utf-8") as arquivoAluno:
#     escritorAluno = csv.writer(arquivoAluno)
#     escritorAluno.writerow([indice, nome, sobrenome, idade, data_de_nascimento, sexo, telefone, classe, professorResponsavel])


Alunos_df = pd.read_csv(caminho_csv)

    
Alunos_df = Alunos_df[Alunos_df['nome'] != 'mariana']
Alunos_df.to_csv(caminho_csv, index=False, encoding='utf-8')


for _, row in Alunos_df.iterrows():
    print(row)
