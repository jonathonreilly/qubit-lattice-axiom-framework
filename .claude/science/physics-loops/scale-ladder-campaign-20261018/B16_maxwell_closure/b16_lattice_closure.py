#!/usr/bin/env python3
"""B16 (scale-ladder campaign, gravity lane): a lattice U(1) gauge field as the matter sector of the
09-24 curvature-member constraint algebra.  Exact rational arithmetic on a periodic L^3 torus.

Reuses the B14 machinery (b14_lattice_closure.py: sparse polynomials over Q, Poisson bracket, gravity
sector kin / R1 / G_g with the 09-24 clauses, the symmetric site scalar H_m / G_m, exact elimination).

SUPPLIED here (premises, not derived):
  * gauge field: A_l (q) and E_l (p) on links l = (x, j); F_p on plaquettes p = (y, (i,j)), i<j,
        F_ij(y) = A_{y+i,j} - A_{y,j} - A_{y+j,i} + A_{y,i}       (noncompact; compact checked in T7)
  * H_EM(N) = sum_l Nlink_l (g^2/2) E_l^2 + sum_p Nplaq_p (cB/(2 g^2)) F_p^2
    with LAPSE TIMINGS Nlink_l = u_tail N_x + u_head N_(x+j),  Nplaq_p = sum_corners w_c N_c (scanned, T2);
    photon speed^2 of this H at unit lapse is the g-independent product (g^2)(cB/g^2) = cB.
  * relabelling generator of the gauge field (fixed by T2/T3: the bracket forces it; its normalisation is
    the translation normalisation checked in T3b):
        G_A[xi] = sum_{y,i} xi_(y,i) sum_{j != i} E_(y+i, j) F_ij(y)      (one-sided lattice "E^j xi^i F_ij")
  * Gauss constraint  Gauss_x = sum_j (E_(x,j) - E_(x-j,j)),  imposed as a first-class constraint; "mod Gauss"
    means: the identity is required only on transverse E (div E = 0), implemented exactly by substituting
    E = curl^T b + h (b on plaquettes, h harmonic) -- equivalent to allowing Gauss terms with ARBITRARY
    (even nonlocal) field-dependent multipliers.
  * gravity: as B14 (09-24 clauses), C(N) = kin(N) + s K R1(N) + matter; s = -1 is the GR sign.

Families:
  T0  transverse parametrisation: div(curl^T b + h) = 0 and it spans ker(div) (rank 2L^3+1).
  T1  gravity alone closes (B14 E1 reproduced through the import), s = -1.
  T2  TIMING CLASSIFICATION of {H_EM(N), H_EM(M)} with symbolic lapses: which link/plaquette timings make
      the bracket depend on (N,M) only through bond xi~ (exact, and modulo Gauss).
  T3  photon cone: with gravity, closure into ONE total relabelling G_g[xi] + G_A[xi] iff cB = -s K/(4 alpha),
      for every g; translation normalisation of G_A.
  T4  scalar + Maxwell + gravity: closes iff c_phi = cB = K/(4 alpha).
  T5  Gauss law: first class; with a pure-translation ("Lie") generator the algebra closes only with a
      Gauss term carrying the field-dependent multiplier -c xi~ . A.
  T6  {G,C} at uniform shift: G_g[uniform] = 0, so NO h- or P-coupling can enter; the Maxwell sector fails
      exactly (also mod Gauss), with an exact defect identity; the B14 scalar obstruction is also
      coupling-independent.
  T7  compact U(1): {H_E(N)+H_Bc(N), same(M)} = G_A^c[-cB xi~] exactly with F -> sin F (sympy, L=3 slice).
Usage: python3 b16_lattice_closure.py L [T0|T1|...|all]
"""
from __future__ import annotations

import importlib.util
import os
import random
import sys
from fractions import Fraction as F

ARGS = sys.argv[1:]
L = int(ARGS[0]) if ARGS else 3
WHICH = ARGS[1] if len(ARGS) > 1 else "all"
HERE = os.path.dirname(os.path.abspath(__file__))
B14PATH = os.path.join(HERE, "..", "B14_gravity_noether_source", "b14_lattice_closure.py")
_saved = sys.argv
sys.argv = [B14PATH, str(L)]
_spec = importlib.util.spec_from_file_location("b14", B14PATH)
b14 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b14)
sys.argv = _saved

