# O módulo cria os siscom no domínio do tempo
# Cria também o vetor amostra do tempo com o período e amostragem
# Os siscom são não periódicos e periódicos
#

import numpy as np
import math


def degrau(tamanho, Ta, amplitude=1.0, delay=0.0, dominio='t'):
    ret = int(delay / Ta)
    t = np.array([i * Ta for i in range(tamanho)])
    x = t * 0
    for i in range(ret, tamanho):  # x = 0, t<delay; x = A, t>= delay
        x[i] = amplitude
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio=='t':
        return t, x
    else:
        return f, Xf


def porta(largura, tamanho, Ta, amplitude=1.0, delay=0.0, dominio='t'):
    ret = int(delay / Ta)
    t = np.array([i * Ta for i in range(tamanho)])
    L = int(largura / Ta)
    x = t * 0
    for i in range(ret, ret + L):  # x = 0, t<delay; x = t, t>= delay
        x[i] = amplitude
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio=='t':
        return t, x
    else:
        return f, Xf


def rampa(tamanho, Ta, delay=0.0, dominio='t'):
    ret = int(delay / Ta)
    t = np.array([i * Ta for i in range(tamanho)])
    x = t * 0
    for i in range(ret, tamanho):  # x = 0, t<delay; x = t, t>= delay
        x[i] = t[i-ret]
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio=='t':
        return t, x
    else:
        return f, Xf


def impulso(tamanho, Ta, amplitude=1.0, delay=0.0, dominio='t'):
    ret = int(delay / Ta)
    t = np.array([i * Ta for i in range(tamanho)])
    x = t * 0
    x[ret] = amplitude
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio == 't':
        return t, x
    else:
        return f, Xf


def serra(tamanho, Ta, frequencia, amplitude = 1.0, delay=0.0, dominio ='t'):
    t = np.array([i * Ta for i in range(tamanho)])
    x = t * 0
    for i in range(tamanho):  # Utiliza série infinita de Fourier
        serie = 0
        for k in range(1, 100):
            serie += (-1) ** k * math.sin(2 * math.pi * k * frequencia * (t[i] - delay)) / k
        x[i] = 2 / math.pi * serie
    x = amplitude * x / np.amax(x)
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio == 't':
        return t, x
    else:
        return f, Xf


def senoide(tamanho, Ta, frequencia, amplitude=1.0, delay=0.0, dominio='t'):
    t = np.array([i * Ta for i in range(tamanho)])
    x = amplitude * np.sin(2 * math.pi * frequencia * (t - delay))
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio == 't':
        return t, x
    else:
        return f, Xf


def triangular(tamanho, Ta, frequencia, amplitude=1.0, delay=0.0, dominio='t'):
    t = np.array([i * Ta for i in range(tamanho)])
    x = t * 0
    for i in range(tamanho):  # Utiliza série infinita de Fourier - wikipedia
        serie = 0
        for k in range(1, 100):
            serie += math.sin(k * math.pi / 2) * math.sin(k * frequencia * (t[i] - delay)) / k ** 2
        x[i] = 8 / math.pi ** 2 * serie
    x = x * amplitude / np.amax(x)
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio == 't':
        return t, x
    else:
        return f, Xf


def sinc(tamanho, Ta, frequencia, amplitude=1.0, delay=0.0, dominio='t'):
    t = np.array([i * Ta for i in range(tamanho)])
    x = amplitude * np.sinc(2 * math.pi * frequencia * (t - delay))
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio == 't':
        return t, x
    else:
        return f, Xf


def quadrada(tamanho, Ta, frequencia, amplitude=1.0, delay=0.0, dominio='t'):
    t = np.array([i * Ta for i in range(tamanho)])
    x = t * 0
    for i in range(tamanho):  # Utiliza série infinita de Fourier - wikipedia
        serie = 0
        for k in range(1, 100):
            serie += math.sin((2 * k - 1) * frequencia * (t[i]-delay)) / (2 * k - 1)
        x[i] = 4 * amplitude / math.pi * serie
    x = amplitude * x / np.amax(x)
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio == 't':
        return t, x
    else:
        return f, Xf
