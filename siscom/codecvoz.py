# O módulo trata das funções do codec - codificador-decodificador de voz
# Cria também o vetor amostra do tempo com o período e amostragem
#

from scipy.io import wavfile
import numpy as np
import siscom.sinais


def captura(arquivo, dominioVoz='t'):
    output = wavfile.read(arquivo)  # O arquivo .wav deve ser um canal - mono
    Ta = 1 / output[0]  # Ta - período de amostragem
    x = np.array(output[1], dtype=float)  # array relativo ao arquivo de voz
    Xf = np.fft.fft(x)
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominioVoz=='t':
        return Ta, x
    else:
        return f, Xf


def amostragem(sinal, Tasinal, Ta):
    Ns = len(sinal)
    #N = int(Ta / (Tasinal / (len(sinal) - 1)))  # Número de amostras do sinal em intervalo Ta
    N = int(Ta/Tasinal)
    delta = np.array([0.0] * Ns)
    for i in range(Ns):
        if (i % N) == 0:
            t, x = siscom.sinais.impulso(Ns, Ta, delay=(i * Ta))
            delta += np.array(x)  # delta(Ta)
    x = np.multiply(sinal, delta)  # Amostragem do sinal
    t = np.array([i * (Tasinal / (len(sinal) - 1)) for i in range(Ns)])
    return t, x


def quantizado(sinal, Ta, L):
    vmax = np.amax(sinal)
    vmin = np.amin(sinal)
    degrau = (vmax - vmin) / (L - 1)
    nivel = np.array([vmin + i * degrau for i in range(L)])  # Níveis da quantização
    x = np.array([0.0] * len(sinal))
    for i in range(len(sinal)):  # Quantizador linear - menor distância
        x[i] = nivel[0]
        min = abs(sinal[i] - nivel[0])
        for j in range(1, L):
            if abs(sinal[i] - nivel[j]) < min:
                min = abs(sinal[i] - nivel[j])
                x[i] = nivel[j]
    t = np.array([i * Ta for i in range(len(sinal))])

    return t, x


def aaliasing(sinal, Ta, fcorte):
    Sf = np.absolute(np.fft.fft(sinal))
    f = np.fft.fftfreq(len(sinal), Ta)
    filtro = np.array([0.0] * len(Sf))
    for i in range(len(Sf)):
        if fcorte >= np.absolute(f[i]):
            filtro[i] = 1.0  # filtro passa-baixas
    Xf = np.multiply(Sf, filtro)
    x = np.fft.ifft(Xf)
    t = np.array([i * Ta for i in range(len(x))])
    return t, x
