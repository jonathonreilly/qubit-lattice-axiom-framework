#!/usr/bin/env python3
"""C2 (continuum, exact): does constraint closure fix the h^2 . matter^2 coupling (the seagull)?

Engine: kb.py (copied verbatim from ../B21_check/kb.py: Poisson brackets on Fourier kernels, no Euler operator).
Conventions (B19/B21): delta_xi F = {F, G[xi]};  G[xi] = int Pt^{ij} L_xi(delta+h)_ij + pi xi.d phi  (lam1 = nu = 1,
i.e. the normalisation premise r = 1 / h = g - delta of B21);  C(N) = int N [kin(P,h) - K R(h) + H0 + V1 + V2];
H0 = pi^2/2 + c/2 (d phi)^2 + mu/2 phi^2 (supplied, B14);  lapse rule N' = s1 xi.dN + s2 N d.xi (field independent).
Power counting h, P ~ eps, phi, pi ~ eps^(1/2).

Ansatz (isotropic, parity even, T even, local, with the seagull's derivative counting):
  V1 = h-linear x matter^2:  trh pi^2, trh phi^2 and every contraction of h phi phi with two derivatives anywhere
  V2 = h^2 x matter^2:       (trh)^2 pi^2, tr(hh) pi^2, the same with phi^2, and every contraction of h h phi phi with two
                             derivatives distributed over the four factors (150 candidates before rank reduction)

Sections
  S0  positive control: the covariant density pi^2/(2 sqrt g) + sqrt g (c/2 g^ij d phi d phi + mu/2 phi^2) closes {C,G}
      at orders matter^2 and h.matter^2 with N' = -xi.dN
  S1  general V1, V2, s1, s2: solve {C(N),G[xi]} = C(N') at matter^2 then at h.matter^2; compare with the covariant family
  S2  homogeneous lemma: no h^2 matter^2 density in the ansatz is invariant under the linear gauge shift (N arbitrary)
  S3  {C,C}: (a) P-free h.matter^2 with the S1 solution (structure function delta - h); (b) P.h.matter^2 with the minimal
      S1 solution and the DeWitt h-linear kinetic term
  S4  the free non-minimal direction zeta R phi^2 in {C,C} at orders matter^2 and P.matter^2: with B14's supplied H0 and no
      P-matter coupling zeta is forced to 0; with a trP phi pi coupling and a N lap(phi^2) term it is not.
Usage: python3 c2_closure.py [S0 S1 S2 S3 S4]
"""
from __future__ import annotations
import sys, os, time, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from kb import (jet, Dk, h, Pt, functional, fadd, pb, eqs_of, sqrtgR_12, COMP, HNAME, Q, ftype)

T0 = time.time()
RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} [{time.time()-T0:.0f}s] {msg}", flush=True)


R3 = range(3)
XI = [jet(f"x{k}") for k in R3]
N, M = jet("N"), jet("M")
phi, pi = jet("phi"), jet("pi")
trh = sum(h(k, k) for k in R3)
trP = sum(Pt(k, k) for k in R3)
dphi2 = sum(Dk(phi, k) ** 2 for k in R3)
# numeric rational parameter point (exact arithmetic; a second point is run in S1)
PARAMS = [(sp.Integer(1), sp.Rational(3, 7)), (sp.Rational(5, 3), sp.Rational(2, 11))]


def keep_order(nh, nP=0, extra=None):
    extra = extra or {}

    def f(fields):
        c = {}
        for x in fields:
            t = ftype(x)
            t = "m" if t in ("phi", "pi") else t
            c[t] = c.get(t, 0) + 1
        want = {"h": nh, "P": nP, "m": 2}
        want.update(extra)
        return all(c.get(k, 0) == v for k, v in want.items()) and set(c) <= set(want)
    return f


def G1d(xi):
    return sp.expand(sum(Pt(i, j) * (Dk(xi[j], i) + Dk(xi[i], j)) for i in R3 for j in R3))


def G2Lie(xi):
    return sp.expand(sum(Pt(i, j) * sum(xi[k] * Dk(h(i, j), k) + h(k, j) * Dk(xi[k], i) + h(i, k) * Dk(xi[k], j)
                                        for k in R3) for i in R3 for j in R3))


