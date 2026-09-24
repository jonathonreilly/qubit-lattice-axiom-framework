#!/usr/bin/env python3
"""Parity-odd couplings under the proper rotations only: checks for ATTEMPT.md (attempt 2 of 2), worker w-macbookpro9927a-j7619
(claude-opus-5-5).

Objects: block 64's co-frame e^j_a (coin index j, bond index a), its curl T^j_ab = d_a e^j_b - d_b e^j_a and the inversion-odd scalar
eps.T = eps_jmn T^j_ab (e^-1)_am (e^-1)_bn; block 64's rotation of the coin axes e -> R(x) e; block 65's twist theta with
theta -> theta + t under that rotation; the dressed co-frame e' = R(-theta) e. Beyond second order: metric-only densities of g = e^T e
and a rate field u = log w. Everything exact: sympy polynomial identities, exact nullspaces, truncated jets with rational coefficients.
"""
from __future__ import annotations

import itertools
import json
import subprocess
import sys

import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


R = sp.Rational
NOTES = [
    ("64", "e568866573", "docs/ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_"
     "IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md",
     ["- **Rotation of the coin axes.** `e → R(x)e`, `R(x)` a rotation acting on the coin index.",
      "iff `c_5 = 0`, `c_1 = −c_4/8`, `c_2 = −c_4/4`, `c_3 = c_4/2`",
      "`ε·T = ε^{jkl}T^j_{kl}` (odd under inversion, which the Lattice axiom does not include)",
      "For the blind member `β = 1`."]),
    ("60", "ec3a6abdf0", "docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_"
     "MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md",
     ["lengths that stretch as `ℓ = (w̄/w)^β` supply the rest if `β = 1`"]),
    ("65", "fb37a985ba", "docs/ADMISSIBILITY_RULE_THE_BLIND_WALK_A_SCALAR_HOP_WEIGHTED_BY_THE_TWIST_OF_THE_COIN_ALONG_THE_BOND_MAKES_A_VARYING_"
     "ROTATION_OF_THE_COIN_AXES_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-21.md",
     ["`H[ϑ + θ] − H[ϑ] = −(i/2)[θ·σ, H]` for all `ϑ`, `θ`: the first-order change of the walk under a rotation of the coin is that "
      "of `ϑ → ϑ + θ`.",
      "it is `−4 div ϑ`",
      "The content then asks nothing of `ϑ`, and a field energy that does not see `ϑ` is consistent with it."]),
    ("70", "8b4eccab5c", "docs/ADMISSIBILITY_RULE_THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS_AND_A_HALF_TURN_OF_THE_COIN_WHAT_EACH_VARYING_"
     "FIELD_BECOMES_BOUNDED_THEOREM_NOTE_2026-09-21.md",
     ["`ΠH[F]Π = −H[F∘Π]` for each of the five kinds of field"]),
    ("a1", "72a8eab788", "probes/work/derive/parity-odd-couplings-under-proper-rotations-only/w-jonathonsmac4f50-jb5a4/ATTEMPT.md",
     ["*Separate `ϑ`.* Blindness is `ϑ → ϑ + θ` for arbitrary `θ(x)` (block 65 T2/T3), which forces `F` to be independent of `ϑ`."]),
]
TASK_Q = ["(c) Would any of them survive block 64's two demands (per-tick; blindness)?",
          "HIT if a parity-odd term survives per-tick counting and blindness."]


