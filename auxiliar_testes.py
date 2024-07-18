import pandas as pd
from datetime import date, time, timedelta, datetime
import pywhatkit as whatsapp



alunos_df = pd.read_csv(r"C:\Users\ROBERT\Desktop\projetoEbd\backend\alunos.csv")
data_atual = datetime.now().date()
data_formatada = data_atual.strftime("%d/%m/%Y")
print(f"a data atual é {data_formatada}")

print('-------------------------------lista de aniversariantes-------------------------------')
for index, row in alunos_df.iterrows():
    print()
    print(f"{row['nome']} {row['sobrenome']} : {row['data_de_nascimento']}")
    print()
    data_nascimento_str = row['data_de_nascimento']

    data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
    
    proximo_aniversario = data_nascimento.replace(year=data_atual.year)
    if proximo_aniversario < data_atual:
        proximo_aniversario = proximo_aniversario.replace(year=data_atual.year + 1)
        
    dias_restantes = (proximo_aniversario - data_atual).days
    print(f"{row['nome']} faz aniversário no dia {data_nascimento.day} do mês {data_nascimento.month}")
    print(f"Dias restantes até o próximo aniversário: {dias_restantes}")
    
    if dias_restantes == 7:
        print(f"falta uma semana para o aniversario de {row['nome']}")
        whatsapp.sendwhatmsg_instantly("+55 98 8718-6908", f"falta uma semana para o aniversario de {row['nome']}", wait_time=60, tab_close=True, close_time=3)

    elif dias_restantes < 7:
        print()
        whatsapp.sendwhatmsg_instantly("+55 98 8718-6908", f"restam {dias_restantes} dias para o aniverario de {row['nome']}", wait_time=60, tab_close=True, close_time=3)
    
    elif dias_restantes == 1:
        print()
        whatsapp.sendwhatmsg_instantly("+55 98 8718-6908", f"falta 1 dia para o aniverario de {row['nome']}", wait_time=60, tab_close=True, close_time=3)
    else:    
        continue
    
    
    print("--------------------------------------------------------------")
    