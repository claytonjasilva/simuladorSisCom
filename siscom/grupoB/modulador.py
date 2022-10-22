import matplotlib.pyplot as plt
import numpy as np
import math

fc = 0

def geraSimbolos(frame, n_simbolos=8):

    simbolos = []

    for letra in frame:
        letra = bin(ord(letra)).replace('0b', '').zfill(8)
        print(letra)
        if n_simbolos == 16:    
            for i in [0, 4]:
                simb = int(letra[i:i + 4], 2)
                simbolos.append(simb)
        else:
            for i in [0, 3, 6]:
                simb = int(letra[i:i + 3], 2)
                simbolos.append(simb)
        
    return simbolos

def geraSinalPAM(simbolos, iteracao):

    GT = 1

    sm = []
    Tc = 1 / fc
    fa = 1000 * fc
    Ta = 1 / fa
    
    t = [i * Ta for i in range(len(simbolos) * int(Tc / Ta))]
    
    count = 0

    for simbolo in simbolos:
        am = ((2 * simbolo) - 9) * 1
        for _ in range(int(Tc / Ta)):
            formula = am * GT * np.cos((2 * np.pi * fc * t[count]))
            sm.append(formula)
            count += 1
    print(len(sm))
    print(sm)
    sm = np.array(sm)

    X = np.absolute(np.fft.fft(sm))
    f = np.fft.fftfreq(len(X), Ta)

    titulo = "8-PAM Iteração:" + str(iteracao)

    fig, axs = plt.subplots(2)
    axs[0].plot(t, sm)
    axs[0].set_title("Dominio do tempo")
    axs[0].set_xlabel("Tempo")
    axs[0].set_ylabel("Amplitude")
    axs[1].plot(f, X)
    axs[1].set_title("Dominio da frequencia")
    axs[1].set_xlabel("Frequencia")
    fig.suptitle(titulo)

    plt.show()

def geraSinalPSK(simbolos, iteracao):
    GT = 1

    sm = []
    Tc = 1 / fc
    fa = 1000 * fc
    Ta = 1 / fa
    
    t = [i * Ta for i in range(len(simbolos) * int(Tc / Ta))]
    
    count = 0

    for simbolo in simbolos:
        fase = (simbolo - 1 ) / 8
        for _ in range(int(Tc / Ta)):
            formula = GT * np.cos((2 * np.pi * fc * t[count]) + (2 * np.pi * fase))
            sm.append(formula)
            count += 1
    print(len(sm))
    print(sm)
    sm = np.array(sm)

    X = np.absolute(np.fft.fft(sm))
    f = np.fft.fftfreq(len(X), Ta)

    titulo = "8-PSK Iteração:" + str(iteracao)

    fig2, axs2 = plt.subplots(2)
    axs2[0].plot(t, sm)
    axs2[0].set_title("Dominio do tempo")
    axs2[0].set_xlabel("Tempo")
    axs2[0].set_ylabel("Amplitude")
    axs2[1].plot(f, X)
    axs2[1].set_title("Dominio da frequencia")
    axs2[1].set_xlabel("Frequencia")
    fig2.suptitle(titulo)

    plt.show()

def geraSinalQAM(simbolos, iteracao):

    GT = 1

    sm = []
    Tc = 1 / fc
    fa = 1000 * fc
    Ta = 1 / fa
    
    t = [i * Ta for i in range(len(simbolos) * int(Tc / Ta))]
    
    count = 0

    for simbolo in simbolos:
        fase = (simbolo - 1 ) / 16
        am = ((2 * simbolo) - 17) * 1
        for _ in range(int(Tc / Ta)):
            formula = am * GT * np.cos((2 * np.pi * fc * t[count]) + (2 * np.pi * fase))
            sm.append(formula)
            count += 1
    print(len(sm))
    print(sm)
    sm = np.array(sm)

    X = np.absolute(np.fft.fft(sm))
    f = np.fft.fftfreq(len(X), Ta)


    titulo = "16-QAM Iteração:" + str(iteracao)

    fig3, axs3 = plt.subplots(2)
    axs3[0].plot(t, sm)
    axs3[0].set_title("Dominio do tempo")
    axs3[0].set_xlabel("Tempo")
    axs3[0].set_ylabel("Amplitude")
    axs3[1].plot(f, X)
    axs3[1].set_title("Dominio da frequencia")
    axs3[1].set_xlabel("Frequencia")
    fig3.suptitle(titulo)

    plt.show()