SITES, PAIRS, sh, var, VAR, CONJ, Q_OF_P, KIND = b14.SITES, b14.PAIRS, b14.sh, b14.var, b14.VAR, b14.CONJ, b14.Q_OF_P, b14.KIND
padd, pscale, pmul, term, bracket = b14.padd, b14.pscale, b14.pmul, b14.term, b14.bracket
kin, r1, g_grav, h_matter, g_matter = b14.kin, b14.r1, b14.g_grav, b14.h_matter, b14.g_matter
Reducer, in_span = b14.Reducer, b14.in_span
ALPHA, KK, MU = b14.ALPHA, b14.KK, b14.MU
KAPPA = KK / (4 * ALPHA)
RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


# ------------------------------------------------------------------ gauge-field variables
def reg(name, kind):
    i = var(name)
    KIND[i] = kind
    return i


for x in SITES:
    for j in range(3):
        a, e = reg(("A", x, j), "A"), reg(("E", x, j), "E")
        CONJ[a] = e
        Q_OF_P[e] = a
INV = {}


def refresh_inv():
    INV.clear()
    for nm, i in VAR.items():
        INV[i] = nm


def Av(x, j):
    return term(1, var(("A", x, j)))


def Ev(x, j):
    return term(1, var(("E", x, j)))


FCACHE = {}


def Fpl(y, i, j):
    """lattice F_ij(y) = A_{y+i,j} - A_{y,j} - A_{y+j,i} + A_{y,i};  F_ji(y) = -F_ij(y)."""
    key = (y, i, j)
    if key not in FCACHE:
        FCACHE[key] = padd(padd(Av(sh(y, i), j), Av(y, j), F(-1)), padd(Av(sh(y, j), i), Av(y, i), F(-1)), F(-1))
    return FCACHE[key]


def cpoly(v):
    if isinstance(v, dict):
        return v
    return {(): F(v)} if v != 0 else {}


def lapse(n, x):
    """n: dict site->number (numeric lapse) or a str tag (symbolic lapse variables, non-canonical)."""
    if isinstance(n, str):
        return term(1, reg(("lap", n, x), "lap"))
    return cpoly(n[x])


# timing scheme: (link weights per axis (u_tail, u_head), plaquette weights per plane (w00, w10, w01, w11))
def scheme(link, plaq):
    lw = {"mean": (F(1, 2), F(1, 2)), "tail": (F(1), F(0)), "head": (F(0), F(1))}
    pw = {"four": (F(1, 4),) * 4, "diagonal": (F(1, 2), 0, 0, F(1, 2)), "antidiagonal": (0, F(1, 2), F(1, 2), 0),
          "c00": (1, 0, 0, 0), "c10": (0, 1, 0, 0), "c01": (0, 0, 1, 0), "c11": (0, 0, 0, 1)}
    links = link if isinstance(link, tuple) else (link,) * 3
    lws = {d: lw[links[d]] for d in range(3)}
    if plaq == "oriented":  # corner consistent with the per-axis orientations
        pws = {}
        for (i, j) in PAIRS:
            ci = 0 if links[i] == "tail" else 1
            cj = 0 if links[j] == "tail" else 1
            w = [0, 0, 0, 0]
            w[{(0, 0): 0, (1, 0): 1, (0, 1): 2, (1, 1): 3}[(ci, cj)]] = 1
            pws[(i, j)] = tuple(F(v) for v in w)
    else:
        pws = {ij: tuple(F(v) for v in pw[plaq]) for ij in PAIRS}
    return lws, pws


FWD = scheme("tail", "c00")
SYM = scheme("mean", "four")


def link_lapse(n, x, j, sch):
    ut, uh = sch[0][j]
    return padd(pscale(lapse(n, x), ut), pscale(lapse(n, sh(x, j)), uh))


def plaq_corners(y, ij):
    i, j = ij
    return [y, sh(y, i), sh(y, j), sh(sh(y, i), j)]


def plaq_lapse(n, y, ij, sch):
    out = {}
    for w, c in zip(sch[1][ij], plaq_corners(y, ij)):
        if w != 0:
            out = padd(out, pscale(lapse(n, c), w))
    return out


