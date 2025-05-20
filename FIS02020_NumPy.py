#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 15:46:46 2025

@author: dudutonetto
"""
import numpy as np
import matplotlib.pyplot as plt

#%% Usando Listas
xl= [0,1,2,3,4,5,6,7,8,9,10]
nxl= []
yl = []
for x in xl:
    x = x/10
    x = x*np.pi
    nxl.append(x)
    y=np.sin(x)
    yl.append(y)
plt.plot(nxl,yl)
plt.show()
#%% Usando Arrays
x = [0,1,2,3,4,5,6,7,8,9,10]

x2=np.array(x)
x2 = x2/10
x2 = x2*np.pi    
y = np.sin(x2)
plt.plot(x2,y)
plt.show()

#%% 

a = np.array([1,2,3])
print(a)

b = np.array([[1,2], [3,4]])
print(b)

c = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]],
    [[9,10],[11,12]]
    ])
print(c)

d = np.zeros(10)
print(d)

e = np.ones(10)
print(e)

e2 = np.ones(5)*2
print(e2)

f = np.linspace(0,10,5)
print(f)

#%% Exemplo 2
def y(x):
 y = 5*np.sin(x)*np.cos(x)
 return y

intervalo = np.linspace(-3*np.pi,3*np.pi)

plt.plot(intervalo,y(intervalo))
plt.xlabel("x")
plt.ylabel("y")
plt.show()

mask = (intervalo >= -np.pi) & (intervalo <= np.pi)
print(mask)
x2 = intervalo[mask]
y2 = 5*np.sin(x2)*np.tan(x2)
plt.plot(x2,y2)
plt.show()
#%% Bingo

import numpy as np
import matplotlib.pyplot as plt

aposta = [2, 22, 44, 66, 88]

#Gerar 1000 números inteiros aleatórios entre 1 e 100
sorteio = np.random.randint(1,100,1000)

mask = (sorteio == aposta[0]) | (sorteio == aposta[1]) | (sorteio == aposta[2]) | (sorteio == aposta[3]) | (sorteio == aposta[4])
resultado = sorteio[mask]
print(resultado)
#%%
mask = (np.isin(sorteio, aposta))
print(sorteio[mask])
