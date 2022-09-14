# O módulo cria os efeitos indesejáveis do canal
# Cria também o vetor amostra do tempo com o período e amostragem
#

import numpy as np
import math
import siscom.sinais


def sin_ruido(sinal, Ta, SNR):
    t = np.array([i * Ta for i in range(len(sinal))])
    ampl_ruido = math.sqrt(np.dot(sinal, sinal) / 10 ** (SNR / 10))
    ruido = np.random.normal(loc=0, scale=ampl_ruido, size=len(sinal))
    x = sinal + ruido
    return t, x


def sin_interf(sinal, Ta, SINR, interferencia):
    t = np.array([i * Ta for i in range(len(sinal))])
    ampl_interf = math.sqrt(np.dot(sinal, sinal) / 10 ** (SINR / 10))
    interferencia_tempo = ampl_interf * np.fft.ifft(interferencia) / np.linalg.norm(interferencia)
    x = sinal + interferencia_tempo

    return t, x


def sin_ganho(sinal, Ta, Gf):
    t = np.array([i * Ta for i in range(len(sinal))])
    Xf = np.fft.fft(sinal)
    Yf = np.dot(Xf, Gf)
    y = np.fft.ifft(Y)

    return t, y


def capacidade(sinal, ruido, Bw):
    SNR = np.dot(sinal, sinal) / np.dot(ruido, ruido)
    C = Bw * math.log10(1 + SNR)
    return C
