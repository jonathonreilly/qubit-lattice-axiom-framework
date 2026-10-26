import sys, numpy as np
sys.path.insert(0, '.')
from sc import *
n = 7
box = Box(n)
m = 3.0
for K in [100.0, 30.0, 10.0, 3.0, 1.0]:
    try:
        S = solve(box, K, m, alpha=0.3, maxit=3000)
    except Exception as ex:
        print(K, 'fail', ex); continue
    ch = charges(box, K, S)
    phi = S['phi']
    print(f"K={K} it={S['it']} res={S['res']:.1e} E={S['E']:.6f} phi_c^2={phi[box.center]**2:.4f} w0={S['w'][box.center]:.4f} chi0={S['chi'][box.center]:.4f}")
    print(f"  Q={ch['Q']:.6f} Qf={ch['Qf']:.6f} P={ch['P']:.6f} Pf={ch['Pf']:.6f} P/Q={ch['P']/ch['Q']:.5f} T={ch['T']:.5e} F={ch['F']:.5e} 4K(P-Q)={4*K*(ch['P']-ch['Q']):.5e} T-F={ch['T']-ch['F']:.5e} E-Hr-T={S['E']-ch['Hrest']-ch['T']:.1e}")
