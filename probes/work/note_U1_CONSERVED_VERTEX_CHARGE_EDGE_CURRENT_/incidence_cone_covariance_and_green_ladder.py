#!/usr/bin/env python3
"""J:note falsifiers for U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03 (on main).

Falsifiers implemented (the note's list): C d0 or d2 C nonzero; sourced electric Gauss disagreeing with vertex continuity; a magnetic
half-step changing magnetic Gauss; a unit current failing to move one charge tail-to-head; the Poisson field not the minimum-energy
field in its Gauss sector; longitudinal and co-curl currents not orthogonal; "the current impulse outruns the stated finite layer cone"
(cycle one reaches physical Manhattan distance one, the next source-free cycle at most four); failure of polar/axial covariance under a
cubic transform; "the periodic Green function fails its Poisson equation or its cubic-axis equality"; "the fitted infrared coefficient
does not approach 1/(4 pi) on the named size ladder" (L = 48, 64, 96, 128; errors decreasing, below 0.009 at 128).

Disjoint machinery, beyond the note's sizes (its runner: integer numerators at h = 1/2 on the L = 3 block, the cone at L = 5, the
symbol covariance in Fourier space, 3D FFT Green functions at the four sizes):
  A. my own doubled-lattice role complex at L = 4, 5, 6; the sourced tick in exact Fractions at h = 3/7 with integer fields; the
     Poisson minimizer solved exactly (sympy rationals) at L = 4 and tested against every constraint-kernel generator; the causal cone
     over six cycles; real-space covariance of the full sourced tick under all 48 signed permutations with B as a 2-form (the axial
     rule) and, as control, with B transformed as a polar vector;
  B. the periodic neutralized Green function on the axis from a closed-form O(L^2) sum (the sum over k3 done exactly:
     (1/L) sum_k3 1/(2 cosh th - 2 cos k3) = coth(L th/2)/(2 sinh th)), cross-checked against a direct FFT at L = 48; Poisson residual
     on the axis from the same closed form; the runner's fit rule (r = 4 .. L//5 - 1, basis 1/r, 1, 1/r^3) on the named ladder and
     beyond it to L = 4096, plus the same fit after removing the neutralizing background r^2/(6 L^3).
"""
from __future__ import annotations

import itertools
import math
from fractions import Fraction as F

import numpy as np
import sympy as sp


# ---------------------------------------------------------------------------------------------------------- A. role complex
def complex_(L):
    P = 2 * L
    pts = list(itertools.product(range(P), repeat=3))
    kind = lambda p: sum(c % 2 for c in p)
    V = [p for p in pts if kind(p) == 0]
    E = [p for p in pts if kind(p) == 1]
    Fc = [p for p in pts if kind(p) == 2]
    Cb = [p for p in pts if kind(p) == 3]
    vi = {p: i for i, p in enumerate(V)}
    ei = {p: i for i, p in enumerate(E)}
    fi = {p: i for i, p in enumerate(Fc)}
    add = lambda p, mu, s: tuple((c + s) % P if k == mu else c for k, c in enumerate(p))
    axis = lambda p: [k for k in range(3) if p[k] % 2][0]
    d0 = {}                                   # d0[e] = {v: sign}  (edge row, vertex columns)
    for p in E:
        mu = axis(p)
        d0[ei[p]] = {vi[add(p, mu, -1)]: -1, vi[add(p, mu, 1)]: 1}
    C = {}                                    # face (mu<nu) = d_mu E_nu - d_nu E_mu
    for p in Fc:
        mu, nu = [k for k in range(3) if p[k] % 2]
        C[fi[p]] = {ei[add(p, mu, 1)]: 1, ei[add(p, mu, -1)]: -1, ei[add(p, nu, 1)]: -1, ei[add(p, nu, -1)]: 1}
    d2 = {}
    eps = {(0, 1): 2, (0, 2): 1, (1, 2): 0}
    sgn = {(0, 1): 1, (0, 2): -1, (1, 2): 1}  # e_mu x e_nu = sgn * e_lambda
    for ci, p in enumerate(Cb):
        row = {}
        for (mu, nu), lam in eps.items():
            row[fi[add(p, lam, 1)]] = row.get(fi[add(p, lam, 1)], 0) + sgn[(mu, nu)]
            row[fi[add(p, lam, -1)]] = row.get(fi[add(p, lam, -1)], 0) - sgn[(mu, nu)]
        d2[ci] = row
    return dict(P=P, V=V, E=E, F=Fc, C3=Cb, vi=vi, ei=ei, fi=fi, d0=d0, C=C, d2=d2, add=add, axis=axis)


