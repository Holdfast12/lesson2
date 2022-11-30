#!/usr/bin/python3
from decimal import Decimal

a = Decimal(input('Введите первое число: '))
b = Decimal(input('Введите второе число: '))

print(f'\n\n---Результаты для чисел {a} и {b}---\n\tСложение:\t{a+b}\n\tВычитание:\t{a-b}\n\tУмножение:\t{a*b}\n\tДеление:\t{a / b}\nВозведение в степень:\t{a**b}\nДеление по модулю:\t{a % b}\nЦелочисленное деление:\t{a//b}')