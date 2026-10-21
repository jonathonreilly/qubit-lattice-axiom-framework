#!/usr/bin/env python3
"""B4 independent check (a): exact polynomial count of symmetry-invariant two-derivative quadratic
forms S(k,h) on symmetric h_{mu nu}, their gauge-invariant subspace, and the eps-eps-M theorem.

Independent path: no SVD, no rank-6 tensors.  Forms are polynomials (degree 2 in the h_ab, a<=b,
degree 2 in k); invariants are Reynolds (orbit) sums of monomials under signed permutations; gauge
invariance is the exact polynomial identity  d/dt S(k, h + t(k xi^T + xi k^T)) = 0, solved over QQ.
Theorem tested: in d = 4 every gauge-invariant form is L_M = eps^{a c e al} eps^{b d f be} M_{al be}
k_e k_f h_ab h_cd for a unique symmetric M (dimension 10); L_M is ray-equal to linearised EH about
g0 = M (nondegenerate M), whose only characteristic is adj(M)(k,k) = 0 -> no birefringence.
"""
import itertools
import random
from fractions import Fraction as F

import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy import QQ

HC4 = [(a, b) for a in range(4) for b in range(a, 4)]


def monomials(d):
    hc = [(a, b) for a in range(d) for b in range(a, d)]
    hh = [(I, J) for I in range(len(hc)) for J in range(I, len(hc))]
    kk = [(e, f) for e in range(d) for f in range(e, d)]
    return hc, [(x, y) for x in hh for y in kk]


def act(g, mon, hc):
    perm, sgn = g
    (I, J), (e, f) = mon
    s = 1
    newh = []
    for X in (I, J):
        a, b = hc[X]
        s *= sgn[a] * sgn[b]
        newh.append(hc.index(tuple(sorted((perm[a], perm[b])))))
    s *= sgn[e] * sgn[f]
    return (tuple(sorted(newh)), tuple(sorted((perm[e], perm[f])))), s


def group(d, kind):
    out = []
    if kind == "trivial":
        return [(tuple(range(d)), (1,) * d)]
    perms = list(itertools.permutations(range(d))) if kind in ("S", "B") else None
    if kind == "B3xZ2":  # permute/sign spatial axes 0..2, sign time axis 3
        for p in itertools.permutations(range(3)):
            for s in itertools.product((1, -1), repeat=4):
                out.append((p + (3,), s))
        return out
    for p in perms:
        for s in (itertools.product((1, -1), repeat=d) if kind == "B" else [(1,) * d]):
            out.append((p, s))
    return out


def invariant_basis(d, G):
    hc, mons = monomials(d)
    idx = {m: i for i, m in enumerate(mons)}
    vecs = set()
    for m in mons:
        acc = {}
        for g in G:
            mm, s = act(g, m, hc)
            acc[mm] = acc.get(mm, 0) + s
        acc = tuple(sorted((idx[k], v) for k, v in acc.items() if v != 0))
        if acc:
            vecs.add(acc)
    return hc, mons, idx, sorted(vecs)


def to_poly_vec(vec, n):
    v = [0] * n
    for i, c in vec:
        v[i] = c
    return v


def gauge_variation_matrix(d, hc, mons):
    """rows: monomials h_X * k^3 * xi_c ; cols: monomial basis of forms."""
    rows = {}
    entries = {}
    for col, ((I, J), (e, f)) in enumerate(mons):
        # d/dt of h_I h_J k_e k_f : (delta h_I) h_J + h_I (delta h_J)
        for (A, B) in ((I, J), (J, I)):
            a, b = hc[A]
            # delta h_ab = k_a xi_b + k_b xi_a  (a==b: 2 k_a xi_a)
            terms = [(a, b), (b, a)]
            for (x, y) in terms:
                key = (B, tuple(sorted((e, f, x))), y)
                r = rows.setdefault(key, len(rows))
                entries[(r, col)] = entries.get((r, col), 0) + 1
    return rows, entries


def exact_null(entries, nrows, ncols):
    M = sp.zeros(nrows, ncols)
    for (r, c), v in entries.items():
        M[r, c] = v
    return M


