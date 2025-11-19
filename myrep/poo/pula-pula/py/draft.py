class Crianca:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = int(idade)
    
    def getNome(self) -> str:
        return self.nome
    
    def getIdade(self) -> int:
        return self.idade
    
    def setNome(self, nome: str) -> str:
        self.nome = nome

    def setIdade(self, idade: int):
        self.idade = int(idade)

    def __str__(self) -> str:
        return f"{self.nome}:{self.idade}"
    
class Trampolim:
    def __init__(self):
        self.brincando: list[Crianca] = []
        self.esperando: list[Crianca] = []

    def removeFromList(self, nome: str, listC: list[Crianca]) -> Crianca | None:
        for i, crianca in enumerate(listC):
            if crianca.getNome() == nome:
                return listC.pop(i)
        return None
    
    def removerCrianca(self, nome: str) -> Crianca | None:
        crianca = self.removeFromList(nome, self.esperando)
        if crianca is not None:
            return crianca
        return self.removeFromList(nome, self.brincando)
    
    def chegar(self, crianca: Crianca):
        self.esperando.insert(0, crianca)

    def entrar(self):
        crianca = self.esperando.pop(-1)
        self.brincando.insert(0, crianca)
    
    def sair(self):
        if len(self.brincando) > 0:
            crianca = self.brincando.pop(-1)
            self.esperando.insert(0, crianca)

    def __str__(self):
        espera = ", ".join(str(x) for x in self.esperando)
        brincando = ", ".join(str(x) for x in self.brincando)
        return f"[{espera}] => [{brincando}]"
    
def main():

    trampolim = Trampolim()
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(trampolim)
        elif args[0] == "arrive":
            nome = args[1]
            idade = int(args[2])
            trampolim.chegar(Crianca(nome, idade))
        elif args[0] == "enter":
            trampolim.entrar()
        elif args[0] == "leave":
            trampolim.sair()
        elif args[0] == "remove":
            nome = args[1]
            crianca = trampolim.removerCrianca(nome)
            if crianca is None:
                print(f"fail: {nome} nao esta no pula-pula")
main()