def Gm(xi):
    return sp.expand(pi * sum(xi[k] * Dk(phi, k) for k in R3))


def lapse(S1, S2):
    return sp.expand(S1 * sum(XI[i] * Dk(N, i) for i in R3) + S2 * N * sum(Dk(XI[i], i) for i in R3))


# ---------------------------------------------------------------- covariant expansions (independent of any bracket)
def cov_family(c, mu, t=0, zeta=0):
    """orders 0,1,2 in h of  (sqrt g)^t [pi^2/(2 sqrt g) + sqrt g (c/2 g^ij dphi dphi + mu/2 phi^2)] + zeta sqrt g R phi^2."""
    e = sp.Symbol("e_")
    H = sp.Matrix(3, 3, lambda i, j: h(i, j))
    gi = sp.eye(3) - e * H + e ** 2 * H * H
    detg = sp.expand((sp.eye(3) + e * H).det())
    sg = sp.series(sp.sqrt(detg), e, 0, 3).removeO()
    isg = sp.series(1 / sp.sqrt(detg), e, 0, 3).removeO()
    sgt = sp.series(detg ** (sp.Rational(1, 2) * t), e, 0, 3).removeO() if t != 0 else 1
    dp = sp.Matrix([Dk(phi, k) for k in R3])
    dens = pi ** 2 / 2 * isg + sg * (c / 2 * (dp.T * gi * dp)[0, 0] + mu / 2 * phi ** 2)
    dens = sp.expand(sp.series(sp.expand(sgt * dens), e, 0, 3).removeO())
    out = [sp.expand(dens.coeff(e, n)) for n in range(3)]
    if zeta != 0:
        R1, R2 = sqrtgR_12()
        out[1] = sp.expand(out[1] + zeta * R1 * phi ** 2)
        out[2] = sp.expand(out[2] + zeta * R2 * phi ** 2)
    return out


# ---------------------------------------------------------------- isotropic contraction enumerator
def pairings(lst):
    if not lst:
        yield []
        return
    a = lst[0]
    for i in range(1, len(lst)):
        for p in pairings(lst[1:i] + lst[i + 1:]):
            yield [(a, lst[i])] + p


def iso_terms(nh, matter, nder):
    """all contractions of nh copies of h_ab, the matter factors (names), nder derivative indices assigned to factors."""
    nf = nh + len(matter)
    out = []
    for assign in itertools.combinations_with_replacement(range(nf), nder):
        nidx = 2 * nh + nder
        for pr in pairings(list(range(nidx))):
            tot = 0
            for vals in itertools.product(R3, repeat=len(pr)):
                v = [None] * nidx
                for (a_, b_), x in zip(pr, vals):
                    v[a_] = v[b_] = x
                term = 1
                for f in range(nf):
                    al = [0, 0, 0]
                    for slot, fa in enumerate(assign):
                        if fa == f:
                            al[v[2 * nh + slot]] += 1
                    if f < nh:
                        i_, j_ = v[2 * f], v[2 * f + 1]
                        term *= jet(HNAME[(min(i_, j_), max(i_, j_))], tuple(al))
                    else:
                        term *= jet(matter[f - nh], tuple(al))
                tot += term
            out.append(sp.expand(tot))
    return out


def kernel_rows(dens_list, weight):
    rows, cols = [], {}
    for d in dens_list:
        F = functional(sp.expand(weight * d))
        row = {}
        for key, ker in F.items():
            qs = [x for x in [q for qq in Q[:len(key) - 1] for q in qq] if ker.has(x)]
            terms = sp.Poly(ker, *qs).terms() if qs else [((), ker)]
            for mon, cc in terms:
                kk = (key, tuple(zip([str(q) for q in qs], mon)))
                cols.setdefault(kk, len(cols))
                row[cols[kk]] = cc
        rows.append(row)
    Mx = sp.zeros(len(rows), len(cols))
    for r, row in enumerate(rows):
        for cidx, cc in row.items():
            Mx[r, cidx] = cc
    return Mx


def independent(cands, weight=N):
    Mx = kernel_rows(cands, weight)
    D = DomainMatrix.from_Matrix(Mx.T).convert_to(sp.QQ_I)
    _, piv = D.rref()
    return [cands[p] for p in piv]


