def program(vector_program):
    while

########
with open ('readme.md') as arq:
        read_data = arq.read()
file_vector=list(read_data)

tam_text=len(file_vector)

if file_vector[0]!="p":
    print ("Erro Lexico")

else:
    vector_program=[]
    vector_program_name=[]
    i=0
    a=0
    while i < tam_text:
        if file_vector[i] != " ":
            if a == 0:
                vector_program.append(file_vector[i])
            if a == 1 :
                if file_vector[i] != "{": 
                    vector_program_name.append(file_vector[i])
                else:
                    a+=1
            if a==2:
                if file_vector[i] != "{":
                    print("Erro Lexico")
                a+=1         

            if i == (tam_text-1) and file_vector[i] != "}":
                print("Erro Lexico")
        else:
            a+=1
        i+=1
    
    first_word=''.join(vector_program)
    program_name=''.join(vector_program_name)
    print(first_word)
    print(program_name)
    if first_word != "program":
        print ("Erro Lexico")