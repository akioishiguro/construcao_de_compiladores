import sys
import re
import csv
from collections import OrderedDict

wordsDict = {"write": 0, "while": 1, "until": 2,  "to": 3,  "then": 4,  "string": 5,  "repeat": 6,  "real": 7,  "read": 8,  "program": 9,  "procedure": 10,  "or": 11,  "of": 12,  "literal": 13,  "integer": 14,  "if": 15,  "identificador": 16,  "î": 17,  "for": 18,  "end": 19,  "else": 20,  "do": 21,  "declaravariaveis": 22, "const": 23 ,"char": 24,  "chamaprocedure": 25,  "begin": 26,  "array": 27,  "and": 28,  "numreal": 36,  "numinteiro": 37, "nomestring": 38, "nomechar": 39}

symbolsDict = { ">=": 29,  ">": 30,  "=": 31,  "<>": 32,  "<=": 33,  "<": 34,  "+": 35,  "]": 40,  "[": 41,  ";": 42,  ":": 43,  "/": 44,  "..": 45,  ".": 46,  ",": 47,  "*": 48,  ")": 49,  "(": 50,  "$": 51,  "-": 52 }

with open('some.csv', 'w', newline='') as f:
        writer = csv.writer(f)

filename = "tokens.csv"
# opening the file with w+ mode truncates the file
f = open(filename, "w+")
writer = csv.writer(f, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)


def number_int(type_number):
    try: 
        int(type_number)
        return True
    except:
        return False

def num_real(type_number):
    try: 
        float(type_number)
        return True
    except:
        return False

def comentario(line_actual):
    for i in range(line_actual,num_lines):
        line=read_data_lines[i].strip()#Ignorando os espacos/tab/enter
        line_words=line.split(' ')##Dividimos as linhas em palavras
        num_line_words=len(line_words)##NUmero de palavras na linha
        for j in range(0,num_line_words):
            if line_words[j].strip():
                if line_words[j] == "*#":
                    return i+1
                elif i == num_lines-1 :
                    return False

def lexico(aux_word,aux_word_size,word,line_words):  
    if word in wordsDict:
        print("Linha:",i+1,"| Palavra:",word,"| Token:",wordsDict[word])
        print_line.append(wordsDict[word])   
     
    elif word in symbolsDict:
        print("Linha:",i+1, "| Simbolo:",word,"| Token:",symbolsDict[word])
        print_line.append(symbolsDict[word])   
    
    else:
        for k in range(0,aux_word_size):
            if aux_word[k] == '"': ##Verifica STRING
                word=" "
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
                        print("Linha:",i+1,"| Palavra:",get_name_string,"| Token:",wordsDict["nomestring"])
                        print_line.append(wordsDict["nomestring"]) 
                        break
                    else:
                        count_string+=1
                if end_string == False:
                    print ("Erro Lexico, na linha",i+1)
            
            elif aux_word[k] == "'": ##Verifica CHAR
                word=" "
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
                        print("Linha:",i+1,"| Palavra:",get_name_char,"| Token:",wordsDict["nomechar"])
                        print_line.append(wordsDict["nomechar"]) 
                        break
                    else:
                        count_char+=1
                if end_char == False:
                    print ("Erro Lexico, na linha",i+1)

            elif aux_word[k] == "`": ##Verifica LITERAL
                word=" "
                count_literal = j
                get_name_literal=[]
                get_name_literal.append(aux_word[k])
                end_literal = False
                aux_word[k]=aux_word[k].replace(aux_word[k]," ") #Troca o simbolo por espaco
                line_words[count_literal]=line_words[count_literal+1].replace(line_words[count_literal+1]," ")
                while count_literal != num_line_words-1:
                    next_symbol= line_words[count_literal+1]
                    get_name_literal.append(next_symbol)
                    line_words[count_literal+1]=line_words[count_literal+1].replace(line_words[count_literal+1]," ")
                    if next_symbol == "`":
                        end_literal = True
                        print("Linha:",i+1,"| Palavra:",get_name_literal,"| Token:",wordsDict["literal"])
                        print_line.append(wordsDict["literal"]) 
                        break
                    else:
                        count_literal+=1
                if end_literal == False:
                    print ("Erro Lexico, na linha",i+1)

        negative_number=re.findall("-", word)
        number=re.findall("[0-9]", word)
        letter=re.findall("[a-z]", word)

        if number and not negative_number and not letter:##Verifica se os numeros são positivos
            aux_type_number_int=number_int(word)
            aux_type_number_real=num_real(word)
            if aux_type_number_int == True:
                print("Linha:", i+1,"| Numero:",word,"eh POSITIVO e INTEIRO, Token:",wordsDict["numinteiro"])
                print_line.append(wordsDict["numinteiro"]) 
            elif aux_type_number_real == True and aux_type_number_int == False:
                print("Linha:", i+1,"| Numero:",word,"eh POSITIVO e REAL, Token:",wordsDict["numreal"])
                print_line.append(wordsDict["numreal"]) 
            else:
                print("Erro Lexico na linha:",i+1)
                print_line.append("ERRO") 

        elif number and negative_number and not letter:##Verifica se os numeros são positivos
            word = re.sub("-", " ",word)
            word=word.strip()
            aux_type_number_int=number_int(word)
            aux_type_number_real=num_real(word)
            if aux_type_number_int == True:
                print("Linha:", i+1,"| Numero:",word,"eh NEGATIVO e INTEIRO, Token:",wordsDict["numinteiro"])
                print_line.append(wordsDict["numinteiro"]) 
            elif aux_type_number_real == True and aux_type_number_int == False:
                print("Linha:", i+1,"| Numero:",word,"eh NEGATIVO e REAL, Token:",wordsDict["numreal"])
                print_line.append(wordsDict["numreal"]) 
            else:
                print("Erro Lexico na linha:",i+1)
                print_line.append("ERRO") 
        
        else:
            check_identifier = re.findall("[0-9|==|@|)|(|>=|>|=|<>|<=|<|+|]|[|;|:|/|..|.|,|*|'$'|-]", word)

            if check_identifier:
                print("Erro Lexico na linha:",i+1)
                print_line.append("ERRO") 
            elif  word != " ":
                print ("Linha:",i+1,"| Palavra:",word,"| Token:",wordsDict["identificador"])
                print_line.append(wordsDict["identificador"]) 
            
                
#with open(sys.argv[1]) as arq:
with open("ex1.txt") as arq:
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
                            #print('Inicio do comentario de bloco na linha:', line_actual+1,' Final do Comentario de bloco na linha:',end_blobo_comment+1)
                            break
                        else:
                            print("ERRO LEXICO NA LINHA",i+1)
                            break
                    else:
                        #print("Comentario na linha:",i+1)
                        break
                    
                aux_word=list(line_words[j])
                aux_word_size = len(aux_word)
                check_lexico=lexico(aux_word,aux_word_size,line_words[j],line_words)

    writer.writerow(print_line)

f.close()