import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]

    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    j = 0
    i = 0
    fi_a_fi_b = []
    soma_elementos = 0

    for elemento in as_a:
        subtrai = abs(elemento - as_b[j])
        fi_a_fi_b += [subtrai]
        j += 1

    while i < len(fi_a_fi_b):
        soma_elementos = soma_elementos + fi_a_fi_b[i]
        i = i + 1

    return soma_elementos / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    sentencas = separa_sentencas(texto) # Variável que armazena uma lista de sentencas de um texto.
    lista_frases = lista_elementos(sentencas, separa_frases) # Variável que armazena uma lista de frases de um total de sentecas.
    lista_palavras = lista_elementos(lista_frases, separa_palavras) # Variável que armazena uma lista de palavras de um total de frases.

    media_palavras = tamanho_medio(lista_palavras)
    rel_type_token = relacao_type_token(lista_palavras)
    raz_hapax_legomana = razão_hapax_legomana(lista_palavras)
    media_sentenca = tamanho_medio(sentencas)
    complex_sentenca = complexidade_sentenca(lista_frases, sentencas)
    media_frases = tamanho_medio(lista_frases)

    ass_texto = [media_palavras, rel_type_token, raz_hapax_legomana, media_sentenca, complex_sentenca, media_frases]
    
    return ass_texto

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    tam = len(textos)
    i = 0
    j = 0
    similaridades = []
    texto_posicao = 0

    while i < tam:
        texto = calcula_assinatura(textos[i])
        comparacao = compara_assinatura(texto, ass_cp)
        similaridades += [comparacao]
        i += 1

    maior_similaridade = similaridades[0]
    
    while j < len(similaridades):
        if maior_similaridade > similaridades[j]:
            maior_similaridade = similaridades[j]
            texto_posicao = j + 1
            j += 1
        else:
            j += 1

    return texto_posicao

def tamanho_medio(lista): # Função para calcular a média de caracteres de uma lista.
    soma_caracteres = 0
    tam = len(lista)
    i = 0

    while i < tam:
        soma_caracteres = soma_caracteres + len(lista[i])
        i = i + 1

    return soma_caracteres / tam

def lista_elementos(lista, separa_lista): # Função para criar uma lista de elementos a partir de outra lista.
    tam = len(lista)
    lista_elementos = []
    i = 0

    while i < tam:
        elementos = separa_lista(lista[i])
        lista_elementos.extend(elementos)
        i = i + 1

    return lista_elementos

def relacao_type_token(lista_palavras):
    palavras_diferentes = n_palavras_diferentes(lista_palavras)
    quantidade_palavras = len(lista_palavras)

    return palavras_diferentes / quantidade_palavras

def razão_hapax_legomana(lista_palavras):
    palavras_unicas = n_palavras_unicas(lista_palavras)
    quantidade_palavras = len(lista_palavras)

    return palavras_unicas / quantidade_palavras

def complexidade_sentenca(lista_frases, lista_sentencas):
    quantidade_frases = len(lista_frases)
    quantidade_sentencas = len(lista_sentencas)

    return quantidade_frases / quantidade_sentencas

ass_cp = le_assinatura()
lista_textos = le_textos()
    
resultado_avaliacao = avalia_textos(lista_textos, ass_cp)
    
print("O autor do texto", resultado_avaliacao, "está infectado com COH-PIAH")