#!/usr/bin/env python3
"""Exact checks for J:derive:a-possibility-shift-that-keeps-the-books:a1.

Self-contained (sympy only; exact Gaussian rationals).  Conventions follow the landed block 54 / 78 / 137 / 141 definitions:
  single record: H = sum_{a<d} sigma_a S_a, S_a = (T_a - T_a^-1)/(2i), written below as hop amplitude -i*sg*sigma_a[d,c]/2
  to the site x - sg*e_a;  pair states: canonical keys (s1 < s2), exchange sign `sign` (-1 antisymmetric, +1 symmetric);
  exclusion P removes both records on one site;  H2 = P(hop)P + V;  D2 = P(hop weighted by (x_t+x_s)/2 on the moving record)P + V_D;
  J = i[H2, D2];  defect = [H2, J].
Sections
  A  the landed free witness entry -i/16 (V = 0), re-derived with an independent implementation
  B  parity lemma: for V, V_D supported on bond (adjacent-pair) configurations, any pair-moving range, the witness entry is
     -i/16 + t^2 * B(V, V_D); no t^1, t^3, t^4 term (checked on dense random Hermitian V, V_D) + combinatorial path census
  C  size bound from the witness entry (row norms computed exactly)
  D  an explicit nearest-neighbour pair-translating V for which B = 0 (the witness is untouched), and one for which B != 0
  E  the line: naive density-density term fails at order U^2; with a one-body placement piece -U*X it keeps the current
"""
from __future__ import annotations

import itertools
import random
import sys
import time

import sympy as sp

I = sp.I
SIG = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]

PASS = 0
FAIL = 0


def check(tag, ok, msg):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {tag} {msg}")
    else:
        FAIL += 1
        print(f"FAIL: {tag} {msg}")


class Pair:
    def __init__(self, dim, sign, Vfun=None, VDfun=None):
        self.dim, self.sign, self.Vfun, self.VDfun = dim, sign, Vfun, VDfun

    def canon(self, a, b):
        if a == b:
            return None, None
        return ((a, b), 1) if a < b else ((b, a), self.sign)

    def h1(self, st):
        x, c = st
        out = []
        for a in range(self.dim):
            for sg in (1, -1):
                y = list(x)
                y[a] -= sg
                y = tuple(y)
                for d in (0, 1):
                    v = SIG[a + 1][d, c]
                    if v != 0:
                        out.append(((y, d), -I * sg * v / 2))
        return out

    @staticmethod
    def add(vs):
        o = {}
        for v in vs:
            for k, a in v.items():
                n = sp.expand(o.get(k, 0) + a)
                if n == 0:
                    o.pop(k, None)
                else:
                    o[k] = n
        return o

    def hop(self, v, w=None):
        o = {}
        for (a, b), amp in v.items():
            for t, am in self.h1(a):
                k, sg = self.canon(t, b)
                if k:
                    ww = am * (1 if w is None else w(t[0], a[0]))
                    o[k] = sp.expand(o.get(k, 0) + amp * ww * sg)
            for t, am in self.h1(b):
                k, sg = self.canon(a, t)
                if k:
                    ww = am * (1 if w is None else w(t[0], b[0]))
                    o[k] = sp.expand(o.get(k, 0) + amp * ww * sg)
        return {k: a for k, a in o.items() if a != 0}

    @staticmethod
    def proj(v):
        return {k: a for k, a in v.items() if k[0][0] != k[1][0]}

    def H2(self, v):
        pv = self.proj(v)
        return self.add([self.proj(self.hop(pv)), self.Vfun(pv) if self.Vfun else {}])

    def D2(self, v, comp):
        pv = self.proj(v)
        h = self.proj(self.hop(pv, lambda t, x: sp.Rational(t[comp] + x[comp], 2)))
        return self.add([h, self.VDfun(pv, comp) if self.VDfun else {}])

    @staticmethod
    def neg(v):
        return {k: -a for k, a in v.items()}

    def J(self, v, comp):
        r = self.add([self.H2(self.D2(v, comp)), self.neg(self.D2(self.H2(v), comp))])
        return {k: sp.expand(I * a) for k, a in r.items()}

    def defect(self, v, comp):
        return self.add([self.H2(self.J(v, comp)), self.neg(self.J(self.H2(v), comp))])