EE = {(x, j): pmul(Ev(x, j), Ev(x, j)) for x in SITES for j in range(3)}
FF = {(y, ij): pmul(Fpl(y, *ij), Fpl(y, *ij)) for y in SITES for ij in PAIRS}


def h_em(n, cb, g2, sch=FWD):
    out = {}
    for x in SITES:
        for j in range(3):
            out = padd(out, pmul(pscale(link_lapse(n, x, j, sch), g2 / 2), EE[(x, j)]))
    for y in SITES:
        for ij in PAIRS:
            out = padd(out, pmul(pscale(plaq_lapse(n, y, ij, sch), cb / (2 * g2)), FF[(y, ij)]))
    return out


def g_A(xi):
    """G_A[xi] = sum_{y,i} xi_(y,i) sum_{j!=i} E_(y+i,j) F_ij(y); xi values may be numbers or polynomials."""
    out = {}
    for y in SITES:
        for i in range(3):
            v = cpoly(xi[(y, i)])
            if not v:
                continue
            for j in range(3):
                if j != i:
                    out = padd(out, pmul(v, pmul(Ev(sh(y, i), j), Fpl(y, i, j))))
    return out


def gauss(x):
    out = {}
    for j in range(3):
        out = padd(padd(out, Ev(x, j)), Ev(sh(x, j, -1), j), F(-1))
    return out


def gauss_poly(theta):
    out = {}
    for x in SITES:
        v = cpoly(theta[x])
        if v:
            out = padd(out, pmul(v, gauss(x)))
    return out


def theta_of(xi):
    """multiplier relating G_A to the pure-translation generator: theta_w = sum_i xi_(w-i,i) A_(w-i,i)."""
    th = {}
    for w in SITES:
        acc = {}
        for i in range(3):
            v = cpoly(xi[(sh(w, i, -1), i)])
            if v:
                acc = padd(acc, pmul(v, Av(sh(w, i, -1), i)))
        th[w] = acc
    return th


def g_L(xi):
    """pure-translation ('Lie') generator: G_L[xi] = G_A[xi] - Gauss[theta(xi, A)]."""
    return padd(g_A(xi), gauss_poly(theta_of(xi)), F(-1))


# ------------------------------------------------------------------ transverse (Gauss-surface) substitution
SUB = {}


def build_sub():
    for y in SITES:
        for ij in PAIRS:
            b = term(1, reg(("bt", y, ij), "bt"))
            refresh_inv()
            for m, cf in Fpl(y, *ij).items():
                nm = INV[m[0]]
                e = var(("E", nm[1], nm[2]))
                SUB[e] = padd(SUB.get(e, {}), pscale(b, cf))
    for j in range(3):
        h = term(1, reg(("ht", j), "ht"))
        for x in SITES:
            e = var(("E", x, j))
            SUB[e] = padd(SUB.get(e, {}), h)


def subst(poly, sub=None):
    sub = SUB if sub is None else sub
    out = {}
    for m, c in poly.items():
        acc = {(): c}
        for v in m:
            acc = pmul(acc, sub[v] if v in sub else {(v,): F(1)})
        out = padd(out, acc)
    return out


build_sub()
refresh_inv()


def unit_bonds():
    out = []
    for x in SITES:
        for j in range(3):
            out.append({(z, l): F(1) if (z, l) == (x, j) else F(0) for z in SITES for l in range(3)})
    return out


UB = unit_bonds()


def rand_field(rng):
    return {x: F(rng.randint(-3, 3)) for x in SITES}


def is_bond(c, d):
    diff = [(c[k] - d[k]) % L for k in range(3)]
    nz = [k for k in range(3) if diff[k] != 0]
    return len(nz) == 1 and diff[nz[0]] in (1, L - 1)


def xi_tilde_sym():
    """symbolic xi~_(y,i) = N_{y+i} M_y - N_y M_{y+i} as polynomials in the lapse variables."""
    out = {}
    for y in SITES:
        for i in range(3):
            out[(y, i)] = padd(pmul(lapse("N", sh(y, i)), lapse("M", y)), pmul(lapse("N", y), lapse("M", sh(y, i))), F(-1))
    return out


