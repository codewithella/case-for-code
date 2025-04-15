#Questão 2


def embaralhador1(pesos):
    '''função que recebe uma lista de pesos e baseada nela gera uma lista
    de acordo uma lógica(encunciado) sobre os pesos dados como entrada.'''
    tobig=pesos
    tosmall=pesos
    list.sort(tobig) #pondo os pesos em ordem crescente
    list.sort(tosmall, reverse=True) #pondo os pesos em ordem decrescente

    gerada=[]
    
    for i in range(len(tosmall)):
        if tosmall[i]<=tobig[i]:
            list.append(gerada,tosmall[i])
            list.append(gerada, tobig[i])
    return gerada
            




def embaralhador2(pesos):
    '''função que recebe uma lista de pesos e baseada nela gera uma lista
    de acordo uma lógica(encunciado) sobre os pesos dados como entrada.'''
    crescente=pesos
    list.sort(crescente) #colocando a lista de pesos em ordem crescente

    gerada=[]
    
    i=0 #pensando na iteração já.
    while i<len(crescente):
        if crescente[i]<=crescente[-(i+1)]:
            list.append(gerada, crescente[-(i+1)]) #adicionando música com maior peso primeiro
            list.append(gerada, crescente[i])
        i=i+1

    return gerada


def embaralhador3(pesos): #versão sem repetição de músicas, não foi especificado no enunciado.
    crescente = pesos
    list.sort(crescente)
    gerada=[0]
    for i in range(len(crescente)):
        p=-(i+1)
        if crescente[i]<crescente[p]:
            list.append(gerada, crescente[p])
            list.append(gerada, crescente[i])
        elif crescente[i]==crescente[p]:
            list.append(crescente[i])
    return gerada
