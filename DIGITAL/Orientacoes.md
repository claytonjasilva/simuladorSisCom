# Orientações Gerais sobre o simulador 
## Codificador de canal, Modulador e Gerador de constelação

O sistema utiliza Python.  
**Funcionalidades**:  
	1.	Ler uma sequência de n bits de uma fonte discreta, de um arquivo .txt.  
	2.	Implementa um codificador de canal que implemente codificador de repetição, com d=2.   
	3.	Implementa um codificador de canal que implemente codificador com d=1, paridade ímpar, definindo o tamanho do bloco, *k*, selecionado pelo usuário.  
	4.	Gera os símbolos da modulação digital da sequência codificada de bits. O usuário pode selecionar três tipos de modulação: 4-PAM, 2-PSK ou 8-QAM. Arbitrar amplitude e fases dos esquemas de modulação.  
	5.	Plota a forma de onda correspondente ao símbolo produzido pelo modulador. Admitir um intervalo de símbolos com 4 ciclos.  
	6.	Plota a constelação de símbolos admitindo ruido aditivo sobre os símbolos transmitidos.  
