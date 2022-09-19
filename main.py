# Módulo de funções especiais em comunicações


import matplotlib.pyplot as plt
import siscom.sinais
import siscom.codecvoz
import siscom.modulador
import siscom.canal
import numpy as np

#arquivo = 'C:/Users/Clayton J A Silva/PycharmProjects/simuladorSisCom/siscom/voz1_clayton.wav'
#b = siscom.codecvoz.captura(arquivo)
# tempo = np.array([i * b[0] for i in range(len(b[1]))])
#mod = np.array([1.] * 30000)
#t,x = siscom.modulador.sinalAM(b[1],2300000)
#print(1/2300000)

t, x = siscom.sinais.porta(50,20000,0.01,delay=2)
plt.plot(t,x)
plt.show()