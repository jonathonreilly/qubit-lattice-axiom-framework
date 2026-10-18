#!/usr/bin/env python3
"""Curvature-member closure with the walker as matter: alpha = K2/4 and one curvature coefficient in the walker's
frame normalisation.

Companion runner of
docs/CURVATURE_MEMBER_CLOSURE_WITH_THE_WALKER_AS_MATTER_FORCES_ALPHA_EQUALS_K2_OVER_FOUR_AND_ONE_CURVATURE_COEFFICIENT_IN_THE_WALKERS_FRAME_NORMALISATION_BOUNDED_THEOREM_NOTE_2026-10-18.md

Self-contained (Python 3 + sympy; numpy for one floating-point cross-check).  Consolidated from the scale-ladder campaign
scripts of blocks B21, C4 and C4b and their fresh-context checks (same model family), with the code reused as written:
  engine K  the B21 check's Fourier-kernel Poisson-bracket engine (kb.py) with C4b's spinor half-density extension
            (c4b_core.py): local functionals stored as Fourier kernels, brackets by kernel contraction, no Euler operator.
  engine V  the C4b check's position-space engine (vc_core.py): sympy-Function densities, brackets from Euler-Lagrange
            derivatives, divergence tests by the Euler operator in the lapse.
Continuum, flat background, the orders stated per check; every gating check is exact (sympy over Q or symbolic), except
C.c4chk.A2 (floating-point torus build, atol 1e-9), which is a cross-check of the symbols used in C.c4chk.A1.

Parts (each tag carries its source: b21chk = B21 check, c4 = C4 runner, c4chk = C4 check, c4b = C4b runner,
c4bchk = C4b check, c4bop = C4b operator route)
  A  Result 1  canonical rescaling Phi_rho, invariants, the invariant TT cone K2/(4 alpha), the premises equivalent to
               K1 = K2, witnesses r = 2, 1, 1/3 and the negative control                                  (b21chk)
  B  Results 1-2  the walker's coupling strength a_s = 1 in block-62 variables (frame identification g^-1 = E^T E,
               block 120's normalisation, two-step placement at all eight species), the lapse identity
               e'' = -(K1 a_s/(4 alpha)) p.Theta.p, the TT cone, Phi_rho invariants, the static ratio gamma     (c4)
  C  Results 1-2  second routes for B                                                                    (c4chk)
  D  Results 3-4  closure with the walker, kernel route: a_s lam1 = lam_f, lam_f = nu, K2 = a_s K1, the cone,
               the forced connection terms, the triad route, the walker's rotation defect and the axial 1/4  (c4b)
  E  Result 3  headline K2 = a_s K1 (gamma = 1) by the position-space route; operator identities  (c4bchk, c4bop)
  F  Result 4  the walker against the Levi-Civita covariant Weyl operator; c_ax = 1/4                       (c4bchk)
  Z  audit     every sympy.solve(..., dict=True) solution is back-substituted into ALL its equations

Usage
  python3 scripts/curvature_member_closure_with_the_walker_forces_alpha_k2_over_four_2026_10_18.py          (default)
  ... --full      adds the slow checks: A.b21chk.T3G (648-coefficient G2), B.c4.B3 and B.c4.C1-C2 (plane-wave
                  sqrt(g)R), D.c4b.A1a (fully general null space) and D.c4b.F1-F2 (next order), E.c4bchk.H1 (density
                  weight), F.c4bchk.G3a-c (second-order covariant operator), F.c4bchk.C1'-C2', F2'/F1', F1'' (constructed
                  G_f^(1); next order with and without the axial term)
  ... --parts A,D runs only the listed parts (the audit always runs)
"""
from __future__ import annotations

import argparse
import itertools
import random
import sys
import time
import traceback
from collections import defaultdict
from types import SimpleNamespace

import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix

T_START = time.time()
RESULTS = []


def _checker(prefix):
    def check(tag, ok, msg):
        ok = bool(ok)
        RESULTS.append((prefix + str(tag), ok))
        print(f"[{'PASS' if ok else 'FAIL'}] {prefix}{tag} [{time.time() - T_START:.0f}s]: {msg}", flush=True)
    return check


# ---------------------------------------------------------------------------------------------------------------------
# Solve audit: sympy.solve silently drops equations that involve only parameters (found by the C4b check), so a
# solution is kept only if it annuls every equation it was solved from.  Rejections are recorded and fail part Z.
_ORIG_SOLVE = sp.solve
AUDIT = {"calls": 0, "solutions": 0, "rejected": []}


def _vanishes(e, s_):
    r = sp.expand(sp.sympify(e).xreplace(s_))
    if r == 0:
        return True
    r = sp.cancel(sp.together(r))
    if r == 0:
        return True
    return sp.simplify(r) == 0


def _audited_solve(eqs, *args, **kw):
    out = _ORIG_SOLVE(eqs, *args, **kw)
    el = list(eqs) if isinstance(eqs, (list, tuple, set)) else [eqs]
    el = [e.lhs - e.rhs if isinstance(e, sp.Equality) else e for e in el]
    if isinstance(out, list) and out and not isinstance(out[0], dict):
        if len(args) == 1 and isinstance(args[0], sp.Symbol):
            sols = [{args[0]: v} for v in out]
        else:
            return out
    elif isinstance(out, list):
        sols = out
    else:
        return out
    AUDIT["calls"] += 1
    good = []
    for s_ in sols:
        AUDIT["solutions"] += 1
        if all(_vanishes(e, s_) for e in el):
            good.append(s_)
        else:
            AUDIT["rejected"].append(s_)
            print(f"   [audit] rejected a solution that does not annul all its equations: {s_}", flush=True)
    if out and not isinstance(out[0], dict):
        return [list(g.values())[0] for g in good]
    return good


sp.solve = _audited_solve


# =====================================================================================================================
# Engine K: Fourier-kernel bracket engine (campaign B21 check kb.py) with the spinor extension (campaign C4b c4b_core.py)
# =====================================================================================================================
_KE = {}


def _kernel_engine():
    if 'ns' in _KE:
        return _KE['ns']

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


    # ---- spinor extension (campaign C4b c4b_core.py)

    I = sp.I
    for _a in range(2):
        DYN[f"c{_a}"] = (f"d{_a}", -I)
        DYN[f"d{_a}"] = (f"c{_a}", I)

    R3 = range(3)
    CH = [jet("c0"), jet("c1")]
    CB = [jet("d0"), jet("d1")]
    SIG = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    XI = [jet(f"x{k}") for k in R3]
    ETA = [jet(f"y{k}") for k in R3]
    N, M = jet("N"), jet("M")
    TH = [jet(f"t{k}") for k in R3]          # rotation-angle field (antisymmetric frame part), external
    EPS = lambda i, j, k: sp.LeviCivita(i, j, k)


    def S(mu, A=None):
        m = SIG[mu] if A is None else A
        return sp.expand(sum(CB[a] * m[a, b] * CH[b] for a in range(2) for b in range(2)))


    def J(j, mu, A=None):
        m = SIG[mu] if A is None else A
        return sp.expand(I / 2 * sum(m[a, b] * (CB[a] * Dk(CH[b], j) - Dk(CB[a], j) * CH[b]) for a in range(2) for b in range(2)))


    Sv = [S(mu) for mu in range(4)]
    Jv = [[J(j, mu) for mu in range(4)] for j in R3]


    def walker(Lp, E, v=1):
        """-v int Lp E_aj J_{j,a}; E is a 3x3 matrix of expressions E[a, j] = E_a^j."""
        return sp.expand(-v * Lp * sum(E[a, j] * Jv[j][a + 1] for a in R3 for j in R3))


    def Hmat():
        return sp.Matrix(3, 3, lambda i, j: h(i, j))


    def frame_sym(a=1, order=2):
        """symmetric section E = (delta + a h)^(-1/2) to the stated order in h."""
        H = Hmat()
        E = sp.eye(3) - a * H / 2
        if order >= 2:
            E += sp.Rational(3, 8) * a ** 2 * H * H
        return E.applyfunc(sp.expand)


    def kosmann(xi, lam=1, spin=sp.Rational(-1, 4)):
        """lam int chibar i(xi.d + div xi/2 + (i/4) curl xi . sigma) chi  =  lam int (xi_k J_{k,0} - 1/4 curl xi . s)."""
        curl = [sum(EPS(c, k, j) * Dk(xi[j], k) for k in R3 for j in R3) for c in R3]
        return sp.expand(lam * (sum(xi[k] * Jv[k][0] for k in R3) + spin * sum(curl[c] * Sv[c + 1] for c in R3)))


    # ------------------------------------------------------------------ gravity (re-written from chk_b21 definitions)
    def G1d(xi):
        return sp.expand(sum(Pt(i, j) * (Dk(xi[j], i) + Dk(xi[i], j)) for i in R3 for j in R3))


    def Lie_h(xi, i, j):
        return sum(xi[k] * Dk(h(i, j), k) + h(k, j) * Dk(xi[k], i) + h(i, k) * Dk(xi[k], j) for k in R3)


    def G2Lie(xi):
        return sp.expand(sum(Pt(i, j) * Lie_h(xi, i, j) for i in R3 for j in R3))


    trP = sum(Pt(k, k) for k in R3)
    trPP = sp.expand(sum(Pt(i, j) * Pt(j, i) for i in R3 for j in R3))
    trh = sum(h(k, k) for k in R3)


    def kin0(al, b):
        return sp.expand((trPP + b * trP ** 2) / (4 * al))


    def lb(a, b_):
        return [sp.expand(sum(a[k] * Dk(b_[i], k) - b_[k] * Dk(a[i], k) for k in R3)) for i in R3]


    def lapse(xi, S1, S2, L_=None):
        L_ = N if L_ is None else L_
        return sp.expand(S1 * sum(xi[i] * Dk(L_, i) for i in R3) + S2 * L_ * sum(Dk(xi[i], i) for i in R3))


    z0 = [sp.expand(N * Dk(M, i) - M * Dk(N, i)) for i in R3]


    # ------------------------------------------------------------------ field counting / filters
    def ftyp(f):
        if f[0] == "h":
            return "h"
        if f[0] == "P":
            return "P"
        if f[0] == "c" or f[0] == "d":
            return "f"
        if f[0] == "x":
            return "x"
        if f[0] == "y":
            return "y"
        if f[0] == "t":
            return "t"
        return f


    def pat(**cnt):
        want = {k: v for k, v in cnt.items() if v}

        def k(fields):
            c = defaultdict(int)
            for x in fields:
                c[ftyp(x)] += 1
            return dict(c) == want
        return k


    def any_of(*ks):
        return lambda f: any(k(f) for k in ks)


    # ------------------------------------------------------------------ equations
    def eqs_ri(F, keep=None):
        out = []
        for e in eqs_of(F, keep):
            e = sp.expand(e)
            re, im = sp.expand(sp.re(e)), sp.expand(sp.im(e))
            if re != 0:
                out.append(re)
            if im != 0:
                out.append(im)
        return out


    def solve_lin(eqs, unk):
        """exact linear solve over QQ via DomainMatrix: returns (rank, consistent, nullity, particular/unique solution or None,
        rref matrix).  Coefficients must be rational numbers."""
        A, rhs = sp.linear_eq_to_matrix(eqs, unk)
        Ad = DomainMatrix.from_Matrix(A).convert_to(sp.QQ)
        Aug = DomainMatrix.from_Matrix(A.row_join(rhs)).convert_to(sp.QQ)
        rk, rka = Ad.rank(), Aug.rank()
        return rk, rk == rka, len(unk) - rk, A, rhs


    def is_zero(F):
        return eqs_ri(F) == []




    # ------------------------------------------------------------------ isotropic (SO(3)) contraction ansatz generator
    def _matchings(lst):
        if not lst:
            yield []
            return
        a = lst[0]
        for i in range(1, len(lst)):
            rest = lst[1:i] + lst[i + 1:]
            for p in _matchings(rest):
                yield [(a, lst[i])] + p


    def iso_candidates(factors):
        """factors: list of (fn(idx_tuple) -> expr, nslots).  Returns all SO(3)-invariant full contractions (delta pairings,
        plus one epsilon when the index count is odd), summed over index values."""
        n = sum(ns for _, ns in factors)
        slots = list(range(n))
        cands = []
        if n % 2 == 0:
            structs = [(None, m) for m in _matchings(slots)]
        else:
            structs = []
            for tri in itertools.combinations(slots, 3):
                rest = [s for s in slots if s not in tri]
                for m in _matchings(rest):
                    structs.append((tri, m))
        for tri, m in structs:
            tot = 0
            free = [s for s in slots if tri is None or s not in tri]
            for vals_e in (itertools.product(R3, repeat=3) if tri is not None else [()]):
                if tri is not None and sp.LeviCivita(*vals_e) == 0:
                    continue
                eps = sp.LeviCivita(*vals_e) if tri is not None else 1
                for vals_d in itertools.product(R3, repeat=len(m)):
                    v_ = [None] * n
                    if tri is not None:
                        for s_, x in zip(tri, vals_e):
                            v_[s_] = x
                    for (p, q), x in zip(m, vals_d):
                        v_[p] = v_[q] = x
                    term = eps
                    pos = 0
                    for fn, ns in factors:
                        term *= fn(tuple(v_[pos:pos + ns]))
                        pos += ns
                    tot += term
            cands.append(sp.expand(tot))
        return cands


    def _rowvec(F):
        row = {}
        for key, ker in F.items():
            qs = [x for x in QALL if ker.has(x)]
            if not qs:
                row[(key, ())] = sp.expand(ker)
                continue
            for mon, cc in sp.Poly(ker, *qs).terms():
                row[(key, tuple(zip([str(x) for x in qs], mon)))] = cc
        return row


    def independent(cands):
        """indices of a maximal linearly independent subset of the candidate densities, as local functionals (kernels)."""
        rows = [_rowvec(functional(c)) for c in cands]
        cols = {}
        for r in rows:
            for k in r:
                cols.setdefault(k, len(cols))
        Mx = sp.zeros(2 * len(cols), len(rows))
        for j, r in enumerate(rows):
            for k, cc in r.items():
                re, im = sp.re(cc), sp.im(cc)
                Mx[2 * cols[k], j] = re
                Mx[2 * cols[k] + 1, j] = im
        if len(rows) == 0:
            return []
        Dm = DomainMatrix.from_Matrix(Mx).convert_to(sp.QQ)
        _, piv = Dm.rref()
        return list(piv)


    def Tax(E, order):
        """axial scalar T(E) = eps_abc E_a^j E_b^k d_j e_ck (e = (E^-1)^T the co-frame), with E^-1 expanded to `order`
        in (E - 1).  Only the parts of the result up to that order in the frame deviation are meaningful."""
        X = E - sp.eye(3)
        Ei, term = sp.eye(3), sp.eye(3)
        for _ in range(order):
            term = (-term * X).applyfunc(sp.expand)
            Ei += term
        e_ = Ei.T
        T = 0
        for a in R3:
            for b_ in R3:
                for c in R3:
                    if EPS(a, b_, c) == 0:
                        continue
                    for j in R3:
                        for k in R3:
                            T += EPS(a, b_, c) * E[a, j] * E[b_, k] * Dk(e_[c, k], j)
        return sp.expand(T)


    def walker_cov(Lp, E, order, v=1):
        """the walker plus the axial (totally antisymmetric) spin-connection term 1/4 N T(E) n: the locally rotation
        covariant half-density Weyl operator (coefficient 1/4 fixed by C4b section G)."""
        return sp.expand(walker(Lp, E, v) + v * sp.Rational(1, 4) * Lp * Tax(E, order) * Sv[0])

    _KE['ns'] = SimpleNamespace(**locals())
    return _KE['ns']


# =====================================================================================================================
# Engine V: position-space Euler-operator engine (campaign C4b check vc_core.py)
# =====================================================================================================================
_VE = {}


def _position_engine():
    if 'ns' in _VE:
        return _VE['ns']

    X = sp.symbols("x0:3", real=True)
    R3 = range(3)
    I = sp.I
    F_ = lambda name: sp.Function(name)(*X)


    def hf(i, j):
        return F_(f"h{min(i, j)}{max(i, j)}")


    def Pf(i, j):
        return F_(f"P{min(i, j)}{max(i, j)}")


    Hm = sp.Matrix(3, 3, lambda i, j: hf(i, j))
    Pm = sp.Matrix(3, 3, lambda i, j: Pf(i, j))
    HCOMP = [(i, j) for i in R3 for j in R3 if i <= j]
    c = [F_("c0"), F_("c1")]
    d = [F_("d0"), F_("d1")]
    N, M = F_("N"), F_("M")
    xi = [F_(f"xi{k}") for k in R3]
    eta = [F_(f"eta{k}") for k in R3]
    th = [F_(f"th{k}") for k in R3]
    SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    ONE2 = sp.eye(2)
    EPS = lambda a, b, cc: sp.LeviCivita(a, b, cc)
    D = lambda e, k: sp.diff(e, X[k])


    def euler(L, u):
        """variational derivative E_u(L) = sum_alpha (-D)^alpha dL/d(D^alpha u)."""
        L = sp.expand(L)
        ders = {a for a in L.atoms(sp.Derivative) if a.expr == u}
        out = sp.diff(L, u)
        for a in ders:
            t = sp.diff(L, a)
            vs = [v for v, n in a.variable_count for _ in range(n)]
            out += (-1) ** len(vs) * sp.diff(t, *vs)
        return sp.expand(out)


    def pb(f, g, grav=True, ferm=True):
        out = 0
        if ferm:
            for al in range(2):
                Ecf, Edf = euler(f, c[al]), euler(f, d[al])
                Ecg, Edg = euler(g, c[al]), euler(g, d[al])
                out += -I * (Ecf * Edg - Edf * Ecg)
        if grav:
            for (i, j) in HCOMP:
                w = 1 if i == j else 2
                hu, pu = hf(i, j), Pf(i, j)
                Ehf, Epf = euler(f, hu), euler(f, pu)
                Ehg, Epg = euler(g, hu), euler(g, pu)
                if (Ehf == 0 or Epg == 0) and (Epf == 0 or Ehg == 0):
                    continue
                out += sp.Rational(1, w) * (Ehf * Epg - Epf * Ehg)
        return sp.expand(out)


    def is_h(a):
        f = a.expr if isinstance(a, sp.Derivative) else a
        return isinstance(f, sp.core.function.AppliedUndef) and f.func.__name__.startswith("h")


    def hdeg_filter(expr, k):
        """keep the monomials of degree k in the h fields."""
        out = 0
        for t in sp.Add.make_args(sp.expand(expr)):
            n = 0
            for fac in sp.Mul.make_args(t):
                b, e = fac.as_base_exp()
                if is_h(b):
                    n += int(e)
            if n == k:
                out += t
        return out


    def jet_atoms(e):
        at = set(a for a in e.atoms(sp.Derivative))
        at |= set(a for a in e.atoms(sp.core.function.AppliedUndef))
        return sorted(at, key=str)


    def coeff_eqs(e):
        e = sp.expand(e)
        if e == 0:
            return []
        gens = jet_atoms(e)
        out = []
        for cf in sp.Poly(e, *gens).coeffs():
            cf = sp.expand(cf)
            re, im = sp.expand(sp.re(cf)), sp.expand(sp.im(cf))
            for z in (re, im):
                if z != 0:
                    out.append(z)
        return out


    def div_eqs(r, test):
        """equations for the density r (linear in the test field `test`) to be a total divergence."""
        return coeff_eqs(euler(r, test))


    # ---------------------------------------------------------------- matter
    def bil(A, op=None):
        """chibar A chi for a 2x2 matrix A (multiplication)."""
        return sp.expand(sum(d[a] * A[a, b] * c[b] for a in range(2) for b in range(2)))


    def walker(Lp, E, v=1):
        """int chibar 1/2{Lp E_aj sigma_a, p_j} chi, p_j = -i d_j, written out directly."""
        out = 0
        for a in R3:
            for j in R3:
                co = Lp * E[a, j]
                for al in range(2):
                    for be in range(2):
                        s = SIG[a][al, be]
                        if s == 0:
                            continue
                        out += d[al] * (-I / 2) * (co * s * D(c[be], j) + D(co * s * c[be], j))
        return sp.expand(v * out)


    def kosmann(vec, lam, w, kap):
        """lam int chibar i (vec.d + w div vec + i kap curl vec . sigma) chi."""
        div = sum(D(vec[k], k) for k in R3)
        curl = [sum(EPS(cc, k, j) * D(vec[j], k) for k in R3 for j in R3) for cc in R3]
        out = 0
        for al in range(2):
            out += d[al] * I * (sum(vec[k] * D(c[al], k) for k in R3) + w * div * c[al])
            for be in range(2):
                out += d[al] * I * (I * kap * sum(curl[cc] * SIG[cc][al, be] for cc in R3)) * c[be]
        return sp.expand(lam * out)


    def spinrot(u, lam=1):
        """lam int chibar (u . sigma) chi  (u a vector of expressions)."""
        return sp.expand(lam * sum(u[k] * bil(SIG[k]) for k in R3))


    # ---------------------------------------------------------------- gravity
    def LieDelta(vec):
        return sp.Matrix(3, 3, lambda i, j: D(vec[j], i) + D(vec[i], j))


    def LieH(vec, H=None):
        H = Hm if H is None else H
        return sp.Matrix(3, 3, lambda i, j: sum(vec[k] * D(H[i, j], k) + H[k, j] * D(vec[k], i) + H[i, k] * D(vec[k], j)
                                                for k in R3))


    def Pdot(Xm):
        return sp.expand(sum(Pm[i, j] * Xm[i, j] for i in R3 for j in R3))


    def sqrtgR_series(order=2):
        """[sqrt(g) R](n) for g = delta + t h, n = 1..order, computed from Christoffel symbols (own code)."""
        t = sp.Symbol("t")
        tr = lambda e: sp.expand(sp.series(e, t, 0, order + 1).removeO()) if e.has(t) else e
        def trunc(e):
            e = sp.expand(e)
            return sum(e.coeff(t, k) * t ** k for k in range(order + 1))
        H = Hm
        g = sp.eye(3) + t * H
        gi = sp.eye(3) - t * H + t ** 2 * H * H
        gi = gi.applyfunc(trunc)
        dg = [[[D(g[i, j], k) for k in R3] for j in R3] for i in R3]
        Gam = [[[trunc(sum(gi[k, l] * (dg[l][j][i] + dg[l][i][j] - dg[i][j][l]) for l in R3) / 2) for j in R3] for i in R3]
               for k in R3]   # Gam[k][i][j] = Gamma^k_ij
        Ric = [[trunc(sum(D(Gam[k][i][j], k) - D(Gam[k][i][k], j) for k in R3)
                      + sum(Gam[k][k][l] * Gam[l][i][j] - Gam[k][j][l] * Gam[l][i][k] for k in R3 for l in R3))
                for j in R3] for i in R3]
        R = trunc(sum(gi[i, j] * Ric[i][j] for i in R3 for j in R3))
        trh = sum(H[k, k] for k in R3)
        trhh = sum(H[i, j] * H[j, i] for i in R3 for j in R3)
        sg = 1 + t * trh / 2 + t ** 2 * (trh ** 2 / 8 - trhh / 4)
        sR = trunc(sg * R)
        return [sp.expand(sR.coeff(t, k)) for k in range(1, order + 1)]


    # ---------------------------------------------------------------- frames
    def frame_sym(a, order):
        """(delta + a h)^(-1/2) to `order` in h."""
        E = sp.eye(3) - a * Hm / 2
        if order >= 2:
            E += sp.Rational(3, 8) * a ** 2 * Hm * Hm
        return E.applyfunc(sp.expand)


    def inv_series(E, order):
        Xd = E - sp.eye(3)
        Ei, term = sp.eye(3), sp.eye(3)
        for _ in range(order):
            term = (-term * Xd).applyfunc(sp.expand)
            Ei += term
        return Ei




    def vsolve(eqs, unk):
        """sp.solve, then back-substitute into EVERY equation: sympy silently drops equations that involve only parameters
        (found in this check), so a solution is kept only if all equations vanish on it."""
        sols = sp.solve(eqs, unk, dict=True)
        good = []
        for s_ in sols:
            if all(sp.simplify(sp.expand(e.subs(s_))) == 0 for e in eqs):
                good.append(s_)
            else:
                print(f"   [vsolve] rejected spurious solution {s_}", flush=True)
        return good

    _VE['ns'] = SimpleNamespace(**locals())
    return _VE['ns']


