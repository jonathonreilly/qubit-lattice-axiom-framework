import sys, time; sys.path.insert(0,'.')
from r137_onshell import *
t0=time.time()
print('N/lam/h convergence of on-shell dc_e*U (naive law and S1), m=0.1')
for lab,b1,b2,r,c1,c2 in [('naive',None,None,0.0,None,None),('S1',1.0,2.0,1.0,1.0,2.0)]:
    for N,lam,h in [(64,0.1,0.02),(96,0.1,0.02),(128,0.1,0.02),(96,0.1,0.04),(96,0.05,0.02),(128,0.025,0.02)]:
        law=Law(b1,b2,r,c1,c2,0.1,naive_photon=(lab=='naive'))
        ce,ct,dE0=ce2_minus_1(law,N,lam,h=h)
        print('%-6s N=%3d lam=%.3f h=%.2f  onshell dc_e*U=%+9.4f  dE(0)=%+.5f'%(lab,N,lam,h,ce/2*U,dE0),flush=True)
print('elapsed %.1f'%(time.time()-t0))
