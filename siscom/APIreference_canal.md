# API - Referência

**siscom.canal**  

Gera funções importantes para simulação e análise de sistemas de comunicações

## siscom.sinais.sinRuido
A função gera o sinal com o ruido gaussiano branco aditivo, *y(t) = x(t) + n(t)*, em uma janela temporal (tamanho x Ta) seg

**Parâmetros**:   
 - `sinal`: tipo n-array   
 Define o sinal no domínio do tempo  
 - `Ta`: tipo float  
 Define o período de amostragem do sinal a ser produzido, em segundos  
 - `SNR`: tipo float  
 Define a razão sinal-ruído, em dB  
 - `dominio`: tipo str, *opcional*  
Define o domínio do *array* de saída; o *default* é 't'.   

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo que contém os instantes de amostragem do sinal 
 - x: *array* do sinal mais ruídio em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* das frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal contaminado pelo ruído, amostrado em função da frequência  

## siscom.sinais.sinInterf
A função gera o sinal contaminado pelo sinal de interferência, *y(t) = x(t) + r(t)*, em uma janela temporal (tamanho x Ta) seg

**Parâmetros**:   
 - `sinal`: tipo n-array 
 Define o sinal no domínio do tempo  
 - `Ta`: tipo float  
 Define o período de amostragem do sinal a ser produzido, em segundos  
 - `SINR`: tipo float  
 Define a razão sinal-ruído interferente, em dB  
 - `interferencia`: tipo n-array  
 Define o sinal interferente no domínio da frequência
 - `dominio`: tipo str, *opcional*  
Define o domínio do *array* de saída; o *default* é 't'.   

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo que contém os instantes de amostragem do sinal 
 - x: *array* do sinal mais ruídio em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* das frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal contaminado pelo ruído, amostrado em função da frequência  

## siscom.sinais.sinGanho
A função gera o sinal com a perda do canal, *y(t) = x(t) * h(t)*, em que o operador * indica convolução, ou *Y(f) = X(f) . H(f)*  
, onde *H(f)* é a resposta de frequência do canal

**Parâmetros**:   
 - `sinal`: tipo n-array  
 Define o sinal no domínio do tempo  
 - `Ta`: tipo float  
 Define o período de amostragem do sinal a ser produzido, em segundos  
 - `Hf`: tipo n-array  
 Define a resposta do canal H(f)  
  - `dominio`: tipo str, *opcional*  
Define o domínio do *array* de saída; o *default* é 't'.   

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo que contém os instantes de amostragem do sinal 
 - x: *array* do sinal mais ruídio em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* das frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal contaminado pelo ruído, amostrado em função da frequência  

## siscom.sinais.capacidade
A função retorna a capacidade do canal de banda Bw submetido a uma razão sinal-ruído SNR

**Parâmetros**:   
 - `sinal`: tipo n-array  
 Define o sinal no domínio do tempo  
 - `ruido`: tipo n-array  
 Define o ruído no domínio do tempo  
 - `Bw`: tipo float  
 Define a largura de banda do canal, em Hz

**Retorna**  
 - `c`: tipo float, a máxima taxa de transmissão, em bits por segundo (bps) suportada pelo canal