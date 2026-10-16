# band-touching search: minimize 1-f^2 (=sin^2 omega) with gauge-fixed f = phi(k)^T Q phi(0), for given b
import numpy as np, pickle, sympy as sp, mpmath as mp, sys
from scipy.optimize import minimize
mp.mp.dps=40
B=[sp.Symbol(n,real=True) for n in ('b0','b1','b2')]
Qf=sp.lambdify(B,pickle.load(open('Q.pkl','rb')),'mpmath')
x=min(mp.polyroots([27,-153432,32])); b2=mp.sqrt(x); b0=b2*(1587357*x**2-9020420424*x+472448)/236224
b1=mp.sqrt(mp.sqrt(-(2037123*x**4-11576290482*x**3-561032*x**2)/236224))
u=sp.Symbol('u'); P=sp.Poly(259200000000*u**4 - 453744000000*u**3 + 12644840000*u**2 + 1185396800*u - 39225499,u)
cases={'main(c) b1=+sqrt(u*)':(11/30,float(sp.sqrt(sp.N(sp.real_roots(P)[1],30))),3/20),'h2=0, b1>0':(b0,b1,b2),'h2=0, b1<0':(b0,-b1,b2)}
for name,b in cases.items():
    fco=np.array(mp.matrix(Qf(*b)).tolist(),float)@np.array([1,3,3,1.])
    def F(k):
        c=np.cos(k); return 1-(fco@np.array([1,c.sum(),c[0]*c[1]+c[0]*c[2]+c[1]*c[2],c.prod()]))**2
    L=48; g=np.linspace(-np.pi,np.pi,L,endpoint=False); pts=np.array(np.meshgrid(g,g,g,indexing='ij')).reshape(3,-1).T
    vals=np.array([F(p) for p in pts]); idx=np.argsort(vals)[:300]
    found=[]
    for i in idx:
        r=minimize(F,pts[i],method='Nelder-Mead',options={'xatol':1e-12,'fatol':1e-22,'maxiter':20000})
        kk=np.abs((r.x+np.pi)%(2*np.pi)-np.pi)
        found.append((r.fun,tuple(np.round(np.sort(kk),5))))
    away=[f for f in found if np.linalg.norm(f[1])>1e-3]
    print(name,"| f coeffs",np.round(fco,6),"| min sin^2 away from 0:",min(away)[0] if away else None,"at |k| (sorted, mod sign)",min(away)[1] if away else None)
    # discrete local minima on periodic grid, excluding k=0 cell
    V3=vals.reshape(L,L,L); ismin=np.ones_like(V3,bool)
    for ax in range(3):
        for sh in (1,-1): ismin&=V3<=np.roll(V3,sh,axis=ax)
    loc=[(V3[i,j,l],(g[i],g[j],g[l])) for i,j,l in np.argwhere(ismin) if (i,j,l)!=(L//2,L//2,L//2)]
    ref=[]
    for v,p in loc:
        r=minimize(F,np.array(p),method='Nelder-Mead',options={'xatol':1e-12,'fatol':1e-22,'maxiter':20000})
        ref.append((r.fun,tuple(np.round(np.abs((r.x+np.pi)%(2*np.pi)-np.pi),4))))
    print("   other local minima of sin^2(omega) (refined):",sorted(set((round(a,8),b) for a,b in ref))[:6])
