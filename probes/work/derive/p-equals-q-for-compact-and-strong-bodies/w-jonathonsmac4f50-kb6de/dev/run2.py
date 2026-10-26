import sys, numpy as np
sys.path.insert(0, '.')
from sc import *
from scipy.optimize import brentq
n = 7
box = Box(n)
def pinned_init(K, m):
    mu = m/(8*K); g0 = box.G(np.eye(box.N)[box.center])[box.center]
    Q = brentq(lambda q: q*(1+q*g0)-mu, 0, mu+1)
    src = np.zeros(box.N); src[box.center] = Q
    chi = 1 + box.G(src)
    # N: (-Delta + Q_x/chi) N = 0 -> N = 1 - P g..., solve P = Q w, w0 = 1/(1+2Qg0)
    P = Q/(1+2*Q*g0)
    src2 = np.zeros(box.N); src2[box.center] = P
    Nn = 1 - box.G(src2)
    return chi, Nn, Q, g0
for m in [3.0, 6.0]:
  for K in [0.3, 0.1, 0.05, 0.03, 0.02]:
    chi0, N0, Q0, g0 = pinned_init(K, m)
    try:
        S = solve(box, K, m, alpha=0.2, maxit=6000, init=(chi0, N0))
    except Exception as ex:
        print(m, K, 'fail', ex); continue
    ch = charges(box, K, S); phi = S['phi']
    print(f"m={m} K={K} Qg0={Q0*g0:.3f} it={S['it']} res={S['res']:.0e} phi_c^2={phi[box.center]**2:.4f} w0={S['w'][box.center]:.4f} P/Q={ch['P']/ch['Q']:.5f} pinned w0={1/(1+2*Q0*g0):.4f} T={ch['T']:.4e} F={ch['F']:.4e} 4K(P-Q)={4*K*(ch['P']-ch['Q']):.4e} T-F={ch['T']-ch['F']:.4e} Q={ch['Q']:.4f}")
