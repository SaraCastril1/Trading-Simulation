class B_tree:
    
    def _init_(self, grade):
        #número máximo de claves por nodo
        self.grade = grade
        self.raiz = None


    def insertar(self, clave, dato):
        # Si el árbol está vacío, creamos un nodo hoja con la clave y el dato
        if self.raiz is None:
            self.raiz = new NodoHoja(self.grade, clave, dato)
        else:
            # Si el árbol no está vacío, buscamos el nodo hoja donde insertar la clave y el dato
            nodo = self.buscar_nodo_hoja(self.raiz, clave)
            # Insertamos la clave y el dato en el nodo hoja
            nodo.insertar(clave, dato)
            # Si el nodo hoja se ha desbordado, lo dividimos y propagamos la división hacia arriba
            if nodo.desbordado():
                self.dividir(nodo)

    # Método para buscar un dato en el árbol
    def buscar(self, clave):
        # Si el árbol está vacío, no hay nada que buscar
        if self.raiz is None:
            return None
        else:
            # Si el árbol no está vacío, buscamos el nodo hoja donde puede estar la clave
            nodo = self.buscar_nodo_hoja(self.raiz, clave)
            # Buscamos el dato asociado a la clave en el nodo hoja
            return nodo.buscar(clave)

    # Método para eliminar un dato del árbol
    def eliminar(self, clave):
        # Si el árbol está vacío, no hay nada que eliminar
        if self.raiz is None:
            return None
        else:
            # Si el árbol no está vacío, buscamos el nodo hoja donde está la clave
            nodo = self.buscar_nodo_hoja(self.raiz, clave)
            # Eliminamos la clave y el dato del nodo hoja
            dato = nodo.eliminar(clave)
            # Si el nodo hoja se ha quedado vacío, lo eliminamos del árbol
            if nodo.vacio():
                self.eliminar_nodo(nodo)
            # Si el nodo hoja se ha quedado con menos claves de las mínimas, lo fusionamos o redistribuimos con sus hermanos
            elif nodo.subutilizado():
                self.fusionar_o_redistribuir(nodo)
            # Devolvemos el dato eliminado
            return dato

    # Método auxiliar para buscar el nodo hoja donde insertar o buscar una clave
    def buscar_nodo_hoja(self, nodo, clave):
        # Si el nodo es interno, buscamos el puntero adecuado según la clave y seguimos bajando por el árbol
        if isinstance(nodo, NodoInterno):
            i = 0
            while i < len(nodo.claves) and clave > nodo.claves[i]:
                i += 1
            return self.buscar_nodo_hoja(nodo.punteros[i], clave)
        # Si el nodo es hoja, lo devolvemos
        else:
            return nodo

    # Método auxiliar para dividir un nodo desbordado y propagar la división hacia arriba
    def dividir(self, nodo):
        # Obtenemos la clave y el nodo resultantes de la división
        clave, nuevo_nodo = nodo.dividir()
        # Si el nodo es la raíz, creamos una nueva raíz con la clave y los dos nodos
        if nodo is self.raiz:
            self.raiz = NodoInterno(self.grade, clave, nodo, nuevo_nodo)
        else:
            # Si el nodo no es la raíz, obtenemos el padre del nodo
            padre = nodo.padre
            # Insertamos la clave y el nuevo nodo en el padre
            padre.insertar(clave, nuevo_nodo)
            # Si el padre se ha desbordado, lo dividimos y propagamos la división hacia arriba
            if padre.desbordado():
                self.dividir(padre)

    # Método auxiliar para eliminar un nodo vacío del árbol
    def eliminar_nodo(self, nodo):
        # Si el nodo es la raíz, el árbol queda vacío
        if nodo is self.raiz:
            self.raiz = None
        else:
            # Si el nodo no es la raíz, obtenemos el padre del nodo
            padre = nodo.padre
            # Eliminamos el puntero al nodo del padre
            padre.eliminar_puntero(nodo)
            # Si el padre se ha quedado vacío, lo eliminamos del árbol
            if padre.vacio():
                self.eliminar_nodo(padre)
            # Si el padre se ha quedado con menos claves de las mínimas, lo fusionamos o redistribuimos con sus hermanos
            elif padre.subutilizado():
                self.fusionar_o_redistribuir(padre)

    # Método auxiliar para fusionar o redistribuir un nodo subutilizado con sus hermanos
    def fusionar_o_redistribuir(self, nodo):
        # Obtenemos el padre y los hermanos del nodo
        padre = nodo.padre
        izquierdo = nodo.izquierdo()
        derecho = nodo.derecho()
        # Si el hermano izquierdo existe y tiene más claves de las mínimas, redistribuimos una clave y un puntero desde él
        if izquierdo is not None and not izquierdo.subutilizado():
            self.redistribuir(izquierdo, nodo)
        # Si el hermano derecho existe y tiene más claves de las mínimas, redistribuimos una clave y un puntero desde él
        elif derecho is not None and not derecho.subutilizado():
            self.redistribuir(derecho, nodo)
        # Si ambos hermanos están subutilizados o no existen, fusionamos el nodo con uno de ellos y eliminamos la clave del padre que los separa
        else:
            # Si existe el hermano izquierdo, lo fusionamos con el nodo y eliminamos la clave izquierda del padre
            if izquierdo is not None:
                clave = padre.claves[padre.punteros.index(nodo) - 1]
                self.fusionar(izquierdo, clave, nodo)
                padre.eliminar(clave)
            # Si existe el hermano derecho, fusionamos el nodo con él y eliminamos la clave derecha del padre
            elif derecho is not None:
                clave = padre.claves[padre.punteros.index(nodo)]
                self.fusionar(nodo, clave, derecho)
                padre.eliminar(clave)

    # Método auxiliar para redistribuir una clave y un puntero desde un nodo a otro
    def redistribuir(self, origen, destino):
        # Obtenemos el padre de los nodos
        padre = origen.padre
        # Obtenemos el índice de la clave del padre que está entre los nodos
        i = min(padre.punteros.index(origen), padre.punteros.index(destino))
        # Si el origen es el izquierdo, movemos la clave derecha del origen al padre y la clave del padre al destino
        if origen is destino.izquierdo():
            clave_origen = origen.claves.pop()
            puntero_origen = origen.punteros.pop()
            clave_padre = padre.claves[i]
            padre.claves[i] = clave_origen
            destino.insertar(clave_padre, puntero_origen)
        # Si el origen es el derecho, movemos la clave izquierda del origen al padre y la clave del padre al destino
