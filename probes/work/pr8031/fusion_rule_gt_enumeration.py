#!/usr/bin/env python3
"""J:attack-g:PR8031 - finite-transporter note (PR #8031), pattern (g) PROOF STEP BY BRUTE FORCE on section 2's finite fact

  "Fundamental fusion is (1,0) tensor (p,q) = (p+1,q) plus (p-1,q+1) plus (p,q-1), with invalid labels omitted. Hence multiplication by
   any g_ij takes p+q <= R-1 entirely into p+q <= R. The same holds for conjugate multiplication using the conjugate fusion rule."

and the normalization of its witness ("psi_R(g) = sqrt(d_(R,0)) g_11^R, d_(R,0) = (R+1)(R+2)/2, ... norm 1 by Schur orthogonality"; "every
g_i1 g_11^R is a matrix coefficient of Sym^(R+1)(C^3) ... the single irrep (R+1,0)"). (The shell support of D_R, ||D_R|| = 1, the energy
bound (2) and the path bound (4) were brute-forced in an explicit Peter-Weyl basis in this PR's pattern-(f) attack; not repeated.)

Verified literally by enumeration:
  * weight multisets of every SU(3) irrep (p, q), p + q <= 14, from Gelfand-Tsetlin patterns of the top row (p+q, q, 0); the multiset of
    (1,0) x (p,q) against the sum of the three stated summands with exactly the stated omissions (a label with a negative entry dropped),
    compared as SU(3) weights (modulo (1,1,1)); likewise the conjugate rule (0,1) x (p,q) = (p,q+1) + (p+1,q-1) + (p-1,q); dimensions;
    the shell statement: every summand of (1,0) x (p,q) and (0,1) x (p,q) with p + q <= R - 1 has label sum <= R;
  * E|g_11|^(2R) = 1/d_(R,0) exactly from the law of |g_11|^2 (the first column of a Haar SU(3) matrix is uniform on the unit sphere of
    C^3, so |g_11|^2 ~ Beta(1, 2)), and by Monte Carlo over 400000 Haar matrices; dim Sym^(R+1)(C^3) = d_(R+1,0).
HIT if a stated decomposition, omission or normalization fails.
"""
import math
import sys
from collections import Counter
from fractions import Fraction

import numpy as np


def gt_weights(top):
    l1, l2, l3 = top
    out = Counter()
    for m12 in range(l2, l1 + 1):
        for m22 in range(l3, l2 + 1):
            for m11 in range(m22, m12 + 1):
                w = (m11, m12 + m22 - m11, l1 + l2 + l3 - m12 - m22)
                out[(w[0] - w[2], w[1] - w[2])] += 1          # SU(3) weight: modulo (1,1,1)
    return out


def irrep(p, q):
    return gt_weights((p + q, q, 0))


