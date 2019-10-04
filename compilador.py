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
    
def inicio():
    print("program")

def procedimento():
    print("procedimento")

def constante():
    print("constante")

def variavel():
    print("varialvel")

def corpo():
    print("corpo")

with open ('arquivo_teste_1.md') as arq:
        read_data = arq.read()##read_data é uma string


read_data_lines=read_data.split('\n')
num_lines=len(read_data_lines)
num_words=len(read_data)##NUmero total de palavras no arquivo
aux_end_com_bloco=0
jump=False

for i in range(0, num_lines):
    line=read_data_lines[i].strip()#Ignorando os espacos/tab/enter
    line_words=line.split(' ')##Dividimos as linhas em palavras
    num_line_words=len(line_words)##NUmero de palavras na linha
    if i>=aux_end_com_bloco:
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
                elif line_words[j] == "program" :
                    inicio()
                elif line_words[j] == "procedure":
                    procedimento()
                elif line_words[j] == "const":
                    constante()
                elif line_words[j] == "declaravariaveis":
                    variavel()
                elif line_words[j] == "begin":
                    corpo()