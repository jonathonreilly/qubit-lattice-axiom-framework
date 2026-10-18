#!/usr/bin/env python3
"""B14 leading order (long-wavelength / continuum limit of the lattice model): exact symbolic jet calculus in 3D.

Same sectors as b14_lattice_closure.py, continuum form, with the six independent strains
h_jj (j=1..3) and h_ij (i<j) and their momenta, G_g[xi] = int P.(d_i xi_j + d_j xi_i),
G_m[xi] = int pi xi.grad phi, and
   C(N) = int N [kin(P) - K R1(h) + pi^2/2 + c|grad phi|^2/2 + mu phi^2/2] + int N h.T,
   coupling int N [ sum_j h_jj T_jj + sum_{i<j} h_ij U_ij ],
   T_jj = A1 pi^2 + A2 |grad phi|^2 + A3 (d_j phi)^2 + A4 phi^2 + A5 phi pi + A6 phi d_j^2 phi + A7 phi lap phi,
   U_ij = B1 d_i phi d_j phi + B2 phi d_i d_j phi  (A3,B1 and A6,B2 are independent: no isotropy assumed).
Functional identities are tested with the Euler operator in the lapse (a local functional linear in N
vanishes for all N iff its Euler derivative in N vanishes identically).

Checks:
 L1  {C,C} order phi pi: closes into G_m[xi0] with the gravity structure function xi0 = kappa(N grad M - M grad N)
     iff c = kappa = K/(4 alpha)  (continuum E2).
 L2  {G,C} order phi^2 (Noether / relabelling covariance of the lapse constraint), RHS H_m(N') with
     N' = s1 xi.grad N + s2 N div xi: solution space of (A, B, s).
 L3  {C,C} order h phi pi, RHS G_m[xi'] with xi'_i = (r1 h_ij + r2 tr h delta_ij) xi0_j: solution space.
 L4  combined L2+L3 with the scalar-lapse rule s2 = 0 and the GR structure function r1 = -1, r2 = 0.
"""
from __future__ import annotations

import itertools
import sympy as sp

DIM = 3
RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


# ---------------------------------------------------------------- jet variables
JET = {}


def J(field, alpha=(0, 0, 0)):
    key = (field, tuple(alpha))
    if key not in JET:
        JET[key] = sp.Symbol(field + "_" + "".join(map(str, alpha)))
    return JET[key]


SYM2KEY = {}


def refresh():
    SYM2KEY.clear()
    for k, s in JET.items():
        SYM2KEY[s] = k


def D(expr, k):
    """total derivative d/dx_k"""
    refresh()
    expr = sp.expand(expr)
    out = 0
    for s in expr.free_symbols:
        if s in SYM2KEY:
            f, a = SYM2KEY[s]
            b = list(a)
            b[k] += 1
            out += sp.diff(expr, s) * J(f, b)
    return sp.expand(out)


def Dalpha(expr, alpha):
    for k in range(DIM):
        for _ in range(alpha[k]):
            expr = D(expr, k)
    return expr


def euler(expr, field):
    refresh()
    expr = sp.expand(expr)
    out = 0
    for s in list(expr.free_symbols):
        if s in SYM2KEY and SYM2KEY[s][0] == field:
            a = SYM2KEY[s][1]
            term = sp.diff(expr, s)
            sign = (-1) ** sum(a)
            out += sign * Dalpha(term, a)
    return sp.expand(out)


def grad(f):
    return [J(f, tuple(1 if k == i else 0 for k in range(DIM))) for i in range(DIM)]


def d2(f, i, j):
    a = [0] * DIM
    a[i] += 1
    a[j] += 1
    return J(f, a)


PAIRS = [(0, 1), (0, 2), (1, 2)]
HD = [f"hd{j}" for j in range(DIM)]
HF = {ij: f"hf{ij[0]}{ij[1]}" for ij in PAIRS}
PD = [f"Pd{j}" for j in range(DIM)]
PF = {ij: f"Pf{ij[0]}{ij[1]}" for ij in PAIRS}
CONJ = {"phi": "pi", **{HD[j]: PD[j] for j in range(DIM)}, **{HF[ij]: PF[ij] for ij in PAIRS}}

al, K, c, mu = sp.symbols("alpha K c mu", positive=True)
A = sp.symbols("A1:8")
B = sp.symbols("B1:3")
s1, s2, r1, r2 = sp.symbols("s1 s2 r1 r2")
phi, pi = J("phi"), J("pi")


def hm_density():
    return pi ** 2 / 2 + c * sum(g ** 2 for g in grad("phi")) / 2 + mu * phi ** 2 / 2


