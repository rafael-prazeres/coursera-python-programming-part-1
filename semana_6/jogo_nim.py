def test_computador_escolhe_jogada():

    ''' 1 - Testa se computador_escolhe_jogada usa a estratégia vencedora (n = 14, m = 4)
        2 - Testa se computador_escolhe_jogada usa a estratégia vencedora (n = 13, m = 4)
        3 - Testa jogada do computador quando é impossível usar a estratégia vencedora (n = 15, m = 4)
            Quando não é possível usar a estratégia vencedora, computador_escolhe_jogada deve remover m peças do tabuleiro
        4 - Checando partida unica (n = 9, m = 2, jogadas = (1, 2, 2))
            Computador deveria ter ganhado
        5 - Checando campeonato (partida 1: n = 5, m = 3, jogadas = [1]; partida 2: n = 5, m = 3, jogadas = [2]; partida 3: n = 9, m = 2, jogadas = [1, 2, 2])
            Computador deveria ter ganhado'''
    
    assert computador_escolhe_jogada(14,4) == 4

    assert computador_escolhe_jogada(13,4) == 3

    assert computador_escolhe_jogada(15,4) == 4

    assert computador_escolhe_jogada(11,4) == 1

    

def computador_escolhe_jogada(n,m):
    '''Recebe, como parâmetros, os números o número de peças restantes no tabuleiro (n) e o número máximo de peças que é possível
    tirar em uma rodada (m) e devolve um inteiro (proxima_jogada) correspondente à próxima jogada do computador de acordo com a estratégia vencedora.'''

    #return utilizar_estrategia_vencedora_primeira_tentativa(n,m)
    #return utilizar_estrategia_vencedora_segunda_tentativa(n,m)
    return utilizar_estrategia_vencedora_corrigida(n,m)

def usuario_escolhe_jogada(n,m):
    ''' Recebe, como parâmetros, os números o número de peças restantes no tabuleiro (n) e o número máximo de peças que é possível
    tirar em uma rodada (m). Solicita que o jogador informe sua jogada e verifica se o valor informado é válido. Se o valor informado for válido,
    a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.'''

    peças_restantes = n
    qtd_max_peças_rodada = m
    jogada_valida = False

    while not jogada_valida:
        jogada_vitima = int(input("Quantas peças você vai tirar? "))
        if jogada_vitima >= 1 and jogada_vitima <= qtd_max_peças_rodada and jogada_vitima <= peças_restantes:
            jogada_valida = True
        else:
            print("Oops! Jogada inválida! Tente de novo.\n")
    return jogada_vitima

def partida():
    
    ''' Não recebe nenhum parâmetro,  solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre jogadas do computador e
    do usuário (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente.
    A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam na mesa.
    Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ga  nhou!" conforme o caso.

    Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no tabuleiro e qual é o máximo de peças a retirar em cada jogada.'''

    n = int(input("Quantas peças? "))
    m = int(input("limite de peças por jogada? "))

    computador = 1
    vitima = 2
    peças_restantes = n
    qtd_max_peças_rodada = m
    
    if peças_restantes % (qtd_max_peças_rodada + 1) == 0:
        print("\nVocê começa!\n")
        proximo_jogador = vitima
    else:
        print("\nComputador começa!\n")
        proximo_jogador = computador

    while peças_restantes > 0:
        
        if proximo_jogador == computador:
            proxima_jogada = computador_escolhe_jogada(peças_restantes, qtd_max_peças_rodada)
            peças_restantes = peças_restantes - proxima_jogada
            if proxima_jogada > 1:
                print("O computador tirou", proxima_jogada,"peças.")
            else:
                print("O computador tirou uma peça.")
            proximo_jogador = vitima
        else:
            proxima_jogada = usuario_escolhe_jogada(peças_restantes, qtd_max_peças_rodada)
            peças_restantes = peças_restantes - proxima_jogada
            if proxima_jogada > 1:
                print("\nVocê tirou", proxima_jogada,"peças.")
            else:
                print("\nVocê tirou uma peça.")
            proximo_jogador = computador
        if peças_restantes > 1:
            print("Agora restam",peças_restantes,"peças no tabuleiro.\n")
        elif peças_restantes == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")

    if proximo_jogador == vitima:
        print("Fim do jogo! O computador ganhou!")
        return computador
    elif proximo_jogador == computador:
        print("Fim do jogo! Você ganhou!")
        return vitima

