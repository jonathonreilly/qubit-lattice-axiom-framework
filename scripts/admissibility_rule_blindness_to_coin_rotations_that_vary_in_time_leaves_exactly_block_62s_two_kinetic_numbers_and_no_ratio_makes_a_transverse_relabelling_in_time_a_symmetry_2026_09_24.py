#!/usr/bin/env python3
"""Exact checks: blindness to coin rotations that vary in time leaves exactly block 62's two kinetic numbers, and no
kinetic ratio makes a transverse relabelling that varies in time a symmetry - a shift-like field and the light-cone ratio
alpha/K stay supplied (a harvest block from a Grok-refereed probes attempt; blocks 60, 62, 64, 101 and 112 as supplied;
not adopted).

B (T1): coin-rotation blindness on a generic frame - the antisymmetric shift and the two surviving invariants.
C (T2): the isotropic stretch, block 60 T5's coefficient, and where the closing ratio beta = -alpha sits.
D (T3): the transverse relabelling (never absorbed), against the gradient relabelling (block 112 T2's field part).
E (T4): the 7x7 mode determinant with K explicit, the null vector at beta = -alpha, the light cone.
Exact symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_BLINDNESS_TO_COIN_ROTATIONS_THAT_VARY_IN_TIME_LEAVES_EXACTLY_BLOCK_62S_TWO_KINETIC_NUMBERS_AND_NO_RATIO_MAKES_A_TRANSVERSE_RELABELLING_IN_TIME_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_blindness_to_coin_rotations_that_vary_in_time_leaves_exactly_block_62s_two_kinetic_numbers_and_no_ratio_makes_a_transverse_relabelling_in_time_a_symmetry_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "rotation_not_antisymmetric": "B",
    "stretch_coefficient_forged": "C",
    "multiplier_shift_forged": "D",
    "mode_determinant_forged": "E",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


Fr = Fraction


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged and no site is privileged; time-dependent invariance demands are separate assumptions; Admissibility is not a dynamics axiom (the frame, the member and its kinetic term are supplied clauses)")


# ============================================================================================ block 62's frame, member and kinetic family
AL, BE, KK, XX = sp.symbols("alpha beta K X")
PV = sp.Matrix(sp.symbols("p1:4"))


def member_terms(hm, pv):
    """block 62's member: R1 = -(p.h.p - p^2 tr h), R2 = -(1/4) p^2 h_ij h_ij + (1/2)|h p|^2 - (1/2)(p.h.p) tr h + (1/4) p^2 (tr h)^2."""
    tr = hm.trace()
    p2 = (pv.T * pv)[0]
    php = (pv.T * hm * pv)[0]
    hp = hm * pv
    hh = sum(hm[i, j] ** 2 for i in range(3) for j in range(3))
    r1 = -(php - p2 * tr)
    r2 = -sp.Rational(1, 4) * p2 * hh + sp.Rational(1, 2) * (hp.T * hp)[0] - sp.Rational(1, 2) * php * tr + sp.Rational(1, 4) * p2 * tr ** 2
    return r1, r2


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: blindness to label-dependent coin rotations leaves exactly two kinetic numbers."""
    e = sp.Matrix([[2, 1, 0], [sp.Rational(1, 2), 3, 1], [0, -1, 2]])
    ed = sp.Matrix(3, 3, sp.symbols("d0:9"))
    w = sp.symbols("w", positive=True)
    om = sp.symbols("o1:4")
    omega = sp.Matrix([[0, om[0], om[1]], [-om[0], 0, om[2]], [-om[1], -om[2], 0]])
    einv = e.inv()
    g = einv.T * einv
    ginv = g.inv()

    def invariants(k):
        i1 = sp.expand((k.T * g * k * ginv).trace())
        i2 = sp.expand((k * k).trace())
        i3 = sp.expand(k.trace() ** 2)
        return i1, i2, i3
    k0 = ed * einv / w
    k1 = k0 + e * omega * einv / w
    a1, a2, a3 = invariants(k0)
    b1, b2, b3 = invariants(k1)
    ok_blind = sp.expand(a1 + a2 - b1 - b2) == 0 and sp.expand(a3 - b3) == 0 and sp.expand((a1 - a2) - (b1 - b2)) != 0
    if mut("rotation_not_antisymmetric"):
        ok_blind = sp.expand((a1 - a2) - (b1 - b2)) == 0
    gdot = -g * (ed * e.T + e * ed.T) * g
    sym_part = (g * k0 + (g * k0).T) / 2
    ok_sym = sp.simplify(sym_part + gdot / (2 * w)) == sp.zeros(3, 3)
    shift = sp.simplify(g * (k1 - k0))
    ok_anti = sp.simplify(shift + shift.T) == sp.zeros(3, 3)
    checks.check("B1", ok_blind and ok_sym and ok_anti,
                 "T1: for a generic rational frame E with nine symbolic rates and three symbolic rotation rates, a rotation of the coin axes varying in time (the tick label) shifts the lowered frame rate g V (V = E' E^-1/w) by an exactly antisymmetric matrix, while sym(g V) = -g'/(2w); so I1 + I2 and (tr V)^2 are unchanged and I1 - I2 is not: a quadratic kinetic term built from V with the metric alone is blind iff c1 = c2 and has exactly two numbers, (det e/w)[alpha tr(g^-1 g' g^-1 g') + beta (tr g^-1 g')^2], block 62's family")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the isotropic stretch and block 60 T5's coefficient."""
    lamd = sp.symbols("lambdadot")
    hd = 2 * lamd * sp.eye(3)
    ck = sp.expand((AL * sum(hd[i, j] ** 2 for i in range(3) for j in range(3)) + BE * hd.trace() ** 2) / lamd ** 2)
    want = 12 * AL + 36 * BE
    if mut("stretch_coefficient_forged"):
        want = 12 * AL + 24 * BE
    ok = sp.expand(ck - want) == 0 and sp.expand(ck.subs(BE, -AL) + 24 * AL) == 0 and sp.expand(ck.subs({AL: KK / 4, BE: -KK / 4}) + 6 * KK) == 0
    neg = sp.solve(sp.Eq(want, 0), BE) == [-AL / 3]
    checks.check("C1", ok and neg,
                 "T2: for the isotropic stretch h = 2 lambda delta the kinetic term is (12 alpha + 36 beta) lambda'^2 / w, block 60 T5's c_k, increasing in beta: for alpha > 0 negative (an algebraic coefficient condition, not an evolution theorem) iff beta < -alpha/3; at the closing ratio beta = -alpha (blocks 101, 112) it is -24 alpha, inside that region; -6K at (K/4, -K/4)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: no ratio makes a transverse relabelling in time a symmetry; the gradient one needs beta = -alpha (block 112 T2)."""
    t = sp.symbols("t")
    hf = [sp.Function(f"h{i}")(t) for i in range(6)]
    hm = sp.Matrix([[hf[0], hf[1], hf[2]], [hf[1], hf[3], hf[4]], [hf[2], hf[4], hf[5]]])
    uf = sp.Function("u")(t)
    zf = sp.Function("zeta")(t)

    def lag(hmat, uu):
        hd = hmat.diff(t)
        r1, r2 = member_terms(hmat, PV)
        return AL * sum(hd[i, j] ** 2 for i in range(3) for j in range(3)) + BE * hd.trace() ** 2 + KK * (uu * r1 + r2)
    shift_u = -(2 * AL / KK) * zf.diff(t, 2)
    if mut("multiplier_shift_forged"):
        shift_u = -(AL / KK) * zf.diff(t, 2)
    dl = sp.expand(lag(hm + PV * PV.T * zf, uf + shift_u) - lag(hm, uf))
    r1, _ = member_terms(hm, PV)
    p2 = (PV.T * PV)[0]
    want = -2 * AL * (zf.diff(t) * r1).diff(t) + (AL + BE) * (2 * p2 * hm.trace().diff(t) * zf.diff(t) + p2 ** 2 * zf.diff(t) ** 2)
    ok_grad = sp.simplify(dl - sp.expand(want)) == 0
    xih = sp.Matrix([PV[1], -PV[0], 0])
    xi = xih * zf
    dh = PV * xi.T + xi * PV.T
    r1a, r2a = member_terms(hm, PV)
    r1b, r2b = member_terms(hm + dh, PV)
    inv_trans = sp.simplify(r1a - r1b) == 0 and sp.simplify(r2a - r2b) == 0
    dl_t = sp.expand(lag(hm + dh, uf) - lag(hm, uf))
    xn = (PV[0] ** 2 + PV[1] ** 2)
    want_t = 4 * AL * zf.diff(t) * (xih.T * hm.diff(t) * PV)[0] + 2 * AL * p2 * xn * zf.diff(t) ** 2
    ok_change = sp.simplify(dl_t - sp.expand(want_t)) == 0
    zd = sp.symbols("zd")
    el = -sp.diff(dl_t.subs(zf.diff(t), zd), zd).subs(zd, zf.diff(t)).diff(t) + sp.diff(dl_t, zf)
    el_want = -4 * AL * ((xih.T * hm.diff(t, 2) * PV)[0] + p2 * xn * zf.diff(t, 2))
    ok_el = sp.simplify(el - sp.expand(el_want)) == 0 and sp.simplify(el) != 0
    ok_trans = inv_trans and ok_change and ok_el
    checks.check("D1", ok_grad and ok_trans,
                 "T3: a transverse relabelling varying in time (h -> h + p xi^T + xi p^T, xi = (p2, -p1, 0) zeta(t), p.xi = 0) leaves R1 and R2 unchanged and changes the Lagrangian by exactly 4 alpha zeta' xi.h'.p + 2 alpha p^2 (p1^2 + p2^2) zeta'^2 (no beta), whose variational derivative in zeta, -4 alpha (xi.h''.p + p^2 (p1^2 + p2^2) zeta''), is not zero: not a total derivative, so a symmetry at no ratio with alpha != 0, and the supplied scalar multiplier cannot cancel it on R1=0; against it, the gradient relabelling h -> h + p p^T zeta(t) with u -> u - (2 alpha/K) zeta'' changes alpha h'_ij h'_ij + beta h'^2 + K(u R1 + R2) by -2 alpha d(zeta' R1)/dt + (alpha + beta)(2 p^2 tr h' zeta' + p^4 zeta'^2) exactly (symbolic functions of time), a symmetry up to a total derivative iff beta = -alpha (block 112 T2's field part, re-checked)")


def variational(expr, fn, t):
    """variational derivative of expr in the function fn(t), for expressions with at most second derivatives of fn."""
    s0, s1, s2 = sp.symbols("vs0 vs1 vs2")
    back = {s0: fn, s1: fn.diff(t), s2: fn.diff(t, 2)}
    e = expr.subs(fn.diff(t, 2), s2).subs(fn.diff(t), s1).subs(fn, s0)
    out = sp.diff(e, s0).subs(back) - sp.diff(sp.diff(e, s1).subs(back), t) + sp.diff(sp.diff(e, s2).subs(back), t, 2)
    return sp.expand(out)


def symmetry_conditions(dl, fields, t, extra):
    """coefficients of every variational derivative of dl, as polynomials in the fields' derivatives, p and extra symbols."""
    eqs = []
    for fn in fields:
        e = variational(dl, fn, t)
        syms = []
        for g in fields:
            for k in range(5, -1, -1):
                s = sp.Symbol(f"D{k}_{g.func.__name__}")
                e = e.subs(g.diff(t, k) if k else g, s)
                syms.append(s)
        eqs += list(sp.Poly(e, *(syms + list(PV) + list(extra))).coeffs())
    return eqs


def family_d2(checks: Checks) -> None:
    """T5: in block 62's cube family the gradient relabelling forces the rotation-invariant member at beta = -alpha."""
    t = sp.symbols("t")
    m1, m2, m3, cc = sp.symbols("M1 M2 M3 c")
    hf = [sp.Function(f"h{i}")(t) for i in range(6)]
    hm = sp.Matrix([[hf[0], hf[1], hf[2]], [hf[1], hf[3], hf[4]], [hf[2], hf[4], hf[5]]])
    uf = sp.Function("u")(t)
    zf = sp.Function("zeta")(t)
    fields = hf + [zf, uf]

    def lag(hmat, uu):
        d = hmat.diff(t)
        r1, r2 = member_terms(hmat, PV)
        kin = (m1 * sum(d[j, j] ** 2 for j in range(3)) + m2 * sum(d[i, i] * d[j, j] for i in range(3) for j in range(i + 1, 3))
               + m3 * sum(d[i, j] ** 2 for i in range(3) for j in range(i + 1, 3)))
        return kin + KK * (uu * r1 + r2)
    dl_g = sp.expand(lag(hm + PV * PV.T * zf, uf + cc * zf.diff(t, 2) / KK) - lag(hm, uf))
    sol_g = sp.solve(symmetry_conditions(dl_g, fields, t, ()), [m1, m2, m3, cc], dict=True)
    av = sp.Matrix(sp.symbols("a1:4"))
    xi = PV.cross(av)
    dl_t = sp.expand(lag(hm + (PV * xi.T + xi * PV.T) * zf, uf) - lag(hm, uf))
    sol_t = sp.solve(symmetry_conditions(dl_t, fields, t, tuple(av)), [m1, m2, m3], dict=True)
    want_g = [{m1: 0, m2: cc, m3: -cc}]
    if mut("multiplier_shift_forged"):
        want_g = [{m1: 0, m2: cc, m3: -2 * cc}]
    ok_g = sol_g == want_g
    ok_rot = sp.expand(want_g[0][m3] - (2 * want_g[0][m1] - want_g[0][m2])) == 0
    ok_t = sol_t == [{m1: m2 / 2, m3: 0}]
    checks.check("D2", ok_g and ok_rot and ok_t,
                 "T5: in block 62's cube family M1 sum h'_jj^2 + M2 sum h'_ii h'_jj + M3 sum h'_ij^2 (no metric premise), the gradient relabelling in time with u -> u + (c/K) zeta'' is a symmetry up to a total derivative iff (M1, M2, M3) = (0, c, -c): the rotation-invariant member (M3 = 2 M1 - M2) at beta = -alpha, alpha = -c/2; a transverse relabelling (xi = p x a, symbolic a) is one iff (M1, M2, M3) = (M, 2M, 0), the pure trace term with alpha = 0; both together only for zero (every variational derivative solved exactly at symbolic p)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the mode determinant, the null vector at beta = -alpha, and the light cone."""
    hs = sp.symbols("h11 h12 h13 h22 h23 h33")
    uu = sp.symbols("u")
    hm = sp.Matrix([[hs[0], hs[1], hs[2]], [hs[1], hs[3], hs[4]], [hs[2], hs[4], hs[5]]])
    ok = True
    for pv in (sp.Matrix([1, 2, 2]), sp.Matrix([sp.Rational(2, 5), sp.Rational(1, 3), sp.Rational(-3, 7)])):
        r1, r2 = member_terms(hm, pv)
        lag = XX * (AL * sum(hm[i, j] ** 2 for i in range(3) for j in range(3)) + BE * hm.trace() ** 2) + KK * (uu * r1 + r2)
        mat = sp.hessian(lag, list(hs) + [uu])
        p2 = (pv.T * pv)[0]
        want = -32 * KK ** 2 * XX ** 3 * AL ** 2 * (AL + BE) * p2 ** 2 * (KK * p2 - 4 * XX * AL) ** 2
        if mut("mode_determinant_forged"):
            want = want * 2
        ok = ok and sp.expand(mat.det() - want) == 0
        nv = sp.Matrix([pv[0] * pv[0], pv[0] * pv[1], pv[0] * pv[2], pv[1] * pv[1], pv[1] * pv[2], pv[2] * pv[2], 2 * AL * XX / KK])
        ok = ok and sp.simplify((mat * nv).subs(BE, -AL)) == sp.zeros(7, 1)
        ok = ok and sp.expand(mat * nv - 2 * (AL + BE) * XX * p2 * sp.Matrix([1, 0, 0, 1, 0, 1, 0])) == sp.zeros(7, 1)
        xih = sp.Matrix([pv[1], -pv[0], 0])
        tm = pv * xih.T + xih * pv.T
        nt = sp.Matrix([tm[0, 0], tm[0, 1], tm[0, 2], tm[1, 1], tm[1, 2], tm[2, 2], 0])
        quad = sp.expand((nt.T * mat * nt)[0])
        ok = ok and sp.expand(mat.subs(XX, 0) * nt) == sp.zeros(7, 1) and sp.expand(quad - 4 * AL * XX * p2 * (pv[0] ** 2 + pv[1] ** 2)) == 0
    light = sp.solve(sp.Eq(KK * sp.symbols("P2") / (4 * AL), sp.symbols("P2")), AL) == [KK / 4]
    checks.check("E1", ok and light,
                 "T4: block 62's 7x7 mode determinant (six strains and the rates' multiplier u; block 62 T4 at K = 1) equals -32 K^2 X^3 alpha^2 (alpha + beta)(p^2)^2 (K p^2 - 4 alpha X)^2 at two rational p; M (p p^T, 2 alpha X/K) = 2 (alpha + beta) X p^2 (delta, 0) exactly, so the gradient direction is null at every X iff beta = -alpha; a transverse relabelling (xi = (p2, -p1, 0), u = 0) is null only at X = 0, with quadratic value 4 alpha X p^2 (p1^2 + p2^2) at every ratio: two of the three zero-frequency directions drift uniformly in time within this supplied action for alpha!=0; positive energy requires alpha>0; the travelling pair X = K p^2/(4 alpha) has long-wavelength speed1 iff alpha=K/4 in the stipulated units; finite lattice dispersion remains anisotropic")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 60, 62, 64 and 101 as landed on main, with block 62's frame, symmetric member and kinetic family; it reports what blindness to coin rotations and to relabellings, both varying in time, fixes in the member's kinetic term and what it leaves supplied; block 112 (open) is placed, not used; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Noether", "Fierz", "Lagrange", "Hamilton", "Einstein", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Einstein)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + nm + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + nm + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the coin-rotation shift of the lowered frame rate, antisymmetric for a generic rational frame with symbolic rates",
    "per_site: executed - the invariants I1 + I2, I1 - I2 and (tr K)^2 before and after the rotation; sym(g K) = -g'/(2w)",
    "per_mode: executed - the 7x7 mode determinant at two rational p; the null vector at beta = -alpha; the travelling pair's light-cone condition",
    "per_block: executed - the gradient and transverse relabellings with the fields as symbolic functions of the tick; the cube family's symmetry conditions solved exactly",
    "lattice_wide: at second order in the strains and first order around the identity frame (T1 for every frame); beyond second order the question is block 112's closure; alpha/K, K and the existence of the kinetic term stay declared",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_d2(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print('scope: Supplied ultralocal metric quadratic family and nonzero-alpha transverse obstruction; no axiom-derived dynamics. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
