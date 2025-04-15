#Questão 3 

def cancao2(n): #versão que funciona mesmo, se, por engano, tenha sido posto um float como entrada
    ''' fazendo a canção com de acordo com a padronização do
        enunciado, com relação direta com a entrada inteira n...'''
    n=int(n)

    level1="Um elefante incomoda muita gente"
    print(level1) #inciando o nível 1 --> primeira sentença da música
    unidade2=" incomodam"
    pack1=" incomodam"

    second="muita gente"
    first="muito mais"   
    for i in range(2, n+1):
        pack1=pack1+" incomodam"
        print(str.format("{} elefantes{} {}", i, pack1, first))
        if i!=n:
            print(str.format("{} elefantes{} {}", i, unidade2, second))

    print(str.format("\n\n\t\tFim"))
