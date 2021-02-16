escolhapagamento = int(input('''Qual a melhor forma de pagamento?
1 - Para pagamento em dinheiro
2 - Para Pagamento com Cartão de Debito
3 - Para Pagamento com Cartão de credito:  '''))

def tipospagamentos(x):
    if escolhapagamento == 1:
        print('Pagamento com dinheiro desconto de 10%')
        return x - (x * (10 / 100))
    elif escolhapagamento == 2:
        print('Pagamento com cartão debito desconto de 5%')
        return x - (x * (5 / 100))
    elif escolhapagamento == 3:
        print('Pagamento com cartão credito não tem desconto')
        return x
    else:
        print('outras formas de pagamento acréscimo de 10%')
        return x + (x *(10 / 100))
