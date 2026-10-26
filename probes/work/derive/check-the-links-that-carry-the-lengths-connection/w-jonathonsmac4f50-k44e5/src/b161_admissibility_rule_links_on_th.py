#!/usr/bin/env python3
"""Exact checks: links on the bonds make turning the coin a symmetry to all orders; links fixed flat by the frame leave the
walker seeing only the lengths; and links carrying the lengths' own connection add, at long wavelength, exactly the
comparator's inversion-odd curl (1/8) eps.C (a harvest of probe #8843, confirmed by an other-family referee in #9308, with
the supervisor's T4 tying it to block 158).

A (premises): landed blocks 62 and 65 carry the quoted lines (no connection; beyond first order a rotation must be carried
   along each bond).
B (T1): a varying coin rotation turns block 62's bond matrix into U_x (Ebar.s) U_y^dag, which differs from the rotated frame's
   by (1/2)[U_x (E_x.s)(U_y^dag - U_x^dag) + (U_x - U_y)(E_y.s) U_y^dag] and has a coin-scalar part no frame has.
C (T2): the bond matrix (1/2)(E_x.s W + W E_y.s) with an SU(2) link W is covariant under psi -> U psi, E -> R E,
   W -> U_x W U_y^dag; flat links fixed by the frame make every bond the stretch bond conjugated by the lifts.
D (T3): for every state, frame and link field, frame torque + link response = (1/2) d<psi^dag s_c psi>/dt at every site and
   axis; on stationary states the frame torque vanishes iff the link response does.
E (T4): a link W = 1 + (i/2) a.s adds (i/2)(E.a) times the identity to the bond; with a_j the frame's connection along the bond,
   the long-wavelength scalar (1/2) sum_j E^j.a_j equals (1/4) eps_abc omega_abc = (1/8) eps.C (checked through second order).
Exact arithmetic (sympy: Gaussian rationals, rational unit quaternions). The runner scans its own source for floating-point
literals.
"""

from __future__ import annotations

import itertools
import random
import re
import sys
import time
from pathlib import Path

import sympy as sp
from sympy.polys.domains import QQ_I
from sympy.polys.rings import ring


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_LINKS_ON_THE_BONDS_MAKE_TURNING_THE_COIN_A_SYMMETRY_FLAT_LINKS_LEAVE_ONLY_THE_LENGTHS_AND_THE_LENGTHS_CONNECTION_ADDS_THE_INVERSION_ODD_CURL_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_THE_BLIND_WALK_A_SCALAR_HOP_WEIGHTED_BY_THE_TWIST_OF_THE_COIN_ALONG_THE_BOND_MAKES_A_VARYING_ROTATION_OF_THE_COIN_AXES_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-21.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_links_on_the_bonds_make_turning_the_coin_a_symmetry_flat_links_leave_only_the_lengths_and_the_lengths_connection_adds_the_inversion_odd_curl_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED_NEEDLES = (
    (2, "compensated by a connection that this note does not have"),
    (3, "Beyond that a rotation must be carried along each bond"),
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "bond_mismatch_forged": "B",
    "link_covariance_forged": "C",
    "torque_factor_forged": "D",
    "connection_coefficient_forged": "E",
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
            print(f"PASS: {tag} {msg}", flush=True)
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}", flush=True)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


T0 = time.time()
LC = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}


def lc(a, b, c):
    return LC.get((a, b, c), 0)


I = sp.I
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
ONE = sp.eye(2)
ZERO2 = sp.zeros(2, 2)


def vs(v):
    return v[0] * SIG[0] + v[1] * SIG[1] + v[2] * SIG[2]


def su2(q):
    return q[0] * ONE - I * vs(q[1:])


def cayley(v):
    n2 = sum(x * x for x in v)
    return [(1 - n2) / (1 + n2)] + [2 * x / (1 + n2) for x in v]


def rot_of(U):
    R = sp.zeros(3, 3)
    for b in range(3):
        M = U * SIG[b] * U.H
        for a in range(3):
            R[a, b] = sp.simplify(sp.expand((M * SIG[a]).trace() / 2))
    assert all(q.is_Rational for q in R)
    return R


def eq0(M):
    return all(sp.simplify(sp.expand(x)) == 0 for x in M)


