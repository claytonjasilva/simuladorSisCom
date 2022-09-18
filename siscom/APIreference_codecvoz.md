# API - Referência

**siscom.codecvoz**  

Gera funções importantes para simulação e análise de sistemas de comunicações

## siscom.sinais.captura
A função captura um arquivo .wav e gera o respectivo array 

**Parâmetros**:   
 - `arquivo`: tipo str  
 Define o nome do arquivo, no formato .wav, contendo o sinal de voz gravado.  
 Deve incluir o caminho do arquivo. O arquivo deve ser mono.
 - `dominio`: tipo caracter, *opcional*  
Define o domínio do *array* de saída; o *default* é 't'.   

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo, que contém os instantes de amostragem do sinal 
 - x: *array* do sinal de voz gravado em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* que contém as frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal degrau amostrado em função da frequência  

## siscom.sinais.amostragem
A função gera o sinal amostrado em um intervalo de amostragem Ta seg

**Parâmetros**:   
 - `sinal`: tipo array  
Define o sinal a ser amostrado, no domínio do tempo  
 - `Tasinal`: tipo float  
 Define o intervalo de amostragem do sinal lido, em segundos  
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
 - t: *array* do tempo, que contém os instantes de amostragem do sinal 
 - x: *array* do sinal amostrado em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* de frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal porta (ou pulso) amostrado em função da frequência  

## siscom.sinais.quantizado
A função gera o sinal quantizado em um intervalo de amostragem Ta seg

**Parâmetros**:   
 - `sinal`: tipo array  
Define o sinal a ser amostrado, no domínio do tempo  
 - `Ta`: tipo float  
 Define o intervalo de amostragem do sinal lido, em segundos  
 - `L`: tipo inteiro  
 Define o número de níveis de quantização

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo, que contém os instantes de amostragem do sinal 
 - x: *array* do sinal quantizado em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* de frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal quantizado em função da frequência  


## siscom.sinais.aalisasing
A função gera o sinal filtrado por um filtro passa-baixas na frequência de corte

**Parâmetros**:   
 - `sinal`: tipo array  
Define o sinal a ser filtrado, no domínio do tempo  
 - `Ta`: tipo float  
 Define o intervalo de amostragem do sinal lido, em segundos  
 - `fcorte`: tipo float  
 Define a frequência de corte, em Hertz

**Retorna**  
Se o parâmetro for o *default*:
 - t: *array* do tempo, que contém os instantes de amostragem do sinal 
 - x: *array* do sinal após filtrado em função do tempo  

Se o parâmetro dominio for diferente do *default*:
 - f: *array* de frequências em largura df = fa/tamanho = 1/(Ta x tamanho).  
f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (Ta x tamanho), se tamanho é par  
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (Ta x tamanho), se tamanho é impar 
 - Xf: *array* da amplitude do sinal filtrado em função da frequência  
