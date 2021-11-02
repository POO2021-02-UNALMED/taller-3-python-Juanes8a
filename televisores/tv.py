class TV:
    numTV=0
    def __init__(self, marca, control): 
       self._marca=marca
       self._canal=1
       self._precio=500
       self._estado=False
       self._volumen=1
       self._control=control

    @classmethod
    def setNumTV(cls,numTV):
        cls._numTV=numTV    
    def getNumTV(self):
        return TV.numTV    

    def setMarca(self,marca):
        self._marca=marca    
    def getMarca(self):
        return self._marca    

    def setControl(self,control):
        self._control=control    
    def getControl(self):
        return self._control

    def setPrecio(self,precio):
        self._precio=precio    
    def getPrecio(self):
        return self._precio    

    def setCanal(self,canal):
        if(self._estado==True and canal>=1 and canal<=120):
            self._canal=canal    
    def getCanal(self):
        return self._canal    

    def setVolumen(self,volumen):
        if(self._estado==True and volumen>=0 and volumen<=7):
            self._volumen=volumen    
    def getVolumen(self):
        return self._volumen

    def getEstado(self):
        return self._estado
    def turnOn(self):
        return self._estado==True
    def turnOff(self):
        return self._estado==False

    def volumenUp(self):
        if(self._estado==True and self._volumen>=0 and self._volumen<7): 
            return TV.setVolumen(TV.getVolumen()+1)
    def volumenDown(self):
        if(self._estado==True and self._volumen>0 and self._volumen<=7): 
            return TV.setVolumen(TV.getVolumen()-1)


    def canalUp(self):
        if(self._estado==True and self._canal>=1 and self._canal<120): 
            return TV.setCanal(TV.getCanal()+1)
    def canalDown(self):
        if(self._estado==True and self._canal>1 and self._canal<=120): 
            return TV.setCanal(TV.getCanal()-1)        