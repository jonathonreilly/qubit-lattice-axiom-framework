#!/usr/bin/env python3
"""C4b: closure of the curvature member with the repo's walker (frame-coupled Weyl half-density) as the matter sector.

Continuum, flat background, leading orders.  Engine: ../B21_check/kb.py (Fourier kernels) + c4b_core spinor extension.
Usage: python3 c4b_closure.py [sections]   sections from T0 A B C D E G F (default: all)
"""
from __future__ import annotations
import sys, random
from c4b_core import *

SEC = sys.argv[1:] or ["T0", "A", "B", "C", "D", "E", "G", "F"]
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
    Gf0, uG = gen_Gf0(XI, "")
    C1d, uC = gen_coup1(N, "")
    E0 = sp.eye(3)
    Cf0N = functional(walker(N, E0))
    # lam1 = 1 here: the coupling unknowns represent lam1 x (coupling coefficients)
    lhs = fadd(pb(Cf0N, functional(Gf0), keep=kA), pb(functional(C1d), functional(G1d(XI)), keep=kA))
    rhs = functional(walker(lapse(XI, s1, s2), E0), keep=kA)
    eqs = eqs_ri(fadd(lhs, rhs, coeffs=[1, -1]))
    unk = uG + uC + [s1, s2]
    print(f"   A: {len(eqs)} real equations, {len(unk)} unknowns (G_f^(0): {len(uG)}, lam1 x coupling: {len(uC)}, s1, s2)")
    Ewalk1 = (frame_sym(1, 1) - sp.eye(3)).applyfunc(sp.expand)
    # A2: the walker's own coupling plugged in with symbolic a_s, lam1, lam_f: residual vanishes iff a_s lam1 = lam_f
    Ea = (frame_sym(aS, 1) - sp.eye(3)).applyfunc(sp.expand)
    lhs = fadd(pb(Cf0N, functional(kosmann(XI, lf)), keep=kA), pb(functional(walker(N, Ea)), functional(lam1 * G1d(XI)), keep=kA))
    rhs = functional(walker(lapse(XI, -lf, 0), E0), keep=kA)
    e2 = eqs_ri(fadd(lhs, rhs, coeffs=[1, -1]))
    s2_ = sp.solve(e2, [aS], dict=True)
    check("A2", s2_ == [{aS: lf / lam1}], f"walker coupling with free strength a_s (E = (delta + a_s h)^(-1/2)): closure at order "
          f"chi chi iff a_s = lam_f/lam1: {s2_}")
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

total()
