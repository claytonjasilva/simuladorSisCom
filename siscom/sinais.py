# O módulo cria os siscom no domínio do tempo
# Cria também o vetor amostra do tempo com o período e amostragem
# Os siscom são não periódicos e periódicos
#

import numpy as np
import math


def degrau(tamanho, Ta, amplitude=1, delay=0):
    ret = int(delay / Ta)
    t = np.array([i * Ta for i in range(tamanho)])
    x = t * 0
    for i in range(ret, tamanho):  # x = 0, t<delay; x = A, t>= delay
        x[i] = amplitude
    return t, x


def porta(largura, tamanho, Ta, amplitude=1, delay=0):
    ret = int(delay / Ta)
    t = np.array([i * Ta for i in range(tamanho)])
    L = int(largura / Ta)
    x = t * 0
    for i in range(ret, ret + L):  # x = 0, t<delay; x = t, t>= delay
        x[i] = amplitude
    return t, x


def rampa(tamanho, Ta, delay=0):
    ret = int(delay / Ta)
    t = np.array([i * Ta - delay for i in range(tamanho)])
    x = t * 0
    for i in range(ret, tamanho):  # x = 0, t<delay; x = t, t>= delay
        x[i] = t[i]
    return t, x


def impulso(tamanho, Ta, amplitude=1, delay=0):
    ret = int(delay / Ta)
    t = np.array([i * Ta for i in range(tamanho)])
    x = t * 0
    x[ret] = amplitude
    return t, x


def serra(frequencia, tamanho, Ta, delay=0):
    t = np.array([i * Ta - delay for i in range(tamanho)])
    x = []
    for i in range(tamanho):  # Utiliza série infinita de Fourier
        serie = 0
        for k in range(1, 100):
            serie += (-1) ** k * math.sin(2 * math.pi * k * frequencia * t[i]) / k
        x.append(2 / math.pi * serie)
    return t, x


def senoide(frequencia, tamanho, Ta, amplitude=1, delay=0):
    t = np.array([i * Ta - delay for i in range(tamanho)])
    x = amplitude * np.sin(2 * math.pi * frequencia * t)
    return t, x


def triangular(frequencia, tamanho, Ta, delay=0):
    t = np.array([i * Ta - delay for i in range(tamanho)])
    x = []
    for i in range(tamanho):  # Utiliza série infinita de Fourier - wikipedia
        serie = 0
        for k in range(1, 100):
            serie += math.sin(k * math.pi / 2) * math.sin(k * frequencia * t[i]) / k ** 2
        x.append(8 / math.pi ** 2 * serie)
    return t, x


def sinc(frequencia, tamanho, Ta, amplitude=1, delay=0):
    t = np.array([i * Ta - delay for i in range(tamanho)])
    x = amplitude * np.sinc(2 * math.pi * frequencia * t)
    return t, x


def quadrada(frequencia, tamanho, Ta, amplitude=1, delay=0):
    t = np.array([i * Ta - delay for i in range(tamanho)])
    x = []
    for i in range(tamanho):  # Utiliza série infinita de Fourier - wikipedia
        serie = 0
        for k in range(1, 100):
            serie += math.sin((2 * k - 1) * frequencia * t[i]) / (2 * k - 1)
        x.append(4 * amplitude / math.pi * serie)
    return t, x
