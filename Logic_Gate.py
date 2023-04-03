class LogicGate:
    def _init_(self, gate_name):
        self.name = gate_name
        self.output = None

    def getName(self):
        return self.name
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    
class BinaryGate(LogicGate):
    def _init_(self, gate_name):
        super().__init__(gate_name)
        self.pinA = None
        self.pinB = None
    
    def getPinA(self):
        return self.pinA
    
    def getPinB(self):
        return self.pinB
    
    def PutPinA(self):
        return int(input("Digite a entrada do pino A para a porta" + self.getName() + ":"))
    
    def PutPinB(self):
        return int(input("Digite a entrada do pino B para a porta" + self.getName() + ":"))
    
class UnaryGate(LogicGate):
    def _init_(self, gate_name):
        super().__init__(gate_name)
        self.pinA = None

    def getPinA(self):
        if self.PinA == None:
            return self.PutPinA()
        else:
            return self.pinA
    
    def PutPinA(self):
        return int(input("Digite a entrada do pino A para a porta" + self.getName() + ":"))
    
class ANDGate(BinaryGate):
    def _init_(self, gate_name):
        super().__init__(gate_name)

    def performGateLogic(self):
        a = self.PutPinA()
        b = self.PutPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0
         
class ORGate(BinaryGate):
    def _init_(self, gate_name):
        super().__init__(gate_name)

    def performGateLogic(self):
        a = self.PutPinA()
        b = self.PutPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0
        
class NOTGate(UnaryGate):
    def _init_(self, gate_name):
        super().__init__(gate_name)

    def performGateLogic(self):
        a = self.PutPinA()

        if a == 1:
            return 0
        else:
            return 1
        
