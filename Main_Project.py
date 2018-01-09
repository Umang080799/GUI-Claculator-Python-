##Umang Gupta
#GUI Scientific Calculator

import tkinter as tk
import math

window = tk.Tk()
window.geometry("400x400")
window.resizable(0,0)
window.title("Calculator")

entry1=tk.Entry(window,width=60,bd=20,relief="ridge")
entry1.grid(row=0,column=0, columnspan=3)

buttonlist = [ "0","1", "2", "3","4","5","6","7","8","9"]
num_pad=tk.Frame(window)
num_pad.grid(row=1,column=0,sticky="nw")

r=0
c=0
for i in buttonlist: 
 def cmd(x=i):
    click(x)
 tk.Button(num_pad, width=6, text=i, command=cmd).grid(row=r, column=c)

 c += 1
 if c>2:
    r+=1
    c=0

operatorslist=[" pi ", " e "]
operators_pad=tk.Frame(window)
operators_pad.grid(row=5,column=1,sticky="e")

r=0
c=0
for i in operatorslist:
 def cmd(x=i):
    click(x) 
 tk.Button(operators_pad, width=25, text=i, command=cmd).grid(row=r, column=c)

 c += 1
 if c>0:
    r+=1
    c=0

operations2list=[" sqrt ", " x^3" , " x^2 "," x^4 "] 
operations2_pad=tk.Frame(window)
operations2_pad.grid(row=3,column=1,sticky="e")

r=0
c=0
for i in operations2list:
 def cmd(x=i):
    click(x) 
 tk.Button(operations2_pad, width=12, text=i, command=cmd).grid(row=r, column=c)

 c += 1
 if c>1:
    r+=1
    c=0

operationslist=[" AC "," + "," - "," / " ," * "," sin "," cos "," tan "," log " ," Factorial "," ** ","="]
operations_pad=tk.Frame(window)
operations_pad.grid(row=1,column=1,sticky="e")

def squareroot(n):
 n=float(n)
 result=math.sqrt(n)
 return result
    
def cosine(n):
 n=float(n)
 result=math.cos(n)
 return result

def sine(n):
 n=float(n)
 result=math.sin(n)
 return result

def tangent(n):
 n=float(n)
 result=math.tan(n)
 return result

def lograthim(n):
 n=float(n)
 result=math.log(n)
 return result

def factorials(n):
 n=float(n)
 result=math.factorial(n)
 return result

def cube(n):
    n=float(n)
    result=n**3
    return result

def square(n):
    n=float(n)
    result=n**2
    return result

def fourth(n):
    n=float(n)
    result=n**4
    return result
    


def f(x):
    return x**2

def derivative(x):
    h=1./1000.
    rise=float(f(x+h)-f(x))
    run=float(h)
    slope=float(rise/run)
    return slope

r=0
c=0
for i in operationslist:
 def cmd(x=i):
    click(x)
 if i==" ** ":
  tk.Button(operations_pad, width=8, text=" x^y", command=cmd).grid(row=r, column=c)

 else:
    
  tk.Button(operations_pad, width=7, text=i, command=cmd).grid(row=r, column=c)

 c += 1
 if c>2:
    r+=1
    c=0

def click(key):
 if key == "=":
    try:
        temp = str(entry1.get())
        resultchars = temp.split()

        for i in range(0,len(resultchars)):
            if not(resultchars[i]=="AC",resultchars[i]=="+",resultchars[i]=="-",resultchars[i]=="/",resultchars[i]=="*",resultchars[i]=="**"):
                
               resultchars[i]=float(resultchars[i]) 
        temp=""
        for i in range(0,len(resultchars)):
            temp= temp + str(resultchars[i])
        result=str(eval(temp))
        entry1.delete(0,tk.END)
        entry1.insert(tk.END,result)

    except:
        entry1.delete(0, tk.END)
        entry1.insert(tk.END, "Syntax error")
        
 elif key==operationslist[6]:
    n=entry1.get()
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,cosine(n))

 elif key==operationslist[5]:
    n=entry1.get()
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,sine(n))
    
 elif key==operationslist[7]:
    n=entry1.get()
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,tangent(n))

 elif key==operationslist[8]:
    n=entry1.get()
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,lograthim(n))
    
 elif key==operationslist[9]:
    n=entry1.get()
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,factorials(n))
    
                   
 elif key==operations2list[0]:
    n=entry1.get()
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,squareroot(n))

 elif key==operatorslist[0]:
    n=entry1.get()
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,math.pi)

 elif key==operatorslist[1]:
    n=entry1.get()
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,math.e)

 elif key==operations2list[0]:
    n=entry1.get()
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,squareroot(n))

 elif key==operations2list[1]:
    n=entry1.get()
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,cube(n))

 elif key==operations2list[2]:
    n=entry1.get()
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,square(n))

 elif key==operations2list[3]:
    n=entry1.get()
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,fourth(n))    
    
 
 elif key==" AC ":
    entry1.delete(0,tk.END)

 else:
    entry1.insert(tk.END, key)  


window.mainloop() 
