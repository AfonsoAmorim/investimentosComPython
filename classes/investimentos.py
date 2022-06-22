
faixaInicialInvestimento = str(1000)
faixaDeInvestimentoPlus = str(12000)
taxaFaixaInicial = float(0.4)
taxaFaixaPlus = float(0.8)

def inicioInvestimento():
    aporteCliente = input("Digite seu aporte: ")   
    if(str(aporteCliente)<=faixaInicialInvestimento):
        print("O valor de investimento é: " + aporteCliente)
        aporte1 = (int(aporteCliente)*taxaFaixaInicial)+int(aporteCliente)
        print("Valor final para essa faixa de investimento é: " + str(aporte1))
    else:
        aporte1 = (int(aporteCliente)*taxaFaixaPlus)+int(aporteCliente)
        print("O valor final será de: " +  str(aporte1) + " para faixa Plus de investimento")
    return aporteCliente

def investimentoEmUmAno():
    aporteCliente = input("Digite qual prazo de investimento: ")   
    print("O resultado será de " + aporteCliente)
