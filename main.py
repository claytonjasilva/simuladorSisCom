# Módulo de funções especiais em comunicações


import matplotlib.pyplot as plt
import siscom.sinais
import siscom.codecvoz
import siscom.modulador
import numpy as np

arquivo = 'C:/Users/Clayton J A Silva/PycharmProjects/simuladorSisCom/siscom/voz1_clayton.wav'
a, b = siscom.codecvoz.captura(arquivo,dominioVoz='t')
#t, x = siscom.codecvoz.amostragem(b, a, 0.03)
#t = np.array([i * a for i in range(len(b))])

f, X = siscom.modulador.sinalAM(b,a,100000,dominioAM='f')

plt.plot(f,X)
plt.show()