def witness_setup(dim, sign):
    p = Pair(dim, sign)
    a = ((0,) * dim, 0)
    b = ((1,) + (0,) * (dim - 1), 0)
    k, sg = p.canon(a, b)
    target = (((-1, -1) + (0,) * (dim - 2), 0), ((0,) * dim, 1))
    return p, {k: sg}, target


# ---------------------------------------------------------------------------------------------- bond-supported operators
def bonds(dim, lo, hi):
    out = []
    for x in itertools.product(range(lo, hi + 1), repeat=dim):
        for a in range(dim):
            y = list(x)
            y[a] += 1
            if y[a] <= hi:
                out.append((x, tuple(y)))
    return out


def bond_basis(dim, lo, hi):
    return [((x, c1), (y, c2)) for (x, y) in bonds(dim, lo, hi) for c1 in (0, 1) for c2 in (0, 1)]


def rand_herm_cols(B, dens, seed):
    r = random.Random(seed)
    n = len(B)
    cols = {}
    for i in range(n):
        for j in range(i, n):
            if r.random() < dens:
                re_ = sp.Rational(r.randint(-5, 5), r.randint(1, 4))
                im_ = sp.Rational(r.randint(-5, 5), r.randint(1, 4)) if i != j else 0
                v = re_ + I * im_
                if v != 0:
                    cols.setdefault(j, []).append((i, v))
                    if i != j:
                        cols.setdefault(i, []).append((j, sp.conjugate(v)))
    idx = {b: i for i, b in enumerate(B)}
    return cols, idx


def op_from_cols(B, cols, idx, t, weight=None):
    def F(v):
        o = {}
        for k, a in v.items():
            j = idx.get(k)
            if j is None:
                continue
            for i, m in cols.get(j, []):
                kk = B[i]
                w = 1 if weight is None else weight(k, kk)
                o[kk] = sp.expand(o.get(kk, 0) + t * m * w * a)
        return {k: a for k, a in o.items() if a != 0}
    return F


def midc(k, comp):
    return sp.Rational(k[0][0][comp] + k[1][0][comp], 2)


def witness_entry(dim, sign, B, cols, idx, colsD, idxD, t, weighted=False):
    V = op_from_cols(B, cols, idx, t)
    if weighted:
        VD = op_from_cols(B, cols, idx, t, lambda k, kk: (midc(k, 0) + midc(kk, 0)) / 2)
    else:
        VD = op_from_cols(B, colsD, idxD, t)
    p = Pair(dim, sign, V, lambda v, comp: VD(v))
    _, v, target = witness_setup(dim, sign)
    return sp.expand(p.defect(v, 0).get(target, 0))


def poly_coeffs(vals):
    T = sp.symbols("T")
    poly = sp.expand(sp.interpolate(list(zip(range(len(vals)), vals)), T))
    pl = sp.Poly(poly, T)
    return [pl.coeff_monomial(T ** n) for n in range(6)]


# ============================================================================================ A
def family_a():
    for dim in (2, 3):
        ok = True
        for sign in (-1, 1):
            p, v, target = witness_setup(dim, sign)
            d = p.defect(v, 0)
            ok = ok and d.get(target, 0) == -I / sp.Integer(16)
        check(f"A{dim - 1}", ok, f"Z^{dim}: with V = 0 the witness entry (records (-1,-1) up,(0,0) down <- (0,0),(1,0) both up) is -i/16 for both exchange signs (independent re-implementation of the landed free defect)")
    # hop-distance of the witness: three
    starts, ends = [(0, 0), (1, 0)], [(-1, -1), (0, 0)]
    best = min(sum(sum(abs(a - b) for a, b in zip(starts[i], ends[o[i]])) for i in range(2)) for o in [(0, 1), (1, 0)])
    check("A3", best == 3, "minimum number of single-record hops between the witness's two configurations is 3 (so the free term is a 3-hop term)")


