#!/usr/bin/env python3
"""Independent re-check of B14 E5: can ANY local coupling sum Lapse * h * (pi pi) make the pi-pi sector of
{G_g[xi] + G_m[xi], H_m(N) + coupling(N)} equal H_m(N') (N' free, per configuration)?

Only the pi-pi sector is tested (a failure there is already a failure of exact closure; the coupling's phi-phi and
phi-pi pieces cannot produce pi-pi monomials). The ansatze are LARGER than B14's 18-term cubic-covariant one and
impose NO lattice symmetry:
  A: matched timing (site lapse N_x on h_jj(x), four-corner mean on h_ij(face)); diag pi pairs from the 7-point star,
     face pi pairs from the 4 face corners.
  B: as A with longer range: diag pi pairs from the 19-point set {0, +-e_k, +-e_k +- e_l}, face pairs from the
     12-point set corners + in-plane neighbours of corners.
  C: as A but the lapse is FREE per term: N_(x+w) with w in the 7-point star (diag) / any corner (face).
Positive control: replace {G_m, H_m}_pipi by itself minus the claimed obstruction
  (1/2) xi_b (N_y - N_x) [pi_x pi_y - (pi_x^2 + pi_y^2)/2]       (b = x -> y)
which should then close (with matched timing).
Exact rational linear algebra (sympy DomainMatrix over QQ, sparse).
"""
import random
import sys
from fractions import Fraction as F
from itertools import product, combinations_with_replacement

from sympy import QQ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.sdm import SDM

L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
S = list(product(range(L), repeat=3))
PAIRS = [(0, 1), (0, 2), (1, 2)]
E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def add(a, b, s=1):
    return tuple((a[k] + s * b[k]) % L for k in range(3))


def vec(*terms):
    v = [0, 0, 0]
    for c, k in terms:
        v[k] += c
    return tuple(v)


STAR = [(0, 0, 0)] + [vec((s, k)) for k in range(3) for s in (1, -1)]
STAR19 = STAR + [vec((s, k), (t, l)) for k in range(3) for l in range(k + 1, 3) for s in (1, -1) for t in (1, -1)]


def corners(ij):
    i, j = ij
    return [(0, 0, 0), E[i], E[j], tuple(E[i][k] + E[j][k] for k in range(3))]


def face_ext(ij):
    i, j = ij
    c = corners(ij)
    ext = set(c)
    for p in c:
        for k in (i, j):
            for s in (1, -1):
                ext.add(tuple(p[m] + (s if m == k else 0) for m in range(3)))
    return sorted(ext)


def mono(z, w):
    return (z, w) if z <= w else (w, z)


def dxi(xi, kind, z, comp):
    """(D xi) component: diag (z, j): 2(xi(z,j) - xi(z-e_j,j)); face (z,(a,b)): xi(z+ea,b)-xi(z,b)+xi(z+eb,a)-xi(z,a)."""
    if kind == "d":
        j = comp
        return 2 * (xi[(z, j)] - xi[(add(z, E[j], -1), j)])
    a, b = comp
    return xi[(add(z, E[a]), b)] - xi[(z, b)] + xi[(add(z, E[b]), a)] - xi[(z, a)]


def build_ops(ansatz):
    ops = []  # (kind, comp, (u, v), lapse spec)
    for j in range(3):
        pts = STAR19 if ansatz == "B" else STAR
        for u, v in combinations_with_replacement(pts, 2):
            lapses = [("site", w) for w in STAR] if ansatz == "C" else [("site", (0, 0, 0))]
            for lp in lapses:
                ops.append(("d", j, (u, v), lp))
    for ij in PAIRS:
        pts = face_ext(ij) if ansatz == "B" else corners(ij)
        for u, v in combinations_with_replacement(pts, 2):
            lapses = [("site", w) for w in corners(ij)] if ansatz == "C" else [("mean4", None)]
            for lp in lapses:
                ops.append(("f", ij, (u, v), lp))
    return ops


def lapse_val(n, z, kind, comp, lp):
    if lp[0] == "site":
        return n[add(z, lp[1])]
    return sum(n[add(z, c)] for c in corners(comp)) / 4


def matter_pipi(n, xi, control):
    out = {}
    def put(m, v):
        out[m] = out.get(m, 0) + v
    for x in S:
        for j in range(3):
            y = add(x, E[j]); b = xi[(x, j)]
            # (1/2)(pi_x + pi_y)(N_y pi_y - N_x pi_x) * xi_b
            put(mono(y, y), b * n[y] / 2); put(mono(x, x), -b * n[x] / 2)
            put(mono(x, y), b * (n[y] - n[x]) / 2)
            if control:
                ob = b * (n[y] - n[x]) / 2
                put(mono(x, y), -ob); put(mono(x, x), ob / 2); put(mono(y, y), ob / 2)
    return out


def run(ansatz, nconf=3, control=False, seed=11):
    rng = random.Random(seed)
    ops = build_ops(ansatz)
    nop = len(ops)
    cols = {}   # column index -> {row: val}; rows keyed (conf, monomial)
    rhs = {}
    rowid = {}
    def rid(key):
        if key not in rowid:
            rowid[key] = len(rowid)
        return rowid[key]
    ncol = nop + nconf * len(S)
    for cf in range(nconf):
        n = {x: F(rng.randint(-4, 4)) for x in S}
        xi = {(x, j): F(rng.randint(-4, 4)) for x in S for j in range(3)}
        for m, v in matter_pipi(n, xi, control).items():
            if v:
                r = rid((cf, m)); rhs[r] = rhs.get(r, 0) + v
        for p, (kind, comp, (u, v), lp) in enumerate(ops):
            col = cols.setdefault(p, {})
            for z in S:
                d = dxi(xi, kind, z, comp)
                if d == 0:
                    continue
                w = d * lapse_val(n, z, kind, comp, lp)
                if w == 0:
                    continue
                r = rid((cf, mono(add(z, u), add(z, v))))
                col[r] = col.get(r, 0) + w
        for zi, z in enumerate(S):  # free N': (1/2) N'_z pi_z^2
            col = cols.setdefault(nop + cf * len(S) + zi, {})
            r = rid((cf, mono(z, z)))
            col[r] = col.get(r, 0) + F(1, 2)
    nrow = len(rowid)
    def q(v):
        v = F(v); return QQ(v.numerator, v.denominator)
    rows = {}
    for c, col in cols.items():
        for r, v in col.items():
            if v:
                rows.setdefault(r, {})[c] = q(v)
    A = DomainMatrix.from_rep(SDM(rows, (nrow, ncol), QQ))
    rowsb = {r: dict(d) for r, d in rows.items()}
    for r, v in rhs.items():
        if v:
            rowsb.setdefault(r, {})[ncol] = q(v)
    Ab = DomainMatrix.from_rep(SDM(rowsb, (nrow, ncol + 1), QQ))
    ra, rb = A.rank(), Ab.rank()
    return nop, nrow, ra, rb


if __name__ == "__main__":
    print(f"L={L}")
    for ans, ctrl in (("A", True), ("A", False), ("C", False), ("B", False)):
        nop, nrow, ra, rb = run(ans, control=ctrl)
        verdict = "CLOSES" if ra == rb else "NO CLOSURE"
        tag = "positive control (obstruction removed)" if ctrl else "B14 matter bracket"
        print(f"ansatz {ans} [{tag}]: {nop} coupling ops, {nrow} eqs, rank A={ra}, rank [A|b]={rb} -> {verdict}", flush=True)