# =====================================================================================================================
def part_A(FULL):
    """Campaign B21 check (chk_b21.py): Phi_rho invariance, the invariant TT cone, the equivalent normalisation premises, witnesses."""
    check = _checker("A.b21chk.")
    KE = _kernel_engine()
    COMP, Dk, ETA, G1d, G2Lie, HNAME, Lie_h, M = KE.COMP, KE.Dk, KE.ETA, KE.G1d, KE.G2Lie, KE.HNAME, KE.Lie_h, KE.M
    N, PNAME, Pt, Q, R3, XI, ab, eqs_of = KE.N, KE.PNAME, KE.Pt, KE.Q, KE.R3, KE.XI, KE.ab, KE.eqs_of
    fadd, functional, h, jet, kin0, lapse, lb, pattern = KE.fadd, KE.functional, KE.h, KE.jet, KE.kin0, KE.lapse, KE.lb, KE.pattern
    pb, restrict, sqrtgR_12, trP, trPP, trh, z0 = KE.pb, KE.restrict, KE.sqrtgR_12, KE.trP, KE.trPP, KE.trh, KE.z0



    R3 = range(3)
    XI = [jet(f"x{k}") for k in R3]
    ETA = [jet(f"y{k}") for k in R3]
    N, M = jet("N"), jet("M")
    phi, pi = jet("phi"), jet("pi")
    trh = sum(h(k, k) for k in R3)
    trP = sum(Pt(k, k) for k in R3)
    trPP = sp.expand(sum(Pt(i, j) * Pt(j, i) for i in R3 for j in R3))
    trhP = sp.expand(sum(h(i, j) * Pt(j, i) for i in R3 for j in R3))
    trhPP = sp.expand(sum(h(i, j) * Pt(j, k) * Pt(k, i) for i in R3 for j in R3 for k in R3))
    R1, R2 = sqrtgR_12()
    lam1, nu, K1, K2, al, c, lams, rho = sp.symbols("lam1 nu K1 K2 alpha c lam_s rho", nonzero=True)
    s1, s2, b, c0, beta, betap = sp.symbols("s1 s2 b c0 beta betap")
    kk = sp.symbols("k1:5")


    def G1d(xi):
        return sp.expand(sum(Pt(i, j) * (Dk(xi[j], i) + Dk(xi[i], j)) for i in R3 for j in R3))


    def Lie_h(xi, i, j):
        return sum(xi[k] * Dk(h(i, j), k) + h(k, j) * Dk(xi[k], i) + h(i, k) * Dk(xi[k], j) for k in R3)


    def G2Lie(xi):
        return sp.expand(sum(Pt(i, j) * Lie_h(xi, i, j) for i in R3 for j in R3))


    def Gm(xi):
        return sp.expand(pi * sum(xi[k] * Dk(phi, k) for k in R3))


    def lb(a, b_):
        return [sp.expand(sum(a[k] * Dk(b_[i], k) - b_[k] * Dk(a[i], k) for k in R3)) for i in R3]


    def kin0(alpha=al, bb=b):
        return sp.expand((trPP + bb * trP ** 2) / (4 * alpha))


    def kin1(kv=kk):
        return sp.expand(kv[0] * trh * trPP + kv[1] * trh * trP ** 2 + kv[2] * trhP * trP + kv[3] * trhPP)


    def lapse(xi=XI, S1=s1, S2=s2):
        return sp.expand(S1 * sum(xi[i] * Dk(N, i) for i in R3) + S2 * N * sum(Dk(xi[i], i) for i in R3))


    z0 = [sp.expand(N * Dk(M, i) - M * Dk(N, i)) for i in R3]


    def zeta(B=beta, Bp=betap):
        return [sp.expand(z0[i] + B * sum(h(i, j) * z0[j] for j in R3) + Bp * trh * z0[i]) for i in R3]


    def dewitt_r(r):
        """h-linear part of the DeWitt kinetic term about g = r delta + h, normalised so its h^0 part is (trPP - trP^2/2)/(4 alpha).
        Computed here by direct expansion (independent of any bracket)."""
        e = sp.Symbol("e_")
        H = sp.Matrix(3, 3, lambda i, j: h(i, j))
        Pm = sp.Matrix(3, 3, lambda i, j: Pt(i, j))
        g = r * sp.eye(3) + e * H
        isq = sp.series(1 / sp.sqrt(sp.expand(g.det())), e, 0, 2).removeO()
        gP = g * Pm
        T = sp.expand(isq * ((gP * gP).trace() - gP.trace() ** 2 / 2))
        n0 = sp.simplify(T.coeff(e, 0) / sp.expand(trPP - trP ** 2 / 2))
        return sp.expand(sp.simplify(T.coeff(e, 1) / n0) / (4 * al)), n0


    def kin1_coeffs(expr):
        """read k1..k4 off an isotropic hPP density."""
        sol = sp.solve(eqs_of(functional(sp.expand(expr - kin1()) * N)), kk, dict=True)
        return sol[0]


    SEC = ["T0", "T1", "T2", "T3", "T4", "T5", "T6", "T7"] + (["T3G"] if FULL else [])

    # =====================================================================================================================
    if "T0" in SEC:
        # R1 kernel and R2 modulo total derivatives = Fierz-Pauli
        F1 = functional(N * R1)
        q = Q[0]  # h slot momentum (h sorts before N); N carries -q
        ok1 = True
        for (ab), nm in HNAME.items():
            key = tuple(sorted([nm, "N"]))
            # predicted kernel of int N (d_i d_j h_ij - lap trh): for h slot momentum p: -p_i p_j h_ij + p^2 trh
            a_, b_ = ab
            p = Q[key.index(nm)] if key.index(nm) == 0 else None
            pred = (-q[a_] * q[b_] * (1 if a_ == b_ else 2) + (sum(x ** 2 for x in q) if a_ == b_ else 0))
            ok1 &= sp.expand(F1.get(key, 0) - pred) == 0
        # FP check of R2 mod total derivatives: int R2 kernel on (h,h)
        hs = {ab: sp.Symbol(f"H{ab[0]}{ab[1]}") for ab in COMP}
        Hm = sp.Matrix(3, 3, lambda i, j: hs[(min(i, j), max(i, j))])
        FP = sp.expand(-sp.Rational(1, 4) * sum(Dk(h(i, j), k) ** 2 for i in R3 for j in R3 for k in R3)
                       + sp.Rational(1, 2) * sum(Dk(h(i, j), i) * Dk(h(k, j), k) for i in R3 for j in R3 for k in R3)
                       - sp.Rational(1, 2) * sum(Dk(h(i, j), i) * Dk(trh, j) for i in R3 for j in R3)
                       + sp.Rational(1, 4) * sum(Dk(trh, k) ** 2 for k in R3))
        okfp = eqs_of(fadd(functional(R2), functional(FP), coeffs=[1, -1])) == []
        check("T0a", ok1 and okfp, "own [sqrt g R]^(1) = d_i d_j h_ij - lap trh (kernel), own [sqrt g R]^(2) = Fierz-Pauli "
              "-1/4(dh)^2 + 1/2(d.h)^2 - 1/2 d.h.dtrh + 1/4(dtrh)^2 modulo total derivatives")
        GX = functional(G1d(XI) + G2Lie(XI)); GY = functional(G1d(ETA) + G2Lie(ETA)); L = lb(XI, ETA)
        ok = eqs_of(fadd(pb(GX, GY), functional(G1d(L) + G2Lie(L)), coeffs=[1, -1])) == []
        okm = eqs_of(fadd(pb(functional(Gm(XI)), functional(Gm(ETA))), functional(Gm(L)), coeffs=[1, -1])) == []
        check("T0b", ok and okm, "positive controls of the kernel bracket: {G_GR[xi],G_GR[eta]} = G_GR[[xi,eta]] with "
              "G_GR = int Pt L_xi(delta+h) (all orders), and {G_m,G_m} = G_m[[xi,eta]]")

    # =====================================================================================================================
    if "T1" in SEC:
        def scl(expr):
            sub = {}
            for s in sp.expand(expr).free_symbols:
                nm = str(s).split("|")[0]
                if "|" in str(s) and nm[0] == "h":
                    sub[s] = rho * s
                elif "|" in str(s) and nm[0] == "P":
                    sub[s] = s / rho
            return sp.expand(sp.expand(expr).xreplace(sub))
        # unit metric stress of the scalar about delta + h (direct expansion of pi^2/(2 sqrt g) + c/2 sqrt g g^ij dphi dphi)
        dphi2 = sum(Dk(phi, k) ** 2 for k in R3)
        stress = sp.expand(-trh * pi ** 2 / 4 + c / 2 * (trh / 2 * dphi2 - sum(h(i, j) * Dk(phi, i) * Dk(phi, j) for i in R3 for j in R3)))
        blocks = {"G1 (coef lam1)": (G1d(XI), -1), "G2 = int P L_xi h (coef nu)": (G2Lie(XI), 0), "R1 (coef K1)": (R1, 1),
                  "R2 (coef K2)": (R2, 2), "kin0 (coef 1/alpha)": (trPP - trP ** 2 / 2, -2), "kin1 (coef k)": (kin1(), -1),
                  "matter coupling (coef a_s)": (stress, 1), "matter H0, G_m (coef 1, c, lam_s)": (pi ** 2 + dphi2 + Gm(XI), 0),
                  "zeta's h-term (coef beta)": (sum(h(0, j) * z0[j] for j in R3), 1)}
        ok = True
        for nm, (ex, p) in blocks.items():
            good = sp.expand(scl(ex) - rho ** p * sp.expand(ex)) == 0
            ok &= good
            print(f"   Phi_rho: {nm}: scales as rho^{p}  {'ok' if good else 'WRONG'}")
        check("T1a", ok, "F' = F o Phi_rho (h -> rho h, P -> P/rho): lam1 -> lam1/rho, nu -> nu, K1 -> rho K1, K2 -> rho^2 K2, "
              "alpha -> rho^2 alpha, kin1 -> kin1/rho, a_s -> rho a_s, beta -> rho beta; matter c, lam_s, s1, s2 and c0 unchanged")
        # invariants
        tab = {lam1: lam1 / rho, K1: rho * K1, K2: rho ** 2 * K2, al: rho ** 2 * al}
        inv = {"lam1 K2/K1": lam1 * K2 / K1, "K2/(4 alpha)": K2 / (4 * al), "nu K1/(4 alpha lam1)": nu * K1 / (4 * al * lam1),
               "c0 = K1/(4 alpha lam1)": K1 / (4 * al * lam1), "K1/(4 alpha)": K1 / (4 * al), "K2/K1": K2 / K1, "r = lam1/nu": lam1 / nu}
        res = {k_: sp.simplify(v.subs(tab, simultaneous=True) / v) for k_, v in inv.items()}
        print("   ratio new/old under Phi_rho:", res)
        check("T1b", all(res[k_] == 1 for k_ in ["lam1 K2/K1", "K2/(4 alpha)", "nu K1/(4 alpha lam1)", "c0 = K1/(4 alpha lam1)"])
              and res["K1/(4 alpha)"] == 1 / rho and res["K2/K1"] == rho and res["r = lam1/nu"] == 1 / rho,
              "invariants: lam1 K2/K1, K2/(4 alpha), nu K1/(4 alpha lam1), c0;  NOT invariant: K1/(4 alpha) (x 1/rho), K2/K1 (x rho), "
              "r (x 1/rho).  Canonicity: Phi_rho preserves int P dh exactly (linear symplectic map)")

    # =====================================================================================================================
    if "T2" in SEC:
        # graviton TT dispersion from the quadratic H = int (trPP - trP^2/2)/(4 alpha) - K2 R2 (N = 1): mode h01, k = (0,0,k)
        Hq = fadd(functional(kin0(al, -sp.Rational(1, 2))), functional(R2), coeffs=[1, -K2])
        kz = sp.Symbol("kz")
        # kernel at slots (h01,h01) and (P01,P01): momenta q0 = (0,0,kz), q1 = -q0 (eliminated)
        sub = {Q[0][0]: 0, Q[0][1]: 0, Q[0][2]: kz}
        Ahh = sp.expand(Hq[("h01", "h01")].xreplace(sub))
        App = sp.expand(Hq[("P01", "P01")].xreplace(sub))
        # cross-check no h01 coupling to other h's at this k for TT (h01 with k along z is TT)
        others = [k_ for k_ in Hq if "h01" in k_ and k_ != ("h01", "h01")]
        oth0 = all(sp.expand(Hq[k_].xreplace(sub)) == 0 for k_ in others)
        w2 = sp.simplify(4 * Ahh * App)
        print(f"   H(h01,h01) kernel = {Ahh}, H(P01,P01) = {App}, omega^2 = 4 A_hh A_PP = {w2}")
        check("T2", sp.simplify(w2 - K2 * kz ** 2 / (4 * al)) == 0 and oth0,
              "TT graviton (h01, k || z, decoupled) has omega^2 = K2 k^2/(4 alpha): the graviton cone is K2/(4 alpha); R1 never "
              "enters TT propagation")

    # =====================================================================================================================
    def iso_basis():
        """isotropic parity-even one-derivative P-linear h-linear xi-linear densities: all 15 pairings x 2 placements,
        reduced to an independent set (own enumeration, not B21's list)."""
        idx = list(range(6))

        def pairings(lst):
            if not lst:
                yield []
                return
            a = lst[0]
            for i in range(1, len(lst)):
                rest = lst[1:i] + lst[i + 1:]
                for p in pairings(rest):
                    yield [(a, lst[i])] + p
        cands = []
        for typ in ("xi_dh", "dxi_h"):
            for pr in pairings(idx):
                tot = 0
                for vals in itertools.product(R3, repeat=3):
                    v = [None] * 6
                    for (a_, b_), x in zip(pr, vals):
                        v[a_] = v[b_] = x
                    i, j, k, l, m, n = v
                    if typ == "xi_dh":
                        tot += Pt(i, j) * XI[k] * Dk(h(m, n), l)
                    else:
                        tot += Pt(i, j) * Dk(XI[k], l) * h(m, n)
                cands.append(sp.expand(tot))
        # independence via kernel coefficients
        vecs, basis = [], []
        allkeys = None
        Fs = [functional(cd) for cd in cands]
        mons = {}
        rows = []
        for F in Fs:
            row = {}
            for key, ker in F.items():
                qs = [x for x in sp.Matrix(Q[:3]).reshape(9, 1)]
                for mon, cc in sp.Poly(ker, *qs).terms():
                    row[(key, mon)] = cc
                    mons.setdefault((key, mon), len(mons))
            rows.append(row)
        Mx = sp.zeros(len(rows), len(mons))
        for r_, row in enumerate(rows):
            for kmon, cc in row.items():
                Mx[r_, mons[kmon]] = cc
        sel = []
        cur = sp.zeros(0, len(mons))
        for r_ in range(len(rows)):
            trial = cur.col_join(Mx[r_, :])
            if trial.rank() > cur.rows:
                cur = trial
                sel.append(r_)
        return [cands[s] for s in sel], cands


    def xi_to_eta(expr):
        return sp.expand(expr.xreplace({XI[k]: ETA[k] for k in R3}).xreplace(
            {jet(f"x{k}", a): jet(f"y{k}", a) for k in R3 for a in itertools.product(range(3), repeat=3) if sum(a) <= 2}))


    def subs_xi(expr, vec):
        """replace the parameter field xi (appearing linearly) by a density-valued vector (for G2[zeta])."""
        out = 0
        for term in sp.Add.make_args(sp.expand(expr)):
            xs = [x for x in term.free_symbols if str(x).split("|")[0] in ("x0", "x1", "x2")]
            assert len(xs) == 1 and sp.degree(term, xs[0]) == 1
            x = xs[0]
            nm, al_ = str(x).split("|")
            v = vec[int(nm[1])]
            for k in R3:
                for _ in range(int(al_[k])):
                    v = Dk(v, k)
            out += sp.expand(term / x * v)
        return sp.expand(out)


    def solve_unique(eqs, unk):
        """exact rank / unique solution via DomainMatrix rref; returns (nullity, consistent, solution dict or None)."""
        A, rhs = sp.linear_eq_to_matrix(eqs, unk)
        Ad = DomainMatrix.from_Matrix(A).convert_to(sp.QQ)
        Aug = DomainMatrix.from_Matrix(A.row_join(rhs)).convert_to(sp.QQ)
        rk, rka = Ad.rank(), Aug.rank()
        if rk != rka:
            return len(unk) - rk, False, None
        if rk < len(unk):
            return len(unk) - rk, True, None
        R, piv = Aug.rref()
        Rm = R.to_Matrix()
        return 0, True, {unk[i]: Rm[i, -1] for i in range(len(unk))}


    if "T3" in SEC or "T3G" in SEC or "T5" in SEC:
        BAS, CANDS = iso_basis()
        print(f"   isotropic one-derivative G2 basis: {len(CANDS)} pairings -> rank {len(BAS)}")

    if "T3" in SEC:
        m = sp.symbols(f"m0:{len(BAS)}")
        G2x = sp.expand(sum(mi * bi for mi, bi in zip(m, BAS)))
        G2y = xi_to_eta(G2x)
        L = lb(XI, ETA)
        GX = functional(lam1 * G1d(XI) + G2x)
        GY = functional(lam1 * G1d(ETA) + G2y)
        kP = pattern(P=1, x=1, y=1)
        gg = fadd(pb(GX, GY, keep=kP), functional(lam1 * G1d(L), keep=kP), coeffs=[1, -nu])
        e_gg = eqs_of(gg)
        C = functional(N * (-K1 * R1 - K2 * R2))
        kh = pattern(N=1, x=1, h=1)
        cg = fadd(pb(C, functional(lam1 * G1d(XI) + G2x), keep=kh), functional(lapse() * (-K1 * R1), keep=kh), coeffs=[1, -1])
        e_cg = eqs_of(cg)
        sgg = sp.solve(e_gg, list(m) + [nu], dict=True)
        scg = sp.solve(e_cg, list(m) + [s1, s2], dict=True)
        sj = sp.solve(e_gg + e_cg, list(m) + [nu, s1, s2], dict=True)
        nfree = lambda sol, unk: len([x for x in unk if x not in sol])
        print(f"   {{G,G}} order P alone: {len(sgg)} branch(es), free m: {nfree(sgg[0], m) if sgg else None}  {sgg}")
        print(f"   {{C,G}} h-linear alone: free m: {nfree(scg[0], m) if scg else None}  {scg}")
        print(f"   joint: {sj}")
        # express joint G2 against nu * L_xi h
        ok = False
        if len(sj) == 1 and nfree(sj[0], m) == 0:
            G2s = sp.expand(G2x.subs(sj[0]))
            nus = sj[0][nu]
            ok = eqs_of(fadd(functional(G2s), functional(G2Lie(XI)), coeffs=[1, -nus])) == [] \
                and sp.simplify(nus - lam1 * K2 / K1) == 0 and sp.simplify(sj[0][s1] + nus) == 0 and sj[0][s2] == 0
        check("T3", ok, "A3 reproduced on an own isotropic basis: {G,G} order P + {C,G} h-linear force G2 = nu int Pt L_xi h "
              "uniquely, nu = lam1 K2/K1, s1 = -nu, s2 = 0 (symbolic lam1, K1, K2)")

    # =====================================================================================================================
    if "T3G" in SEC:
        # fully general (non-isotropic, no parity) 648-coefficient one-derivative P-linear h-linear G2, numeric parameters
        coef = []
        dens = 0
        for ab in COMP:
            Pab = jet(PNAME[ab])
            for cc in R3:
                for d in R3:
                    for ef in COMP:
                        u = sp.Symbol(f"u_{ab[0]}{ab[1]}_{cc}{d}_{ef[0]}{ef[1]}")
                        w = sp.Symbol(f"w_{ab[0]}{ab[1]}_{cc}{d}_{ef[0]}{ef[1]}")
                        coef += [u, w]
                        dens += u * Pab * XI[cc] * Dk(jet(HNAME[ef]), d) + w * Pab * jet(HNAME[ef]) * Dk(XI[cc], d)
        dens = sp.expand(dens)
        print(f"   general G2: {len(coef)} coefficients")
        L = lb(XI, ETA)
        random.seed(21)
        allok = True
        for trial in range(2):
            L1v, K1v, K2v = [sp.Rational(random.randint(1, 9), random.randint(1, 9)) for _ in range(3)]
            GX = functional(L1v * G1d(XI) + dens)
            GY = functional(L1v * G1d(ETA) + xi_to_eta(dens))
            kP = pattern(P=1, x=1, y=1)
            gg = fadd(pb(GX, GY, keep=kP), functional(L1v * G1d(L), keep=kP), coeffs=[1, -nu])
            C = functional(N * (-K1v * R1 - K2v * R2))
            kh = pattern(N=1, x=1, h=1)
            cg = fadd(pb(C, GX, keep=kh), functional(lapse() * (-K1v * R1), keep=kh), coeffs=[1, -1])
            unk = coef + [nu, s1, s2]
            out = {}
            for nm, eqs in (("GG", eqs_of(gg)), ("CG", eqs_of(cg)), ("joint", eqs_of(gg) + eqs_of(cg))):
                nul, cons, sol = solve_unique(eqs, unk)
                out[nm] = (nul, cons)
                if nm == "joint" and sol is not None:
                    nus = sol[nu]
                    G2s = sp.expand(dens.subs(sol))
                    okL = eqs_of(fadd(functional(G2s), functional(G2Lie(XI)), coeffs=[1, -nus])) == []
                    out["sol"] = (nus, sol[s1], sol[s2], okL)
            print(f"   trial {trial}: lam1={L1v} K1={K1v} K2={K2v}: null dims (GG, CG, joint) = "
                  f"{out['GG'][0]}, {out['CG'][0]}, {out['joint'][0]}; consistent={out['joint'][1]}; joint sol nu, s1, s2, free, ==nu*Lie: {out.get('sol')}")
            sol = out.get("sol")
            allok &= out["joint"][0] == 0 and sol is not None and sp.simplify(sol[0] - L1v * K2v / K1v) == 0 and sol[3] \
                and sol[1] == -sol[0] and sol[2] == 0
        check("T3G", allok, "A3 in the FULLY GENERAL 648-coefficient one-derivative G2 (no isotropy, no parity), two random "
              "rational (lam1, K1, K2): {G,G} order P + {C,G} h-linear have a unique solution G2 = nu int Pt L_xi h, nu = lam1 K2/K1")

    # =====================================================================================================================
    def model_r(r, nu_=sp.Integer(1), K1_=sp.Integer(3), al_=sp.Integer(5), K2_=None):
        lam1_ = r * nu_
        K2v = K1_ / r if K2_ is None else K2_
        k1d, _ = dewitt_r(r)
        k1d = k1d.subs(al, al_)
        Cd = lambda L_: sp.expand(L_ * (kin0(al_, -sp.Rational(1, 2)) + k1d - K1_ * R1 - K2v * R2))
        Gd = lambda xi: sp.expand(lam1_ * G1d(xi) + nu_ * G2Lie(xi))
        return dict(lam1=lam1_, nu=nu_, K1=K1_, K2=K2v, al=al_, Cd=Cd, Gd=Gd, beta=-1 / r, c0=K1_ / (4 * al_ * lam1_))


    def run_witness(tag, r, K2_=None):
        md = model_r(r, K2_=K2_)
        L = lb(XI, ETA)
        GX, GY = functional(md["Gd"](XI)), functional(md["Gd"](ETA))
        out = {}
        gg = fadd(pb(GX, GY), functional(md["Gd"](L)), coeffs=[1, -md["nu"]])
        out["GG_P"] = eqs_of(restrict(gg, pattern(P=1, x=1, y=1))) == []
        out["GG_Ph"] = eqs_of(restrict(gg, pattern(P=1, h=1, x=1, y=1))) == []
        CN = functional(md["Cd"](N), keep=lambda f: sum(1 for x in f if x[0] in "hP") <= 3)
        CM = functional(md["Cd"](M), keep=lambda f: sum(1 for x in f if x[0] in "hP") <= 3)
        Np = lapse(XI, -md["nu"], 0)
        kh = pattern(N=1, x=1, h=1)
        kPP = pattern(N=1, x=1, P=2)
        cg = fadd(pb(CN, GX, keep=lambda f: kh(f) or kPP(f)), functional(md["Cd"](Np), keep=lambda f: kh(f) or kPP(f)), coeffs=[1, -1])
        out["CG_h"] = eqs_of(restrict(cg, kh)) == []
        out["CG_PP"] = eqs_of(restrict(cg, kPP)) == []
        kP = pattern(N=1, M=1, P=1)
        kPh = pattern(N=1, M=1, P=1, h=1)
        keep = lambda f: kP(f) or kPh(f)
        cc = fadd(pb(CN, CM, keep=keep), functional(md["c0"] * md["Gd"](zeta(md["beta"], 0)), keep=keep), coeffs=[1, -1])
        out["CC_P"] = eqs_of(restrict(cc, kP)) == []
        out["CC_Ph"] = eqs_of(restrict(cc, kPh)) == []
        print(f"   {tag}: r={r} lam1={md['lam1']} nu={md['nu']} K1={md['K1']} K2={md['K2']} alpha={md['al']} beta={md['beta']} "
              f"c0={md['c0']}: {out}", flush=True)
        return out


    if "T4" in SEC:
        o = run_witness("W1", sp.Integer(2))
        check("T4a", all(o.values()), "witness r = 2 (lam1 = 2, nu = 1, K1 = 3, K2 = 3/2, alpha = 5, kin1 = DeWitt about 2 delta, "
              "beta = -1/2, s1 = -1): closes in {G,G} (P, Ph), {C,G} (h, P^2), {C,C} (P, Ph): K1 != K2 closes")
        o = run_witness("W2", sp.Integer(2), K2_=sp.Integer(3))
        check("T4b", (not o["CG_h"]) and (not o["CC_Ph"]) and o["GG_P"] and o["CC_P"],
              "negative control r = 2 with K2 := K1 = 3: {C,G} h-linear and {C,C} Ph FAIL (others pass)")
        o = run_witness("W3", sp.Integer(1))
        check("T4c", all(o.values()), "r = 1 (lam1 = nu, K1 = K2 = 3): closes in all six sectors")
        o = run_witness("W4", sp.Rational(1, 3))
        check("T4d", all(o.values()), "r = 1/3 (K1 = 3, K2 = 9; the Phi_3 image of r = 1, rho > 1 direction): closes in all six sectors")

    # =====================================================================================================================
    if "T5" in SEC:
        # route 2: {C,C} at order Ph alone with G2 = nu L_xi h; kin1 general (4 isotropic), beta, beta', K2 unknown
        CN = functional(N * (kin0(al, -sp.Rational(1, 2)) + kin1() - K1 * R1 - K2 * R2))
        CM = functional(M * (kin0(al, -sp.Rational(1, 2)) + kin1() - K1 * R1 - K2 * R2))
        kPh = pattern(N=1, M=1, P=1, h=1)
        rhs = functional(K1 / (4 * al * lam1) * (lam1 * G1d(zeta()) + nu * G2Lie(zeta())), keep=kPh)
        e7 = eqs_of(fadd(pb(CN, CM, keep=kPh), rhs, coeffs=[1, -1]))
        s7 = sp.solve(e7, list(kk) + [beta, betap, K2], dict=True)
        dw, _ = dewitt_r(lam1 / nu)
        dwc = kin1_coeffs(dw)
        print("   {C,C} Ph, G2 = nu Lie, unknown kin1/beta/beta'/K2:", s7)
        ok = len(s7) == 1 and sp.simplify(s7[0][K2] - nu * K1 / lam1) == 0 and sp.simplify(s7[0][beta] + nu / lam1) == 0 \
            and s7[0][betap] == 0 and all(sp.simplify(s7[0][x] - dwc[x]) == 0 for x in kk)
        check("T5a", ok, "route 2 (A7b): {C,C} at order Ph with G2 = nu L_xi h forces lam1 K2 = nu K1, beta = -nu/lam1, beta' = 0 and "
              "kin1 = DeWitt about (lam1/nu) delta (own direct expansion)")
        # A7d: impose beta = -1, unknown lam1 and K2, with the isotropic G2 restricted by {G,G} order P (recomputed here)
        m = sp.symbols(f"m0:{len(BAS)}")
        G2x = sp.expand(sum(mi * bi for mi, bi in zip(m, BAS)))
        L = lb(XI, ETA)
        kP = pattern(P=1, x=1, y=1)
        gg = fadd(pb(functional(lam1 * G1d(XI) + G2x), functional(lam1 * G1d(ETA) + xi_to_eta(G2x)), keep=kP),
                  functional(lam1 * G1d(L), keep=kP), coeffs=[1, -nu])
        sgg = sp.solve(eqs_of(gg), list(m), dict=True)[0]
        G2gg = sp.expand(G2x.subs(sgg))
        rhs = functional(K1 / (4 * al * lam1) * (lam1 * G1d(zeta(-1, betap)) + subs_xi(G2gg, zeta(-1, betap))), keep=kPh)
        e7d = eqs_of(fadd(pb(CN, CM, keep=kPh), rhs, coeffs=[1, -1]))
        unk = [x for x in m if x not in sgg] + list(kk) + [betap, K2, lam1]
        s7d = sp.solve(e7d, unk, dict=True)
        print("   {G,G}P + {C,C}Ph with beta = -1 (lam1, K2 unknown):", s7d)
        okd = len(s7d) >= 1 and all(sp.simplify(s_[K2] - K1) == 0 and sp.simplify(s_[lam1] - nu) == 0 for s_ in s7d)
        check("T5b", okd, "A7d: with the structure function fixed to delta - h (beta = -1), {G,G} order P + {C,C} Ph force "
              "K2 = K1 and lam1 = nu (so beta = -1 is a normalisation premise equivalent to K1 = K2)")

    # =====================================================================================================================
    if "T6" in SEC:
        # matter: scalar, general isotropic h-linear coupling with <= 2 derivatives on (phi, phi) or pi^2
        a = sp.symbols("a1:11")
        dp = lambda k: Dk(phi, k)
        coup = (a[0] * trh * sum(dp(k) ** 2 for k in R3) + a[1] * sum(h(i, j) * dp(i) * dp(j) for i in R3 for j in R3)
                + a[2] * trh * phi * sum(Dk(dp(k), k) for k in R3) + a[3] * sum(h(i, j) * phi * Dk(dp(i), j) for i in R3 for j in R3)
                + a[4] * sum(Dk(h(i, j), i) * phi * dp(j) for i in R3 for j in R3) + a[5] * sum(Dk(trh, k) * phi * dp(k) for k in R3)
                + a[6] * sum(Dk(Dk(h(i, j), i), j) for i in R3 for j in R3) * phi ** 2
                + a[7] * sum(Dk(Dk(trh, k), k) for k in R3) * phi ** 2 + a[8] * trh * pi ** 2 + a[9] * trh * phi ** 2)
        H0 = pi ** 2 / 2 + c / 2 * sum(dp(k) ** 2 for k in R3)
        Cm = lambda L_: sp.expand(L_ * (H0 + coup))

        def keepm(f):
            return sum(1 for x in f if x in ("phi", "pi")) == 2 and not any(x[0] in "hP" for x in f) \
                and any(x[0] == "x" for x in f) and "N" in f
        Gtot = functional(lam1 * G1d(XI) + nu * G2Lie(XI) + lams * Gm(XI))
        cg = fadd(pb(functional(Cm(N)), Gtot, keep=keepm), functional(lapse() * H0, keep=keepm), coeffs=[1, -1])
        sm = sp.solve(eqs_of(cg), list(a) + [s1, s2], dict=True)
        print("   matter {C,G} at order matter^2:", sm)
        dphi2 = sum(dp(k) ** 2 for k in R3)
        unit = sp.expand(-trh * pi ** 2 / 4 + c / 2 * (trh / 2 * dphi2 - sum(h(i, j) * dp(i) * dp(j) for i in R3 for j in R3)))
        okm = len(sm) == 1 and sp.simplify(sm[0][s1] + lams) == 0
        if okm:
            cs = sp.expand(coup.subs(sm[0]).subs(s2, 0))
            free = sorted({str(x) for x in cs.free_symbols if str(x) in [str(y) for y in a]})
            print(f"   with s2 = 0: free coupling directions left = {free}")
            # run-1 expectation bug (kept as run_T6_run1_Rphi2_EXPECTATION_BUG.log): the solve leaves a7 = -a8 free, i.e. the
            # covariant non-minimal coupling a8 (lap trh - d_i d_j h_ij) phi^2 = -a8 R1 phi^2 (xi R phi^2 at h-linear order).
            # That is a genuine covariant freedom, not a defect; it is now subtracted explicitly and must be the ONLY freedom.
            Rphi2 = sp.expand(R1 * phi ** 2)
            okm &= free == ["a8"] and eqs_of(fadd(functional(N * cs), functional(N * unit), functional(N * Rphi2),
                                                  coeffs=[1, -lams / lam1, a[7]])) == []
        check("T6a", okm, "matter {C,G} (scalar, 10-term isotropic h-linear coupling ansatz): s1 = -lam_s and, with gravity's s2 = 0, "
              "the coupling is (lam_s/lam1) x the unit metric stress of delta + h, plus only the covariant non-minimal R1 phi^2 "
              "direction  =>  a_s = lam_s/lam1")
        # matter {C,C}: c = c0 lam_s with c0 from the gravity order-P sector
        CN, CM = functional(N * (kin0() - K1 * R1)), functional(M * (kin0() - K1 * R1))
        CNm, CMm = functional(Cm(N)), functional(Cm(M))
        kP = pattern(N=1, M=1, P=1)
        km = lambda f: sorted(f) == sorted(["N", "M", "phi", "pi"])
        lhs = pb(fadd(CN, CNm), fadd(CM, CMm), keep=lambda f: kP(f) or km(f))
        rhs = functional(c0 * (lam1 * G1d(z0) + lams * Gm(z0)), keep=lambda f: kP(f) or km(f))
        scc = sp.solve(eqs_of(fadd(lhs, rhs, coeffs=[1, -1])), [b, c0, c], dict=True)
        print("   {C,C} order P + order phi pi:", scc)
        okc = len(scc) == 1 and scc[0][b] == -sp.Rational(1, 2) and sp.simplify(scc[0][c0] - K1 / (4 * al * lam1)) == 0 \
            and sp.simplify(scc[0][c] - lams * K1 / (4 * al * lam1)) == 0
        check("T6b", okc, "{C,C}: b = -1/2, c0 = K1/(4 alpha lam1), matter cone c = lam_s K1/(4 alpha lam1); with lam_s = nu "
              "(matter {G,G}, T0b) and nu = lam1 K2/K1 (T3): c = K2/(4 alpha) = graviton TT cone (T2)")
        # premise (d) as a computation: matter coupling FIXED to unit strength, lam_s = nu; unknown lam1, K2, s1, s2
        Cg = functional(N * (-K1 * R1 - K2 * R2))
        kh = pattern(N=1, x=1, h=1)
        cgg = fadd(pb(Cg, functional(lam1 * G1d(XI) + nu * G2Lie(XI)), keep=kh), functional(lapse() * (-K1 * R1), keep=kh),
                   coeffs=[1, -1])
        Cmu = functional(N * (H0 + unit))
        Gt = functional(lam1 * G1d(XI) + nu * G2Lie(XI) + nu * Gm(XI))
        cgm = fadd(pb(Cmu, Gt, keep=keepm), functional(lapse() * H0, keep=keepm), coeffs=[1, -1])
        sd = sp.solve(eqs_of(cgg) + eqs_of(cgm), [lam1, K2, s1, s2], dict=True)
        print("   unit matter coupling fixed, lam_s = nu; solve gravity + matter {C,G} for lam1, K2, s1, s2:", sd)
        okd = len(sd) == 1 and sp.simplify(sd[0][lam1] - nu) == 0 and sp.simplify(sd[0][K2] - K1) == 0
        check("T6c", okd, "premise (d) computed: with the matter coupling FIXED to unit metric stress of delta + h (not "
              "Phi_rho-covariant: a_s -> rho a_s) the h-linear {C,G} brackets force lam1 = nu and K2 = K1.  So 'no bracket can force "
              "K1 = K2' holds only when every Phi_rho-non-invariant normalisation in the ansatz is left free")

    # =====================================================================================================================
    if "T7" in SEC:
        # A6: {C,G} P^2 sector with G2 = nu Lie, s1 = -nu, s2 = 0 forces kin1 = DeWitt / r
        C = functional(N * (kin0(al, -sp.Rational(1, 2)) + kin1()))
        kPP = pattern(N=1, x=1, P=2)
        cg = fadd(pb(C, functional(lam1 * G1d(XI) + nu * G2Lie(XI)), keep=kPP),
                  functional(lapse(XI, -nu, 0) * kin0(al, -sp.Rational(1, 2)), keep=kPP), coeffs=[1, -1])
        s6 = sp.solve(eqs_of(cg), list(kk), dict=True)
        dw, n0 = dewitt_r(lam1 / nu)
        dwc = kin1_coeffs(dw)
        print("   A6:", s6, " DeWitt/r:", dwc)
        ok = len(s6) == 1 and all(sp.simplify(s6[0][x] - dwc[x]) == 0 for x in kk)
        check("T7", ok, "A6: {C,G} P^2 sector with G2 = nu L_xi h and N' = -nu xi.dN forces kin1 = h-linear DeWitt about "
              "(lam1/nu) delta (own expansion; = (nu/lam1) x DeWitt about delta)")




