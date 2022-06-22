class Cliente():
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    def informacao(self):
        print("O nome do cliente é: " + str(self.nome))
        print("Sua idade é: " + str(self.idade))

s1=Cliente("André Gomes ", 22)
print(s1.nome)
s1.informacao()
