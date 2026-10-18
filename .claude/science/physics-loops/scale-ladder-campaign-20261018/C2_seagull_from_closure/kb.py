"""B21 check core: Poisson brackets computed directly on Fourier kernels (written fresh for this check).

Different path from B21 (position-space jets + Euler operator) and B19_check (sympy Functions + euler_equations):
here a local functional  F = int prod_s (d^{alpha_s} phi_s)(x)  is stored ONLY as its Fourier kernel
    K(q_0..q_{n-1}) = c * prod_s prod_j (i q_s^j)^{alpha_s^j}   on the surface sum_s q_s = 0,
canonicalised (slots sorted by field name, symmetrised over identical fields, last momentum eliminated).
The functional derivative wrt slot a is the kernel with q_a -> -(sum of the other momenta); the bracket
    {F,G} = sum_c dF/dh_c dG/dP_c - dF/dP_c dG/dh_c
is the product of the two contracted kernels with all remaining slots concatenated.  No Euler operator is used.

Canonical pairs (h_ab, P_ab), a <= b; tensor momentum Pt^ij = P_ii (i = j), P_ab / 2 (i != j); matter (phi, pi).
"""
from __future__ import annotations
import itertools
from collections import defaultdict
import sympy as sp

I = sp.I
NQ = 24
Q = [[sp.Symbol(f"q{s}_{j}") for j in range(3)] for s in range(NQ)]
QALL = [x for row in Q for x in row]

# ------------------------------------------------------------------ jets (only to WRITE densities; never differentiated variationally)
_J, _K = {}, {}


def jet(f, al=(0, 0, 0)):
    key = (f, tuple(al))
    s = _J.get(key)
    if s is None:
        s = sp.Symbol(f"{f}|{al[0]}{al[1]}{al[2]}")
        _J[key] = s
        _K[s] = key
    return s


def Dk(e, k):
    e = sp.expand(e)
    out = 0
    for s in e.free_symbols:
        if s in _K:
            f, a = _K[s]
            b = list(a)
            b[k] += 1
            out += sp.diff(e, s) * jet(f, b)
    return sp.expand(out)


COMP = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
HNAME = {ab: f"h{ab[0]}{ab[1]}" for ab in COMP}
PNAME = {ab: f"P{ab[0]}{ab[1]}" for ab in COMP}
DYN = {}
for ab in COMP:
    DYN[HNAME[ab]] = (PNAME[ab], 1)
    DYN[PNAME[ab]] = (HNAME[ab], -1)
DYN["phi"] = ("pi", 1)
DYN["pi"] = ("phi", -1)


def h(i, j):
    return jet(HNAME[(min(i, j), max(i, j))])


def Pt(i, j):
    s = jet(PNAME[(min(i, j), max(i, j))])
    return s if i == j else s / 2


def ftype(f):
    if f[0] == "h":
        return "h"
    if f[0] == "P":
        return "P"
    return f.rstrip("012") if f[0] in "xy" else f


# ------------------------------------------------------------------ kernels
def _finish(key, raw):
    """symmetrise over identical-field slots, then eliminate the last momentum."""
    n = len(key)
    blocks = [list(g) for _, g in itertools.groupby(range(n), key=lambda t: key[t])]
    blocks = [b for b in blocks if len(b) > 1]
    ker = raw
    if blocks:
        tot, cnt = 0, 0
        for combo in itertools.product(*[list(itertools.permutations(b)) for b in blocks]):
            sub = {}
            for b, p in zip(blocks, combo):
                for src, dst in zip(b, p):
                    for j in range(3):
                        sub[Q[src][j]] = Q[dst][j]
            tot += ker.xreplace(sub)
            cnt += 1
        ker = tot / cnt
    ker = ker.xreplace({Q[n - 1][j]: -sum((Q[t][j] for t in range(n - 1)), sp.Integer(0)) for j in range(3)})
    return sp.expand(ker)


def _bucket_add(B, fields, moms, ker):
    order = sorted(range(len(fields)), key=lambda i: fields[i])
    key = tuple(fields[i] for i in order)
    sub = {}
    for t, i in enumerate(order):
        for j in range(3):
            sub[moms[i][j]] = Q[t][j]
    B[key] += ker.xreplace(sub)


def _close(B):
    out = {}
    for key, raw in B.items():
        k = _finish(key, sp.expand(raw))
        if k != 0:
            out[key] = k
    return out


def functional(dens, keep=None):
    B = defaultdict(lambda: sp.Integer(0))
    for term in sp.Add.make_args(sp.expand(dens)):
        c = sp.Integer(1)
        facs = []
        for b, e in term.as_powers_dict().items():
            if b in _K:
                facs += [_K[b]] * int(e)
            else:
                c *= b ** e
        if not facs:
            continue
        fields = [f for f, a in facs]
        if keep is not None and not keep(fields):
            continue
        ker = c * sp.Mul(*[(I * Q[s][j]) ** a[j] for s, (f, a) in enumerate(facs) for j in range(3)])
        _bucket_add(B, fields, [Q[s] for s in range(len(facs))], ker)
    return _close(B)


