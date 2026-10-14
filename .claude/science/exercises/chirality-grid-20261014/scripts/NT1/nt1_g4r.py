"""NT-1 follow-up F1 (G4 with Richardson): R(N) = (4 W(2N) - W(N))/3 convergence on the gate configurations."""
import numpy as np, sys
from nt1_lib import *
from lat2d import Geom, nodes
fn, T = sys.argv[1], int(sys.argv[2]); G = Geom(2, T, False, -1); LK = Links(G)
z = np.load(fn); U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]
cfg = []
for (a, b) in [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]:
    ph, w = nodes(G, U[a], U[b], 0.6, 16, 'hard'); i = len(w) // 3; cfg.append(LK.joined(U[a], U[b], ph[i:i+1]))
A = np.concatenate(cfg); Wn = {}
for Ns in (8, 16, 32, 64, 128, 256):
    Wn[Ns] = Chiral(LK, '11112', Ns=Ns, sk=-1).logrho(A)[0]
for Ns in (8, 16, 32, 64, 128):
    R = (4 * Wn[2*Ns] - Wn[Ns]) / 3; Wn[('R', Ns)] = R
for Ns in (8, 16, 32, 64):
    print(f"R({Ns},{2*Ns}) -> R({2*Ns},{4*Ns}): max|dW| {np.abs(Wn[('R', 2*Ns)] - Wn[('R', Ns)]).max():.2e}   plain W({2*Ns})->W({4*Ns}) {np.abs(Wn[4*Ns]-Wn[2*Ns]).max():.2e}")
