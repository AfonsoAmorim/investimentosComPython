#Analista de Investimentos 
class Analista():
    def __init__(self,nome,registroInvestidor):
        self.nome=nome
        self.registroInvestidor=registroInvestidor
    def infoAnalista(self):
        print("O responsável pela operação é o: " + str(self.nome) + ", seu registro é: " + str(self.registroInvestidor))

 