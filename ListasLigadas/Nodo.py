#Clase Nodo

class Nodo(object):
	#constructor
	def __init__(self, elemento):
		self.elemento = elemento
		#None es Nulo en python
		self.sig = None
		
	#Get dato
	def getElemento(self):
		return self.elemento
