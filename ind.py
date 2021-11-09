#!/usr/bin/env python3
# -*- coding: utf-8 -*-Результаты выполнения программы:

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")
    # Определим исходные множества
    A = {'b', 'd', 'f', 'g', 'l', 'u'}
    B = {'d', 'e', 'f', 'm', 'n', 'z'}
    C = {'h', 'i', 'r', 'x', 'y'}
    D = {'a', 'e', 'f', 'k', 'r', 's', 'x'}

    X = (A.difference(B)).intersection(C.union(D))
    print(f'X = {X}')

    An = u.difference(A)
    Bn = u.difference(B)
    Y = (An.intersection(D)).union(C.difference(B))
    print(f'Y = {Y}')