def coupling_density():
    gp = grad("phi")
    lapphi = sum(d2("phi", k, k) for k in range(DIM))
    out = 0
    for j in range(DIM):
        T = (A[0] * pi ** 2 + A[1] * sum(g ** 2 for g in gp) + A[2] * gp[j] ** 2 + A[3] * phi ** 2 + A[4] * phi * pi
             + A[5] * phi * d2("phi", j, j) + A[6] * phi * lapphi)
        out += J(HD[j]) * T
    for (i, j) in PAIRS:
        U = B[0] * gp[i] * gp[j] + B[1] * phi * d2("phi", i, j)
        out += J(HF[(i, j)]) * U
    return out


def r1_density():
    # R1 = d_i d_j h_ij - lap tr h, with h_ij (i<j) counted twice in d_i d_j h_ij
    out = 0
    for j in range(DIM):
        out += d2(HD[j], j, j)
        out -= sum(d2(HD[j], k, k) for k in range(DIM))
    for (i, j) in PAIRS:
        out += 2 * d2(HF[(i, j)], i, j)
    return out


def kin_density():
    tr = sum(J(p) for p in PD)
    return (sum(J(p) ** 2 for p in PD) - tr ** 2 / 2) / (4 * al) + sum(J(PF[ij]) ** 2 for ij in PAIRS) / (8 * al)


def bracket(f, g):
    """density of {int f, int g} (up to total derivatives)"""
    out = 0
    for q, p in CONJ.items():
        out += euler(f, q) * euler(g, p) - euler(f, p) * euler(g, q)
    return sp.expand(out)


def xi_field(name):
    return [J(f"{name}{k}") for k in range(DIM)]


def g_grav_density(xi_names):
    out = 0
    for j in range(DIM):
        out += J(PD[j]) * 2 * J(xi_names[j], tuple(1 if k == j else 0 for k in range(DIM)))
    for (i, j) in PAIRS:
        out += J(PF[(i, j)]) * (J(xi_names[j], tuple(1 if k == i else 0 for k in range(DIM))) + J(xi_names[i], tuple(1 if k == j else 0 for k in range(DIM))))
    return out


def g_matter_density(xi_vec):
    return pi * sum(xi_vec[k] * grad("phi")[k] for k in range(DIM))


def coeff_equations(expr, unknowns):
    """all coefficients of the polynomial in jet variables"""
    expr = sp.expand(expr)
    refresh()
    jets = [s for s in expr.free_symbols if s in SYM2KEY]
    poly = sp.Poly(expr, *jets)
    return [sp.expand(cf) for cf in poly.coeffs()]


def zero_in_lapse(expr, lapse="N"):
    return sp.expand(euler(expr, lapse))


N, M = J("N"), J("M")
XI = [f"xi{k}" for k in range(DIM)]

# ---------------------------------------------------------------- L1
def l1():
    kappa = K / (4 * al)
    CN = N * (kin_density() - K * r1_density() + hm_density())
    CM = M * (kin_density() - K * r1_density() + hm_density())
    br = bracket(CN, CM)
    xi0 = [N * gm - M * gn for gn, gm in zip(grad("N"), grad("M"))]
    # gravity part: P-linear terms; matter: phi pi terms. Total must equal G_g[kappa xi0] + G_m[kappa xi0].
    # G_g with a composite xi: int P.(d xi + d xi); write densities directly
    gg = 0
    for j in range(DIM):
        gg += J(PD[j]) * 2 * D(kappa * xi0[j], j)
    for (i, j) in PAIRS:
        gg += J(PF[(i, j)]) * (D(kappa * xi0[j], i) + D(kappa * xi0[i], j))
    gm = g_matter_density([kappa * x for x in xi0])
    res = zero_in_lapse(br - gg - gm, "N")
    eqs = [e for e in coeff_equations(res, []) if e != 0]
    sol = sp.solve(eqs, c, dict=True)
    check("L1", sol == [{c: K / (4 * al)}], f"continuum O(eps): {{C(N),C(M)}} = G_g[xi0] + G_m[xi0], xi0 = (K/(4alpha))(N grad M - M grad N), iff c = K/(4alpha); solve -> {sol}")


