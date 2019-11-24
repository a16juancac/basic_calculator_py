from tkinter import *



def agregaNum(add):
	global operacion
	global oper

	if add==",":
		add = "."

	if oper== "final":
		num.set(add)
		
		oper=""
	elif oper !="":
		
		num.set(add)
		oper =""
		 
	else:

		num.set(num.get() + add)


def resta(varsum):
	global operacion

	global resultado
	global oper

	if operacion != "resta" and operacion !="":
		
		resultfinal()
		resultado=verificarTipoNum(num.get())

		oper="final"	
	else:


		if resultado !=0:

			if int(float(varsum)) == float(varsum):
				resultado= resultado - int(float(varsum))

			else:
				resultado= resultado - float(varsum)
			
			
		else:
			if int(float(varsum)) == float(varsum):
				resultado= int(float(varsum))

			else:
				resultado= float(varsum)
		
		num.set(resultado)

		
		oper="resta"
	operacion="resta"



def multiplicacion(varsum):
	global operacion
	global resultado
	global oper

	if operacion != "multiplicacion" and operacion !="":
		
		resultfinal()
		if num.get() != "Error":

			resultado=verificarTipoNum(num.get())
		else:

			resultado=0;

		oper="final"
	else:

		if resultado !=0:

			if int(float(varsum)) == float(varsum):
				resultado= resultado * int(float(varsum))

			else:
				resultado= resultado * float(varsum)
			
		
		else:

			if int(float(varsum)) == float(varsum):
				resultado= int(float(varsum))

			else:
				resultado= float(varsum)

		num.set(resultado)

		
		oper="multiplicacion"
	operacion="multiplicacion"


def divison(varsum):
	global operacion
	global resultado
	global oper

	if resultado=='Error':
		resultado = 0

	if operacion != "division" and operacion !="":
		
		resultfinal()
		if num.get() != "Error":

			resultado=verificarTipoNum(num.get())
		else:

			resultado=0;

		oper="final"	
	else:

		if resultado !=0:

			try:

				if int(float(varsum)) == float(varsum):
					resultado= resultado / int(float(varsum))

				else:
					resultado= resultado / float(varsum)

			except ZeroDivisionError:
				
				resultado='Error'

		
		else:

			if int(float(varsum)) == float(varsum):
				resultado= int(float(varsum))

			else:
				resultado= float(varsum)


		num.set(resultado)

		
		oper="division"
	operacion="division"


def suma(varsum):
	global operacion

	global resultado
	global oper

	if operacion != "suma" and operacion !="":
		
		resultfinal()
		if num.get() != "Error":

			resultado=verificarTipoNum(num.get())
		else:

			resultado=0;

		oper="final"
	else:
		if int(float(varsum)) == float(varsum):
			resultado+=int(float(varsum))

		else:
			resultado+=float(varsum)
		num.set(resultado)
		
		oper="suma"
	operacion="suma"

#Verificar si es un numero entero o decimal
def verificarTipoNum(varsum):

	if int(float(varsum)) == float(varsum):

		return int(float(varsum))
	else:
		return float(varsum)

def resetear():
	global operacion

	global resultado
	global oper

	operacion = ""
	resultado=0
	oper=""
	num.set('')

def resultfinal():
	global resultado
	global operacion
	global oper

	if operacion == "suma":

		if int(float(num.get())) == float(num.get()):
			num.set(resultado+int(float(num.get())))

		else:

			num.set(resultado+float((num.get())))

	elif operacion == "multiplicacion":
		if resultado == 0:
			if int(float(num.get())) == float(num.get()):

				num.set(int(float(num.get())))
			else:
				num.set(float(num.get()))
		else:

			if(int(float(num.get()))) == float(num.get()):
				num.set(resultado*int(float(num.get())))
			else:
				num.set(resultado*float(num.get()))

	elif operacion == "resta":

		if resultado == 0:
			if int(float(num.get())) == float(num.get()):

				num.set(int(float(num.get())))
			else:
				num.set(float(num.get()))
		else:
			if(int(float(num.get()))) == float(num.get()):
				num.set(resultado-int(float(num.get())))
			else:
				num.set(resultado-float(num.get()))


	elif operacion == "division":

		if resultado == 0:
			if int(float(num.get())) == float(num.get()):

				num.set(int(float(num.get())))
			else:
				num.set(float(num.get()))
		else:
			if num.get() == '0':
				num.set('Error')
			
			else:
				if(int(float(num.get()))) == float(num.get()):
					num.set(resultado/int(float(num.get())))
				else:
					num.set(resultado/float(num.get()))
					

	resultado=0
	
	oper = "final"

