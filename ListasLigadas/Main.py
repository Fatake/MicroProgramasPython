import ListaLigada
import os

aux = ListaLigada
Lista = aux.ListaLigada()
#
#Funciones
#
def AgregarElemento():
	os.system('clear')
	print ("\t Agregar elemento\n")
	print "Ingrese un elemento \n"
	elemento = input("->")
	Lista.insertaOrden(elemento)
def EliminarElemento():
	os.system('clear')
	print "\t Eliminar elemento\n"
	Lista.printLista()
	print "Ingrese un elemento \n"
	elemento = input("->")
	if Lista.eliminar(elemento):
		print ("Elemento Eliminado")
	else:
		print ("No existe ese elemento")
def MostrarElementos():
	os.system('clear')
	print "\t Mostrar Elemento\n"
	Lista.printLista()
##
##Main
##

while True:
	print "\tPrograma de lista ligadas en Python\n"
	print ("Opciones\n")
	print ("1) Agregar Elemento")
	print ("2) Eliminar elemento")
	print ("3) Mostrar lista")
	print ("<-------------------------->")
	print ("0) Salir")
	print ("Selecione una opcion:")
	opcion = input("->")
	if opcion == 1:
		AgregarElemento()
	elif opcion == 2:
		EliminarElemento()
	elif opcion == 3:
		MostrarElementos()
	elif opcion == 0:
		break
	else:
		os.system('clear')
		print ("No existe esa opcion")