# ================================================================== T0
def t0():
    ok_div = all(not subst(gauss(x)) for x in SITES)
    red = Reducer()
    rank = 0
    params = [v for v in VAR.values() if KIND.get(v) in ("bt", "ht")]
    for p in params:
        vec = {}
        for e, poly in SUB.items():
            cf = poly.get((p,), 0)
            if cf:
                vec[e] = cf
        if red.add(vec, {}) is None:
            rank += 1
    check("T0", ok_div and rank == 2 * L ** 3 + 1, f"transverse parametrisation E = curl^T b + h: div = 0 identically ({ok_div}); rank = {rank} = dim ker(div) = 2L^3+1 = {2 * L ** 3 + 1}")


# ================================================================== T1
def t1(rng):
    n, m = rand_field(rng), rand_field(rng)
    s = F(-1)
    br = bracket(padd(kin(n), pscale(r1(n), s * KK)), padd(kin(m), pscale(r1(m), s * KK)))
    xi = {k: v * s * KAPPA for k, v in b14.xi_tilde(n, m).items()}
    check("T1", not padd(br, g_grav(xi), F(-1)), f"gravity alone (L={L}, s=-1): {{C_g(N),C_g(M)}} = G_g[-kappa xi~] exactly (09-24 T1 via the B14 import)")


# ================================================================== T2
def classify(sch, cb=F(3, 2), g2=F(5, 7)):
    br = bracket(h_em("N", cb, g2, sch), h_em("M", cb, g2, sch))
    refresh_inv()
    groups = {}
    for mn, cf in br.items():
        ln = [v for v in mn if KIND[v] == "lap"]
        rest = tuple(v for v in mn if KIND[v] != "lap")
        nmN = [INV[v] for v in ln if INV[v][1] == "N"]
        nmM = [INV[v] for v in ln if INV[v][1] == "M"]
        c, d = nmN[0][2], nmM[0][2]
        key = (min(c, d), max(c, d))
        sgn = 1 if c <= d else -1  # antisymmetric pair coefficient of (N_c M_d - N_d M_c)
        g = groups.setdefault(key, {})
        g[rest] = g.get(rest, 0) + sgn * cf
    nonbond = {k: {r: v for r, v in g.items() if v != 0} for k, g in groups.items() if not is_bond(*k) and k[0] != k[1]}
    nonbond = {k: g for k, g in nonbond.items() if g}
    exact = not nonbond
    modg = all(not subst(g) for g in nonbond.values())
    return br, exact, modg, len(nonbond)


def t2():
    refresh_inv()
    table = {}
    for link in ("mean", "tail", "head"):
        for plaq in ("four", "diagonal", "antidiagonal", "c00", "c10", "c01", "c11"):
            _, ex, mg, nb = classify(scheme(link, plaq))
            refresh_inv()
            table[(link, plaq)] = (ex, mg, nb)
    closing = sorted(k for k, v in table.items() if v[0])
    closing_g = sorted(k for k, v in table.items() if v[1])
    print("T2 table {(link, plaquette): (bond-supported exactly, bond-supported mod Gauss, #non-bond lapse pairs)}:")
    for k in sorted(table):
        print("   ", k, table[k])
    check("T2a", closing == [("head", "c11"), ("tail", "c00")] and closing_g == closing,
          f"of 21 uniform timings (link: mean/tail/head x plaquette: four/diagonal/antidiagonal/one corner), {{H_EM(N),H_EM(M)}} depends on (N,M) only through bond xi~ for exactly {closing}; Gauss law (any multiplier) rescues none; in particular the reflection-symmetric (mean, four) fails")
    # all 8 per-axis orientation choices with the consistent corner
    from itertools import product
    oks = []
    for o in product(("tail", "head"), repeat=3):
        _, ex, mg, nb = classify(scheme(o, "oriented"))
        refresh_inv()
        oks.append(ex)
    # a wrong corner for a mixed orientation fails
    _, exw, mgw, _ = classify(scheme(("tail", "head", "tail"), "c00"))
    refresh_inv()
    check("T2b", all(oks) and not exw and not mgw, "all 8 per-axis orientation choices (each axis timed at its tail or head, each plaquette at the corner where its two axes' chosen endpoints meet) close exactly; a mismatched corner fails even mod Gauss")
    # exact identity for the forward scheme
    cb, g2 = F(3, 2), F(5, 7)
    br = bracket(h_em("N", cb, g2, FWD), h_em("M", cb, g2, FWD))
    xs = xi_tilde_sym()
    rhs = g_A({k: pscale(v, -cb) for k, v in xs.items()})
    check("T2c", not padd(br, rhs, F(-1)), "forward timing (links at tail, plaquettes at base corner): {H_EM(N),H_EM(M)} = G_A[-cB xi~] EXACTLY with symbolic lapses; g drops out (product g^2 * cB/g^2); same form as the scalar's {H_m(N),H_m(M)} = G_m[-c xi~]")
    # Gauss cannot be supported on the 4 links of one plaquette (the analytic reason no multiplier rescues T2a)
    red = Reducer()
    for x in SITES:
        red.add(gauss(x), {})
    rk_g = len(red.basis)
    y0, ij0 = SITES[0], (0, 1)
    added = 0
    for m in Fpl(y0, *ij0):
        nm = INV[m[0]]
        if red.add(Ev(nm[1], nm[2]), {}) is None:
            added += 1
    check("T2d", rk_g == L ** 3 - 1 and added == 4, f"span{{Gauss_x}} (rank {rk_g} = L^3-1) meets span{{E_l : l in boundary of one plaquette}} only in 0 (4 new directions): a diagonal-pair residual B_p * (sum of E around p) can never be a Gauss term")