def campeonato():
    
    '''Como todos sabemos, uma única rodada de um jogo não é suficiente para definir quem é o melhor jogador. Assim, uma vez que a função partida esteja funcionando, você
    deverá criar uma outra função chamada campeonato. Essa nova função deve realizar três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e
    indicar o vencedor do campeonato. O placar deve ser impresso na forma Placar: Você ??? X ??? Computador'''

    print("\nVocê escolheu um campeonato!")
    rodada = 1
    computador = 1
    vitima = 2
    partidas_vencidas_vitima = 0
    partidas_vencidas_computador = 0
    while rodada <= 3:
        print("\n**** Rodada",rodada,"****\n")
        vencedor_partida = partida()
        if vencedor_partida == computador:
            partidas_vencidas_computador = partidas_vencidas_computador + 1
        elif vencedor_partida == vitima:
            partidas_vencidas_vitima = partidas_vencidas_vitima + 1
        rodada = rodada + 1

    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você ", partidas_vencidas_vitima," X ", partidas_vencidas_computador," Computador")

def selecionar_modo_partida():
    opcao_partida_isolada = 1
    opcao_campeonato = 2
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")

    opcao = int(input("2 - para jogar um campeonato "))

    if opcao == opcao_partida_isolada:
        print("\nVocê escolheu uma partida isolada!\n")
        partida()
    elif opcao == opcao_campeonato:
        campeonato()

def utilizar_estrategia_vencedora_primeira_tentativa(n,m): # essa função tá bugada... testar começaando com qtd_max_peças_rodada = 1 e ir incrementando até m
    peças_restantes = n
    qtd_max_peças_rodada = m
    if qtd_max_peças_rodada > peças_restantes:
        qtd_max_peças_rodada = peças_restantes
    else:
        while qtd_max_peças_rodada >= 1:
            if (peças_restantes - qtd_max_peças_rodada) % (qtd_max_peças_rodada + 1) != 0:
                qtd_max_peças_rodada = qtd_max_peças_rodada - 1
            else:
                break
    if qtd_max_peças_rodada == 0 and peças_restantes >= m:
        qtd_max_peças_rodada = m
    
    return qtd_max_peças_rodada

def utilizar_estrategia_vencedora_segunda_tentativa(n,m): # essa função tá bugada... testar começaando com qtd_max_peças_rodada = 1 e ir incrementando até m
    peças_restantes = n
    qtd_max_peças_jogada = m
    qtd_peças_jogada = 1

    
    if qtd_max_peças_jogada >= peças_restantes:
        qtd_peças_jogada = peças_restantes
    else:
        while qtd_peças_jogada <= qtd_max_peças_jogada:
            if (peças_restantes - qtd_peças_jogada) % (qtd_peças_jogada + 1) != 0:
                qtd_peças_jogada = qtd_peças_jogada + 1
            else:
                break

    if qtd_peças_jogada > qtd_max_peças_jogada and peças_restantes >= qtd_max_peças_jogada:
        qtd_peças_jogada = qtd_max_peças_jogada
    
    return qtd_peças_jogada

def utilizar_estrategia_vencedora_corrigida(n,m):
    peças_restantes = n
    qtd_max_peças_jogada = m
    qtd_peças_jogada = qtd_max_peças_jogada
    
    if qtd_max_peças_jogada >= peças_restantes:
        qtd_peças_jogada = peças_restantes
    else:
        while qtd_peças_jogada >= 1:
            if (peças_restantes - qtd_peças_jogada) % (qtd_max_peças_jogada + 1) != 0:
                qtd_peças_jogada = qtd_peças_jogada - 1
            else:
                break

    if qtd_peças_jogada == 0:
        qtd_peças_jogada = qtd_max_peças_jogada
    
    return qtd_peças_jogada


def main():
    selecionar_modo_partida()

main()
