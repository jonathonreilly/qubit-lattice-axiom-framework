import sys, numpy as np
sys.path.insert(0,'.')
from sc import *
box=Box(7)
# heavy limit at fixed mu: K=m/(8 mu)
for mu in [0.5, 2.0]:
    print('mu',mu)
    for m in [3,6,12,25,50,100,200]:
        K=m/(8*mu)
        chi,Nn,Q,P,g0,g=pinned(box,K,m)
        S=solve(box,K,m,alpha=0.3,maxit=5000,init=(chi,Nn)); ch=charges(box,K,S)
        w0p=1/(1+2*Q*g0)
        # predicted T*m from pinned fields
        w=Nn/chi; c=box.center
        nb=[box.idx[(3+d[0],3+d[1],3+d[2])] for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
        t1=sum(0.5*w[c]*w[y]/(chi[c]**2*chi[y]**2*(w[c]+w[y])) for y in nb)
        print(f" m={m} res={S['res']:.0e} Qg0={Q*g0:.4f} P/Q={ch['P']/ch['Q']:.8f} pinned={w0p:.8f} m^2*diff={m*m*(ch['P']/ch['Q']-w0p):.5f} T*m={ch['T']*m:.6f} t1={t1:.6f} T/F={ch['T']/ch['F']:.3e}")
