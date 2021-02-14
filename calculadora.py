from tkinter import *
ventana = Tk()
ventana.title("Calculadora")

#Entrada de texto
e_text=Entry(ventana, font=("calibri 20"))
e_text.grid(row=0,column=0,columnspan =4,padx=5,pady=5)
i = 0
def click_boton(value):
    global i
    e_text.insert(i,value)
    i += 1
    
def erase():
    e_text.delete(0,END)
    i = 0
    
def ops():
    operacion = e_text.get()
    result = eval(operacion)
    e_text.delete(0,END)
    e_text.insert(0,result)
    i = 0

#Botones
boton1 = Button(ventana,text = "1",width = 8, height = 2,command = lambda:click_boton(1))
boton2 = Button(ventana,text = "2",width = 8, height = 2,command = lambda:click_boton(2))
boton3 = Button(ventana,text = "3",width = 8, height = 2,command = lambda:click_boton(3))
boton4 = Button(ventana,text = "4",width = 8, height = 2,command = lambda:click_boton(4))
boton5 = Button(ventana,text = "5",width = 8, height = 2,command = lambda:click_boton(5))
boton6 = Button(ventana,text = "6",width = 8, height = 2,command = lambda:click_boton(6))
boton7 = Button(ventana,text = "7",width = 8, height = 2,command = lambda:click_boton(7))
boton8 = Button(ventana,text = "8",width = 8, height = 2,command = lambda:click_boton(8))
boton9 = Button(ventana,text = "9",width = 8, height = 2,command = lambda:click_boton(9))
boton0 = Button(ventana,text = "0",width = 20, height = 2,command = lambda:click_boton(0))

boton_erase = Button(ventana,text = "AC",width = 8, height = 2,command = lambda:erase())
boton_parentesis1 = Button(ventana,text = "(",width = 8, height = 2,command = lambda:click_boton("("))
boton_parentesis2 = Button(ventana,text = ")",width = 8, height = 2,command = lambda:click_boton(")"))
boton_dot = Button(ventana,text = ".",width = 8, height = 2,command = lambda:click_boton("."))

boton_div = Button(ventana,text = "/",width = 8, height = 2,command = lambda:click_boton("/"))
boton_mult = Button(ventana,text = "x",width = 8, height = 2,command = lambda:click_boton("x"))
boton_sum = Button(ventana,text = "+",width = 8, height = 2,command = lambda:click_boton("+"))
boton_res = Button(ventana,text = "-",width = 8, height = 2,command = lambda:click_boton("-"))
boton_equal = Button(ventana,text = "=",width = 8, height = 2,command = lambda:ops())

#Botones en posicion
boton_erase.grid(row = 1,column = 0,padx = 5,pady = 5)
boton_parentesis1.grid(row = 1,column = 1,padx = 5,pady = 5)
boton_parentesis2.grid(row = 1,column = 2,padx = 5,pady = 5)
boton_div.grid(row = 1,column = 3,padx = 5,pady = 5)
boton7.grid(row = 2,column = 0,padx = 5,pady = 5)
boton8.grid(row = 2,column = 1,padx = 5,pady = 5)
boton9.grid(row = 2,column = 2,padx = 5,pady = 5)
boton_mult.grid(row = 2,column = 3,padx = 5,pady = 5)
boton4.grid(row = 3,column = 0,padx = 5,pady = 5)
boton5.grid(row = 3,column = 1,padx = 5,pady = 5)
boton6.grid(row = 3,column = 2,padx = 5,pady = 5)
boton_sum.grid(row = 3,column = 3,padx = 5,pady = 5)
boton1.grid(row = 4,column = 0,padx = 5,pady = 5)
boton2.grid(row = 4,column = 1,padx = 5,pady = 5)
boton3.grid(row = 4,column = 2,padx = 5,pady = 5)
boton_res.grid(row = 4,column = 3,padx = 5,pady = 5)
boton0.grid(row = 5,column = 0,columnspan = 2,padx = 5,pady = 5)
boton_dot.grid(row = 5,column = 2,padx = 5,pady = 5)
boton_equal.grid(row = 5,column = 3,padx = 5,pady = 5)





ventana.mainloop()