def B(Ea, Eb, Wb):
    return (vs(Ea) * Wb + Wb * vs(Eb)) / 2


RQ = random.Random(20260923)


def rq():
    return sp.Rational(RQ.randint(-4, 4), RQ.randint(1, 4))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[0], texts[1]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the frame, the links and the comparator are supplied)")
    needles = list(LANDED_NEEDLES)
    if mut("landed_quote_forged"):
        needles[1] = (3, "Beyond that a rotation is carried along each bond")
    checks.check("A3", all(nd in texts[i] for i, nd in needles), "landed block 62 has no connection (the comparator's is quoted as a comparator) and landed block 65 says that beyond first order a rotation must be carried along each bond, not constructed there")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    Ux, Uy = su2(cayley([rq(), rq(), rq()])), su2(cayley([rq(), rq(), rq()]))
    ok0 = eq0(Ux * Ux.H - ONE) and eq0(Uy * Uy.H - ONE) and sp.simplify(Ux.det()) == 1
    Rx, Ry = rot_of(Ux), rot_of(Uy)
    Ex, Ey = sp.Matrix([rq(), rq(), rq()]), sp.Matrix([rq(), rq(), rq()])
    Ebar = (Ex + Ey) / 2
    M_conj = Ux * vs(Ebar) * Uy.H
    M_frame = vs((Rx * Ex + Ry * Ey) / 2)
    extra = (Ux * vs(Ex) * (Uy.H - Ux.H) + (Ux - Uy) * vs(Ey) * Uy.H) / 2
    if mut("bond_mismatch_forged"):
        extra = (Ux * vs(Ex) * (Uy.H - Ux.H)) / 2
    ok1 = eq0(M_conj - M_frame - extra)
    ok2 = sp.simplify(M_conj.trace()) != 0 and all(sp.simplify(vs(v).trace()) == 0 for v in (Ex, Ey))
    t1 = sp.Matrix(sp.symbols("ta1:4", real=True))
    t2 = sp.Matrix(sp.symbols("tb1:4", real=True))
    ep = sp.symbols("epsilon", real=True)
    U1 = ONE - I * ep * vs(t1) / 2 - ep ** 2 * (t1.dot(t1)) * ONE / 8
    U2 = ONE - I * ep * vs(t2) / 2 - ep ** 2 * (t2.dot(t2)) * ONE / 8
    fo = True
    for j in range(3):
        ej = sp.Matrix([1 if i == j else 0 for i in range(3)])
        Mb = (U1 * SIG[j] * U2.H).applyfunc(lambda z: sp.expand(z).coeff(ep, 1))
        target = vs(((t1 + t2) / 2).cross(ej)) + (I / 2) * (t2[j] - t1[j]) * ONE
        fo &= eq0(Mb - target)
    checks.check("B1", ok0 and ok1 and ok2 and fo, "exact rational SU(2) turns (Cayley) and rational frames: U_x (Ebar.s) U_y^dag - ((R_x E_x + R_y E_y)/2).s = (1/2)[U_x (E_x.s)(U_y^dag - U_x^dag) + (U_x - U_y)(E_y.s) U_y^dag], with a nonzero trace that no frame bond has; at first order it is block 65's frame rotation plus the twist (i/2)(th_y - th_x)_j")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    Ux, Uy = su2(cayley([rq(), rq(), rq()])), su2(cayley([rq(), rq(), rq()]))
    Rx, Ry = rot_of(Ux), rot_of(Uy)
    Ex, Ey = sp.Matrix([rq(), rq(), rq()]), sp.Matrix([rq(), rq(), rq()])
    W = su2(cayley([rq(), rq(), rq()]))
    Wt = Ux * W * Ux.H if mut("link_covariance_forged") else Ux * W * Uy.H
    okcov = eq0(B(Rx * Ex, Ry * Ey, Wt) - Ux * B(Ex, Ey, W) * Uy.H) and eq0(B(Ex, Ey, ONE) - vs((Ex + Ey) / 2))
    Sx = sp.zeros(3, 3)
    Sy = sp.zeros(3, 3)
    for i in range(3):
        for j in range(i, 3):
            Sx[i, j] = Sx[j, i] = rq() + (3 if i == j else 0)
            Sy[i, j] = Sy[j, i] = rq() + (3 if i == j else 0)
    Uhx, Uhy = su2(cayley([rq(), rq(), rq()])), su2(cayley([rq(), rq(), rq()]))
    Rhx, Rhy = rot_of(Uhx), rot_of(Uhy)
    flat = True
    for j in range(3):
        flat &= eq0(B((Rhx * Sx)[:, j], (Rhy * Sy)[:, j], Uhx * Uhy.H) - Uhx * B(Sx[:, j], Sy[:, j], ONE) * Uhy.H)
    lift = eq0(rot_of(-Ux) - Rx)
    checks.check("C1", okcov and flat and lift, "the bond (1/2)(E_x.s W + W E_y.s) is covariant, B[R_x E_x, R_y E_y, U_x W U_y^dag] = U_x B U_y^dag, and at W = 1 it is block 62's bond; with E = R_E S and flat links W = Uhat_x Uhat_y^dag every bond is Uhat_x B[S_x, S_y, 1] Uhat_y^dag, so the walker sees only S = sqrt(g); a lift fixes the link up to a site sign")


