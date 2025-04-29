#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 16:30:53 2025

@author: dudutonetto
"""

# Funçoes
# Funçoes retornam um unico objeto
# def <nome_da_funçao>(arg1,arg2,...):
#   <corpo_da_funçao>

#Exemplo 1:
def sayHello():
    '''diz Hello'''
    print("Hello!!")

r= sayHello()
print(f'r = {r}')
#Exemplo 2:
def quadrado(x):
    '''retorna o quadrado de x'''
    return x**2
x2 = 5
y2 = quadrado(x2)
print(f' o quadrado de {x2} e {quadrado(5)}')

#Exemplo 3

def soma(a,b,c):
    '''soma 3 numeros'''
    s= a + b + c
    return s
A = 10
B = 15
C = 17
y3 = soma(A,B,C)
print(f' {A} + {B} + {C} = {y3}')

