from Lista import Lista

lista = Lista()
print("Tamanho da lista: " + str( lista.tamanho ) )
lista.adicionar(30)
print("Tamanho da lista: " , lista.tamanho  )
lista.adicionar(40)
lista.adicionar(42)

lista.imprimir()

lista.inserir(1, 50 )
print("-----")

lista.imprimir()
