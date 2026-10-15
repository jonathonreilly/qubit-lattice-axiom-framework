"""CLS-1 step 6b (copy of cls1_loop.py header + quadratic-form check); step 6 (added after PREREG; see follow-up): is the corner-off-diagonal c-type structure regenerated at one loop
if the law sets P-c = P-d = 0 at tree level?  Toy: on-site pairing Yukawa sum_x y(x) [psi^T (i sigma_y) psi' H + h.c.],
y(x) = y0 + y1 sum_K cos(K.x) (class-S modulated; cubic- and Theta-covariant), psi, psi' walkers, H a relativistic lattice
scalar with Omega(l)^2 = m^2 + sum 4 sin^2(l/2). Continuous-time one loop, frequency integral done analytically:
  Sigma_{c'c}(iw=0, Q_c+q) = sum_{K1+K2 = Q_c+Q_c'} y_K1 y_K2 int_l  sigma.sin(p) / (2 Omega E (Omega+E)),  p = K1 - Q_c - q - l, E = |sin p|
  dSigma/d(iw)_{c'c}      = sum y_K1 y_K2 int_l 1 / (2 Omega (Omega+E)^2)
(overall sign convention irrelevant for the structure test). Output: decomposition of the linear-in-q light block into the
5 cubic-invariant structures (2 corner-diagonal = OBS-3's speed + tetragonal counterterms; 3 corner-off-diagonal = new under BCC),
and the flavour speed spread left after the two allowed per-field counterterms."""
import numpy as np, itertools, sys
sys.path.insert(0, '.')
from cls1_core import *
def P(*a): print(*a); sys.stdout.flush()
LC = [np.array([PI, 0, 0]), np.array([0, PI, 0]), np.array([0, 0, PI])]
KK = [np.zeros(3), KX, KY, KZ]
def same(a, b):
    d = (a - b) / (2 * PI); return np.allclose(d, np.round(d))
# ---- invariant basis (recomputed as in cls1_count.py) ----
def cidx(Q):
    for i, C in enumerate(LC):
        if same(Q, C): return i
Us = []
for R in rotations():
    Pm = np.zeros((3, 3))
    for i, C in enumerate(LC): Pm[cidx(R @ C), i] = 1
    Us.append((R, np.kron(Pm, spin_lift(R))))
def herm_basis(n, mask=None):
    B = []
    for i in range(n):
        for j in range(i, n):
            if mask is not None and not mask[i, j]: continue
            E = np.zeros((n, n), complex); E[i, j] = 1; E[j, i] = 1; B.append(E)
            if i != j:
                E = np.zeros((n, n), complex); E[i, j] = -1j; E[j, i] = 1j; B.append(E)
    return B
def inv4(mask=None):
    B = herm_basis(6, mask); nb = len(B); rows = []
    for R, U in Us:
        for b in range(3):
            blocks = []
            for bb in range(3):
                cols = [((1.0 if bb == b else 0.0) * (U @ E @ U.conj().T) - R[bb, b] * E).ravel() for E in B]
                blocks.append(np.array(cols).T)
            A = np.hstack(blocks); rows.append(np.vstack([A.real, A.imag]))
    A = np.vstack(rows); _, s, vh = np.linalg.svd(A, full_matrices=False)
    null = vh[np.sum(s > 1e-9):]
    return [np.concatenate([sum(v[b*nb+n] * B[n] for n in range(nb)).ravel() for b in range(3)]) for v in null]
dmask = np.kron(np.eye(3), np.ones((2, 2))).astype(bool)
Vall = np.array(inv4()).T; Vdiag = np.array(inv4(dmask)).T
# orthonormal: diagonal subspace + its complement inside the invariant span
Qd, _ = np.linalg.qr(np.vstack([Vdiag.real, Vdiag.imag]) if False else Vdiag)
proj_d = Qd @ Qd.conj().T
Voff = Vall - proj_d @ Vall
uo, so, _ = np.linalg.svd(Voff, full_matrices=False); Qo = uo[:, so > 1e-8]
P(f"invariant dim-4 span: {Vall.shape[1]} (diag {Qd.shape[1]}, off-diag {Qo.shape[1]})")

def sigma_light(N, m, y0, y1, q, shift=0.5):
    g = 2 * PI * (np.arange(N) + shift) / N
    l = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    Om = np.sqrt(m * m + (4 * np.sin(l / 2) ** 2).sum(1))
    yK = [y0, y1, y1, y1]
    S = np.zeros((6, 6), complex); Zm = np.zeros((6, 6), complex)
    for c, Qc in enumerate(LC):
        for cp, Qcp in enumerate(LC):
            for i1, K1 in enumerate(KK):
                for i2, K2 in enumerate(KK):
                    if not same(K1 + K2, Qc + Qcp): continue
                    p = K1 - Qc - q - l
                    s = np.sin(p); E = np.sqrt((s ** 2).sum(1))
                    w = 1.0 / (2 * Om * E * (Om + E))
                    vec = (s * w[:, None]).mean(0)
                    blk = sum(SIG[a] * vec[a] for a in range(3))
                    S[2*cp:2*cp+2, 2*c:2*c+2] += yK[i1] * yK[i2] * blk
                    Zm[2*cp:2*cp+2, 2*c:2*c+2] += yK[i1] * yK[i2] * np.mean(1.0 / (2 * Om * (Om + E) ** 2)) * s0
    return S, Zm

H0lin = [np.kron(np.diag([np.cos(C[b]) for C in LC]), SIG[b]) for b in range(3)]
rng = np.random.default_rng(7)
qdirs = [x / np.linalg.norm(x) for x in rng.normal(size=(30, 3))]

import sys as _s
cfgs = [(48, 0.1, 0.01, y0, 0.33) for y0 in (-0.33, 0.1, 0.2, 0.0, 0.33)]
for (N, m, d, y0, y1) in cfgs:
    Ms = []
    for b in range(3):
        e = np.eye(3)[b] * d
        Sp, _ = sigma_light(N, m, y0, y1, e); Sm, _ = sigma_light(N, m, y0, y1, -e)
        Ms.append((Sp - Sm) / (2 * d))
    vec = np.concatenate([M.ravel() for M in Ms])
    cd = Qd.conj().T @ vec; co = Qo.conj().T @ vec
    P(f"N={N} y0={y0:+.2f} y1={y1}: (y0-y1)^2={(y0-y1)**2:.4f} (y0-y1)y1={(y0-y1)*y1:+.4f} | |diag coeffs| {np.round(np.abs(cd),6)} | |off coeffs| {np.round(np.abs(co),6)}"
      f" | off/((y0-y1)y1) = {np.abs(co).max()/max(abs((y0-y1)*y1),1e-30):.5f}  diag/((y0-y1)^2) = {np.abs(cd).max()/max((y0-y1)**2,1e-30):.5f}")
