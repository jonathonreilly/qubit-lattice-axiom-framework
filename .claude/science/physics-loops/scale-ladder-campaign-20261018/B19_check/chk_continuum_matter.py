#!/usr/bin/env python3
"""B19 check, matter sectors and the chain (fresh code; Fourier-kernel zero test, sympy euler_equations).

M1  {G,G}: lam G_m closes with structure const nu iff lam in {0,nu}; gravity lam1 G1 + lam2 G2 (Lie) closes iff lam2 = nu, lam1 free;
    Maxwell G_L closes; G_c closes mod Gauss[-xi^i eta^j F_ij].
M5  {C(N),C(M)} at O(eps), C = kin - K1 R1 + H_m + H_A: RHS lam1 G1 + lam_m G_m + lam_A G_c [chi_kl (N d_l M - M d_l N)] (general chi matrix)
    + Gauss[d . (N dM - M dN) A]: forces chi = K1/(4 alpha lam1) delta and v_s^2 = lam_s K1/(4 alpha lam1).
M6  {C_s(N), lam1 G1 + lam_s G_s} at O(matter^2, h^0) with a GENERAL coupling (scalar 120 coeffs incl. d h phi dphi and pi dphi;
    Maxwell 126 coeffs = all quadratics in (E,F) per strain component), general lapse N' (18), general G_s[B N xi] and
    general Gauss multipliers: S1 = -lam_s delta forced; S2 tied to the coupling's trace.
J   joint: gravity (isotropic G2) + scalar + Maxwell, ONE N': forces lam_m = lam_A = lam1 K2/K1, S2 = 0 and then (M5)
    v_m^2 = v_A^2 = K2/(4 alpha) = TT graviton speed^2; three random rational parameter points, exact.
K12d gravity with a trace-reweighted constraint C_g -> C_g - t K1 trh R1 (a field-dependent lapse redefinition): S1 unchanged,
    S2 = 2 lam1 t  => s2 = 0 is a density-weight/basis convention, s1 is basis-independent.
"""
from __future__ import annotations
import time, pickle, random
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from fourier_core import X, Fn, vd, pb, Slot, fourier_kernel, kernel_eqs, is_zero, I
from grav_common import COMP, HF, PF, NF, XIF, h, kin, D

RES = {"pass": 0, "fail": 0}
def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)

from grav_common import load_R12
R1, R2 = load_R12()
phi, pi = Fn("phi"), Fn("pi")
A = [Fn(f"A{i}") for i in range(3)]; E = [Fn(f"E{i}") for i in range(3)]
ETA = [Fn(f"eta{k}") for k in range(3)]
MF = Fn("M")
xi = XIF; N = NF
Hl = [[h(i, j) for j in range(3)] for i in range(3)]
GP = [(HF[ab], PF[ab]) for ab in COMP]
SP = [(phi, pi)]
AP = [(A[i], E[i]) for i in range(3)]

def F_(k, i): return D(A[i], k) - D(A[k], i)
def G1(x): return sum(PF[(i, j)] * (D(x[j], i) + D(x[i], j)) for (i, j) in COMP)
def G2(x):
    out = 0
    for (i, j) in COMP:
        v = sum(x[k] * D(h(i, j), k) for k in range(3)) + sum(h(k, j) * D(x[k], i) + h(i, k) * D(x[k], j) for k in range(3))
        out += PF[(i, j)] * v
    return out
def Gm(x): return pi * sum(x[k] * D(phi, k) for k in range(3))
def Gc(x): return sum(E[i] * sum(x[k] * F_(k, i) for k in range(3)) for i in range(3))
def GL(x): return sum(E[i] * sum(x[k] * D(A[i], k) + A[k] * D(x[k], i) for k in range(3)) for i in range(3))
def gauss(th): return th * sum(D(E[i], i) for i in range(3))
def lie(x, y): return [sum(x[l] * D(y[k], l) - y[l] * D(x[k], l) for l in range(3)) for k in range(3)]

