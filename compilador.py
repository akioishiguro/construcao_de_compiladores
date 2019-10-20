import sys
import re

wordsDict = {"write": 0, "while": 1, "until": 2,  "to": 3,  "then": 4,  "string": 5,  "repeat": 6,  "real": 7,  "read": 8,  "program": 9,  "procedure": 10,  "or": 11,  "of": 12,  "literal": 13,  "integer": 14,  "if": 15,  "identificador": 16,  "î": 17,  "for": 18,  "end": 19,  "else": 20,  "do": 21,  "declaravariaveis": 22, "const": 23 ,"char": 24,  "chamaprocedure": 25,  "begin": 26,  "array": 27,  "and": 28,  "numreal": 36,  "numinteiro": 37, "nomestring": 38, "nomechar": 39}

symbolsDict = { ">=": 29,  ">": 30,  "=": 31,  "<>": 32,  "<=": 33,  "<": 34,  "+": 35,  "]": 40,  "[": 41,  ";": 42,  ":": 43,  "/": 44,  "..": 45,  ".": 46,  ",": 47,  "*": 48,  ")": 49,  "(": 50,  "$": 51,  "-": 52 }

words_name_print=[]
words_token_print=[]
words_line_print=[]

symbols_name_print=[]
symbols_token_print=[]
symbols_line_print=[]

def print_words(words_name_print):
    size_words_name_print=len(words_name_print)
    for i in range(0,size_words_name_print):
        print("Palavra:",words_name_print[i],"| Token:",words_token_print[i],"| Linha:",words_line_print[i])

def print_symbols(symbols_name_print):
    size_symbols_name_print=len(symbols_name_print)
    for i in range(0,size_symbols_name_print):
        print("Simbolo:",symbols_name_print[i],"| Token:",symbols_token_print[i],"| Linha:",symbols_line_print[i])

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

def lexico(aux_word,aux_word_size,line_words):  
    for k in range(0,aux_word_size):
        if aux_word[k] in symbolsDict:  #Verifica se o Simbolo esta presente na gramatica
            if k!= aux_word_size-1: #Verifica se o Simbolo eh Concatenado
                next_symbol= aux_word[k+1]
                actual_symbol= aux_word[k]
                if actual_symbol in symbolsDict and next_symbol in symbolsDict:
                    comp_symbol=actual_symbol+next_symbol
                    if comp_symbol in symbolsDict:
                        symbols_name_print.append(comp_symbol)
                        symbols_token_print.append(symbolsDict[comp_symbol])
                        symbols_line_print.append(i+1)
                        #print ("Simbolo:",comp_symbol,"Token:",symbolsDict[comp_symbol],"| Na linha:",i+1)
                        break                 
            #print ("Simbolo:",aux_word[k],"Token:",symbolsDict[aux_word[k]],"| Na linha:",i+1)
            symbols_name_print.append(aux_word[k])
            symbols_token_print.append(symbolsDict[aux_word[k]])
            symbols_line_print.append(i+1)

            aux_word[k]=aux_word[k].replace(aux_word[k]," ") #Troca o simbolo por espaco
        
        elif aux_word[k] == '"':
            count_string = j
            get_name_string=[]
            get_name_string.append(aux_word[k])
            aux_word[k]=aux_word[k].replace(aux_word[k]," ") #Troca o simbolo por espaco
            end_string = False
            line_words[count_string]=line_words[count_string+1].replace(line_words[count_string+1]," ")
            while count_string != num_line_words-1:
                next_symbol= line_words[count_string+1]
                get_name_string.append(next_symbol)
                line_words[count_string+1]=line_words[count_string+1].replace(line_words[count_string+1]," ")
                if next_symbol == '"':
                    end_string = True
                    words_name_print.append(get_name_string)
                    words_token_print.append(wordsDict["nomestring"])
                    words_line_print.append(i+1)
                    break
                else:
                    count_string+=1
            if end_string == False:
                print ("Erro Lexico, na linha",i+1)

        elif aux_word[k] == "'":
            count_char = j
            get_name_char=[]
            get_name_char.append(aux_word[k])
            end_char = False
            aux_word[k]=aux_word[k].replace(aux_word[k]," ") #Troca o simbolo por espaco
            line_words[count_char]=line_words[count_char+1].replace(line_words[count_char+1]," ")
            while count_char != num_line_words-1:
                next_symbol= line_words[count_char+1]
                get_name_char.append(next_symbol)
                line_words[count_char+1]=line_words[count_char+1].replace(line_words[count_char+1]," ")
                if next_symbol == "'":
                    end_char = True
                    words_name_print.append(get_name_char)
                    words_token_print.append(wordsDict["nomechar"])
                    words_line_print.append(i+1)
                    break
                else:
                    count_char+=1
            if end_char == False:
                print ("Erro Lexico, na linha",i+1)

    new_string="".join(map(str,aux_word)).strip().split(' ')
    num_new_string=len(new_string)

    for l in range (0,num_new_string):
        if new_string[l].strip():
            if new_string[l] in wordsDict:
                    words_name_print.append(new_string[l])
                    words_token_print.append(wordsDict[new_string[l]])
                    words_line_print.append(i+1)
                    #print ("Palavra:",new_string[l],"| Token:",wordsDict[new_string[l]],"| Na linha:",i+1)
            else:
                if new_string[l] not in symbolsDict:#Falat verificar algumas coisassss
                    if new_string[l].isdigit() == True:
                        break
                    else:
                        check_identifier = re.findall("[0-9|==|@]", new_string[l])

                        if check_identifier:
                            print("Erro Lexico na linha:",i+1)
                        else:
                            words_name_print.append(new_string[l])
                            words_token_print.append(wordsDict["identificador"])
                            words_line_print.append(i+1)
                            #print ("Palavra:",new_string[l],"| Token:",wordsDict["identificador"],"| Na linha:",i+1)
                   
