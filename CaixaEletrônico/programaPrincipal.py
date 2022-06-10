from modulos import titulo, linha, fpag

total_compras = []
produto = {}
preçotot = 0

# -PROGRAMA PRINCIPAL
while True:
    titulo('SUPERMERCADO_VIAMÃO-RS')
    while True:
        # -ENTRADA DE DADOS
        produto['nome_produto'] = input('Produto: ').strip().title()
        produto['preço'] = float(input('Preço: R$'))
        preçotot += produto['preço']
        total_compras.append(produto.copy())
        produto.clear()
        # -CONDIÇÃO PARA ENTRADA DE NOVOS DADOS
        continuar = input(
            'Adicionar mais produtos >>> [\033[31mS\033[m(sim)/\033[31mN\033[m(não)]: ').strip().upper()[0]
        while continuar not in 'SN':
            continuar = input(
                'Adicionar mais produtos >>> [\033[31mS\033[m(sim)/\033[31mN\033[m(não)]: ').strip().upper()[0]
        if continuar == 'N':
            break
    # -FORMA DE PAGAMENTO
    titulo('FORMA DE PAGAMENTO')
    formaPagamento = int(input('''[1] - A VISTA NO DINHERIO_10% DE DESCONTO
[2] - A VISTA NO CARTÃO_8% DE DESCONTO
[3] - EM 5X VEZES SEM JUROS
[4] - EM 12X VEZES COM 10% DE JUROS
Qual a forma de pagamento? '''))
    while formaPagamento < 0 or formaPagamento > 4:
        formaPagamento = int(input('''[1] - A VISTA NO DINHERIO_10% DE DESCONTO
[2] - A VISTA NO CARTÃO_8% DE DESCONTO
[3] - EM 5X VEZES SEM JUROS
[4] - EM 12X VEZES COM 10% DE JUROS
Qual a forma de pagamento? '''))

    print('\033[34m')
    linha()

    # -APRESENTAÇÃO DSO DADOS
    titulo('NOTA FISCAL_PRODUTOS')
    for i, v in enumerate(total_compras):
        print(f'{i+1:2}:  {v["nome_produto"]:.<26}R${v["preço"]:>9.2f}')
    fpag(preçotot,formaPagamento)

    # -CONTINUAR PROGRAMA
    total_compras.clear()
    preçotot = 0
    continuarPrograma = input('\033[mPróximo cliente >>> [\033[31mS\033[m(sim)/\033[31mN\033[m(não)]: ').strip().upper()[0]
    while continuarPrograma not in 'SN':
        continuarPrograma = input('Próximo cliente >>> [\033[31mS\033[m(sim)/\033[31mN\033[m(não)]: ').strip().upper()[0]
    if continuarPrograma == 'N':
        break