# =====================================================================================================================
def part_B(FULL):
    """Campaign C4 runner (c4_h_normalisation.py): the walker's coupling strength, the lapse identity with K1, K2, a_s, Phi_rho invariants, R1/R2."""
    check = _checker("B.c4.")


    # ----------------------------------------------------------------------------- common objects
    s1, s2, s3 = sp.symbols('s1 s2 s3', real=True)
    svec = sp.Matrix([s1, s2, s3])
    sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    I2 = sp.eye(2)


    def symm(name):
        a = sp.symbols(f'{name}11 {name}22 {name}33 {name}12 {name}13 {name}23', real=True)
        M = sp.Matrix([[a[0], a[3], a[4]], [a[3], a[1], a[5]], [a[4], a[5], a[2]]])
        return M, list(a)


    h, hv = symm('h')

    # ============================================================================ PART A
    print("   -- C4 runner part A: the walker's coupling strength to h")

    # A1 block 62 T1(a): uniform frame E (E[a, j] = E_a^j), H(k) = sum_j (E^j . sigma) s_j,
    #    H^2 = (s^T E^T E s) 1, i.e. g^{ij} = sum_a E_a^i E_a^j.  Exact for a general 3x3 frame.
    E = sp.Matrix(3, 3, lambda a, j: sp.Symbol(f'E{a+1}{j+1}', real=True))
    Hk = sp.zeros(2, 2)
    for j in range(3):
        for a in range(3):
            Hk += E[a, j] * sig[a] * svec[j]
    lhs = sp.expand(Hk * Hk)
    rhs = sp.expand((svec.T * E.T * E * svec)[0, 0]) * I2
    check("A1", sp.simplify(lhs - rhs) == sp.zeros(2, 2),
          "uniform frame: H(k)^2 = s^T (E^T E) s * 1 exactly (Clifford relation of the coin); the walker's cone is g^{-1} = E^T E")

    # A2 With E = 1 + t*eps (general eps), h := (E^T E)^{-1} - delta.  Matter on the metric
    #    delta + a h has omega^2 = s^T (delta + a h)^{-1} s.  The order-t match with the walker fixes a.
    t, a_cpl = sp.symbols('t a', real=True)
    eps = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'e{i+1}{j+1}', real=True))
    Ef = sp.eye(3) + t * eps
    ginv_walker = Ef.T * Ef
    h1 = -(eps + eps.T)  # first-order h from h = (E^T E)^{-1} - 1
    g_series = sp.eye(3) - t * (eps + eps.T)  # (1 + t X)^{-1} to first order, X = eps + eps^T
    chk_h1 = sp.expand((g_series * ginv_walker - sp.eye(3)).applyfunc(lambda z: sp.expand(z).coeff(t, 1)))
    check("A2a", chk_h1 == sp.zeros(3, 3),
          "h = (E^T E)^{-1} - delta = -(eps + eps^T) t + O(t^2): only the symmetric part of the tilt enters (block 62 T3(a))")
    om2_walker = sp.expand((svec.T * ginv_walker * svec)[0, 0])
    om2_matter_first = sp.expand((svec.T * (sp.eye(3) - a_cpl * t * h1) * svec)[0, 0])  # (delta + a t h1)^{-1} to O(t)
    eq = sp.expand(om2_walker.coeff(t, 1) - om2_matter_first.coeff(t, 1))
    sol = sp.solve(sp.Poly(eq, *list(eps), s1, s2, s3).coeffs(), a_cpl, dict=True)
    check("A2b", sol == [{a_cpl: 1}],
          f"order-t match of the walker's cone with matter on delta + a h for all eps, s: solution {sol} (a_s = 1 uniquely)")

    # A2c exact to all orders: (delta + h)^{-1} = E^T E by definition, so the walker's uniform cone is
    #     exactly that of g = delta + h.  Check at second order explicitly (not just definitional).
    X = eps + eps.T
    g2 = sp.eye(3) - t * X + t**2 * (X * X - eps.T * eps)  # (1 + tX + t^2 eps^T eps)^{-1} to O(t^2)
    prod = (g2 * ginv_walker).applyfunc(lambda z: sp.expand(z))
    ok = all(sp.expand(prod[i, j]).coeff(t, 2) == 0 and sp.expand(prod[i, j]).coeff(t, 1) == 0
             for i in range(3) for j in range(3))
    check("A2c", ok, "second order: (delta + h)(E^T E) = 1 + O(t^3) with h = -tX + t^2(X^2 - eps^T eps); unit coupling persists beyond first order")

    # A3 block 62 T2: plane wave positive branch, identity frame, Theta_ij = s_i s_j/|s|.
    #    Fixed-state shift d<H> = sum E Theta with E = 1 - h/2 (symmetric tilt) = -(1/2) sum Theta h.
    #    Matter on delta + a h: d omega = d sqrt(s^T (1 - a h) s) = -(a/2) s^T h s/|s|.
    nrm = sp.sqrt(s1**2 + s2**2 + s3**2)
    Theta = svec * svec.T / nrm
    dH_walker = sum(Theta[i, j] * (-h[i, j] / 2) for i in range(3) for j in range(3))
    dom_matter = sp.diff(sp.sqrt((svec.T * (sp.eye(3) - a_cpl * t * h) * svec)[0, 0]), t).subs(t, 0)
    sol3 = sp.solve(sp.simplify(dH_walker - dom_matter).subs({h[0, 0]: 1, h[1, 1]: 0, h[2, 2]: 0,
                                                              h[0, 1]: 0, h[0, 2]: 0, h[1, 2]: 0, s1: 1, s2: 0, s3: 0}), a_cpl)
    resid3 = sp.simplify((dH_walker - dom_matter).subs(a_cpl, 1))
    check("A3", sol3 == [1] and resid3 == 0,
          "block 62's source -(1/2) sum Theta_(ij) h_ij is the metric-variational stress at unit strength: a_s = 1")

    # A4/A5 bond couplings with the realisation B = -(a_R/2) h (uniform, phi_j = 1 at q = 0):
    #   block 64 (one-step):  H(k) = sum_a sigma_a [ s_a + sum_j B_aj c_a s_j ]
    #   block 73 (two-step):  H(k) = sum_a sigma_a [ s_a + sum_j B_aj c_a P_j ],  P_j = s_j c_j
    k1, k2, k3, d1, d2, d3, aR, lam = sp.symbols('k1 k2 k3 d1 d2 d3 a_R lam', real=True)
    kk = [k1, k2, k3]
    sk = [sp.sin(x) for x in kk]
    ck = [sp.cos(x) for x in kk]
    Pk = [sk[i] * ck[i] for i in range(3)]


    def h2_first_order(xvec, bond=True):
        B = -(aR / 2) * h
        vec = [sk[a] + lam * sum(B[a, j] * (ck[a] if bond else 1) * xvec[j] for j in range(3)) for a in range(3)]
        H2 = sum(v**2 for v in vec)
        return sp.expand(sp.diff(H2, lam).subs(lam, 0))


    first_two = h2_first_order(Pk)
    target_two = -aR * sum(Pk[i] * h[i, j] * Pk[j] for i in range(3) for j in range(3))
    check("A5a", sp.simplify(first_two - sp.expand(target_two)) == 0,
          "two-step coupling: H^2 = |s|^2 - a_R P^T h P + O(h^2) at every wave vector (s_a c_a = P_a)")


    def corner_form(first, K):
        # quadratic form in delta-k at the species corner K (entries 0 or pi)
        sub = {kk[i]: K[i] + [d1, d2, d3][i] * t for i in range(3)}
        ser = sp.series(first.subs(sub), t, 0, 3).removeO()
        return sp.expand(sp.expand(ser).coeff(t, 2))


    dvec = sp.Matrix([d1, d2, d3])
    first_site = h2_first_order(sk, bond=False)   # block 62 site frame E = 1 + B
    first_one = h2_first_order(sk, bond=True)     # block 64 one-step bond coupling
    ok_two = ok_site = ok_one = True
    unit_species = {'site': 0, 'one-step': 0, 'two-step': 0}
    for K in itertools.product([0, sp.pi], repeat=3):
        eta = [sp.cos(x) for x in K]
        q2 = corner_form(first_two, K)
        ok_two &= sp.simplify(q2 - sp.expand(-aR * (dvec.T * h * dvec)[0, 0])) == 0
        qs = corner_form(first_site, K)
        ok_site &= sp.simplify(qs - sp.expand(-aR * sum(eta[i] * dvec[i] * h[i, j] * eta[j] * dvec[j]
                                                         for i in range(3) for j in range(3)))) == 0
        q1 = corner_form(first_one, K)
        ok_one &= sp.simplify(q1 - sp.expand(-aR * sum(dvec[i] * h[i, j] * eta[j] * dvec[j]
                                                        for i in range(3) for j in range(3)))) == 0
        unit = sp.expand(-aR * (dvec.T * h * dvec)[0, 0])
        unit_species['two-step'] += int(sp.simplify(q2 - unit) == 0)
        unit_species['site'] += int(sp.simplify(qs - unit) == 0)
        unit_species['one-step'] += int(sp.simplify(q1 - unit) == 0)
    check("A5b", ok_two,
          "two-step coupling at all eight species corners: H^2 = dk^T (1 - a_R h) dk + O(dk^3, h^2) -> a_s = a_R for every species")
    check("A4", ok_site and ok_one and unit_species == {'site': 2, 'one-step': 1, 'two-step': 8},
          "species corners: site frame (block 62) sees eta h eta (diagonals unit, mixed off-diagonals flipped); "
          f"one-step bond (block 64) sees sym(h eta); species seeing exactly delta + a_R h: {unit_species}")
    long_wave = sp.expand(sp.series(first_two.subs({k1: d1 * t, k2: d2 * t, k3: d3 * t}), t, 0, 3).removeO().coeff(t, 2))
    check("A5c", sp.simplify(long_wave + aR * (dvec.T * h * dvec)[0, 0]) == 0,
          "long wavelength: the realisation's normalisation clause 'Lambda R(0) = 1' (block 120 note) is a_R = 1, i.e. a_s = 1")

    # ============================================================================ PART B
    print("   -- C4 runner part B: the member's lapse identity with K1 != K2 and source strength a_s")
    p1, p2, p3 = sp.symbols('p1 p2 p3', real=True)
    pv = sp.Matrix([p1, p2, p3])
    pp = p1**2 + p2**2 + p3**2
    K1, K2, al, be, a_s, u = sp.symbols('K1 K2 alpha beta a_s u', real=True)
    Th, thv = symm('Th')


    def R1(M):
        return pp * M.trace() - (pv.T * M * pv)[0, 0]


    def R2(M):
        return (-(pp / 4) * (M.T * M).trace() + sp.Rational(1, 2) * ((M * pv).T * (M * pv))[0, 0]
                - sp.Rational(1, 2) * (pv.T * M * pv)[0, 0] * M.trace() + (pp / 4) * M.trace()**2)


    # B1 relabelling invariance of R2 and transversality of its gradient
    xi = sp.Matrix(sp.symbols('x1 x2 x3', real=True))
    shift = pv * xi.T + xi * pv.T
    inv_R2 = sp.expand(R2(h + shift) - R2(h))
    inv_R1 = sp.expand(R1(shift))
    grad = sp.Matrix(3, 3, lambda i, j: sp.diff(R2(h), hv[[0, 3, 4, 3, 1, 5, 4, 5, 2][3 * i + j]])
                     * (1 if i == j else sp.Rational(1, 2)))
    transverse = sp.simplify(grad * pv)
    check("B1", inv_R2 == 0 and inv_R1 == 0 and transverse == sp.zeros(3, 1),
          "R1, R2 invariant under h -> h + p xi + xi p; p_i dR2/dh_ij = 0 (block 62 T3(b))")

    # Lagrangian on the 6 independent components (off-diagonals counted twice in traces)
    hd = sp.Matrix(sp.symbols('hd11 hd22 hd33 hd12 hd13 hd23', real=True))
    Hd = sp.Matrix([[hd[0], hd[3], hd[4]], [hd[3], hd[1], hd[5]], [hd[4], hd[5], hd[2]]])
    eu = sp.Symbol('e_u', real=True)


    def lapse_demand(beta_val):
        kin = al * (Hd * Hd).trace() + beta_val * Hd.trace()**2
        pot = K1 * u * R1(h) + K2 * R2(h) - eu * u + (a_s / 2) * (Th * h).trace()
        Mkin = sp.hessian(kin, list(hd))
        force = sp.Matrix([sp.diff(pot, c) for c in hv])
        hdd = Mkin.LUsolve(force)
        Hdd = sp.Matrix([[hdd[0], hdd[3], hdd[4]], [hdd[3], hdd[1], hdd[5]], [hdd[4], hdd[5], hdd[2]]])
        # lapse equation dL/du = K1 R1(h) - e_u = 0  =>  e_u'' = K1 R1(h'')
        return sp.simplify(K1 * R1(Hdd))


    demand = lapse_demand(-al)
    target = -(K1 * a_s / (4 * al)) * (pv.T * Th * pv)[0, 0]
    resB2 = sp.simplify(demand - target)
    check("B2", resB2 == 0 and not demand.has(K2) and not demand.has(u) and all(not demand.has(c) for c in hv),
          "at beta = -alpha: e_u'' = -(K1 a_s/(4 alpha)) p.Theta.p identically; no K2, no h, no u dependence")

    if FULL:   # slow (about 25 s); C.c4chk.B2 is the default route for this control
        demand_gen = lapse_demand(be)
        resB3 = sp.simplify(demand_gen - target)
        check("B3", resB3 != 0 and sp.simplify(resB3.subs(be, -al)) == 0,
              "control: for generic beta the identity acquires trace terms (vanishing only at beta = -alpha)")

    # B4 TT cone with K2: p along 3, h11 = -h22 = A, h12 = B
    Pz, A_, B_ = sp.symbols('P A B', real=True)
    subsTT = {p1: 0, p2: 0, p3: Pz}
    hTT = {hv[0]: A_, hv[1]: -A_, hv[2]: 0, hv[3]: B_, hv[4]: 0, hv[5]: 0}
    R2TT = sp.expand(R2(h).subs(subsTT).subs(hTT))
    kinTT = sp.expand((al * (Hd * Hd).trace() + be * Hd.trace()**2).subs(
        {hd[0]: sp.Symbol('Ad'), hd[1]: -sp.Symbol('Ad'), hd[2]: 0, hd[3]: sp.Symbol('Bd'), hd[4]: 0, hd[5]: 0}))
    MA = sp.diff(kinTT, sp.Symbol('Ad'), 2)
    QA = sp.diff(K2 * R2TT, A_, 2)
    om2 = sp.simplify(-QA / MA)
    R1TT = sp.simplify(R1(h).subs(subsTT).subs(hTT))
    check("B4", sp.simplify(om2 - K2 * Pz**2 / (4 * al)) == 0 and R1TT == 0,
          f"TT disturbance: omega^2 = {om2} (K1 does not enter: R1 vanishes on TT)")

    # B5 canonical rescaling Phi_rho (h = rho h', P = P'/rho): K1 -> rho K1, K2 -> rho^2 K2,
    #    alpha -> rho^2 alpha, a_s -> rho a_s.  Verify by substituting into the action.
    rho = sp.Symbol('rho', positive=True)
    hp, hpv = symm('hp')
    hdp = sp.Matrix(sp.symbols('hpd11 hpd22 hpd33 hpd12 hpd13 hpd23', real=True))
    Hdp = sp.Matrix([[hdp[0], hdp[3], hdp[4]], [hdp[3], hdp[1], hdp[5]], [hdp[4], hdp[5], hdp[2]]])


    def action(Hm, Hdm, k1, k2, alpha_, asv):
        return (alpha_ * (Hdm * Hdm).trace() - alpha_ * Hdm.trace()**2 + k1 * u * R1(Hm) + k2 * R2(Hm)
                + (asv / 2) * (Th * Hm).trace())


    Lold = action(rho * hp, rho * Hdp, K1, K2, al, a_s)
    Lnew = action(hp, Hdp, rho * K1, rho**2 * K2, rho**2 * al, rho * a_s)
    check("B5a", sp.expand(Lold - Lnew) == 0,
          "Phi_rho: the member+source in h = rho h' is the member+source in h' with (rho K1, rho^2 K2, rho^2 alpha, rho a_s)")
    inv = {
        'K1 a_s/alpha (lapse identity, B2)': K1 * a_s / al,
        'K2/alpha (TT cone, B4)': K2 / al,
        'K1 a_s/K2': K1 * a_s / K2,
        'K1/K2': K1 / K2,
        'a_s': a_s,
    }
    scal = {K1: rho * K1, K2: rho**2 * K2, al: rho**2 * al, a_s: rho * a_s}
    inv_status = {name: sp.simplify(expr.subs(scal, simultaneous=True) / expr) == 1 for name, expr in inv.items()}
    check("B5b", inv_status == {'K1 a_s/alpha (lapse identity, B2)': True, 'K2/alpha (TT cone, B4)': True,
                                'K1 a_s/K2': True, 'K1/K2': False, 'a_s': False},
          f"invariance under Phi_rho: {inv_status}")

    # B6 static pull with separate K1, K2 (block 62 T5(c) generalised): Theta = 0, source e on the clock.
    #    u-equation K1 R1(h) = e; h-equation K1 u grad R1 + K2 grad R2 = 0.  Isotropic representative h = 2 lam delta.
    lam_s, e_s = sp.symbols('lam e', real=True)
    hiso = {hv[0]: 2 * lam_s, hv[1]: 2 * lam_s, hv[2]: 2 * lam_s, hv[3]: 0, hv[4]: 0, hv[5]: 0}
    potS = K1 * u * R1(h) + K2 * R2(h) - e_s * u
    eqs = [sp.diff(potS, u).subs(hiso)] + [sp.expand(sp.diff(potS, c).subs(hiso)) for c in hv]
    solS = sp.solve(eqs, [lam_s, u], dict=True)
    ok6 = (len(solS) == 1 and sp.simplify(solS[0][lam_s] - e_s / (4 * K1 * pp)) == 0
           and sp.simplify(solS[0][u] + (K2 / K1) * solS[0][lam_s]) == 0)
    # matter on spatial metric delta + a_s h = (1 + 2 a_s lam) delta and clock 1 + u: gamma = a_s lam / (-u)
    gam = sp.simplify(a_s * solS[0][lam_s] / (-solS[0][u])) if ok6 else None
    gam_inv = sp.simplify(gam.subs(scal, simultaneous=True) - gam) == 0 if ok6 else False
    check("B6", ok6 and sp.simplify(gam - a_s * K1 / K2) == 0 and gam_inv,
          f"static pull: lam = e/(4 K1 p^2), u = -(K2/K1) lam; the matter's space/time curvature ratio gamma = {gam} "
          "(Phi_rho-invariant); block 62 (K1 = K2, a_s = 1) gives gamma = 1")

    if FULL:   # slow (about 40 s); C.c4chk.C1-C3 are the default route
        # ============================================================================ PART C
        print("   -- C4 runner part C: R1, R2 are the expansion of sqrt(g) R for g = delta + h (plane-wave route)")
        x1, x2, x3 = sp.symbols('y1 y2 y3', real=True)
        X3 = [x1, x2, x3]
        ep = sp.Symbol('ep')
        Amp, av = symm('A')
        # a fixed rational wave vector and rational amplitudes keep this fast and exact
        pnum = [1, 2, 2]
        phase = sum(pnum[i] * X3[i] for i in range(3))


        def sqrtgR_series(Amat):
            hx = Amat * sp.cos(phase)
            g = sp.eye(3) + ep * hx
            ginv = sp.eye(3) - ep * hx + ep**2 * hx * hx
            detg = g.det()
            sqrtg = sp.series(sp.sqrt(detg), ep, 0, 3).removeO()
            dg = [[[sp.diff(g[i, j], X3[k]) for k in range(3)] for j in range(3)] for i in range(3)]
            Gam = [[[sp.expand(sum(ginv[l, m] * (dg[m][i][j] + dg[m][j][i] - dg[i][j][m]) for m in range(3)) / 2)
                     for j in range(3)] for i in range(3)] for l in range(3)]
            Ric = 0
            for i in range(3):
                for j in range(3):
                    rij = 0
                    for l in range(3):
                        rij += sp.diff(Gam[l][i][j], X3[l]) - sp.diff(Gam[l][i][l], X3[j])
                        for m in range(3):
                            rij += Gam[l][l][m] * Gam[m][i][j] - Gam[l][j][m] * Gam[m][i][l]
                    Ric += ginv[i, j] * rij
            dens = sp.expand(sp.series(sp.expand(sqrtg * Ric), ep, 0, 3).removeO())
            return dens.coeff(ep, 1), dens.coeff(ep, 2)


        def period_average(expr):
            # average over the plane-wave phase: substitute y = (theta, 0, 0)/... -> expression depends on phase only
            th = sp.Symbol('th')
            e = sp.expand(expr.subs({x1: th, x2: 0, x3: 0}))  # phase = th since pnum[0] = 1
            return sp.simplify(sp.integrate(e, (th, 0, 2 * sp.pi)) / (2 * sp.pi))


        pnv = sp.Matrix(pnum)
        ppn = sum(c**2 for c in pnum)
        ok1, ratios = True, []
        for trial in [(1, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0), (2, -1, 3, 1, -2, 1), (1, 1, -2, 0, 1, 0)]:
            Am = sp.Matrix([[trial[0], trial[3], trial[4]], [trial[3], trial[1], trial[5]], [trial[4], trial[5], trial[2]]])
            first, second = sqrtgR_series(Am)
            R1num = ppn * Am.trace() - (pnv.T * Am * pnv)[0, 0]
            ok1 &= sp.simplify(first - R1num * sp.cos(phase)) == 0
            R2num = (-(ppn / sp.Integer(4)) * (Am.T * Am).trace() + sp.Rational(1, 2) * ((Am * pnv).T * (Am * pnv))[0, 0]
                     - sp.Rational(1, 2) * (pnv.T * Am * pnv)[0, 0] * Am.trace() + (ppn / sp.Integer(4)) * Am.trace()**2)
            avg2 = period_average(second)
            ratios.append((avg2, R2num))
        check("C1", ok1, "order-1 part of sqrt(g)R[delta + h] is R1(h) pointwise (unit coefficient), four amplitudes at p = (1,2,2)")
        # a trial with R2(A) = 0 must also have zero average (run1 harness bug: 0/0 was scored as a failure)
        rat = [sp.nsimplify(a / b) if b != 0 else ('0=0' if a == 0 else 'inf') for a, b in ratios]
        check("C2", all(r == sp.Rational(1, 2) or r == '0=0' for r in rat) and sum(r == sp.Rational(1, 2) for r in rat) >= 3,
              f"period average of the order-2 part / block-62 R2(A) = {rat} (1/2 = <cos^2>): R2 is [sqrt(g)R]^(2) of delta + h")


