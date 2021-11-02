from televisores.tv import TV

class Control:
    def __init__(self) :
        pass  
    def enlazar(self,tele):
        self._tv=tele    

    def turnOn(self):
        return TV.turnOn      
    def turnOff(self):
        return TV.turnOff   

    def setCanal(self,canal):
        self._canal=canal

    def canalUp(self):
        return TV.canalUp      
    def canalDown(self):
        return TV.canalDown

    def volumenUp(self):
        return TV.volumenUp      
    def volumenDown(self):
        return TV.volumenDown 

    def getTv(self):
        return self._tv