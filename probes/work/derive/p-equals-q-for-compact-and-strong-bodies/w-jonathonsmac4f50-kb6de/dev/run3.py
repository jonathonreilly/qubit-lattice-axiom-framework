import sys, numpy as np
sys.path.insert(0, '.')
from sc import *
from run2 import pinned_init
n=7; box=Box(n)
for m in [3.0, 1.5, 0.8]:
    print('m=',m)
    chi0,N0,Q0,g0 = pinned_init(0.3*m/3, m)
    init=(chi0,N0)
    for K in np.array([0.3,0.5,0.8,1.2,2,3,5,8,12])*m/3:
        try:
            S = solve(box,K,m,alpha=0.2,maxit=8000,init=init)
        except Exception as ex:
            print(' K',K,'fail',ex); break
        init=(S['chi'],S['N'])
        ch=charges(box,K,S); phi=S['phi']
        print(f" K={K:.3f} it={S['it']} res={S['res']:.0e} phi_c^2={phi[box.center]**2:.4f} w0={S['w'][box.center]:.4f} P/Q={ch['P']/ch['Q']:.4f} T={ch['T']:.3e} F={ch['F']:.3e} T/F={ch['T']/ch['F']:.3f}")
