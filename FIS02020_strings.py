#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 13 15:41:38 2025

@author: dudutonetto
"""

#%% Aspas triplas

docstring = '''

Strings na linguagem Python

'''
print(docstring)

#%% Escape de caracteres

s = 'abc/ndef/nghi'
print(s)

tab1= 'tabc/tdef/tghi'
tab2= '123/t456/t789'

print(tab1)
print(tab2)

#%% Métodos da classe str
# 1, Transformação de Maiúsculas em minúsculas

s = 'abc DEF'
print(s)
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.swapcase())

#%% 2 Métodos para pesquisa e localização

s = 'Linguagem Python'

print(s.find('g'))
print(s.find('g',4))
print(s.find('x'))

print(s.rfind('y'))
print(s.index("g"))
#print(s.indes("x"))

print(s.count("g"))

print(s.find("gem"))

#%% 3 Métodos para verificações booleanas

print(s.startswith("Lin"))
print(s.endswith("hon"))

print('abc12'.isalpha()) #Retorna se são letras
print('1234'.isdigit()) #Retorna se são apenas dígitos
print('12.34'.isdigit())
print('iv'.isdigit())

print('abc123'.isalnum())

print(' '.isspace())
print('abc'.islower())
print('ab c'.islower())
print('ABC'.isupper())

print("Porto Alegre".istitle())

#%% 4 Remoção de espaços e caracteres

print('  oi  '.strip())
print('  oi  '.lstrip())
print('  oi  '.rstrip())

print('-xyz-'.strip("-"))

#%% 5 Substituição e Divisão

x = '123.48'
print()
print(x.replace(".",","))

s= "1,11,23,45"
print(s.split(','))

s2= "1 11 23 45"
print(s2.split(" "))

s2= "1  11  23  45"
print(s2.split(" "))

s3= "1/t11/t23/t45"
print(s3.split("/t"))

print(s3.replace("/t", "/n"))

#%% 6 Alinhamento e preenchimento

print()
print("py".center(10,"."))
print("py".ljust(10,"."))
print("py".rjust(10,"."))
print('42'.zfill(5))

#%% Exemplos
#1. Formatação de coordenadas

ra = 10.684
dec = 41.269

c = f'RA: {ra:6.2f}\u00b0, DEC: {dec:6.2f}\u00b0'

print()
print(c)

# 2. Interpretação de cabeçalho

header = '# id | RA(deg) | DEC(deg) | Magnitude_v'

print(header.split('#')[1].replace(' ','').split('|'))
print(header.replace('#','').replace(' ','').split('|'))
print(header.lstrip('#').replace(' ','').split('|'))

#3. Gerar nome de arquivos

objeto= "M61"
data = "2025-05-13"
banda = "H_alpha"

filename = f'{objeto}_{banda}_{data}.fit'

print(filename)

#%%

obj_name = "SDSSJ123456.78+123456.7"

def sintax(obj_name):
    if len(obj_name) != 23:
        return False
    if not obj_name.startswith("SDSSJ"):
        return False
    for i in range(5,11):
        if not obj_name[i].isdigit():
            return False
    if not obj_name[11] in (".", ","):
            return False
    for i in range(12,14):
        if not obj_name[i].isdigit():
            return False
    if not obj_name[14] in ['+','-']:
        return False
    for i in range(15,21):
       if not obj_name[i].isdigit():
           return False
    if not obj_name[21] in (".", ","):
        return False
    if not obj_name[22].isdigit():
       return False  
    else:
        return True
if sintax(obj_name) == True:
    print("A sintaxe está correta")
else:
    print("A sintaxe está incorreta")