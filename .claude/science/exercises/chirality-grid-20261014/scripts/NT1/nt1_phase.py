"""NT-1 descriptive P1: how much phase does the chiral weight carry on the witnesses? Spread of Im ln rho over the crossing
nodes of an entry and across entries, for 11112 (anomaly-free) vs L1 (single left-handed charge 1, anomalous) vs one
left-handed charge-2 Weyl ('L2' built ad hoc), with the Theta convention constant removed. Transport R(8).
usage: python3 nt1_phase.py POOL.npz T"""
import numpy as np, sys
import nt1_lib
from nt1_lib import *
from lat2d import Geom, nodes
fn, T = sys.argv[1], int(sys.argv[2]); G = Geom(2, T, False, -1); LK = Links(G)
z = np.load(fn); U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]
nt1_lib.MODELS['L2'] = [(2, 'L', 1)]; nt1_lib.MODELS['R2'] = [(2, 'R', 1)]
def RW(mdl, A):
    a = Chiral(LK, mdl, Ns=8, sk=-1).logrho(A)[0]; b = Chiral(LK, mdl, Ns=16, sk=-1).logrho(A)[0]
    a = a + 2j * np.pi * np.round((b - a).imag / (2 * np.pi)); return (4 * b - a) / 3
ents = [(0, 0), (0, 1), (5, 9), (12, 3), (19, 7)]
for mdl in ('11112', 'L1', 'L2', 'R2'):
    allph = []; within = []
    # Theta constant from entry (0,1) mid node
    ph, w = nodes(G, U[0], U[1], 0.6, 32, 'hard'); i = len(w) // 3
    c = RW(mdl, LK.joined(U[1], U[0], -ph[i:i+1])) - np.conj(RW(mdl, LK.joined(U[0], U[1], ph[i:i+1])))
    cp = -0.5 * np.angle(np.exp(1j * c.imag))[0]
    for (a, b) in ents:
        ph, w = nodes(G, U[a], U[b], 0.6, 32, 'hard'); W = RW(mdl, LK.joined(U[a], U[b], ph)).imag + cp
        W = np.unwrap(W); within.append(W.max() - W.min()); allph.append(np.angle(np.exp(1j * W.mean())))
    allph = np.unwrap(np.array(allph))
    print(f"[{mdl:5s}] spread of Im ln rho over the 32 crossing nodes, per entry: " + " ".join(f"{v:.2e}" for v in within)
          + f" | node-mean phase mod pi across entries: " + " ".join(f"{np.angle(np.exp(2j*v))/2:+.2e}" for v in allph), flush=True)
