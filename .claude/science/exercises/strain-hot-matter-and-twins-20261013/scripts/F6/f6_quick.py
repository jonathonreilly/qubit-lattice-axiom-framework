"""quick timing/sanity: gauge loop at t=0 and d on a small grid"""
import numpy as np, time
from f6_lib import *
S = Phot(BS); G = Phot(CPH)
x, w = mkgrid(BS, 6, 0.25, 6)
print('nodes', len(x), 'sum w', w.sum())
t0 = time.time()
print('Sig_g(0) parts', sig_gauge(S, G, x, w, 0.0, parts=True), time.time()-t0)
print('3 G_gam(0) =', 3*sig_gauge(G, G, x, w, 0.0)/3, ' (scalar=photon edge: should equal 3<1/2Om>)')
print('hess', hess_even(lambda t: sig_gauge(S, G, x, w, t), 0.003), time.time()-t0)