def t2_sympy():
    """General corner-supported smearing: link lapse u_tail N_x + u_head N_{x+j} (per axis), plaquette lapse
    sum_c w_c N_c (per plane). Exact solution of the bond-support conditions (diagonal-pair coefficients = 0)."""
    import sympy as sp
    u = {d: sp.symbols(f"u{d}t u{d}h") for d in range(3)}
    w = {ij: sp.symbols(f"w{ij[0]}{ij[1]}_00 w{ij[0]}{ij[1]}_10 w{ij[0]}{ij[1]}_01 w{ij[0]}{ij[1]}_11") for ij in PAIRS}
    eqs = []
    for d in range(3):
        eqs.append(u[d][0] + u[d][1] - 1)
    for (i, j) in PAIRS:
        W = dict(zip(["00", "10", "01", "11"], w[(i, j)]))
        eqs.append(sum(W.values()) - 1)
        # links of the plaquette as corner pairs (tail, head) with axis
        links = [("00", "10", i), ("01", "11", i), ("00", "01", j), ("10", "11", j)]
        for (t, h, ax) in links:
            U = {t: u[ax][0], h: u[ax][1]}
            for (c, dd) in (("00", "11"), ("10", "01")):
                eqs.append(sp.expand(U.get(c, 0) * W[dd] - U.get(dd, 0) * W[c]))
    unknowns = [s for d in range(3) for s in u[d]] + [s for ij in PAIRS for s in w[ij]]
    sols = sp.solve(eqs, unknowns, dict=True)
    full = [s for s in sols if len(s) == len(unknowns)]
    print("T2e solutions (u_tail per axis; plaquette corner with weight 1):")
    desc = []
    for s in full:
        ut = tuple(int(s[u[d][0]]) for d in range(3))
        corners = tuple(["00", "10", "01", "11"][[s[v] for v in w[ij]].index(1)] if 1 in [s[v] for v in w[ij]] else "?" for ij in PAIRS)
        desc.append((ut, corners))
        print("    u_tail =", ut, " corners (01,02,12 planes) =", corners)
    sym_ok = all(not (s[u[d][0]] == s[u[d][1]]) for s in full for d in range(3))
    check("T2e", len(sols) == 8 and len(full) == 8 and sym_ok,
          "exact classification (sympy) over ALL corner-supported smearings (2 weights per link axis, 4 per plaquette plane, normalised): exactly 8 solutions, each link axis timed at ONE endpoint and each plaquette at the matching corner; no solution is reflection-symmetric (u_tail = u_head never occurs)")


# ================================================================== T3
def total_cols(with_scalar=False, gen=None):
    gen = g_A if gen is None else gen
    cols = []
    for xi in UB:
        c = padd(g_grav(xi), gen(xi))
        if with_scalar:
            c = padd(c, g_matter(xi))
        cols.append(c)
    return cols