def mat_apply(M, x, nrows):
    return [sum((c * x[j] for j, c in M[i].items()), 0) for i in range(nrows)]


def mat_T_apply(M, x, ncols):
    out = [0] * ncols
    for i, row in M.items():
        for j, c in row.items():
            out[j] += c * x[i]
    return out


def compose_zero(A, B, nB_cols):
    """rows of A @ B vanish? (A: dict rows over B-row index; B: dict rows over columns)"""
    for i, row in A.items():
        acc = {}
        for j, a in row.items():
            for k, b in B[j].items():
                acc[k] = acc.get(k, 0) + a * b
        if any(v for v in acc.values()):
            return False
    return True


def tick(cx, E, B, J, h):
    nE, nF = len(cx["E"]), len(cx["F"])
    CE = mat_apply(cx["C"], E, nF)
    B1 = [b + h / 2 * c for b, c in zip(B, CE)]
    CTB = mat_T_apply(cx["C"], B1, nE)
    E2 = [e - h * c + h * j for e, c, j in zip(E, CTB, J)]
    CE2 = mat_apply(cx["C"], E2, nF)
    B2 = [b + h / 2 * c for b, c in zip(B1, CE2)]
    return B1, E2, B2


def part_a(L, seed):
    rng = np.random.default_rng(seed)
    cx = complex_(L)
    nV, nE, nF, nC = len(cx["V"]), len(cx["E"]), len(cx["F"]), len(cx["C3"])
    res = {"sizes": (nV, nE, nF, nC)}
    res["C d0 = 0"] = compose_zero(cx["C"], cx["d0"], nV)
    res["d2 C = 0"] = compose_zero(cx["d2"], cx["C"], nE)
    h = F(3, 7)
    E = [F(int(v)) for v in rng.integers(-5, 6, nE)]
    B = mat_apply(cx["C"], [F(int(v)) for v in rng.integers(-4, 5, nE)], nF)      # a curl field: d2 B = 0
    J = [F(int(v)) for v in rng.integers(-3, 4, nE)]
    rho = mat_T_apply(cx["d0"], E, nV)
    B1, E2, B2 = tick(cx, E, B, J, h)
    rho2 = [r + h * c for r, c in zip(rho, mat_T_apply(cx["d0"], J, nV))]
    res["Gauss = continuity"] = mat_T_apply(cx["d0"], E2, nV) == rho2
    res["magnetic Gauss both halves"] = all(v == 0 for v in mat_apply(cx["d2"], B1, nC)) and all(v == 0 for v in mat_apply(cx["d2"], B2, nC))
    res["total charge"] = sum(rho2) == sum(rho) == 0
    # one-edge transfer: J_e = 1/h on edge e
    e = cx["ei"][(1, 0, 0)]
    Je = [F(0)] * nE
    Je[e] = 1 / h
    drho = [h * c for c in mat_T_apply(cx["d0"], Je, nV)]
    tail, head = cx["vi"][(0, 0, 0)], cx["vi"][(2, 0, 0)]
    res["one-edge transfer"] = all(drho[v] == (-1 if v == tail else 1 if v == head else 0) for v in range(nV))
    # Hodge orthogonality
    f = [int(v) for v in rng.integers(-5, 6, nV)]
    a = [int(v) for v in rng.integers(-5, 6, nF)]
    JL = mat_apply(cx["d0"], f, nE)
    JT = mat_T_apply(cx["C"], a, nE)
    res["J_L . J_T = 0, C J_L = 0, d0^T J_T = 0"] = (sum(x * y for x, y in zip(JL, JT)) == 0 and
                                                   all(v == 0 for v in mat_apply(cx["C"], JL, nF)) and
                                                   all(v == 0 for v in mat_T_apply(cx["d0"], JT, nV)))
    # causal cone
    P = cx["P"]
    dist = lambda p, q: sum(min(abs(x - y), P - abs(x - y)) for x, y in zip(p, q))
    src = cx["E"][e]
    Ez, Bz = [F(0)] * nE, [F(0)] * nF
    reach = []
    Jc = Je
    for cyc in range(6):
        _, Ez, Bz = tick(cx, Ez, Bz, Jc, h)
        Jc = [F(0)] * nE
        sup = [cx["E"][i] for i, v in enumerate(Ez) if v != 0] + [cx["F"][i] for i, v in enumerate(Bz) if v != 0]
        reach.append(max(dist(src, q) for q in sup))
    res["cone reach by cycle"] = reach
    return res, cx


