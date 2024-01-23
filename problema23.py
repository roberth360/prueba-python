class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None

    def insertar_al_principio(self, valor):
        nodo = Node(valor)
        nodo.next = self._head
        self._head = nodo
        if self._tail is None:
            self._tail = nodo

    def insertar_al_final(self, valor):
        nodo = Node(valor)
        if self._tail is None:
            self._head = nodo
            self._tail = nodo
        else:
            self._tail.next = nodo
            self._tail = nodo

    def imprimir(self):
        nodo = self._head
        while nodo is not None:
            print(nodo.valor)
            nodo = nodo.next
            
lista = LinkedList()



lista.imprimir()