raiz = Tk()

num=StringVar()

raiz.title("Calculadora")

raiz.resizable(0,0)

miframe = Frame(raiz, width="500", height="400", bg ="#cce5ff")

miframe.pack()

operacion=""
resultado=0
oper=""


#PANTALLA
pantalla = Entry(miframe, width=25, bg="black", fg="green", justify="right", textvariable=num).grid(row=1, column=1, padx=10, pady=10, columnspan=4)


#Resetear
btnreset=Button(miframe, text="C", width=3,bg ="#cce5ff", command=lambda:resetear()).grid(row=2, column=4,padx=(0,10))

#FILA 1 

btn7=Button(miframe, text="7", width=3,bg ="#cce5ff", command=lambda:agregaNum("7")).grid(row=3, column=1, padx=(10,0))
btn8=Button(miframe, text="8", width=3,bg ="#cce5ff", command=lambda:agregaNum("8")).grid(row=3, column=2)
btn9=Button(miframe, text="9", width=3,bg ="#cce5ff", command=lambda:agregaNum("9")).grid(row=3, column=3)
btndividir=Button(miframe, text="/", width=3,bg ="#cce5ff", command=lambda:divison(num.get())).grid(row=3, column=4,padx=(0,10))


#FILA 2 

btn4=Button(miframe, text="4", width=3,bg ="#cce5ff", command=lambda:agregaNum("4")).grid(row=4, column=1, padx=(10,0))
btn5=Button(miframe, text="5", width=3,bg ="#cce5ff", command=lambda:agregaNum("5")).grid(row=4, column=2)
btn6=Button(miframe, text="6", width=3,bg ="#cce5ff", command=lambda:agregaNum("6")).grid(row=4, column=3)
btnmulti=Button(miframe, text="x", width=3,bg ="#cce5ff", command=lambda:multiplicacion(num.get())).grid(row=4, column=4,padx=(0,10))

#FILA 3 

btn1=Button(miframe, text="1", width=3,bg ="#cce5ff", command=lambda:agregaNum("1")).grid(row=5, column=1, padx=(10,0))
btn2=Button(miframe, text="2", width=3,bg ="#cce5ff", command=lambda:agregaNum("2")).grid(row=5, column=2)
btn3=Button(miframe, text="3", width=3,bg ="#cce5ff", command=lambda:agregaNum("3")).grid(row=5, column=3)
btnrestar=Button(miframe, text="-", width=3,bg ="#cce5ff", command=lambda:resta(num.get())).grid(row=5, column=4,padx=(0,10))


#FILA 3 

btn0=Button(miframe, text="0", width=3,bg ="#cce5ff", command=lambda:agregaNum("0")).grid(row=6, column=1, padx=(10,0),pady=(0,10))
btncoma=Button(miframe, text=",", width=3,bg ="#cce5ff", command=lambda:agregaNum(",")).grid(row=6, column=2,pady=(0,10))
btnigual=Button(miframe, text="=", width=3,bg ="#cce5ff", command=lambda:resultfinal()).grid(row=6, column=3,pady=(0,10))
btnsuma=Button(miframe, text="+", width=3,bg ="#cce5ff", command=lambda:suma(num.get())).grid(row=6, column=4,padx=(0,10),pady=(0,10))





raiz.mainloop()