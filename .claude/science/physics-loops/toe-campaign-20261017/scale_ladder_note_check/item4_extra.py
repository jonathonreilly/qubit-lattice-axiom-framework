"""Item 4 extras: inversion-symmetric A2 term; valley mixing in the inversion-broken control;
item 5 group theory check (independent counting by Reynolds projection on a basis)."""
import itertools
import numpy as np
from common import *
from item3_isotropy import H0, makeX
from item4_gap import symm, nrm, lv, randH, B2, Hb, Mm, rng
Bk, Bm = Bloch(kst), Bloch(-kst)
Mi = (Mm + conj_mat(Mm, INV)) / 2; Mo = (Mm - conj_mat(Mm, INV)) / 2
print("|inv-even part| / |inv-odd part| of A2 term:", np.linalg.norm(Mi) / np.linalg.norm(Mo))
Bg = Hb + 0.3 * nrm(symm(randH(), inv=True)) + 0.3 * nrm(symm(randH(), stag=True, inv=True))
L0 = lv(np.linalg.eigvalsh(B2.conj().T @ Bg @ B2))
for lab, M in (("inversion-even A2", Mi), ("inversion-odd A2", Mo)):
    e = np.linalg.eigvalsh(B2.conj().T @ (Bg + 1e-3 * M / np.abs(M).max()) @ B2)
    print(f"  {lab}: gap/eps per quartet", np.round([(e[a + 2] - e[a + 1]) / 1e-3 for a, b in L0], 4),
          "multiplicities", [b - a for a, b in lv(e)])
# valley weights in inversion-broken staggered control
Bo = Hb + 0.3 * nrm(symm(randH(), stag=True))
ev, W = np.linalg.eigh(B2.conj().T @ Bo @ B2)
print("control (staggered, no inv): levels and k*-weight of each level's eigenvectors")
for a, b in lv(ev):
    wk = np.sum(np.abs(W[:12, a:b]) ** 2) / (b - a)
    print(f"   E={ev[a]:+.4f} mult {b-a} k*-weight {wk:.3f}")
# item 5: invariant symmetric 2-tensors via Reynolds operator on the 10-dim basis
def sp(n, fix_last):
    out = []
    m = n - 1 if fix_last else n
    for p in itertools.permutations(range(m)):
        for s in itertools.product((1, -1), repeat=n):
            M = np.zeros((n, n))
            for i, j in enumerate(p): M[i, j] = s[i]
            if fix_last: M[n - 1, n - 1] = s[n - 1]
            out.append(M)
    return out
for lab, G in (("hyperoctahedral B4", sp(4, False)), ("O_h x time reversal", sp(4, True))):
    basis = []
    for i in range(4):
        for j in range(i, 4):
            E = np.zeros((4, 4)); E[i, j] = E[j, i] = 1; basis.append(sum(g @ E @ g.T for g in G).ravel() / len(G))
    print(f"item 5: {lab} ({len(G)} elements): invariant sym rank-2 dim =", np.linalg.matrix_rank(np.array(basis)))
