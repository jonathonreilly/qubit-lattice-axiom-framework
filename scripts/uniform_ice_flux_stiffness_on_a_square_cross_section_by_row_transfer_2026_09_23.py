#!/usr/bin/env python3
"""Finite flux-sector estimates from a row-wise ice transfer.

Only the listed finite cross-sections and supplied uniform-ice transfer model are studied. Large spectra are numerical eigensolver estimates, with residual controls rather than an exact completeness proof. Negative eigenvalues imply alternating contributions only for observables overlapping those modes. No large-cross-section limit, physical phase, axiom selection or retained audit grade is established.
"""
import sys

AUDIT_TIMEOUT_SEC = 900
import time

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

PASS = FAIL = 0
T0 = time.time()


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))


def row_tensor(a):
    """R[v, out, w, in]: number of horizontal link sets h in {0,1}^a with
    h[x-1] + h[x] + in[x] + out[x] + v[x] + w[x] = 3 at every vertex x of the row."""
    n = 1 << a
    R = np.zeros((n, n, n, n))
    bits = lambda z: [(z >> i) & 1 for i in range(a)]
    for h in range(n):
        hb = bits(h)
        hdeg = [hb[(x - 1) % a] + hb[x] for x in range(a)]
        for w in range(n):
            wb = bits(w)
            for i in range(n):
                ib = bits(i)
                for o in range(n):
                    ob = bits(o)
                    need = [3 - hdeg[x] - ib[x] - ob[x] - wb[x] for x in range(a)]
                    if all(t in (0, 1) for t in need):
                        R[sum(t << x for x, t in enumerate(need)), o, w, i] += 1
    return R


def make_matvec(a, b):
    R = row_tensor(a)
    n = 1 << a

    def matvec(phi):
        A = phi.reshape((n,) * b)
        A = np.einsum("...,ij->...ij", A, np.eye(n))
        for r in range(b):
            A = np.tensordot(A, R, axes=([r, b], [2, 3]))
            A = np.moveaxis(A, [b, b + 1], [r, b])
        return np.einsum("...ii->...", A).reshape(-1)
    return matvec


def flux(a, b):
    idx = np.arange(1 << (a * b))
    S = np.zeros(len(idx), dtype=np.int64)
    for y in range(b):
        for x in range(a):
            S += (-1) ** (x + y) * (2 * ((idx >> ((b - 1 - y) * a + x)) & 1) - 1)
    return S


def sector_top(matvec, S, s):
    sel = np.where(np.abs(S) == s)[0]
    N = len(S)

    def mv(u):
        full = np.zeros(N)
        full[sel] = u
        return matvec(full)[sel]
    if len(sel) <= 400:
        Mx = np.column_stack([mv(e) for e in np.eye(len(sel))])
        assert np.allclose(Mx,Mx.T,rtol=0,atol=1e-10), "transfer symmetry"
        return float(np.linalg.eigvalsh(Mx).max())
    op = LinearOperator((len(sel), len(sel)), matvec=mv, dtype=np.float64)
    rng = np.random.default_rng(8859 + len(sel))
    u,z = rng.normal(size=len(sel)),rng.normal(size=len(sel))
    assert abs(u@mv(z)-z@mv(u)) < 1e-10 * max(1,np.linalg.norm(u)*np.linalg.norm(mv(z))), "bilinear symmetry"
    vals,vecs = eigsh(op,k=1,which="LA",tol=1e-12,maxiter=20000,v0=rng.normal(size=len(sel)))
    assert np.linalg.norm(mv(vecs[:,0])-vals[0]*vecs[:,0]) < 1e-9*abs(vals[0]), "Perron residual"
    return float(vals[0])


def stiffness(a, b, smax=2):
    mv = make_matvec(a, b)
    S = flux(a, b)
    lam = {s: sector_top(mv, S, s) for s in range(0, smax + 1, 2)}
    A = a * b
    return lam, {s: A / s ** 2 * np.log(lam[0] / lam[s]) for s in lam if s}


print("== A. The row transfer reproduces open PR #8746 ==")
mv22 = make_matvec(2, 2)
T22 = np.column_stack([mv22(e) for e in np.eye(16)])
lam, c = {}, {}
for b in (2, 4, 6):
    lam[b], c[b] = stiffness(2, b)
ref = {2: (60.9137, 46.0), 4: (2401.3316, 2059.3564), 6: (105338.1323, 94930.3065)}
check("trace T^2 = 9600 on 2 x 2, the transfer is symmetric, and the top eigenvalues match open PR #8746 on 2 x 2, 2 x 4, 2 x 6",
      round(float(np.trace(T22 @ T22))) == 9600 and np.allclose(T22, T22.T)
      and all(abs(lam[b][0] - ref[b][0]) < 1e-3 and abs(lam[b][2] - ref[b][1]) < 1e-3 for b in ref),
      "lam0 = " + ", ".join(f"{lam[b][0]:.4f}" for b in ref))
print()

print("== B. The square 4 x 4 ==")
L44, C44 = stiffness(4, 4, smax=8)
mono = all(L44[s] > L44[s + 2] for s in range(0, 8, 2))
check("the top eigenvalue falls with the flux across |S| = 0, 2, 4, 6, 8", mono,
      "lam = " + ", ".join(f"{L44[s]:.1f}" for s in sorted(L44)))
check("c(S) = (A / S^2) ln(lam_0 / lam_S) is 0.327 at |S| = 2 and within 3% of it up to |S| = 6",
      abs(C44[2] - 0.327) < 0.001 and all(abs(C44[s] / C44[2] - 1) < 0.03 for s in (4, 6)),
      "c = " + ", ".join(f"{C44[s]:.4f}" for s in sorted(C44)))
print()

print("== C. Shape at equal area ==")
L28, C28 = stiffness(2, 8)
check("the strip 2 x 8 has c = 0.314 at |S| = 2, about 4% below the square's",
      abs(C28[2] - 0.314) < 0.001 and 0.03 < 1 - C28[2] / C44[2] < 0.05, f"{C28[2]:.4f} vs {C44[2]:.4f}")
print()

print("== D. Strips of width 2 ==")
L210, C210 = stiffness(2, 10)
seq = [c[2][2], c[4][2], c[6][2], C28[2], C210[2]]
check("c at |S| = 2 rises with the strip's length, b = 2, 4, 6, 8, 10",
      all(seq[i] < seq[i + 1] for i in range(4)) and seq[-1] - seq[-2] < 0.002, ", ".join(f"{x:.4f}" for x in seq))
print()
print(f"time {time.time() - T0:.0f} s")
print('per_element: Row tensors count binary horizontal occupations; matrix contractions and all large spectral solves use floating-point arithmetic.')
print('per_site: Only the declared even periodic cross-sections are computed; the row ordering and bit convention are supplied implementation choices.')
print('per_mode: Numerical eigenpairs pass residual and symmetry controls; a finite computed spectrum is not a proof of asymptotic scaling.')
print('per_block: The quoted coefficient or gap inequalities concern the printed finite geometry list, with separate small exact-value controls.')
print('lattice_wide: Infinite transverse size, a Gaussian continuum limit and physical phase selection are not established by these finite computations.')
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
