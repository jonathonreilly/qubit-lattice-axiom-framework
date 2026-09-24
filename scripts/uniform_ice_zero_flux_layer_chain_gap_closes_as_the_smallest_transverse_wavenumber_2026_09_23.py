#!/usr/bin/env python3
"""Finite zero-flux transfer spectra and layer-memory gap estimates.

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


def zero_flux(a, b):
    idx = np.arange(1 << (a * b))
    S = np.zeros(len(idx), dtype=np.int64)
    for y in range(b):
        for x in range(a):
            S += (-1) ** (x + y) * (2 * ((idx >> ((b - 1 - y) * a + x)) & 1) - 1)
    return np.where(S == 0)[0], len(idx)


def top_levels(a, b, k=7):
    mv = make_matvec(a, b)
    sel, N = zero_flux(a, b)

    def f(u):
        full = np.zeros(N)
        full[sel] = u
        return mv(full)[sel]
    if len(sel) <= 400:
        Mx = np.column_stack([f(e) for e in np.eye(len(sel))])
        assert np.allclose(Mx,Mx.T,rtol=0,atol=1e-10), "transfer symmetry"
        ev = np.linalg.eigvalsh(Mx)
    else:
        op = LinearOperator((len(sel), len(sel)), matvec=f, dtype=np.float64)
        rng = np.random.default_rng(8864+a*100+b)
        u,z = rng.normal(size=len(sel)),rng.normal(size=len(sel))
        assert abs(u@f(z)-z@f(u)) < 1e-10*max(1,np.linalg.norm(u)*np.linalg.norm(f(z))), "bilinear symmetry"
        ev,vecs = eigsh(op,k=k,which="LM",tol=1e-11,maxiter=50000,ncv=40,v0=rng.normal(size=len(sel)))
        assert np.allclose(vecs.T@vecs,np.eye(k),rtol=0,atol=1e-9), "Ritz orthogonality"
        assert all(np.linalg.norm(f(vecs[:,j])-ev[j]*vecs[:,j]) < 1e-8*max(abs(ev)) for j in range(k)), "Ritz residuals"
    return sorted(ev, key=lambda x: -abs(x))


LV = {}
for a, b in ((2, 2), (2, 4), (2, 6), (2, 8), (2, 10), (4, 4)):
    LV[(a, b)] = top_levels(a, b)
gap = {ab: float(np.log(abs(LV[ab][0]) / abs(LV[ab][1]))) for ab in LV}

print("== A. The values of open PR #8740 ==")
check("2 x 2: top 32 + 2 sqrt(209), next modulus 14; 2 x 4: next modulus 668.3638",
      abs(LV[(2, 2)][0] - (32 + 2 * 209 ** 0.5)) < 1e-9 and abs(abs(LV[(2, 2)][1]) - 14) < 1e-9
      and abs(abs(LV[(2, 4)][1]) - 668.3638) < 1e-4,
      f"{LV[(2, 2)][0]:.4f}, {abs(LV[(2, 2)][1]):.4f}; {abs(LV[(2, 4)][1]):.4f}")
print()

print("== B. The next level ==")
deg = {}
for ab, ev in LV.items():
    nxt = ev[1]
    deg[ab] = sum(1 for x in ev[1:] if abs(x - nxt) < 1e-6 * abs(nxt))
strips_ok = all(LV[(2, b)][1] < 0 and deg[(2, b)] == 2 for b in (2, 4, 6, 8, 10))
check("the next level is negative on every cross-section, twice degenerate on the strips and four times on the square",
      strips_ok and LV[(4, 4)][1] < 0 and deg[(4, 4)] == 4
      and all(len(ev)>deg[ab]+1 and abs(ev[deg[ab]+1]) < (1-1e-6)*abs(ev[1]) for ab,ev in LV.items()),
      "degeneracies " + ", ".join(f"{a}x{b}: {deg[(a, b)]}" for a, b in LV))
print()

print("== C. Strips: finite gap-times-width values ==")
seq = [gap[(2, b)] * b for b in (2, 4, 6, 8, 10)]
check("gap times b rises and stays below 2 pi on the five computed strips",
      all(seq[i] < seq[i + 1] for i in range(4)) and seq[-1] < 2 * np.pi and seq[-1] > 0.96 * 2 * np.pi,
      "gap x b = " + ", ".join(f"{x:.4f}" for x in seq) + f"; 2 pi = {2 * np.pi:.4f}")
print()

print("== D. Finite square and strip comparison ==")
check("the square 4 x 4 has the gap of the strip 2 x 4 within 2%",
      abs(gap[(4, 4)] / gap[(2, 4)] - 1) < 0.02, f"{gap[(4, 4)]:.5f} vs {gap[(2, 4)]:.5f}")
print()
print(f"time {time.time() - T0:.0f} s")
print('per_element: Row tensors count binary horizontal occupations; matrix contractions and all large spectral solves use floating-point arithmetic.')
print('per_site: Only the declared even periodic cross-sections are computed; the row ordering and bit convention are supplied implementation choices.')
print('per_mode: Numerical eigenpairs pass residual and symmetry controls; a finite computed spectrum is not a proof of asymptotic scaling.')
print('per_block: The quoted coefficient or gap inequalities concern the printed finite geometry list, with separate small exact-value controls.')
print('lattice_wide: Infinite transverse size, a Gaussian continuum limit and physical phase selection are not established by these finite computations.')
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
