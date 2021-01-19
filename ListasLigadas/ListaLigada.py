import Nodo

CN = Nodo

class ListaLigada(object):
	#Constructor
	def __init__(self):
		self.inicio = None
		self.ultimo = None
		
	#Retorna si la Lista esta vacia
	def getVacio(self):
		if self.inicio == None:
			return True
		else:
			return False
		
	#Insertar al inicio
	def setElementoInicio(self, elemento):
		nuevo = CN.Nodo(elemento)
		if self.getVacio() == True:
			self.inicio = self.ultimo = nuevo
			return True
		else:
			nuevo.sig = self.inicio
			self.inicio = nuevo
			return True
		return False
			
	#Inserta al final
	def setElementoFinal(self, elemento):
		nuevo = CN.Nodo(elemento)
		if self.getVacio() == True:
			self.inicio = self.ultimo = nuevo
			return True
		else:
			self.ultimo.sig = nuevo
			self.ultimo = nuevo
			return True
		return False
			
	#Eliminar al inicio
	def eliminarInicio(self):
		if self.getVacio() == True:
			print ("Lista vacia");
			return False
		elif self.inicio == self.ultimo:
			self.inicio = None
			self.ultimo = None
		else:
			temp = self.inicio
			self.inicio = self.inicio.sig
			temp = None
			print("Elemento eliminado")
		return True
		
	#Eliniar al final
	def eliminarFinal(self):
		if self.getVacio() == True:
			print ("Lista vacia");
			return False
		elif self.inicio == self.ultimo:
			self.inicio = None
			self.ultimo = None
		else:
			validar = True
			temp = self.inicio
			while(validar):
				if temp.sig == self.ultimo:
					aux = self.ultimo
					self.ultimo = temp
					aux = None
					validar = false
					print("Elemento Eliminado")
				else:
					temp = temp.sig
		return true
		
	#Metodos de apoyo
	def getInicio(self):
		if self.getVacio() == True:
			return ("Lista vacia")
		else:
			return self.inicio
	def getUltimo(self):
		if self.getVacio() == True:
			return ("Lista vacia")
		else:
			return self.ultimo
			
	#Imprimir
	def printLista(self,dato):
		if self.getVacio() == True:
			print ("Lista vacia")
		else:
			f = True
			temp = self.inicio
			while(f):
				print (temp.getElemento())
				if temp == self.ultimo:
					f = False
				else:
					temp = temp.sig
	#Mostrar
	def printLista(self):
		if self.getVacio() == True:
			print ("Lista vacia")
		else:
			temp = self.inicio
			while temp != None :
				print (temp.getElemento())
				temp = temp.sig
	#Inserta Ordenadamente
	def insertaOrden(self, dato):
		nuevo = CN.Nodo(dato)
		
		if self.getVacio() == True:
			self.inicio = self.ultimo = nuevo
			return True
		elif self.inicio.getElemento() > dato:
			nuevo.sig = self.inicio
			self.inicio = nuevo
		else:
			aux = self.inicio
			aux1 = self.inicio.sig
			while aux1 != None and aux1.getElemento() < dato :
				aux = aux1
				aux1 = aux1.sig
			aux.sig = nuevo
			nuevo.sig = aux1
			
	#Eliminar
	def eliminar(self, dato):
		if self.getVacio() == True:
			print ("Lista vacia");
			return False
		elif self.inicio.getElemento() == dato:
			self.inicio = self.inicio.sig
		else:
			aux = self.inicio
			aux1 = self.inicio.sig
			while aux1 != None and aux1.getElemento() != dato :
				aux = aux1;
				aux1 = aux1.sig;
			if aux1 != None:
				aux.sig = aux1.sig
			else:
				return False
		return True
