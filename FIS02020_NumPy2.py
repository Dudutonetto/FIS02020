#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 15:49:59 2025

@author: dudutonetto
"""


#%% Ex: - Definir uma função linear
import numpy as np
import matplotlib.pyplot as plt

def xylinear(a,b,n,x1,x2):
    X = np.linspace(x1,x2,n)
    Y = a*X + b
    return np.array([X,Y])

a3 = (xylinear(2,6,10,2,10))
print(a3)

def graf(a,b,n,x1,x2):
    plt.plot(xylinear(a,b,n,x1,x2)[0],xylinear(a,b,n,x1,x2)[1],c='red',lw=2,label='Modelo')
    plt.scatter(xylinear(a,b,n,x1,x2)[0],xylinear(a,b,n,x1,x2)[1],s=50,label='Medidas')
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

graf(1.5,2,20,4,16)

#%% Exemplo 2: Definir uma função linear com erro

def xylinear(a,b,n,x1,x2,sd):
    X = np.linspace(x1,x2,n)
    erro = np.random.normal(0,sd,n)
    Y = a*X + b + erro
    return np.array([X,Y])

a3 = (xylinear(2,6,10,2,10,0))
print(a3)

def graf(a,b,n,x1,x2,sd):
    plt.plot(xylinear(a,b,n,x1,x2,0)[0],xylinear(a,b,n,x1,x2,0)[1],c='red',lw=2,label='Modelo')
    plt.scatter(xylinear(a,b,n,x1,x2,sd)[0],xylinear(a,b,n,x1,x2,sd)[1],s=50,label=f'Medidas, erro={sd}')
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

graf(1.5,2,20,4,16,0.4)

def polyfit(a,b,n,x1,x2,sd):
    p = np.polyfit(xylinear(a, b, n, x1, x2, sd)[0],xylinear(a, b, n, x1, x2, sd)[1],1)
    pa=np.polyval(p, xylinear(a, b, n, x1, x2, sd)[0])
    plt.scatter(xylinear(a,b,n,x1,x2,sd)[0],xylinear(a,b,n,x1,x2,sd)[1],s=50,label=f'Medidas, erro={sd}')
    plt.plot(xylinear(a, b, n, x1, x2, sd)[0],pa, c='r', label=f' a = {p[0]:.4f}, b = {p[1]:.4f}')
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

polyfit(2,6,20,2,10,0.8)
