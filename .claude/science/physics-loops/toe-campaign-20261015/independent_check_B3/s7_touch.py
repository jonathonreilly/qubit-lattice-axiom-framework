# global check: min of sin(omega)^2 = |h|^2+|g|^2 away from k=0; and f gauge-invariance f = phi^T Q phi(0)
import numpy as np, pickle, sympy as sp
B0,B1,B2,u=sp.symbols('b0 b1 b2 u',real=True)
P=sp.Poly(259200000000*u**4 - 453744000000*u**3 + 12644840000*u**2 + 1185396800*u - 39225499,u)
b=(sp.Rational(11,30),sp.sqrt(sp.real_roots(P)[1]),sp.Rational(3,20))
Q=np.array(pickle.load(open('Q.pkl','rb')).subs({B0:b[0],B1:b[1],B2:b[2]}).evalf(30),float)
fco=Q@np.array([1,3,3,1.]); print("gauge-fixed f coefficients (1,e1,e2,e3):",fco)
L=96; x=np.linspace(-np.pi,np.pi,L,endpoint=False); X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
C=[np.cos(X),np.cos(Y),np.cos(Z)]; phi=[np.ones_like(X),C[0]+C[1]+C[2],C[0]*C[1]+C[0]*C[2]+C[1]*C[2],C[0]*C[1]*C[2]]
f=sum(fco[i]*phi[i] for i in range(4)); s2=1-f**2  # = |h|^2+|g|^2 by unitarity
r=np.sqrt(X**2+Y**2+Z**2)
print("min sin^2(omega) over grid with |k|>0.3:",s2[r>0.3].min(),"  max f:",f[r>0.3].max()," min f:",f.min())
