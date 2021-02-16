print("BEM VINDO AO SUPERMERCADO BEM BOM")

compra = {}
def efetuacompra():
    ## Função que define os produtos e os valores dos mesmos a serem comprados
    fimcompra = 0
    while fimcompra != 'sim':
        compraproduto = input('Digite o nome do produto: ')
        try:
            valorproduto = float(input('Qual o valor do produto: '))
        except:print('Digite somento valor numerico')   
        compra[(valorproduto)] = compraproduto
        fimcompra = input('Terminou as compras ?  Digite sim para finalizar ou não para Continuar ')
        if fimcompra != 'sim' or fimcompra != 'não':
            print('Digite sim ou não nas opções')

efetuacompra()

## Executa a soma dos valores dos produtos a serem comprados
soma = sum(map(lambda compra:float(compra),compra.keys()))
print('O Valor Total da Compra é: {:.2f}'.format(soma))