def family_q() -> None:
    miss = []
    for tag, sha, path, qs in NOTES:
        txt = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True).stdout
        miss += [f"{tag}[{i}]" for i, q in enumerate(qs) if q not in txt]
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict)
                 and t.get("id") == "J:derive:parity-odd-couplings-under-proper-rotations-only:a2"), "")
    miss += [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    n = sum(len(q) for *_, q in NOTES) + len(TASK_Q)
    check("Q", not miss, f"blocks 60, 64, 65, 70 (PR heads), attempt 1's step 8 (ai/probes 72a8eab7) and the task quoted verbatim ({n} lines)"
          f"{'; missing ' + str(miss) if miss else ''}")


X = sp.symbols("x y z")
LC = lambda i, j, k: sp.LeviCivita(i, j, k)


def Omega(v):
    """Omega(v) w = v x w: Omega_jk = eps_jmk v_m."""
    return sp.Matrix(3, 3, lambda j, k: sum(LC(j, m, k) * v[m] for m in range(3)))


def d_odd(E):
    """det e (eps.T) written as 2 eps^{abc} e^j_c d_a e^j_b (identity checked in family A)."""
    return sp.expand(2 * sum(LC(a, b, c) * E[j, c] * sp.diff(E[j, b], X[a])
                             for a in range(3) for b in range(3) for c in range(3) for j in range(3) if LC(a, b, c) != 0))


# ------------------------------------------------------------------------------------------------ A: the cofactor form of det e (eps.T)
def family_a() -> None:
    M = sp.Matrix(3, 3, sp.symbols("m0:9"))
    adj = M.adjugate()
    det = M.det()
    ok = all(sp.expand(sum(LC(j, m, n) * adj[a, m] * adj[b, n] for m in range(3) for n in range(3))
                       - det * sum(LC(a, b, c) * M[j, c] for c in range(3))) == 0
             for j in range(3) for a in range(3) for b in range(3))
    # hence det e * eps_jmn T^j_ab (e^-1)_am (e^-1)_bn = eps^{abc} e^j_c T^j_ab = 2 eps^{abc} e^j_c d_a e^j_b, for every co-frame
    check("A", ok, "det e eps_jmn (e^-1)_am (e^-1)_bn = eps_abc e^j_c for a general 3x3 matrix (27 polynomial identities), so "
          "det e (eps.T) = eps^{abc} e^j_c T^j_ab = 2 eps^{abc} e^j_c d_a e^j_b exactly")


# ------------------------------------------------------------------------------------------------ D: the dressed odd density is blind
def family_d() -> None:
    s, t = sp.symbols("s t")
    B = sp.Matrix(3, 3, lambda j, b: sp.Function(f"B{j}{b}")(*X))
    th = [sp.Function(f"th{m}")(*X) for m in range(3)]      # the twist
    rt = [sp.Function(f"r{m}")(*X) for m in range(3)]       # a rotation of the coin axes
    I3 = sp.eye(3)
    base = I3 + s * B

    def coef(expr, ps, qt):
        e = sp.diff(expr, s, ps) if ps else expr
        e = sp.diff(e, t, qt) if qt else e
        return sp.expand(e.subs({s: 0, t: 0}) / (sp.factorial(ps) * sp.factorial(qt)))

    div = lambda v: sum(sp.diff(v[m], X[m]) for m in range(3))
    # control: the undressed term under a rotation (block 64 T2's 4 c5 div omega at zero strain)
    D0 = d_odd(base)
    D1 = d_odd((I3 + t * Omega(rt)) * base)
    ctrl_t = coef(D1 - D0, 0, 1)
    ctrl_st = coef(D1 - D0, 1, 1)
    ok = sp.expand(ctrl_t - 4 * div(rt)) == 0 and ctrl_st != 0
    # dressed: e' = (1 - t Omega(th)) e; rotation: e -> (1 + t Omega(r)) e, th -> th + r
    Dd = d_odd((I3 - t * Omega(th)) * base)
    Dd_rot = d_odd((I3 - t * Omega([th[m] + rt[m] for m in range(3)])) * (I3 + t * Omega(rt)) * base)
    ok &= coef(Dd_rot - Dd, 0, 1) == 0 and coef(Dd_rot - Dd, 1, 1) == 0
    # its linear form at zero strain: eps.T[e] - 4 div th
    ok &= sp.expand(coef(Dd, 0, 1) + 4 * div(th)) == 0
    ok &= sp.expand(coef(Dd, 1, 0) - 2 * sum(LC(a, b, c) * sp.diff(B[c, b], X[a]) for a in range(3) for b in range(3) for c in range(3))) == 0
    check("D", ok, "undressed: det e (eps.T) changes by 4 div(r) under a coin rotation r at zero strain, and at first order in the strain "
          "too (block 64 T2); dressed e' = R(-th) e with th -> th + r: the change vanishes at orders t and s*t for nine general strain "
          "functions; at zero strain the dressed density is eps.T[e] - 4 div th")


# ------------------------------------------------------------------------------------------------ E: the twist's equation
def family_e() -> None:
    tau = sp.Symbol("tau")
    E = sp.Matrix(3, 3, lambda j, b: sp.Function(f"E{j}{b}")(*X))
    dth = [sp.Function(f"dth{m}")(*X) for m in range(3)]
    Dvar = d_odd(E - tau * Omega(dth) * E)
    first = sp.expand(sp.diff(Dvar, tau).subs(tau, 0))
    adj = E.adjugate()
    want = -4 * sum(adj[a, m] * sp.diff(dth[m], X[a]) for a in range(3) for m in range(3))
    ok = sp.expand(first - want) == 0
    # isotropic stretch: w det e' (e'^-1)^a_m = w l^2 delta_am
    l, w = sp.Function("l")(*X), sp.Function("w")(*X)
    Ei = l * sp.eye(3)
    ok &= all(sp.simplify(w * Ei.adjugate()[a, m] - (w * l ** 2 if a == m else 0)) == 0 for a in range(3) for m in range(3))
    ok &= d_odd(Ei) == 0          # the odd density vanishes on every isotropic co-frame: it adds nothing to the lengths' own equation
    # with block 59/60's lengths at first order, lambda = -beta (u - ubar): grad(w l^2) = w l^2 (1 - 2 beta) grad u
    u, beta = sp.Function("u")(*X), sp.Symbol("beta")
    lin = sp.expand(sp.diff(sp.exp(u) * sp.exp(-2 * beta * u), X[0]) / (sp.exp(u) * sp.exp(-2 * beta * u)))
    ok &= sp.simplify(lin - (1 - 2 * beta) * sp.diff(u, X[0])) == 0
    # first order around the uniform state: e' = (1 + s lam)(1 + s Omega(rho)), w = wbar e^{s u}:
    # d_a(w adj(e')_am) = s wbar [d_m(u + 2 lam) - (curl rho)_m] + O(s^2)
    sv, wbar = sp.symbols("s wbar", positive=True)
    lam = sp.Function("lam")(*X)
    rho = [sp.Function(f"rho{m}")(*X) for m in range(3)]
    Ep = (1 + sv * lam) * (sp.eye(3) + sv * Omega(rho))
    adjE = Ep.adjugate()
    curl = [sum(LC(m, a, k) * sp.diff(rho[k], X[a]) for a in range(3) for k in range(3)) for m in range(3)]
    for m in range(3):
        expr = sum(sp.diff(wbar * sp.exp(sv * u) * adjE[a, m], X[a]) for a in range(3))
        c1 = sp.expand(sp.diff(expr, sv).subs(sv, 0))
        ok &= sp.simplify(c1 - wbar * (sp.diff(u + 2 * lam, X[m]) - curl[m])) == 0
    ok &= sp.simplify(sum(sp.diff(curl[m], X[m]) for m in range(3))) == 0
    check("E", ok, "exact in the co-frame, first order in the twist: delta[det e' (eps.T[e'])] = -4 adj(e')_am d_a (delta th)_m, so the "
          "twist's static equation for F = sum_x w_x c5 det e'(eps.T[e']) is c5 d_a(w adj(e')_am) = 0; for e' = l*1 it reads grad(w l^2) = 0, "
          "and the odd density vanishes there; with l = (wbar/w)^beta, grad(w l^2) = w l^2 (1 - 2 beta) grad u; to first order, with the "
          "frame's rotation rho relative to the twist, it is curl rho = grad(u + 2 lam), and div curl rho = 0")


# ------------------------------------------------------------------------------------------------ N: no invariants at one and three derivatives
def gens_on(tensor_rank, sym=None):
    """so(3) generators acting on tensors of the given rank (optionally restricted to a symmetric subspace)."""
    L = [sp.Matrix(3, 3, lambda i, j: -LC(k, i, j)) for k in range(3)]
    idx = list(itertools.product(range(3), repeat=tensor_rank))
    pos = {ix: n for n, ix in enumerate(idx)}
    mats = []
    for Lk in L:
        G = sp.zeros(len(idx), len(idx))
        for ix in idx:
            for slot in range(tensor_rank):
                for new in range(3):
                    c = Lk[new, ix[slot]]
                    if c != 0:
                        jx = list(ix); jx[slot] = new
                        G[pos[tuple(jx)], pos[ix]] += c
        mats.append(G)
    return mats, idx, pos


def invariant_dim(rank, sym_groups):
    """dimension of so(3)-invariant tensors of `rank` symmetric within each group of slots in sym_groups."""
    mats, idx, pos = gens_on(rank)
    # basis of the symmetric subspace
    reps = {}
    for ix in idx:
        key = tuple(tuple(sorted(ix[s] for s in grp)) for grp in sym_groups)
        reps.setdefault(key, []).append(ix)
    basis = []
    for key, members in reps.items():
        v = sp.zeros(len(idx), 1)
        for ix in members:
            v[pos[ix]] = 1
        basis.append(v)
    P = sp.Matrix.hstack(*basis)
    # invariant vectors inside span(P): solve G P c = 0 for all generators
    A = sp.Matrix.vstack(*[G * P for G in mats])
    return P.shape[1] - A.rank()


def family_n() -> None:
    cases = {
        "V (du; n = 1)": (1, [[0]]),
        "Sym3 V ((du)^3, the third derivatives of u)": (3, [[0, 1, 2]]),
        "V x Sym2 V (du Hess u, du Ric, grad Ric)": (3, [[0], [1, 2]]),
        "V x V x V (control: eps)": (3, [[0], [1], [2]]),
        "Sym2 V x Sym2 V x V (n = 5 blocks: Ric Hess u du)": (5, [[0, 1], [2, 3], [4]]),
    }
    dims = {k: invariant_dim(*v) for k, v in cases.items()}
    ok = (dims["V (du; n = 1)"] == 0 and dims["Sym3 V ((du)^3, the third derivatives of u)"] == 0
          and dims["V x Sym2 V (du Hess u, du Ric, grad Ric)"] == 0 and dims["V x V x V (control: eps)"] == 1
          and dims["Sym2 V x Sym2 V x V (n = 5 blocks: Ric Hess u du)"] > 0)
    check("N", ok, "so(3)-invariant tensors (exact nullspaces): V 0, Sym3 V 0, V x Sym2 V 0 - so in normal coordinates no blind density "
          "has an odd number (1 or 3) of derivatives; controls: V x V x V 1 (eps), Sym2 x Sym2 x V "
          f"{dims['Sym2 V x Sym2 V x V (n = 5 blocks: Ric Hess u du)']} (five derivatives admit invariants)")


# ------------------------------------------------------------------------------------------------ O: the odd sector under the 24 rotations
def family_o() -> None:
    mats = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            M = sp.zeros(3, 3)
            for i in range(3):
                M[i, perm[i]] = sg[i]
            mats.append(M)
    O = [M for M in mats if M.det() == 1]
    Oh = mats
    lam2 = lambda M: (M.trace() ** 2 - (M * M).trace()) / 2
    count = lambda G: sum(M.trace() * lam2(M) for M in G) / len(G)       # invariants in V (x) Lambda^2 V: the curl T^j_ab
    sym2 = lambda M: (M.trace() ** 2 + (M * M).trace()) / 2
    count_even = lambda G: sum(lam2(M) * sym2(M) for M in G) / len(G)     # control: a two-index object has no such issue
    ok = len(O) == 24 and len(Oh) == 48 and count(O) == 1 and count(Oh) == 0
    check("O", ok, f"characters over the 24 proper rotations and the 48 of the full cubic group: linear invariants of the curl "
          f"T^j_ab (V x Lambda^2 V) number {count(O)} and {count(Oh)} - one, eps.T, kept by the 24 and reversed by inversion, so with "
          "relabelling covariance the odd sector at one derivative is c5 det e (eps.T) alone, for e or for the dressed e'")


# ------------------------------------------------------------------------------------------------ F: five derivatives, explicit fields
def trunc(expr, n):
    p = sp.Poly(sp.expand(expr), *X)
    return sum((c * sp.prod([X[i] ** k for i, k in enumerate(mon)]) for mon, c in p.terms() if sum(mon) <= n), sp.Integer(0))


def five_derivative_terms(h, u):
    """C^ij R_ij and eps^{abc} d_a u R_b^d (Hess u)_dc at the origin for g = 1 + h (h(0) = 0), exact from jets of order three."""
    g = sp.eye(3) + h
    hh = h
    ginv = sp.eye(3) - hh + hh * hh - hh * hh * hh
    ginv = ginv.applyfunc(lambda e: trunc(e, 3))
    dg = [[[sp.diff(g[i, j], X[k]) for k in range(3)] for j in range(3)] for i in range(3)]
    Gam = [[[trunc(R(1, 2) * sum(ginv[a, d] * (dg[d][c][b] + dg[d][b][c] - dg[b][c][d]) for d in range(3)), 2)
             for c in range(3)] for b in range(3)] for a in range(3)]
    Riem = [[[[trunc(sp.diff(Gam[a][d][b], X[c]) - sp.diff(Gam[a][c][b], X[d])
                     + sum(Gam[a][c][e] * Gam[e][d][b] - Gam[a][d][e] * Gam[e][c][b] for e in range(3)), 1)
               for d in range(3)] for c in range(3)] for b in range(3)] for a in range(3)]
    Ric = [[trunc(sum(Riem[a][b][a][d] for a in range(3)), 1) for d in range(3)] for b in range(3)]
    at0 = {X[0]: 0, X[1]: 0, X[2]: 0}
    R0 = sp.Matrix(3, 3, lambda i, j: Ric[i][j].subs(at0))
    G0 = [[[Gam[a][b][c].subs(at0) for c in range(3)] for b in range(3)] for a in range(3)]
    dR0 = [[[sp.diff(Ric[i][j], X[k]).subs(at0) for j in range(3)] for i in range(3)] for k in range(3)]
    nabR = [[[dR0[k][i][j] - sum(G0[m][k][i] * R0[m, j] + G0[m][k][j] * R0[i, m] for m in range(3)) for j in range(3)]
             for i in range(3)] for k in range(3)]
    cotton_ric = sum(LC(i, k, l) * nabR[k][l][j] * R0[i, j] for i in range(3) for k in range(3) for l in range(3) for j in range(3))
    du = [sp.diff(u, X[a]).subs(at0) for a in range(3)]
    hess = sp.Matrix(3, 3, lambda d, c: sp.diff(u, X[d], X[c]).subs(at0) - sum(G0[e][d][c] * du[e] for e in range(3)))
    uterm = sum(LC(a, b, c) * du[a] * R0[b, d] * hess[d, c] for a in range(3) for b in range(3) for c in range(3) for d in range(3))
    return sp.nsimplify(cotton_ric), sp.nsimplify(uterm)


def family_f() -> tuple:
    x, y, z = X
    h = sp.Matrix([[R(1, 3) * x * y + R(1, 5) * z ** 2 * x, R(1, 7) * y * z + R(1, 4) * x ** 2 * y, R(2, 9) * x * z + R(1, 6) * y ** 3],
                   [0, R(1, 2) * x ** 2 + R(1, 8) * x * y * z, R(1, 3) * z * y ** 2 + R(1, 5) * x],
                   [0, 0, R(1, 4) * y * z + R(1, 9) * x ** 3 + R(1, 7) * z]])
    h = sp.Matrix(3, 3, lambda i, j: h[min(i, j), max(i, j)])        # symmetric, h(0) = 0
    u = x + R(1, 2) * y * z + R(1, 3) * x * y + R(1, 5) * z ** 2
    c1, u1 = five_derivative_terms(h, u)
    mirror = {x: -x, y: -y, z: -z}
    hm = h.applyfunc(lambda e: sp.expand(e.subs(mirror, simultaneous=True)))
    um = sp.expand(u.subs(mirror, simultaneous=True))
    c2, u2 = five_derivative_terms(hm, um)
    ok = c1 != 0 and u1 != 0 and c2 == -c1 and u2 == -u1
    check("F", ok, f"five derivatives, explicit polynomial metric and rate field at the origin: C^ij R_ij = {c1}, "
          f"eps d_a u R_b^d (Hess u)_dc = {u1}; for the mirrored fields g(-x), u(-x) both change sign exactly")
    return c1, u1


def main() -> int:
    family_q()
    family_a()
    family_d()
    family_e()
    family_o()
    family_n()
    c1, u1 = family_f()
    print("Parity-odd couplings under proper rotations only - checks; worker w-macbookpro9927a-j7619 (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {len(OUT) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    print("SUMMARY: PARTIAL exact: (1) when the field energy sees the twist, blindness (e -> R e, th -> th + r) keeps every density of the "
          "dressed co-frame e' = R(-th) e, and the parity-odd one c5 det e'(eps.T[e']) = 2 c5 eps^{abc} e'^j_c d_a e'^j_b (at zero strain "
          "c5(eps.T - 4 div th)) survives per-tick counting and blindness; its twist equation is c5 d_a(w adj(e')_am) = 0, to first order "
          "curl rho = grad(u + 2 lam), so the flux of grad(u + 2 lam) = (1 - 2 beta) grad u through every closed surface must vanish: with "
          "block 64's beta = 1 no body at rest is allowed; (2) when it does not, blind densities are metric-only, none is odd at one or three "
          "derivatives, and C^ij R_ij and eps d_a u R_b^d (Hess u)_dc are odd, blind and per-tick at five")
    print("HIT: a parity-odd field energy survives per-tick counting and blindness: c5 det e'(eps.T[e']), the co-frame turned back by block "
          "65's twist (at zero strain c5(eps.T - 4 div th)); its twist equation, curl rho = grad(u + 2 lam) at first order, has no solution "
          "around a body when lam = -beta u with beta != 1/2 (block 64's member: beta = 1); without the twist the first odd, blind, per-tick "
          "density has five derivatives (sqrt(g) C^ij R_ij)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