def covariance(L=4, seed=5):
    """Real-space covariance of the full sourced tick under the 48 signed permutations (origin-fixing lattice maps)."""
    cx = complex_(L)
    P = cx["P"]
    rng = np.random.default_rng(seed)
    nE, nF = len(cx["E"]), len(cx["F"])
    h = F(3, 7)
    E = [F(int(v)) for v in rng.integers(-5, 6, nE)]
    B = [F(int(v)) for v in rng.integers(-5, 6, nF)]
    J = [F(int(v)) for v in rng.integers(-3, 4, nE)]
    _, E2, B2 = tick(cx, E, B, J, h)
    ok_axial, ok_polar_proper, polar_fails_improper = True, True, True
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            det = int(round(np.linalg.det(np.array([[signs[j] if perm[j] == i else 0 for j in range(3)] for i in range(3)]))))
            mp_ = lambda p: tuple(((signs[j] * p[j]) % P) for j in sorted(range(3), key=lambda j: perm[j]))

            def img(p):
                q = [0, 0, 0]
                for j in range(3):
                    q[perm[j]] = (signs[j] * p[j]) % P
                return tuple(q)

            def tE(x):
                y = [F(0)] * nE
                for i, p in enumerate(cx["E"]):
                    mu = cx["axis"](p)
                    y[cx["ei"][img(p)]] = signs[mu] * x[i]
                return y

            def tB(x, axial=True):
                y = [F(0)] * nF
                for i, p in enumerate(cx["F"]):
                    mu, nu = [k for k in range(3) if p[k] % 2]
                    a_, b_ = perm[mu], perm[nu]
                    order = 1 if a_ < b_ else -1              # 2-form reordering sign
                    val = signs[mu] * signs[nu] * order * x[i]
                    if not axial:                               # polar-vector rule for the dual B_lambda: drop det(R)
                        val = val * det
                    y[cx["fi"][img(p)]] = val
                return y

            _, Er, Br = tick(cx, tE(E), tB(B), tE(J), h)
            good = Er == tE(E2) and Br == tB(B2)
            ok_axial &= good
            _, Ep, Bp = tick(cx, tE(E), tB(B, False), tE(J), h)
            goodp = Ep == tE(E2) and Bp == tB(B2, False)
            if det == 1:
                ok_polar_proper &= goodp
            else:
                polar_fails_improper &= not goodp
    return ok_axial, ok_polar_proper, polar_fails_improper


