class Nodo:
    def __init__(self):
        self.info = None
        self.sig = None

class Polinomio:
    def __init__(self):
        self.primero = None

class datoPolinomio:
    def __init__(self):
        self.coeficiente = None
        self.exponente = None
    
    def __str__(self):
        return str(self.coeficiente) + "x^" + str(self.exponente)
    
    def __repr__(self):
        return str(self.coeficiente) + "x^" + str(self.exponente)
    
    def __add__(self, otro):
        if self.exponente == otro.exponente:
            return datoPolinomio(self.coeficiente + otro.coeficiente, self.exponente)
        else:
            return None
        
    def __sub__(self, otro):
        if self.exponente == otro.exponente:
            return datoPolinomio(self.coeficiente - otro.coeficiente, self.exponente)
        else:
            return None
        
    def __mul__(self, otro):
        return datoPolinomio(self.coeficiente * otro.coeficiente, self.exponente + otro.exponente)
    


