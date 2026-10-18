#!/usr/bin/env python3
"""Independent re-check of B14 E2 (order-eps closure of {C(N),C(M)} with a site scalar).

Different path from b14_lattice_closure.py: no polynomial Poisson engine. Every constraint at this order is a
quadratic/linear form, so the brackets are computed as matrices:
  kin(N) = 1/2 P^T A_N P,  R1(N) = r_N . h,  H_m(N) = 1/2 pi^T Lam_N pi + 1/2 phi^T W_N phi
  {kin(N)+sK R1(N), kin(M)+sK R1(M)} = sK (A_M r_N - A_N r_M) . P        ({h,P} = {phi,pi} = 1)
  {H_m(N), H_m(M)} = phi^T (W_N Lam_M - W_M Lam_N) pi
R1 is built independently from position-space second differences: R1 = sum_ij d_i d_j h_ij - lap tr h.
Closure test: does ONE bond field xi exist with D xi = gravity vector AND B_phi(xi) = Q_phi (AND B_chi(xi) = Q_chi)?
Solved as an exact linear system over QQ (sympy DomainMatrix rank). Torus side L (default 3; B14 used 4, 5).
"""
import random
import sys
from fractions import Fraction as F
from itertools import product

from sympy import QQ
from sympy.polys.matrices import DomainMatrix

L = int(sys.argv[1]) if len(sys.argv) > 1 else 3
ALPHA, K, MU = F(2, 5), F(7, 3), F(5, 2)   # different numbers from B14 (3/7, 5/11, 2/3)
KAP = K / (4 * ALPHA)
S = list(product(range(L), repeat=3))
SI = {x: i for i, x in enumerate(S)}
PAIRS = [(0, 1), (0, 2), (1, 2)]


def sh(x, j, s=1):
    y = list(x); y[j] = (y[j] + s) % L; return tuple(y)


# P/h index: diag (x,j), face (y,ij)
HIDX = {}
for x in S:
    for j in range(3):
        HIDX[("d", x, j)] = len(HIDX)
for y in S:
    for ij in PAIRS:
        HIDX[("f", y, ij)] = len(HIDX)
NB = 3 * len(S)  # bonds (x,j)
BIDX = {(x, j): 3 * SI[x] + j for x in S for j in range(3)}


def face_mean(n, y, ij):
    i, j = ij
    return (n[y] + n[sh(y, i)] + n[sh(y, j)] + n[sh(sh(y, i), j)]) / 4


def kin_grad(n, P):
    """A_N P as dict: d kin(N)/dP. kin = (1/4a) sum N (sum P_jj^2 - 1/2 (tr P)^2) + sum Nbar4 P_f^2/(8a)."""
    out = {}
    for x in S:
        tr = sum(P.get(("d", x, j), 0) for j in range(3))
        for j in range(3):
            out[("d", x, j)] = n[x] / (2 * ALPHA) * (P.get(("d", x, j), 0) - tr / 2)
    for y in S:
        for ij in PAIRS:
            out[("f", y, ij)] = face_mean(n, y, ij) / (4 * ALPHA) * P.get(("f", y, ij), 0)
    return out


def r1_coeffs(n):
    """d/dh of sum_x N_x R1_x with R1_x built in position space:
    diag: sum_j (d_j^2 h_jj - lap h_jj) ; face: 2 * mixed difference of h_ij landing on site x
    (face y spans y, y+ei, y+ej, y+ei+ej; the site-x mixed difference uses faces x, x-ei, x-ej, x-ei-ej)."""
    out = {k: F(0) for k in HIDX}
    for x in S:
        for j in range(3):
            for i in range(3):
                if i == j:
                    continue
                # -d_i^2 h_jj at x = -(h(x+i) - 2h(x) + h(x-i))
                for z, w in ((sh(x, i), -1), (x, 2), (sh(x, i, -1), -1)):
                    out[("d", z, j)] += n[x] * w
        for (i, j) in PAIRS:
            for z, w in ((x, 1), (sh(x, i, -1), -1), (sh(x, j, -1), -1), (sh(sh(x, i, -1), j, -1), 1)):
                out[("f", z, (i, j))] += 2 * n[x] * w
    return out


def D_of_bond(x, j):
    """column of G_g: delta h = d_i xi_j + d_j xi_i (diag: 2 * backward diff of xi_j at site; face: forward diffs)."""
    col = {}
    def add(k, v):
        col[k] = col.get(k, 0) + v
    add(("d", x, j), 2); add(("d", sh(x, j), j), -2)  # h_jj(z) = 2(xi(z,j) - xi(z-e_j,j))
    for (a, b) in PAIRS:
        # face y: xi(y+ea, b) - xi(y, b) + xi(y+eb, a) - xi(y, a)
        if j == b:
            add(("f", sh(x, a, -1), (a, b)), 1); add(("f", x, (a, b)), -1)
        if j == a:
            add(("f", sh(x, b, -1), (a, b)), 1); add(("f", x, (a, b)), -1)
    return col