def solve_lin(eqs, unk, domain=sp.QQ):
    A, b = sp.linear_eq_to_matrix(eqs, unk)
    Ad = DomainMatrix.from_Matrix(A).convert_to(domain)
    Aug = DomainMatrix.from_Matrix(A.row_join(b)).convert_to(domain)
    rk, rka = Ad.rank(), Aug.rank()
    if rk != rka:
        return False, None, None
    R, piv = Aug.rref()
    Rm = R.to_Matrix()
    free = [unk[j] for j in range(len(unk)) if j not in piv]
    sol = {}
    for r, j in enumerate(piv):
        sol[unk[j]] = sp.expand(Rm[r, -1] - sum(Rm[r, k] * unk[k] for k in range(len(unk)) if k not in piv))
    return True, sol, free


def same_functional(a, b, weight=N):
    return eqs_of(fadd(functional(sp.expand(weight * a)), functional(sp.expand(weight * b)), coeffs=[1, -1])) == []


SEC = sys.argv[1:] or ["S0", "S1", "S2", "S3", "S4"]
GX = None

if any(s in SEC for s in ("S0", "S1", "S3")):
    GX = functional(G1d(XI) + G2Lie(XI) + Gm(XI))

# ======================================================================================================== S0
if "S0" in SEC:
    c, mu = PARAMS[0]
    H0, V1c, V2c = cov_family(c, mu)
    C = functional(N * (H0 + V1c + V2c))
    ok = True
    for nh in (0, 1):
        kp = keep_order(nh, extra={"N": 1, "x": 1})
        lhs = pb(C, GX, keep=kp)
        rhs = functional(lapse(-1, 0) * (H0 + V1c), keep=kp)
        ok &= eqs_of(fadd(lhs, rhs, coeffs=[1, -1])) == []
    # negative control: perturb the seagull by eps trh^2 pi^2 -> must fail at h.matter^2
    Cbad = functional(N * (H0 + V1c + V2c + trh ** 2 * pi ** 2 / 5))
    kp = keep_order(1, extra={"N": 1, "x": 1})
    bad = eqs_of(fadd(pb(Cbad, GX, keep=kp), functional(lapse(-1, 0) * (H0 + V1c), keep=kp), coeffs=[1, -1])) != []
    ok &= bad
    check("S0", ok, "negative control (seagull + trh^2 pi^2/5 fails) and covariant scalar density closes {C(N),G[xi]} = C(-xi.dN) at orders matter^2 and h.matter^2 (positive "
          "control of engine + expansions)")

# ======================================================================================================== S1 / S2
if "S1" in SEC or "S2" in SEC:
    c1 = [trh * pi ** 2, trh * phi ** 2] + iso_terms(1, ["phi", "phi"], 2)
    B1 = independent(c1)
    c2 = iso_terms(2, ["pi", "pi"], 0) + iso_terms(2, ["phi", "phi"], 0) + iso_terms(2, ["phi", "phi"], 2)
    B2 = independent(c2)
    print(f"   V1 ansatz: {len(c1)} candidates -> {len(B1)} independent (with lapse weight N);  "
          f"V2 ansatz: {len(c2)} candidates -> {len(B2)} independent", flush=True)
    u = sp.symbols(f"u0:{len(B1)}")
    v = sp.symbols(f"v0:{len(B2)}")
    s1, s2 = sp.symbols("s1 s2")
    V1 = sp.expand(sum(a * b for a, b in zip(u, B1)))
    V2 = sp.expand(sum(a * b for a, b in zip(v, B2)))

if "S2" in SEC:
    G1f = functional(G1d(XI))
    kp = keep_order(1, extra={"N": 1, "x": 1})
    br = pb(functional(N * V2), G1f, keep=kp)
    ok_, sol, free = solve_lin(eqs_of(br), list(v), sp.QQ_I)
    # every surviving direction must be the zero functional
    zero = ok_ and all(same_functional(sp.expand(V2.subs(sol).subs({f: (1 if f == ff else 0) for f in free})), 0)
                       for ff in free) if free else ok_
    check("S2", ok_ and zero, f"homogeneous lemma: {{int N V2, int Pt 2 d xi}} = 0 for all N, xi forces V2 = 0 "
          f"({len(B2)}-dim independent ansatz, residual free directions {len(free) if free else 0} all null) -- there is no "
          f"linearly gauge-invariant h^2 matter^2 density with <= 2 derivatives, so V2 is fixed by V1")

