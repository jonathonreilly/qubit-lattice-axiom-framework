"""Test C: the same walker and coupling under different permanent-record formation orders (T21 depends on T01)."""
import sys, time
import numpy as np
from numba import njit
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from t21_common import *

L = int(sys.argv[1]); nsamp = int(sys.argv[2]); c = float(sys.argv[3])
N = L ** 3
nb = neighbours(L)
eps = eps_array(L).astype(np.int8)
H0 = walker_H0(L)

@njit(cache=True)
def greedy(order, nb):
    N = order.shape[0]
    occ = np.zeros(N, dtype=np.int8)
    for t in range(N):
        i = order[t]
        ok = True
        for k in range(6):
            if occ[nb[i, k]] == 1:
                ok = False
        if ok:
            occ[i] = 1
    return occ

@njit(cache=True)
def soft_sequential(nb, g, target, seed):
    """visit sites in random order repeatedly; an empty site forms a record with prob g^k (k = occupied neighbours)
    until density target is reached; records permanent."""
    np.random.seed(seed)
    N = nb.shape[0]
    occ = np.zeros(N, dtype=np.int8)
    cnt = 0
    while cnt < target * N:
        i = np.random.randint(0, N)
        if occ[i] == 0:
            k = 0
            for q in range(6):
                k += occ[nb[i, q]]
            if np.random.random() < g ** k:
                occ[i] = 1
                cnt += 1
    return occ

def imbalance(n):
    A = n[eps == 1].sum(); B = n[eps == -1].sum()
    return (A - B) / max(A + B, 1)

def report(name, occs):
    w = []; f = []; im = []; rho = []; fl = []
    for n in occs:
        E = spectrum(H0, n, c)
        a, b, e = gap_metrics(E, c)
        w.append(a); f.append(b); im.append(abs(imbalance(n))); rho.append(n.mean())
    print(f"{name:34s} density={np.mean(rho):.3f} |sublattice imbalance|={np.mean(im):.3f} | "
          f"w_max/c med={np.median(w):.3f} | f_in(0.1c,0.9c) med={np.median(f):.4f} max={np.max(f):.4f}")
    sys.stdout.flush()

rng = np.random.default_rng(3)
# (i) lexicographic order
lex = greedy(np.arange(N), nb)
report("(i) lexicographic greedy", [lex])
E = spectrum(H0, lex, c); print("    lexicographic: w_max/c =", gap_metrics(E, c)[0], " equals even sublattice:",
                                 bool(np.array_equal(lex, (1 + eps) // 2)))
# (ii) random-order sequential adsorption (hard NN exclusion, to jamming)
report("(ii) random-order RSA, hard NN", [greedy(rng.permutation(N).astype(np.int64), nb) for _ in range(nsamp)])
# (iv) soft rule: prob g^k, stopped at density 1/2
for g in (0.25, 0.05):
    report(f"(iv) soft sequential g={g}, stop 1/2", [soft_sequential(nb, g, 0.5, 1000 + s) for s in range(nsamp)])
# reference: Gibbs g=0.25 (ordered) and random half filling
K = np.log(4.0) / 4.0; pbond = 1 - np.exp(-2 * K)
seed_numba(5); sig = np.ones(N, dtype=np.int8); wolff_steps(sig, nb, pbond, 500, 0)
gibbs = []
for _ in range(nsamp):
    wolff_steps(sig, nb, pbond, 40, 0); s = sig.copy()
    if s.sum() < 0: s = -s
    gibbs.append(((1 + eps * s) // 2).astype(np.int8))
report("ref: Gibbs gas g=0.25", gibbs)
report("ref: random half filling (g=1)", [(rng.random(N) < 0.5).astype(np.int8) for _ in range(nsamp)])