# =====================================================================================================================
def part_C(FULL):
    """Campaign C4 check (chk_c4.py): second routes (Jacobian corners, torus build, closed-form DeWitt inverse, variational R2)."""
    check = _checker("C.c4chk.")


    def symm(n):
        a = sp.symbols(f'{n}11 {n}22 {n}33 {n}12 {n}13 {n}23', real=True)
        return sp.Matrix([[a[0], a[3], a[4]], [a[3], a[1], a[5]], [a[4], a[5], a[2]]]), list(a)


    h, hv = symm('h')
    I3 = sp.eye(3)

    # ---------------------------------------------------------------- A: Jacobian at species corners
    print("   -- C4 check part A: walker coupling strength and species (Jacobian route)")
    B = -h / 2  # block 120 realisation at q = 0 (phi_j = 1), Lambda(B) = -(B + B^T) = h
    assert sp.simplify(-(B + B.T) - h) == sp.zeros(3, 3)
    counts = {}
    ok_forms = True
    for name in ['site', 'one', 'two']:
        n_unit = 0
        for K in itertools.product([0, 1], repeat=3):
            eta = sp.diag(*[(-1) ** c for c in K])
            # d s_a/dk_b = eta_a delta_ab ; c_a -> eta_a ; d(sin k_j)/dk = eta_j ; d(sin 2k_j /2)/dk = 1
            if name == 'site':      # v_a = s_a + sum_j B_aj s_j
                J = eta + B * eta
            elif name == 'one':     # v_a = s_a + sum_j B_aj c_a s_j
                J = eta + eta * B * eta
            else:                   # v_a = s_a + sum_j B_aj c_a P_j
                J = eta + eta * B
            form = (J.T * J).applyfunc(sp.expand)
            lin = (form - I3).applyfunc(lambda z: sum(t for t in sp.Add.make_args(sp.expand(z))
                                                       if sp.Poly(t, *hv).total_degree() == 1))
            expect = {'site': -(eta * h * eta), 'one': -(h * eta + eta * h) / 2, 'two': -h}[name]
            ok_forms &= sp.simplify(lin - expect) == sp.zeros(3, 3)
            n_unit += int(sp.simplify(lin + h) == sp.zeros(3, 3))
        counts[name] = n_unit
    check("A1", ok_forms and counts == {'site': 2, 'one': 1, 'two': 8},
          f"first-order cone at the 8 corners: site -eta h eta, one-step -sym(h eta), two-step -h; corners seeing delta+h: {counts}")

    # A2 floating torus build of the couplings from position-space operators (L = 6, uniform random B)
    L = 6
    N = L ** 3
    idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
    Tm = []
    for a in range(3):
        M = np.zeros((N, N))
        for x, y, z in itertools.product(range(L), repeat=3):
            e = [0, 0, 0]; e[a] = 1
            M[idx(x, y, z), idx(x + e[0], y + e[1], z + e[2])] = 1.0
        Tm.append(M)
    S = [(T - T.T) / 2j for T in Tm]
    C = [(T + T.T) / 2 for T in Tm]
    Pop = [S[j] @ C[j] for j in range(3)]
    sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
    rng = np.random.default_rng(7)
    Bn = rng.normal(size=(3, 3)) * 0.05
    H0 = sum(np.kron(S[a], sig[a]) for a in range(3))
    Hone = H0 + sum(np.kron(0.5 * (Bn[a, j] * C[a] @ S[j] + S[j] @ (Bn[a, j] * C[a])), sig[a]) for a in range(3) for j in range(3))
    Htwo = H0 + sum(np.kron(0.5 * (Bn[a, j] * C[a] @ Pop[j] + Pop[j] @ (Bn[a, j] * C[a])), sig[a]) for a in range(3) for j in range(3))
    okA2 = np.allclose(Hone, Hone.conj().T) and np.allclose(Htwo, Htwo.conj().T)
    # compare spectra with the symbol formula on the grid
    ev_two = np.sort(np.linalg.eigvalsh(Htwo))
    ev_one = np.sort(np.linalg.eigvalsh(Hone))
    sym_two, sym_one = [], []
    for n in itertools.product(range(L), repeat=3):
        k = 2 * np.pi * np.array(n) / L
        s, c = np.sin(k), np.cos(k)
        P = s * c
        v2 = s + np.array([sum(Bn[a, j] * c[a] * P[j] for j in range(3)) for a in range(3)])
        v1 = s + np.array([sum(Bn[a, j] * c[a] * s[j] for j in range(3)) for a in range(3)])
        sym_two += [np.linalg.norm(v2), -np.linalg.norm(v2)]
        sym_one += [np.linalg.norm(v1), -np.linalg.norm(v1)]
    okA2 &= np.allclose(ev_two, np.sort(sym_two), atol=1e-9) and np.allclose(ev_one, np.sort(sym_one), atol=1e-9)
    check("A2", okA2, "6^3 torus, position-space anticommutator couplings (blocks 64/73) with a uniform strain: hermitian, "
          "spectra equal the symbol |s + B c P| (two-step) and |s + B c s| (one-step) used in A1 (floating point, atol 1e-9)")

    # A3 block 120's compatibility <K, R G xi> = 0 is linear in R: c*R is compatible iff R is; so a_R is a stipulation
    print("[NOTE] A3 (not a computed check): compatibility <K, R G xi> is homogeneous of degree 1 in R (definition, block 120 line 67): "
          "rescaling R -> cR preserves it for every c != 0; 'Lambda R(0) = 1' (line 66) is a normalisation clause, not a consequence")

    # A4 uniform frame second order: walker cone E^T E vs matter on delta + a h with h := (E^T E)^{-1} - delta
    t = sp.Symbol('t')
    eps = sp.Matrix(3, 3, lambda i, j: sp.Rational((3 * i + 5 * j) % 7 - 3, 5))  # a fixed rational tilt
    E = I3 + t * eps
    hE = ((E.T * E).inv() - I3).applyfunc(lambda z: sp.series(z, t, 0, 3).removeO())
    asym = sp.Symbol('a')
    match = ((I3 + asym * hE).applyfunc(sp.expand) * (E.T * E)).applyfunc(lambda z: sp.expand(z))
    c1 = [sp.expand(z).coeff(t, 1) for z in match]
    sol = sp.solve([z for z in c1 if z != 0], asym, dict=True)
    check("A4", sol == [{asym: 1}] and sp.simplify(hE.applyfunc(lambda z: z.coeff(t, 1)) + eps + eps.T) == sp.zeros(3, 3),
          f"rational tilt: h = -(eps+eps^T)t + O(t^2) and unit matter coupling a = {sol}")

    # ---------------------------------------------------------------- B: lapse identity by DeWitt inverse
    print("   -- C4 check part B: member's lapse identity with K1, K2, a_s (closed-form DeWitt inverse)")
    p = sp.Matrix(sp.symbols('p1 p2 p3', real=True))
    pp = (p.T * p)[0, 0]
    K1, K2, al, be, a_s, u = sp.symbols('K1 K2 alpha beta a_s u', real=True)
    Th, _ = symm('Th')


    def R1(M):
        return pp * M.trace() - (p.T * M * p)[0, 0]


    def R2(M):
        return (-(pp / 4) * (M * M).trace() + sp.Rational(1, 2) * ((M * p).T * (M * p))[0, 0]
                - sp.Rational(1, 2) * (p.T * M * p)[0, 0] * M.trace() + (pp / 4) * M.trace() ** 2)


    def tgrad(f):
        # symmetric tensor derivative: (d f/d h_ij) with off-diagonals split equally
        m = {(0, 0): 0, (1, 1): 1, (2, 2): 2, (0, 1): 3, (0, 2): 4, (1, 2): 5}
        G = sp.zeros(3, 3)
        for i in range(3):
            for j in range(3):
                key = (min(i, j), max(i, j))
                G[i, j] = sp.diff(f, hv[m[key]]) * (1 if i == j else sp.Rational(1, 2))
        return G


    # EL for L = alpha hdot:hdot + beta (tr hdot)^2 + pot: 2 alpha hdd + 2 beta delta tr hdd = F, F = tgrad(pot)
    pot = K1 * u * R1(h) + K2 * R2(h) + (a_s / 2) * (Th * h).trace()
    F = tgrad(pot)
    trhdd = F.trace() / (2 * al + 6 * be)
    hdd = (F - 2 * be * I3 * trhdd) / (2 * al)
    dem = sp.simplify(K1 * R1(hdd))
    dem_closing = sp.simplify(dem.subs(be, -al))
    tgt = -(K1 * a_s / (4 * al)) * (p.T * Th * p)[0, 0]
    check("B1", sp.simplify(dem_closing - tgt) == 0 and not dem_closing.has(K2),
          "beta = -alpha: e_u'' = K1 R1(hdd) = -(K1 a_s/(4 alpha)) p.Theta.p; K2, u, h drop (transversality of dR2, p.(p^2-pp).p = 0)")
    check("B2", sp.simplify(dem - tgt) != 0,
          "generic beta: extra trace terms (1 + beta/alpha) p^2 tr(hdd) survive; identity is special to the closing ratio")
    # B3 consistency with the source notes: walker gives e'' = -wbar^2 p.Theta.p (wbar = 1) => K1 a_s = 4 alpha
    sol = sp.solve(sp.Eq(K1 * a_s / (4 * al), 1), K1)
    check("B3", sol == [4 * al / a_s],
          "matching the walker's exact identity (09-25 exact-lattice T1, block 134 T2) fixes K1 a_s = 4 alpha; "
          "the notes' 'alpha = K/4' is this with a_s = 1 and K := K1")
    # B4 TT cone: p = (0,0,P), h = A(e1e1 - e2e2) + Bx(e1e2 + e2e1)
    P_, A_, Bx = sp.symbols('P A Bx', real=True)
    hTT = sp.Matrix([[A_, Bx, 0], [Bx, -A_, 0], [0, 0, 0]])
    subs_p = {p[0]: 0, p[1]: 0, p[2]: P_}
    FTT = tgrad(K2 * R2(h)).subs(subs_p).subs(dict(zip(hv, [A_, -A_, 0, Bx, 0, 0])))
    # 2 alpha hdd = F (tr hdd = 0 on TT) ; F = -omega^2-independent: F = -(K2 P^2/2) h
    okTT = sp.simplify(FTT + (K2 * P_ ** 2 / 2) * hTT) == sp.zeros(3, 3)
    om2 = K2 * P_ ** 2 / (4 * al)
    okR1 = sp.simplify(R1(hTT).subs(subs_p)) == 0
    check("B4", okTT and okR1, f"TT pair: 2 alpha hdd = -(K2 P^2/2) h, omega^2 = {om2}; R1 = 0 on TT so K1 is absent")
    # B5 single light cone: with K1 a_s = 4 alpha (B3), TT speed^2 = K2/(4 alpha) = K2/(K1 a_s) -> 1 iff K2 = K1 a_s
    v2 = sp.simplify((K2 / (4 * al)).subs(al, K1 * a_s / 4))
    check("B5", sp.simplify(v2 - K2 / (K1 * a_s)) == 0,
          f"after lapse matching the TT speed^2 is {v2}: '= walker top speed' holds iff K2 = a_s K1 (gamma = 1); "
          "the notes' sentence 'at alpha = K/4 the disturbances move at the walker's top speed' uses the single-K member")
    # B6 static pull with K1 != K2: isotropic gauge h = 2 lam delta, Theta = 0, source e on the clock
    lam, e = sp.symbols('lam e', real=True)
    iso = dict(zip(hv, [2 * lam, 2 * lam, 2 * lam, 0, 0, 0]))
    potS = K1 * u * R1(h) + K2 * R2(h) - e * u
    Fs = tgrad(potS).subs(iso)
    cons = sp.diff(potS, u).subs(iso)
    sol6 = sp.solve([cons] + list(Fs), [lam, u], dict=True)
    gam = sp.simplify(a_s * sol6[0][lam] / (-sol6[0][u])) if len(sol6) == 1 else None
    check("B6", gam is not None and sp.simplify(gam - a_s * K1 / K2) == 0,
          f"static pull: lam = {sol6[0][lam] if sol6 else None}, u = {sol6[0][u] if sol6 else None}; gamma = {gam}")

    # ---------------------------------------------------------------- C: R1, R2 vs linearised Einstein tensor
    print("   -- C4 check part C: R1, R2 against the variational identity")
    # Fourier convention d -> i p. Linearised Ricci and scalar for g = delta + h:
    Ric = sp.zeros(3, 3)
    trh = h.trace()
    for i in range(3):
        for j in range(3):
            Ric[i, j] = sp.Rational(1, 2) * (-sum(p[k] * p[i] * h[k, j] for k in range(3))
                                              - sum(p[k] * p[j] * h[k, i] for k in range(3))
                                              + pp * h[i, j] + p[i] * p[j] * trh)
    Rs = sp.expand(sum(Ric[i, i] for i in range(3)))
    check("C1", sp.expand(Rs - R1(h)) == 0, "linearised scalar curvature of delta + h is R1(h) = p^2 tr h - p.h.p (unit coefficient)")
    G1 = Ric - I3 * Rs / 2
    # int [sqrt g R]^(2) = -(1/2) int h_ij G^(1)ij(h) (from d/de int sqrt g R = -int sqrt g G^ij dg_ij; the first-order
    # term of sqrt g R is a total derivative). For a real Fourier mode the quadratic symbol is -(1/2) h:G1(h).
    Q = sp.expand(-sp.Rational(1, 2) * sum(h[i, j] * G1[i, j] for i in range(3) for j in range(3)))
    check("C2", sp.expand(Q - R2(h)) == 0,
          "block 62's R2(h) = -(1/2) h:G^(1)(h): R2 is the second-order part of sqrt(g)R[delta + h] (modulo divergences) with unit coefficient")
    # C3 consequence: GR on delta + h/r gives (R1/r, R2/r^2): K1 = K r, K2 = K, K2/K1 = 1/r (B21 family), single K iff r = 1
    r, Kc = sp.symbols('r K', positive=True)
    check("C3", sp.simplify((Kc * r * R2(h / r)) / (Kc * R2(h)) - 1 / r) == 0 and sp.simplify(Kc * r * R1(h / r) - Kc * R1(h)) == 0,
          "K r sqrt(g)R[delta + h/r] = K R1 + (K/r) R2 at quadratic order: B21's one-parameter family, matter on delta + h/r has a_s = 1/r")




