
def main():
    baralho = criar_baralho()
    print('baralho criado com', len(baralho), 'cartas')
    cartas = cartas_iniciais(baralho)
    print('cartas sortada:', cartas)

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
        valor_carta = 1
        return valor_carta  
    else:
        valor_carta = 10
        return valor_carta

def cartas_iniciais(baralho):
    baralho_jogador = []
    for x in range(0,2):
        baralho_jogador.append(sortear_carta(baralho))
    return baralho_jogador


if __name__ == '__main__':
    main()