al, K1s, K2s, ak, c, mu, g2, cB = sp.symbols("alpha K1 K2 a_k c mu g2 c_B", positive=True)
def Hm0(ak=ak, c=c, mu=mu): return ak * pi ** 2 / 2 + c * sum(D(phi, k) ** 2 for k in range(3)) / 2 + mu * phi ** 2 / 2
def HA0(g2=g2, cB=cB): return g2 / 2 * sum(x ** 2 for x in E) + cB / (4 * g2) * sum(F_(i, j) ** 2 for i in range(3) for j in range(3))

S_xi, S_eta, S_N, S_M = Slot("xi", xi), Slot("eta", ETA), Slot("N", [N]), Slot("M", [MF])
S_h, S_P = Slot("h", list(HF.values())), Slot("P", list(PF.values()))
S_s2 = Slot("m", [phi, pi], 2); S_s1 = Slot("m", [phi, pi], 1)
S_A2 = Slot("a", A + E, 2); S_A1 = Slot("a", A + E, 1)

def solveQ(eqs, unknowns, targets):
    Am, b = sp.linear_eq_to_matrix(eqs, unknowns)
    M = DomainMatrix.from_Matrix(Am.row_join(b)).convert_to(sp.QQ_I)
    R, piv = M.rref(); n = len(unknowns)
    if n in piv: return False, {}, None
    Rm = R.to_Matrix(); free = [j for j in range(n) if j not in piv]; out = {}
    for t in targets:
        j = unknowns.index(t)
        if j not in piv: out[t] = None; continue
        r = piv.index(j)
        out[t] = None if any(Rm[r, f] != 0 for f in free) else sp.nsimplify(Rm[r, n])
    return True, out, len(free)

# ------------------------------------------------------------------ M1
def m1():
    lam, nu, lam1, lam2, bb = sp.symbols("lam nu lam1 lam2 bb")
    LB = lie(xi, ETA)
    br = pb(Gm(xi), Gm(ETA), SP)
    sol = sp.solve(kernel_eqs(lam ** 2 * br - nu * lam * Gm(LB), [S_xi, S_eta, S_s1, ]) if False else
                   kernel_eqs(lam ** 2 * br - nu * lam * Gm(LB), [S_xi, S_eta, Slot("phi", [phi]), Slot("pi", [pi])]), [lam], dict=True)
    ok1 = sorted([s[lam] for s in sol], key=str) == sorted([0, nu], key=str)
    G = lambda x: lam1 * G1(x) + lam2 * G2(x)
    brg = pb(G(xi), G(ETA), GP)
    eqg = kernel_eqs(brg - nu * G(LB), [S_xi, S_eta, S_h, S_P]) + kernel_eqs(brg - nu * G(LB), [S_xi, S_eta, S_P])
    solg = sp.solve(eqg, [lam1, lam2], dict=True)
    ok2 = any(s.get(lam2) == nu and lam1 not in s for s in solg)
    okL = is_zero(pb(GL(xi), GL(ETA), AP) - GL(LB), [S_xi, S_eta, Slot("A", A), Slot("E", E)])
    th = sum(xi[i] * ETA[j] * F_(i, j) for i in range(3) for j in range(3))
    brc = pb(Gc(xi), Gc(ETA), AP)
    solc = sp.solve(kernel_eqs(brc - Gc(LB) - gauss(bb * th), [S_xi, S_eta, Slot("A", A), Slot("E", E)]), [bb], dict=True)
    check("M1", ok1 and ok2 and okL and solc == [{bb: -1}],
          f"lam G_m: lam in {sol}; gravity lam1 G1 + lam2 G2: {solg} (lam1 free); G_L closes exactly; G_c closes mod Gauss[b xi^i eta^j F_ij], b = {solc}")