# =====================================================================================================================
def part_D(FULL):
    """Campaign C4b runner (c4b_closure.py): closure with the walker as matter, Fourier-kernel route."""
    check = _checker("D.c4b.")
    KE = _kernel_engine()
    COMP, Dk, EPS, ETA, G1d, G2Lie, Jv, M = KE.COMP, KE.Dk, KE.EPS, KE.ETA, KE.G1d, KE.G2Lie, KE.Jv, KE.M
    N, Pt, R3, Sv, TH, Tax, XI, ab = KE.N, KE.Pt, KE.R3, KE.Sv, KE.TH, KE.Tax, KE.XI, KE.ab
    any_of, eqs_ri, fadd, frame_sym, functional, h, independent, is_zero = KE.any_of, KE.eqs_ri, KE.fadd, KE.frame_sym, KE.functional, KE.h, KE.independent, KE.is_zero
    iso_candidates, kin0, kosmann, lapse, lb, pat, pb, restrict = KE.iso_candidates, KE.kin0, KE.kosmann, KE.lapse, KE.lb, KE.pat, KE.pb, KE.restrict
    sqrtgR_12, trh, walker, walker_cov, z0 = KE.sqrtgR_12, KE.trh, KE.walker, KE.walker_cov, KE.z0

    SEC = ["T0", "A", "B", "C", "D", "E", "G"] + (["F"] if FULL else [])
    lam1, nu, K1, K2, al, lf, v = sp.symbols("lam1 nu K1 K2 alpha lam_f v", positive=True)
    s1, s2, b, c0, beta, betap, aS = sp.symbols("s1 s2 b c0 beta betap a_s", real=True)
    R1, R2 = sqrtgR_12()
    L = lb(XI, ETA)

    # =====================================================================================================================
    if "T0" in SEC:
        F1, F2 = functional(Sv[1]), functional(Sv[2])
        ok = is_zero(fadd(pb(F1, F2), functional(Sv[3]), coeffs=[1, -2]))
        # x-dependent: {int N n, int M J_{0,0}} = -i chibar [N, M p_0 sym] chi ... = int (M d_0 N) n ... checked against hand value
        lhs = pb(functional(N * Sv[0]), functional(M * Jv[0][0]))
        ok2 = is_zero(fadd(lhs, functional(M * Dk(N, 0) * Sv[0]), coeffs=[1, 1]))
        check("T0a", ok and ok2, "spinor bracket controls: {int s_1, int s_2} = 2 int s_3 (= -i chibar[sigma1,sigma2]chi); "
              "{int N n, int M J_(0,0)} = -int M d_0N n (hand value: J_(0,0) generates -translation of density weight 1/2)")
        # flat walker algebra: {C_f[N], C_f[M]} = v^2 G_K[z0], with the Kosmann spin coefficient determined, both signs tested
        E0 = sp.eye(3)
        CN, CM = functional(walker(N, E0, v)), functional(walker(M, E0, v))
        br = pb(CN, CM)
        res = {sg: is_zero(fadd(br, functional(kosmann(z0, v ** 2, sg * sp.Rational(1, 4))), coeffs=[1, -1])) for sg in (1, -1)}
        check("T0b", res == {1: False, -1: True}, f"flat walker: {{C_f[N],C_f[M]}} = v^2 G_K[N dM - M dN] with G_K[xi] = int chibar "
              f"i(xi.d + div xi/2 + (i/4) curl xi.sigma) chi (spin term -1/4 curl xi.s; +1/4 fails): {res}  (B15 C2 analogue)")
        # gravity control
        GX, GY = functional(G1d(XI) + G2Lie(XI)), functional(G1d(ETA) + G2Lie(ETA))
        okg = is_zero(fadd(pb(GX, GY), functional(G1d(L) + G2Lie(L)), coeffs=[1, -1]))
        check("T0c", okg, "gravity control: {G_GR[xi], G_GR[eta]} = G_GR[[xi,eta]], G_GR = int Pt L_xi(delta + h)")

    # =====================================================================================================================
    # A. {C[N], G[xi]} at order chi chi (h^0): fully general constant-coefficient G_f^(0) and h-linear coupling C_f^(1)
    def gen_Gf0(xi, tag):
        unk, dens = [], 0
        for k in R3:
            for mu in range(4):
                for j in R3:
                    u = sp.Symbol(f"{tag}A_{k}{j}{mu}", real=True); unk.append(u); dens += u * xi[k] * Jv[j][mu]
                    w = sp.Symbol(f"{tag}B_{k}{j}{mu}", real=True); unk.append(w); dens += w * Dk(xi[j], k) * Sv[mu]
                z = sp.Symbol(f"{tag}C_{k}{mu}", real=True); unk.append(z); dens += z * xi[k] * Sv[mu]
        return sp.expand(dens), unk


    def gen_coup1(Lp, tag):
        unk, dens = [], 0
        for ab in COMP:
            hab = h(*ab)
            for mu in range(4):
                for k in R3:
                    e = sp.Symbol(f"{tag}e_{ab[0]}{ab[1]}{k}{mu}", real=True); unk.append(e); dens += e * hab * Jv[k][mu]
                    f = sp.Symbol(f"{tag}f_{ab[0]}{ab[1]}{k}{mu}", real=True); unk.append(f); dens += f * Dk(hab, k) * Sv[mu]
                g = sp.Symbol(f"{tag}g_{ab[0]}{ab[1]}{mu}", real=True); unk.append(g); dens += g * hab * Sv[mu]
        return sp.expand(Lp * dens), unk


    if "A" in SEC:
        kA = pat(N=1, x=1, f=2)
        E0 = sp.eye(3)
        Cf0N = functional(walker(N, E0))
        Ewalk1 = (frame_sym(1, 1) - sp.eye(3)).applyfunc(sp.expand)
        # A2: the walker's own coupling plugged in with symbolic a_s, lam1, lam_f: residual vanishes iff a_s lam1 = lam_f
        Ea = (frame_sym(aS, 1) - sp.eye(3)).applyfunc(sp.expand)
        lhs = fadd(pb(Cf0N, functional(kosmann(XI, lf)), keep=kA), pb(functional(walker(N, Ea)), functional(lam1 * G1d(XI)), keep=kA))
        rhs = functional(walker(lapse(XI, -lf, 0), E0), keep=kA)
        e2 = eqs_ri(fadd(lhs, rhs, coeffs=[1, -1]))
        s2_ = sp.solve(e2, [aS], dict=True)
        check("A2", s2_ == [{aS: lf / lam1}], f"walker coupling with free strength a_s (E = (delta + a_s h)^(-1/2)): closure at order "
              f"chi chi iff a_s = lam_f/lam1: {s2_}")
        if FULL:   # slow (about 60 s)
            # fully general ansatz: constant-coefficient G_f^(0) (84) and h-linear coupling (168)
            Gf0, uG = gen_Gf0(XI, "")
            C1d, uC = gen_coup1(N, "")
            # lam1 = 1 here: the coupling unknowns represent lam1 x (coupling coefficients)
            lhs = fadd(pb(Cf0N, functional(Gf0), keep=kA), pb(functional(C1d), functional(G1d(XI)), keep=kA))
            rhs = functional(walker(lapse(XI, s1, s2), E0), keep=kA)
            eqs = eqs_ri(fadd(lhs, rhs, coeffs=[1, -1]))
            unk = uG + uC + [s1, s2]
            print(f"   A: {len(eqs)} real equations, {len(unk)} unknowns (G_f^(0): {len(uG)}, lam1 x coupling: {len(uC)}, s1, s2)")
            # A1 decomposition of the general null space (constructive): 24 canonical redefinitions W = int h_ab S_mu
            A_, b_ = sp.linear_eq_to_matrix(eqs, unk)
            NS = A_.nullspace()
            dirs = []
            for ab in COMP:
                for mu in range(4):
                    W = functional(h(*ab) * Sv[mu])
                    eqW = eqs_ri(fadd(functional(Gf0), pb(functional(G1d(XI)), W), coeffs=[1, -1])) + \
                        eqs_ri(fadd(functional(C1d), pb(Cf0N, W), coeffs=[1, -1]))
                    sW = sp.solve(eqW, uG + uC, dict=True)
                    if len(sW) == 1:
                        dirs.append(sp.Matrix([sW[0].get(x, 0) for x in uG + uC] + [0, 0]).subs({x: 0 for x in uG + uC}))
            Dm = sp.Matrix.hstack(*dirs)
            okW = len(dirs) == 24 and Dm.rank() == 24 and (A_ * Dm).is_zero_matrix
            # remaining directions: lam_f, s2 (trh x walker density) and constant-vector phases c.curl(xi) n (non-isotropic)
            cur, extra = Dm, []
            for v_ in NS:
                t_ = sp.Matrix.hstack(cur, v_)
                if t_.rank() > cur.shape[1]:
                    cur, extra = t_, extra + [v_]
            names = [str(x) for x in unk]
            tags = []
            for v_ in extra:
                nz = {names[i] for i in range(len(unk)) if v_[i] != 0}
                tags.append("s1" if "s1" in nz else "s2" if "s2" in nz else
                            "phase" if all(n_[0] in "Bf" for n_ in nz) and any(n_.startswith("B_") and n_.endswith("0") for n_ in nz) else "?")
            print(f"   general null space {len(NS)} = 24 canonical W-directions (in null space: {okW}) + {tags}")
            check("A1a", len(NS) == 29 and okW and sorted(tags) == ["phase", "phase", "phase", "s1", "s2"],
                  "FULLY GENERAL ansatz (84 + 168 coefficients): null space 29 = 24 canonical field redefinitions chi -> exp(i k h_ab "
                  "sigma_mu) chi (W = int h_ab S_mu, constructed and verified) + lam_f (s1 direction) + s2 (trh x walker density "
                  "convention) + 3 phase rotations by c.curl(xi) with a constant vector c (not rotation invariant)")


        # A1b: SO(3)-isotropic ansatz (all invariant contractions, epsilon allowed: the Weyl field is chiral)
        fx = lambda vec: (lambda t: vec[t[0]], 1)
        fdx = lambda vec: (lambda t: Dk(vec[t[1]], t[0]), 2)
        fh = (lambda t: h(t[0], t[1]), 2)
        fdh = (lambda t: Dk(h(t[1], t[2]), t[0]), 3)
        fn = (lambda t: Sv[0], 0)
        fs = (lambda t: Sv[t[0] + 1], 1)
        fJ0 = (lambda t: Jv[t[0]][0], 1)
        fJs = (lambda t: Jv[t[0]][t[1] + 1], 2)
        Gc = []
        for fam in ([fx(XI), fJ0], [fx(XI), fJs], [fdx(XI), fn], [fdx(XI), fs], [fx(XI), fs], [fx(XI), fn]):
            Gc += iso_candidates(fam)
        Gc = [Gc[i] for i in independent(Gc)]
        Cc = []
        for fam in ([fh, fJ0], [fh, fJs], [fdh, fn], [fdh, fs], [fh, fn], [fh, fs]):
            Cc += iso_candidates(fam)
        Cc = [Cc[i] for i in independent(Cc)]
        gG = sp.symbols(f"gG0:{len(Gc)}", real=True)
        gC = sp.symbols(f"gC0:{len(Cc)}", real=True)
        GisoD = sp.expand(sum(g_ * c_ for g_, c_ in zip(gG, Gc)))
        CisoD = sp.expand(N * sum(g_ * c_ for g_, c_ in zip(gC, Cc)))
        lhs = fadd(pb(Cf0N, functional(GisoD), keep=kA), pb(functional(CisoD), functional(G1d(XI)), keep=kA))
        rhs = functional(walker(lapse(XI, s1, s2), E0), keep=kA)
        eqi = eqs_ri(fadd(lhs, rhs, coeffs=[1, -1]))
        ui = list(gG) + list(gC) + [s1, s2]
        A_i, _ = sp.linear_eq_to_matrix(eqi, ui)
        NSi = A_i.nullspace()
        # expected spanning set: (lam_f) Kosmann + walker coupling, s2: trh x walker, W_trh = int trh n (phase exp(i k trh))
        def vec_of(Gd, Cd, S1, S2):
            e_ = eqs_ri(fadd(functional(GisoD), functional(Gd), coeffs=[1, -1])) + eqs_ri(fadd(functional(CisoD), functional(Cd), coeffs=[1, -1]))
            so = sp.solve(e_, list(gG) + list(gC), dict=True)
            assert len(so) == 1
            return sp.Matrix([so[0].get(x, 0) for x in list(gG) + list(gC)] + [S1, S2]).subs({x: 0 for x in list(gG) + list(gC)})
        Wt = functional(trh * Sv[0])
        v_l = vec_of(kosmann(XI), walker(N, Ewalk1), -1, 0)
        v_s2 = vec_of(0, trh * walker(N, E0) / 2, 0, 1)
        gW = pb(functional(G1d(XI)), Wt); cW = pb(Cf0N, Wt)
        eW = eqs_ri(fadd(functional(GisoD), gW, coeffs=[1, -1])) + eqs_ri(fadd(functional(CisoD), cW, coeffs=[1, -1]))
        sWt = sp.solve(eW, list(gG) + list(gC), dict=True)
        v_W = sp.Matrix([sWt[0].get(x, 0) for x in list(gG) + list(gC)] + [0, 0]).subs({x: 0 for x in list(gG) + list(gC)})
        Vexp = sp.Matrix.hstack(v_l, v_s2, v_W)
        okI = len(NSi) == 3 and (A_i * Vexp).is_zero_matrix and Vexp.rank() == 3
        print(f"   isotropic ansatz: G_f^(0) {len(Gc)} terms, coupling {len(Cc)} terms; null space {len(NSi)}; spanned by "
              f"(lam_f: Kosmann + walker), (s2: trh walker), (W_trh): {okI}")
        check("A1b", okI, "SO(3)-isotropic ansatz (all invariant contractions incl. epsilon): the solution space is exactly 3-dim, "
              "spanned by lam_f x [Kosmann, walker coupling on E = (delta+h)^(-1/2), s1 = -1], the density convention s2 (coupling "
              "+ (s2/2) trh x walker) and the canonical phase redefinition chi -> exp(i k trh) chi.  No other coupling closes")

    # =====================================================================================================================
    # shared: isotropic h-linear fermion part of the total relabelling, G_f^(1)[xi] (Darboux variables: this is where the
    # configuration-space spin connection of the symmetric section enters, cf. 2026-09-13 native-Weyl note P1/P2)
    fx = lambda vec: (lambda t: vec[t[0]], 1)
    fdx = lambda vec: (lambda t: Dk(vec[t[1]], t[0]), 2)
    fh = (lambda t: h(t[0], t[1]), 2)
    fdh = (lambda t: Dk(h(t[1], t[2]), t[0]), 3)
    fn = (lambda t: Sv[0], 0)
    fs = (lambda t: Sv[t[0] + 1], 1)
    fJ0 = (lambda t: Jv[t[0]][0], 1)
    fJs = (lambda t: Jv[t[0]][t[1] + 1], 2)
    fP = (lambda t: Pt(t[0], t[1]), 2)


    def G1f_cands(vec):
        out = []
        for fam in ([fh, fdx(vec), fn], [fh, fdx(vec), fs], [fdh, fx(vec), fn], [fdh, fx(vec), fs], [fh, fx(vec), fJ0],
                    [fh, fx(vec), fJs], [fh, fx(vec), fs]):
            out += iso_candidates(fam)
        return out


    _G1F = {}


    def G1f_basis():
        if "idx" not in _G1F:
            _G1F["idx"] = independent(G1f_cands(XI))
        return _G1F["idx"]


    def G1f(vec, coeffs):
        c_ = G1f_cands(vec)
        return sp.expand(sum(cf * c_[i] for cf, i in zip(coeffs, G1f_basis())))


    def solve_GG(nu_):
        """{G,G} at order chi chi: lam_f^2 {K,K} + lam1({G1, G_f1} + {G_f1, G1}) = nu lam_f K[[xi,eta]].  Unknowns: lam_f and
        gp = lam1 x (G_f^(1) coefficients).  Returns list of solutions and the unknown list."""
        idx = G1f_basis()
        gp = sp.symbols(f"gp0:{len(idx)}", real=True)
        lfu = sp.Symbol("lfu", real=True)
        kxy = pat(x=1, y=1, f=2)
        KK = pb(functional(kosmann(XI)), functional(kosmann(ETA)), keep=kxy)
        X1 = pb(functional(G1d(XI)), functional(G1f(ETA, gp)), keep=kxy)
        X2 = pb(functional(G1f(XI, gp)), functional(G1d(ETA)), keep=kxy)
        KL = functional(kosmann(L), keep=kxy)
        e_ = eqs_ri(fadd(KK, X1, X2, KL, coeffs=[lfu ** 2, 1, 1, -nu_ * lfu]))
        return sp.solve(e_, [lfu] + list(gp), dict=True), lfu, gp, (KK, KL)


    if "C" in SEC:
        print(f"   G_f^(1) isotropic basis: {len(G1f_basis())} terms")
        sols, lfu, gp, (KK, KL) = solve_GG(nu)
        print(f"   {{G,G}} chi chi solutions: {sols}")
        lams = sorted({sp.simplify(s_[lfu]) for s_ in sols}, key=str)
        ok = set(lams) == {0, nu}
        s_nu = [s_ for s_ in sols if sp.simplify(s_[lfu] - nu) == 0]
        freeC = [g for g in gp if s_nu and g not in s_nu[0]]
        check("C1", ok, f"{{G,G}} at order chi chi with the h-linear fermion relabelling part G_f^(1) free (isotropic, "
              f"{len(gp)} terms): lam_f in {{0, nu}} only -> lam_f = nu (the fermion's structure constant is the common one, "
              f"as for the scalar, B19 C1b); free G_f^(1) directions at lam_f = nu: {len(freeC)}")
        # C2: without G_f^(1) (product bracket, Kosmann alone): the remainder is a pure on-site spin rotation, nonzero
        res = fadd(KK, KL, coeffs=[nu ** 2, -nu ** 2])
        nz = eqs_ri(res) != []
        # remainder equals -(1/2)... compare with the spin-1/2 note's N2 form: [L_xi, L_eta] - L_[xi,eta] = -(i/2) eps_kij (S_xi S_eta)_ij sigma_k
        Sx = [[(Dk(XI[i], j) + Dk(XI[j], i)) / 2 for j in R3] for i in R3]
        Se = [[(Dk(ETA[i], j) + Dk(ETA[j], i)) / 2 for j in R3] for i in R3]
        rot = sp.expand(sum(EPS(k, i, j) * sum(Sx[i][l] * Se[l][j] for l in R3) * Sv[k + 1] for k in R3 for i in R3 for j in R3))
        cmp_ = {cc: is_zero(fadd(res, functional(rot), coeffs=[1, -cc * nu ** 2])) for cc in (sp.Rational(1, 2), -sp.Rational(1, 2), 1, -1)}
        check("C2", nz and sum(cmp_.values()) == 1, f"product bracket without G_f^(1): {{nu K[xi], nu K[eta]}} - nu^2 K[[xi,eta]] != 0 "
              f"and equals c nu^2 int eps_kij (S_xi S_eta)_ij s_k (S = symmetric strain) for exactly one c: {cmp_} "
              f"(on-site rotation remainder, spin-1/2 note Result 4 / N2; G_f^(1) is what absorbs it)")
        _G1F["sol_nu"] = s_nu[0] if s_nu else None
        _G1F["gp"] = gp

    # =====================================================================================================================
    if "B" in SEC:
        # B1: T6c analogue for the walker. Fermion: lam_f = nu (C1), coupling FIXED to the walker's a_s = 1; gravity: G2 = nu L_xi h
        # (B21 A3 / check T3, T3G).  Unknowns lam1, K2, s1, s2.
        kh = pat(N=1, x=1, h=1)
        kA = pat(N=1, x=1, f=2)
        def joint(aval):
            Cg = functional(N * (-K1 * R1 - K2 * R2))
            Gg = functional(lam1 * G1d(XI) + nu * G2Lie(XI))
            eg = eqs_ri(fadd(pb(Cg, Gg, keep=kh), functional(lapse(XI, s1, s2) * (-K1 * R1), keep=kh), coeffs=[1, -1]))
            Ea = (frame_sym(aval, 1)).applyfunc(sp.expand)
            Cf = functional(walker(N, Ea))
            Gt = functional(lam1 * G1d(XI) + nu * G2Lie(XI) + kosmann(XI, nu))
            ef = eqs_ri(fadd(pb(Cf, Gt, keep=kA), functional(walker(lapse(XI, s1, s2), sp.eye(3)), keep=kA), coeffs=[1, -1]))
            return sp.solve(eg + ef, [lam1, K2, s1, s2], dict=True)
        sB = joint(1)
        print(f"   walker a_s = 1, lam_f = nu: {sB}")
        check("B1", sB == [{lam1: nu, K2: K1, s1: -nu, s2: 0}], "gravity's h-linear {C,G} + the walker's order-chi-chi {C,G}, "
              "with the walker's coupling FIXED at a_s = 1 (C4) and lam_f = nu (C1): unique solution lam1 = nu, K2 = K1, "
              "s1 = -nu, s2 = 0  (fermion analogue of B21-check T6c)")
        sB2 = joint(aS)
        print(f"   walker a_s free: {sB2}")
        check("B2", len(sB2) == 1 and sp.simplify(sB2[0][lam1] - nu / aS) == 0 and sp.simplify(sB2[0][K2] - aS * K1) == 0,
              "with the coupling strength a_s left free the same brackets give lam1 = nu/a_s and K2 = a_s K1: closure ties "
              "a_s = K2/K1 (C4 route II), so a_s = 1 <=> K1 = K2; with a_s free nothing fixes K2/K1 (B21 no-go, Phi_rho)")

    # =====================================================================================================================
    if "D" in SEC:
        vv = sp.Symbol("vv", real=True)
        kP = pat(N=1, M=1, P=1)
        kF = pat(N=1, M=1, f=2)
        keep = any_of(kP, kF)
        CN = fadd(functional(N * (kin0(al, b) - K1 * R1)), functional(walker(N, sp.eye(3))), coeffs=[1, 1])
        CM = fadd(functional(M * (kin0(al, b) - K1 * R1)), functional(walker(M, sp.eye(3))), coeffs=[1, 1])
        lhs = pb(CN, CM, keep=keep)
        lhs = fadd(restrict(lhs, kP), restrict(lhs, kF), coeffs=[1, vv])     # walker speed v: fermion bracket scales by v^2
        rhs = functional(c0 * (lam1 * G1d(z0) + lf * kosmann(z0)), keep=keep)
        sD = sp.solve(eqs_ri(fadd(lhs, rhs, coeffs=[1, -1])), [b, c0, vv], dict=True)
        print(f"   {{C,C}} P + chi chi: {sD}")
        ok = len(sD) == 1 and sD[0][b] == -sp.Rational(1, 2) and sp.simplify(sD[0][c0] - K1 / (4 * al * lam1)) == 0 \
            and sp.simplify(sD[0][vv] - lf * K1 / (4 * al * lam1)) == 0
        check("D1", ok, "{C,C} at order P (member) and chi chi (walker): b = -1/2, c0 = K1/(4 alpha lam1), walker speed^2 "
              "v^2 = lam_f K1/(4 alpha lam1) = a_s K1/(4 alpha) (A2).  With a_s = 1: v^2 = K1/(4 alpha) (C4 B2's lapse identity); "
              "with B1 (lam_f = lam1 = nu, K2 = K1): v^2 = K2/(4 alpha) = TT graviton cone (B21 check T2)")
        # D3: {C,C} at order P chi chi vanishes identically for the walker's coupling (ultralocal in the lapse)
        kPF = pat(N=1, M=1, P=1, f=2)
        CN1 = fadd(functional(N * kin0(al, b)), functional(walker(N, frame_sym(aS, 1))))
        CM1 = fadd(functional(M * kin0(al, b)), functional(walker(M, frame_sym(aS, 1))))
        check("D3", eqs_ri(pb(CN1, CM1, keep=kPF)) == [], "{C,C} at order P chi chi: zero identically (the walker's h-coupling "
              "has no lapse gradient), so it imposes nothing; rhs c0 G[zeta] has no P chi chi term")
        # D4 (consolidation of D1 with B2): insert the closure solution of B2 (lam_f = nu, lam1 = nu/a_s, K2 = a_s K1, a_s
        #    free) into D1's walker speed^2; the walker's own speed is 1 (block 62: H^2 = g^ij s_i s_j at the identity frame)
        if "B" in SEC:
            vB = sp.simplify(sD[0][vv].subs(lf, nu).subs(sB2[0]))
            K2B = sB2[0][K2]                              # = a_s K1 (B2): the TT coefficient on the closure solution
            okv = sp.simplify(vB - K2B / (4 * al)) == 0 and sp.simplify(vB - aS * K1 / (4 * al)) == 0
            sal = sp.solve([vB - 1], [al], dict=True)
            oka = len(sal) == 1 and sp.simplify(sal[0][al] - K2B / 4) == 0 and sp.simplify(sal[0][al] - aS * K1 / 4) == 0
            check("D4", okv and oka, f"with B2's closure solution the walker's speed^2 is v^2 = {vB} = K2/(4 alpha) = a_s K1/(4 "
                  f"alpha) (one cone for walker and TT member, every a_s); the walker's speed v = 1 then forces alpha = "
                  f"{sal[0][al] if sal else None} = K2/4 = a_s K1/4, i.e. alpha = K1/4 = K2/4 at block 62's a_s = 1")

    # =====================================================================================================================
    def gf1_from_C1():
        """G_f^(1) coefficients (as lam1 x coeff = gp) on the lam_f = nu branch of C1, remaining free gp's left symbolic."""
        if _G1F.get("sol_nu") is None:
            sols, lfu, gp, _ = solve_GG(nu)
            _G1F["sol_nu"] = [s_ for s_ in sols if sp.simplify(s_[lfu] - nu) == 0][0]
            _G1F["gp"] = gp
        sol, gp = _G1F["sol_nu"], _G1F["gp"]
        vals = [sp.expand(sol.get(g, g)) for g in gp]
        free = [g for g in gp if g not in sol]
        return vals, free




    if "E" in SEC or "F" in SEC:
        GPV, GPF = gf1_from_C1()

    if "E" in SEC:
        # E1: {C,G} at order P chi chi: {N kin0, G_f^(1)} + {kin_X[N], lam1 G1} = 0 (no P chi chi term on the right).
        #     kin_X: isotropic P h n and P h s terms (the Darboux image of the configuration-space connection in kin(pi)).
        kxc = []
        for fam in ([fP, fh, fn], [fP, fh, fs]):
            kxc += iso_candidates(fam)
        kxc = [kxc[i] for i in independent(kxc)]
        kx = sp.symbols(f"kx0:{len(kxc)}", real=True)
        KXd = lambda Lp, kv: sp.expand(Lp * sum(k_ * c_ for k_, c_ in zip(kv, kxc)))     # kv = lam1 x kin_X coefficient
        kPF = pat(N=1, x=1, P=1, f=2)
        G1fX = functional(G1f(XI, [g / lam1 for g in GPV]))
        lhs = fadd(pb(functional(N * kin0(al, -sp.Rational(1, 2))), G1fX, keep=kPF), pb(functional(KXd(N, kx)), functional(G1d(XI)), keep=kPF))
        sE = sp.solve(eqs_ri(lhs), list(kx) + GPF, dict=True)
        print(f"   {{C,G}} P chi chi: kin_X basis {len(kxc)}; solution {sE}")
        ok = len(sE) == 1 and any(sp.expand(sE[0].get(k_, k_)) != 0 for k_ in kx)
        check("E1", ok, "{C,G} at order P chi chi: solvable for the P h s / P h n cross term kin_X of the kinetic term, and kin_X "
              "is forced nonzero (its P h s part is nu^2/(32 alpha lam1^2) x [one epsilon structure], independent of the free "
              "G_f^(1) directions): the Darboux form of the symmetric-section connection term pi = P - a(h, s) (2026-09-13 note "
              "P1); a product-bracket kinetic term (kin_X = 0) does not close")
        kxv = [sp.expand(sE[0].get(k_, k_) / lam1) for k_ in kx]
        # E2: {C,C} at order h chi chi with the FULL C_tot = N(kin0 + kin_X) - K1 R1 + v walker; v^2 = c0 lam_f (D1),
        #     c0 = K1/(4 alpha lam1), lam_f = nu.  Unknowns beta, beta', a_s and the remaining G_f^(1) directions.
        khF = pat(N=1, M=1, h=1, f=2)
        cc0 = K1 / (4 * al * lam1)
        vv_ = cc0 * nu
        CtN = fadd(functional(N * (kin0(al, -sp.Rational(1, 2)) - K1 * R1) + KXd(N, kxv)), functional(walker(N, frame_sym(aS, 1))),
                   coeffs=[1, sp.sqrt(vv_)])
        CtM = fadd(functional(M * (kin0(al, -sp.Rational(1, 2)) - K1 * R1) + KXd(M, kxv)), functional(walker(M, frame_sym(aS, 1))),
                   coeffs=[1, sp.sqrt(vv_)])
        lhs = pb(CtN, CtM, keep=khF)
        zb = [sp.expand(beta * sum(h(i, j) * z0[j] for j in R3) + betap * trh * z0[i]) for i in R3]
        rhs = fadd(functional(kosmann(zb, nu), keep=khF), functional(G1f(z0, [g / lam1 for g in GPV]), keep=khF), coeffs=[cc0, cc0])
        eE2 = eqs_ri(fadd(lhs, rhs, coeffs=[1, -1]))
        sE2 = sp.solve(eE2, [beta, betap, aS] + GPF, dict=True)
        print(f"   {{C,C}} h chi chi (full C_tot): {sE2}")
        ok = len(sE2) == 1 and sp.simplify(sE2[0][aS] - nu / lam1) == 0 and sp.simplify(sE2[0][beta] + nu / lam1) == 0 \
            and sE2[0][betap] == 0
        check("E2", ok, "{C,C} at order h chi chi (full C_tot incl. kin_X from E1, G_f^(1) from C1, v^2 = c0 nu): forces "
              "a_s = nu/lam1 and the structure function zeta = c0 (delta + beta h) w with beta = -nu/lam1 = -a_s, beta' = 0, i.e. "
              "B21 A7's beta = -1/r with r = lam1/nu.  A second, independent route to a_s lam1 = nu (A2 + C1 is the first); "
              "with the walker's a_s = 1: r = 1, beta = -1 (structure function delta - h)")

    # =====================================================================================================================
    if "G" in SEC:
        # antisymmetric frame part (local rotation) and the triad route
        A = sp.Matrix(3, 3, lambda a, j: sum(EPS(a, j, k) * TH[k] for k in R3))
        divt = sum(Dk(TH[k], k) for k in R3)
        C0 = functional(walker(N, sp.eye(3)))
        kap, cc, cax = sp.symbols("kap cc c_ax", real=True)
        WA = functional(walker(N, A))
        Wr = functional(kap * sum(TH[c] * Sv[c + 1] for c in R3))
        noV = sp.solve(eqs_ri(fadd(WA, pb(C0, Wr), coeffs=[1, -1])), [kap], dict=True)
        withV = sp.solve(eqs_ri(fadd(WA, pb(C0, Wr), functional(cc * N * divt * Sv[0]), coeffs=[1, -1, -1])), [kap, cc], dict=True)
        check("G1", noV == [] and withV == [{kap: sp.Rational(1, 2), cc: sp.Rational(1, 2)}],
              f"walker on E = 1 + A, A_aj = eps_ajk theta_k: C_f[E] - C_f[1] = {{C_f[1], 1/2 int theta.s}} + 1/2 int N div(theta) n "
              f"(unique: {withV}); no spin rotation alone reproduces it ({noV}).  So the walker is NOT locally rotation covariant: "
              f"its antisymmetric frame part is a rotation of chi plus the scalar potential V = div(theta)/2")
        T1A = Tax(sp.eye(3) + A, 1)
        T1A_lin = sp.expand(sum(t_ for t_ in sp.Add.make_args(T1A) if sum(1 for s_ in t_.free_symbols if str(s_)[0] == "t") == 1
                                and sp.Poly(t_, *[s_ for s_ in t_.free_symbols if str(s_)[0] == "t"]).total_degree() == 1))
        WAc = functional(walker(N, A) + cax * N * T1A_lin * Sv[0])
        sc = sp.solve(eqs_ri(fadd(WAc, pb(C0, functional(sum(TH[c] * Sv[c + 1] for c in R3) / 2)), coeffs=[1, -1])), [cax], dict=True)
        check("G2", sp.expand(T1A_lin + 2 * divt) == 0 and sc == [{cax: sp.Rational(1, 4)}],
              f"axial scalar T(E) = eps_abc E_a^j E_b^k d_j e_ck has T^(1)(1 + A) = -2 div(theta); walker + c_ax N T n is locally "
              f"rotation covariant at first order iff c_ax = 1/4 ({sc}): this is the totally antisymmetric spin-connection term "
              f"(1/4) eps^abc omega_abc of the half-density Weyl operator, absent from the walker")
        Ts1 = Tax(frame_sym(1, 1), 1)
        z1 = eqs_ri(functional(N * Ts1 * Sv[0], keep=pat(N=1, h=1, f=2))) == []
        z2 = eqs_ri(functional(N * Tax(frame_sym(1, 2), 2) * Sv[0], keep=pat(N=1, h=2, f=2))) != []
        check("G3", z1 and z2, "symmetric section E = (delta + h)^(-1/2): T^(1) = 0 identically, so the walker EQUALS the covariant "
              "operator at O(h) (all order-chi-chi results above and the a_s = 1 of C4 hold for both); T^(2) != 0, so they differ "
              "at O(h^2) by 1/4 int N T^(2)(h) n")
        # G4: triad route at order chi chi: frame E = 1 + eps (9 comps) relabelled by its own linear shift eps_aj -> eps_aj
        #     - lam_E d_a xi_j (L_xi E at E = delta), chi by the PLAIN half-density Lie derivative plus a free spin term.
        lE, ks = sp.symbols("lam_E kappa_s", real=True)
        kA = pat(N=1, x=1, f=2)
        Dl = sp.Matrix(3, 3, lambda a, j: -lE * Dk(XI[j], a))
        curl = [sum(EPS(c, k, j) * Dk(XI[j], k) for k in R3 for j in R3) for c in R3]
        for nm, Wfun in (("walker", lambda Lp, E_: walker(Lp, E_)), ("covariant", lambda Lp, E_: walker_cov(Lp, E_, 1))):
            dC = functional(Wfun(N, sp.eye(3) + Dl), keep=kA)
            Glie = functional(lf * sum(XI[k] * Jv[k][0] for k in R3) + ks * sum(curl[c] * Sv[c + 1] for c in R3))
            lhs = fadd(dC, pb(C0, Glie, keep=kA))
            rhs = functional(walker(lapse(XI, s1, s2), sp.eye(3)), keep=kA)
            sG4 = sp.solve(eqs_ri(fadd(lhs, rhs, coeffs=[1, -1])), [lE, ks, s1, s2], dict=True)
            print(f"   G4 ({nm}): {sG4}")
            ok = sG4 == [{lE: lf, ks: 0, s1: -lf, s2: 0}]
            check(f"G4{nm[0]}", ok, f"triad route ({nm}), order chi chi: {{C_f[N], lam_E G_E + lam_f G_Lie + kappa_s int curl xi.s}} = "
                  f"C_f[N'] iff lam_E = lam_f, kappa_s = 0 (plain Lie: the frame's antisymmetric shift carries the Kosmann "
                  f"rotation; V = div curl xi /2 = 0), s1 = -lam_f, s2 = 0.  Since h = (E^T E)^-1 - delta shifts by "
                  f"lam_E (d_a xi_j + d_j xi_a), lam1 = lam_E: the triad route gives lam1 = lam_f with a_s = 1 directly")

    # =====================================================================================================================
    if "F" in SEC:
        # F: {C,G} at order h chi chi: needs the matter operator's SECOND-order frame coupling, G2 = nu L_xi h, lam_f = nu,
        #    G_f^(1) (C1 with its free directions), lapse N' = -nu xi.dN.  Witnesses in r = lam1/nu with a_s = 1/r.
        khF = pat(N=1, x=1, h=1, f=2)

        def F_run(l1, nu_, a_, cov):
            sub = {lam1: l1, nu: nu_}
            gpv = [sp.expand(g.subs(sub)) for g in GPV]
            W = walker_cov(N, frame_sym(a_, 2), 2) if cov else walker(N, frame_sym(a_, 2))
            Cf = functional(W, keep=lambda f: sum(1 for x in f if x[0] == "h") <= 2)
            Gt = functional(l1 * G1d(XI) + nu_ * G2Lie(XI) + kosmann(XI, nu_) + G1f(XI, [g / l1 for g in gpv]))
            lhs = pb(Cf, Gt, keep=khF)
            rhs = functional(walker(lapse(XI, -nu_, 0), frame_sym(a_, 1)), keep=khF)
            e_ = eqs_ri(fadd(lhs, rhs, coeffs=[1, -1]))
            return sp.solve(e_, GPF, dict=True)
        one, two, half = sp.Integer(1), sp.Integer(2), sp.Rational(1, 2)
        w1, w2 = F_run(one, one, one, False), F_run(two, one, half, False)
        c1, c2, c3 = F_run(one, one, one, True), F_run(two, one, half, True), F_run(one, one, half, True)
        print(f"   F: bare walker r=1: {w1}, r=2: {w2};  covariant r=1: {c1}, r=2: {c2}, control (lam1 = nu, a_s = 1/2): {c3}")
        check("F1", w1 == [] and w2 == [], "{C,G} at order h chi chi with the BARE walker's second-order symmetric-section "
              "coupling: NO solution for the remaining G_f^(1) directions, at r = 1 (a_s = 1) or r = 2 (a_s = 1/2).  The walker "
              "as supplied does not close beyond leading order (its missing axial term T^(2), G3)")
        check("F2", len(c1) == 1 and len(c2) == 1 and c3 == [], f"with the covariant operator (walker + 1/4 N T n): closes at r = 1 "
              f"({c1}) and r = 2 ({c2}); the mismatched control lam1 = nu, a_s = 1/2 fails ({c3})")




