# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Bibliotecas escogidas para el programa
import matplotlib.pyplot as plt#importa libreria matematica y abreviar cdad comando
import numpy as np#import la liberria de numeros de python con un nombre mas corto
import scipy.special as sp# bilbioteca para la creacion de graficos con ayuda de lista
import pylab as pl# importa la libreria de pylab con un nombre mas corto
from math import pi# trae el unmero pi de la libreria de mateaticas
from math import log10#trae comnado de algorimo en base diez de la libreria
plt.close ('all')
# variables ingresadas por el usuarios
# float perimitedecimales 
Vm= float (input("ingrese amplitud modularidad:  "))# pide el valor de la amplitud
Fm= float (input("ingrese frecuencia moduladora:  "))
Vc= float (input ("ingrese amplitud portadora:  "))
Fc= float (input("ingrese    frecuencia portadora: "))
Kf= float (input("ingrese el valor de la sensibilidad de frecuencia: "))
n= float (input("ingrese el numero de periodos: "))
print()
#VARIABLES QUE USAREMOS A LO LARGO DEL PROGRAMA

z=50 #establecemos la impedancia caracteristica portadora
Δf=Kf*Vm #desviacion de frecuencia
β=Δf/Fm #Indice de modulacion

Fs=50000 #Frecuencia de muestreo establecida para el programa
x=0 #se inicializan los variables a trabajr en cero
n0=[] #vector vacio para ingresar los datos resualtantes
bessel=[] #vector vacio para ingresar los datos resultantes
f=np.arange(0,10,1)#vector con el qye empezaremos a trabajar

#ECUACIONES PARA HALLAR BESSEL
for i in range (0, len(f)): #realizar el calculo para cada valor del vector f
    x= round(sp.jv(i,β),2) #funcion bessel incluida en el libreria, redeondear el resultado a
    bessel.append(x)#llenar el vector bessel antes declarado con los resultados de X anterior

n_positivos=bessel[1:11]; #componentes positivos de los componentes bessel
n_negativos=np.flip(n_positivos); #cambiar posiciones dentro del vector, ngativos de bessel
n0.append(bessel[0]); #definir el vector central, es decir posicion cero del vesctor

jn=np.concatenate((n_negativos, n0,n_positivos)) #unir los vectores designados previamente


nB=4 #numero n presentes en besser
BWb=2*Fm*nB #ancho de banda bessel
BWc=2*(f*Vm) #ancho de banda por carson

#VALORES PARA LA FRECUENCIA

f_ns=[] #definicion de vesctores vacios
f_ps=[] #definicion de vectores vacios
F0=[] #definicion de vectores vacios
F0.append(Fc) #fijar en el vector F0 la Fc coni posicion central

for f_inicial in range(0,len(f)): #realizar el caluclo para el cada valor del vesctor f

    if f_inicial==0: 
       f_1=Fc-Fm;
       f_inicial=f_1;
else:
    f_1=f_1+Fm;
    f_inicial= f_1;
    
    f_ns.append(f_inicial); #llenar el vector con los resultados anteriores
    finv_ns=np.flip(f_ns);
    
    
for f_final in range(0,len(f)): #realizar el caluclo para el cada valor del vesctor f

    if f_final==0: # condicional para la frecuencia positivo
       f_1=Fc-Fm;
       f_final=f_1;
else:
    f_1=f_1+Fm;
    f_final= f_1;
    
    f_ps.append(f_final); #llenar el vector con los resultados anteriores
    finv_ps=np.flip(f_ps);
    
Fn= np.concatenate((finv_ns,F0,f_ps))#unir componentes de frecuencias
    
t=np.arange(0, n*1/Fm,1/Fs)
    
    #HALLAR Vc * Jn
f_VcJn=[] #definir un vector inicial vacio
VcJn= np.round(abs((jn*Vc)/(np.sqrt(2))),2) #multiplicar Jn*Vc aplicando valor absoluto
f_VcJn.append(VcJn) #llenar el vector con el calculo anterior
    
    
    #HALLAR VALORES EN D8 DE Jn*Vc
f_VndB=[] #deifinir vector inicial vacio
VndB=0 #inilizacion en cero
Vnb=np.round(abs((20*np.log10(VcJn))),2)
f_VndB.append(VndB)
    
    #HALLAR POTENCIA EN WATTS (W)
f_pnW=[] #definir vector inicial vacio
PnW=0 #inicializcion en cero
PnW=abs(((jn*Vc)**2)/1000) #operamos de acuerdo a la formula
f_pnW.append(PnW) #llenar el vector con el calculo anteirior


#HALLAR POTENCIA EN DBm
f_PndBm=[] #definir vector inicial vacio
PndBm=0 #inicializacion en cero
PndBm=np.round(abs((10*np.log10(PnW*1000))),2) #en esta operacion calculamos la potencia
f_PndBm.append(PndBm) #llenar el vector con el calculo anterior


#CALCULOS DE ECUACIONES PRESENTES EN EL PROGRAMA DE MODULACION 
Vportadora=Vc*np.cos(2*pi*Fc*t); #calculo señal portadora
Vmoduladora=Vm*np.sin(2*pi*Fm*t); #Calculo señal moduladora
Vfm=Vc*np.cos(2*pi*Fc*t+β*np.sin(2*pi*Fm*t)); #Calculo modulacion FM

#FORMULAS RESULTANTES

print("RESULTADOS MODULACION FM")
print()
print("{:^10} {:^10} {:^10} {:^10}".format("Δf","B","Bwb", "Bwc"))
print('{:^10} {:^10} {:^10} {:^10}'.format(Δf,β,BWb,BWc))
print()
print("{:^10} {:^9} {:^9} {:^9} {:^9}".format("Jn","Fn", "Vc*Jn","Vn(dB","Vn(dBm","Vn(dBm)"))

for formatted in map("{:^10} {:^10} {:^9} {:^10} {:^10}".format,jn,Fn, VcJn, VndB, PndBm):
     print(formatted)
         
print()
print("LA ECUACION PORTADORA ES")
print("Vc(t)=",Vc, "cos(2",Fm,"t")
print()
print("LA ECUACION MODULADORA ES")
print("Vm(t)=2",Vm,"sen(2",Fm,"t)")
print()
print("LA ECUACION GENERAL PARA FM ES:")
print ("Vfm(t)=",Vc, "cos[2",Fc,"t +",β,"sen(2",Fm,"t)]")
print()



#GRAFICAS RESULTANTES
fig=plt.figure()
fig,plt.subplot(1,1,1)
plt.plot(t,Vportadora,color="blue", linewidth=0.8)
plt.title("señal portadora");
plt.xlabel("tiempo");
plt.ylabel("amplitud");
plt.grid(True)

fig=plt.figure()
fig,plt.subplot(1,1,1)
plt.plot(t,Vportadora,color="blue", linewidth=0.8)
plt.title("señal moduladora");
plt.xlabel("tiempo");
plt.ylabel("amplitud");
plt.grid(True)


fig=plt.figure()
fig,plt.subplot(1,1,1)
plt.plot(t,Vportadora,color="blue", linewidth=0.8)
plt.title("Modulacion de frecuencia");
plt.xlabel("tiempo");
plt.ylabel("amplitud");
plt.grid(True)

