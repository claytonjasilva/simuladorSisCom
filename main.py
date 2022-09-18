# Módulo de funções especiais em comunicações


import matplotlib.pyplot as plt
import siscom.sinais
import siscom.codecvoz
import siscom.modulador
import siscom.canal
import numpy as np

arquivo = 'C:/Users/Clayton J A Silva/PycharmProjects/simuladorSisCom/siscom/voz1_clayton.wav'
b = siscom.codecvoz.captura(arquivo)
# tempo = np.array([i * b[0] for i in range(len(b[1]))])
t,x = siscom.codecvoz.aaliasing(b[1],b[0],2000, dominio='f')

plt.plot(t,x)
plt.show()