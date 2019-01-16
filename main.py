
def main():
    baralho = criar_baralho()
    print('baralho criado com', len(baralho), 'cartas')
    baralho_jogador = []
    baralho_dealer = []
    cartas_iniciais(baralho, baralho_jogador)
    print('cartas jog:', baralho_jogador)
    cartas_iniciais(baralho, baralho_dealer)
    # for l1 in baralho_jogador:
    #     print(dar_valor_a_carta(l1))     
    # print('cartas dealer', baralho_dealer)
    # for l in baralho_dealer:
    #     print(dar_valor_a_carta(l))
    # print(dar_valor_a_carta(l1)+dar_valor_a_carta(l))
    jogada_jogador(baralho, baralho_jogador, baralho_dealer)

def criar_baralho():
    baralho_real = []
    letras_baralho = ['A', 'J', 'Q', 'K']
    cont = 0
    for each in letras_baralho:
        x = str(letras_baralho[cont])+'♠'
        baralho_real.append(x)
        x = str(letras_baralho[cont])+'♣'
        baralho_real.append(x)
        x = str(letras_baralho[cont])+'♥'
        baralho_real.append(x)
        x = str(letras_baralho[cont])+'♦'
        baralho_real.append(x)
        cont = cont + 1
    for each in range(2, 11):
        x = str(each)+'♠'
        baralho_real.append(x)
        x = str(each)+'♣'
        baralho_real.append(x)
        x = str(each)+'♥'
        baralho_real.append(x)
        x = str(each)+'♦'
        baralho_real.append(x)
        cont = cont + 1
    return baralho_real

class Fichas:

    def __init__(self, qtd_fichas):
        self.qtd_fichas = int(qtd_fichas)

    def __str__(self):
        return str(self.qtd_fichas)
    
    def perdeu(self, qtd_perdida):
        self.qtd_fichas = self.qtd_fichas - qtd_perdida
        return self.qtd_fichas

    def ganhou(self, qtd_ganha):
        self.qtd_fichas = self.qtd_fichas + qtd_ganha
        return self.qtd_fichas

def sortear_carta(baralho):
    from random import randint
    x = randint(0,52)
    carta_sorteada = baralho[x]
    baralho.pop(x)
    return carta_sorteada

def dar_valor_a_carta(carta_sorteada):
    try:
        if int(carta_sorteada[0]) in range(0,10):
            valor_carta = int(carta_sorteada[0])
            return valor_carta
    except:
        if carta_sorteada[0:2] == '10':
            valor_carta = 10
            return valor_carta
        elif carta_sorteada[0] == "A":
            valor_carta = 1
            return valor_carta  
        else:
            valor_carta = 10
            return valor_carta

def cartas_iniciais(baralho, baralho_atual):
    for x in range(0,2):
        baralho_atual.append(sortear_carta(baralho))
    return baralho_atual

def dealer(baralho, baralho_dealer):
    pass
            
def verificar_ganhou(baralho_jogador, baralho_dealer):
    cont_jog = 0
    cont_dealer = 0
    for x in baralho_jogador:
        cont_jog = cont_jog + dar_valor_a_carta(x)
    for x in baralho_dealer:
        cont_dealer = cont_dealer + dar_valor_a_carta(x)
    if cont_jog > 21:
        print('você perdeu!')
    elif (21 - cont_jog) > (21 - cont_dealer):
        print('você perdeu!')
    else:
        print('você ganhou!')

def jogada_jogador(baralho, baralho_jogador, baralho_dealer):

    resp = input('quer comprar carta?')

    if resp.upper() == 'SIM':
        baralho_jogador.append(sortear_carta(baralho))
        print('esse é seu baralho:', baralho_jogador)
    elif resp.upper() == 'NÃO' or resp.upper() == 'NAO':
        verificar_ganhou(baralho_jogador, baralho_dealer)
    else:
        print('favor escolher apenas sim ou nao.')
        jogada_jogador(baralho, baralho_jogador, baralho_dealer)


if __name__ == '__main__':
    main()