def t3(rng):
    n, m = rand_field(rng), rand_field(rng)
    cols = total_cols()
    res = {}
    for s in (F(-1), F(1)):
        cg = padd(kin(n), pscale(r1(n), s * KK))
        cm = padd(kin(m), pscale(r1(m), s * KK))
        for g2 in (F(1), F(9, 4)):
            for cb in (KAPPA, 2 * KAPPA, KAPPA / 3, -KAPPA):
                br = bracket(padd(cg, h_em(n, cb, g2)), padd(cm, h_em(m, cb, g2)))
                res[(int(s), str(g2), str(cb / KAPPA))] = in_span(br, cols)
    expect = {k: (F(k[2]) == -k[0]) for k in res}
    check("T3a", res == expect, f"gravity + Maxwell (forward timing, supplied G_A): total O(eps) bracket closes into ONE G_g[xi] + G_A[xi] iff cB = -s K/(4 alpha), independently of g; table {{(s, g^2, cB/kappa): closes}} = {res}")
    # control: the cone value is tied to the generator's normalisation (a rescaled generator moves it)
    cols2 = [padd(g_grav(xi), pscale(g_A(xi), F(2))) for xi in UB]
    cg = padd(kin(n), pscale(r1(n), -KK))
    cm = padd(kin(m), pscale(r1(m), -KK))
    r2 = {str(cb / KAPPA): in_span(bracket(padd(cg, h_em(n, cb, F(1))), padd(cm, h_em(m, cb, F(1)))), cols2) for cb in (KAPPA, 2 * KAPPA)}
    check("T3c", r2 == {"1": False, "2": True}, f"control: with the generator rescaled to 2 G_A the closing value moves to cB = 2 kappa ({r2}); the cone is fixed only together with the generator normalisation, which T3b fixes by the translation action")
    # translation normalisation
    xi_u = {(x, j): F(1) if j == 0 else F(0) for x in SITES for j in range(3)}
    ga = g_A(xi_u)
    ok = True
    for z in SITES:
        for j in range(3):
            act = bracket(Av(z, j), ga)
            # expected: backward difference along axis 0 plus a gauge gradient of theta_w = -A_(w-e0, 0)
            exp = padd(Av(z, j), Av(sh(z, 0, -1), j), F(-1))
            exp = padd(exp, padd(Av(sh(sh(z, j), 0, -1), 0), Av(sh(z, 0, -1), 0), F(-1)), F(-1))
            ok = ok and not padd(act, exp, F(-1))
    gm = g_matter(xi_u)
    ok2 = all(not padd(bracket(term(1, var(("phi", z))), gm),
                       padd(pscale(term(1, var(("phi", sh(z, 0)))), F(1, 2)), pscale(term(1, var(("phi", sh(z, 0, -1)))), F(-1, 2))), F(-1)) for z in SITES)
    check("T3b", ok and ok2, "normalisation: {A_(z,j), G_A[xi = e_0 uniform]} = (A_(z,j) - A_(z-e0,j)) - (A_(z-e0+ej,0) - A_(z-e0,0)) exactly (unit backward translation + gauge); {phi_z, G_m[same]} = (phi_(z+e0) - phi_(z-e0))/2 (unit central translation): both generators carry the same unit normalisation, so the speed conditions are comparable")


# ================================================================== T4
def t4(rng):
    n, m = rand_field(rng), rand_field(rng)
    cols = total_cols(with_scalar=True)
    cg = padd(kin(n), pscale(r1(n), -KK))
    cm = padd(kin(m), pscale(r1(m), -KK))
    g2 = F(4, 9)
    res = {}
    for c in (KAPPA, 2 * KAPPA):
        for cb in (KAPPA, 2 * KAPPA):
            br = bracket(padd(padd(cg, h_matter(n, c)), h_em(n, cb, g2)), padd(padd(cm, h_matter(m, c)), h_em(m, cb, g2)))
            res[(str(c / KAPPA), str(cb / KAPPA))] = in_span(br, cols)
    check("T4", res == {("1", "1"): True, ("1", "2"): False, ("2", "1"): False, ("2", "2"): False},
          f"scalar (symmetric timing, G_m) + Maxwell (forward timing, G_A) + gravity (s=-1): one total relabelling iff c_phi = cB = K/(4 alpha); table {{(c/kappa, cB/kappa): closes}} = {res}")