def geraSinalPSKRuido(simbolos, iteracao, snr):
    GT = 1

    sm = []
    Tc = 1 / fc
    fa = 1000 * fc
    Ta = 1 / fa
    
    t = [i * Ta for i in range(len(simbolos) * int(Tc / Ta))]
    
    count = 0

    for simbolo in simbolos:
        fase = (simbolo - 1 ) / 8
        for _ in range(int(Tc / Ta)):
            formula = GT * np.cos((2 * np.pi * fc * t[count]) + (2 * np.pi * fase))
            sm.append(formula)
            count += 1
    print(len(sm))
    print(sm)

    t, sm = sinRuido(sm, Ta, snr)
    f, X = sinRuido(sm, Ta, snr, dominio='f')
    yf = np.fft.fft(sm, norm='ortho')
    magnitude = np.abs(yf)
    phase = np.angle(yf)

    titulo = "8-PSK com Ruído Iteração:" + str(iteracao)

    fig2, axs2 = plt.subplots(2)
    axs2[0].plot(t, sm)
    axs2[0].set_title("Dominio do tempo")
    axs2[0].set_xlabel("Tempo")
    axs2[0].set_ylabel("Amplitude")
    axs2[1].plot(f, X)
    axs2[1].set_title("Dominio da frequencia")
    axs2[1].set_xlabel("Frequencia")
    fig2.suptitle(titulo)

    plt.show()

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(projection='polar')
    ax2.scatter(phase, magnitude)

    plt.show()

def geraSinalQAMRuido(simbolos, iteracao, snr):

    GT = 1

    sm = []
    Tc = 1 / fc
    fa = 1000 * fc
    Ta = 1 / fa
    
    t = [i * Ta for i in range(len(simbolos) * int(Tc / Ta))]
    
    count = 0

    for simbolo in simbolos:
        fase = (simbolo - 1 ) / 16
        am = ((2 * simbolo) - 17) * 1
        for _ in range(int(Tc / Ta)):
            formula = am * GT * np.cos((2 * np.pi * fc * t[count]) + (2 * np.pi * fase))
            sm.append(formula)
            count += 1
    print(len(sm))
    print(sm)

    t, sm = sinRuido(sm, Ta, snr)
    sm = np.array(sm)

    f, X = sinRuido(sm, Ta, snr, dominio='f')


    titulo = "16-QAM com Ruído Iteração:" + str(iteracao)

    fig4, axs4 = plt.subplots(2)
    axs4[0].plot(t, sm)
    axs4[0].set_title("Dominio do tempo")
    axs4[0].set_xlabel("Tempo")
    axs4[0].set_ylabel("Amplitude")
    axs4[1].plot(f, X)
    axs4[1].set_title("Dominio da frequencia")
    axs4[1].set_xlabel("Frequencia")
    fig4.suptitle(titulo)

    plt.show()

def sinRuido(sinal, Ta, SNR, dominio='t'):

    t = np.array([i * Ta for i in range(len(sinal))])
    ampl_ruido = math.sqrt(np.dot(sinal, sinal) / 10 ** (SNR / 10))
    ruido = np.random.normal(loc=0, scale=ampl_ruido, size=len(sinal))
    x = sinal + ruido
    Xf = np.absolute(np.fft.fft(x))
    f = np.fft.fftfreq(len(Xf), Ta)
    if dominio == 't':
        return t, x
    else:
        return f, Xf

def main():
    global fc
    string = input("Informa a frase a ser enviada: ")
    fc = int(input("Informe a frequencia da portadora: "))
    tipo_modulacao = input("Informe o sinal:\n1 - 8-QAM\n2 - 8-PSK\n3 - 16-QAM\n4 - 8-PSK com Ruido\n5 - 16-QAM com Ruido\n")
    SNR = 0
    
    if tipo_modulacao == '4' or tipo_modulacao == '5':
        SNR = int(input("Informe a razão sinal ruído (SNR): "))

    string_frames = 0
    count = 0
    frames = []
    
    if (len(string) / 20) % 20 == 0:
        string_frames =  int(len(string) / 20)
    else:
        string_frames = int(len(string) / 20) + 1
    
    for i in range(string_frames):
        if i == string_frames - 1:
            frames.append(string[count:])
        else:
            frames.append(string[count:count + 20])
            count += 20

    print(frames)
    iteracao = 1

    for frame in frames:
        if tipo_modulacao == '1':

            frame8 = geraSimbolos(frame)
            print("Frame8 -->", frame8, iteracao)
            geraSinalPAM(frame8, iteracao)

        elif tipo_modulacao == '2':

            frame8 = geraSimbolos(frame)
            print("Frame8 -->", frame8, iteracao)
            geraSinalPSK(frame8, iteracao)

        elif tipo_modulacao == '3':

            frame16 = geraSimbolos(frame, n_simbolos=16)
            print("Frame16 -->", frame16, iteracao)
            geraSinalQAM(frame16, iteracao)

        elif tipo_modulacao == '4':

            frame8 = geraSimbolos(frame)
            print("Frame8 -->", frame8, iteracao)
            geraSinalPSKRuido(frame8, iteracao, SNR)

        elif tipo_modulacao == '5':

            frame16 = geraSimbolos(frame, n_simbolos=16)
            print("Frame16 -->", frame16, iteracao)
            geraSinalQAMRuido(frame16, iteracao, SNR)
        iteracao += 1
        
if __name__ == "__main__":
    main()
