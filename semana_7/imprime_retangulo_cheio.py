def imprime_retangulo_cheio(largura, altura):
    i = 1
    while i <= altura:
        j = 1
        while j <= largura:
            print('#', end='')
            j = j + 1
        print()
        i = i + 1

def imprime_retangulo_vazado(largura, altura):
    posicao_linha = 1
    while posicao_linha <= altura:
        posicao_coluna = 1
        while posicao_coluna <= largura:
            if caractere_esta_na_borda(posicao_linha, posicao_coluna, largura, altura):
                print('#', end='')
            else:
                print(' ', end='')
            posicao_coluna = posicao_coluna + 1
        print()
        posicao_linha = posicao_linha + 1

def caractere_esta_na_borda(posicao_linha, posicao_coluna, largura, altura):
    resposta = False
    if posicao_linha == 1 or posicao_linha == altura or posicao_coluna == 1 or posicao_coluna == largura:
        resposta = True
    return resposta
    

def main():
    l = int(input('digite a largura: '))
    a = int(input('digite a altura: '))
    imprime_retangulo_cheio(l,a)
    #imprime_retangulo_vazado(l,a)

main()
