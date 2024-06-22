Alunos = [
    {"nome": "Miguel", "sobrenome": "Santos", "idade": 17, "sexo": "masculino", "telefone": "9####-####", "classe": "jovens"},
    {"nome": "Robert", "sobrenome": "Santos", "idade": 22, "sexo": "masculino", "telefone": "9####-####", "classe": "jovens"},
]


def acessar_aluno():
    print('escolha o numero do aluno desejado')
    aluno_escolhido = int(input("Qual aluno deseja acessar?"))
    aluno_acessado = Alunos[aluno_escolhido]
    
    print(30 * "_")
    print(f"Nome Completo: {aluno_acessado['nome']} {aluno_acessado['sobrenome']}")
    print(f"Idade: {aluno_acessado['idade']}")
    print(f"Sexo: {aluno_acessado['sexo']}")
    print(f"Telefone: {aluno_acessado['telefone']}")
    print(f"Classe: {aluno_acessado['classe']}")
    print(30 * "_")
acessar_aluno()
