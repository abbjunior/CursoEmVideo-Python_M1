# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if  n1 > n2 and n1 > n3:
    print('{} é o maior'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} é o maior'.format(n2))
else:
    print('{} é o maior'.format(n3))


if  n1 < n2 and n1 < n3:
    print('{} é o menor'.format(n1))
elif n2 < n1 and n2 < n3:
    print('{} é o menor'.format(n2))
else:
    print('{} é o menor'.format(n3))