# ------------------------------------------------------------------ M5
def m5():
    lam1, lamm, lamA = sp.symbols("lam1 lam_m lam_A", nonzero=True)
    dens = kin(al) - K1s * R1 + Hm0() + HA0()
    chi = sp.Matrix(3, 3, lambda k, l: sp.Symbol(f"chi{k}{l}")); dg = sp.symbols("dg0:3")
    x0 = [N * D(MF, l) - MF * D(N, l) for l in range(3)]
    xc = [sum(chi[k, l] * x0[l] for l in range(3)) for k in range(3)]
    t0 = time.time()
    br = pb(N * dens, MF * dens, GP + SP + AP)
    rhs = lam1 * G1(xc) + lamm * Gm(xc) + lamA * Gc(xc) + gauss(sum(dg[l] * x0[l] * A[l] for l in range(3)))
    res = sp.expand(br - rhs)
    eqs = kernel_eqs(res, [S_N, S_M, S_P]) + kernel_eqs(res, [S_N, S_M, S_s2]) + kernel_eqs(res, [S_N, S_M, S_A2])
    sol = sp.solve(eqs, list(chi) + [c, cB] + list(dg), dict=True)
    print(f"   M5 ({time.time()-t0:.1f}s):", sol)
    ok = len(sol) == 1 and all(sp.simplify(sol[0][chi[k, l]] - (K1s / (4 * al * lam1) if k == l else 0)) == 0 for k in range(3) for l in range(3)) \
        and sp.simplify(ak * sol[0][c] - lamm * K1s / (4 * al * lam1)) == 0 and sp.simplify(sol[0][cB] - lamA * K1s / (4 * al * lam1)) == 0
    check("M5", ok, "{C,C} at O(eps) with a general 3x3 structure matrix chi: chi = K1/(4 alpha lam1) * delta, v_m^2 = a_k c = lam_m K1/(4 alpha lam1), v_A^2 = c_B = lam_A K1/(4 alpha lam1)")

# ------------------------------------------------------------------ couplings
def scalar_coupling():
    cs = []; out = 0
    for ab in COMP:
        hab = HF[ab]; q = 0
        for k in range(3):
            for l in range(k, 3):
                s = sp.Symbol(f"c1_{ab[0]}{ab[1]}_{k}{l}"); cs.append(s); q += s * D(phi, k) * D(phi, l)
        for nm, mon in (("c2", pi ** 2), ("c3", phi ** 2)):
            s = sp.Symbol(f"{nm}_{ab[0]}{ab[1]}"); cs.append(s); q += s * mon
        for k in range(3):
            s = sp.Symbol(f"c4_{ab[0]}{ab[1]}_{k}"); cs.append(s); q += s * pi * D(phi, k)
        out += hab * q
        for k in range(3):
            for l in range(3):
                s = sp.Symbol(f"c6_{ab[0]}{ab[1]}_{k}{l}"); cs.append(s); out += s * D(hab, k) * phi * D(phi, l)
    return sp.expand(out), cs

def maxwell_coupling():
    cs = []; out = 0
    Fc = [F_(0, 1), F_(0, 2), F_(1, 2)]
    quads = []
    for i in range(3):
        for j in range(i, 3):
            quads.append(E[i] * E[j]); quads.append(Fc[i] * Fc[j])
    for i in range(3):
        for j in range(3):
            quads.append(E[i] * Fc[j])
    for ab in COMP:
        for n, qd in enumerate(quads):
            s = sp.Symbol(f"d_{ab[0]}{ab[1]}_{n}"); cs.append(s); out += s * HF[ab] * qd
    return sp.expand(out), cs

def lapse(kind="general"):
    S1 = sp.Matrix(3, 3, lambda k, l: sp.Symbol(f"S1_{k}{l}")); S2 = sp.Matrix(3, 3, lambda k, l: sp.Symbol(f"S2_{k}{l}"))
    Np = sum(S1[k, l] * xi[k] * D(N, l) + S2[k, l] * N * D(xi[l], k) for k in range(3) for l in range(3))
    return S1, S2, Np

