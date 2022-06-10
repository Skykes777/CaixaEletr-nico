def titulo(msg):
    """
    -> Função de título editada e centralizada.
    :param (msg): Mensagem a ser escrita como título.
    :return: Retorna o título editado.
    """
    print('=='*21)
    print(f'{msg:^42}')
    print('=='*21)


def linha():
    """
    Função para emprimir linhas ordenadas.
    :return: Retorna as linhas, exp..'--'.. x 20
    """
    print('--'*21)


def fpag(p, f):
    """
    -> Função para forma de pagamento.
    :param (p): Preço do produto.
    :param (f): Forma de pagamento entre 1 e 4.
    :return: Retorna a apresentação da forma de pagamento.
    """
    print('=='*21)
    if f == 1: # -DESCONTO DINHEIRO A VISTA 10%
        des10 = p * 0.10 
        totalDesconto10 = p - des10
        print(f'''PAGAMENTO: A VISTA DINH. 10% DE DESCONTO
PREÇO TOTAL: R${totalDesconto10:.2f}''')
    elif f == 2: # -DESCONTO CARTÃO A VISTA 8%
        des8 = p * 0.08
        totalDesconto8 = p - des8
        print(f'''PAGAMENTO: A VISTA CARTÃO 8% DE DESCONTO
PREÇO TOTAL: R${totalDesconto8:.2f}''')
    elif f == 3: # -PARCELAS 5X VEZES SEM JÚROS
        parcela5 = p / 5
        print(f'''PAGAMENTO: PARCELAS 5X VEZES SEM JUROS
PREÇO TOTAL: {p:.2f}
PARCELAS 5X: R${parcela5:.2f}''')
    else: # -PARCELAS 12X VEZES COM 105 DE JUROS
        juros10 = p * 0.10
        preçoTotalJuros10 = p + juros10 
        parcelas12 = preçoTotalJuros10 / 12
        print(f'''PAGAMENTO: PARCELAS 12X VEZES/ 10% JUROS
PREÇO TOTAL: {preçoTotalJuros10:.2f}
PARCELAS 5X: R${parcelas12:.2f}''')
    linha()
    print()