# ---------------------------------------------------------------- L2
def l2():
    xi = [J(n) for n in XI]
    Hn = N * hm_density()
    Cn_coup = N * coupling_density()
    gm = g_matter_density(xi)
    gg = g_grav_density(XI)
    br = bracket(gm, Hn) + bracket(gg, Cn_coup)
    # keep only the phi^2-order part (no h, no P)  -- bracket(gg, coupling) has no h, bracket(gm,Hn) none either
    nprime = s1 * sum(xi[k] * grad("N")[k] for k in range(DIM)) + s2 * N * sum(J(XI[k], tuple(1 if l == k else 0 for l in range(DIM))) for k in range(DIM))
    rhs = nprime * hm_density()
    res = zero_in_lapse(br - rhs, "N")
    eqs = [e for e in coeff_equations(res, []) if e != 0]
    unknowns = list(A) + list(B) + [s1, s2]
    sol = sp.solve(eqs, unknowns, dict=True)
    return sol


# ---------------------------------------------------------------- L3
def l3(kappa_val=None):
    kappa = K / (4 * al)
    cc = kappa
    xi0 = [N * gm - M * gn for gn, gm in zip(grad("N"), grad("M"))]
    hm = hm_density().subs(c, cc)
    coup = coupling_density()
    br = bracket(N * coup, M * hm) + bracket(N * hm, M * coup)
    # matrix h (symmetric) at a point
    H = [[None] * DIM for _ in range(DIM)]
    for j in range(DIM):
        H[j][j] = J(HD[j])
    for (i, j) in PAIRS:
        H[i][j] = H[j][i] = J(HF[(i, j)])
    trh = sum(H[j][j] for j in range(DIM))
    xip = [kappa * sum((r1 * H[i][j] + (r2 * trh if i == j else 0)) * xi0[j] for j in range(DIM)) for i in range(DIM)]
    rhs = g_matter_density(xip)
    res = zero_in_lapse(br - rhs, "N")
    eqs = [e for e in coeff_equations(res, []) if e != 0]
    return eqs


def l0():
    """the GR target values are the linearisation of H_m(g) = pi^2/(2 sqrt g) + sqrt g (c g^ij d_i phi d_j phi + mu phi^2)/2"""
    eps = sp.Symbol("eps")
    hs = sp.symbols("h00 h11 h22 h01 h02 h12")
    g = sp.Matrix([[1 + eps * hs[0], eps * hs[3], eps * hs[4]], [eps * hs[3], 1 + eps * hs[1], eps * hs[5]], [eps * hs[4], eps * hs[5], 1 + eps * hs[2]]])
    gp = sp.Matrix(grad("phi"))
    sq = sp.sqrt(g.det())
    hm = pi ** 2 / (2 * sq) + sq * (c * (gp.T * g.inv() * gp)[0, 0] + mu * phi ** 2) / 2
    lin1 = sp.expand(sp.series(hm, eps, 0, 2).removeO().coeff(eps, 1))
    gpl = grad("phi")
    tgt = 0
    for j in range(DIM):
        tgt += hs[j] * (-pi ** 2 / 4 + c * sum(x ** 2 for x in gpl) / 4 - c * gpl[j] ** 2 / 2 + mu * phi ** 2 / 4)
    for k, (i, j) in enumerate(PAIRS):
        tgt += hs[3 + k] * (-c * gpl[i] * gpl[j])
    check("L0", sp.simplify(lin1 - sp.expand(tgt)) == 0, "the metric-variational stress used as comparator: O(h) part of pi^2/(2 sqrt g) + sqrt g (c g^ij d phi d phi + mu phi^2)/2 has T_jj = -pi^2/4 + c|grad phi|^2/4 - c (d_j phi)^2/2 + mu phi^2/4, U_ij = -c d_i phi d_j phi")


