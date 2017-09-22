# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 19:49:51 2017

@author: Kevin
"""

E = 69911 #Modulous find using excel make sure units match xlist

ylist = []
xlist = []
Data_File = open('Data.txt','r') 
#Data.txt is text file with two coloums of numbers stain,stress no lables 
#make sure stress and modulus units match strain is in mm/mm
#also make sure Data.txt is in the same directory as this file
for line in Data_File:
    xlist.append(float(line.split()[0]))
    ylist.append(float(line.split()[1]))
Data_File.close()

for i in range(len(xlist)):
    try:
        x1 = xlist[i]
        x2 = xlist[i+1]
        y1 = ylist[i]
        y2 = ylist[i+1]
    except:
        pass
    if (x2-x1)!= 0:
        m = (y2-y1)/(x2-x1)
    else:
        i+=1
    if m != E:
        y = (E*(m + 500*y1 - 500*m*x1))/(500*(E - m))
        x = (E + 500*y1 - 500*m*x1)/(500*(E - m))
    else:
        i+=1     
    if y>y1 and y<y2 and x>x1 and x<x2:
        print(y)
    else:
        i+=1
 
    
