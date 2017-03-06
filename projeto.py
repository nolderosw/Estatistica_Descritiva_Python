# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:31:14 2017

@author: wesley150
"""

# importando bibliotecas necessárias

import pandas as pd

import matplotlib.pyplot as plt

from math import *

dados = pd.read_csv('gripe.csv') #leitura do arquivo por meio da biblioteca pandas

#Exclusão das colunas que não quero analisar
del dados['Distrito Federal']
del dados['Rio Grande do Sul']
del dados['Santa Catarina']
del dados['São Paulo']

#Percorrendo a coluna de datas para achar a data 22 de janeiro de 2006 para começar a analise
for i in range(len(dados)):
    if (dados.get_value(i,'Date') == '2006-01-22'):
        posicao_data = i
#crio um novo dataframe apenas a partir da posição da data 22 de janeiro de 2006
dados = dados[posicao_data:]

print "\n~~~Medidas de Posição~~~" #calculo de medidas de posição por meio de funções prontas da biblioteca pandas.
print "\nMedia dos valores observados:\n\n", dados.mean()
print "\nMediana dos valores observados:\n\n", dados.median()
print "\nModa dos valores observados:\n\n", dados.ix[:, dados.columns != 'Date'].mode()
print "\n~~~Medidas de Dispersão~~~" #calculo de medidas de dispersão por meio de funções prontas da biblioteca pandas.
print "\nAmplitude dos valores observados:\n\n", dados.ix[:, dados.columns != 'Date'].max() - dados.ix[:, dados.columns != 'Date'].min()
print "\nVariância dos valores observados:\n\n", dados.var()
print "\nDesvio Padrão dos valores observados:\n\n", dados.std()
print "\nDesvio Absoluto dos valores observados:\n\n", dados.mad()
print "\nCovariância dos valores observados:\n\n", dados.cov()
print "\nCorrelação dos valores observados:\n\n", dados.corr()

#calculo do numero de classes e das frequencias em cada classe para cada estado e para os dados nacionais.

n_ceara = dados.describe()['Ceará']['count']
k_ceara = int(round(sqrt(n_ceara)))
classes_ceara = pd.cut(dados['Ceará'], k_ceara)
frequencias_ceara = pd.value_counts(classes_ceara, sort = False)

n_minas = dados.describe()['Minas Gerais']['count']
k_minas = int(round(sqrt(n_minas)))
classes_minas = pd.cut(dados['Minas Gerais'], k_minas)
frequencias_minas = pd.value_counts(classes_minas, sort = False)

n_rio = dados.describe()['Rio de Janeiro']['count']
k_rio = int(round(sqrt(n_rio)))
classes_rio = pd.cut(dados['Rio de Janeiro'], k_rio)
frequencias_rio = pd.value_counts(classes_rio, sort = False)

n_parana = dados.describe()['Paraná']['count']
k_parana = int(round(sqrt(n_parana)))
classes_parana = pd.cut(dados['Paraná'], k_parana)
frequencias_parana = pd.value_counts(classes_parana, sort = False)

n_br = dados.describe()['Brazil']['count']
k_br = int(round(sqrt(n_br)))
classes_br = pd.cut(dados['Brazil'], k_br)
frequencias_br = pd.value_counts(classes_br, sort = False)

#Exibição na tela das tabelas de frequencias calculadas

print "\nTabela de frequencias simples absolutas do Ceará:\n\n", frequencias_ceara
print "\nTabela de frequencias simples absolutas de Minas Gerais:\n\n", frequencias_minas
print "\nTabela de frequencias simples absolutas do Rio de Janeiro:\n\n", frequencias_rio
print "\nTabela de frequencias simples absolutas do Paraná:\n\n", frequencias_parana
print "\nTabela de frequencias simples absolutas do Brazil:\n\n", frequencias_br

#Gerando o boxplot para todos os Estados e para o Brasil
plt.figure(1)
plt.style.use('seaborn-white')
#plt.style.available <-- mostra os estilos de graficos disponiveis! (está aqui para lembrar para próximos projetos)
plt.title('Boxplot Nacional e dos Estados')
dados.boxplot()

#Gerando histogramas para todos os Estados e para o Brasil
plt.figure(2)
plt.style.use('ggplot')
plt.style.available
plt.xlabel('Class')
dados['Ceará'].plot.hist(bins = k_ceara, grid = True, title = 'Histograma do Ceara')
plt.figure(3)
plt.xlabel('Class')
dados['Minas Gerais'].plot.hist(bins = k_minas, grid = True, title = 'Histograma de Minas Gerais')
plt.figure(4)
plt.xlabel('Class')
dados['Rio de Janeiro'].plot.hist(bins = k_rio, grid = True, title = 'Histograma do Rio de Janeiro')
plt.figure(5)
plt.xlabel('Class')
dados['Paraná'].plot.hist(bins = k_parana, grid = True, title = 'Histograma do Parana')
plt.figure(6)
plt.xlabel('Class')
dados['Brazil'].plot.hist(bins = k_br, grid = True, title = 'Histograma Nacional')











