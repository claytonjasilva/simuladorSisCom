# Módulo de funções especiais em comunicações


import matplotlib.pyplot as plt
import siscom.sinais
import siscom.codecvoz
import siscom.modulador
import numpy as np

# arquivo = 'C:/Users/Clayton J A Silva/PycharmProjects/simuladorSisCom/siscom/voz1_clayton.wav'
# a, b = siscom.codecvoz.captura(arquivo,dominioVoz='t')

t, x = siscom.sinais.quadrada(10000,0.001, 50, amplitude=2.0, delay=2.8, dominio='f')

plt.plot(t,x)
plt.show()