def matter_eqs(lam1, lamm, lamA, Np, pars, scalar=True, maxwell=True):
    """{C_matter(N), lam1 G1 + lam_m G_m + lam_A G_c} at h^0, matter^2 == N' H0 + G_s[B N xi] + Gauss[...]"""
    eqs = []; unk = []
    akv, cv, muv, g2v, cBv = pars
    if scalar:
        cpl, cs = scalar_coupling()
        Bm = sp.Matrix(3, 3, lambda k, l: sp.Symbol(f"Bm{k}{l}"))
        H0 = Hm0(akv, cv, muv)
        lhs = lamm * pb(N * H0, Gm(xi), SP) + lam1 * sum(vd(N * cpl, HF[ab]) * (D(xi[ab[1]], ab[0]) + D(xi[ab[0]], ab[1])) for ab in COMP)
        rhs = Np * H0 + Gm([sum(Bm[k, l] * N * xi[l] for l in range(3)) for k in range(3)])
        eqs += kernel_eqs(sp.expand(lhs - rhs), [S_N, S_xi, S_s2]); unk += cs + list(Bm)
    if maxwell:
        cpl, cs = maxwell_coupling()
        BA = sp.Matrix(3, 3, lambda k, l: sp.Symbol(f"BA{k}{l}"))
        b1 = sp.Matrix(3, 3, lambda k, l: sp.Symbol(f"gb1_{k}{l}")); b2 = sp.Matrix(3, 3, lambda k, l: sp.Symbol(f"gb2_{k}{l}"))
        H0 = HA0(g2v, cBv)
        lhs = lamA * pb(N * H0, Gc(xi), AP) + lam1 * sum(vd(N * cpl, HF[ab]) * (D(xi[ab[1]], ab[0]) + D(xi[ab[0]], ab[1])) for ab in COMP)
        th = sum(b1[k, l] * N * xi[k] * E[l] + b2[k, l] * N * xi[k] * A[l] for k in range(3) for l in range(3))
        rhs = Np * H0 + Gc([sum(BA[k, l] * N * xi[l] for l in range(3)) for k in range(3)]) + gauss(th)
        eqs += kernel_eqs(sp.expand(lhs - rhs), [S_N, S_xi, S_A2]); unk += cs + list(BA) + list(b1) + list(b2)
    return eqs, unk

def grav_eqs_iso(lam1, K1, K2, Np_f, extra_t=0):
    """gravity degree-1 bracket with the isotropic 12-term G2 (sympy-Function form, Fourier zero test)."""
    mu_ = sp.symbols("g1:13")
    trh = sum(h(k, k) for k in range(3)); dx = lambda i, j: D(xi[j], i); div = sum(dx(k, k) for k in range(3))
    dh = lambda k, i, j: D(h(i, j), k); dtr = lambda k: D(trh, k); dl = lambda i, j: 1 if i == j else 0
    T = [lambda i, j: sum(xi[k] * dh(k, i, j) for k in range(3)),
         lambda i, j: sum(h(i, k) * dx(j, k) + h(j, k) * dx(i, k) for k in range(3)),
         lambda i, j: sum(h(k, i) * dx(k, j) + h(k, j) * dx(k, i) for k in range(3)),
         lambda i, j: dl(i, j) * sum(h(k, l) * dx(k, l) for k in range(3) for l in range(3)),
         lambda i, j: dl(i, j) * trh * div, lambda i, j: h(i, j) * div, lambda i, j: trh * (dx(i, j) + dx(j, i)),
         lambda i, j: dl(i, j) * sum(xi[k] * dtr(k) for k in range(3)),
         lambda i, j: sum(xi[k] * (dh(i, j, k) + dh(j, i, k)) for k in range(3)),
         lambda i, j: dl(i, j) * sum(xi[k] * dh(l, k, l) for k in range(3) for l in range(3)),
         lambda i, j: xi[i] * dtr(j) + xi[j] * dtr(i),
         lambda i, j: sum(xi[i] * dh(k, k, j) + xi[j] * dh(k, k, i) for k in range(3))]
    Cd = N * (-K1 * R1 - K2 * R2 - extra_t * K1 * trh * R1)
    lhs = 0
    for (i, j) in COMP:
        dC = vd(Cd, HF[(i, j)])
        lhs += dC * (lam1 * (D(xi[j], i) + D(xi[i], j)) + sum(mu_[n] * T[n](i, j) for n in range(12)))
    lhs = sp.expand(lhs)
    # degree-1 part in h
    tt = sp.Symbol("tt")
    lhs1 = sp.expand(lhs.subs({HF[ab]: tt * HF[ab] for ab in COMP}).doit()).coeff(tt, 1)
    rhs = sp.expand(Np_f * (-K1 * R1))
    return kernel_eqs(lhs1 - rhs, [S_N, S_xi, S_h]), list(mu_)