def gauge_inv_dim(d, kind):
    G = group(d, kind)
    hc, mons, idx, inv = invariant_basis(d, G)
    rows, ent = gauge_variation_matrix(d, hc, mons)
    n = len(mons)
    # V (rows x n) ; B (n x m) invariant basis ; gauge-invariant = null(V B)
    Vd = DomainMatrix([[QQ(0)] * n for _ in range(len(rows))], (len(rows), n), QQ).to_sparse()
    Vl = [[QQ(0)] * n for _ in range(len(rows))]
    for (r, c), v in ent.items():
        Vl[r][c] = QQ(v)
    Bl = [[QQ(0)] * len(inv) for _ in range(n)]
    for j, vec in enumerate(inv):
        for i, c in vec:
            Bl[i][j] = QQ(c)
    V = DomainMatrix(Vl, (len(rows), n), QQ)
    B = DomainMatrix(Bl, (n, len(inv)), QQ)
    rkB = B.rank()
    VB = V * B
    ns = VB.nullspace()
    nullB = B * ns.transpose() if ns.shape[0] else None
    return len(mons), rkB, ns.shape[0], hc, mons, idx, (nullB if nullB is not None else None)


# ---------------------------------------------------------------- eps-eps-M forms
def levi(n):
    E = {}
    for p in itertools.permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
        E[p] = -1 if inv % 2 else 1
    return E


def LM_vec(M, d, hc, idx):
    """L_M as coefficient vector in the monomial basis (h_ab symmetric, variables a<=b)."""
    E = levi(d)
    vec = {}
    rng = range(d)
    for (a, c, e, al) in E:
        s1 = E[(a, c, e, al)]
        for (b, dd, f, be) in E:
            co = s1 * E[(b, dd, f, be)] * M[al][be]
            if co == 0:
                continue
            I = hc.index(tuple(sorted((a, b))))
            J = hc.index(tuple(sorted((c, dd))))
            key = ((min(I, J), max(I, J)), tuple(sorted((e, f))))
            vec[idx[key]] = vec.get(idx[key], 0) + co
    return vec


def fierz_pauli_vec(d, hc, idx, mons):
    k = sp.symbols(f"k0:{d}")
    hv = sp.symbols(f"h0:{len(hc)}")
    H = sp.Matrix(d, d, lambda a, b: hv[hc.index(tuple(sorted((a, b))))])
    K = sp.Matrix(k)
    k2 = (K.T * K)[0]
    L = sp.expand(k2 * (H * H).trace() - 2 * (K.T * H * H * K)[0] + 2 * (K.T * H * K)[0] * H.trace()
                  - k2 * H.trace() ** 2)
    P = sp.Poly(L, *hv, *k)
    vec = {}
    for monom, co in P.terms():
        hs = [i for i in range(len(hc)) for _ in range(monom[i])]
        ks = [e for e in range(d) for _ in range(monom[len(hc) + e])]
        vec[idx[((hs[0], hs[1]), tuple(ks))]] = co
    return vec


def ray_equal(v1, v2):
    keys = set(v1) | set(v2)
    k0 = next(k for k in keys if v1.get(k, 0) != 0)
    r = sp.Rational(v2.get(k0, 0)) / sp.Rational(v1[k0])
    return all(sp.Rational(v2.get(k, 0)) == r * sp.Rational(v1.get(k, 0)) for k in keys), r