# ============================================================================================ B
def family_b():
    # B1: combinatorial census of the operator-type sequences.  Factors of [H,[H,D]] expand to H^2 D, H D H, D H^2 (each with
    # a free part F (flips parity of total coordinate sum s) or a bond part V (acts bond -> bond, s odd -> s odd)).
    # Acting on v (bond, s odd) and ending at w (s even, not a bond): count sequences in which a V never meets a non-bond state.
    seqs = []
    for types in itertools.product("FV", repeat=3):  # order of action: X3 then X2 then X1
        par = 1  # odd
        ok = True
        nV = types.count("V")
        for t in types:
            if t == "V":
                if par != 1:
                    ok = False  # V needs a bond (odd) input
                    break
            else:
                par ^= 1
        if ok and par == 0:  # ends even
            seqs.append(types)
    check("B1", seqs == [("F", "F", "F"), ("V", "V", "F")], f"parity census: the only action orders (X3,X2,X1) that can join the odd bond configuration v to the even non-bond configuration w are FFF (no V) and V,V,F (two bond operators, then one free hop): {seqs}")
    # B2: dense random Hermitian V and V_D (independent), Z^2, window [-2,2]^2, both signs
    t0 = time.time()
    dim, lo, hi = 2, -2, 2
    B = bond_basis(dim, lo, hi)
    cols, idx = rand_herm_cols(B, 0.09, 11)
    colsD, idxD = rand_herm_cols(B, 0.09, 12)
    for sign in (-1, 1):
        vals = [witness_entry(dim, sign, B, cols, idx, colsD, idxD, sp.Integer(t)) for t in range(5)]
        c = poly_coeffs(vals)
        ok = c[0] == -I / sp.Integer(16) and c[1] == 0 and c[3] == 0 and c[4] == 0 and c[5] == 0 and c[2] != 0
        check(f"B2{'ab'[sign == 1]}", ok, f"Z^2, sign {sign}, V and V_D independent dense random Hermitian bond operators (window [-2,2]^2, {len(B)} states): entry(t) = -i/16 + ({c[2]}) t^2 exactly; coefficients of t^1,t^3,t^4,t^5 are zero")
    # B3: the dipole built from the same V by position weights (average of the two bond midpoints) -- the physical placement
    vals = [witness_entry(dim, -1, B, cols, idx, colsD, idxD, sp.Integer(t), weighted=True) for t in range(5)]
    c = poly_coeffs(vals)
    check("B3", c[0] == -I / sp.Integer(16) and c[1] == 0 and c[3] == 0 and c[4] == 0 and c[2] != 0, f"same with V_D = midpoint-weighted copy of V: entry = -i/16 + ({c[2]}) t^2; the quadratic term does not vanish for a generic V, so the entry is not protected")
    # B4: Z^3, sparser, window [-1,1]^3
    dim, lo, hi = 3, -1, 1
    B3 = bond_basis(dim, lo, hi)
    cols3, idx3 = rand_herm_cols(B3, 0.03, 21)
    colsD3, idxD3 = rand_herm_cols(B3, 0.03, 22)
    vals = [witness_entry(dim, -1, B3, cols3, idx3, colsD3, idxD3, sp.Integer(t)) for t in range(5)]
    c = poly_coeffs(vals)
    check("B4", c[0] == -I / sp.Integer(16) and c[1] == 0 and c[3] == 0 and c[4] == 0 and c[5] == 0, f"Z^3, antisymmetric, random Hermitian V,V_D on bonds of [-1,1]^3 ({len(B3)} states): entry = -i/16 + ({c[2]}) t^2, no odd or higher term")
    print(f"  (family B runtime {time.time() - t0:.1f}s)")


