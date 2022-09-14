# Módulo de funções especiais em comunicações


import matplotlib.pyplot as plt
import siscom.sinais
import siscom.codecvoz
import siscom.modulador
import numpy as np

arquivo = 'C:/Users/Clayton J A Silva/PycharmProjects/simuladorSisCom/siscom/voz1_clayton.wav'
a, b = siscom.codecvoz.captura(arquivo,dominioVoz='f')

# t, x = siscom.modulador.sinalFM(sinal,t,10000,delta=10,dominioFM='f')

plt.plot(a,b)
plt.show()
