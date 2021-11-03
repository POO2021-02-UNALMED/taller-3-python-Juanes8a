from televisores.tv import TV

class Control:
    def __init__(self) :
        self._tv=None
    def enlazar(self,tele):
        self._tv=tele    
        tele.setControl(self)
    def turnOn(self):
        return TV.turnOn(self)      
    def turnOff(self):
        return TV.turnOff(self)   

    def setCanal(self,canal):
        self._canal=canal

    def canalUp(self):
        return TV.canalUp(self)     
    def canalDown(self):
        return TV.canalDown(self)

    def volumenUp(self):
        return TV.volumenUp(self)     
    def volumenDown(self):
        return TV.volumenDown(self) 

    def getTv(self):
        return self._tv