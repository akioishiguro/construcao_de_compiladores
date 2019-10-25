import json

push_table = []

parsing_table = [
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1,  0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 23, 23, -1, -1, 23, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  3,  2, -1, -1,  3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  6, -1, -1, -1,  7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 26, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, 20, -1, 21, -1, -1, -1, -1, -1, -1, 18, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19, -1, -1, 13, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  4, -1, -1, -1, -1, -1,  5, -1, -1, -1,  5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1,  9, -1, 10, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, 16, -1, 17, -1, -1, -1, -1, -1, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 25, -1, -1, -1, 25, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 24, -1, -1 ],
    [ 34, 30, 36, -1, -1, -1, 31, -1, 32, -1, -1, -1, -1, -1, -1, 29, -1, -1, 35, 36, -1, -1, -1, -1, -1, 33, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 36, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ 27, 27, -1, -1, -1, -1, 27, -1, 27, -1, -1, -1, -1, -1, -1, 27, -1, -1, 27, 28, -1, -1, -1, -1, -1, 27, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 27, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 43, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 43, 43, 43, 43, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 43, -1, -1 ],
    [ -1, -1, 70, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 70, 69, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 70, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 71, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 72, -1, 73, -1, -1, -1 ],
    [ -1, -1, 38, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 38, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 38, -1, -1, -1, -1, -1, -1, -1, 37, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 39, -1, -1, 40, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 40, 40, 40, 40, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 40, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 41, -1, 42, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 44, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 44, 44, 44, 44, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 44, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 63, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 64, 64, 64, 64, 64, 64, 61, -1, -1, -1, -1, 64, -1, -1, -1, -1, -1, -1, 64, -1, 64, -1, -1, 62 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 54, 53, 51, 56, 55, 52, -1, -1, -1, -1, -1, 57, -1, -1, -1, -1, -1, -1, 57, -1, 57, -1, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 46, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 49, 45, 47, 48, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 50, -1, -1 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 68, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 67, 68, 68, 68, 68, 68, 68, 68, -1, -1, -1, -1, 68, -1, -1, -1, 66, -1, -1, 68, 65, 68, -1, -1, 68 ],
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 60, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 58, 60, 60, 60, 60, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 60, -1, 59 ]
]

token_dictionary = [
    'write',
    'while',
    'until',
    'to',
    'then',
    'string',
    'repeat',
    'real',
    'read',
    'program',
    'procedure',
    'or',
    'of',
    'literal',
    'integer',
    'if',
    'identifier',
    'empty',
    'for',
    'end',
    'else',
    'do',
    'declaravariaveis',
    'const',
    'char',
    'chamaprocedure',
    'begin',
    'array',
    'and',
    '>=',
    '>',
    '=',
    '<>',
    '<=',
    '<',
    '+',
    'real',
    'integer',
    'string',
    'char',
    ']',
    '[',
    ';',
    ':',
    '/',
    '..',
    '.',
    ',',
    '*',
    ')',
    '(',
    '$',
    '-'
]


class Pilha(object):
    def __init__(self):
        self.dados = [51 , 53]
 
    def empilha(self, token):
        self.dados.append(token)
 
    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)
 
    def vazia(self):
        return len(self.dados) == 0



p = Pilha()
X = p.dados[-1]#Topo da pilha

with open('pushtable.json', encoding='utf-8') as json_file:
    push_table = json.loads(json_file.read())

with open("tokens.csv") as arq:
    read_data = arq.read()###read_data é o meu programa dentro de uma string

read_data_lines=read_data.split('\n')###read_data_lines, separa todo o meu programa por linhas
num_lines=len(read_data_lines)
num_words=len(read_data)##NUmero total de palavras no arquivo
aux_end_blobo_comment=0

for i in range(0, num_lines):
    print_line=[]
    line=read_data_lines[i].strip()#Ignorando os espacos/tab/enter
    line_words=line.split(' ')##Dividimos as linhas em palavras
    num_line_words=len(line_words)##NUmero de palavras na linha    
    
    for j in range(0, num_line_words):
        if line_words[j].strip():
            a = line_words[j]
            if a == "ERRO":
                print("Erro lexico na linha:",i+1)
                exit()
            a = int(a)
            while X != 51:
                X=p.dados[-1]
                if X == 17:
                    p.desempilha()
                    X = p.dados[-1]
                elif X >= 0 and X <= 52:        
                    if X == a:#simbolo de entrada:
                        p.desempilha()
                        break
                    else:
                        print('erro:', token_dictionary[X],"linha:",i+1)
                        exit()
                else: 
                    production = parsing_table[(X-53)][a]
                    if production != -1:
                        p.desempilha()
                        teste=len(push_table[str(production)])
                        production_list = push_table[str(production)]
                        production_list = production_list [::-1]
                        for token in production_list:
                            p.empilha(token)                        
                            X=p.dados[-1]
                    else:
                        print("erro inha:",i+1)
                        exit()   

            print("Finalizado!")  