# =====================================================================================================================
def part_E(FULL):
    """Campaign C4b check (chk_B.py): the headline K2 = a_s K1 by an independent position-space Euler-operator engine."""
    check = _checker("E.c4bchk.")
    VE = _position_engine()
    D, Hm, LieDelta, LieH, M, N, Pdot, R3 = VE.D, VE.Hm, VE.LieDelta, VE.LieH, VE.M, VE.N, VE.Pdot, VE.R3
    SIG, bil, div_eqs, eta, hdeg_filter, hf, kosmann, pb = VE.SIG, VE.bil, VE.div_eqs, VE.eta, VE.hdeg_filter, VE.hf, VE.kosmann, VE.pb
    spinrot, sqrtgR_series, vsolve, walker, xi = VE.spinrot, VE.sqrtgR_series, VE.vsolve, VE.walker, VE.xi

    lam1, nu, K1, K2, mu, lf = sp.symbols("lam1 nu K1 K2 mu lam_f", positive=True)
    s1, s2, kap, w, q, a = sp.symbols("s1 s2 kappa w q a", real=True)
    divxi = sum(D(xi[k], k) for k in R3)
    Np = lambda S1, S2: S1 * sum(xi[k] * D(N, k) for k in R3) + S2 * N * divxi

    # ---------------------------------------------------------------- controls
    R1, R2 = sqrtgR_series(2)
    trh = sum(hf(k, k) for k in R3)
    R1hand = sum(D(D(hf(i, j), i), j) for i in R3 for j in R3) - sum(D(D(trh, k), k) for k in R3)
    check("T1", sp.expand(R1 - R1hand) == 0, "own [sqrt g R]^(1) of delta + h = d_i d_j h_ij - lap tr h")
    # linearised diffeo identity of sqrt(g) R as a density (a test of the code's R2, not an input)
    dR = hdeg_filter(pb(N * R1 + N * R2, Pdot(LieDelta(xi) + LieH(xi)), ferm=False), 1)
    idt = div_eqs(sp.expand(dR + sum(xi[k] * D(N, k) for k in R3) * R1), N)
    check("T2", idt == [], "{int N sqrt(g)R, int P L_xi(delta+h)} at O(h) = -int (xi.dN) R1 (density of weight 1): "
          "own R2 consistent with own R1")
    F1, F2 = spinrot([1, 0, 0]), spinrot([0, 1, 0])
    check("T3", div_eqs(sp.expand(N * (pb(F1, F2, grav=False) - 2 * bil(SIG[2]))), N) == [],
          "spinor bracket {int s1, int s2} = 2 int s3")
    # flat walker algebra: {C[N], C[M]} = v^2 Kosmann[w] with w = N dM - M dN, solve for weight and spin coefficient
    w0 = [sp.expand(N * D(M, k) - M * D(N, k)) for k in R3]
    E0 = sp.eye(3)
    br = pb(walker(N, E0), walker(M, E0), grav=False)
    ww, kk, cv = sp.symbols("ww kk cv", real=True)
    sol = vsolve(div_eqs(sp.expand(br - kosmann(w0, cv, ww, kk)), N), [cv, ww, kk])
    check("T4", sol == [{cv: 1, ww: sp.Rational(1, 2), kk: sp.Rational(1, 4)}],
          f"flat walker {{C[N],C[M]}} = G_K[N dM - M dN] with G_K = int chibar i(xi.d + w div xi + i kap curl xi.sigma) chi: "
          f"forces w = 1/2 (half-density) and kap = 1/4: {sol}")

    # ---------------------------------------------------------------- gravity h-linear {C, G}
    Cg = N * (-K1 * R1 - K2 * R2)
    Gg = Pdot(lam1 * LieDelta(xi) + mu * LieH(xi))
    rg = sp.expand(hdeg_filter(pb(Cg, Gg, ferm=False), 1) - Np(s1, s2) * (-K1 * R1))
    eg = div_eqs(rg, N)
    solg = vsolve(eg, [K2, s1, s2])
    check("G1", solg == [{K2: mu * K1 / lam1, s1: -mu, s2: 0}],
          f"gravity's h-linear {{C,G}} (G = lam1 G1 + mu int P L_xi h): lam1 K2 = mu K1, s1 = -mu, s2 = 0: {solg}")
    # {G,G} at order P (h^0) fixes mu to the structure constant nu
    lb = [sp.expand(sum(xi[k] * D(eta[i], k) - eta[k] * D(xi[i], k) for k in R3)) for i in R3]
    Ge = Pdot(lam1 * LieDelta(eta) + mu * LieH(eta))
    gg = hdeg_filter(pb(Gg, Ge, ferm=False), 0)
    nus = sp.Symbol("nus", real=True)
    Pr = Pdot(lam1 * LieDelta(lb))
    # compare modulo divergence: test field = xi0 (gg is linear in xi)
    sgg = vsolve(div_eqs(sp.expand(gg - nus * Pr), xi[0]), [nus])
    check("G2", sgg == [{nus: mu}] or sgg == [{nus: -mu}],
          f"{{G[xi],G[eta]}} at order P = (+-)mu lam1 G1[[xi,eta]] (sign = bracket orientation): {sgg}; so the structure "
          f"constant nu of {{G,G}} = nu G[[xi,eta]] equals mu: G2 = nu int P L_xi h is forced, not a choice")
    ORI = sgg[0][nus] / mu    # +-1: orientation of {G,G}

    # ---------------------------------------------------------------- matter {C, G} at order chi chi
    def matter_res(Ef, lam_f, wt, kp, S1, S2, Gmu=None):
        Cf = walker(N, Ef)
        G = Pdot(lam1 * LieDelta(xi)) + kosmann(xi, lam_f, wt, kp)
        r = hdeg_filter(pb(Cf, G), 0) - walker(Np(S1, S2), E0)
        return div_eqs(sp.expand(r), N)

    Ea = (sp.eye(3) - a * Hm / 2).applyfunc(sp.expand)
    ef = matter_res(Ea, lf, sp.Rational(1, 2), kap, s1, s2)
    solf = vsolve(ef, [a, s1, s2, kap])
    check("M1", solf == [{a: lf / lam1, s1: -lf, s2: 0, kap: sp.Rational(1, 4)}],
          f"walker {{C,G}} at order chi chi, frame delta - a h/2: a lam1 = lam_f, s1 = -lam_f, s2 = 0, Kosmann kap = 1/4: {solf}  "
          f"(C4b A2)")

    # ---------------------------------------------------------------- B1, B2: joint
    def joint(aval, extra_unk=()):
        efa = matter_res((sp.eye(3) - aval * Hm / 2).applyfunc(sp.expand), nu, sp.Rational(1, 2), sp.Rational(1, 4), s1, s2)
        egn = [sp.expand(e.subs(mu, nu)) for e in eg]
        return vsolve(egn + efa, [lam1, K2, s1, s2] + list(extra_unk))
    sB1 = joint(1)
    check("B1", sB1 == [{lam1: nu, K2: K1, s1: -nu, s2: 0}], f"a = 1, lam_f = nu, mu = nu: unique lam1 = nu, K2 = K1: {sB1}")
    sB2 = joint(a)
    check("B2", len(sB2) == 1 and sp.simplify(sB2[0][K2] - a * K1) == 0 and sp.simplify(sB2[0][lam1] - nu / a) == 0,
          f"a free: lam1 = nu/a, K2 = a K1: {sB2}.  Invariant content: gamma = a K1/K2 = 1 for every a")

    # ---------------------------------------------------------------- hidden-choice probes
    if FULL:   # about 15 s
        # H1: density weight of chi free (w), plus an isotropic trace coupling q trh delta in the frame (the only other
        #     isotropic no-derivative h-linear frame term); unknowns a-relation, s1, s2, kap, q
        Eq = (sp.eye(3) - a * Hm / 2 + q * trh * sp.eye(3)).applyfunc(sp.expand)
        eH1 = matter_res(Eq, lf, w, kap, s1, s2)
        sH1 = vsolve(eH1, [a, s1, s2, kap, q, w])
        print("   H1 solutions:", sH1)
        okH1 = len(sH1) == 1 and sp.simplify(sH1[0][a] - lf / lam1) == 0 and sH1[0][kap] == sp.Rational(1, 4) and sH1[0][w] == sp.Rational(1, 2) and sp.simplify(sH1[0][s2] - 2 * lam1 * q) == 0
        check("H1", okH1, f"density weight w of chi left free and a trace coupling q tr h delta added: a lam1 = lam_f survives; "
              f"w = 1/2 is FORCED (with w free sympy.solve silently drops the w-equations; vsolve back-substitutes), q only moves s2 = 2 lam1 q (density convention): {sH1}")
    # H2: G2 normalisation mu kept free in gravity (the matter side has no mu at this order): K2 = (mu/nu) a K1 ...
    egm = eg
    efa = matter_res(Ea, lf, sp.Rational(1, 2), sp.Rational(1, 4), s1, s2)
    sH2 = vsolve(egm + efa, [K2, s1, s2, a, mu])
    print("   H2 solutions:", sH2)
    okH2 = len(sH2) == 1 and sp.simplify(sH2[0][mu] - lf) == 0 and sp.simplify(sH2[0][K2] - lf * K1 / lam1) == 0 \
        and sp.simplify(sH2[0][a] - lf / lam1) == 0
    check("H2", okH2,
          f"mu, lam_f free: common lapse rule s1 = -mu = -lam_f forces mu = lam_f; K2/K1 = mu/lam1 = a.  So K2 = a K1 needs only "
          f"one common lapse rule (mu = lam_f), and {{G,G}} (G2) plus the fermion {{G,G}} (C1) both give it as nu: {sH2}")



