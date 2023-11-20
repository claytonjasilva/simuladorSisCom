# Bernardo James
# Bernardo Paschoal
# Matheus Jannotti
# Gabriel Lage
# Vinícius Mendes
# Renan Habib

# Importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

# Definindo uma função para ler os bits de um arquivo
def ler_bits_do_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        bits = arquivo.read().replace('\n', '')  # Lê o conteúdo do arquivo e remove quebras de linha
    return bits

# Definindo uma função para codificar os bits usando repetição
def codificador_repeticao(bits, d):
    bits_codificados = ''.join([bit * d for bit in bits])  # Repete cada bit 'd' vezes
    return bits_codificados

# Definindo uma função para codificar os bits usando paridade
def codificador_parity(bits, k):
    bits_codificados = bits
    while len(bits_codificados) % k != 0:
        bits_codificados += '0'  # Preenche com zeros até que o comprimento seja múltiplo de k
    
    blocos = [bits_codificados[i:i+k] for i in range(0, len(bits_codificados), k)]  # Divide em blocos de tamanho k
    blocos_codificados = []
    for bloco in blocos:
        bit_parity = str(bloco.count('1') % 2)  # Calcula o bit de paridade (paridade ímpar)
        blocos_codificados.append(bit_parity + bloco)  # Adiciona o bit de paridade ao início do bloco
    
    return ''.join(blocos_codificados)

# Definindo uma função para modular os símbolos
def modular_simbolos(bits, tipo_modulacao):
    simbolos = []
    for i in range(0, len(bits), 2):
        simbolo = bits[i:i+2]
        if tipo_modulacao == '4-PAM':
            amplitude = 1.0
            simbolos.append(amplitude * (2 * int(simbolo, 2) - 3))  # Mapeia os bits para amplitudes em 4-PAM
        elif tipo_modulacao == '2-PSK':
            amplitude = 1.0
            fase = np.pi * int(simbolo, 2)
            simbolos.append(amplitude * np.exp(1j * fase))  # Mapeia os bits para fases em 2-PSK
        elif tipo_modulacao == '8-QAM':
            amplitude = 1.0
            parte_real = 2 * int(simbolo[0], 2) - 1
            parte_imaginaria = 2 * int(simbolo[1], 2) - 1
            simbolos.append(amplitude * (parte_real + 1j * parte_imaginaria))  # Mapeia os bits para amplitudes em 8-QAM

    return simbolos

# Definindo uma função para plotar a forma de onda dos símbolos
def plotar_forma_onda(simbolos, ciclos=4):
    tempo = np.linspace(0, ciclos, len(simbolos), endpoint=False)
    plt.plot(tempo, np.real(simbolos))  # Plota a parte real dos símbolos em função do tempo
    plt.title('Forma de Onda')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.show()

# Definindo uma função para plotar a constelação dos símbolos com ruído
def plotar_constelacao(simbolos, desvio_padrao_ruido=0.1):
    simbolos_com_ruido = simbolos + np.random.normal(0, desvio_padrao_ruido, len(simbolos))
    plt.scatter(np.real(simbolos_com_ruido), np.imag(simbolos_com_ruido))  # Plota a constelação com ruído
    plt.title('Constelação com Ruído')
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginária')
    plt.show()

# Bloco principal do programa
if __name__ == "__main__":
    caminho_arquivo = 'sequencia_bits.txt'  # Atualize com o caminho do seu arquivo
    d_repeticao = 2
    k_parity = int(input('Informe o tamanho do bloco (k) para codificação de paridade: '))
    tipo_modulacao = input('Informe o tipo de modulação (4-PAM, 2-PSK, 8-QAM): ')

    # Passo 1: Ler bits do arquivo
    bits = ler_bits_do_arquivo(caminho_arquivo)

    # Passo 2: Codificação por repetição
    bits_codificados_repeticao = codificador_repeticao(bits, d_repeticao)

    # Passo 3: Codificação de paridade
    bits_codificados_parity = codificador_parity(bits_codificados_repeticao, k_parity)

    # Passo 4: Modular símbolos
    simbolos = modular_simbolos(bits_codificados_parity, tipo_modulacao)

    # Passo 5: Plotar forma de onda
    plotar_forma_onda(simbolos)

    # Passo 6: Plotar constelação com ruído
    plotar_constelacao(simbolos)