if __name__ == "__main__":
  import sys
  if "--skip-a1" not in sys.argv:
    print("== (a1) exact invariant / gauge-invariant counts (polynomial orbit sums, QQ) ==")
    for d, kind in ((4, "S"), (4, "B"), (4, "B3xZ2"), (3, "S"), (3, "B"), (4, "trivial"), (3, "trivial")):
        n, m, g, *_ = gauge_inv_dim(d, kind)
        print(f"   d={d} group={kind:8s}: ambient {n}, invariant forms {m}, gauge-invariant {g}")
  if True:

    # (a2) eps-eps-M theorem in d = 4
    print("\n== (a2) eps-eps-M forms span the full gauge-invariant space (d=4) ==")
    hc, mons = monomials(4)
    idx = {mm: i for i, mm in enumerate(mons)}
    g = 10  # from (a1), exact
    rows, ent = gauge_variation_matrix(4, hc, mons)
    basisM = []
    for i in range(4):
        for j in range(i, 4):
            M = [[0] * 4 for _ in range(4)]
            M[i][j] = M[j][i] = 1
            basisM.append(LM_vec(M, 4, hc, idx))
    Lmat = sp.zeros(len(mons), 10)
    for j, v in enumerate(basisM):
        for i, c in v.items():
            Lmat[i, j] = c
    Vd = DomainMatrix({r: {} for r in range(len(rows))}, (len(rows), len(mons)), QQ)
    Vl = [[QQ(0)] * len(mons) for _ in range(len(rows))]
    for (r, c), v in ent.items():
        Vl[r][c] = QQ(v)
    Vd = DomainMatrix(Vl, (len(rows), len(mons)), QQ)
    Ld = DomainMatrix([[QQ(int(Lmat[i, j])) for j in range(10)] for i in range(len(mons))], (len(mons), 10), QQ)
    print(f"   rank of {{L_M}} over the 10 symmetric M: {Ld.rank()};  gauge variation of all L_M zero: "
          f"{(Vd * Ld).to_Matrix().is_zero_matrix};  dim gauge-invariant space (no symmetry): {g}")
    FP = fierz_pauli_vec(4, hc, idx, mons)
    ok, r = ray_equal(LM_vec([[int(i == j) for j in range(4)] for i in range(4)], 4, hc, idx), FP)
    print(f"   L_I ray-equal to flat Fierz-Pauli/linearised EH: {ok} (ratio {r})")

    # (a3) S4: L_I, L_J span; B3xZ2: L_I, L_diag(0,0,0,1)
    for kind, Ms in (("S", ([[int(i == j) for j in range(4)] for i in range(4)], [[1] * 4 for _ in range(4)])),
                     ("B3xZ2", ([[int(i == j) for j in range(4)] for i in range(4)],
                                [[int(i == j == 3) for j in range(4)] for i in range(4)]))):
        _, _, gk, hc, mons, idx, nullB = gauge_inv_dim(4, kind)
        A = sp.Matrix(nullB.to_Matrix())
        Ls = sp.zeros(len(mons), 2)
        for j, Mx in enumerate(Ms):
            for i, c in LM_vec(Mx, 4, hc, idx).items():
                Ls[i, j] = c
        print(f"   {kind}: rank[gauge-inv basis | L_M1, L_M2] = {A.row_join(Ls).rank()} = dim {gk}: "
              f"{A.row_join(Ls).rank() == gk == Ls.rank()}")

    # (a4) characteristic determinant for random rational symmetric M (incl. S4 tilts c beyond probed range)
    print("\n== (a4) temporal-gauge characteristic polynomial of L_M (k = (n1,n2,n3, w)) ==")
    w = sp.symbols("w")
    random.seed(7)
    hv = sp.symbols("h0:10")
    Hs = sp.Matrix(4, 4, lambda a, b: hv[HC4.index(tuple(sorted((a, b))))])
    E = levi(4)

    def LM_poly(M, k):
        L = 0
        for (a, c, e, al), s1 in E.items():
            for (b, dd, f, be), s2 in E.items():
                if M[al, be] != 0:
                    L += s1 * s2 * M[al, be] * k[e] * k[f] * Hs[a, b] * Hs[c, dd]
        return sp.expand(L)

    cases = []
    for t in range(3):
        A = sp.Matrix(4, 4, lambda i, j: sp.Rational(random.randint(-4, 4), random.randint(1, 3)))
        cases.append((f"random M #{t}", (A + A.T) / 2 + sp.diag(0, 0, 0, -6)))
    I4, J4 = sp.eye(4), sp.ones(4, 4)
    for c in (sp.Rational(-1, 2), sp.Rational(3, 2), sp.Rational(5)):
        cases.append((f"S4 tilt c={c}", I4 + c * (J4 - I4)))
    sp_idx = [i for i, (a, b) in enumerate(HC4) if a != 3 and b != 3]
    for name, M in cases:
        n3 = [sp.Rational(1), sp.Rational(2), sp.Rational(-1)]
        k = n3 + [w]
        L = LM_poly(M, k)
        S = sp.Matrix(10, 10, lambda i, j: sp.diff(L, hv[i], hv[j]) / 2)
        det = sp.factor(S.extract(sp.Matrix(sp_idx), sp.Matrix(sp_idx)).det())
        Q = sp.expand((sp.Matrix(k).T * M.adjugate() * sp.Matrix(k))[0])
        rem = sp.cancel(det / Q ** 2)
        polyrem = sp.Poly(sp.numer(rem), w)
        print(f"   {name}: det(spatial block) = Q^2 * ({sp.factor(rem)}) ; Q=adj(M)(k,k); "
              f"remainder has w-degree {polyrem.degree()} and is a pure power of w: "
              f"{len(polyrem.terms()) == 1}")
