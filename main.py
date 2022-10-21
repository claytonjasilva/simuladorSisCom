import matplotlib.pyplot as plt
import siscom.modulador
import siscom.canal

choose_option = input('Escolha o simulador: 1-> 8-PAM, 2-> 8-PSK, 3-> 16-QAM \n')
# simbolos = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
cad_caracteres = input('Digite um frame de uma mensagem:\n')
select_mode = input('Digite para escolher: 1 (3 bits por simbolo) ou 2 (4 bits por simbolo)\n')
simbolos = siscom.modulador.geraSimbolos(cad_caracteres, select_mode)
fc = 10000
figure, axis = plt.subplots(2)

if choose_option == "1":
    # 8-PAM
    t, x = siscom.modulador.geraSinalPAM(simbolos, fc)
    f, Xf = siscom.modulador.geraSinalPAM(simbolos, fc, 'f')
    axis[0].set_title("8-PAM - Tempo")
    axis[1].set_title("8-PAM - Frequência")

elif choose_option == "2":
    # 8-PSK
    t, x = siscom.modulador.geraSinalPSK(simbolos, fc)
    f, Xf = siscom.modulador.geraSinalPAM(simbolos, fc, 'f')
    axis[0].set_title("8-PSK - Tempo")
    axis[1].set_title("8-PSK - Frequência")

elif choose_option == "3":
    # 16-QAM
    t, x = siscom.modulador.geraSinalQAM(simbolos, fc)
    f, Xf = siscom.modulador.geraSinalQAM(simbolos, fc, 'f')
    axis[0].set_title("16-QAM - Tempo")
    axis[1].set_title("16-QAM - Frequência")

axis[0].plot(t,x)
axis[1].plot(f,Xf)
plt.show()

if choose_option == "2" or choose_option == "3":
    generateConstelation = input('Digite para escolher: 1 - Gera constelacao ou 2 - Não gera constelacao\n')
    if generateConstelation == "1":
        Ta = 1 / (50*fc)
        tR, xR = siscom.canal.sinRuido(x, Ta, 100)
        magnitude, phase = siscom.modulador.geraConstelacao(xR)
        fig = plt.figure()
        ax1 = plt.subplot(121)
        ax2 = plt.subplot(122, projection='polar')
        ax1.set_title("Sinal com ruído")
        ax1.plot(tR, xR)
        ax2.set_title("Constelação")
        ax2.scatter(magnitude, phase)
        ax2.set_rorigin(0)
        plt.grid(True)
        plt.show()