# ------------------------------------------------------------------ M6
def m6():
    rng = random.Random(7)
    ok_all = True
    for trial in range(2):
        r = lambda: sp.Rational(rng.randint(1, 9), rng.randint(1, 9))
        lam1, lamm, lamA = r(), r(), r(); pars = (r(), r(), r(), r(), r())
        S1, S2, Np = lapse()
        t0 = time.time()
        eqs_s, unk_s = matter_eqs(lam1, lamm, lamA, Np, pars, True, False)
        oks, sols, nuls = solveQ(eqs_s, unk_s + list(S1) + list(S2), list(S1) + list(S2))
        eqs_a, unk_a = matter_eqs(lam1, lamm, lamA, Np, pars, False, True)
        oka, sola, nula = solveQ(eqs_a, unk_a + list(S1) + list(S2), list(S1) + list(S2))
        s1s = [sols.get(S1[k, l]) for k in range(3) for l in range(3)]; s1a = [sola.get(S1[k, l]) for k in range(3) for l in range(3)]
        print(f"   M6 trial {trial} ({time.time()-t0:.0f}s) lam1={lam1} lam_m={lamm} lam_A={lamA}: scalar consistent={oks} S1={s1s} S2 unique?={[sols.get(x) for x in S2]}; "
              f"Maxwell consistent={oka} S1={s1a} S2 unique?={[sola.get(x) for x in S2]}", flush=True)
        exp_s = [(-lamm if k == l else 0) for k in range(3) for l in range(3)]
        exp_a = [(-lamA if k == l else 0) for k in range(3) for l in range(3)]
        ok_all = ok_all and oks and oka and s1s == exp_s and s1a == exp_a
    check("M6", ok_all, "general matter couplings (scalar 120, Maxwell 126 coefficients), general N', G_s[B N xi], general Gauss multipliers: "
          "S1 = -lam_s * delta forced for each species; S2 is NOT fixed by the matter bracket alone (trace freedom)")

