#QUESTÃO 3 --> CANÇÃO PADRONIZADA DO ELEFANTE

def cancao2meio(n):
    ''' de acordo com a entrada inteira n, esta função retorna a canção padronizada do elefante
    como idicando no enunciado da questão.'''

    level1="Um elefante incomoda muita gente" #frase inicial da canção sempre
    print(level1) #inciando o nível 1 
    unidade2=" incomodam" #salvando string que será usada várias vezes ao longo do código em uma variável
    pack1=unidade2 #iniciando o armazenador de strings que será modificado a cada iteração

    second="muita gente"
    first="muito mais" #-->strings que serão úteis
    
    for i in range(2, n+1): #iteração FOR -> do primeiro 'round' da música até o último
        pack1=pack1+unidade2 #atualização do armazenador por 'round'
        print(str.format("{} elefantes{} {}", i, pack1, first)) #inicializando linha principal do 'round'/linha sujeita a mudanças a cada iteração/'round'
        if i!=n: #casos diferentes do último 'round'
            print(str.format("{} elefantes{} {}", i, unidade2, second)) #inicializando a linha padrão da canção -> todo 'round' menos o último

    print(str.format("\n\n\t\tFim")) #finalinzando a canção
