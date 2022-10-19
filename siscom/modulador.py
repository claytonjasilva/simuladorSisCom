# O módulo trata dos esquemas de modulação digital e analógica
# Cria também o mapeamento Gray para os esquemas de modulação
#

import math
import numpy as np

def sinalAM(modulante, fc, A=1, delta=1, dominio='t'):
    Ta = 1 / (20 * fc)
    t = np.array([i * Ta for i in range(len(modulante))])
    portadora = A * np.cos(2 * math.pi * fc * t)
    x = np.multiply((1 + delta * modulante), portadora)
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio =='t':
        return t, x
    else:
        return f, Xf
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

def geraSimbolos(cad_caracteres, select_mode):
    lista_binarios=[]
    lista_de_simbolos = []

    if select_mode == "1":
        for carac in cad_caracteres:
            ascii_palavra = ord(carac)
            string_binario = bin(ascii_palavra)
            string_sem_0b = string_binario.replace('0b','')
            string_completa_8_bits = string_sem_0b.zfill(8)
            lista_binarios.append(string_completa_8_bits)

            for palavra_binaria in lista_binarios:
                bits_1 = palavra_binaria[0:3]
                bits_2 = palavra_binaria[3:6]
                bits_3 = palavra_binaria[6:]

            lista_de_simbolos.append(int(bits_1, 2))
            lista_de_simbolos.append(int(bits_2, 2))
            lista_de_simbolos.append(int(bits_3, 2))

        return lista_de_simbolos

    elif select_mode == "2":
        for carac in cad_caracteres:
            ascii_palavra = ord(carac)
            string_binario = bin(ascii_palavra)
            string_sem_0b = string_binario.replace('0b','')
            string_completa_8_bits = string_sem_0b.zfill(8)
            lista_binarios.append(string_completa_8_bits)

            for palavra_binaria in lista_binarios:
                bits_1 = palavra_binaria[0:4]
                bits_2 = palavra_binaria[4:]

            lista_de_simbolos.append(int(bits_1, 2))
            lista_de_simbolos.append(int(bits_2, 2))

        return lista_de_simbolos

    else:
        print('erro! Código inválido!')

def geraSinalPAM(simbolosPAM, fc, dominio='t'):
    s = []
    d = 1
    M = 8
    gt = 1
    Tc = 1 / fc
    Fa = 50 * fc
    Ta = 1 / Fa

    t = [i * Ta for i in range(len(simbolosPAM) * int(Tc / Ta))]
    for simbolo in simbolosPAM:
        Am = ((2 * simbolo) - M) * d
        for i in range(int(Tc / Ta)):
            s.append(Am * gt * np.cos(2 * math.pi * fc * t[i]))

    Xf = np.absolute(np.fft.fft(s))
    f = np.fft.fftfreq(len(Xf), Ta)

    if dominio == 't':
        return t, s

    return f, Xf

def geraSinalPSK(simbolosPSK, fc, dominio='t'):
    s = []
    M = 8
    gt = 1
    Tc = 1 / fc
    Fa = 50 * fc
    Ta = 1 / Fa

    t = [i * Ta for i in range(len(simbolosPSK) * int(Tc / Ta))]
    for simbolo in simbolosPSK:
        for i in range(int(Tc / Ta)):
            op = (2 * math.pi * fc * t[i]) + ((2 * math.pi / M) * (simbolo - 1))
            s.append(gt * np.cos(op))

    Xf = np.absolute(np.fft.fft(s))
    f = np.fft.fftfreq(len(Xf), Ta)

    if dominio == 't':
        return t, s

    return f, Xf

def geraConstelacao(sinal):
    yf = np.fft.fft(sinal, norm="ortho")
    magnitude = np.abs(yf)
    phase = np.angle(yf)

    return magnitude, phase

def geraSinalQAM(simbolosQAM, fc, dominio='t'):
    s = []
    M = 16
    N = 16
    d = 1
    gt = 1
    Tc = 1 / fc
    Fa = 50 * fc
    Ta = 1 / Fa

    t = [i * Ta for i in range(len(simbolosQAM) * int(Tc / Ta))]
    for simbolo in simbolosQAM:
        Am = (2 * simbolo - 1 - M) * d
        phi = (2 * math.pi / N) * (simbolo - 1)
        for i in range(int(Tc / Ta)):
            op = 2 * math.pi * fc * t[i] + phi
            s.append(Am * gt * np.cos(op))

    Xf = np.absolute(np.fft.fft(s))
    f = np.fft.fftfreq(len(Xf), Ta)

    if dominio == 't':
        return t, s

    return f, Xf
