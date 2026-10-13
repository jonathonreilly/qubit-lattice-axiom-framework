"""R18-1 s2 (written before running; measurement schedule alternates sweep length by one move, since at bU = 0
every move is accepted and a fixed even number of flips per measurement samples only an index-2 sub-coset). Detailed balance / ergodicity check by exact enumeration at L = 2.
Exact: enumerate the coset 0 + span(moves) (dim 10 at L=2 -> 1024 states), Boltzmann weights exp(-bU sum gamma^2);
compare <sum gamma^2> and the histogram with MC (same move set) at bU = 0, 1, 2."""
import numpy as np, itertools, time
from common import *
from mc import *
L = 2; V = L**3; G = G_matrix(L); P = pattern_vectors(L); B = f2_basis(P); d = B.shape[0]
print("L=2: span dim", d)
states = np.array([(np.array(c) @ B) % 2 for c in itertools.product([0,1], repeat=d)])
gam = (G @ states.T)//2; Es = (gam**2).sum(0)
assert np.all((G @ states.T) % 2 == 0)
S, GE, GN = move_tables(L)
for bU in [0.0, 1.0, 2.0]:
    w = np.exp(-bU*Es); w /= w.sum(); Eex = (w*Es).sum()
    hist_ex = np.bincount(Es, weights=w, minlength=40)
    n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L)
    sweeps(n, g, L, bU, S, GE, GN, 2000, 1)
    hist = np.zeros(40); Es_mc = []
    for it in range(40000):
        sweeps(n, g, L, bU, S, GE, GN, 1, 100 + it, it % 2)
        e = int((g**2).sum()//4); hist[e] += 1; Es_mc.append(e)
    assert np.array_equal(g, charges(n, L))
    hist /= hist.sum(); Es_mc = np.array(Es_mc)
    # blocking error
    blk = Es_mc.reshape(40, -1).mean(1); err = blk.std()/np.sqrt(len(blk))
    print("bU=%.1f: exact <E> = %.4f, MC <E> = %.4f +- %.4f ; max |hist diff| = %.4f ; states visited weight-support %d"
          % (bU, Eex, Es_mc.mean(), err, np.abs(hist - hist_ex[:40]).max(), int((hist_ex > 0).sum())))