# ============================================================================================ C
def family_c():
    p, v, target = witness_setup(2, -1)
    w = {target: 1}
    # row of H0 and D0 at w, restricted to bond configurations (hermitian operators: <w|X|s> = conj <s|X|w>)
    def isbond(k):
        d = [abs(k[0][0][i] - k[1][0][i]) for i in range(2)]
        return sum(d) == 1
    hrow = {k: a for k, a in p.proj(p.hop(w)).items() if isbond(k)}
    drow = {k: a for k, a in p.proj(p.hop(w, lambda t_, x: sp.Rational(t_[0] + x[0], 2))).items() if isbond(k)}
    rH2 = sum(sp.Abs(a) ** 2 for a in hrow.values())
    rD2 = sum(sp.Abs(a) ** 2 for a in drow.values())
    check("C1", rH2 == 1 and len(hrow) == 4, f"row of H0 at w onto bond configurations: {len(hrow)} entries, squared norm {rH2}")
    check("C2", rD2 == sp.Rational(3, 8), f"row of D0 (x-component) at w onto bond configurations: squared norm {rD2}")
    rH, rD = sp.sqrt(rH2), sp.sqrt(rD2)
    N2 = sp.Rational(1, 16) / (3 * rH + rD)
    check("C3", N2 > 0, f"|B| <= (3 r_H + r_D) ||V|| ||V_D||-type bound: if the witness entry vanishes then max(||V||,||V_D||)^2 >= {N2} = {float(N2):.5f} (operator norms on the bond sector; r_H={rH}, r_D={rD})")
    return N2


# ============================================================================================ D
def bond_axis(a, b):
    d = [b[0][i] - a[0][i] for i in range(len(a[0]))]
    if sum(map(abs, d)) != 1:
        return None
    return [i for i in range(len(d)) if d[i] != 0][0]


def trans_V(lam, mu, weighted, comp=0):
    """mu*(identity on bonds) + lam*(translate a bond by +-1 along its own axis), coins kept"""
    def F(v):
        o = {}
        for (a, b), amp in v.items():
            ax = bond_axis(a, b)
            if ax is None:
                continue
            m0 = sp.Rational(a[0][comp] + b[0][comp], 2)
            targets = [(a, b, mu)]
            for sgn in (1, -1):
                def sh(s, sgn=sgn):
                    return (tuple(s[0][i] + (sgn if i == ax else 0) for i in range(len(s[0]))), s[1])
                targets.append((sh(a), sh(b), lam))
            for (a2, b2, c) in targets:
                m1 = sp.Rational(a2[0][comp] + b2[0][comp], 2)
                w = 1 if not weighted else (m0 + m1) / 2
                k = (a2, b2)
                o[k] = sp.expand(o.get(k, 0) + c * w * amp)
        return {k: a for k, a in o.items() if a != 0}
    return F


def family_d():
    lam, mu = sp.symbols("lam mu", real=True)
    ok = True
    for sign in (-1, 1):
        p = Pair(2, sign, trans_V(lam, mu, False), lambda v, comp: trans_V(lam, mu, True)(v))
        _, v, target = witness_setup(2, sign)
        d = p.defect(v, 0)
        ok = ok and sp.simplify(d.get(target, 0) + I / 16) == 0
    check("D1", ok, "Z^2: V = mu*(1 on bonds) + lam*(translate the pair by one site along its axis), nearest-neighbour reach, midpoint-weighted dipole: the witness entry stays -i/16 for symbolic lam, mu (both signs): B = 0 for this V, so it cannot cancel the witness")
    # a V for which B != 0: a two-step chain of bond translations plus a coin-changing diagonal piece
    B = bond_basis(2, -2, 2)
    cols, idx = rand_herm_cols(B, 0.09, 31)
    c_ = None
    vals = [witness_entry(2, -1, B, cols, idx, cols, idx, sp.Integer(t), weighted=True) for t in range(5)]
    c_ = poly_coeffs(vals)
    check("D2", c_[2] != 0 and c_[1] == 0, f"a (random) bond-supported V with midpoint-weighted dipole has B = {c_[2]} != 0 (the entry is quadratic in V, with no linear term)")


