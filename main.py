import efetua_compra
import tipos_pagamento
import grava_csv

# Lista as compras
print(efetua_compra.compra)

# Valor total da Compra
totalcompra = (efetua_compra.soma)


finalizandopagamento = tipos_pagamento.tipospagamentos(totalcompra)
if finalizandopagamento == "Digite Apenas as Opções acima":
    print(finalizandopagamento)
else:
    print(" O valor total de compras é: ",finalizandopagamento)

import grava_csv
grava_csv.grava(efetua_compra.compra)