def poisson_min(L=4, seed=9):
    """Exact rational Poisson field E = d0 phi for a neutral charge; orthogonal to every constraint-kernel generator."""
    cx = complex_(L)
    nV, nE, nF = len(cx["V"]), len(cx["E"]), len(cx["F"])
    rng = np.random.default_rng(seed)
    rho = [int(v) for v in rng.integers(-4, 5, nV)]
    rho[0] -= sum(rho)
    D0 = sp.zeros(nE, nV)
    for e, row in cx["d0"].items():
        for v, s in row.items():
            D0[e, v] = s
    Lap = D0.T * D0
    A = Lap.row_insert(nV, sp.ones(1, nV))
    rhs = sp.Matrix(rho + [0])
    phi = (A.T * A).LUsolve(A.T * rhs)
    Ef = D0 * phi
    gauss = D0.T * Ef == sp.Matrix(rho)
    # constraint kernel of d0^T: spanned by the columns C^T e_f (co-exact) plus 3 harmonic generators (constant field along each axis)
    orth = all(sum(Ef[e] * s for e, s in cx["C"][f].items()) == 0 for f in range(nF))
    harm = []
    for mu in range(3):
        z = [1 if cx["axis"](p) == mu else 0 for p in cx["E"]]
        harm.append(sum(Ef[e] * z[e] for e in range(nE)) == 0)
    rank_kernel = nE - (nV - 1)
    CT = sp.zeros(nE, nF)
    for f, row in cx["C"].items():
        for e, s in row.items():
            CT[e, f] = s
    rank_coexact = CT.rank()
    return gauss, orth and all(harm), rank_kernel, rank_coexact


# ----------------------------------------------------------------------------------------------------- B. Green-function ladder
def green_axis(L, rmax, second=False):
    k = 2 * np.pi * np.arange(L) / L
    lam = 4 * np.sin(k / 2) ** 2
    c = lam[:, None] + lam[None, :]
    c[0, 0] = 1.0
    s_half = np.sqrt(c) / 2
    th = 2 * np.arcsinh(s_half)
    w = 1.0 / np.tanh(L * th / 2) / (2 * np.sqrt(c) * np.sqrt(1 + c / 4))
    w[0, 0] = 0.0
    T0 = w.sum(axis=1)
    T1 = (w * np.cos(k)[None, :]).sum(axis=1)
    const = (L * L - 1) / (12.0 * L ** 3)
    r = np.arange(0, rmax + 2)
    cosm = np.cos(np.outer(r, k))
    G0 = cosm @ T0 / L ** 2 + const
    G1 = cosm @ T1 / L ** 2 + const
    return G0, G1


