class Grafite:
    def __init__(self, dureza: float = 0.0, afiadez: str = "", tamanho: int = 0):
        self._dureza = dureza 
        self._afiadez = afiadez 
        self._tamanho = tamanho

    def usoPorPag(self) -> int:
        if self._afiadez == "HB":
            return 1
        if self._afiadez == "2B":
            return 2
        if self._afiadez == "4B":
            return 4
        if self._afiadez == "6B":
            return 6
        return 0

    def getAfiadez(self):
        return self._afiadez
    
    def getDureza(self):
        return self._dureza 
    
    def getTamanho(self):
        return self._tamanho

    def gastarFolha(self):
        return self.usoPorPag()

    def __str__(self):
        return f"{self._dureza}:{self._afiadez}:{self._tamanho}"


class Lapiseira:
    def __init__(self, afiado: float = 0.0):
        self._afiado = afiado       
        self._bico: Grafite | None = None
        self._tambor: list[Grafite] = []

    def __str__(self):
        bico = f"[{self._bico}]" if self._bico else "[]"
        tambor = "<" + "".join(f"[{g}]" for g in self._tambor) + ">" if self._tambor else "<>"
        return f"calibre: {self._afiado}, bico: {bico}, tambor: {tambor}"

    def colocarGraf(self, bico: Grafite) -> bool:
        if bico.getDureza() != self._afiado:
            return False     
        
        self._tambor.append(bico)
        return True
    
    def puxar(self):
        if self._bico != None:
            print("fail: ja existe grafite no bico")
            return
        if not self._tambor:
            print("fail: tambor vazio")
            return
        self._bico = self._tambor.pop(0)

    def remover(self):
        if self._bico is None:
            print("fail: nao existe grafite no bico")
            return
        self._bico = None

    def escrever(self):
        if self._bico is None:
            print("fail: nao existe grafite no bico")
            return
        
        gasto = self._bico.gastarFolha()
        tamanho_atual = self._bico.getTamanho()

        
        if tamanho_atual <= 10:
            print("fail: tamanho insuficiente")
            self._bico = None
            return
        
        novo_tamanho = tamanho_atual - gasto

      
        if novo_tamanho < 10:
            print("fail: folha incompleta")
            self._bico._tamanho = 10
            return

        self._bico._tamanho = novo_tamanho


def main():
    lapiseira = None

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(lapiseira)
        elif args[0] == "init":
            q = float(args[1])
            lapiseira = Lapiseira(q)
        elif args[0] == "insert":
            afiado = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])

            grafite = Grafite(afiado, dureza, tamanho)

            if lapiseira is None:
                print("fail: lapiseira nao iniciada")
            elif not lapiseira.colocarGraf(grafite):
                print("fail: calibre incompatível")
        
        elif args[0] == "pull":
            if lapiseira is None:
                print("fail: lapiseira nao iniciada")
            else:
                lapiseira.puxar()

        elif args[0] == "remove":
            lapiseira.remover()

        elif args[0] == "write":
            lapiseira.escrever()
main()