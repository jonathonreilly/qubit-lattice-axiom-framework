# GUIDE only: 2D Ising on periodic strips. Checks Lemma CS (e(x)/x non-increasing, Cas >= 0)
# and the crossing identity g(a;b) - g(b;a) = b e(a) - a e(b). A run can refute, never prove.
import numpy as np, itertools
def tm(x, J):
    confs = np.array(list(itertools.product([-1,1], repeat=x)))
    D = np.array([sum(c[i]*c[(i+1)%x] for i in range(x)) for c in confs], dtype=float)
    inter = confs @ confs.T
    T = np.exp(J*D/2)[:,None] * np.exp(J*inter) * np.exp(J*D/2)[None,:]
    return T
for J in (0.2, 0.44, 0.7):
    ev = {}
    for x in range(3, 11):
        w = np.linalg.eigvalsh(tm(x, J))
        ev[x] = np.sort(w)[::-1]
    e = {x: np.log(ev[x][0]) for x in ev}
    ratios = [e[x]/x for x in sorted(e)]
    mono = all(ratios[i] >= ratios[i+1]-1e-12 for i in range(len(ratios)-1))
    def g(t, x):  # log(1+S(t; strip x))
        return np.log(np.sum((ev[x]/ev[x][0])**t))
    worst = 0.0
    for a in range(3, 10):
        for b in range(a+1, 11):
            cas = b*e[a] - a*e[b]
            ident = g(a, b) - g(b, a)
            worst = max(worst, abs(cas-ident))
            assert cas >= -1e-10, (J, a, b, cas)
    print("J", J, "e(x)/x non-increasing:", mono, " min Cas>=0 ok; max |Cas - (g(a;b)-g(b;a))| =", f"{worst:.2e}")
    print("   e(x)/x:", " ".join(f"{r:.6f}" for r in ratios))
