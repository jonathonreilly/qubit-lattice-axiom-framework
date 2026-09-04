"""T22 - CONTINUUM cross-check of the simplicial S_Regge.  For the diagonal metric
g_mumu = 1 + alpha_mu * A sin(k x0) compute int sqrt(g) R exactly to O(A^2) with
sympy and compare against the measured Regge action.  S_Regge must equal
(1/2) int sqrt(g) R."""
import sympy as sp, numpy as np, sys; sys.path.insert(0,".")
x,A,k=sp.symbols('x A k',real=True,positive=True)
al=sp.symbols('a0 a1 a2 a3',real=True)
f=A*sp.sin(k*x)
g=sp.diag(*[1+al[i]*f for i in range(4)])
gi=g.inv()
X=[x,sp.Symbol('y1'),sp.Symbol('y2'),sp.Symbol('y3')]
def d(e,mu): return sp.diff(e,X[mu]) if mu==0 else 0
Gam=[[[sp.simplify(sum(gi[l,s]*(d(g[s,m],n)+d(g[s,n],m)-d(g[m,n],s)) for s in range(4))/2)
       for n in range(4)] for m in range(4)] for l in range(4)]
Ric=[[sp.simplify(sum(d(Gam[l][m][n],l) for l in range(4)) - sum(d(Gam[l][m][l],n) for l in range(4))
      + sum(Gam[l][l][s]*Gam[s][m][n]-Gam[l][n][s]*Gam[s][m][l] for l in range(4) for s in range(4)))
      for n in range(4)] for m in range(4)]
R=sp.simplify(sum(gi[m,n]*Ric[m][n] for m in range(4) for n in range(4)))
dens=sp.sqrt(g.det())*R
ser=sp.simplify(sp.series(dens,A,0,3).removeO())
avg=sp.integrate(ser,(x,0,2*sp.pi/k))*k/(2*sp.pi)      # spatial average of sqrt(g) R
avg=sp.simplify(sp.expand(avg))
print("T22  < sqrt(g) R >  to O(A^2)  =", sp.simplify(avg))
print()
from bridge_fit import *
L=32; AMP=0.06; NKW=1; kv=2*np.pi*NKW/L; Vol=L**4
S0=edge_s(L,0.0,NKW,[0,0,0,0]); g0=geometry(S0,L)
for nm,a in (('conf(1,1,1,1)',[1,1,1,1]),('TT(0,1,-1,0)',[0,1,-1,0]),
             ('V0a(0,1,1,0)',[0,1,1,0]),('V0b(0,1,1,4)',[0,1,1,4]),
             ('V0c(1,1,0,0)',[1,1,0,0]),('gauge(1,0,0,0)',[1,0,0,0]),
             ('tran(0,1,0,0)',[0,1,0,0])):
    S=edge_s(L,AMP,NKW,a); gg=geometry(S,L)
    cont=float(avg.subs({A:AMP,k:kv,al[0]:a[0],al[1]:a[1],al[2]:a[2],al[3]:a[3]}))*Vol
    meas=2.0*(gg['Reg']-g0['Reg'])
    print(f"  {nm:>16}:  continuum int sqrt(g) R = {cont:+13.6f}   "
          f"2*Delta S_Regge = {meas:+13.6f}   ratio {meas/cont if cont!=0 else float('nan'):8.5f}")
