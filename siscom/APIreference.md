# API - Referência

**siscom.sinais**  

Gera funções importantes para simulação e análise de sistemas de comunicações

## siscom.sinais.degrau
A função gera o sinal degrau variando com o tempo, *x(t)*, em uma janela temporal (tamanho x Ta) seg

**Parâmetros**:   
 - `tamanho`: tipo inteiro  
 Define o número de amostras do sinal a ser produzido  
 - `Ta`: tipo float  
 Define o período de amostragem do sinal a ser produzido, em segundos  
 - `amplitude`: tipo float, *opcional*  
 Define a amplitude do sinal; o *default* é 1.0  
 - `delay`: tipo float, *opcional*  
 Define o *delay* do sinal, em segundos; o *default* é 0 segundos  
 - `dominio`: tipo caracter, *opcional*  
Define o domínio do *array* de saída; o *default* é 't'.   

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo com dimensão definida pelo parâmetro `tamanho` que contém os instantes de amostragem do sinal 
 - x: *array* do sinal degrau amostrado em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* de dimensão definida pelo parâmetro tamanho que contém as frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal degrau amostrado em função da frequência  

## siscom.sinais.porta
A função gera o sinal porta (ou pulso) de largura L, variando com o tempo, *x(t)*, em uma janela temporal (tamanho x Ta) seg

**Parâmetros**:   
 - `largura`: tipo float  
Define a largura, em segundos  
 - `tamanho`: tipo inteiro  
 Define o número de amostras do sinal a ser produzido  
 - `Ta`: tipo float  
 Define o período de amostragem do sinal a ser produzido, em segundos  
 - `amplitude`: tipo float, *opcional*  
 Define a amplitude do sinal; o *default* é 1.0  
 - `delay`: tipo float, *opcional*  
 Define o *delay* do sinal, em segundos; o *default* é 0 segundos  
 - `dominio`: tipo caracter, *opcional*  
Define o domínio do *array* de saída; o *default* é 't'.   

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo com dimensão definida pelo parâmetro `tamanho` que contém os instantes de amostragem do sinal 
 - x: *array* do sinal porta (ou pulso) amostrado em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* de dimensão definida pelo parâmetro tamanho que contém as frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal porta (ou pulso) amostrado em função da frequência  

## siscom.sinais.rampa
A função gera o sinal rampa, variando com o tempo, *x(t)*, em uma janela temporal (tamanho x Ta) seg

**Parâmetros**:   
 - `tamanho`: tipo inteiro  
 Define o número de amostras do sinal a ser produzido  
 - `Ta`: tipo float  
 Define o período de amostragem do sinal a ser produzido, em segundos  
 - `delay`: tipo float, *opcional*  
 Define o *delay* do sinal, em segundos; o *default* é 0 segundos  
 - `dominio`: tipo caracter, *opcional*  
Define o domínio do *array* de saída; o *default* é 't'.   

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo com dimensão definida pelo parâmetro `tamanho` que contém os instantes de amostragem do sinal 
 - x: *array* do sinal rampa amostrado em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* de dimensão definida pelo parâmetro tamanho que contém as frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal rampa amostrado em função da frequência  

## siscom.sinais.impulso
A função gera o sinal impulso ou delta de Dirac, variando com o tempo, *x(t)*, em uma janela temporal (tamanho x Ta) seg

**Parâmetros**:   
 - `tamanho`: tipo inteiro  
 Define o número de amostras do sinal a ser produzido  
 - `Ta`: tipo float  
 Define o período de amostragem do sinal a ser produzido, em segundos  
 - `delay`: tipo float, *opcional*  
 Define o *delay* do sinal, em segundos; o *default* é 0 segundos  
 - `dominio`: tipo caracter, *opcional*  
Define o domínio do *array* de saída; o *default* é 't'.   

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo com dimensão definida pelo parâmetro `tamanho` que contém os instantes de amostragem do sinal 
 - x: *array* do sinal impulso (ou delta de Dirac) amostrado em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* de dimensão definida pelo parâmetro tamanho que contém as frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal impulso (ou delta de Dirac) amostrado em função da frequência  

## siscom.sinais.serra
A função gera o sinal dente de serra, variando com o tempo, *x(t)*, em uma janela temporal (tamanho x Ta) seg  
Utiliza série de Fourier com 100 iterações para produzir o sinal


**Parâmetros**:   
 - `tamanho`: tipo inteiro  
 Define o número de amostras do sinal a ser produzido  
 - `Ta`: tipo float  
 Define o período de amostragem do sinal a ser produzido, em segundos  
 - `frequencia`: tipo float  
Define a frequência do sinal em Hertz
 - `amplitude`: tipo float, *opcional*  
 Define a amplitude do sinal; o *default* é 1.0  
 - `delay`: tipo float, *opcional*  
 Define o *delay* do sinal, em segundos; o *default* é 0 segundos  
 - `dominio`: tipo caracter, *opcional*  
