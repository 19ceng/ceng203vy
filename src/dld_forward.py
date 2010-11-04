class LogicGate:
        def __init__(self,n):
                self.label = n
                self.output = None

        def getLabel(self):
                return self.label

        def getOutput(self):
                self.output = self.performGateLogic()
                return self.output

class BinaryGate(LogicGate):
        def __init__(self,n):
                LogicGate.__init__(self,n)
                self.pinA, self.pinB = None, None

        def setNextPin(self,source):
                if self.pinA == None:
                    self.pinA = source
                elif self.pinB == None:
                    self.pinB = source
                else:
                	print "Cannot Connect: NO EMPTY PINS"

        def getPinA(self):
			pin = self.pinA	
			if pin in (0, 1):
				return pin
			elif isinstance(pin, Connector):
				return pin.getFrom().getOutput()
			elif pin == None:
				raise ValueError, self.label + ":pinA = " + str(pin)

        def getPinB(self):
			pin = self.pinB
			if pin in (0, 1):
				return pin
			elif isinstance(pin, Connector):
				return pin.getFrom().getOutput()
			elif pin == None:
				raise ValueError, self.label + ":pinB = " + str(pin)

        def setPin(self, pinA=None, pinB=None):
			""" TODO
			- pin e eger Connector bagliysa kullaniciyi uyar
   			- yine de Connector u degerle degistirmek isterse, degistir
			"""
			if pinA != None:	self.pinA = pinA
			if pinB != None:	self.pinB = pinB

class AndGate(BinaryGate):
        def __init__(self, n, pinA=None, pinB=None):
                BinaryGate.__init__(self,n)
                self.pinA, self.pinB = pinA, pinB

        def performGateLogic(self):
                if self.getPinA()==1 and self.getPinB()==1:
                        return 1
                else:
                        return 0

class NandGate(BinaryGate):
        def __init__(self, n, pinA=None, pinB=None):
                BinaryGate.__init__(self,n)
                self.pinA, self.pinB = pinA, pinB
        def performGateLogic(self):
                if self.getPinA()==1 and self.getPinB()==1:
                        return 0
                else:
                        return 1

class OrGate(BinaryGate):
        def __init__(self, n, pinA=None, pinB=None):
                BinaryGate.__init__(self,n)
                self.pinA, self.pinB = pinA, pinB
        def performGateLogic(self):
                if self.getPinA()==0 and self.getPinB()==0:
                        return 0
                else:
                        return 1

class XorGate(BinaryGate):
        def __init__(self, n, pinA=None, pinB=None):
                BinaryGate.__init__(self,n)
                self.pinA, self.pinB = pinA, pinB
        def performGateLogic(self):
                if self.getPinA()==self.getPinB():
                        return 0
                else:
                        return 1

class NorGate(BinaryGate):
        def __init__(self, n, pinA=None, pinB=None):
                BinaryGate.__init__(self,n)
                self.pinA, self.pinB = pinA, pinB
        def performGateLogic(self):
                if self.getPinA()==0 and self.getPinB()==0:
                        return 1
                else:
                        return 0

class UnaryGate(LogicGate):
        def __init__(self, n):
                LogicGate.__init__(self,n)
                self.pin = None

        def setNextPin(self,source):
                if self.pin == None:
                        self.pin = source
                else:
                        print "Cannot Connect: NO EMPTY PINS"

        def getPin(self):
			pin = self.pin
			if pin in (0, 1):
				return pin
			elif isinstance(pin, Connector):
				return pin.getFrom().getOutput()
			elif pin == None:
				raise ValueError, self.label + ":pin = " + str(pin)

        def setPin(self, pin=None):
			if pin != None:	self.pin = pin

class NotGate(UnaryGate):
        def __init__(self, n, pin=None):
                UnaryGate.__init__(self,n)
                self.p = pin
        def performGateLogic(self):
                if self.getPin()==1:
                        return 0
                else:
                        return 1

class Connector:
        def __init__(self, fgate, tgate):
                self.fromgate = fgate
                self.togate   = tgate
                tgate.setNextPin(self)

        def getFrom(self):
                return self.fromgate

        def getTo(self):
                return self.togate

# test
g1 = AndGate("g1", 1)
g2 = NotGate("g3")
c1 = Connector(g1, g2)
g1.setPin(None,1)
print g2.getOutput()