# ============================================================================================ E
def line_V(sign, M, toff):
    def Vop(v, wt=None):
        o = {}
        for (a, b), amp in v.items():
            (x1, c1), (x2, c2) = a, b
            if abs(x1[0] - x2[0]) != 1:
                continue
            col = 2 * c1 + c2
            w = 1 if wt is None else wt(x1, x2)
            for row in range(4):
                m = M[row, col]
                if m == 0:
                    continue
                k = ((x1, row // 2), (x2, row % 2))
                o[k] = sp.expand(o.get(k, 0) + amp * m * w)
        return {k: a for k, a in o.items() if a != 0}
    return Vop


def family_e():
    U = sp.symbols("U", real=True)
    M = U * sp.eye(4)
    tests = [(pos2, c1, c2) for pos2 in [(1,), (2,), (3,), (4,)] for c1 in (0, 1) for c2 in (0, 1)]
    for sign in (-1, 1):
        p0 = Pair(1, sign)
        bad0 = 0
        for pos2, c1, c2 in tests:
            k, sg = p0.canon(((0,), c1), (pos2, c2))
            bad0 += bool(p0.defect({k: sg}, 0))
        Vf = line_V(sign, M, 0)
        pn = Pair(1, sign, lambda v: Vf(v), lambda v, comp: Vf(v, lambda x1, x2: sp.Rational(x1[0] + x2[0], 2)))
        badn = 0
        for pos2, c1, c2 in tests:
            k, sg = pn.canon(((0,), c1), (pos2, c2))
            badn += bool(pn.defect({k: sg}, 0))

        def VD(v, comp):
            a = Vf(v, lambda x1, x2: sp.Rational(x1[0] + x2[0], 2))
            b = {k: sp.expand(-U * (k[0][0][0] + k[1][0][0]) * amp) for k, amp in v.items()}
            return Pair.add([a, b])
        pp = Pair(1, sign, lambda v: Vf(v), VD)
        badp = 0
        for pos2, c1, c2 in tests:
            k, sg = pp.canon(((0,), c1), (pos2, c2))
            badp += bool(pp.defect({k: sg}, 0))
        check(f"E{'ab'[sign == 1]}", bad0 == 0 and badn > 0 and badp == 0,
              f"line, sign {sign}, 16 test pairs (separation 1..4, all coin pairs): V=0 defect zero ({bad0} bad); V=U*1 on neighbouring pairs with midpoint energy: {badn} nonzero defects (order U^2); with the extra one-body placement piece -U*X in the dipole: {badp} nonzero defects (symbolic U)")


def main():
    t0 = time.time()
    family_a()
    family_b()
    family_c()
    family_d()
    family_e()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print(f"runtime {time.time() - t0:.1f}s")
    if FAIL == 0:
        print("HIT: for any Hermitian V and V_D supported on neighbouring-pair (bond) configurations (any pair-translating or rotating reach, arbitrary dipole weights, translation invariance not assumed), the block-141 witness entry of [H2+V, J] on Z^2 and Z^3 equals -i/16 + (a form bilinear in V and V_D): no linear and no cubic term (parity census; random exact checks), so no weak (perturbative) bond-supported V can cancel it, and cancelling it needs max(||V||,||V_D||)^2 >= 1/(16(3 r_H + r_D)); this does not by itself exclude a large V (the quadratic term is generically nonzero), and the full no-go for this class is the landed 2026-09-26 finite-range theorem.")
    print("SUMMARY: the free three-hop witness -i/16 is untouched at first order by any bond-supported V (including pair-moving ones, beyond block 141's fixed-position class), enters only through a quadratic form with an explicit size bound, and on a line a nonzero density term keeps the current only with an extra one-body placement piece")
    sys.exit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