Define o domínio do *array* de saída; o *default* é 't'.   

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo com dimensão definida pelo parâmetro `tamanho` que contém os instantes de amostragem do sinal 
 - x: *array* do sinal dente de serra amostrado em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* de dimensão definida pelo parâmetro tamanho que contém as frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal dente de serra amostrado em função da frequência  

## siscom.sinais.senoide
A função gera um sinal senoidal, variando com o tempo, *x(t)*, em uma janela temporal (tamanho x Ta) seg

**Parâmetros**:   
 - `tamanho`: tipo inteiro  
 Define o número de amostras do sinal a ser produzido  
 - `Ta`: tipo float  
 Define o período de amostragem do sinal a ser produzido, em segundos  
- `frequencia`: tipo float  
Define a frequência do sinal em Hertz
 - `amplitude`: tipo float, *opcional*  
 Define a amplitude do sinal; o *default* é 1.0  
 - `delay`: tipo float, *opcional*  
 Define o *delay* do sinal, em segundos; o *default* é 0 segundos  
 - `dominio`: tipo caracter, *opcional*  
Define o domínio do *array* de saída; o *default* é 't'.   

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo com dimensão definida pelo parâmetro `tamanho` que contém os instantes de amostragem do sinal 
 - x: *array* do sinal senoidal amostrado em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* de dimensão definida pelo parâmetro tamanho que contém as frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal senoidal amostrado em função da frequência  

## siscom.sinais.triangular
A função gera sinal triangular, variando com o tempo, *x(t)*, em uma janela temporal (tamanho x Ta) seg  
Utiliza série de Fourier com 100 iterações para produzir o sinal


**Parâmetros**:   
 - `tamanho`: tipo inteiro  
 Define o número de amostras do sinal a ser produzido  
 - `Ta`: tipo float  
 Define o período de amostragem do sinal a ser produzido, em segundos  
- `frequencia`: tipo float  
Define a frequência do sinal em Hertz
 - `amplitude`: tipo float, *opcional*  
 Define a amplitude do sinal; o *default* é 1.0  
 - `delay`: tipo float, *opcional*  
 Define o *delay* do sinal, em segundos; o *default* é 0 segundos  
 - `dominio`: tipo caracter, *opcional*  
Define o domínio do *array* de saída; o *default* é 't'.   

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo com dimensão definida pelo parâmetro `tamanho` que contém os instantes de amostragem do sinal 
 - x: *array* do sinal triangular amostrado em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* de dimensão definida pelo parâmetro tamanho que contém as frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal triangular amostrado em função da frequência  

## siscom.sinais.sinc
A função gera o sinal sinc(x) = sen(pi.x)/(pi.x), variando com o tempo, *x(t)*, em uma janela temporal (tamanho x Ta) se

**Parâmetros**:   
 - `tamanho`: tipo inteiro  
 Define o número de amostras do sinal a ser produzido  
 - `Ta`: tipo float  
 Define o período de amostragem do sinal a ser produzido, em segundos  
- `frequencia`: tipo float  
Define a frequência do sinal em Hertz
 - `amplitude`: tipo float, *opcional*  
 Define a amplitude do sinal; o *default* é 1.0  
 - `delay`: tipo float, *opcional*  
 Define o *delay* do sinal, em segundos; o *default* é 0 segundos  
 - `dominio`: tipo caracter, *opcional*  
Define o domínio do *array* de saída; o *default* é 't'.   

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo com dimensão definida pelo parâmetro `tamanho` que contém os instantes de amostragem do sinal 
 - x: *array* do sinal *sinc* amostrado em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* de dimensão definida pelo parâmetro tamanho que contém as frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal *sinc* amostrado em função da frequência  

## siscom.sinais.quadrada
A função gera onda quadrada, variando com o tempo, *x(t)*, em uma janela temporal (tamanho x Ta) seg  
Utiliza série de Fourier com 100 iterações para produzir o sinal


**Parâmetros**:   
 - `tamanho`: tipo inteiro  
 Define o número de amostras do sinal a ser produzido  
 - `Ta`: tipo float  
 Define o período de amostragem do sinal a ser produzido, em segundos  
- `frequencia`: tipo float  
Define a frequência do sinal em Hertz
 - `amplitude`: tipo float, *opcional*  
 Define a amplitude do sinal; o *default* é 1.0  
 - `delay`: tipo float, *opcional*  
 Define o *delay* do sinal, em segundos; o *default* é 0 segundos  
 - `dominio`: tipo caracter, *opcional*  
Define o domínio do *array* de saída; o *default* é 't'.   

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo com dimensão definida pelo parâmetro `tamanho` que contém os instantes de amostragem do sinal 
 - x: *array* do sinal de onda quadrada amostrado em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* de dimensão definida pelo parâmetro tamanho que contém as frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal de onda quadrada amostrado em função da frequência  

