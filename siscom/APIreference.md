# API - Referência

**siscom.sinais**  

Gera funções importantes para simulação e análise de sistemas de comunicações

## siscom.sinais.degrau
A função gera o sinal degrau em função do tempo, *x(t)*

**Parâmetros**:   
 - tamanho: tipo inteiro  
 Define o número de amostras do sinal a ser produzido  
 - Ta: tipo float  
 Define o período de amostragem do sinal a ser produzido, em segundos  
 - amplitude: tipo float, *opcional*  
 Define a amplitude do sinal; o *default* é 1.0  
 - delay: tipo float
 Define o *delay* do sinal, em segundos; o *default* é 0 segundos  
 
 **Retorna**  
 - t: *array* de dimensão definida pelo tamanho  
 O *array* apresenta os instantes de tempo da amostragem do sinal produzido
 - x: *array* de dimensão definida pelo tamanho  
 O *array* apresenta o sinal amostrado em função do tempo
