
def main():
    baralho = criar_baralho()
    baralho_jogador = []
    baralho_dealer = [] 
    cartas_iniciais(baralho, baralho_jogador, baralho_dealer)
    print('carta virada do dealer:', baralho_dealer[0])
    dealer(baralho, baralho_dealer)
    jogador(baralho, baralho_jogador, baralho_dealer)

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
    x = randint(0,len(baralho)-1)
    carta_sorteada = baralho[x]
    baralho.pop(x)
    return carta_sorteada

def comprar_carta(baralho, baralho_jogador):
    baralho_jogador.append(sortear_carta(baralho))
    return baralho_jogador

def dar_valor_a_carta(carta_sorteada):
    try:
        if carta_sorteada[0:2] == '10':
            valor_carta = 10
            return valor_carta
        elif int(carta_sorteada[0]) in range(1,10):
            valor_carta = int(carta_sorteada[0])
            return valor_carta
        elif carta_sorteada[0] == "A":
            valor_carta = 1 
            return valor_carta 
    except:
        valor_carta = 10
        return valor_carta

def cartas_iniciais(baralho, baralho_jogador, baralho_dealer):
    for x in range(0,2):
        baralho_jogador.append(sortear_carta(baralho))
        baralho_dealer.append(sortear_carta(baralho))
    return baralho_jogador, baralho_dealer

def contar_dealer(baralho, baralho_dealer):
    cont_dealer = 0
    for x in baralho_dealer:
        y = dar_valor_a_carta(x)
        cont_dealer = cont_dealer + y
    return cont_dealer

def dealer(baralho, baralho_dealer):
    cont_dealer = contar_dealer(baralho, baralho_dealer)
    if contar_dealer == 17:
        return baralho_dealer
    if cont_dealer == 21 or cont_dealer > 21:
        return baralho_dealer
    if len(baralho_dealer) == 5:
        return baralho_dealer
    else:
        baralho_dealer.append(sortear_carta(baralho))
        dealer(baralho, baralho_dealer)
    
def verificar_ganhou(baralho_jogador, baralho_dealer):
    cont_jog = 0
    cont_dealer = 0
    for x in baralho_jogador:
        cont_jog = cont_jog + dar_valor_a_carta(x)
    for x in baralho_dealer:
        cont_dealer = cont_dealer + dar_valor_a_carta(x)
    if cont_jog > 21:
        print('você perdeu')
        print('soma dealer:', cont_dealer)
        print('sua soma:', cont_jog)
    elif cont_dealer > 21 and cont_jog < 21:
        print('você ganhou')
        print('soma dealer:', cont_dealer)
        print('sua soma:', cont_jog)
    elif (21 - cont_jog) > (21 - cont_dealer):
        print('você perdeu')
        print('soma dealer:', cont_dealer)
        print('sua soma:', cont_jog)

def jogador(baralho, baralho_jogador, baralho_dealer):
    
    print('seu baralho é:', baralho_jogador)

    resp = input('quer comprar carta?')
    if resp.upper() == 'SIM':
        comprar_carta(baralho, baralho_jogador)
        print('seu baralho é:', baralho_jogador)
        resp = input('quer comprar mais carta?')
        if resp == 'SIM':
            jogador(baralho, baralho_jogador, baralho_dealer)
    if resp.upper() == 'NÃO' or resp.upper() == 'NAO':
        verificar_ganhou(baralho_jogador, baralho_dealer)
    else:
        print('favor escolher apenas sim ou nao.')
        jogador(baralho, baralho_jogador, baralho_dealer)
    
    resp = input('quer comprar mais carta?')


if __name__ == '__main__':
    main()