if "S1" in SEC:
    for pidx, (c, mu) in enumerate(PARAMS):
        H0 = sp.expand(pi ** 2 / 2 + c / 2 * dphi2 + mu / 2 * phi ** 2)
        # order matter^2
        kp0 = keep_order(0, extra={"N": 1, "x": 1})
        Cf = functional(N * (H0 + V1 + V2))
        lhs0 = pb(Cf, GX, keep=kp0)
        rhs0 = functional(lapse(s1, s2) * H0, keep=kp0)
        ok0, sol0, free0 = solve_lin(eqs_of(fadd(lhs0, rhs0, coeffs=[1, -1])), list(u) + [s1, s2], sp.QQ_I)
        print(f"   [c={c}, mu={mu}] order matter^2: consistent={ok0}, free = {free0}, s1 = {sol0.get(s1) if ok0 else None},"
              f" s2 = {sol0.get(s2, s2) if ok0 else None}", flush=True)
        # order h.matter^2 with the order-0 solution (free parameters kept symbolic)
        kp1 = keep_order(1, extra={"N": 1, "x": 1})
        V1s = sp.expand(V1.subs(sol0))
        s1s, s2s = sp.sympify(sol0.get(s1, s1)), sp.sympify(sol0.get(s2, s2))
        Cf1 = functional(N * (H0 + V1s + V2))
        lhs1 = pb(Cf1, GX, keep=kp1)
        rhs1 = functional(lapse(s1s, s2s) * V1s, keep=kp1)
        fr = [x for x in free0]
        dom = sp.QQ_I.frac_field(*fr) if fr else sp.QQ_I
        ok1, sol1, free1 = solve_lin(eqs_of(fadd(lhs1, rhs1, coeffs=[1, -1])), list(v), dom)
        print(f"   [c={c}, mu={mu}] order h.matter^2: consistent={ok1}, free V2 directions = {free1}", flush=True)
        V2s = sp.expand(V2.subs(sol1)) if ok1 else None
        nullfree = ok1 and all(same_functional(sp.expand(sp.diff(V2s, f)), 0) for f in free1)
        # identify the family: t (density weight) and zeta (R phi^2)
        t, z = sp.symbols("t zeta")
        H0c, V1c, V2c = cov_family(c, mu)
        Fv1 = fadd(functional(N * V1s), functional(N * V1c), coeffs=[1, -1])
        # fit V1s - V1c = t/2 trh H0 + zeta R1 phi^2 with t, zeta linear in the free u's
        R1, R2 = sqrtgR_12()
        fitF = fadd(Fv1, functional(N * sp.expand(t / 2 * trh * H0 + z * R1 * phi ** 2)), coeffs=[1, -1])
        solfit = sp.solve(eqs_of(fitF), [t, z] + fr, dict=True)
        print(f"   [c={c}, mu={mu}] V1 = covariant stress + (t/2) trh H0 + zeta R1 phi^2 with {solfit}", flush=True)
        okfam = len(solfit) == 1
        if okfam:
            sf = solfit[0]
            # express t and zeta through the free parameters; check s2 = t, s1 = -1, and V2 = covariant family order 2
            tt, zz = sp.sympify(sf.get(t, t)), sp.sympify(sf.get(z, z))
            cov = cov_family(c, mu, t=sp.Symbol("tw"), zeta=0)
            # (sqrt g)^t expansion with symbolic t: rebuild via series in e with symbolic exponent
            e = sp.Symbol("e_")
            Hm = sp.Matrix(3, 3, lambda i, j: h(i, j))
            detg = sp.expand((sp.eye(3) + e * Hm).det())
            sgt = sp.expand(sp.series(sp.exp(tt / 2 * sp.log(detg)), e, 0, 3).removeO())
            base = H0c + e * V1c + e ** 2 * V2c
            full = sp.expand(sgt * base)
            # (sqrt g)^t multiplies the zeta term too: its order-2 part is zeta (R2 + t/2 trh R1) phi^2
            V2fam = sp.expand(full.coeff(e, 2) + zz * (R2 + tt / 2 * trh * R1) * phi ** 2)
            V1fam = sp.expand(full.coeff(e, 1) + zz * R1 * phi ** 2)
            okv1 = same_functional(V1s, V1fam)
            okv2 = same_functional(V2s, V2fam)
            oks = sp.simplify(s1s + 1) == 0 and sp.simplify(s2s - tt) == 0
            print(f"   t = {tt}, zeta = {zz}; s1 = {s1s}, s2 = {s2s}; V1 = family: {okv1}; V2 = family: {okv2}", flush=True)
            okfam = okv1 and okv2 and oks
        check(f"S1.{pidx}", ok0 and ok1 and nullfree and okfam and len(fr) == 2,
              f"[c={c}, mu={mu}] {{C,G}} at matter^2 + h.matter^2 over the general ansatz: solution space is exactly the "
              f"2-parameter covariant family (density weight t <-> s2 = t, non-minimal zeta R phi^2), s1 = -1, and V2 is "
              f"uniquely the second-order expansion of (sqrt g)^t H_m(g) + zeta sqrt g R phi^2 (no free V2 direction)")
        if pidx == 0:
            SOL_MIN = (H0, sp.expand(V1s.subs({f: 0 for f in fr})), sp.expand(V2s.subs({f: 0 for f in fr})), c, mu,
                       (sp.expand(V1s), sp.expand(V2s), fr, solfit[0] if okfam else None))