# ------------------------------------------------------------------ J and K12d
def joint():
    rng = random.Random(11)
    ok_all = True
    for trial in range(3):
        r = lambda: sp.Rational(rng.randint(1, 9), rng.randint(1, 9))
        lam1, K1, K2, alv = r(), r(), r(), r(); pars = (r(), r(), r(), r(), r())
        lamm, lamA = sp.symbols("LAMm LAMA")
        S1, S2, Np = lapse()
        t0 = time.time()
        eg, ug = grav_eqs_iso(lam1, K1, K2, Np)
        em, um = matter_eqs(lam1, lamm, lamA, Np, pars, True, True)
        unk = ug + um + list(S1) + list(S2) + [lamm, lamA]
        ok, sol, nul = solveQ(eg + em, unk, [lamm, lamA] + list(S1) + list(S2))
        tgt = lam1 * K2 / K1
        good = ok and sol[lamm] == tgt and sol[lamA] == tgt and all(sol[x] == 0 for x in S2) \
            and all(sol[S1[k, l]] == (-tgt if k == l else 0) for k in range(3) for l in range(3))
        # chain: plug lam_m, lam_A into M5's relation (re-derived here at this numeric point by solving {C,C} for c, c_B)
        v2 = None
        if good:
            akv, cv, muv, g2v, cBv = pars
            dens = kin(alv) - K1 * R1 + Hm0(akv, c, muv) + HA0(g2v, cB)
            chi = sp.Symbol("chi"); x0 = [N * D(MF, l) - MF * D(N, l) for l in range(3)]
            xc = [chi * x0[l] for l in range(3)]
            br = pb(N * dens, MF * dens, GP + SP + AP)
            dg = sp.Symbol("dg")
            rhs = lam1 * G1(xc) + tgt * Gm(xc) + tgt * Gc(xc) + gauss(dg * sum(x0[l] * A[l] for l in range(3)))
            res = sp.expand(br - rhs)
            eqs = kernel_eqs(res, [S_N, S_M, S_P]) + kernel_eqs(res, [S_N, S_M, S_s2]) + kernel_eqs(res, [S_N, S_M, S_A2])
            sc = sp.solve(eqs, [chi, c, cB, dg], dict=True)
            v2 = (akv * sc[0][c], sc[0][cB], K2 / (4 * alv)) if len(sc) == 1 else None
            good = good and v2 is not None and v2[0] == v2[2] and v2[1] == v2[2]
        print(f"   J trial {trial} ({time.time()-t0:.0f}s) lam1={lam1} K1={K1} K2={K2} alpha={alv}: consistent={ok}, lam_m={sol.get(lamm)}, lam_A={sol.get(lamA)} "
              f"(expect lam1 K2/K1 = {tgt}), S2 = 0: {all(sol.get(x)==0 for x in S2)}; (v_m^2, v_A^2, K2/4alpha) = {v2}", flush=True)
        ok_all = ok_all and good
    check("J", ok_all, "ONE constraint, ONE N', general matter couplings, isotropic G2: order-eps {G,C} forces lam_m = lam_A = lam1 K2/K1 and N' = -(lam1 K2/K1) xi.dN; "
          "then {C,C} gives v_m^2 = v_A^2 = K2/(4 alpha) = TT graviton speed^2, at three exact random points")

def k12d():
    lam1, K1, K2, t = sp.Rational(2, 3), sp.Rational(1, 4), sp.Rational(5, 7), sp.Rational(3, 5)
    S1, S2, Np = lapse()
    eg, ug = grav_eqs_iso(lam1, K1, K2, Np, extra_t=t)
    ok, sol, nul = solveQ(eg, ug + list(S1) + list(S2), list(S1) + list(S2))
    s1 = [sol.get(S1[k, l]) for k in range(3) for l in range(3)]; s2 = [sol.get(S2[k, l]) for k in range(3) for l in range(3)]
    print("   K12d: S1 =", s1, " S2 =", s2)
    exp1 = [(-lam1 * K2 / K1 if k == l else 0) for k in range(3) for l in range(3)]
    exp2 = [(2 * lam1 * t if k == l else 0) for k in range(3) for l in range(3)]
    check("K12d", ok and s1 == exp1 and s2 == exp2, "C_g -> C_g - t K1 trh R1 (lapse redefinition N -> N(1 + t trh) at this order): S1 unchanged, S2 = 2 lam1 t: "
          "the s2 = 0 output is a density-weight/basis convention; s1 (the transport coefficient) is basis-independent")

if __name__ == "__main__":
    import sys
    which = sys.argv[1:] or ["m1", "m5", "k12d", "m6", "joint"]
    for w in which:
        globals()[w]()
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