def fadd(*Fs, coeffs=None):
    out = defaultdict(lambda: sp.Integer(0))
    for n, F in enumerate(Fs):
        c = 1 if coeffs is None else coeffs[n]
        for k, v in F.items():
            out[k] += c * v
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def pb(F, G, keep=None):
    """kernel of {F, G}; keep(fields) filters the result pattern BEFORE contraction is done."""
    B = defaultdict(lambda: sp.Integer(0))
    for fk, fK in F.items():
        n = len(fk)
        for gk, gK in G.items():
            m = len(gk)
            gsh = None
            for a, fa in enumerate(fk):
                if fa not in DYN:
                    continue
                conj, sgn = DYN[fa]
                for b, gb in enumerate(gk):
                    if gb != conj:
                        continue
                    fields = [fk[i] for i in range(n) if i != a] + [gk[j] for j in range(m) if j != b]
                    if keep is not None and not keep(fields):
                        continue
                    if gsh is None:
                        gsh = gK.xreplace({Q[j][c]: Q[n + j][c] for j in range(m) for c in range(3)})
                    kf = fK.xreplace({Q[a][c]: -sum((Q[i][c] for i in range(n) if i != a), sp.Integer(0)) for c in range(3)})
                    kg = gsh.xreplace({Q[n + b][c]: -sum((Q[n + j][c] for j in range(m) if j != b), sp.Integer(0))
                                       for c in range(3)})
                    moms = [Q[i] for i in range(n) if i != a] + [Q[n + j] for j in range(m) if j != b]
                    _bucket_add(B, fields, moms, sgn * kf * kg)
    return _close(B)


def restrict(F, keep):
    return {k: v for k, v in F.items() if keep(list(k))}


def eqs_of(F, keep=None):
    """real coefficient equations for F == 0 (each momentum monomial of degree d carries i^d)."""
    out = []
    for key, ker in F.items():
        if keep is not None and not keep(list(key)):
            continue
        qs = [x for x in QALL if ker.has(x)]
        if not qs:
            c = sp.expand(ker)
            if c != 0:
                out.append(c)
            continue
        for mon, c in sp.Poly(ker, *qs).terms():
            c = sp.expand(c / I ** sum(mon))
            if c != 0:
                out.append(c)
    return out


def pattern(**cnt):
    """keep-function: exact counts per field type, e.g. pattern(h=1, P=1, N=1, M=1)."""
    def f(fields):
        c = defaultdict(int)
        for x in fields:
            c[ftype(x)] += 1
        return dict(c) == {k: v for k, v in cnt.items() if v}
    return f


def ptype_le(**mx):
    """keep-function: counts per type <= given maxima (types not listed: unrestricted)."""
    def f(fields):
        c = defaultdict(int)
        for x in fields:
            c[ftype(x)] += 1
        return all(c[k] <= v for k, v in mx.items())
    return f


# ------------------------------------------------------------------ geometry, written fresh: exact density [sqrt g R]^(1),(2), g = delta + e h
def sqrtgR_12():
    e = sp.Symbol("eps_")
    H = sp.Matrix(3, 3, lambda i, j: h(i, j))
    g = sp.eye(3) + e * H
    gi = sp.eye(3) - e * H + e ** 2 * H * H
    trh = H.trace()
    sg = 1 + e * trh / 2 + e ** 2 * (trh ** 2 / 8 - (H * H).trace() / 4)

    def tr2(x):
        x = sp.expand(x)
        return sum(x.coeff(e, p) * e ** p for p in range(3))
    dg = lambda i, j, k: Dk(g[i, j], k)
    # Christoffel of the first kind, then raise
    G1k = [[[(dg(l, i, j) + dg(l, j, i) - dg(i, j, l)) / 2 for j in range(3)] for i in range(3)] for l in range(3)]
    Gam = [[[tr2(sum(gi[k, l] * G1k[l][i][j] for l in range(3))) for j in range(3)] for i in range(3)] for k in range(3)]
    R = 0
    for i in range(3):
        for j in range(3):
            Rij = sum(Dk(Gam[k][i][j], k) - Dk(Gam[k][i][k], j) for k in range(3))
            Rij += sum(Gam[k][k][l] * Gam[l][i][j] - Gam[k][j][l] * Gam[l][i][k] for k in range(3) for l in range(3))
            R += gi[i, j] * tr2(Rij)
    out = tr2(sg * tr2(R))
    return sp.expand(out.coeff(e, 1)), sp.expand(out.coeff(e, 2))
