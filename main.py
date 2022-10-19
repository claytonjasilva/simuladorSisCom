import matplotlib.pyplot as plt
import siscom.modulador

choose_option = input('Escreva o simulador que deseja utilizar: 8-PAM, 8-PSK ou 16-QAM \n')
# simbolos = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
cad_caracteres = input('Digite um frame de uma mensagem:\n')
select_mode = input('Digite para escolher: 1 (3 bits por simbolo) ou 2 (4 bits por simbolo)\n')
simbolos = siscom.modulador.geraSimbolos(cad_caracteres, select_mode)
fc = 10000
figure, axis = plt.subplots(2)

match choose_option:
    case "8-PAM":
        # 8-PAM
        t, x = siscom.modulador.geraSinalPAM(simbolos, fc)
        f, Xf = siscom.modulador.geraSinalPAM(simbolos, fc, 'f')
        axis[0].set_title("8-PAM - Tempo")
        axis[1].set_title("8-PAM - Frequência")

    case "8-PSK":
        # 8-PSK
        t, x = siscom.modulador.geraSinalPSK(simbolos, fc)
        f, Xf = siscom.modulador.geraSinalPAM(simbolos, fc, 'f')
        axis[0].set_title("8-PSK - Tempo")
        axis[1].set_title("8-PSK - Frequência")

    case "16-QAM":
        # 16-QAM
        t, x = siscom.modulador.geraSinalQAM(simbolos, fc)
        f, Xf = siscom.modulador.geraSinalQAM(simbolos, fc, 'f')
        axis[0].set_title("16-QAM - Tempo")
        axis[1].set_title("16-QAM - Frequência")


axis[0].plot(t,x)
axis[1].plot(f,Xf)
plt.show()