# ============================================================================================ family D (T3)
def build(L, E, Wl, psi):
    sites = list(itertools.product(range(L), repeat=3))
    sh = lambda x, j, s=1: tuple((x[i] + (s if i == j else 0)) % L for i in range(3))
    Bb = {(x, j): B(E[x][:, j], E[sh(x, j)][:, j], Wl[(x, j)]) for x in sites for j in range(3)}
    Hpsi = {}
    for x in sites:
        v = sp.zeros(2, 1)
        for j in range(3):
            v += Bb[(x, j)] * psi[sh(x, j)] / (2 * I)
            xm = sh(x, j, -1)
            v += (Bb[(xm, j)] / (2 * I)).H * psi[xm]
        Hpsi[x] = v.applyfunc(sp.expand)
    return sites, sh, Bb, Hpsi


def noether(L, E, Wl, psi):
    sites, sh, Bb, Hpsi = build(L, E, Wl, psi)
    out = {}
    for x in sites:
        for c in range(3):
            ec = sp.Matrix([1 if i == c else 0 for i in range(3)])
            frame = 0
            for j in range(3):
                y, xm = sh(x, j), sh(x, j, -1)
                dE = ec.cross(E[x][:, j])
                d1 = (vs(dE) * Wl[(x, j)]) / 2
                d2 = (Wl[(xm, j)] * vs(dE)) / 2
                frame += 2 * sp.re((psi[x].H * d1 * psi[y])[0] / (2 * I)) + 2 * sp.re((psi[xm].H * d2 * psi[x])[0] / (2 * I))
            link = 0
            for j in range(3):
                y, xm = sh(x, j), sh(x, j, -1)
                dW1 = -I * SIG[c] * Wl[(x, j)] / 2
                dW2 = I * Wl[(xm, j)] * SIG[c] / 2
                link += 2 * sp.re((psi[x].H * B(E[x][:, j], E[y][:, j], dW1) * psi[y])[0] / (2 * I))
                link += 2 * sp.re((psi[xm].H * B(E[xm][:, j], E[x][:, j], dW2) * psi[x])[0] / (2 * I))
            dG = -sp.im(sp.expand((Hpsi[x].H * SIG[c] * psi[x])[0]))
            out[(x, c)] = (sp.simplify(sp.expand(frame)), sp.simplify(sp.expand(link)), sp.simplify(sp.expand(dG)))
    return out


