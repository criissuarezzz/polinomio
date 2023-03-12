class Nodo(object):
    """Clase nodo simmplemente enlazado"""

    info, sig = None, None


class datoPolinomio(object):
    """Clase dato polinomio"""

    def __init__(self, valor, termino):
        """Crea un dato polinomio con valor y término"""
        self.valor = valor # valor equivale al coeficiente
        self.termino = termino # termino equivale al exponente


class Polinomio(object):
    """Clase polinomio"""

    def __init__(self):
        """Crea un polinomio del grado cero"""
        self.termino_mayor = None   # Nodo con el término de mayor grado, y None para polinomio de grado cero para empezar
        self.grado = -1         # Grado del polinomio, -1 para polinomio de grado cero para empezar

    def agregar_termino(polinomio, termino, valor):
        """Agrega un termino y su valor al polinomio"""
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if (termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while (actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    def modificar_termino(pol, termino, valor):
        """Modifica el valor de un termino del polinomio"""
        actual = pol.termino_mayor
        while (actual is not None and actual.info.termino != termino):
            actual = actual.sig
        if (actual is not None):
            actual.info.valor = valor
    
    def eliminar_termino(pol, termino):
        """Elimina un termino del polinomio"""
        if (pol.termino_mayor is not None):
            if (pol.termino_mayor.info.termino == termino):
                pol.termino_mayor = pol.termino_mayor.sig
            else:
                actual = pol.termino_mayor
                while (actual.sig is not None and actual.sig.info.termino != termino):
                    actual = actual.sig
                if (actual.sig is not None):
                    actual.sig = actual.sig.sig
    
    def mostrar_polinomio(polinomio):
        """Muestra el polinomio"""
        aux = polinomio.termino_mayor
        pol = ""
        if (aux is not None):
            while (aux is not None):
                signo = ""
                if aux.info.valor >= 0:
                    signo += "+"
                pol += signo + str(aux.info.valor) + "x^" + str(aux.info.termino)
                aux = aux.sig
        return pol

    def evaluar_polinomio(pol, x):
        """Evalua el polinomio en x"""
        actual = pol.termino_mayor
        resultado = 0
        while (actual is not None):
            resultado += actual.info.valor * (x ** actual.info.termino)
            actual = actual.sig
        return resultado
    
    def sumar_polinomios(pol1, pol2):
        """Suma dos polinomios"""
        pol3 = Polinomio()
        actual = pol1.termino_mayor
        while (actual is not None):
            Polinomio.agregar_termino(pol3, actual.info.termino, actual.info.valor)
            actual = actual.sig
        actual = pol2.termino_mayor
        while (actual is not None):
            Polinomio.modificar_termino(pol3, actual.info.termino, actual.info.valor + Polinomio.evaluar_polinomio(pol3, actual.info.termino))
            actual = actual.sig
        return pol3
    
    def restar_polinomios(pol1, pol2):
        """Resta dos polinomios"""
        pol3 = Polinomio()
        actual = pol1.termino_mayor
        while (actual is not None):
            Polinomio.agregar_termino(pol3, actual.info.termino, actual.info.valor)
            actual = actual.sig
        actual = pol2.termino_mayor
        while (actual is not None):
            Polinomio.modificar_termino(pol3, actual.info.termino, actual.info.valor - Polinomio.evaluar_polinomio(pol3, actual.info.termino))
            actual = actual.sig
        return pol3
    
    def multiplicar_polinomios(pol1, pol2):
        """Multiplica dos polinomios"""
        pol3 = Polinomio()
        actual = pol1.termino_mayor
        while (actual is not None):
            actual2 = pol2.termino_mayor
            while (actual2 is not None):
                Polinomio.modificar_termino(pol3, actual.info.termino + actual2.info.termino, actual.info.valor * actual2.info.valor + Polinomio.evaluar_polinomio(pol3, actual.info.termino + actual2.info.termino))
                actual2 = actual2.sig
            actual = actual.sig
        return pol3
    
    def dividir_polinomios(pol1, pol2):
        """Divide dos polinomios"""
        pol3 = Polinomio()
        pol4 = Polinomio()
        actual = pol1.termino_mayor
        while (actual is not None):
            Polinomio.agregar_termino(pol4, actual.info.termino, actual.info.valor)
            actual = actual.sig
        while (pol4.grado >= pol2.grado):
            termino = pol4.grado - pol2.grado
            valor = pol4.termino_mayor.info.valor / pol2.termino_mayor.info.valor
            Polinomio.agregar_termino(pol3, termino, valor)
            actual = pol2.termino_mayor
            while (actual is not None):
                Polinomio.modificar_termino(pol4, actual.info.termino + termino, actual.info.valor * valor - Polinomio.evaluar_polinomio(pol4, actual.info.termino + termino))
                actual = actual.sig
        return pol3, pol4
    
#ejemplos
p1=Polinomio()
p1.agregar_termino(2,-4)  #-4x^2
p1.agregar_termino(3,2)   #2x^3


p2=Polinomio()
p2.agregar_termino(3,4)   #4x^3
p2.agregar_termino(6,1)   #x^6

print(p1.mostrar_polinomio()) # Muestra el polinomio p1
print(p2.mostrar_polinomio()) # Muestra el polinomio p2
print(p1.evaluar_polinomio(4)) # Evalua el polinomio en x=4
print(p2.evaluar_polinomio(4))  # Evalua el polinomio en x=4

p3=p1.sumar_polinomios(p2) # Suma los polinomios p1 y p2
p3.mostrar_polinomio() # Muestra el polinomio p3

p4=p1.restar_polinomios(p2) # Resta los polinomios p1 y p2
p4.mostrar_polinomio() # Muestra el polinomio p4

p5=p1.multiplicar_polinomios(p2) # Multiplica los polinomios p1 y p2
p5.mostrar_polinomio() # Muestra el polinomio p5

p6,p7=p1.dividir_polinomios(p2) # Divide los polinomios p1 y p2
p6.mostrar_polinomio() # Muestra el polinomio p6    
p7.mostrar_polinomio() # Muestra el polinomio p7

