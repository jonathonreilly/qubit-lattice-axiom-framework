"""Plug u=p ln n into the exact 1D stationarity residual for f=|d|^q; find root p at large n.
(Checks the formal lemma p = order of vanishing of f; NOT a solution of the boundary-value problem.)"""
import numpy as np
from scipy.optimize import brentq
def R(p,n,f,fp):
    u=lambda m:p*np.log(m)
    tot=0
    for y in (n-1.,n+1.):
        d=u(n)-u(y); tot+=np.exp(-d/2)*(f(d)/2+fp(d))
    return tot
for q in (1.0,1.5,2.0,3.0,4.0,6.0):
    f=lambda d,q=q: np.abs(d)**q
    fp=lambda d,q=q: q*np.abs(d)**(q-1)*np.sign(d)
    roots=[]
    for n in (50.,200.,1000.):
        ps=np.linspace(0.3,9,4000); v=[R(p,n,f,fp)*n**(q) for p in ps]
        r=[brentq(lambda p:R(p,n,f,fp)*n**q,ps[i],ps[i+1]) for i in range(len(ps)-1) if v[i]*v[i+1]<0]
        roots.append(np.round(r,3))
    print("q=",q,"roots p at n=50,200,1000:",roots)
# family f = 2cosh(d/2)-2 (F1) and F2 for control
for name,f,fp in (("F1",lambda d:2*np.cosh(d/2)-2,lambda d:np.sinh(d/2)),("d^2+d^4",lambda d:d**2+d**4,lambda d:2*d+4*d**3)):
    for n in (200.,1000.):
        ps=np.linspace(0.3,9,4000); v=[R(p,n,f,fp)*n**2 for p in ps]
        r=[brentq(lambda p:R(p,n,f,fp)*n**2,ps[i],ps[i+1]) for i in range(len(ps)-1) if v[i]*v[i+1]<0]
        print(name,n,np.round(r,4))
