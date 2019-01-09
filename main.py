
def main():
    baralho = criar_baralho()
    print('baralho criado com', len(baralho), 'cartas')


    # ♠ ♣ ♥ ♦
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

if __name__ == '__main__':
    main()