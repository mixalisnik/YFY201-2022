#SU3.py:SU3matrixmanipulations
from numpy import *
from numpy.linalg import *


L1=array([[0,1,0],[1,0,0],[0,0,0]]) #Eight generators
L2=array([[0,-1j,0],[1j,0,0],[0,0,0]])
L3=array([[1,0,0],[0,-1,0],[0,0,0]])
L4=array([[0,0,1],[0,0,0],[1,0,0]])
L5=array([[0,0,-1j],[0,0,0],[1j,0,0]])
L6=array([[0,0,0],[0,0,1],[0,1,0]])
L7=array([[0,0,0],[0,0,-1j],[0,1j,0]])
L8=array([[1,0,0],[0,1,0],[0,0,-2]])*1/sqrt(3)
u=array([1,0,0])#Up quark
d=array([0,1,0])#Down quark
s=array([0,0,1])#Strange quark


Ip=0.5*(L1+1j*L2)#Raising operators
Up=0.5*(L6+1j*L7)
Vp=0.5*(L4+1j*L5)

Im=0.5*(L1-1j*L2)#Lowering operators
Um=0.5*(L6-1j*L7)
Vm=0.5*(L4-1j*L5)


Ipxd=dot(Ip,d)#Raise d to u
print("Raise d to u with I+ raising operator",Ipxd)
Imxu=dot(Im,u)#Lower u to d
print("lower u to d with I- lowering operator",Imxu)

Vpxs=dot(Vp,s)#Raise s to u
print("Raise s to u with V+ raising operator",Vpxs)
Vmxu=dot(Vm,u)#Lower u to s
print("Lower u to s with V- lowering operator",Vmxu)

Upxs=dot(Up,s)#Raise s to d
print("Raise s to d with U+ raising operator",Upxs)
Umxd=dot(Um,d)#Raise d to s
print("Lower d to s with U- lowering operator",Umxd)
