import sys, numpy as np, time
sys.path.insert(0, '.')
from sc import *
from run2 import pinned_init
from scipy.optimize import brentq
def branch(box, m, K, init):
    S = solve(box,K,m,alpha=0.2,maxit=8000,init=init); return S
def cross(box, m, Klo, Khi):
    chi0,N0,Q0,g0 = pinned_init(Klo, m)
    S = solve(box,Klo,m,alpha=0.2,maxit=8000,init=(chi0,N0))
    init=[(S['chi'],S['N'])]
    def f(K):
        S = solve(box,K,m,alpha=0.2,maxit=8000,init=init[0]); init[0]=(S['chi'],S['N'])
        ch=charges(box,K,S); return ch['P']/ch['Q']-1
    # march K upward to bracket
    Ks=np.geomspace(Klo,Khi,12); prev=(Ks[0],f(Ks[0]))
    for K in Ks[1:]:
        v=f(K)
        if prev[1]<0<=v:
            # reset init to branch at prev K for stability
            Kb=brentq(f,prev[0],K,xtol=1e-12)
            return Kb
        prev=(K,v)
    return None
for n in [7,9]:
    box=Box(n)
    for m in [1.5,3.0,6.0]:
        t=time.time()
        Kb=cross(box,m,0.02*m/3,3.0*m/3*2)
        if Kb is None: print(n,m,'no crossing'); continue
        chi0,N0,Q0,g0 = pinned_init(Kb,m)
        S=solve(box,Kb,m,alpha=0.2,maxit=8000,init=(chi0,N0)); ch=charges(box,Kb,S); phi=S['phi']
        # second identity
        sec = 4*Kb*(ch['P']+ch['Q']) - (ch['Hrest']+2*ch['T'])
        print(f"n={n} m={m} K*={Kb:.6f} mu={m/(8*Kb):.4f} Qg0={ch['Q']*g0:.4f} phi_c^2={phi[box.center]**2:.4f} w0={S['w'][box.center]:.4f} T/F={ch['T']/ch['F']:.5f} P/Q={ch['P']/ch['Q']:.6f} sec.id={sec:.1e} t={time.time()-t:.0f}s")
