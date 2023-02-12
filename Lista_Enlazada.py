class Nodo:
    def __init__(self,dato:int)->None:
        self.elemento = dato;
        self.siguiente = None

class Lista_enlazada:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.longitud = 0

    def print(self)->None:
        temp = self.inicio
        while(temp is not None):
            print(temp.elemento,end = '')
            if(temp.siguiente is not None):
                print(' -> ',end = '')
            temp = temp.siguiente
        print('\n')

    def append(self,dato:int)->bool:
        nodo = Nodo(dato)
        if(self.longitud == 0):
            self.inicio = nodo
            self.final = nodo
        else:
            self.final.siguiente = nodo
            self.final = nodo
        self.longitud += 1
        return True


    def pop(self)->int:
        if self.longitud == 0:
            return None
        temp = self.inicio
        pre = self.inicio
        while(temp.siguiente is not None):
            pre = temp
            temp = temp.siguiente
        self.final = pre
        self.final.siguiente = None
        self.longitud -= 1
        if(self.longitud == 0):
            self.inicio = None
            self.final = None
        return temp.elemento

    def prepend(self,dato:int)->bool:
        nodo = Nodo(dato)
        if(self.longitud == 0):
            self.inicio = nodo
            self.final = nodo
        else:
            nodo.siguiente = self.inicio
            self.inicio = nodo
        self.longitud+=1
        return True


    def prepop(self)->int:
        if self.longitud == 0:
            return None
        temp = self.inicio
        self.inicio = self.inicio.siguiente
        temp.siguiente = None
        self.longitud-=1
        if(self.longitud == 0):
            self.inicio = None
            self.final = None
        return temp.elemento
    def get(self,indice:int)->Nodo:
        if(indice < 0 or indice > self.longitud):
            return None
        temp = self.inicio
        for i in range(indice):
            temp = temp.siguiente
        return temp
    def insert(self,indice:int,dato:int)->bool:
        if(indice < 0 or indice > self.longitud):
            return False
        if (indice == 0):
            return self.prepend(dato)
        if(indice == self.longitud):
            return self.append(dato)
        nodo = Nodo(dato)
        temp = self.get(indice-2)
        nodo.siguiente = temp.siguiente
        temp.siguiente = nodo
        self.longitud+=1
        return True
    def remove(self,indice:int)->int:
        if indice < 0 or indice > self.longitud:
            return False
        if indice == 0:
            return self.prepop();
        if indice == self.longitud:
            return self.pop()
        pre = self.get(indice-2)
        temp = pre.siguiente
        pre.siguiente = temp.siguiente
        temp.siguiente = None
        self.longitud -= 1
        if(self.longitud == 0):
            self.head = None
            self.fin = None
        return temp.elemento



l = Lista_enlazada()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.remove(3)
l.print()