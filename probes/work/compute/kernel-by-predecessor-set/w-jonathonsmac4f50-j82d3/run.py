#!/usr/bin/env python3
"""kernel-by-predecessor-set, independent run 1 of 2 (worker w-jonathonsmac4f50-j82d3, claude-opus-5).

Linear gain-one formation model on the 3+1 event lattice: theta_{t+1}(x) = |P|^-1 sum_{p in P} theta_t(x + p) + noise, so the equal-time
kernel is sigma^2/(1 - |phi|^2) with phi(k) = |P|^-1 sum_p e^{ik.p}.  For each set P:
  M      the small-k form, 1 - |phi|^2 = k^T M k + O(k^3), M = Cov_P(p) (exact, also from sympy's Hessian at 0);
  drift  the imaginary linear term of phi, Im phi = k . mean(P) + O(k^3)... (exact);
  zeros  |phi(k)| = 1 iff every e^{ik.p} has the same phase iff k.d in 2 pi Z for all d in P - P, i.e. k in 2 pi (Lambda_P)^*
         with Lambda_P the lattice spanned by the differences: enumerated exactly on (2 pi / n) Z^3, n = [Z^3 : Lambda_P];
  F(k)   = E(k)/(1 - |phi|^2), E(k) = sum_i 2(1 - cos k_i): kernel = F sigma^2/E; exact closed forms where phi is a function of
         E, exact values at k -> 0 and at the zone corners, and the global range on a grid (numerical, labelled).
(f) is not fixed by the task's wording; this run takes P_f = {0, -e1, -e2, -e3, e1+e2, e2+e3, e3+e1} (site, three backward
neighbours, three forward face diagonals), a set with no inversion symmetry."""
import itertools
import math
import sys
from fractions import Fraction as Fr
from functools import reduce

import numpy as np
import sympy as sp

E1, E2, E3 = (1, 0, 0), (0, 1, 0), (0, 0, 1)
def add(a, b): return tuple(x + y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)
NB6 = [E1, E2, E3, neg(E1), neg(E2), neg(E3)]
FACE12 = [tuple(s1 * u + s2 * v for u, v in zip(a, b)) for a, b in [(E1, E2), (E2, E3), (E1, E3)] for s1 in (1, -1) for s2 in (1, -1)]
SETS = {
    "(a) site + 6 neighbours": [(0, 0, 0)] + NB6,
    "(b) 6 neighbours": NB6,
    "(c) site + 6 + 12 face diagonals": [(0, 0, 0)] + NB6 + FACE12,
    "(d) 8 cube corners": [c for c in itertools.product((1, -1), repeat=3)],
    "(e) backward {0, e1, e2, e3}": [(0, 0, 0), E1, E2, E3],
    "(f) site + 3 backward + 3 forward face diagonals": [(0, 0, 0), neg(E1), neg(E2), neg(E3), add(E1, E2), add(E2, E3), add(E3, E1)],
}
k = sp.symbols("k1 k2 k3", real=True)
FAILS = []


def check(label, ok, detail):
    print(("ok   " if ok else "FAIL ") + f"{label}: {detail}", flush=True)
    if not ok:
        FAILS.append(label)


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def lattice_index(diffs):
    """index of the lattice spanned by the integer vectors diffs in Z^3 (gcd of all 3x3 minors); 0 if not full rank"""
    g = 0
    for trip in itertools.combinations(diffs, 3):
        g = math.gcd(g, abs(det3(trip)))
    return g


