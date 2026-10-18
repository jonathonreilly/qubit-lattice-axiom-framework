"""Item 4: own backgrounds (rot x inv, uniform+staggered, strength 0.3 and 1.0), A2 breaking gap vs eps,
inversion-broken control, and dispersion near k* to distinguish a Dirac mass from a valley energy offset."""
import itertools, time
import numpy as np
from common import *
from item3_isotropy import H0, makeX, blocks, Hk

t0 = time.time()
EVEN = [t for t in TV if sum(t) % 2 == 0]
def symm(Hm, stag=False, a2=False, inv=False):
    Y = sum(((-1.0) ** sum(t) if stag else 1.0) * conj_mat(Hm, TR[t]) for t in TV) / 64
    Y = sum(((-1.0) ** w if a2 else 1.0) * conj_mat(Y, A) for A, w in zip(ROT, W1)) / 24
    if inv: Y = (Y + conj_mat(Y, INV)) / 2
    return Y
def nrm(M): return M / np.abs(M).max()
def lv(ev, tol=1e-8):
    out = []; i = 0
    while i < len(ev):
        j = i
        while j + 1 < len(ev) and ev[j + 1] - ev[i] < tol: j += 1
        out.append((i, j + 1)); i = j + 1
    return out
rng = np.random.default_rng(4242)
def randH():
    A = rng.normal(size=(nV, nV)) + 1j * rng.normal(size=(nV, nV)); return (A + A.conj().T) / 2
B2 = np.hstack([Bloch(kst), Bloch(-kst)])
Hb = H0(-1, 0.2) + 0.05 * makeX(5)
# A2 imaginary staggered on-site term
A = rng.normal(size=(12, 12)); S = np.zeros((nV, nV), complex); S[np.ix_(loc0, loc0)] = 1j * (A - A.T)
Mm = nrm(symm(S, stag=True, a2=True)); Mm = (Mm + Mm.conj().T) / 2
print("A2 term: T-rotations commute:", all(np.allclose(conj_mat(Mm, R_), Mm) for R_, w in zip(ROT, W1) if w == 0),
      "| w1-odd rotations give -M:", all(np.allclose(conj_mat(Mm, R_), -Mm) for R_, w in zip(ROT, W1) if w == 1),
      "| inversion: +M", np.allclose(conj_mat(Mm, INV), Mm), " -M", np.allclose(conj_mat(Mm, INV), -Mm))
for strength in (0.3, 1.0):
    for trial in range(2):
        Bg = Hb + strength * nrm(symm(randH(), inv=True)) + strength * nrm(symm(randH(), stag=True, inv=True))
        ev0 = np.linalg.eigvalsh(B2.conj().T @ Bg @ B2); L0 = lv(ev0)
        ms = [b - a for a, b in L0]
        gaps = []
        for eps in (4e-3, 2e-3, 1e-3, 5e-4, 2.5e-4):
            e = np.linalg.eigvalsh(B2.conj().T @ (Bg + eps * Mm) @ B2)
            gaps.append(np.array([e[a + 2] - e[a + 1] for a, b in L0]) / eps)
        rel = [np.max(np.abs(gaps[i] - gaps[i + 1]) / np.abs(gaps[i + 1])) for i in range(len(gaps) - 1)]
        print(f"bg strength {strength} trial {trial}: folded multiplicities {ms}")
        print("   gap/eps per quartet (eps=2.5e-4):", np.round(gaps[-1], 4))
        print("   max relative change of gap/eps between successive halvings:", ["%.2e" % r for r in rel])
# control: rotations kept, inversion broken (staggered only, and uniform only)
for lab, Hx in (("staggered, no inv", symm(randH(), stag=True)), ("uniform, no inv", symm(randH()))):
    Bo = Hb + 0.3 * nrm(Hx)
    ev = np.linalg.eigvalsh(B2.conj().T @ Bo @ B2)
    print(f"control ({lab}): multiplicities", [b - a for a, b in lv(ev)])
# dispersion near k*: Dirac mass (A2) vs inversion-broken offset, using the folded Bloch Hamiltonian
def folded_k(Hm, q):
    # states at k*+q and -k*+q coupled by staggered parts: use real-space blocks with Q folding
    bl = blocks(Hm); k1 = kst + q; k2 = -kst + q
    # H(k) blocks between momenta k and k' = k+Q: need off-diagonal staggered blocks
    return bl, k1, k2
def lattice_levels_near(Hm, q):
    """exact: Bloch states at k*+q and -k*+q span an invariant space only for q on the grid; use
    the full real-space H with twisted boundary instead -> use blocks of uniform/staggered parts."""
    raise NotImplementedError
print(f"time {time.time()-t0:.1f}s")