# ======================================================================================================== S3
if "S3" in SEC:
    if "S1" not in SEC:
        print("   S3 needs S1 (run together)")
    else:
        H0, V1m, V2m, c, mu, _ = SOL_MIN
        # at the zero point of the free parameters the S1 solution must be the minimal covariant one (t = zeta = 0)
        _, V1c, V2c = cov_family(c, mu)
        print(f"   minimal point: V1 = cov {same_functional(V1m, V1c)}, V2 = cov {same_functional(V2m, V2c)}")
        al, K = sp.Rational(1, 4) * 1, sp.Integer(1)   # GR units: 16 pi G = 1 -> alpha = 1/4, K = 1;  cone c = K/(4 alpha) = 1
        # only c = 1 is consistent with the cone (B14); S3 uses PARAMS[0] which has c = 1
        trPP = sp.expand(sum(Pt(i, j) * Pt(j, i) for i in R3 for j in R3))
        kin0 = sp.expand((trPP - trP ** 2 / 2) / (4 * al))
        # DeWitt h-linear part of (1/sqrt g)(g g P P - (gP)^2/2): direct expansion
        e = sp.Symbol("e_")
        Hm = sp.Matrix(3, 3, lambda i, j: h(i, j))
        Pm = sp.Matrix(3, 3, lambda i, j: Pt(i, j))
        g = sp.eye(3) + e * Hm
        isq = sp.series(1 / sp.sqrt(sp.expand(g.det())), e, 0, 2).removeO()
        gP = g * Pm
        kin1 = sp.expand(sp.expand(isq * ((gP * gP).trace() - gP.trace() ** 2 / 2)).coeff(e, 1) / (4 * al))
        R1, R2 = sqrtgR_12()
        C_N = functional(N * (kin0 + kin1 - K * R1 - K * R2 + H0 + V1m + V2m))
        C_M = functional(M * (kin0 + kin1 - K * R1 - K * R2 + H0 + V1m + V2m))
        z0 = [sp.expand(N * Dk(M, i) - M * Dk(N, i)) for i in R3]
        beta, c0 = sp.symbols("beta c0")
        zs = [sp.expand(c0 * (z0[i] + beta * sum(h(i, j) * z0[j] for j in R3))) for i in R3]

        def Gfull(vec):
            return sp.expand(sum(Pt(i, j) * (Dk(vec[j], i) + Dk(vec[i], j)) for i in R3 for j in R3)
                             + sum(Pt(i, j) * sum(vec[k] * Dk(h(i, j), k) + h(k, j) * Dk(vec[k], i) + h(i, k) * Dk(vec[k], j)
                                                   for k in R3) for i in R3 for j in R3)
                             + pi * sum(vec[k] * Dk(phi, k) for k in R3))
        # (a) P-free, matter^2 and h.matter^2
        oka = True
        sols = []
        alleq = []
        for nh in (0, 1):
            kp = keep_order(nh, extra={"N": 1, "M": 1})
            lhs = pb(C_N, C_M, keep=kp)
            rhs = functional(Gfull(zs), keep=kp)
            eqs = eqs_of(fadd(lhs, rhs, coeffs=[1, -1]))
            alleq += eqs
            s = sp.solve(alleq, [c0, beta], dict=True)
            sols.append(s)
        print(f"   {{C,C}} P-free: matter^2 -> {sols[0]};  h.matter^2 (with c0 from matter^2) -> {sols[1]}")
        oka = sols[0] == [{c0: 1}] or (len(sols[0]) == 1 and sols[0][0].get(c0) == 1)
        oka = oka and sols[1] == [{c0: 1, beta: -1}]
        check("S3a", oka, "{C,C} P-free with the S1 (minimal) coupling: matter^2 gives c0 = K/(4 alpha) = 1, h.matter^2 gives "
              "structure function delta - h (beta = -1); V2 does not enter this sector")
        # (b) P.h.matter^2: must close with the same G[zeta] (which has no P.matter^2 or P.h.matter^2 part)
        kp = keep_order(1, nP=1, extra={"N": 1, "M": 1})
        lhs = pb(C_N, C_M, keep=kp)
        rhs = functional(Gfull([sp.expand(z0[i] - sum(h(i, j) * z0[j] for j in R3)) for i in R3]), keep=kp)
        okb = eqs_of(fadd(lhs, rhs, coeffs=[1, -1])) == []
        # and the same sector is blind to the h-underived part of V2 (it only sees derivative-on-h terms)
        check("S3b", okb, "{C,C} at P.h.matter^2 closes identically for the minimal S1 solution with the DeWitt h-linear "
              "kinetic term: no new condition on the seagull (ultralocal-in-h couplings give lapse-symmetric terms)")

