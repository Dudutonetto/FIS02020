#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Thu May  8 16:15:16 2025
=======
Created on Thu May  8 16:04:36 2025
>>>>>>> 216fcd564e5c44e9baa1c550a04e30bf0a250b19

@author: dudutonetto
"""
dir_dados = '/home/dudutonetto/work/Prog/Python/FIS02020/dados/'

#%% 1: Escrevendo em um arquivo (modo texto)

file1 = dir_dados + 'exemplo.txt'

with open(file1, "w") as arquivo:
    arquivo.write('Primeira linha\n')
    arquivo.write('Segunda linha\n')
    arquivo.write('Terceira linha\n')
    
    
#%% 2: Lendo arquivo linha por linha 

with open(file1, 'r') as arquivo:
    for linha in arquivo:
        #print(linha, end='')
        print(linha.strip())     # quebra a string em partes
        

#%% 3: Lendo todo conteúdo de uma vez 

with open(file1, 'r') as arquivo:
    conteudo = arquivo.read()

print(conteudo)


#%% 4: Acrescentando dados no final do arquivo 

with open(file1, 'a') as arquivo:
    arquivo.write('Mais uma linha\n')
    
    
#%% 5: Lendo e escrevendo dados tabulares com csv

import csv

file2 = dir_dados + 'stars.csv'

with open(file2, 'w', newline = '') as arquivo:
    escritor = csv.writer(arquivo)
    
    escritor.writerow(['Id', 'Dec', 'RA'])    
    escritor.writerow(['star1', -30.001, 3.415])
    escritor.writerow(['star2', -29.232, 12.789])
    escritor.writerow(['star3', +40.123, 23.123])
    
#%% 

with open(file2, 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
        
        
#%% 6: Lendo dados tabulares
import csv

file3 = dir_dados + 'dados2.cvs'

with open(file3, 'r') as fid:
    leitor = csv.reader(fid)
    matriz = []
    for linha in leitor:
        t = int(linha[0])
        x = float(linha[1])
        y = float(linha[2])
        matriz.append([t, x, y])
        
print(matriz)


#%% 

import csv

file3 = dir_dados + 'dados2.cvs'

with open(file3, 'r') as fid:
    leitor = csv.reader(fid)
    matriz = []
    for linha in leitor:
       row = [float(e) for e in linha]
       matriz.append(row)
       
print(matriz)
