# O módulo trata dos esquemas de modulação digital e analógica
# Cria também o mapeamento Gray para os esquemas de modulação
#

import math
import numpy as np

def sinalAM(modulante, Ta, fc, delta=1, A=1, dominioAM='t'):
    # O simulador representa um sinal modulante modulado em amplitude por uma onda portadora
    # Simula também o comportamento espectral do sinal resultante
    # A é amplitude da portadora, delta é coeficiente de modulação
    TN = len(modulante) * Ta # tempo de observação
    t = np.array([i * Ta for i in range(len(modulante))])
    #x = np.multiply((1 + delta * modulante), A * np.cos(2 * math.pi * fc * t))
    x = A * np.cos(2 * math.pi * fc * t)
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)

    if dominioAM =='t':
        return t, x
    else:
        return f, Xf


def sinalSSB(modulante, Ta, fc, delta=1, A=1):
    # O simulador representa um sinal senoidal modulado em SSB por uma onda portadora
    # Simula também o comportamento espectral do sinal resultante
    # A é amplitude da portadora, delta é coeficiente de modulação
    f, Xf_am = sinalAM(modulante, Ta, fc, delta, A, dominioAM='f')
    filtro = np.array([0.0] * len(Xf_am))
    for i in range(len(Xf_am)):
        if fc >= np.absolute(f[i]):
            filtro[i] = 1.0  # filtro passa-baixas
    Xf = np.multiply(Xf_am, filtro)
    return f, Xf


def sinalFM(modulante, Ta, fc, delta=1, A=1, dominioFM='t'):
    # O simulador representa um sinal modulante modulado em frequencia por uma onda portadora
    # Simula também o comportamento espectral do sinal resultante
    # A é amplitude da portadora, delta é coeficiente de modulação

    t = np.array([i * Ta for i in range(len(modulante))])
    x = A * np.cos(2 * math.pi * (fc + delta * modulante) * t)
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)

    if dominioFM == 't':
        return t, x
    else:
        return f, Xf