# ======================================================================================================== S4
if "S4" in SEC:
    # zeta sector, linearised in the non-minimal amplitude (eps): unknowns at O(eps) are zeta, the h-linear coupling V1',
    # w trP phi pi, cp N lap(phi^2), phi^2 (y1 trPP + y2 trP^2).  Brackets: {C,G} at matter^2 and {C,C} at matter^2 and
    # P.matter^2 (V1 feeds the latter through {V1, kin0}).  c = 1 (cone), alpha = 1/4, K = 1, s1 = -1, s2 = 0.
    al, K = sp.Rational(1, 4), sp.Integer(1)
    trPP = sp.expand(sum(Pt(i, j) * Pt(j, i) for i in R3 for j in R3))
    kin0 = sp.expand((trPP - trP ** 2 / 2) / (4 * al))
    R1, R2 = sqrtgR_12()
    ep = sp.Symbol("ep")
    mu = sp.Rational(3, 7)
    H0c, V1c, _ = cov_family(sp.Integer(1), mu)
    c1 = [trh * pi ** 2, trh * phi ** 2] + iso_terms(1, ["phi", "phi"], 2)
    B1 = independent(c1)
    up = sp.symbols(f"up0:{len(B1)}")
    w, cp, y1, y2 = sp.symbols("w cp y1 y2")
    z0 = [sp.expand(N * Dk(M, i) - M * Dk(N, i)) for i in R3]
    Gz = sp.expand(sum(Pt(i, j) * (Dk(z0[j], i) + Dk(z0[i], j)) for i in R3 for j in R3)
                   + pi * sum(z0[k] * Dk(phi, k) for k in R3))
    lap_phi2 = sp.expand(sum(Dk(Dk(phi ** 2, k), k) for k in R3))
    GXs = functional(G1d(XI) + G2Lie(XI) + Gm(XI))

    def run(with_mix):
        V1p = sp.expand(sum(a * b for a, b in zip(up, B1)))
        H0 = sp.expand(H0c + ep * (cp * lap_phi2 if with_mix else 0))
        W = sp.expand(ep * (w * trP * phi * pi + phi ** 2 * (y1 * trPP + y2 * trP ** 2))) if with_mix else 0
        dens = kin0 - K * R1 + H0 + V1c + ep * V1p + W
        eqs = []
        kp = keep_order(0, extra={"N": 1, "x": 1})
        Cf = functional(N * dens)
        r = fadd(pb(Cf, GXs, keep=kp), functional(lapse(-1, 0) * H0, keep=kp), coeffs=[1, -1])
        eqs += [sp.expand(e).coeff(ep, 1) for e in eqs_of(r)]
        CN, CM = Cf, functional(M * dens)
        for nP in (0, 1):
            kp = keep_order(0, nP=nP, extra={"N": 1, "M": 1})
            r = fadd(pb(CN, CM, keep=kp), functional(Gz, keep=kp), coeffs=[1, -1])
            eqs += [sp.expand(e).coeff(ep, 1) for e in eqs_of(r)]
        eqs = [e for e in eqs if e != 0]
        unk = list(up) + ([w, cp, y1, y2] if with_mix else [])
        ok_, sol, free = solve_lin(eqs, unk, sp.QQ_I)
        if not ok_:
            return ok_, None, None, None
        V1s = sp.expand(sum(a * b for a, b in zip(up, B1)).subs(sol))
        return ok_, sol, free, V1s
    oka_, sa, fa, Va = run(False)
    okb_, sb, fb, Vb = run(True)
    print(f"   B14-style (no P-matter coupling, H0 supplied): consistent={oka_}, free O(eps) directions = {fa}")
    print(f"   with w trP phi pi + cp N lap(phi^2) + phi^2 (y1 trPP + y2 trP^2): consistent={okb_}, free = {fb}")
    oka = oka_ and fa == [] and same_functional(Va, 0)
    okb = okb_ and fb is not None and len(fb) == 1
    if okb:
        f0 = fb[0]
        one = {f0: 1}
        V1one = sp.expand(Vb.subs(one))
        # identify V1' = zeta R1 phi^2 + cp x (h-linear part of d_i(sqrt g g^ij d_j phi^2))
        e = sp.Symbol("e_")
        Hm = sp.Matrix(3, 3, lambda i, j: h(i, j))
        detg = sp.expand((sp.eye(3) + e * Hm).det())
        sg = sp.series(sp.sqrt(detg), e, 0, 2).removeO()
        gi = sp.eye(3) - e * Hm
        dphi2v = [Dk(phi ** 2, k) for k in R3]
        divv = sp.expand(sum(Dk(sp.expand(sg * sum(gi[i, j] * dphi2v[j] for j in R3)), i) for i in R3))
        div1 = sp.expand(divv.coeff(e, 1))
        zt = sp.Symbol("zt")
        cpv, wv, y1v, y2v = [sp.sympify(sb[x_]).subs(one) if x_ in sb else (1 if x_ == f0 else 0) for x_ in (cp, w, y1, y2)]
        fit = sp.solve(eqs_of(fadd(functional(N * V1one), functional(N * sp.expand(zt * R1 * phi ** 2 + cpv * div1)),
                                   coeffs=[1, -1])), [zt], dict=True)
        print(f"   free direction normalised: cp = {cpv}, w = {wv}, y1 = {y1v}, y2 = {y2v}; V1' = zeta R1 phi^2 + cp [d(sqrt g g dphi^2)]^(1)"
              f" with {fit}")
        if len(fit) == 1:
            zv = fit[0][zt]
            # Jordan-frame prediction (independent): g~ = (1 - 2 s phi^2) g, N~ = (1 - s phi^2) N  =>
            # zeta = 2 s K, cp = -4 s K, w = 4 s, y1 = 2 s, y2 = -s  (K = 1, alpha = 1/4)
            sv = zv / 2
            okb = all(sp.simplify(a_ - b_) == 0 for a_, b_ in ((cpv, -4 * sv), (wv, 4 * sv), (y1v, 2 * sv), (y2v, -sv)))
        else:
            okb = False
    check("S4", oka and okb, "non-minimal direction (linearised): with B14's supplied H0 and no P-matter coupling the "
          "brackets {C,G} matter^2 + {C,C} matter^2, P.matter^2 force it to zero; admitting trP phi pi, N lap(phi^2), "
          "phi^2 P^2 leaves exactly one free direction = the Jordan-frame map of the minimal theory "
          "(g~ = (1-2s phi^2) g, N~ = (1-s phi^2) N): zeta = 2s, cp = -4s, w = 4s, y1 = 2s, y2 = -s")

print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}  ({time.time()-T0:.0f}s)")