def family_d(checks: Checks) -> None:
    L = 3
    sites3 = list(itertools.product(range(L), repeat=3))
    E3 = {x: sp.Matrix(3, 3, lambda i, j: rq() + (2 if i == j else 0)) for x in sites3}
    W3 = {(x, j): su2(cayley([rq(), rq(), rq()])) for x in sites3 for j in range(3)}
    P3 = {x: sp.Matrix([rq() + I * rq(), rq() + I * rq()]) for x in sites3}
    res = noether(L, E3, W3, P3)
    fac = 2 if mut("torque_factor_forged") else 1
    ident = all(sp.simplify(f + l - fac * g) == 0 for f, l, g in res.values())
    nontriv = sum(1 for f, l, g in res.values() if f != 0 and l != 0 and g != 0)
    checks.check("D1", ident and nontriv > 60, f"for a random exact state, frame and link field on the 3^3 torus: frame torque + link response = (1/2) d<psi^dag s_c psi>(x)/dt at all {len(res)} site-axis pairs ({nontriv} with every term nonzero)")
    L4 = 4
    sites4 = list(itertools.product(range(L4), repeat=3))
    coins = [sp.Matrix([1, 1]), sp.Matrix([1, I]), sp.Matrix([1, 0])]
    P4 = {x: sum((I ** x[j] * coins[j] for j in range(3)), sp.zeros(2, 1)) for x in sites4}
    Eid = {x: sp.eye(3) for x in sites4}
    W1 = {(x, j): ONE for x in sites4 for j in range(3)}
    _, _, _, Hp4 = build(L4, Eid, W1, P4)
    eig = all(eq0(Hp4[x] - P4[x]) for x in sites4)
    res4 = noether(L4, Eid, W1, P4)
    f_nz = sum(1 for f, l, g in res4.values() if f != 0)
    no_link = all(g == 0 and sp.simplify(f + l) == 0 for f, l, g in res4.values()) and f_nz > 0
    Uh = {x: su2(cayley([rq(), rq(), rq()])) for x in sites4}
    Er = {x: rot_of(Uh[x]) for x in sites4}
    sh4 = lambda x, j: tuple((x[i] + (1 if i == j else 0)) % L4 for i in range(3))
    Wf = {(x, j): Uh[x] * Uh[sh4(x, j)].H for x in sites4 for j in range(3)}
    Pr = {x: (Uh[x] * P4[x]).applyfunc(sp.expand) for x in sites4}
    _, _, _, Hpr = build(L4, Er, Wf, Pr)
    eig2 = all(eq0(Hpr[x] - Pr[x]) for x in sites4)
    resr = noether(L4, Er, Wf, Pr)
    tot0 = all(sp.simplify(f + l) == 0 and g == 0 for f, l, g in resr.values())
    checks.check("D2", eig and no_link and eig2 and tot0, f"on the exactly stationary 4^3 state sum_j i^(x_j) c_j (energy +1): with no links the frame torque is nonzero at {f_nz} of {len(res4)} pairs and equals minus the link response; with flat links fixed by a rotated frame the dressed state is again an eigenstate and the total torque vanishes at every pair")


# ============================================================================================ family E (T4, the supervisor's)
def connection_scalar_vs_curl(sym: bool, coef):
    """At a point, with generic jets of the covector frame e = 1 + s eta: (1/2) sum_j E^j_c a_{j,c} with
    a_{j,c} = (1/2) eps_cab omega_jab equals coef * eps.C through s^2 (claim: coef = 1/8)."""
    pairs = [(a, i) for a in range(3) for i in range(3) if (not sym or a <= i)]
    names = [f"v{a}{i}" for (a, i) in pairs] + [f"d{a}{i}_{k}" for (a, i) in pairs for k in range(3)] + ["s"]
    Rb, *G = ring(names, QQ_I)
    g = dict(zip(names, G))
    s = g["s"]
    one, zero = Rb.one, Rb.zero
    isx = names.index("s")

    def trb(p):
        return Rb({m: c for m, c in p.items() if m[isx] <= 2})

    def ent(a, i, k=None):
        key = (a, i) if (a, i) in pairs else (i, a)
        return g[f"v{key[0]}{key[1]}"] if k is None else g[f"d{key[0]}{key[1]}_{k}"]

    def mmb(A, Bm):
        return [[trb(sum((A[p][q] * Bm[q][r] for q in range(3)), zero)) for r in range(3)] for p in range(3)]
    e0 = [[(one if a == i else zero) + s * ent(a, i) for i in range(3)] for a in range(3)]
    de = [[[s * ent(a, i, k) for i in range(3)] for a in range(3)] for k in range(3)]
    A = [[e0[a][i] - (one if a == i else zero) for i in range(3)] for a in range(3)]
    A2 = mmb(A, A)
    E0 = [[trb((one if i == a else zero) - A[i][a] + A2[i][a]) for a in range(3)] for i in range(3)]
    dE = [[[-x for x in row] for row in mmb(mmb(E0, de[k]), E0)] for k in range(3)]
    dg = [[[trb(sum((de[k][a][i] * e0[a][j] + e0[a][i] * de[k][a][j] for a in range(3)), zero)) for j in range(3)] for i in range(3)] for k in range(3)]
    gi = [[trb(sum((E0[i][a] * E0[j][a] for a in range(3)), zero)) for j in range(3)] for i in range(3)]
    Chr = [[[trb(sum((gi[k][l] * (dg[i][l][j] + dg[j][l][i] - dg[l][i][j]) for l in range(3)), zero) / 2) for j in range(3)] for i in range(3)] for k in range(3)]

    def om(j, a, b):
        return trb(sum((e0[a][k] * (dE[j][k][b] + sum((Chr[k][j][l] * E0[l][b] for l in range(3)), zero)) for k in range(3)), zero))
    V = zero
    for j in range(3):
        a_j = [trb(sum((lc(c, a, b) * om(j, a, b) for a in range(3) for b in range(3)), zero) / 2) for c in range(3)]
        V = trb(V + sum((E0[j][c] * a_j[c] for c in range(3)), zero) / 2)
    Bc = trb(sum((sg * E0[i][b] * E0[j][c] * (de[i][a][j] - de[j][a][i]) for (a, b, c), sg in LC.items() for i in range(3) for j in range(3)), zero))
    return trb(V - coef * Bc) == 0