# =====================================================================================================================
def part_E2(FULL):
    """Campaign C4b operator route (c4b_operator_route.py): one-particle operator identities on a test spinor."""
    check = _checker("E.c4bop.")

    x = sp.symbols("x0:3", real=True)
    I = sp.I
    sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    one = sp.eye(2)
    f, g = sp.Function("f")(*x), sp.Function("g")(*x)
    psi = sp.Matrix([f, g])
    Nf, Mf = sp.Function("N")(*x), sp.Function("M")(*x)
    xi = [sp.Function(f"xi{k}")(*x) for k in range(3)]
    th = [sp.Function(f"th{k}")(*x) for k in range(3)]
    hm = sp.Matrix(3, 3, lambda i, j: sp.Function(f"h{min(i, j)}{max(i, j)}")(*x))


    def d(e, k):
        return e.applyfunc(lambda z: sp.diff(z, x[k])) if isinstance(e, sp.MatrixBase) else sp.diff(e, x[k])


    def hN(Lp, E, ps, v=1):
        """h_N psi = 1/2 {Lp E_aj sigma_a, p_j} psi, p = -i d."""
        out = sp.zeros(2, 1)
        for a in range(3):
            for j in range(3):
                c = Lp * E[a, j]
                out += v * (-I / 2) * (c * sig[a] * d(ps, j) + d(c * sig[a] * ps, j))
        return out.applyfunc(sp.expand)


    def LK(vec, ps, spin):
        """Kosmann-class transport on half-densities: (vec.d + div vec / 2 + spin * i curl vec . sigma) psi."""
        div = sum(sp.diff(vec[k], x[k]) for k in range(3))
        curl = [sum(sp.LeviCivita(c, k, j) * sp.diff(vec[j], x[k]) for k in range(3) for j in range(3)) for c in range(3)]
        out = sum((vec[k] * d(ps, k) for k in range(3)), sp.zeros(2, 1)) + div / 2 * ps
        out += spin * I * sum((curl[c] * sig[c] for c in range(3)), sp.zeros(2, 2)) * ps
        return out.applyfunc(sp.expand)


    def zero(m):
        return all(sp.expand(z) == 0 for z in m)


    # O1 flat walker algebra: -i [h_N, h_M] must equal v^2 i L^K_w  => [h_N, h_M] = -v^2 L^K_w
    E0 = sp.eye(3)
    w = [sp.expand(Nf * sp.diff(Mf, x[k]) - Mf * sp.diff(Nf, x[k])) for k in range(3)]
    comm = (hN(Nf, E0, hN(Mf, E0, psi)) - hN(Mf, E0, hN(Nf, E0, psi))).applyfunc(sp.expand)
    res = {sg: zero(comm + LK(w, psi, sg * sp.Rational(1, 4))) for sg in (1, -1)}
    check("O1", res == {1: True, -1: False}, f"[h_N, h_M] = -L^K_w with spin coefficient +i/4 curl w.sigma (i.e. -1/4 curl w.s "
          f"in the bilinear, as in c4b T0b): {res}")

    # O2 order chi chi {C,G}: unknown a_s, s1, s2, spin coefficient kap; lam1, lam_f symbolic
    lam1, lf = sp.symbols("lam1 lam_f", positive=True)
    aS, s1, s2, kap = sp.symbols("a_s s1 s2 kap", real=True)
    lhs = lf * (hN(Nf, E0, LK(xi, psi, kap)) - LK(xi, hN(Nf, E0, psi), kap))
    dh = sp.Matrix(3, 3, lambda i, j: lam1 * (sp.diff(xi[j], x[i]) + sp.diff(xi[i], x[j])))
    E1 = -aS * dh / 2                     # first-order part of (delta + a_s h)^(-1/2) at h -> delta h
    lhs += hN(Nf, E1, psi)
    Np = s1 * sum(xi[k] * sp.diff(Nf, x[k]) for k in range(3)) + s2 * Nf * sum(sp.diff(xi[k], x[k]) for k in range(3))
    resid = (lhs - hN(Np, E0, psi)).applyfunc(sp.expand)
    # collect coefficients of all derivative monomials of the test and parameter functions
    eqs = []
    for comp in resid:
        comp = sp.expand(comp)
        atoms = [a_ for a_ in comp.atoms(sp.Derivative) | {f, g, Nf} | set(xi)]
        gens = sorted(set(atoms), key=str)
        P = sp.Poly(comp, *gens)
        for _, c in P.terms():
            c = sp.expand(c)
            if c != 0:
                eqs += [sp.re(c), sp.im(c)]
    eqs = [e for e in (sp.expand(e) for e in eqs) if e != 0]
    sol = sp.solve(eqs, [aS, s1, s2, kap], dict=True)
    check("O2", sol == [{aS: lf / lam1, s1: -lf, s2: 0, kap: sp.Rational(1, 4)}],
          f"operator route, order chi chi: lam_f [h_N, L_xi] + h^(1)_N[h -> lam1 (d xi + d xi^T)] = h_(N') iff "
          f"a_s = lam_f/lam1, s1 = -lam_f, s2 = 0 and the Kosmann spin coefficient (+i/4): {sol}")

    # O3 antisymmetric frame part: h_N[A] - (-i)[h_N, (1/2)(theta.s generator)]: the bilinear bracket {C_f, 1/2 int theta.s}
    #    = -i int chibar [h_N, theta.sigma/2] chi; claim  h_N[A] = -i [h_N, theta.sigma/2] + N div(theta)/2
    A = sp.Matrix(3, 3, lambda a, j: sum(sp.LeviCivita(a, j, k) * th[k] for k in range(3)))
    ths = sum((th[c] * sig[c] for c in range(3)), sp.zeros(2, 2)) / 2
    rot = (-I * (hN(Nf, E0, ths * psi) - ths * hN(Nf, E0, psi))).applyfunc(sp.expand)
    divth = sum(sp.diff(th[k], x[k]) for k in range(3))
    ok3 = zero(hN(Nf, A, psi) - rot - Nf * divth / 2 * psi)
    ok3b = not zero(hN(Nf, A, psi) - rot)
    check("O3", ok3 and ok3b, "operator route: h_N[E = 1 + A] - h_N[1] = -i[h_N, theta.sigma/2] + N div(theta)/2 exactly; the "
          "scalar remainder is nonzero (the walker is not locally rotation covariant; c4b G1)")