# ================================================================== T5
def t5(rng):
    n, m = rand_field(rng), rand_field(rng)
    th, th2 = rand_field(rng), rand_field(rng)
    xi = {k: F(rng.randint(-3, 3)) for k in UB[0]}
    cb, g2 = KAPPA, F(9, 4)
    gth = gauss_poly(th)
    a1 = not bracket(gth, h_em(n, cb, g2))
    a2 = not bracket(gth, g_A(xi))
    a3 = not bracket(gth, gauss_poly(th2))
    a4 = in_span(bracket(gth, g_L(xi)), [gauss(x) for x in SITES])
    check("T5a", a1 and a2 and a3 and a4, "Gauss is first class: {Gauss[theta], H_EM(N)} = 0, {Gauss[theta], G_A[xi]} = 0, {Gauss, Gauss} = 0 exactly; {Gauss[theta], G_L[xi]} is a pure Gauss term (theta transported)")
    xt = b14.xi_tilde(n, m)
    br_em = bracket(h_em(n, cb, g2), h_em(m, cb, g2))
    xin = {k: -cb * v for k, v in xt.items()}
    ident = padd(g_L(xin), gauss_poly(theta_of(xin)))
    check("T5b", not padd(br_em, ident, F(-1)), "with the pure-translation generator G_L (G_L[e0 uniform] shifts every A component by its backward difference, no gauge part): {H_EM(N),H_EM(M)} = G_L[-cB xi~] + Gauss[lambda], lambda_w = -cB sum_i xi~_(w-i,i) A_(w-i,i)  (field-dependent structure function, lattice image of -xi.A)")
    cg = padd(padd(kin(n), pscale(r1(n), -KK)), h_em(n, cb, g2))
    cm = padd(padd(kin(m), pscale(r1(m), -KK)), h_em(m, cb, g2))
    br = bracket(cg, cm)
    colsL = total_cols(gen=g_L)
    no = in_span(br, colsL)
    yes_t = in_span(subst(br), [subst(c) for c in colsL])
    loc = colsL + [pmul(gauss(w), Av(sh(w, i, -1), i)) for w in SITES for i in range(3)] + [pmul(gauss(w), Av(w, i)) for w in SITES for i in range(3)]
    yes_l = in_span(br, loc)
    check("T5c", (not no) and yes_t and yes_l, "full algebra with G_g + G_L: does NOT close into relabellings alone; closes on the Gauss surface; and closes exactly once local Gauss terms Gauss_w * A_l (l touching w) are allowed -> the Gauss constraint enters {C,C} with an A-dependent structure function unless the gauge-covariant generator G_A is used")


# ================================================================== T6
def t6(rng):
    xi_u = {(x, j): F(1) if j == 0 else F(0) for x in SITES for j in range(3)}
    check("T6a", not g_grav(xi_u), "G_g[uniform shift] = 0 identically (delta h = symmetric lattice gradient of xi): at uniform xi every coupling built from h or P drops out of {G,C}")
    cb, g2 = KAPPA, F(9, 4)
    one = {x: F(1) for x in SITES}
    ga = g_A(xi_u)
    R1 = bracket(ga, h_em(one, cb, g2))
    # exact defect identity
    dE = {}
    for x in SITES:
        for j in range(3):
            d = padd(Ev(x, j), Ev(sh(x, 0, -1), j), F(-1))
            dE = padd(dE, pmul(d, d))
    dF = {}
    for y in SITES:
        for ij in PAIRS:
            d = padd(Fpl(y, *ij), Fpl(sh(y, 0, -1), *ij), F(-1))
            dF = padd(dF, pmul(d, d))
    gterm = {}
    for w in SITES:
        gterm = padd(gterm, pmul(Ev(sh(w, 0, -1), 0), gauss(w)))
    ident = padd(padd(pscale(dE, g2 / 2), pscale(dF, -cb / (2 * g2))), pscale(gterm, g2))
    check("T6b", not padd(R1, ident, F(-1)), "exact defect at unit lapse: {G_A[e0], H_EM(1)} = (g^2/2) sum_l (E_l - E_(l-e0))^2 - (cB/(2g^2)) sum_p (F_p - F_(p-e0))^2 + g^2 sum_w E_(w-e0,0) Gauss_w  (squares of one-sided differences)")
    hcols = [subst(h_em({z: F(1) if z == x else F(0) for z in SITES}, cb, g2)) for x in SITES]
    f1 = in_span(subst(R1), hcols)
    n = rand_field(rng)
    Rn = bracket(ga, h_em(n, cb, g2))
    f2 = in_span(subst(Rn), hcols)
    check("T6c", (not f1) and (not f2), "Maxwell {G_A[uniform], H_EM(N)} is NOT H_EM(N') for any N', even on the Gauss surface, both at N = 1 and random N: coupling-independent lattice obstruction to {G,C} = C(N') (lattice translation is not an exact symmetry of H_EM; one-sided generator)")
    sm1 = bracket(g_matter(xi_u), h_matter(one, KAPPA))
    smn = bracket(g_matter(xi_u), h_matter(n, KAPPA))
    scols = [h_matter({z: F(1) if z == x else F(0) for z in SITES}, KAPPA) for x in SITES]
    check("T6d", (not sm1) and not in_span(smn, scols), "scalar comparison: {G_m[uniform], H_m(1)} = 0 exactly (symmetric generator, central difference), but for random N {G_m[uniform], H_m(N)} is not any H_m(N'): B14's E5 obstruction already occurs at uniform xi where G_g = 0, so it is independent of the coupling ansatz")