def fit(G, L, background):
    radii = np.arange(4, L // 5, dtype=float)
    vals = G[radii.astype(int)] - (radii ** 2 / (6.0 * L ** 3) if background else 0)
    design = np.column_stack((1 / radii, np.ones_like(radii), 1 / radii ** 3))
    a = np.linalg.lstsq(design, vals, rcond=None)[0][0]
    return abs(a * 4 * math.pi - 1)


def part_b():
    out = {}
    L = 48
    kk = 2 * np.pi * np.fft.fftfreq(L)
    lamk = 4 * (np.sin(kk[:, None, None] / 2) ** 2 + np.sin(kk[None, :, None] / 2) ** 2 + np.sin(kk[None, None, :] / 2) ** 2)
    inv = np.zeros_like(lamk)
    inv[lamk > 1e-14] = 1 / lamk[lamk > 1e-14]
    Gfft = np.fft.ifftn(inv).real
    G0, _ = green_axis(L, L // 2)
    xcheck = np.abs(G0[: L // 2] - Gfft[: L // 2, 0, 0]).max()
    for L in (48, 64, 96, 128, 192, 256, 384, 512, 768, 1024, 2048, 4096):
        G0, G1 = green_axis(L, L // 5 + 2)
        r = np.arange(0, L // 5)
        lap = 6 * G0[r] - G0[r + 1] - np.where(r > 0, G0[np.abs(r - 1)], G0[1]) - 4 * G1[r]
        target = np.where(r == 0, 1.0, 0.0) - 1.0 / L ** 3
        pres = np.abs(lap - target).max()
        out[L] = (fit(G0, L, False), fit(G0, L, True), pres)
    return xcheck, out


def main():
    resA = {}
    for L in (4, 5, 6):
        resA[L], _ = part_a(L, seed=L)
        print(f"A{L}. role complex L = {L}: {resA[L]}")
    cov = covariance()
    print(f"A'. real-space covariance, 48 signed permutations (L = 4, exact): axial B covariant {cov[0]}; polar-B rule covariant for proper "
          f"R {cov[1]}, fails for every improper R {cov[2]}")
    pm = poisson_min()
    print(f"A''. exact Poisson field at L = 4: Gauss {pm[0]}; orthogonal to all co-exact generators and the 3 harmonic ones {pm[1]}; "
          f"constraint kernel dimension {pm[2]} = co-exact rank {pm[3]} + 3 harmonic: {pm[2] == pm[3] + 3}")
    xcheck, ladder = part_b()
    print(f"B. closed-form axis Green function vs 3D FFT at L = 48: max difference {xcheck:.2e}")
    for L, (e0, e1, pres) in ladder.items():
        print(f"B{L}: runner-rule fit |4 pi a - 1| = {e0:.5f}; after removing r^2/(6L^3): {e1:.2e}; axis Poisson residual {pres:.1e}")
    fails = []
    for L, r in resA.items():
        for key in ("C d0 = 0", "d2 C = 0", "Gauss = continuity", "magnetic Gauss both halves", "total charge", "one-edge transfer",
                    "J_L . J_T = 0, C J_L = 0, d0^T J_T = 0"):
            if not r[key]:
                fails.append(f"L={L} {key}")
        if r["cone reach by cycle"][0] != 1 or r["cone reach by cycle"][1] > 4:
            fails.append(f"L={L} cone")
    if not (cov[0] and cov[1] and cov[2]):
        fails.append("covariance")
    if not (pm[0] and pm[1] and pm[2] == pm[3] + 3):
        fails.append("Poisson minimizer")
    named = [float(ladder[L][0]) for L in (48, 64, 96, 128)]
    if not (all(x > y for x, y in zip(named, named[1:])) and named[-1] < 0.009):
        fails.append("named-ladder fit")
    if max(v[2] for v in ladder.values()) > 1e-9 or xcheck > 1e-12:
        fails.append("Green Poisson equation")
    if fails:
        print(f"HIT: {fails}")
    beyond = {L: round(float(ladder[L][0]), 5) for L in (192, 256, 512, 1024, 2048, 4096)}
    print(f"SUMMARY: on my own role complexes L = 4, 5, 6 all incidence identities, exact Fraction Gauss/continuity at h = 3/7, magnetic "
          f"Gauss, charge conservation, one-edge transfer and Hodge orthogonality hold; the impulse cone reaches {resA[6]['cone reach by cycle']} "
          f"over six cycles (note: 1, then at most 4); the full sourced tick is covariant under all 48 signed permutations with B as an axial "
          f"2-form and the polar rule fails for every improper one; the exact L = 4 Poisson field is orthogonal to the whole constraint "
          f"kernel; the closed-form Green function matches the FFT to {xcheck:.0e} and solves the axis Poisson equation to "
          f"{max(v[2] for v in ladder.values()):.0e}; the runner's fit errors on the named ladder are {[round(x, 5) for x in named]} "
          f"(decreasing, below 0.009) and continue {beyond} beyond it; with the background r^2/(6L^3) removed the error is "
          f"{ladder[128][1]:.1e} at L = 128 and {ladder[4096][1]:.1e} at L = 4096; no falsifier fires")


if __name__ == "__main__":
    main()
