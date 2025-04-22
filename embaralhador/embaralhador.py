#Questão 2

def embaralhador2meio(pesos):
    '''função que recebe uma lista de pesos e baseada nela retorna uma lista
    com os pesos reorganizados, alternados entre maior e menor - enunciado da questão '''
    
    crescente=pesos #passando a lista de pesos para outra lista independente
    list.sort(crescente) #colocando a nova lista, com os pesos, em ordem crescente

    gerada=[] #criando uma lista vazia que armazanará os pesos na organização pedida no enunciado (organização intercalada)


    i=0 #inicializando o indicador da iteração em WHILE
    while i<len(crescente): #limitando o percurso da iteração para todos os índices da lista de pesos ordenada
        if crescente[i]<crescente[-(i+1)]: 
            list.append(gerada, crescente[-(i+1)]) 
            list.append(gerada, crescente[i]) 
        elif crescente[i]==crescente[-(i+1)]: #caso dos pesos das músicas serem iguais: os pesos não serão repetidos
            list.append(gerada,crescente[-(i+1)])
        i=i+1 #atualizando indicador iterativo

    return gerada
