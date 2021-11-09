#!/usr/bin/env python3
# -*- coding: utf-8 -*-Результаты выполнения программы:
#определите общие символы в двух строках, введенных с клавиатуры.
if __name__ == "__main__":
    str1 = set(input())
    str2 = set(input())

    #Найдём пересечение строк
    diff = str1.intersection(str2)
    print(diff)