#!/bin/python3


# **kwargs


def resultado_f1(p1,p2,p3):
    print(f'1, {p1}'),
    print(f'2, {p2}')
    print(f'3, {p3}')


podium = {'p1': 'wastappen','p2': 'Luis','p3': 'hamilton'}
resultado_f1(*podium)
resultado_f1(**podium)