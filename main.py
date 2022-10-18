# Módulo de funções especiais em comunicações


import matplotlib.pyplot as plt
# import siscom.sinais
# import siscom.codecvoz
import siscom.modulador
# import siscom.canal

#arquivo = 'C:/Users/Clayton J A Silva/PycharmProjects/simuladorSisCom/siscom/voz1_clayton.wav'
#b = siscom.codecvoz.captura(arquivo)
# tempo = np.array([i * b[0] for i in range(len(b[1]))])
#mod = np.array([1.] * 30000)
#t,x = siscom.modulador.sinalAM(b[1],2300000)
#print(1/2300000)

# simbolos = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
cad_caracteres = input('Digite um frame de uma mensagem:\n')
select_mode = input('Digite para escolher: 1 (3 bits por simbolo) ou 2 (4 bits por simbolo)\n')
simbolos = siscom.modulador.geraSimbolos(cad_caracteres, select_mode)
fc = 10000
figure, axis = plt.subplots(2)

# 8-PSM
t, x = siscom.modulador.geraSinalPAM(simbolos, fc)
f, Xf = siscom.modulador.geraSinalPAM(simbolos, fc, 'f')
axis[0].set_title("8-PSM - Tempo")
axis[1].set_title("8-PSM - Frequência")

# 8-PSK
# t, x = siscom.modulador.geraSinalPSK(simbolos, fc)
# f, Xf = siscom.modulador.geraSinalPAM(simbolos, fc, 'f')
# axis[0].set_title("8-PSK - Tempo")
# axis[1].set_title("8-PSK - Frequência")

# 16-QAM
# t, x = siscom.modulador.geraSinalQAM(simbolos, fc)
# f, Xf = siscom.modulador.geraSinalQAM(simbolos, fc, 'f')
# axis[0].set_title("16-QAM - Tempo")
# axis[1].set_title("16-QAM - Frequência")


axis[0].plot(t,x)
axis[1].plot(f,Xf)
plt.show()