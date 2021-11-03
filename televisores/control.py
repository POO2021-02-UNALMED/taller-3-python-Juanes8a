from televisores.tv import TV

class Control:
    def __init__(self) :
        self._tv=None
    def enlazar(self,tele):
        self._tv=tele    
        tele.setControl(self)
    def turnOn(self):
        return TV.turnOn(self._tv)      
    def turnOff(self):
        return TV.turnOff(self._tv)   

    def setCanal(self,canal):
        self._canal=canal

    def canalUp(self):
        return TV.canalUp(self._tv)     
    def canalDown(self):
        return TV.canalDown(self._tv)

    def volumenUp(self):
        return TV.volumenUp(self._tv)     
    def volumenDown(self):
        return TV.volumenDown(self._tv) 

    def getTv(self):
        return self._tv