#!/usr/bin/env python3
"""Fresh-context check of B21 (K1 = K2?) on the Fourier-kernel bracket path of kb.py.  Imports nothing from B21/B19.

Usage: python3 chk_b21.py [sections]   sections from T0 T1 T2 T3 T3G T4 T5 T6 T7 (default: all)
"""
from __future__ import annotations
import sys, os, time, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from kb import (jet, Dk, h, Pt, functional, fadd, pb, eqs_of, pattern, restrict, sqrtgR_12, COMP, PNAME, HNAME, Q)

T0 = time.time()
RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} [{time.time()-T0:.0f}s] {msg}", flush=True)


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


SEC = sys.argv[1:] or ["T0", "T1", "T2", "T3", "T3G", "T4", "T5", "T6", "T7"]

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

print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}  ({time.time()-T0:.0f}s)")
