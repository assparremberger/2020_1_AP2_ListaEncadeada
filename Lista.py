from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho
    
    def adicionar(self, valor):
        if self.inicio: 
            aux = self.inicio
            while( aux.proximo ):
                aux = aux.proximo
            aux.proximo = No(valor)
        else:
            self.inicio = No(valor)

        self.tamanho = self.tamanho + 1



    def inserir(self, posicao, valor):
        if posicao == 0:
            no = No( valor )
            no.proximo = self.inicio
            self.inicio = no
        else:
            anterior = self.inicio
            for i in range( posicao - 1 ):
                if anterior:
                    anterior = anterior.proximo
            no = No( valor )
            no.proximo = anterior.proximo
            anterior.proximo = no

        self.tamanho = self.tamanho + 1

    def imprimir(self):
        aux = self.inicio
        while( aux ):
            print( aux.dado , "\n")
            aux = aux.proximo
    


