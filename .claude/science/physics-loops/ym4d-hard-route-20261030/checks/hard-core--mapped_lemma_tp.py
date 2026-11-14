#!/usr/bin/env python3
"""Lemma TP of Text 5.9, at the trivial background: Poincare for transverse fields with a closed coarse average.

Written before running. Fine lattice spacing 1, coarse spacing ell (odd), periodic with coarse momenta p = 2 pi m/(ell n_c).
Space at p: H = (H(q_n)), q_n = p + 2 pi n/ell, n in Z_ell^d, each H(q_n) transverse at the fine lattice: qhat^* . H = 0.
Constraint: the coarse average Y_mu = sum_n conj(rho_mu(q_n)) H_mu(q_n) has zero transverse part at the coarse lattice,
that is Y is proportional to the coarse gradient symbol, so curl Q H = 0. Form: <H, -Delta H> = sum_n |qhat_n|^2 |H(q_n)|^2.
Let lambda(p) be the lowest value of the form on the unit sphere of this space, and lam := min over the p used.
In coarse units the statement is ||H||^2 <= C ||grad H||^2, that is ell^2 lam >= 1/C, with C free of ell.

PRE-STATED criteria.
 T0. Consistency: at each p, a null vector of the constraint found numerically has residual below 1e-10.
 T1. ell^2 lam > 0.05 for every case run.
 T2. Uniformity: for each d and n_c, ell^2 lam at the largest ell is at least 0.5 times its value at the smallest ell.
 T3. Control, to show the constraint is what gives the gap: with the constraint removed, ell^2 lambda(p) at the smallest nonzero p
     equals ell^2 |phat|^2, tending to 0 as n_c grows, relative error below 1e-10.
FAIL if any fails. Limitation: abelian, trivial background. RSS guard 2 GB.
"""
import itertools
import resource
import sys

import numpy as np


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def d_box(q, ell):
    s = np.sin(q / 2)
    if abs(s) < 1e-12:
        return float(ell)
    return np.sin(ell * q / 2) / s


def rho(q, mu, ell, d):
    out = 1.0 + 0j
    for nu in range(d):
        f = d_box(q[nu], ell) / ell
        if nu == mu:
            f = f * d_box(q[nu], ell) * np.exp(-1j * q[nu] * (ell - 1) / 2)
        out = out * f
    return out


def lowest(d, ell, p):
    qhat_list, basis_list = [], []
    rows = []
    cols = 0
    dc = np.exp(1j * ell * p) - 1
    Pc = np.eye(d, dtype=complex) - np.outer(dc, np.conj(dc)) / np.sum(np.abs(dc) ** 2)
    uc, sc, _ = np.linalg.svd(Pc)
    Ec = uc[:, sc > 0.5]  # coarse transverse directions, d-1 of them
    diag = []
    blocks = []
    for n in itertools.product(range(ell), repeat=d):
        q = p + 2 * np.pi * np.array(n) / ell
        qh = np.exp(1j * q) - 1
        nq = np.sum(np.abs(qh) ** 2)
        Pt = np.eye(d, dtype=complex) - np.outer(qh, np.conj(qh)) / nq
        u, sv, _ = np.linalg.svd(Pt)
        B = u[:, sv > 0.5]  # (d, d-1)
        R = np.array([np.conj(rho(q, mu, ell, d)) for mu in range(d)])
        blocks.append(np.conj(Ec.T) @ (R[:, None] * B))  # (d-1, d-1)
        diag.extend([nq] * (d - 1))
    A = np.hstack(blocks)  # constraint matrix (d-1, N)
    diag = np.array(diag)
    # null space of A
    u, sv, vh = np.linalg.svd(A, full_matrices=True)
    r = int(np.sum(sv > 1e-12 * sv[0]))
    Z = vh[r:].conj().T
    res = float(np.abs(A @ Z).max())
    M = (Z.conj().T * diag) @ Z
    lam = float(np.linalg.eigvalsh(M).min())
    return lam, res, float(diag.min())


def main():
    ok = True
    table = {}
    for d, ells, ncs in ((3, (3, 5, 7, 9), (8, 32)), (4, (3, 5), (8, 32))):
        for nc in ncs:
            for ell in ells:
                best = np.inf
                rmax = 0.0
                ms = [(1,) + (0,) * (d - 1), (1, 1) + (0,) * (d - 2), (nc // 2,) + (0,) * (d - 1), (nc // 2, nc // 2) + (0,) * (d - 2), (1,) * d]
                for m in ms:
                    p = 2 * np.pi * np.array(m) / (ell * nc)
                    lam, res, dmin = lowest(d, ell, p)
                    best = min(best, lam)
                    rmax = max(rmax, res)
                    if m == ms[0]:
                        p1 = np.sum(np.abs(np.exp(1j * p) - 1) ** 2)
                        ctl = abs(dmin - p1) / p1
                        ok = ok and ctl < 1e-10
                v = ell**2 * best
                table[(d, nc, ell)] = v
                good = rmax < 1e-10 and v > 0.05
                ok = ok and good
                print(f"d={d} nc={nc:3d} ell={ell} ell^2 lam={v:.4f} ctl_low={ell**2*p1:.4f} res={rmax:.1e} rss={rss_gb():.2f}GB {'ok' if good else 'VIOLATION'}", flush=True)
                if rss_gb() > 2:
                    print("RSS above 2 GB")
                    return 1
    for d, ells, ncs in ((3, (3, 5, 7, 9), (8, 32)), (4, (3, 5), (8, 32))):
        for nc in ncs:
            a, b = table[(d, nc, ells[0])], table[(d, nc, ells[-1])]
            good = b >= 0.5 * a
            ok = ok and good
            print(f"T2 d={d} nc={nc}: {a:.4f} -> {b:.4f} {'ok' if good else 'NOT UNIFORM'}")
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
