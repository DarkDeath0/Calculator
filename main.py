# Call Library

import tkinter
import pygame
from pygame import *
from math import *
import sys

# Build the main window with tkinter and Build an entrance window 

window=tkinter.Tk()
window.title("Calculator")
eqn=[]
b=0
y=tkinter.Entry(window, borderwidth=5)
y.grid(row=4,column=0,columnspan=3, padx=10, pady=10)

# Enter variables into the main window

def Append(s):
	global b
	if s == "x" and b!=1:
		b+=1
	if s == "y" and b!=2:
		b+=2
	eqn.append(s)
	y.insert(tkinter.END,s)

# Evaluate the variables in and enter the answer in the input window

def Eval():
	try:
		global b
		if b == 0:
			x = eval(''.join(eqn))
			Del()
			eqn.append(str(x))
			y.delete(0,tkinter.END)
			y.insert(tkinter.END,str(x))
		else:
			Append("=")
	except:
		Del()
		y.insert(tkinter.END, 'Error')

# Charts 

k=20 # Auxiliary variable
def Graph():
	global b
	pygame.init()
	white = (255,255,255)
	black = (0,0,0)
	graphcolor = (255,0,0)
	gridcolor = (100,250,240) #light blue
	green = (0,200,50)
	blue = (0,50,200)
	width,height = 480, 480
	screen = pygame.display.set_mode((width,height))
	pygame.display.set_caption("Graphic Calculator")

	def GraphEq(eqn,k):
		if b == 1 or b == 5:
			for i in range(width):
				try:
					x = (width/2-i)/float(k)
					y1 = eval(''.join(eqn))
					pos1 = (width/2+x*k, height/2-y1*k)
					nx = x = (width/2-(i+1))/float(k)
					ny = eval(''.join(eqn))
					pos2 = (width/2+nx*k, height/2-ny*k)
					pygame.draw.line(screen, graphcolor, pos1, pos2, 1)
				except:
					pass

		if b == 2 or b == 4:
			for i in range(width):
				try:
					y=(width/2 - i)/float(k)
					x1=eval(''.join(eqn))
					pos1=(width/2+x1*k, height/2-y*k)
					ny=y=(width/2-(i+1))/float(k)
					nx=eval(''.join(eqn))
					pos2=(width/2+nx*k, height/2-ny*k)
					pygame.draw.line(screen, graphcolor, pos1, pos2, 1)
				except:
					pass

	def graphpaper(k):
			screen.set_clip(0, 0, width, height)
			screen.fill(white)
			for i in range(width//k):
				gridx = k*i
				gridy = k*i
				pygame.draw.line(screen, gridcolor, (gridx,0), (gridx,height), 1)
				pygame.draw.line(screen, gridcolor, (0,gridy), (width, gridy), 1)

			pygame.draw.line(screen, gridcolor, (width,0), (width, height), 5)
			midx, midy = width/(2*k), height/(2*k)
			pygame.draw.line(screen, black, (midx*k,0), (midx*k,height), 3)
			pygame.draw.line(screen, black, (0,midy*k), (width,midy*k), 3)
			screen.set_clip(None)
			GraphEq(eqn,k)

	global k	
	c=True	
	while c:	
		if width % k == 0 and k>0:
			graphpaper(k)
			pygame.display.update()

		for event in pygame.event.get():
			if event.type == QUIT:
				c=False
				pygame.quit()
				break

# 

def Backspace():
	s=eqn.pop()
	global b
	if s == "x":
		cout=0
		for i in eqn:
			if i == "x" :
				cout=-1
				break
		if cout!=-1 :
			b-=1
	if s == "y":
		cout=0
		for i in eqn:
			if i == "y" :
				cout=-1
				break
		if cout!=-1 :
			b-=2
	y.delete(0,tkinter.END)
	y.insert(tkinter.END, (''.join(eqn)))

def Del():
	global b
	b=0
	y.delete(0,tkinter.END)
	del eqn[:]

def Break():
	global a
	a=False
	sys.exit()

# Add buttons to the main window

a=True
while(a):
	a=False
	b1=tkinter.Button(window, text="1",height=1,width=5, command=lambda:Append("1"))
	b1.grid(row=0,column=0)
	b2=tkinter.Button(window, text="2",height=1,width=5, command=lambda:Append("2"))
	b2.grid(row=0,column=1)
	b3=tkinter.Button(window, text="3",height=1,width=5, command=lambda:Append("3"))	
	b3.grid(row=0,column=2)
	b4=tkinter.Button(window, text="4",height=1,width=5, command=lambda:Append("4"))
	b4.grid(row=1,column=0)
	b5=tkinter.Button(window, text="5", height=1,width=5,command=lambda:Append("5"))
	b5.grid(row=1,column=1)
	b6=tkinter.Button(window, text="6",height=1,width=5, command=lambda:Append("6"))
	b6.grid(row=1,column=2)
	b7=tkinter.Button(window, text="7", height=1,width=5,command=lambda:Append("7"))
	b7.grid(row=2,column=0)
	b8=tkinter.Button(window, text="8",height=1,width=5, command=lambda:Append("8"))	
	b8.grid(row=2,column=1)
	b9=tkinter.Button(window, text="9",height=1,width=5, command=lambda:Append("9"))
	b9.grid(row=2,column=2)
	b10=tkinter.Button(window, text="0",height=1,width=5, command=lambda:Append("0"))
	b10.grid(row=3,column=1)
	b11=tkinter.Button(window, text="/",height=1,width=5, command=lambda:Append("/"))
	b11.grid(row=0,column=3)
	b12=tkinter.Button(window, text="+",height=1,width=5, command=lambda:Append("+"))
	b12.grid(row=3,column=3)
	b13=tkinter.Button(window, text="-",height=1,width=5, command=lambda:Append("-"))
	b13.grid(row=2,column=3)
	b14=tkinter.Button(window, text="*",height=1,width=5, command=lambda:Append("*"))
	b14.grid(row=1,column=3)
	b15=tkinter.Button(window, text="C",height=1,width=5, command=lambda:Del())
	b15.grid(row=0,column=9)
	b16=tkinter.Button(window, text=".",height=1,width=5, command=lambda:Append("."))
	b16.grid(row=3,column=0)
	b17=tkinter.Button(window, text="=",height=1,width=5, command=lambda:Eval())
	b17.grid(row=3,column=2)
	b18=tkinter.Button(window, text="<-",height=1,width=5, command=lambda:Backspace())
	b18.grid(row=0,column=10)
	b19=tkinter.Button(window, text="(",height=1,width=5, command=lambda:Append("("))
	b19.grid(row=3,column=5)
	b20=tkinter.Button(window, text=")",height=1,width=5, command=lambda:Append(")"))
	b20.grid(row=3,column=6)
	b21=tkinter.Button(window, height=1,width=5, text="x", command=lambda:Append("x"))
	b21.grid(row=0,column=4)
	b22=tkinter.Button(window, height=1,width=5, text="y", command=lambda:Append("y"))
	b22.grid(row=0,column=5)
	b23=tkinter.Button(window, height=1,width=5, text="a^^b", command=lambda:Append("**"))
	b23.grid(row=0,column=6)
	b24=tkinter.Button(window, text="1/x",height=1,width=5,command=lambda:Append("(1/"))
	b24.grid(row=1,column=10)
	b25=tkinter.Button(window, text="|x|",height=1,width=5,command=lambda:Append("abs("))
	b25.grid(row=0,column=7)
	b26=tkinter.Button(window, text="sqrt",height=1,width=5,command=lambda:Append("sqrt("))
	b26.grid(row=0,column=8)
	b27=tkinter.Button(window, text="pi",height=1,width=5,command=lambda:Append("pi"))
	b27.grid(row=3,column=7)
	b28=tkinter.Button(window, text="e",height=1,width=5,command=lambda:Append("e"))
	b28.grid(row=3,column=8)
	b29=tkinter.Button(window, text="sin",height=1,width=5,command=lambda:Append("sin("))
	b29.grid(row=1,column=4)
	b30=tkinter.Button(window, text="cos",height=1,width=5,command=lambda:Append("cos("))
	b30.grid(row=1,column=5)
	b31=tkinter.Button(window, text="tan",height=1,width=5,command=lambda:Append("tan("))
	b31.grid(row=1,column=6)
	b32=tkinter.Button(window, text="sec",height=1,width=5,command=lambda:Append("1/cos("))	
	b32.grid(row=1,column=7)
	b33=tkinter.Button(window, text="cosec",height=1,width=5,command=lambda:Append("1/sin("))
	b33.grid(row=1,column=8)
	b34=tkinter.Button(window, text="cot",height=1,width=5,command=lambda:Append("1/tan("))
	b34.grid(row=1,column=9)
	b35=tkinter.Button(window, text="sinh",height=1,width=5,command=lambda:Append("sinh("))
	b35.grid(row=2,column=4)
	b36=tkinter.Button(window, text="cosh",height=1,width=5,command=lambda:Append("cosh("))
	b36.grid(row=2,column=5)
	b37=tkinter.Button(window, text="tanh",height=1,width=5,command=lambda:Append("tanh("))
	b37.grid(row=2,column=6)
	b38=tkinter.Button(window, text="coth",height=1,width=5,command=lambda:Append("1/tanh("))
	b38.grid(row=2,column=7)
	b39=tkinter.Button(window, text="log",height=1,width=5,command=lambda:Append("log("))
	b39.grid(row=3,column=4)
	b42=tkinter.Button(window, text="sin^(-1)",height=1,width=5,command=lambda:Append("asin("))
	b42.grid(row=2,column=8)
	b43=tkinter.Button(window, text="cos^(-1)",height=1,width=5,command=lambda:Append("acos("))
	b43.grid(row=2,column=9)
	b44=tkinter.Button(window, text="tan^(-1)",height=1,width=5,command=lambda:Append("atan("))
	b44.grid(row=2,column=10)
	b45=tkinter.Button(window, text="Graph",height=1,width=5,command= lambda: Graph(), bd=4)
	b45.grid(row=3,column=9)
	b46=tkinter.Button(window, text="Quit",height=1, width=5, command=lambda:Break(), bd=4)
	b46.grid(row=3,column=10)

window.mainloop()
