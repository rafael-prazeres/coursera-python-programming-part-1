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
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve
        devolver o grau de similaridade nas assinaturas.'''
    grau_similaridade = 0
    qtd_tracos_linguisticos = 6
    for i in range(len(as_a)):
        grau_similaridade += abs(as_a[i] - as_b[i])
        #print(as_a[i], " - ", as_b[i], " = ", as_a[i] - as_b[i])
    grau_similaridade = grau_similaridade / qtd_tracos_linguisticos
    return grau_similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a
        assinatura do texto.'''
    lista_palavras = lista_palavras_texto(texto)
    assinatura = []
    assinatura.append(calcula_tamanho_medio_de_palavra(lista_palavras))
    assinatura.append(calcula_relacao_type_token(lista_palavras))
    assinatura.append(calcula_razao_hapax_legomana(lista_palavras))
    assinatura.append(calcula_tamanho_medio_de_sentenca(texto))
    assinatura.append(calcula_complexidade_media_da_sentenca(texto))
    assinatura.append(calcula_tamanho_medio_de_frase(texto))
    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma
        assinatura ass_cp e deve devolver o numero (1 a n) do texto
        com maior probabilidade de ter sido infectado por COH-PIAH.'''
    graus_similaridade = []
    texto_provavelmente_infectado = 0
    for i in range(len(textos)):
        graus_similaridade.append(compara_assinatura(calcula_assinatura(textos[i]), ass_cp))                         
    for i in range(1, len(graus_similaridade)):
        if (graus_similaridade[i] < graus_similaridade[i - 1]):
            texto_provavelmente_infectado = i 
    return texto_provavelmente_infectado + 1

def calcula_tamanho_medio_de_frase(texto):
    lista_frases = []
    soma_numero_caracteres_cada_frase = 0
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            lista_frases.append(frase)
            soma_numero_caracteres_cada_frase += len(frase)
    return soma_numero_caracteres_cada_frase / len(lista_frases)

def calcula_complexidade_media_da_sentenca(texto):
    lista_sentencas = separa_sentencas(texto)
    numero_total_frases = 0
    for sentenca in lista_sentencas:
        numero_total_frases += len(separa_frases(sentenca))
    return numero_total_frases / len(lista_sentencas)

def calcula_tamanho_medio_de_sentenca(texto):
    lista_sentencas = separa_sentencas(texto)
    soma_numero_caracteres_todas_sentencas = 0
    for sentenca in lista_sentencas:
        soma_numero_caracteres_todas_sentencas += len(sentenca)
    return soma_numero_caracteres_todas_sentencas / len(lista_sentencas)

def calcula_razao_hapax_legomana(lista_palavras):
    return n_palavras_unicas(lista_palavras) / len(lista_palavras)

def calcula_relacao_type_token(lista_palavras):
    return n_palavras_diferentes(lista_palavras) / len(lista_palavras)

def calcula_tamanho_medio_de_palavra(lista_palavras):
    soma_tamanhos_palavras = 0
    for palavra in lista_palavras:
        soma_tamanhos_palavras = soma_tamanhos_palavras + len(palavra)
    return soma_tamanhos_palavras / len(lista_palavras)

def lista_palavras_texto(texto):
    lista_palavras = []
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            for palavra in separa_palavras(frase):
                lista_palavras.append(palavra)
    return lista_palavras

def main():
    assinatura_coh_piah = le_assinatura()
    print()
    textos_avaliacao = le_textos()
    texto_provavelmente_infectado = avalia_textos(
        textos_avaliacao,assinatura_coh_piah
        )
    print()
    print("O autor do texto ", texto_provavelmente_infectado,
          " está infectado com COH-PIAH")
main()