def matter_Q(n, m, c):
    """phi^T (W_N Lam_M - W_M Lam_N) pi as dict (a,b)->coef; W_N = mu diag N + c sum_b Nbar_b d_b d_b^T."""
    def W(nn):
        w = {}
        for x in S:
            w[(x, x)] = w.get((x, x), 0) + MU * nn[x]
            for j in range(3):
                y = sh(x, j); nb = (nn[x] + nn[y]) / 2 * c
                for (a, b, v) in ((x, x, 1), (y, y, 1), (x, y, -1), (y, x, -1)):
                    w[(a, b)] = w.get((a, b), 0) + nb * v
        return w
    q = {}
    for (lapA, lapB, sgn) in ((n, m, 1), (m, n, -1)):
        for (a, b), v in W(lapA).items():
            q[(a, b)] = q.get((a, b), 0) + sgn * v * lapB[b]
    return {k: v for k, v in q.items() if v != 0}


def B_of_bond(x, j):
    """G_m[e_b] = (phi_y - phi_x)(pi_x + pi_y)/2 as dict (phi site, pi site)->coef."""
    y = sh(x, j)
    return {(y, x): F(1, 2), (y, y): F(1, 2), (x, x): F(-1, 2), (x, y): F(-1, 2)}


def closes(n, m, s, cs):
    """Exists xi with D xi = sK(A_M r_N - A_N r_M) and, for every species c in cs, B(xi) = Q_c ?"""
    rn, rm = r1_coeffs(n), r1_coeffs(m)
    am, an = kin_grad(m, rn), kin_grad(n, rm)
    vg = {k: s * K * (am[k] - an[k]) for k in HIDX}
    rows = {}
    def put(rowkey, col, val):
        rows.setdefault(rowkey, {})
        rows[rowkey][col] = rows[rowkey].get(col, 0) + val
    for (x, j), bi in BIDX.items():
        for k, v in D_of_bond(x, j).items():
            put(("g", k), bi, v)
        for sp in range(len(cs)):
            for k, v in B_of_bond(x, j).items():
                put(("m", sp, k), bi, v)
    rhs = {("g", k): v for k, v in vg.items()}
    for sp, c in enumerate(cs):
        for k, v in matter_Q(n, m, c).items():
            rhs[("m", sp, k)] = v
    keys = sorted(set(rows) | set(rhs), key=str)
    A = [[QQ(rows.get(r, {}).get(b, 0).numerator if isinstance(rows.get(r, {}).get(b, 0), F) else rows.get(r, {}).get(b, 0),
             rows.get(r, {}).get(b, 0).denominator if isinstance(rows.get(r, {}).get(b, 0), F) else 1) for b in range(NB)] for r in keys]
    def q(v):
        v = F(v); return QQ(v.numerator, v.denominator)
    Aug = [row + [q(rhs.get(r, 0))] for row, r in zip(A, keys)]
    r1 = DomainMatrix(A, (len(keys), NB), QQ).rank()
    r2 = DomainMatrix(Aug, (len(keys), NB + 1), QQ).rank()
    return r1 == r2


def gravity_alone(n, m, s):
    """sanity: D xi = gravity vector with the stated xi = (sK/4a)(N_{x+e}M_x - N_x M_{x+e})."""
    rn, rm = r1_coeffs(n), r1_coeffs(m)
    am, an = kin_grad(m, rn), kin_grad(n, rm)
    vg = {k: s * K * (am[k] - an[k]) for k in HIDX}
    tot = {k: F(0) for k in HIDX}
    for (x, j) in BIDX:
        xi = s * KAP * (n[sh(x, j)] * m[x] - n[x] * m[sh(x, j)])
        for k, v in D_of_bond(x, j).items():
            tot[k] += xi * v
    return all(tot[k] == vg[k] for k in HIDX)


if __name__ == "__main__":
    rng = random.Random(777)
    lap = lambda: {x: F(rng.randint(-4, 4)) for x in S}
    n, m = lap(), lap()
    print(f"L={L} alpha={ALPHA} K={K} kappa=K/(4alpha)={KAP}")
    print("gravity alone closes with xi=(sK/4a)(N_{x+e}M_x-N_xM_{x+e}):", {s: gravity_alone(n, m, s) for s in (1, -1)})
    for s in (1, -1):
        for cr in (F(1), F(-1), F(2), F(1, 2)):
            print(f"  s={s:+d} c/kappa={str(cr):>4}: closes={closes(n, m, s, [cr * KAP])}")
    for (c1, c2) in ((F(1), F(1)), (F(1), F(2)), (F(1), F(1, 3))):
        print(f"  two species s=-1 c1/kappa={c1} c2/kappa={c2}: closes={closes(n, m, -1, [c1 * KAP, c2 * KAP])}")
