class Grafite:
    def __init__(self, dureza: float = 0.0, afiadez: str = "", tamanho: int = 0):
        self._dureza = dureza
        self._afiadez = afiadez 
        self._tamanho = tamanho

    def usoPorPag(self) -> int:
        if self._dureza == "HB":
            return 1
        if self._dureza == "2B":
            return 2 
        if self._dureza == "4B":
            return 4
        if self._dureza == "6B":
            return 6
        else:
            return 0
        
    def getAfiadez(self):
        return self._afiadez
    
    def getDureza(self):
        return self._dureza
    
    def getTamanho(self):
        return self._tamanho

    def __str__(self):
        return f"{self._afiadez}:{self._dureza}:{self._tamanho}"

class Lapiseira:
    def __init__(self, afiado: float = 0.0):
        self._afiado = afiado
        self._bico: Grafite | None = None
        self._tambor: list[Grafite] = []

    def quantGraf(self):
        if self._bico != None:
            return self._bico 
    
    def colocarGraf(self, bico: Grafite):
        if bico.afiado != self._afiado:
            return False     
        
        self._tambor.append(bico)
        return True
    
    def puxar(self):
        if self.bico != None:
            print("fail: tem grafite no bico")
            return
        if not self.tambor:
            print("fail: tambor vazio")
            return
        self._bico = self.tambor.pop(0)

    def remover(self):
        if self.bico is None:
            print("fail: nao tem grafite no bico")
            return
        
        gasto = self.bico.gastarFolha()

        if self.bico.tamanho <= 10:
            self.bico = None 
            print("fail: tamanho insuficiente")
            return
        
        novo_tamanho = self.bico.tamanho - gasto 

        if novo_tamanho 