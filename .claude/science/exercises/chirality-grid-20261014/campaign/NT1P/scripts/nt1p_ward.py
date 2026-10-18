"""NT-1' (b1-W) descriptive breakdown: Ward residual of the NON-canonical ray measure per gauge transformation, both signs s_k
and without the Q correction, transport R(2)..R(16).  usage: python3 nt1p_ward.py"""
import numpy as np
from nt1p_lib import *
from lat2d import Geom, nodes
S = Strip(4, 4); G = Geom(4, 4, False, -1); z = np.load('pool_NT1P_PB_random_Lx4_Lt8_seed2504.npz')
U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]; rng = np.random.default_rng(7); J = []
for (a, b) in [(0, 1), (2, 5), (7, 9)]:
    ph, w = nodes(G, U[a], U[b], 0.6, 3, 'hard'); idx = rng.choice(len(w), 2, replace=False); J.append(S.joined(U[a], U[b], ph[idx]))
J = np.concatenate(J); lower = (S.site_t < 1).astype(float)
Om = {'shift0.3': np.repeat((0.3 * lower)[None], len(J), 0), 'rand0.3': rng.normal(0, 0.3, (len(J), S.ns)), 'rand2.0': rng.normal(0, 2.0, (len(J), S.ns))}
for model, sk, uq in (('11112', -1, True), ('11112', +1, True), ('11112', -1, False), ('L1', -1, True), ('L1', -1, False)):
    M = Measure(S, model, sk=sk, use_Q=uq)
    for nm, om in Om.items():
        line = []
        for Ns in (4, 8, 16, 32):
            W1, _, _ = M.logrho(J, Ns=Ns, canon=False); Wg, _, _ = M.logrho(S.gauge(J, om), Ns=Ns, canon=False)
            d = Wg - W1; line.append(max(np.abs(d.real).max(), np.abs(np.angle(np.exp(1j * d.imag))).max()))
        print(f"{model:5s} s_k={sk:+d} Q={uq!s:5s} {nm:8s}: R(2) R(4) R(8) R(16) = " + " ".join(f"{v:.2e}" for v in line), flush=True)
