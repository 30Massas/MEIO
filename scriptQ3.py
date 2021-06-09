import random
import numpy as np
import pandas as pd

# Inicialização pandas

writer = pd.ExcelWriter(r'outputValoresQ2.xlsx', engine='xlsxwriter')



# Variáveis fixas
mu = 513.35
sigma = 66.9322
C1 = 0.345
C2 = 20
C3 = 1500
T = 4
prazos = [1,2,3]
probabilidades = [0.27,0.53,0.2]
t = -1

# Lista com procuras semanais aleatórias
procura = np.random.normal(mu,sigma,50)

# Parâmetros de teste
S = int(input('Indique o valor de S: '))
s = int(input('Indique o valor de s: '))


# Inicializar stock inicial
stock_atual = S

custos_semanais = []
stocks_atuais = []
stocks_finais = []
prazos_entrega = []
custos_quebra_semanal = []
custos_posse_semanal = []
custos_encomenda_semanal = []
quantidades_a_encomendar = []


for semana in range(50):
    custo_semanal = 0
    custo_quebra = 0
    custo_encomenda = 0

    # print(f'Semana {semana+1}')

    # print(f'Stock Atual: {stock_atual}')

    stocks_atuais.append(stock_atual)

    p = procura[semana]
    
    stock_final = stock_atual - p

    # print(f'Stock Final: {stock_final}')

    stocks_finais.append(stock_final)
    
    stock_atual = stock_final

    if T==0:
        pass
    else:
        T-=1

    if stock_final<0:
        custo_quebra = C2*(-stock_final)
        custo_semanal += custo_quebra

    custos_quebra_semanal.append(custo_quebra)
    # print(f'Custo Quebra: {custo_quebra}')

    if T==0 and stock_atual < s:

        t = random.choices(prazos,probabilidades)[0]
        prazos_entrega.append(t)
        
        q = S - stock_final
        quantidades_a_encomendar.append(q)

        T=4
    else:
        quantidades_a_encomendar.append(0)

    
    if t==0:
        stock_atual = stock_final + q
        custo_encomenda = 1500
        t = -1
    elif t == -1:
        prazos_entrega.append(0)
    else:
        t -= 1
        prazos_entrega.append(t)
    
    custo_semanal += custo_encomenda

    custos_encomenda_semanal.append(custo_encomenda)

    

    if p < stock_atual:
        custo_posse = C1*(stock_atual-p/2)
    else:
        custo_posse = C1*(stock_atual/2)

    # print(f'Custo Posse: {custo_posse}')

    custo_semanal += custo_posse
    
    custos_posse_semanal.append(custo_posse)

    # print(f'Custo Semanal: {custo_semanal}')
    custos_semanais.append(custo_semanal)

# print(custos_semanais)

custo_anual = sum(custos_semanais)

print(f'Custo Anual: {custo_anual}')

custo_semanal_medio = custo_anual/50

print(f'Custo Semanal Medio: {custo_semanal_medio}')


data = {
    'Semana': [x+1 for x in range(50)],
    'Stock Inicial': stocks_atuais,
    'Procura': procura,
    'Stock Final': stocks_finais,
    'Encomenda': quantidades_a_encomendar,
    'Prazo de Entrega': prazos_entrega,
    'Custo de Quebra': custos_quebra_semanal,
    'Custo de Encomenda': custos_encomenda_semanal,
    'Custo de Posse': custos_posse_semanal
}

df = pd.DataFrame(data)

df.to_excel(writer, sheet_name='Sheet1',index=False)


data2 = {
    'S': [S],
    's' : [s],
    'C1' : [C1],
    'C2' : [C2],
    'C3' : [C3],
    'Custo Total Anual': [custo_anual],
    'Custo Médio Semanal': [custo_semanal_medio],
    'Média DDPP': [mu],
    'Desvio Padrão DDPP': [sigma]
}

dp = pd.DataFrame(data2)

dp.to_excel(writer, sheet_name='Sheet1',index=False,startcol=10)

writer.save()