def dim(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def tensor(A, B):
    out = Counter()
    for a, ma in A.items():
        for b, mb in B.items():
            out[(a[0] + b[0], a[1] + b[1])] += ma * mb
    return out


def main():
    N = 14
    fund, conj = irrep(1, 0), irrep(0, 1)
    bad, badc, dim_bad, shell_bad, checked = [], [], [], [], 0
    for p in range(N + 1):
        for q in range(N + 1 - p):
            V = irrep(p, q)
            assert sum(V.values()) == dim(p, q)
            lhs = tensor(fund, V)
            stated = [(p + 1, q), (p - 1, q + 1), (p, q - 1)]
            kept = [(a, b) for a, b in stated if a >= 0 and b >= 0]
            rhs = Counter()
            for a, b in kept:
                rhs.update(irrep(a, b))
            if lhs != rhs:
                bad.append((p, q))
            lhs_c = tensor(conj, V)
            stated_c = [(p, q + 1), (p + 1, q - 1), (p - 1, q)]
            kept_c = [(a, b) for a, b in stated_c if a >= 0 and b >= 0]
            rhs_c = Counter()
            for a, b in kept_c:
                rhs_c.update(irrep(a, b))
            if lhs_c != rhs_c:
                badc.append((p, q))
            if 3 * dim(p, q) != sum(dim(a, b) for a, b in kept) or 3 * dim(p, q) != sum(dim(a, b) for a, b in kept_c):
                dim_bad.append((p, q))
            for R in range(p + q + 1, N + 2):
                if any(a + b > R for a, b in kept + kept_c):
                    shell_bad.append((p, q, R))
            checked += 1
    print(f"[fusion] {checked} labels (p, q) with p + q <= {N}: (1,0) x (p,q) equals the stated sum with its omissions in {checked - len(bad)} "
          f"(failures {bad[:5]}); (0,1) x (p,q) equals the conjugate rule in {checked - len(badc)} (failures {badc[:5]}); dimensions "
          f"3 d(p,q) = sum of the kept summands' dimensions everywhere: {not dim_bad}; every summand of a label with p + q <= R - 1 lies in "
          f"p + q <= R: {not shell_bad}; e.g. (1,0) x (0,0) -> {[(a, b) for a, b in [(1, 0), (-1, 1), (0, -1)] if a >= 0 and b >= 0]}, "
          f"(1,0) x (0,2) -> {[(a, b) for a, b in [(1, 2), (-1, 3), (0, 1)] if a >= 0 and b >= 0]}")
    # ---- the witness normalization
    exact = [Fraction(2 * math.factorial(R), math.factorial(R + 2)) for R in range(0, 11)]
    inv_d = [Fraction(1, (R + 1) * (R + 2) // 2) for R in range(0, 11)]
    rng = np.random.default_rng(8031)
    Z = rng.standard_normal((400000, 3, 3)) + 1j * rng.standard_normal((400000, 3, 3))
    Qm, Rm = np.linalg.qr(Z)
    ph = np.diagonal(Rm, axis1=1, axis2=2) / np.abs(np.diagonal(Rm, axis1=1, axis2=2))
    Qm = Qm * ph[:, None, :]
    Qm = Qm / np.linalg.det(Qm)[:, None, None] ** (1 / 3)
    x = np.abs(Qm[:, 0, 0]) ** 2
    mc = [float(np.mean(x ** R)) for R in range(0, 11)]
    se = [float(np.std(x ** R) / math.sqrt(len(x))) for R in range(0, 11)]
    z_max = max(abs(m - float(e)) / s if s > 0 else 0 for m, e, s in zip(mc, exact, se))
    sym_ok = all(math.comb(R + 1 + 2, 2) == dim(R + 1, 0) for R in range(0, 40))
    print(f"[witness] E|g_11|^(2R) = B(R+1, 2)/B(1, 2) = 2 R!/(R+2)! equals 1/d_(R,0) for R = 0..10: {exact == inv_d}; Monte Carlo over "
          f"400000 Haar SU(3) matrices agrees within {z_max:.2f} standard errors (R = 0..10; R = 3: {mc[3]:.6f} vs {float(exact[3]):.6f}); "
          f"dim Sym^(R+1)(C^3) = C(R+3, 2) = d_(R+1,0) for R < 40: {sym_ok}")
    hits = []
    if bad or badc or dim_bad or shell_bad:
        hits.append(f"fusion: {bad[:3]} conjugate {badc[:3]} dims {dim_bad[:3]} shell {shell_bad[:3]}")
    if exact != inv_d or z_max > 5 or not sym_ok:
        hits.append(f"witness normalization: exact {exact == inv_d}, MC z {z_max}, Sym {sym_ok}")
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: pattern (g) PROOF STEP BY BRUTE FORCE on section 2's fusion step - both fusion rules hold with exactly the stated "
          f"omissions for all {checked} labels with p + q <= {N} by Gelfand-Tsetlin weight enumeration (dimensions and the shell statement "
          f"included), and the witness psi_R is normalized as stated (E|g_11|^(2R) = 1/d_(R,0) exactly, Monte Carlo within {z_max:.1f} s.e.); "
          f"{len(hits)} failures; the step holds as written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