def number_int(type_number):
    try: 
        int(type_number)
    except:
        return False

def num_real(type_number):
    try: 
        float(type_number)
    except:
        return False

def number(aux_number,aux_number_size,line_words,line_actual):
    possible_negative_number=False
    for i in range(0,aux_number_size):
        count=0
        if i != aux_number_size-1:
            next_number= aux_number[i+1]
            actual_number= aux_number[i]
            
            if possible_negative_number ==True:#Numero negativo
                if actual_number == " " and  next_number.isdigit() == True:
                    count=i
                    count+=1
                    get_number=[]
                    get_number.append(next_number)
                    while count != aux_number_size-1:
                        next_number= aux_number[count+1]
                        if next_number.isdigit() == True or next_number == ".":
                            get_number.append(next_number)
                            count+=1
                        else:
                            break                       
                    type_number="".join(map(str,get_number))             
                    aux_type_number=number_int(type_number)
                    if aux_type_number == False:
                        num_real(type_number)
                        print("Numero: -",type_number,"eh NEGATIVO e REAL, Token:",wordsDict["numreal"],"| Linha:", line_actual+1)
                    else:
                        print("Numero: -",type_number,"eh NEGATIVO e INTEIRO, Token:",wordsDict["numinteiro"],"| Linha:", line_actual+1)
                    continue

            possible_negative_number = False
            
            if actual_number == "-" and next_number.isdigit() == True: #Sinal de menos
                count=i
                count+=1
                get_number=[]
                get_number.append(next_number)
                while count != aux_number_size-1:
                    next_number= aux_number[count+1]
                    if next_number.isdigit() == True or next_number == ".":
                        get_number.append(next_number)
                        count+=1
                    else:
                        break
                type_number="".join(map(str,get_number))
                aux_type_number=number_int(type_number)
                if aux_type_number == False:
                    num_real(type_number)
                    print("Numero:",type_number,"eh POSITIVO e REAL, Token:",wordsDict["numreal"],"| Linha:", line_actual+1)
                else:
                    print("Numero:",type_number,"eh POSITIVO e INTEIRO, Token:",wordsDict["numinteiro"],"| Linha:", line_actual+1)
                continue

            elif actual_number == "-" and next_number==" ":#Verifica se o numero pode ser ou não negativo
                possible_negative_number=True
                line_words = [w.replace('-', ' ') for w in line_words]

            elif (actual_number ==" " and  next_number.isdigit() == True):
                count=i
                count+=1
                get_number=[]
                get_number.append(next_number)
                while count != aux_number_size-1:
                    next_number= aux_number[count+1]
                    if next_number.isdigit() == True or next_number == ".":
                        get_number.append(next_number)
                        count+=1
                    else:
                        break
                type_number="".join(map(str,get_number))
                aux_type_number=number_int(type_number)
                if aux_type_number == False:
                    num_real(type_number)
                    print("Numero:",type_number,"eh POSITIVO e REAL, Token:",wordsDict["numreal"],"| Linha:", line_actual+1)
                else:
                    print("Numero:",type_number,"eh POSITIVO e INTEIRO, Token:",wordsDict["numinteiro"],"| Linha:", line_actual+1)
                continue       
    return line_words

#with open(sys.argv[1]) as arq:
with open("ex1.txt") as arq:
    read_data = arq.read()###read_data é o meu programa dentro de uma string

read_data_lines=read_data.split('\n')###read_data_lines, separa todo o meu programa por linhas
num_lines=len(read_data_lines)
num_words=len(read_data)##NUmero total de palavras no arquivo
aux_end_blobo_comment=0

for i in range(0, num_lines):
    line=read_data_lines[i].strip()#Ignorando os espacos/tab/enter
    line_words=line.split(' ')##Dividimos as linhas em palavras
    num_line_words=len(line_words)##NUmero de palavras na linha
    line_actual=0
    ck_number=False
    if i>=aux_end_blobo_comment:
        for j in range(0, num_line_words):
            if line_words[j].strip():
                if line_words[j].startswith('#'):
                    if line_words[j].startswith('#*'):
                        line_actual=i
                        end_blobo_comment=comentario(line_actual)
                        if end_blobo_comment != False and aux_end_blobo_comment != end_blobo_comment:
                            aux_end_blobo_comment=end_blobo_comment
                            print('Inicio do comentario de bloco na linha:', line_actual+1,' Final do Comentario de bloco na linha:',end_blobo_comment+1)
                            break
                        else:
                            print("ERRO LEXICO")
                            break
                    else:
                        print("Comentario na linha:",i+1)
                        break

                elif i>aux_end_blobo_comment:
                    check_number=re.findall("[0-9]", line)
                    
                    if check_number:
                        if ck_number==False:
                            aux_number=list(line)
                            aux_number_size = len(aux_number)
                            line_words=number(aux_number,aux_number_size,line_words,i)
                            ck_number=True
                    
                aux_word=list(line_words[j])
                aux_word_size = len(aux_word)
                check_lexico=lexico(aux_word,aux_word_size,line_words)

print_words(words_name_print)
print_symbols(symbols_name_print)