"""Items 2 and 4: representation content at +-k* with a single global 2O lift; class invariants;
inversion-rotation commutator; isotypic map under inversion; commutant multiplicities;
random symmetric Hamiltonians (own seeds/strengths) and break attempts."""
import itertools, time
import numpy as np
from common import *
from lift2O import build, so3, rid, TW

t0 = time.time()
G = build(1, -1)
Bk, Bm = Bloch(kst), Bloch(-kst)
Bs = {'k*': Bk, '-k*': Bm}
cen = [M for U, M in G if np.allclose(U, -np.eye(2))][0]
print("central element acts as -I on full space:", np.allclose(cen, -np.eye(nV)))

# class invariants on k*-restricted untwisted+twisted ops (no lift needed)
D = {lab: [B.conj().T @ dense(ROT[r]) @ B for r in range(24)] for lab, B in Bs.items()}
for lab in D:
    uni = all(np.allclose(X.conj().T @ X, np.eye(12)) for X in D[lab])
    inv = {}
    for r, R in enumerate(ROTS):
        tr = int(np.trace(R)); order = {3: 1, -1: 2, 0: 3, 1: 4}[tr]
        kind = {1: 'E', 3: 'C3', 4: 'C4'}.get(order) or ('C2axis' if np.allclose(np.abs(np.diag(R)), 1) else 'C2edge')
        Xt = (1j ** W1[r]) * D[lab][r]
        P = np.linalg.matrix_power(Xt, order)
        sc = P[0, 0] if np.allclose(P, P[0, 0] * np.eye(12)) else None
        inv.setdefault(kind, set()).add(None if sc is None else complex(np.round(sc, 8)))
    print(f"{lab}: restricted ops unitary {uni}; twisted (lift)^order scalars by class: {inv}")

def spin_char(j2, U):
    tr = max(-1, min(1, np.real(np.trace(U)) / 2)); th = 2 * np.arccos(tr)
    if abs(np.sin(th / 2)) < 1e-12: return float(j2 + 1) * (1 if np.isclose(tr, 1) else (-1) ** j2)
    return np.sin((j2 + 1) * th / 2) / np.sin(th / 2)
A2 = np.array([(-1.0) ** W1[rid(so3(U))] for U, M in G])
IRR = {'E1/2': np.array([spin_char(1, U) for U, M in G])}
IRR['E5/2'] = A2 * IRR['E1/2']; IRR['G3/2'] = np.array([spin_char(3, U) for U, M in G])
T1 = np.array([spin_char(2, U) for U, M in G])
IRR.update({'A1': np.ones(48), 'A2': A2, 'T1': T1, 'T2': A2 * T1, 'E': np.array([spin_char(4, U) for U, M in G]) - A2 * T1})
# sanity: orthonormality of the 8 irreps
Gram = np.array([[np.real(np.sum(np.conj(IRR[a]) * IRR[b])) / 48 for b in IRR] for a in IRR])
assert np.allclose(Gram, np.eye(len(IRR)))
Dl = {lab: [B.conj().T @ M @ B for U, M in G] for lab, B in Bs.items()}
def decomp(ops):
    ch = np.array([np.trace(X) for X in ops])
    d = {k: int(round(np.real(np.sum(np.conj(v) * ch)) / 48)) for k, v in IRR.items()}
    return {k: n for k, n in d.items() if n}
for lab in Dl: print(f"decomposition at {lab} (global lift):", decomp(Dl[lab]))
def isoproj(lab, irr):
    dim = int(round(np.real(IRR[irr][0])))
    return sum(dim / 48 * np.conj(c) * X for c, X in zip(IRR[irr], Dl[lab]))

# ---- item 4: inversion vs rotations
comm = []
for r in range(24):
    Y = compose(compose(INV, ROT[r]), compose(inverse(INV), inverse(ROT[r])))
    comm.append(const_sign(Y))
print("I R I^-1 R^-1 constant signs:", comm)
print("equals A2(R)=(-1)^w1:", comm == [(-1) ** w for w in W1], "; I^2 =", const_sign(compose(INV, INV)))
DI = Bm.conj().T @ dense(INV) @ Bk  # inversion k* -> -k*
print("inversion maps k* Bloch space onto -k* (unitary block):", np.allclose(DI.conj().T @ DI, np.eye(12)))
for a in ('E1/2', 'E5/2', 'G3/2'):
    Pa = isoproj('k*', a); img = DI @ Pa
    hits = {b: round(float(np.linalg.norm(isoproj('-k*', b) @ img) ** 2 / max(np.linalg.norm(img) ** 2, 1e-30)), 6) for b in ('E1/2', 'E5/2', 'G3/2')}
    print(f"  inversion image of {a}(k*) lies in -k* sectors (weight):", hits)

# commutant of {rotations, inversion} on the 24-dim folded space
B2 = np.hstack([Bk, Bm]); rng = np.random.default_rng(2026)
ops24 = [B2.conj().T @ dense(ROT[r]) @ B2 for r in range(24)] + [B2.conj().T @ dense(compose(INV, ROT[r])) @ B2 for r in range(24)]
assert all(np.allclose(X.conj().T @ X, np.eye(24)) for X in ops24)
def lv(ev, tol=1e-8):
    out = []; i = 0
    while i < len(ev):
        j = i
        while j + 1 < len(ev) and ev[j + 1] - ev[i] < tol: j += 1
        out.append(j + 1 - i); i = j + 1
    return out
mults = []
for trial in range(5):
    A = rng.normal(size=(24, 24)) + 1j * rng.normal(size=(24, 24)); A = A + A.conj().T
    Hc = sum(X @ A @ X.conj().T for X in ops24) / 48
    mults.append(lv(np.linalg.eigvalsh(Hc)))
print("commutant random elements on folded 24-space, level multiplicities:", mults)
# commutant dimension via averaging basis
basis = []
for i in range(24):
    for j in range(24):
        E = np.zeros((24, 24), complex); E[i, j] = 1
        basis.append((sum(X @ E @ X.conj().T for X in ops24) / 48).ravel())
cd = np.linalg.matrix_rank(np.array(basis), tol=1e-8)
print("commutant dimension (sum m_i^2):", cd)
# same without inversion
ops_rot = ops24[:24]
mults_r = []
for trial in range(3):
    A = rng.normal(size=(24, 24)) + 1j * rng.normal(size=(24, 24)); A = A + A.conj().T
    mults_r.append(lv(np.linalg.eigvalsh(sum(X @ A @ X.conj().T for X in ops_rot) / 24)))
print("rotations only (folded, no inversion):", mults_r)
print(f"time {time.time()-t0:.1f}s")
