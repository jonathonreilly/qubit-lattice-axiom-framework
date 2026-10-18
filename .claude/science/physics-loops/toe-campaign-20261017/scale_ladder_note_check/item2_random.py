"""Item 2/4: own random symmetric Hamiltonians (new seeds, strengths, ranges) and break attempts."""
import itertools, time
import numpy as np
from common import *

t0 = time.time()
Bk, Bm = Bloch(kst), Bloch(-kst); B2 = np.hstack([Bk, Bm]); BG = Bloch(np.zeros(3))
def lv(ev, tol=1e-8):
    out = []; i = 0
    while i < len(ev):
        j = i
        while j + 1 < len(ev) and ev[j + 1] - ev[i] < tol * max(1, abs(ev[i])): j += 1
        out.append(j + 1 - i); i = j + 1
    return out
EVEN = [t for t in TV if sum(t) % 2 == 0]
def avg(Hm, ops):
    return sum(conj_mat(Hm, A) for A in ops) / len(ops)
def symm(Hm, trans=TV, rot=True, inv=False):
    Y = avg(Hm, [TR[t] for t in trans])
    if rot: Y = avg(Y, ROT)
    if inv: Y = (Y + conj_mat(Y, INV)) / 2
    return Y
def randH(rng, cplx=True):
    A = rng.normal(size=(nV, nV)) + (1j * rng.normal(size=(nV, nV)) if cplx else 0)
    return (A + A.conj().T) / 2

res = {}
# (a) item 2: rotations + all translations, dense random (every range), strengths 1e-2..1e2, no H0
rng = np.random.default_rng(777)
mk, mg, okk = [], [], True
for trial in range(6):
    Hs = symm(randH(rng, cplx=trial % 3 != 0)); Hs *= 10.0 ** (trial - 2) / np.abs(Hs).max()
    assert all(np.allclose(conj_mat(Hs, A), Hs) for A in ROT[:6] + [TR[(1,0,0)]])
    m1 = lv(np.linalg.eigvalsh(Bk.conj().T @ Hs @ Bk)); m2 = lv(np.linalg.eigvalsh(Bm.conj().T @ Hs @ Bm))
    okk &= all(m % 2 == 0 for m in m1 + m2); mk.append(m1); mg.append(lv(np.linalg.eigvalsh(BG.conj().T @ Hs @ BG)))
print("(a) rot+trans symmetric, strengths 1e-2..1e3: all levels at +-k* even:", okk)
print("    k* multiplicities:", mk); print("    Gamma multiplicities:", mg)

# (b) break attempt: rotations + only even translations (staggered allowed). k* mixes with -k*
ok_b = True; mb = []
for trial in range(3):
    Hs = symm(randH(rng), trans=EVEN); Hs /= np.abs(Hs).max()
    m = lv(np.linalg.eigvalsh(B2.conj().T @ Hs @ B2)); mb.append(m); ok_b &= all(x % 2 == 0 for x in m)
    leak = np.linalg.norm(Hs @ B2 - B2 @ (B2.conj().T @ Hs @ B2))
    assert leak < 1e-8
print("(b) rot + even translations only: folded {k*,-k*} levels all even:", ok_b, mb)

# (c) break attempt: bare (ungauged) rotation permutations instead of PSG ops
BARE = [(P, np.zeros_like(s)) for P, s in ROT]
Hs = symm(randH(rng)); Hb = avg(avg(randH(rng), [TR[t] for t in TV]), BARE)
print("(c) H0-like PSG-symmetric hopping commutes with bare permutations?",
      all(np.allclose(conj_mat(Hs, A), Hs) for A in BARE))
mc = lv(np.linalg.eigvalsh(Bk.conj().T @ Hb @ Bk))
print("    bare-permutation-symmetric H: k* block invariant?", np.linalg.norm(Hb @ Bk - Bk @ (Bk.conj().T @ Hb @ Bk)) < 1e-8,
      "k* multiplicities", mc, "Gamma", lv(np.linalg.eigvalsh(BG.conj().T @ Hb @ BG)))

# (d) only the C3 subgroup about [111] (order-3 lift exists) -> odd levels possible at k*?
c3 = [r for r, R in enumerate(ROTS) if int(np.trace(R)) == 0 and (R @ np.array([1,1,1]) == np.array([1,1,1])).all()]
H3 = avg(avg(randH(rng), [TR[t] for t in TV]), [ROT[0]] + [ROT[r] for r in c3])
print("(d) C3[111] + translations only: k* fixed by C3[111]?",
      np.linalg.norm(H3 @ Bk - Bk @ (Bk.conj().T @ H3 @ Bk)) < 1e-8, "k* multiplicities", lv(np.linalg.eigvalsh(Bk.conj().T @ H3 @ Bk)))

# (e) item 4 real space: rotations + inversion + even translations, strong (strength 3) random, no H0
ok4 = True; m4 = []
for trial in range(3):
    Hs = symm(randH(rng), trans=EVEN, inv=True); Hs *= 3 / np.abs(Hs).max()
    assert np.allclose(conj_mat(Hs, INV), Hs)
    m = lv(np.linalg.eigvalsh(B2.conj().T @ Hs @ B2)); m4.append(m); ok4 &= all(x % 4 == 0 for x in m)
print("(e) rot + inv + even trans, strength 3, every range: folded levels all 4-fold:", ok4, m4)
# (f) inversion-only-by-uniform-part: uniform symmetric, staggered without inversion (control)
Hs = symm(randH(rng), trans=TV, inv=True) + symm(randH(rng), trans=EVEN) - symm(randH(rng), trans=TV)
print("(f) control without inversion:", lv(np.linalg.eigvalsh(B2.conj().T @ Hs @ B2)))
print(f"time {time.time()-t0:.1f}s")