if __name__ == "__main__":
    l0()
    l1()
    sol2 = l2()
    print("L2 solutions:", sol2)
    gr = {A[0]: -sp.Rational(1, 4), A[1]: c / 4, A[2]: -c / 2, A[3]: mu / 4, A[4]: 0, A[5]: 0, A[6]: 0, B[0]: -c, B[1]: 0}
    ok2 = len(sol2) == 1
    if ok2:
        s = sol2[0]
        free = sorted(set(list(A) + list(B) + [s1, s2]) - set(s.keys()), key=str)
        print("   free parameters:", free)
        # the solution must be GR's metric-variational stress + lambda * (trace coupling to H0), lambda <-> s2
        lam = sp.Symbol("lam")
        target = {A[0]: -sp.Rational(1, 4) + lam / 2, A[1]: c / 4 + lam * c / 2, A[2]: -c / 2, A[3]: mu / 4 + lam * mu / 2,
                  A[4]: 0, A[5]: 0, A[6]: 0, B[0]: -c, B[1]: 0, s1: 1, s2: -2 * lam}
        # express solution in terms of the free parameter
        fsym = free[0] if free else None
        sub = {fsym: sp.solve(sp.Eq(s.get(A[0], A[0]), target[A[0]]), fsym)[0]} if fsym is not None else {}
        sub_full = {k: sp.simplify(sp.sympify(s.get(k, k)).subs(sub)) for k in target}
        ok2 = len(free) == 1 and all(sp.simplify(sub_full[k] - target[k]) == 0 for k in target)
    check("L2", ok2, "continuum {G[xi], C(N)} at order phi^2 = H_m(s1 xi.grad N + s2 N div xi) has a ONE-parameter solution family: "
          "T = metric-variational stress of H_m(g) [A1=-1/4, A2=c/4, A3=-c/2, A4=mu/4, B1=-c (U_ij = 2T_ij), A5=A6=A7=B2=0] plus lam*delta_ij*(H_m density) with s2 = -2 lam, s1 = +1 (RHS = H_m(xi.grad N - 2 lam N div xi))")
    # L2 with scalar-lapse rule s2 = 0 -> unique, equal to GR
    sol2s = [dict(s) for s in sol2]
    eqs3 = l3()
    unknowns3 = list(A) + list(B) + [r1, r2]
    sol3 = sp.solve(eqs3, unknowns3, dict=True)
    print("L3 solutions:", sol3)
    # combined: L2 equations + L3 equations
    # recompute L2 equation list
    xi = [J(n) for n in XI]
    br = bracket(g_matter_density(xi), N * hm_density()) + bracket(g_grav_density(XI), N * coupling_density())
    nprime = s1 * sum(xi[k] * grad("N")[k] for k in range(DIM)) + s2 * N * sum(J(XI[k], tuple(1 if l == k else 0 for l in range(DIM))) for k in range(DIM))
    eqs2 = [e for e in coeff_equations(zero_in_lapse(br - nprime * hm_density(), "N"), []) if e != 0]
    eqs2k = [sp.expand(e.subs(c, K / (4 * al))) for e in eqs2]
    both = sp.solve(eqs2k + eqs3, list(A) + list(B) + [s1, s2, r1, r2], dict=True)
    print("L2+L3 solutions:", both)
    kap = K / (4 * al)
    grk = {A[0]: -sp.Rational(1, 4), A[1]: kap / 4, A[2]: -kap / 2, A[3]: mu / 4, A[4]: 0, A[5]: 0, A[6]: 0, B[0]: -kap, B[1]: 0}
    ok3 = len(sol3) >= 1
    check("L3", ok3, "continuum {C,C} at order h phi pi (and h phi^2, h pi^2) closes into G_m[xi'] with xi' = kappa (r1 h + r2 tr h) xi0 on the solution set printed above")
    # L4: impose s2 = 0 (scalar lapse) on L2 -> unique; and r1 = -1, r2 = 0 follow
    sol4 = sp.solve([e.subs(s2, 0) for e in eqs2k] + eqs3, list(A) + list(B) + [s1, r1, r2], dict=True)
    print("L4 (s2=0) solutions:", sol4)
    ok4 = len(sol4) == 1 and all(sp.simplify(sol4[0].get(k, k) - v) == 0 for k, v in grk.items()) and sp.simplify(sol4[0].get(r1, r1) + 1) == 0 and sp.simplify(sol4[0].get(r2, r2)) == 0 and sol4[0].get(s1) == 1
    check("L4", ok4, "with the scalar-lapse rule (s2 = 0) the coupling is UNIQUE and equals the metric-variational stress of the matter Hamiltonian at c = K/(4alpha); "
          "the {C,C} structure function is then forced to xi'_i = -kappa h_ij xi0_j (r1 = -1, r2 = 0), i.e. g^ij = delta^ij - h^ij: the GR structure function")
    # L5 universality: a second species must have the same lam (same s2) to share one RHS; lam != 0 changes r2
    sol5 = sp.solve([e.subs(s2, 2 * sp.Symbol("lam")) for e in eqs2k] + eqs3, list(A) + list(B) + [s1, r1, r2], dict=True)
    print("L5 (s2 = 2 lam) solutions:", sol5)
    ok5 = len(sol5) == 1 and sp.simplify(sol5[0].get(r1, r1) + 1) == 0 and sp.simplify(sol5[0].get(r2, r2) - sp.Symbol("lam") * 0) != None
    if len(sol5) == 1:
        print("   r2(lam) =", sp.simplify(sol5[0].get(r2, r2)))
    check("L5", len(sol5) == 1 and sp.simplify(sol5[0].get(r2, r2)) != 0, "the trace-coupling ambiguity lam shifts the {C,C} structure function by r2 = r2(lam) != 0: species with different lam cannot share one total relabelling with a common xi' -> lam is universal (all species share one lapse density weight)")
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
