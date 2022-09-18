# O módulo trata das funções do codec - codificador-decodificador de voz
# Cria também o vetor amostra do tempo com o período e amostragem
#

from scipy.io import wavfile
import numpy as np
import siscom.sinais


def captura(arquivo, dominio='t'):
    output = wavfile.read(arquivo)  # O arquivo .wav deve ser um canal - mono
    Ta = 1 / output[0]  # Ta - período de amostragem
    x = np.array(output[1], dtype=float)  # array relativo ao arquivo de voz
    Xf = np.fft.fft(x)
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio=='t':
        return Ta, x
    else:
        return f, Xf


def amostragem(sinal, Tasinal, Ta, dominio='t'):
    N = int(Ta/Tasinal)
    x = [0.0] * len(sinal)
    for i in range(len(sinal)):
        if (i % N) == 0:
            x[i] = sinal[i]
    t = np.array([i * Tasinal for i in range(len(sinal))])
    Xf = np.fft.fft(x)
    f = np.fft.fftfreq(len(Xf), Tasinal)
    if dominio=='t':
        return t, x
    else:
        return f, Xf


def quantizado(sinal, Ta, L, dominio='t'):
    vmax = np.amax(sinal)
    vmin = np.amin(sinal)
    degrau = (vmax - vmin) / (L - 1)
    nivel = [vmin + i * degrau for i in range(L)]
    x = np.array([0.0] * len(sinal))
    for i in range(len(sinal)):  # Quantizador linear - menor distância
        decisao = [abs(sinal[i] - x[j]) for j in range(L)]
        menor = min(decisao)
        ind = decisao.index(menor)
        x[i] = nivel[ind]
    t = np.array([i * Ta for i in range(len(sinal))])
    Xf = np.fft.fft(x)
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio=='t':
        return t, x
    else:
        return f, Xf


def aaliasing(sinal, Ta, fcorte, dominio='t'):
    Sf = np.fft.fft(sinal)
    Xf = np.array([0.0] * len(Sf))
    f = np.fft.fftfreq(len(Sf), Ta)
    for i in range(len(Sf)):
        if fcorte >= abs(f[i]):
            Xf[i] = Sf[i]  # filtro passa-baixas
    x = np.fft.ifft(Xf)
    t = np.array([i * Ta for i in range(len(x))])
    if dominio=='t':
        return t, x
    else:
        return f, Xf