def family_e(checks: Checks) -> None:
    a = sp.Matrix(sp.symbols("a1:4", real=True))
    Ev = sp.Matrix(sp.symbols("E1:4", real=True))
    ep = sp.symbols("epsilon", real=True)
    Wlin = ONE + I * ep * vs(a) / 2
    first = (B(Ev, Ev, Wlin) - vs(Ev)).applyfunc(lambda z: sp.expand(z).coeff(ep, 1))
    ok_bond = eq0(first - (I / 2) * (Ev.dot(a)) * ONE)
    coef = QQ_I(sp.Rational(1, 4) if mut("connection_coefficient_forged") else sp.Rational(1, 8), 0)
    ok_gen = connection_scalar_vs_curl(False, coef)
    ok_sym = connection_scalar_vs_curl(True, coef)
    checks.check("E1", ok_bond and ok_gen and ok_sym, "a link W = 1 + (i/2) a.s adds (i/2)(E.a) times the identity to the bond at first order, i.e. the scalar hop (1/4)(E.a)(psi_x^dag psi_y + h.c.), whose long-wavelength value on smooth zero-corner states is (1/2) E.a per bond direction; with a_j the frame's own connection along the bond (a_{j,c} = (1/2) eps_cab omega_jab), (1/2) sum_j E^j.a_j = (1/4) eps_abc omega_abc = (1/8) eps.C through second order, for general and for symmetric frames with generic jets")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 62 and 65 as landed on main (the walker's framed coupling and what turning the coin does at first order); it reports links on the bonds that make turning the coin a symmetry to all orders, what flat links and links carrying the lengths' connection give, and the torque balance; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at flat links."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Ivanenko", "Belinfante", "Rosenfeld", "Cartan", "Kibble",
                   "Sciama", "Hehl", "Wilson", "Pauli", "Fierz", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace", "Poisson", "Gauss", "Planck", "Green", "Hamilton",
                   "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Weyl) —", 1)
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
            if re.search(r"\b" + re.escape(nm) + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + re.escape(nm) + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the bond identities with exact rational SU(2) turns, frames and links",
    "per_site: executed - the torque balance at every site and axis of a 3^3 torus with random exact data",
    "per_mode: executed - the exactly stationary 4^3 state, with no links and with flat links fixed by a rotated frame",
    "per_block: executed - the link's first-order bond term and the connection scalar against (1/8) eps.C at a point, generic jets through second order",
    "lattice_wide: checked and not executed - a nearest-neighbour rule fixing the links from the lengths on the lattice, link dynamics, and the eight species",
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
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: SU(2) links on the bonds (1/2)(E_x.s W + W E_y.s): turning the coin a symmetry to all orders; flat links fixed by the frame leave only sqrt(g); frame torque + link response = (1/2) d<s_c>/dt; links carrying the lengths' connection add (1/8) eps.C at long wavelength; harvest of #8843 (confirmed by #9308) with the supervisor's T4; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
