wordsDict = {"write": 0, "while": 1, "until": 2,  "to": 3,  "then": 4,  "string": 5,  "repeat": 6,  "real": 7,  "read": 8,  "program": 9,  "procedure": 10,  "or": 11,  "of": 12,  "literal": 13,  "integer": 14,  "if": 15,  "identificador": 16,  "î": 17,  "for": 18,  "end": 19,  "else": 20,  "do": 21,  "declaravariaveis": 22, "const": 23 ,"char": 24,  "chamaprocedure": 25,  "begin": 26,  "array": 27,  "and": 28,  "numreal": 36,  "numinteiro": 37, "nomestring": 38, "nomechar": 39}

symbolsDict = { ">=": 29,  ">": 30,  "=": 31,  "<>": 32,  "<=": 33,  "<": 34,  "+": 35,  "]": 40,  "[": 41,  ";": 42,  ":": 43,  "/": 44,  "..": 45,  ".": 46,  ",": 47,  "*": 48,  ")": 49,  "(": 50,  "$": 51,  "-": 52 }

def comentario(line_actual):
    for i in range(line_actual,num_lines):
        line=read_data_lines[i].strip()#Ignorando os espacos/tab/enter
        line_words=line.split(' ')##Dividimos as linhas em palavras
        num_line_words=len(line_words)##NUmero de palavras na linha
        for j in range(0,num_line_words):
            if line_words[j].strip():
                if line_words[j] == "*#":
                    return i
                elif i == num_lines-1 :
                    return False
    
def program(line_actual):
    valid=0
    for i in range(line_actual,num_lines):
        line=read_data_lines[i].strip()#Ignorando os espacos/tab/enter
        line_words=line.split(' ')##Dividimos as linhas em palavras
        num_line_words=len(line_words)##NUmero de palavras na linha
        for j in range(0,num_line_words):
            if line_words[j].strip():
                if i == line_actual and line_words[num_line_words-1].endswith(";"):
                    valid+=1
                    break
                if line_words[j] == ".":
                    valid+=1
                elif i == num_lines-1 :
                    return False
                if valid == 2:
                    return True

def lexico_word(line_actual):
    for i in range(line_actual,num_lines):
        line=read_data_lines[i].strip()#Ignorando os espacos/tab/enter
        line_words=line.split(' ')##Dividimos as linhas em palavras
        num_line_words=len(line_words)##NUmero de palavras na linha
        for j in range(0,num_line_words):
            if line_words[j].strip():
                if line_words[j] in wordsDict:
                    print ("Palavra:",line_words[j],"| Token:",wordsDict[line_words[j]],"| Na linha:",i+1)
                    
                    ###Identificador
                    if j!= num_line_words-1:
                        next_word= line_words[j+1]
                        actual_word= line_words[j]

                        if actual_word in wordsDict :
                            if next_word not in wordsDict:
                                if next_word not in symbolsDict:
                                    next_word=next_word.strip(":>=<+][;/..,*)($-")
                                    print ("Palavra:",next_word,"| Token:",wordsDict["identificador"],"| Na linha:",i+1)
                    
    return True

def lexico_symbol(line_actual):
    for i in range(line_actual,num_lines):
        line=read_data_lines[i].strip()#Ignorando os espacos/tab/enter
        line_words=line.split(' ')##Dividimos as linhas em palavras
        num_line_words=len(line_words)##NUmero de palavras na linha
        for j in range(0,num_line_words):
            if line_words[j].strip():
                aux_symbol=list(line_words[j])
                aux_symbol_size=len(aux_symbol)
                for k in range (0, aux_symbol_size):
                    if aux_symbol[k] in symbolsDict:
                        ###Simbolo Concatenado
                        if k!= aux_symbol_size-1:
                            next_symbol= aux_symbol[k+1]
                            actual_symbol= aux_symbol[k]

                            if actual_symbol in symbolsDict :
                                if next_symbol in symbolsDict:
                                    comp_symbol=actual_symbol+next_symbol
                                    if comp_symbol in symbolsDict:
                                        print ("Simbolo:",comp_symbol,"Token:",symbolsDict[comp_symbol],"| Na linha:",i+1)
                                        break
                        
                        print ("Simbolo:",aux_symbol[k],"Token:",symbolsDict[aux_symbol[k]],"| Na linha:",i+1)
    return True


with open ('arquivo_teste_1.md') as arq:
        read_data = arq.read()###read_data é o meu programa dentro de uma string


read_data_lines=read_data.split('\n')###read_data_lines, separa todo o meu programa por linhas
num_lines=len(read_data_lines)
num_words=len(read_data)##NUmero total de palavras no arquivo
aux_end_com_bloco=0
check_word=False
check_symbol=False
for i in range(0, num_lines):
    line=read_data_lines[i].strip()#Ignorando os espacos/tab/enter
    line_words=line.split(' ')##Dividimos as linhas em palavras
    num_line_words=len(line_words)##NUmero de palavras na linha
    line_actual=0
    if i>aux_end_com_bloco:
        for j in range(0, num_line_words):
            if line_words[j].strip():
                if line_words[j].startswith('#'):
                    if line_words[j].startswith('#*'):
                        line_actual=i
                        end_com_bloco=comentario(line_actual)
                        if end_com_bloco != False and aux_end_com_bloco != end_com_bloco:
                            aux_end_com_bloco=end_com_bloco
                            print('Inicio do comentario de bloco na linha:', line_actual+1,' Final do Comentario de bloco na linha:',end_com_bloco+1)
                            break
                        else:
                            print("ERRO LEXICO")
                            break
                    else:
                        print("temos um comentario na linha:",i+1)
                        break
                #elif line_words[j] == "program" :
                #    line_actual=i
                #    aux_begin=program(line_actual)
                #    if aux_begin == True:
                #        print("ok")
                #        break
                elif check_word==False:
                    line_actual=i
                    check_word=lexico_word(line_actual)

                elif check_symbol==False:
                    line_actual=i
                    check_symbol=lexico_symbol(line_actual)
                #
                #else:
                #    print("Erro na linha",i+1,"A palavra:",line_words[j],"Não existe na gramatica")