# =====================================================================================================================
def part_F(FULL):
    """Campaign C4b check (chk_G.py): the walker against the covariant Weyl operator built from the Levi-Civita spin connection."""
    check = _checker("F.c4bchk.")
    VE = _position_engine()
    D, EPS, F_, Hm, I, N, R3, SIG = VE.D, VE.EPS, VE.F_, VE.Hm, VE.I, VE.N, VE.R3, VE.SIG
    c, coeff_eqs, d, div_eqs, inv_series, pb, spinrot, th = VE.c, VE.coeff_eqs, VE.d, VE.div_eqs, VE.inv_series, VE.pb, VE.spinrot, VE.th
    vsolve, walker = VE.vsolve, VE.walker

    ORD = ["1"] + (["2"] if FULL else [])
    t = sp.Symbol("t")
    cax = sp.Symbol("c_ax", real=True)


    def trunc(e, order):
        e = sp.expand(e)
        return sum(e.coeff(t, k) * t ** k for k in range(order + 1))


    def trM(Mx, order):
        return Mx.applyfunc(lambda z: trunc(z, order))


    def sqrt_series(x, order):
        """(1 + x)^(1/2), x = O(t)."""
        out, term = 1, 1
        for n in range(1, order + 1):
            term = trunc(term * x, order)
            out += sp.binomial(sp.Rational(1, 2), n) * term
        return trunc(out, order)


    def pow_series(x, p, order):
        out, term = 1, 1
        for n in range(1, order + 1):
            term = trunc(term * x, order)
            out += sp.binomial(p, n) * term
        return trunc(out, order)


    def covariant_functional(E, order, sgn):
        """C_cov[N] = int sqrt(g) psibar 1/2 (N H psi + H (N psi)),  H = -i sigma_a E_a^j (d_j + Omega_j),
        Omega_j = sgn (i/4) eps_abc omega_jab sigma_c,  omega_jab = e^a_k (d_j E_b^k + Gamma^k_jl E_b^l),
        psi = g^(-1/4) chi, psibar = g^(-1/4) chibar.  E = 1 + O(t); everything truncated at t^order."""
        Ei = trM(inv_series(E, order), order)      # E^{-1}[j, a]
        e_ = Ei.T                                  # e_[a, j] = e^a_j
        g = trM(e_.T * e_, order)                  # g_ij
        gi = trM(E.T * E, order)                   # g^ij
        dete = trunc(e_.det(), order)              # sqrt(g)
        g14m = pow_series(dete - 1, -sp.Rational(1, 2), order)   # g^(-1/4) = (sqrt g)^(-1/2)
        Gam = [[[trunc(sum(gi[k, l] * (D(g[l, j], i) + D(g[l, i], j) - D(g[i, j], l)) for l in R3) / 2, order)
                 for j in R3] for i in R3] for k in R3]
        om = [[[trunc(sum(e_[a, k] * (D(E[b, k], j) + sum(Gam[k][j][l] * E[b, l] for l in R3)) for k in R3), order)
                for b in R3] for a in R3] for j in R3]       # om[j][a][b]
        Om = [sgn * I / 4 * sum(((EPS(a, b, cc) * om[j][a][b]) * SIG[cc] for a in R3 for b in R3 for cc in R3 if EPS(a, b, cc) != 0), sp.zeros(2, 2))
              for j in R3]

        def Hop(ps):
            out = sp.zeros(2, 1)
            for j in R3:
                dps = ps.applyfunc(lambda z: D(z, j)) + Om[j] * ps
                for a in R3:
                    out += -I * E[a, j] * SIG[a] * dps
            return out.applyfunc(lambda z: trunc(z, order))
        psi = sp.Matrix([g14m * c[0], g14m * c[1]]).applyfunc(lambda z: trunc(z, order))
        psib = [trunc(g14m * d[0], order), trunc(g14m * d[1], order)]
        A1 = Hop(psi)
        A2 = Hop(psi.applyfunc(lambda z: N * z))
        dens = sum(psib[al] * dete * (N * A1[al] + A2[al]) / 2 for al in range(2))
        return trunc(dens, order), (e_, om)


    def Tax(E, e_):
        return sp.expand(sum(EPS(a, b, cc) * E[a, j] * E[b, k] * D(e_[cc, k], j)
                             for a in R3 for b in R3 for cc in R3 if EPS(a, b, cc) != 0 for j in R3 for k in R3))


    nt = lambda e: sp.expand(sp.expand(e).subs(t, 1))

    if "1" in ORD:
        eps = sp.Matrix(3, 3, lambda a, j: F_(f"e{a}{j}"))
        E = (sp.eye(3) + t * eps)
        res = {}
        for sgn in (1, -1):
            cov, (e_, om) = covariant_functional(E, 1, sgn)
            cov1 = sp.expand(cov).coeff(t, 1)
            T1 = sp.expand(trunc(Tax(E, e_), 1)).coeff(t, 1)
            wk1 = sp.expand(walker(N, E)).coeff(t, 1)
            cov0 = sp.expand(cov).coeff(t, 0)
            ok0 = div_eqs(sp.expand(cov0 - walker(N, sp.eye(3))), N) == []
            r = sp.expand(cov1 - wk1 - cax * N * T1 * (d[0] * c[0] + d[1] * c[1]))
            res[sgn] = (ok0, vsolve(div_eqs(r, N), [cax]))
            print(f"   sign {sgn}: flat part = walker: {ok0}; c_ax solutions {res[sgn][1]}", flush=True)
            if sgn == 1:
                # totally antisymmetric spin connection vs T (Hehl-Datta type scalar)
                omabc = sp.expand(sum(EPS(a, b, cc) * sum(E[a, j] * om[j][b][cc] for j in R3)
                                      for a in R3 for b in R3 for cc in R3 if EPS(a, b, cc) != 0)).coeff(t, 1)
                rr = sp.Symbol("rr")
                rel = vsolve(coeff_eqs(sp.expand(omabc - rr * T1)), [rr])
                print(f"   eps_abc omega_abc (first order) = rr * T^(1): {rel}", flush=True)
        okG = res[1][0] and res[1][1] == [{cax: sp.Rational(1, 4)}] and res[-1][1] == []
        check("G2a", okG, f"general first-order frame 1 + t eps (9 free functions): covariant Weyl functional (LC spin "
              f"connection, the sign that makes it Hermitian/covariant) = walker + c_ax int N T n with c_ax = 1/4 uniquely; "
              f"other sign: no c_ax. {res}")
        check("G2b", len(rel) == 1 and rel[0][rr] != 0, f"eps_abc omega_abc = {rel[0][rr] if rel else None} x T at first order: "
              f"T is (proportional to) the totally antisymmetric part of the LC spin connection, so the 1/4 N T n term is the "
              f"Hehl-Datta-type 'axial' coupling eps^abc omega_abc to chi^dag chi (= the Weyl field's axial density)")
        # rotation defect of the bare walker (C4b G1) by direct substitution, own convention
        A = sp.Matrix(3, 3, lambda a, j: sum(EPS(a, j, k) * th[k] for k in R3))
        kap, cc_ = sp.symbols("kap cc", real=True)
        divth = sum(D(th[k], k) for k in R3)
        W1 = walker(N, A)
        rot = pb(walker(N, sp.eye(3)), spinrot(th, kap), grav=False)
        nb = d[0] * c[0] + d[1] * c[1]
        s_no = vsolve(div_eqs(sp.expand(W1 - rot), N), [kap])
        s_w = vsolve(div_eqs(sp.expand(W1 - rot - cc_ * N * divth * nb), N), [kap, cc_])
        check("G1", s_no == [] and s_w == [{kap: sp.Rational(1, 2), cc_: sp.Rational(1, 2)}],
              f"walker on E = 1 + A (A_aj = eps_ajk th_k): = {{C[1], kap int th.s}} + cc int N div(th) n with kap = cc = 1/2 "
              f"({s_w}); no pure spin rotation ({s_no})")

    if "2" in ORD:
        # symmetric section to second order: covariant functional vs walker + 1/4 N T n (C4b G3 and the operator used in F2)
        Es = (sp.eye(3) - t * Hm / 2 + sp.Rational(3, 8) * t ** 2 * Hm * Hm).applyfunc(sp.expand)
        cov, (e_, om) = covariant_functional(Es, 2, 1)
        T = trunc(Tax(Es, e_), 2)
        nb = d[0] * c[0] + d[1] * c[1]
        wk = sp.expand(walker(N, Es))
        T1c, T2c = sp.expand(T).coeff(t, 1), sp.expand(T).coeff(t, 2)
        check("G3a", T1c == 0 or coeff_eqs(T1c) == [], "symmetric section: T^(1) = 0 identically")
        r1 = sp.expand(sp.expand(cov).coeff(t, 1) - wk.coeff(t, 1))
        check("G3b", div_eqs(r1, N) == [], "symmetric section, O(h): covariant functional = bare walker")
        r2b = sp.expand(sp.expand(cov).coeff(t, 2) - wk.coeff(t, 2))
        r2c = sp.expand(r2b - sp.Rational(1, 4) * N * T2c * nb)
        nzb, nzc = div_eqs(r2b, N) != [], div_eqs(r2c, N) == []
        check("G3c", nzb and nzc, f"symmetric section, O(h^2): covariant functional != bare walker ({nzb}) and == walker + "
              f"1/4 int N T^(2) n ({nzc}): c4b's walker_cov IS the covariant Weyl operator to second order")



# =====================================================================================================================
def part_F2(FULL):
    """Campaign C4b check (chk_C_fast.py): constructed symmetric-gauge G_f^(1); next order with and without the axial term."""
    check = _checker("F.c4bchk.")
    VE = _position_engine()
    D, EPS, Hm, I, LieDelta, LieH, N, Pdot = VE.D, VE.EPS, VE.Hm, VE.I, VE.LieDelta, VE.LieH, VE.N, VE.Pdot
    R3, SIG, bil, c, coeff_eqs, d, div_eqs, eta = VE.R3, VE.SIG, VE.bil, VE.c, VE.coeff_eqs, VE.d, VE.div_eqs, VE.eta
    euler, frame_sym, hdeg_filter, hf, inv_series, kosmann, pb, vsolve = VE.euler, VE.frame_sym, VE.hdeg_filter, VE.hf, VE.inv_series, VE.kosmann, VE.pb, VE.vsolve
    walker, xi = VE.walker, VE.xi

    SEC = ["C", "F", "F1"] if FULL else []
    nb = d[0] * c[0] + d[1] * c[1]
    lb = [sp.expand(sum(xi[k] * D(eta[i], k) - eta[k] * D(xi[i], k) for k in R3)) for i in R3]
    HALF, QTR = sp.Rational(1, 2), sp.Rational(1, 4)


    def has_chi(t_):
        return any(t_.has(f) for f in c + d)


    def chi_filter(e):
        return sp.expand(sum(t_ for t_ in sp.Add.make_args(sp.expand(e)) if has_chi(t_)))


    def Asym(Xm):
        return (Xm - Xm.T) / 2


    def G_f1_BG(vec, a, nu_):
        """h-linear part of the symmetric-gauge spinor lift (times nu_), as a functional int chibar i Lambda1 chi.
        Frame E = 1 - a h/2 + O(h^2); L_xi E_a^j = xi.dE_a^j - E_a^k d_k xi^j; omega with omega E + L_xi E symmetric;
        spinor rotation dchi = (i/2) theta.sigma chi, omega_ab = eps_abk theta_k (fixed by the walker's global rotation
        covariance, chk_G G1 at uniform theta)."""
        dxi = sp.Matrix(3, 3, lambda a_, j: D(vec[j], a_))      # [a, j] = d_a xi_j
        om0 = Asym(dxi)                                           # zeroth order: omega0 - dxi symmetric
        hA = a * Hm
        LE1 = sp.Matrix(3, 3, lambda a_, j: -sum(vec[k] * D(hA[a_, j], k) for k in R3) / 2
                        + sum(hA[a_, k] * D(vec[j], k) for k in R3) / 2)      # O(h) part of L_xi E
        om1 = -Asym(-om0 * hA / 2 + LE1)
        th1 = [sp.expand(sum(EPS(k, a_, b) * om1[a_, b] for a_ in R3 for b in R3) / 2) for k in R3]
        # int chibar i (i/2) th1.sigma chi = -1/2 int th1.s
        return sp.expand(-nu_ * HALF * sum(th1[k] * bil(SIG[k]) for k in R3)), th1


    def Gtot(vec, lam1, nu_, a, lam_f, beta=1, with_f1=True):
        G = Pdot(lam1 * LieDelta(vec) + nu_ * LieH(vec)) + kosmann(vec, lam_f, HALF, QTR)
        if with_f1:
            G += beta * G_f1_BG(vec, a, nu_)[0]
        return sp.expand(G)


    if "C" in SEC:
        # th0 check: zeroth-order rotation reproduces the Kosmann spin term (1/2 curl xi)
        lf, bt = sp.symbols("lam_f beta", real=True)
        G1x, G1e = G_f1_BG(xi, 1, 1)[0], G_f1_BG(eta, 1, 1)[0]
        Gx = Pdot(LieDelta(xi) + LieH(xi))
        Ge = Pdot(LieDelta(eta) + LieH(eta))
        Kx, Ke = kosmann(xi, 1, HALF, QTR), kosmann(eta, 1, HALF, QTR)
        KK = chi_filter(hdeg_filter(pb(Kx, Ke), 0))
        X1 = chi_filter(hdeg_filter(pb(Gx, G1e) + pb(G1x, Ge), 0))
        KL = kosmann(lb, 1, HALF, QTR)
        # orientation: chk_B G2 found {G[xi], G[eta]} = + G[[xi, eta]] with [xi, eta] = lb
        r_full = sp.expand(KK + X1 - KL)
        ok1 = div_eqs(r_full, xi[0]) == []
        check("C1'", ok1, "{G[xi], G[eta]} at order chi chi with lam1 = nu = lam_f = 1 and the CONSTRUCTED symmetric-gauge "
              "G_f^(1): = Kosmann[[xi, eta]] exactly (mod divergence): the metric route closes {G,G} with no triad")
        # C1'': lam_f free, G_f^(1) scaled by beta
        r_lb = sp.expand(lf ** 2 * KK + bt * X1 - lf * KL)
        sl = vsolve(div_eqs(r_lb, xi[0]), [lf, bt])
        check("C1''", sorted([tuple(sorted(s_.items(), key=str)) for s_ in sl]) ==
              sorted([((bt, 0), (lf, 0)), ((bt, 1), (lf, 1))]),
              f"lam_f free, G_f^(1) = beta x BG: closure iff (lam_f, beta) in {{(0, 0), (nu, nu^2)}}  (nu = 1): {sl}")
        # C2': product bracket remainder vs the spin-1/2 note's on-site rotation
        Sx = [[(D(xi[i], j) + D(xi[j], i)) / 2 for j in R3] for i in R3]
        Se = [[(D(eta[i], j) + D(eta[j], i)) / 2 for j in R3] for i in R3]
        rot = sp.expand(sum(EPS(k, i, j) * sum(Sx[i][l] * Se[l][j] for l in R3) * bil(SIG[k])
                            for k in R3 for i in R3 for j in R3 if EPS(k, i, j) != 0))
        cc = sp.Symbol("cc", real=True)
        sc = vsolve(div_eqs(sp.expand(KK - KL - cc * rot), xi[0]), [cc])
        check("C2'", sc == [{cc: HALF}], f"without G_f^(1): {{K[xi],K[eta]}} - K[[xi,eta]] = cc int eps_kij (S_xi S_eta)_ij s_k, "
              f"cc = {sc} (spin-1/2 note Result 4 / N2 form); and {{G1, G_f^(1)}} terms cancel it exactly (C1')")

    if "F" in SEC or "F1" in SEC:

        def Tax(E, order):
            Ei = inv_series(E, order)
            e_ = Ei.T
            return sp.expand(sum(EPS(a_, b, cc_) * E[a_, j] * E[b, k] * D(e_[cc_, k], j)
                                 for a_ in R3 for b in R3 for cc_ in R3 if EPS(a_, b, cc_) != 0 for j in R3 for k in R3))

        def F_res(lam1, nu_, a, cov, extra=0):
            E2 = frame_sym(a, 2)
            Cf = walker(N, E2)
            if cov:
                Cf += QTR * N * hdeg_filter(Tax(E2, 2), 2) * nb
            Cf = sp.expand(sum(hdeg_filter(Cf, k) for k in (0, 1, 2)))
            G = Gtot(xi, lam1, nu_, a, nu_) + extra
            lhs = hdeg_filter(pb(Cf, G), 1)
            Npr = -nu_ * sum(xi[k] * D(N, k) for k in R3)
            rhs = hdeg_filter(walker(Npr, frame_sym(a, 1)), 1)
            return div_eqs(sp.expand(lhs - rhs), N)

    if "F" in SEC:
        one, two = sp.Integer(1), sp.Integer(2)
        out = {}
        for tag, (l1, n_, a_, cov) in {"cov r=1": (one, one, one, True), "cov r=2": (two, one, HALF, True),
                                       "bare r=1": (one, one, one, False), "bare r=2": (two, one, HALF, False)}.items():
            e_ = F_res(l1, n_, a_, cov)
            out[tag] = (len(e_) == 0)
            print(f"   F {tag}: residual equations {len(e_)}", flush=True)
        check("F2'", out["cov r=1"] and out["cov r=2"], f"{{C,G}} at order h chi chi: walker + 1/4 N T n with the constructed "
              f"symmetric-gauge G_f^(1) closes at r = 1 and r = 2 (a = 1/r) with NO free parameter: {out}")
        check("F1'", (not out["bare r=1"]) and (not out["bare r=2"]), f"bare walker with the same G_f^(1): fails at r = 1, 2: {out}")

    if "F1" in SEC:
        # own isotropic basis for an h-linear correction dG to G_f^(1) (one derivative in total, as in C4b's families)
        nfun = lambda idx: nb
        sfun = lambda idx: bil(SIG[idx[0]])
        def J(j, mu_mat):
            return sp.expand(I / 2 * sum(mu_mat[a_, b] * (d[a_] * D(c[b], j) - D(d[a_], j) * c[b]) for a_ in range(2) for b in range(2)))
        fams = [
            [("h", 2), ("dx", 2), ("n", 0)], [("h", 2), ("dx", 2), ("s", 1)], [("dh", 3), ("x", 1), ("n", 0)],
            [("dh", 3), ("x", 1), ("s", 1)], [("h", 2), ("x", 1), ("J0", 1)], [("h", 2), ("x", 1), ("Js", 2)],
            [("h", 2), ("x", 1), ("s", 1)], [("h", 2), ("x", 1), ("n", 0)]]
        def val(kind, idx):
            if kind == "h":
                return hf(idx[0], idx[1])
            if kind == "dh":
                return D(hf(idx[1], idx[2]), idx[0])
            if kind == "dx":
                return D(xi[idx[1]], idx[0])
            if kind == "x":
                return xi[idx[0]]
            if kind == "n":
                return nb
            if kind == "s":
                return bil(SIG[idx[0]])
            if kind == "J0":
                return J(idx[0], sp.eye(2))
            if kind == "Js":
                return J(idx[0], SIG[idx[1]])
        def pairings(sl):
            if not sl:
                yield []
                return
            a0 = sl[0]
            for i in range(1, len(sl)):
                for p in pairings(sl[1:i] + sl[i + 1:]):
                    yield [(a0, sl[i])] + p
        cands = []
        for fam in fams:
            n_ = sum(k for _, k in fam)
            slots = list(range(n_))
            structs = [(None, p) for p in pairings(slots)] if n_ % 2 == 0 else \
                [(tri, p) for tri in itertools.combinations(slots, 3) for p in pairings([s for s in slots if s not in tri])]
            for tri, p in structs:
                tot = 0
                for ve in (itertools.permutations(R3) if tri else [()]):
                    for vd in itertools.product(R3, repeat=len(p)):
                        v_ = [None] * n_
                        sg = 1
                        if tri:
                            sg = EPS(*ve)
                            for s_, x_ in zip(tri, ve):
                                v_[s_] = x_
                        for (p1, p2), x_ in zip(p, vd):
                            v_[p1] = v_[p2] = x_
                        term, pos = sg, 0
                        for kind, k in fam:
                            term *= val(kind, tuple(v_[pos:pos + k]))
                            pos += k
                        tot += term
                tot = sp.expand(tot)
                if tot != 0:
                    cands.append(tot)
        print(f"   own isotropic h-linear relabelling candidates: {len(cands)}", flush=True)
        gs = sp.symbols(f"g0:{len(cands)}", real=True)
        # linear in dG: only the flat walker brackets with an h-linear, P-free dG at order h chi chi
        C0 = walker(N, sp.eye(3))
        cols = [euler(hdeg_filter(pb(C0, c_, grav=False), 1), N) for c_ in cands]
        print("   per-candidate brackets done", flush=True)
        res = {}
        for tag, (l1, n_, a_, cov) in {"bare r=1": (1, 1, 1, False), "cov r=1": (1, 1, 1, True)}.items():
            Cf = walker(N, frame_sym(sp.Integer(a_), 2))
            if cov:
                Cf += QTR * N * hdeg_filter(Tax(frame_sym(sp.Integer(a_), 2), 2), 2) * nb
            G = Gtot(xi, sp.Integer(l1), sp.Integer(n_), sp.Integer(a_), sp.Integer(n_))
            lhs = hdeg_filter(pb(Cf, G), 1)
            rhs = hdeg_filter(walker(-sp.Integer(n_) * sum(xi[k] * D(N, k) for k in R3), frame_sym(sp.Integer(a_), 1)), 1)
            e_ = coeff_eqs(sp.expand(euler(sp.expand(lhs - rhs), N) + sum(g_ * col for g_, col in zip(gs, cols))))
            A_, b_ = sp.linear_eq_to_matrix(e_, gs)
            rk, rka = A_.rank(), A_.row_join(b_).rank()
            res[tag] = (rk, rka)
            print(f"   F1'' {tag}: {len(e_)} equations, rank {rk}, augmented rank {rka}", flush=True)
        check("F1''", res["bare r=1"][0] < res["bare r=1"][1] and res["cov r=1"][0] == res["cov r=1"][1],
              f"bare walker: NO correction dG in the full own isotropic h-linear basis ({len(cands)} terms, not constrained "
              f"by {{G,G}}) closes {{C,G}} at h chi chi (inconsistent system); covariant: consistent: {res}")



# =====================================================================================================================
PARTS = [
    ("A", part_A, "Result 1: Phi_rho invariance, the invariant TT cone, premises equivalent to K1 = K2 (B21 check)"),
    ("B", part_B, "Results 1-2: the walker's coupling strength, the lapse identity with K1, K2, a_s (C4 runner)"),
    ("C", part_C, "Results 1-2: second routes (C4 check)"),
    ("D", part_D, "Results 3-4: closure with the walker as matter, Fourier-kernel route (C4b runner)"),
    ("E", part_E, "Result 3: K2 = a_s K1 by the position-space route (C4b check)"),
    ("E", part_E2, "Result 3: one-particle operator identities (C4b operator route)"),
    ("F", part_F, "Result 4: the walker against the Levi-Civita covariant Weyl operator (C4b check)"),
    ("F", part_F2, "Result 4 (--full): constructed G_f^(1) and the next order (C4b check)"),
]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--full", action="store_true", help="also run the slow checks")
    ap.add_argument("--parts", default="ABCDEF", help="letters of the parts to run, e.g. A,D")
    a = ap.parse_args()
    want = set(a.parts.replace(",", "").upper())
    for letter, fn, title in PARTS:
        if letter not in want:
            continue
        if fn is part_F2 and not a.full:
            continue
        print(f"== Part {letter} [{fn.__name__}]: {title}", flush=True)
        try:
            fn(a.full)
        except Exception:
            traceback.print_exc()
            _checker(f"{letter}.")("crash", False, f"{fn.__name__} raised an exception (traceback above)")
    print("== Part Z: solve audit", flush=True)
    _checker("Z.")("audit", AUDIT["rejected"] == [] and AUDIT["solutions"] > 0,
                   f"{AUDIT['calls']} sympy.solve calls, {AUDIT['solutions']} solutions back-substituted into all their "
                   f"equations, {len(AUDIT['rejected'])} rejected")
    npass = sum(ok for _, ok in RESULTS)
    nfail = len(RESULTS) - npass
    print(f"TOTAL: PASS={npass} FAIL={nfail}  ({time.time() - T_START:.0f} s{', --full' if a.full else ''})", flush=True)
    sys.exit(0 if nfail == 0 else 1)


if __name__ == "__main__":
    main()
