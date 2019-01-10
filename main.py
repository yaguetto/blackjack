
def main():
    baralho = criar_baralho()
    print('baralho criado com', len(baralho), 'cartas')
    sortear_carta(baralho)
    print('carta sortada:',baralho)

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
    if carta_sorteada[0] == int(carta_sorteada[0]) or carta_sorteada[0:2] == '10':
        valor_carta = carta_sorteada[0]
        return valor_carta
    elif carta_sorteada[0] == "A":
        y = carta_sorteada[0]
        def carta_as(y):
            carta_a = input('quer que a carta seja 1 ou 11?')
            if carta_a == '1' or carta_a == '11':
                valor_carta = int(carta_a)
                return valor_carta
            else:
                carta_a = input('escolha apenas 1 ou 11:')
                carta_as(carta_a)
    else:
        valor_carta = 10
        return valor_carta

if __name__ == '__main__':
    main()