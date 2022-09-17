# Módulo de funções especiais em comunicações


import matplotlib.pyplot as plt
import siscom.sinais
import siscom.codecvoz
import siscom.modulador
import siscom.canal
import numpy as np

# arquivo = 'C:/Users/Clayton J A Silva/PycharmProjects/simuladorSisCom/siscom/voz1_clayton.wav'
# a, b = siscom.codecvoz.captura(arquivo,dominioVoz='t')

r = siscom.sinais.senoide(10000,0.001,56)
h = siscom.sinais.impulso(10000,0.001,amplitude = 2)

c = siscom.canal.capacidade(r[1], h[1], 100)
print(c)
#plt.plot(t,x)
#plt.show()
