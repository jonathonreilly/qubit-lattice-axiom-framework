"""R18-10 s2: exact checks at L = 2 (coset 0 + span(moves), dim 10 -> 1024 states, as R18-1 s2).
(i) connected components of the D-conserving (dN = 0) filtered move graph vs the partition by N = (N_ab);
(ii) MC (mode 0) vs exact Boltzmann restricted to the start state's component, bU = 0, 1, 2.
Caveat: at L = 2 the mu8 patterns wrap, so dN = 0 is the torus-safe form of dD = 0 (s1 proves equivalence only for
non-wrapping supports)."""
import numpy as np, itertools
from common import *
from mc import move_tables, charges
from mc10 import sweeps_c, counts
L = 2; V = L**3; G = G_matrix(L); P = pattern_vectors(L); B = f2_basis(P); d = B.shape[0]
states = np.array([(np.array(c) @ B) % 2 for c in itertools.product([0, 1], repeat=d)])
idx = {s.tobytes(): i for i, s in enumerate(states.astype(np.int8))}
Ns = np.array([[s[t*V:(t+1)*V].sum() for t in range(6)] for s in states])
gam = (G @ states.T)//2; Es = (gam**2).sum(0)
Pd = np.unique(P % 2, axis=0)
parent = list(range(len(states)))
def find(a):
    while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
    return a
for i, s in enumerate(states):
    for p in Pd:
        t2 = (s + p) % 2
        sgn = (t2.astype(int) - s.astype(int))
        dN = [sgn[t*V:(t+1)*V].sum() for t in range(6)]
        if any(dN): continue
        j = idx[t2.astype(np.int8).tobytes()]
        a, b = find(i), find(j)
        if a != b: parent[a] = b
comp = np.array([find(i) for i in range(len(states))])
ncomp = len(set(comp)); nsec = len(set(map(tuple, Ns)))
# is every N-sector a single component?
split = 0
for Nv in set(map(tuple, Ns)):
    members = np.where((Ns == np.array(Nv)).all(1))[0]
    if len(set(comp[members])) > 1: split += 1
print("L=2: states %d, N-sectors %d, filtered components %d, N-sectors split into >1 component: %d" % (len(states), nsec, ncomp, split))
from collections import Counter
cs = Counter(comp); big = cs.most_common(1)[0][0]
print("component size histogram (size: count):", sorted(Counter(cs.values()).items()))
print("largest component: size %d, N = %s; its N-sector size %d" % (cs[big], Ns[comp == big][0], int((Ns == Ns[comp == big][0]).all(1).sum())))
hs = np.where(comp == big)[0]
S, GE, GN = move_tables(L)
st0 = states[hs[0]]
for bU in [0.0, 1.0, 2.0]:
    memb = np.where(comp == comp[hs[0]])[0]
    w = np.exp(-bU*Es[memb]); w /= w.sum(); Eex = (w*Es[memb]).sum()
    n = np.array(st0).reshape(6, L, L, L).astype(np.int64); g = charges(n, L); Nc = counts(n); fl = np.zeros_like(n)
    sweeps_c(n, g, Nc, L, bU, S, GE, GN, 2000, 1, 0, 0, V//2, fl)
    Es_mc = []; hist = np.zeros(len(states))
    for it in range(40000):
        sweeps_c(n, g, Nc, L, bU, S, GE, GN, 1, 100 + it, it % 2, 0, V//2, fl)
        Es_mc.append(int((g**2).sum()//4)); hist[idx[n.reshape(-1).astype(np.int8).tobytes()]] += 1
    assert np.array_equal(g, charges(n, L)) and np.array_equal(Nc, counts(n))
    hist /= hist.sum(); Es_mc = np.array(Es_mc); blk = Es_mc.reshape(40, -1).mean(1)
    ex = np.zeros(len(states)); ex[memb] = w
    print("bU=%.1f component size %d: exact <sum g^2> = %.4f, MC = %.4f +- %.4f; max |state-prob diff| = %.4f; MC left component: %s"
          % (bU, len(memb), Eex, Es_mc.mean(), blk.std()/np.sqrt(40), np.abs(hist - ex).max(), bool(hist[comp != comp[hs[0]]].sum() > 0)))
