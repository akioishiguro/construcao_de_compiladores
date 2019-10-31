Manual:
	- Tudo que se encontra em amarelo, são alterações feitas pelo grupo para à etapa atual.

analisador_lexico.py:
	- Para compilar o programa, deve-se escrever: python3 analisador_lexico.py segunda"nome_do_arquivo.txt"
		-Ex: python3 analisador_lexico.py ex1.txt

analisador_sintatico.py:
	- Para compilar o programa, deve-se escrever: python3 analisador_sintatico.py
		-Isto fara que ele compile o exemplo analisado pelo analisador lexico.

token.csv e tokens_syntax_analisys.csv :
	- No arquivo token.csv, temos os tokens gerados pelos analisador léxico. Vale ressaltar, que neste arquivo temos os tokens distribuídos da mesma forma que o exemplo que o compõe.

	-Por outro lado, no arquivo tokens_syntax_analisys.csv, temos estes mesmos tokens, gerados em apenas uma linha, para que o analisador sintático possa verificá lo.

pushtable.json:
	-Neste arquivo temos a tabela de produções utilizada no analisador sintático.

ex1.txt, ex2.txt e ex3.txt:
	-Estes três arquivos, são os exemplos a serem usados para testar o compilador.