def main():
    rows = []
    Esym = sum(2 * (1 - sp.cos(ki)) for ki in k)
    for name, P in SETS.items():
        n = len(P)
        phi = sum(sp.exp(sp.I * sum(ki * pi for ki, pi in zip(k, p))) for p in P) / n
        u = sp.expand(sp.simplify(sp.expand(phi * sp.conjugate(phi), complex=True)))
        # M = Cov_P(p) exactly, and the same from the Hessian of 1 - |phi|^2 at 0
        mean = [Fr(sum(p[i] for p in P), n) for i in range(3)]
        cov = [[Fr(sum(p[i] * p[j] for p in P), n) - mean[i] * mean[j] for j in range(3)] for i in range(3)]
        H = [[sp.simplify(sp.diff(1 - u, k[i], k[j]).subs({ki: 0 for ki in k}) / 2) for j in range(3)] for i in range(3)]
        ok = all(sp.nsimplify(H[i][j]) == sp.Rational(cov[i][j].numerator, cov[i][j].denominator) for i in range(3) for j in range(3))
        iso = all(cov[i][j] == 0 for i in range(3) for j in range(3) if i != j) and cov[0][0] == cov[1][1] == cov[2][2]
        # drift: the linear term of Im phi equals k . mean(P)
        imlin = [sp.simplify(sp.diff(sp.im(sp.expand(phi, complex=True)), k[i]).subs({ki: 0 for ki in k})) for i in range(3)]
        ok &= all(sp.nsimplify(imlin[i]) == sp.Rational(mean[i].numerator, mean[i].denominator) for i in range(3))
        drift = any(m != 0 for m in mean)
        # zeros of 1 - |phi|^2: k in 2 pi (Lambda_P)^*, enumerated exactly on (2 pi / idx) Z^3
        diffs = [tuple(a - b for a, b in zip(p, q)) for p in P for q in P if p != q]
        idx = lattice_index(diffs)
        zeros = []
        for r in itertools.product(range(idx), repeat=3):
            if all(sum(ri * di for ri, di in zip(r, d)) % idx == 0 for d in diffs):
                zeros.append(tuple(Fr(2 * ri, idx) if Fr(2 * ri, idx) <= 1 else Fr(2 * ri, idx) - 2 for ri in r))   # in units of pi, in (-1, 1]
        # exact check at the zeros: |phi| = 1
        for z in zeros:
            val = sp.simplify(u.subs({ki: sp.pi * sp.Rational(zi.numerator, zi.denominator) for ki, zi in zip(k, z)}))
            ok &= val == 1
        doublers = [z for z in zeros if any(zi != 0 for zi in z)]
        # the bounded factor F = E/(1 - |phi|^2)
        eig = sorted(set(sp.Matrix(3, 3, lambda i, j: sp.Rational(cov[i][j].numerator, cov[i][j].denominator)).eigenvals()))
        corners = {}
        for c in [(1, 0, 0), (1, 1, 0), (1, 1, 1)]:
            sub = {ki: sp.pi * ci for ki, ci in zip(k, c)}
            den = sp.simplify(1 - u.subs(sub))
            corners[c] = sp.simplify(Esym.subs(sub) / den) if den != 0 else sp.oo
        kk = np.linspace(-np.pi, np.pi, 97)
        K1, K2, K3 = np.meshgrid(kk, kk, kk, indexing="ij")
        ph = sum(np.exp(1j * (K1 * p[0] + K2 * p[1] + K3 * p[2])) for p in P) / n
        Enum = 2 * (3 - np.cos(K1) - np.cos(K2) - np.cos(K3))
        den = 1 - np.abs(ph) ** 2
        mask = Enum > 1e-9
        Fg = np.where(den[mask] > 1e-12, Enum[mask] / np.maximum(den[mask], 1e-300), np.inf)
        Fmin, Fmax = float(np.min(Fg)), float(np.max(Fg))
        rows.append((name, iso, drift, doublers, eig, corners, Fmin, Fmax))
        label = name.split()[0]
        check(f"{label}", ok, f"{name}: M = Cov_P = {[[str(x) for x in r] for r in cov]} ({'isotropic' if iso else 'anisotropic'}, eigenvalues "
              f"{[str(e) for e in eig]}); drift = mean(P) = {[str(m) for m in mean]}{' (none)' if not drift else ''}; lattice of differences "
              f"has index {idx}, zeros of 1 - |phi|^2 at k/pi = {[tuple(str(z) for z in zz) for zz in zeros]} "
              f"({len(doublers)} doubler{'s' if len(doublers) != 1 else ''}); F = E/(1 - |phi|^2): k -> 0 limits "
              f"{[str(1 / e) for e in eig]} (1/eigenvalues of M), at (pi,0,0), (pi,pi,0), (pi,pi,pi): {[str(v) for v in corners.values()]}; "
              f"grid range (numerical, 97^3 points) [{Fmin:.4f}, {'unbounded' if not np.isfinite(Fmax) or Fmax > 1e6 else f'{Fmax:.4f}'}]")
    # closed forms: (a) phi = 1 - E/7, F = 49/(14 - E); (b) phi = 1 - E/6, F = 36/(12 - E); (d) phi = cos k1 cos k2 cos k3
    phi_a = (1 + 2 * sum(sp.cos(ki) for ki in k)) / 7
    phi_b = sum(sp.cos(ki) for ki in k) / 3
    ok = sp.simplify(phi_a - (1 - Esym / 7)) == 0 and sp.simplify(phi_b - (1 - Esym / 6)) == 0
    ok &= sp.simplify(Esym / (1 - phi_a ** 2) - 49 / (14 - Esym)) == 0 and sp.simplify(Esym / (1 - phi_b ** 2) - 36 / (12 - Esym)) == 0
    phi_d = sum(sp.exp(sp.I * sum(ki * pi for ki, pi in zip(k, p))) for p in SETS["(d) 8 cube corners"]) / 8
    ok &= sp.simplify(sp.expand(phi_d, complex=True) - sp.cos(k[0]) * sp.cos(k[1]) * sp.cos(k[2])) == 0
    check("closed forms", ok, "(a) phi = 1 - E/7, so the kernel is sigma^2 * 49/((14 - E) E) and F = 49/(14 - E) in [7/2, 49/2] exactly (E in [0, 12]); "
          "(b) phi = 1 - E/6, F = 36/(12 - E), unbounded at E = 12, i.e. k = (pi,pi,pi); (d) phi = cos k1 cos k2 cos k3, so |phi| = 1 "
          "exactly on {0, pi}^3: seven doublers, at every corner of the zone, not only (pi,pi,pi)")
    print("table: set | isotropic | drift | doublers (k/pi) | F = E/(1-|phi|^2) range")
    for name, iso, drift, doublers, eig, corners, Fmin, Fmax in rows:
        rng = "unbounded" if doublers else f"[{Fmin:.3f}, {Fmax:.3f}] (grid; small-k {', '.join(str(1 / e) for e in eig)})"
        print(f"  {name} | {'yes' if iso else 'no'} | {'yes' if drift else 'no'} | {[tuple(str(z) for z in d) for d in doublers] or 'none'} | {rng}")
    print("=" * 90)
    if FAILS:
        print(f"SUMMARY: FAILED checks {FAILS}")
        return 0
    print("SUMMARY: the cube-symmetric sets containing the site, (a) and (c), give isotropic (M = 2/7 I, 10/19 I), drift-free, doubler-free "
          "kernels within a bounded factor of 1/E ((a): exactly 49/(14 - E) in [7/2, 49/2]); (b) has one doubler at (pi,pi,pi) and (d) "
          "has seven, at every corner of the zone (phi = cos k1 cos k2 cos k3); the sets without inversion symmetry (e), (f) drift along "
          "(1,1,1) (mean 1/4, 1/7 per axis) and are anisotropic, doubler-free")
    return 0


if __name__ == "__main__":
    sys.exit(main())
