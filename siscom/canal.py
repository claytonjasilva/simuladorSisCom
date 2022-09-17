# O módulo cria os efeitos indesejáveis do canal
# Cria também o vetor amostra do tempo com o período e amostragem
#

import numpy as np
import math
import siscom.sinais


def sinRuido(sinal, Ta, SNR, dominio='t'):
    t = np.array([i * Ta for i in range(len(sinal))])
    ampl_ruido = math.sqrt(np.dot(sinal, sinal) / 10 ** (SNR / 10))
    ruido = np.random.normal(loc=0, scale=ampl_ruido, size=len(sinal))
    x = sinal + ruido
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio == 't':
        return t, x
    else:
        return f, Xf


def sinInterf(sinal, Ta, SINR, interferencia, dominio='t'):
    t = np.array([i * Ta for i in range(len(sinal))])
    ampl_interf = math.sqrt(np.dot(sinal, sinal) / 10 ** (SINR / 10))
    print(np.linalg.norm(interferencia))
    interferencia_tempo = ampl_interf * np.fft.ifft(interferencia)
    x = sinal + interferencia_tempo
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio == 't':
        return t, x
    else:
        return f, Xf


def sinGanho(sinal, Ta, Hf, dominio='t'):
    sinalf = np.fft.fft(sinal)
    Yf = np.multiply(sinalf, Hf)
    Xf = np.absolute(Yf)
    x = np.fft.ifft(Yf)
    t = np.array([i * Ta for i in range(len(sinal))])
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio == 't':
        return t, x
    else:
        return f, Xf


def capacidade(sinal, ruido, Bw):
    SNR = np.dot(sinal, sinal) / np.dot(ruido, ruido)
    C = Bw * math.log10(1 + SNR)
    return C