# ================================================================== T7
def t7(rng):
    import sympy as sp
    LL = L
    Asym = {(x, j): sp.Symbol(f"A_{x[0]}{x[1]}{x[2]}_{j}") for x in SITES for j in range(3)}
    Esym = {(x, j): sp.Symbol(f"E_{x[0]}{x[1]}{x[2]}_{j}") for x in SITES for j in range(3)}

    def Fs(y, i, j):
        return Asym[(sh(y, i), j)] - Asym[(y, j)] - Asym[(sh(y, j), i)] + Asym[(y, i)]
    n, m = rand_field(rng), rand_field(rng)
    cb, g2 = sp.Rational(3, 2), sp.Rational(5, 7)

    def H(nn):
        out = 0
        for x in SITES:
            for j in range(3):
                out += sp.Rational(nn[x]) * g2 / 2 * Esym[(x, j)] ** 2
        for y in SITES:
            for (i, j) in PAIRS:
                out += sp.Rational(nn[y]) * cb / g2 * (1 - sp.cos(Fs(y, i, j)))
        return out
    Hn, Hm = H(n), H(m)
    br = 0
    for k in Asym:
        br += sp.diff(Hn, Asym[k]) * sp.diff(Hm, Esym[k]) - sp.diff(Hn, Esym[k]) * sp.diff(Hm, Asym[k])
    xt = b14.xi_tilde(n, m)
    rhs = 0
    for y in SITES:
        for i in range(3):
            v = -cb * sp.Rational(xt[(y, i)])
            if v == 0:
                continue
            for j in range(3):
                if j != i:
                    rhs += v * Esym[(sh(y, i), j)] * sp.sin(Fs(y, i, j))
    ok = sp.expand(br - rhs) == 0
    check("T7", ok, f"compact U(1) (L={LL}): H_B = sum Nplaq (cB/g^2)(1 - cos F_p); {{H(N),H(M)}} = G_A^c[-cB xi~] with G_A^c[xi] = sum xi_(y,i) E_(y+i,j) sin F_ij(y), exactly to all orders in the field: the timing selection and the cone condition are unchanged by compactness")


if __name__ == "__main__":
    rng = random.Random(20261018 + 16)
    print(f"B16 lattice closure, L={L}, alpha={ALPHA}, K={KK}, kappa=K/(4 alpha)={KAPPA}")
    if WHICH in ("all", "T0"):
        t0()
    if WHICH in ("all", "T1"):
        t1(rng)
    if WHICH in ("all", "T2"):
        t2()
        t2_sympy()
    if WHICH in ("all", "T3"):
        t3(rng)
    if WHICH in ("all", "T4"):
        t4(rng)
    if WHICH in ("all", "T5"):
        t5(rng)
    if WHICH in ("all", "T6"):
        t6(rng)
    if WHICH in ("all", "T7"):
        t7(rng)
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
