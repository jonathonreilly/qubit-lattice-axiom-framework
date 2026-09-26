#!/usr/bin/env python3
"""Exact checks: in block 62's cube kinetic family, relabellings in time fix the kinetic term's shape, and the frame's full rate
has four cube-invariant numbers of which blindness to coin rotations removes one (a harvest of probe #9225, confirmed by an
other-family referee in #9312). Block 62's member (R1, R2, the multiplier u, K), cube kinetic family
T = M1 sum h'_jj^2 + M2 sum h'_ii h'_jj + M3 sum h'_ij^2, rotation-rate coefficient N, relabelling d eps = -xi p^T:

A (premises): landed block 124's premise (a kinetic term built with the metric alone) and the axioms.
B (T1): the gradient relabelling in time is a symmetry iff (M1, M2, M3) = (0, c, -c) with u -> u + (c/K) zeta'' (the change a
   total derivative d(c zeta' R1)/dt); the transverse one iff (M, 2M, 0), N = 0, no shift; both only for zero.
C (T2): quadratic forms in the frame's full rate invariant under the cube group: exactly four numbers; blindness to coin
   rotations in time removes the antisymmetric one, leaving three (block 124's count of two uses its metric premise); rotation
   blindness with the gradient demand leaves block 62's member at beta = -alpha.
D (T3): the survivor (0, c, -c), c = -2 alpha: one travelling transverse traceless pair X = K p^2/(4 alpha); the gradient gauge
   direction; drifting transverse relabellings; the rotation block decouples.
Exact (sympy). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
import time
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_IN_THE_CUBE_KINETIC_FAMILY_RELABELLINGS_IN_TIME_FIX_THE_KINETIC_SHAPE_AND_THE_FRAMES_FULL_RATE_HAS_FOUR_NUMBERS_OF_WHICH_BLINDNESS_REMOVES_ONE_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_BLINDNESS_TO_COIN_ROTATIONS_THAT_VARY_IN_TIME_LEAVES_EXACTLY_BLOCK_62S_TWO_KINETIC_NUMBERS_AND_NO_RATIO_MAKES_A_TRANSVERSE_RELABELLING_IN_TIME_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-24.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_in_the_cube_kinetic_family_relabellings_in_time_fix_the_kinetic_shape_and_the_frames_full_rate_has_four_numbers_of_which_blindness_removes_one_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "gradient_shift_forged": "B",
    "cube_count_forged": "C",
    "mode_root_forged": "D",
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
RES: list = []


def check(tag, ok, msg):
    RES.append((tag, bool(ok), msg))


# ============================================================================================ the probe's machinery (#9225, ported)
t = sp.symbols('t')
p1, p2, p3, K = sp.symbols('p1 p2 p3 K', real=True)
M1, M2, M3, N = sp.symbols('M1 M2 M3 N', real=True)
cs = sp.symbols('c0:4', real=True)            # multiplier shift coefficients
b1, b2, b3 = sp.symbols('b1 b2 b3', real=True)
P = sp.Matrix([p1, p2, p3])
PAIRS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
OFF = [(0, 1), (0, 2), (1, 2)]
hf = {ij: sp.Function('h%d%d' % (ij[0] + 1, ij[1] + 1))(t) for ij in PAIRS}
wf = {ij: sp.Function('w%d%d' % (ij[0] + 1, ij[1] + 1))(t) for ij in OFF}
u = sp.Function('u')(t)
z = sp.Function('zeta')(t)


def sym(f):
    H = sp.zeros(3)
    for (i, j), v in f.items():
        H[i, j] = v; H[j, i] = v
    return H


def asym(f):
    W = sp.zeros(3)
    for (i, j), v in f.items():
        W[i, j] = v; W[j, i] = -v
    return W


H, W = sym(hf), asym(wf)


def R1(H):
    return P.dot(P) * H.trace() - (P.T * H * P)[0]


def R2(H):
    q = P.dot(P); hp = H * P
    return -q / 4 * (H * H).trace() + hp.dot(hp) / 2 - (P.T * H * P)[0] * H.trace() / 2 + q / 4 * H.trace() ** 2


def Tcube(Hd):
    return (M1 * sum(Hd[j, j] ** 2 for j in range(3)) + M2 * sum(Hd[i, i] * Hd[j, j] for i, j in OFF)
            + M3 * sum(Hd[i, j] ** 2 for i, j in OFF))


def Lag(H, u, W):
    Wd = W.diff(t)
    return Tcube(H.diff(t)) + N * sum(Wd[i, j] ** 2 for i, j in OFF) + K * (u * R1(H) + R2(H))


FIELDS = list(hf.values()) + list(wf.values()) + [u, z]


def euler(expr, f, order=4):
    e = sp.diff(expr, f)
    for n in range(1, order + 1):
        e += (-1) ** n * sp.diff(sp.diff(expr, sp.diff(f, t, n)), t, n)
    return sp.expand(e)


def conditions(dL, extra_syms=()):
    """coefficients (in field derivatives, p and extra symbols) of every Euler derivative of dL"""
    derivs = [sp.diff(g, t, n) for g in FIELDS for n in range(8, -1, -1)]
    reps = {d: sp.Symbol('D%d' % k) for k, d in enumerate(derivs)}
    eqs = set()
    for f in FIELDS:
        E = euler(dL, f).subs(reps)
        if E == 0:
            continue
        for cf in sp.Poly(E, *reps.values()).coeffs():
            for cc in sp.Poly(sp.expand(cf), p1, p2, p3, *extra_syms).coeffs():
                eqs.add(cc)
    return list(eqs)


du = sum(cs[n] * sp.diff(z, t, n) for n in range(4))
L0 = Lag(H, u, W)



def run_probe_checks():
    du = sum(cs[n] * sp.diff(z, t, n) for n in range(4))
    L0 = Lag(H, u, W)

    # ---------------------------------------------------------------- A: forms in h' (block 124 T5's family) and the rotation part
    xi_g = P * z / 2                                  # gradient relabelling: d h = p p^T zeta (d eps = -xi p^T symmetric)
    dL = sp.expand(Lag(H + P * xi_g.T + xi_g * P.T, u + du, W) - L0)
    eq_g = conditions(dL)
    sol_g = sp.solve(eq_g, [M1, M2, M3, N] + list(cs), dict=True)
    c = sp.Symbol('c')
    lam = sp.expand(dL.subs({M1: 0, M2: c, M3: -c, cs[0]: 0, cs[1]: 0, cs[2]: c / K, cs[3]: 0}))
    Lam = c * z.diff(t) * R1(H)                        # explicit total-derivative witness
    ok = sol_g == [{M1: 0, M2: (2 if mut('gradient_shift_forged') else 1) * K * cs[2], M3: -K * cs[2], cs[0]: 0, cs[1]: 0, cs[3]: 0}] and sp.simplify(lam - Lam.diff(t)) == 0
    check("A1", ok, "gradient relabelling h -> h + p p^T zeta(t) with u -> u + sum_n c_n zeta^(n): a symmetry iff "
          "(M1, M2, M3) = (0, c, -c) and u -> u + (c/K) zeta'' (c_0 = c_1 = c_3 = 0), N free; change = d(c zeta' R1)/dt")

    xi_t = P.cross(sp.Matrix([b1, b2, b3])) * z        # transverse: xi = (p x b) zeta(t)
    dom = (P * xi_t.T - xi_t * P.T) / 2               # omega's change from d eps = -xi p^T
    dL = sp.expand(Lag(H + P * xi_t.T + xi_t * P.T, u + du, W + dom) - L0)
    eq_t = conditions(dL, (b1, b2, b3))
    sol_t = sp.solve(eq_t, [M2, M3, N] + list(cs), dict=True)
    ok = sol_t == [{M2: 2 * M1, M3: 0, N: 0, cs[0]: 0, cs[1]: 0, cs[2]: 0, cs[3]: 0}]
    dL0 = sp.expand(Lag(H + P * xi_t.T + xi_t * P.T, u, W + dom).subs({M2: 2 * M1, M3: 0, N: 0}) - L0.subs({M2: 2 * M1, M3: 0, N: 0}))
    check("A2", ok and dL0 == 0, "transverse relabelling xi = (p x b) zeta(t): a symmetry iff (M1, M2, M3) = (M, 2M, 0), N = 0 and no "
          "multiplier shift; then the Lagrangian is exactly unchanged (the pure trace term M (tr h')^2)")
    both = sp.solve(eq_g + eq_t, [M1, M2, M3, N] + list(cs), dict=True)
    check("A3", both == [{M1: 0, M2: 0, M3: 0, N: 0, cs[0]: 0, cs[1]: 0, cs[2]: 0, cs[3]: 0}],
          "both relabelling demands together (the union of all Euler-operator conditions): only the zero kinetic term")

    V = sp.Matrix(3, 3, sp.symbols('v0:9'))
    vec = list(V)
    Q = sp.Matrix(9, 9, lambda i, j: sp.Symbol('q_%d_%d' % (min(i, j), max(i, j))))
    qs = sorted(Q.free_symbols, key=str)
    R4 = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])          # quarter turn about e3
    R3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])           # third turn about (1,1,1)
    Pi = sp.Matrix([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])        # inversion
    eqs = []
    for R in (R4, R3, Pi):
        Vr = list(R * V * R.T)
        A = sp.Matrix(9, 9, lambda i, j: sp.diff(Vr[i], vec[j]))  # linear action on the 9 components
        eqs += list(A.T * Q * A - Q)
    solQ = sp.solve(eqs, qs, dict=True)[0]
    Qg = Q.subs(solQ)
    free = sorted(Qg.free_symbols, key=str)
    S_ = (V + V.T) / 2; A_ = (V - V.T) / 2
    basis = [sum(V[j, j] ** 2 for j in range(3)), sum(V[i, i] * V[j, j] for i, j in OFF),
             sum(S_[i, j] ** 2 for i, j in OFF), sum(A_[i, j] ** 2 for i, j in OFF)]
    form = sp.expand((sp.Matrix([vec]) * Qg * sp.Matrix(vec))[0])
    cb = sp.symbols('k0:4')
    match = sp.solve(sp.Poly(sp.expand(form - sum(k * bb for k, bb in zip(cb, basis))), *vec).coeffs(), cb + tuple(free), dict=True)
    ok = len(free) == (5 if mut('cube_count_forged') else 4) and len(match) == 1 and all(match[0].get(k) is not None for k in cb) and len(set(match[0][k] for k in cb)) == 4
    check("B1", ok, "quadratic forms in the frame's full rate V (9 components) invariant under the cube group (V -> R V R^T): "
          "exactly 4 numbers, sum V_jj^2, sum V_ii V_jj, sum sym(V)_ij^2 and sum antisym(V)_ij^2; no cross term (T1g vs T2g)")
    Om = asym({ij: sp.Symbol('o%d%d' % ij) for ij in OFF})
    n1, n2, n3, n4 = sp.symbols('n1:5')
    Qn = n1 * basis[0] + n2 * basis[1] + n3 * basis[2] + n4 * basis[3]
    shift = sp.expand(Qn.subs({vec[k]: (V + Om)[k] for k in range(9)}, simultaneous=True) - Qn)
    okb = sp.solve(sp.Poly(shift, *vec, *Om.free_symbols).coeffs(), [n1, n2, n3, n4], dict=True) == [{n4: 0}]
    check("B2", okb, "blindness to coin rotations in time (V -> V + antisymmetric, arbitrary at each tick; block 124 T1): iff the "
          "antisymmetric number vanishes; the other three are free (block 62's cube family), so a count of two needs T1's metric premise")
    check("B3", sol_g[0].get(N, N) == N and sol_t[0][N] == 0,
          "with the rotation part N: the gradient demand leaves N free (a gradient relabelling does not rotate the frame); the "
          "transverse demand forces N = 0; rotation blindness + gradient -> (0, c, -c, 0) = block 62's member at beta = -alpha")

    X = sp.Symbol('X')
    al = sp.Symbol('alpha', positive=True)
    qv = list(hf.values()) + [u] + list(wf.values())
    sub = {M1: 0, M2: -2 * al, M3: 2 * al}
    Lk = sp.expand(Tcube(H.diff(t)).subs(sub) + N * sum(W.diff(t)[i, j] ** 2 for i, j in OFF))
    Lp = sp.expand(K * (u * R1(H) + R2(H)))
    dq = [sp.diff(q, t) for q in qv]
    A = sp.Matrix(10, 10, lambda i, j: sp.diff(Lk, dq[i], dq[j]))
    C = sp.Matrix(10, 10, lambda i, j: sp.diff(Lp, qv[i], qv[j]))
    spec = {}
    PV = ((1, 2, 2), (sp.Rational(2, 5), sp.Rational(1, 3), -sp.Rational(3, 7)))
    for pv in PV:
        rep = {p1: pv[0], p2: pv[1], p3: pv[2], K: 1, al: 1}
        Mx = (X * A + C).subs(rep)
        Mh = Mx[:7, :7]                                # (h, u) block; the rotation block decouples
        r = Mh.rank()
        g = 0
        for rows in itertools.combinations(range(7), r):
            for cols in itertools.combinations(range(7), r):
                g = sp.gcd(g, Mh.extract(list(rows), list(cols)).det())
        spec[pv] = (r, sp.factor(g), Mx[7:, :7].is_zero_matrix and Mx[:7, 7:].is_zero_matrix, sp.factor(Mx[7:, 7:].det()))
    ok = True
    for pv in PV:
        r, g, dec, rot = spec[pv]
        q2 = sum(v ** 2 for v in pv)
        roots = sp.roots(sp.Poly(g, X))
        ok &= r == 6 and dec and roots.get(sp.Rational(q2, (2 if mut('mode_root_forged') else 4))) == 2 and set(roots) <= {0, sp.Rational(q2, 4)}
        ok &= sp.simplify(rot - 8 * N ** 3 * X ** 3) == 0
    check("C1", ok, "survivor (0, c, -c), c = -2 alpha, K = alpha = 1, at p = (1,2,2) and (2/5,1/3,-3/7): the (h, u) pencil X A + C "
          "has normal rank 6 (one gauge direction) and the gcd of its 6x6 minors is " + str(spec[PV[0]][1]) + " at the first p: "
          "roots X = p^2/4 twice (the travelling pair) and X = 0; the rotation block decouples with det (2 N X)^3")
    # the travelling pair is transverse traceless; the gradient direction is null at every X
    pv = (1, 2, 2); rep = {p1: 1, p2: 2, p3: 2, K: 1, al: 1, N: 1}
    Mx = (X * A + C).subs(rep)
    gvec = sp.Matrix([1, 4, 4, 2, 2, 4, 0, 0, 0, 0])      # h = p p^T at p = (1,2,2)
    gvec[6] = 2 * X                                      # u = 2 alpha X / K
    ns = Mx.subs(X, sp.Rational(9, 4)).nullspace()
    NS = sp.Matrix.hstack(*ns)
    # transverse traceless vectors with u = 0 and no rotation, inside the null space
    y = sp.symbols('y0:%d' % len(ns))
    v = NS * sp.Matrix(y)
    Hv = sp.Matrix(3, 3, lambda i, j: v[PAIRS.index((min(i, j), max(i, j)))])
    cons = list(Hv * sp.Matrix(pv)) + [Hv.trace(), v[6], v[7], v[8], v[9]]
    tt_dim = len(ns) - sp.Matrix([[sp.diff(cc, yy) for yy in y] for cc in cons]).rank()
    g_in = sp.Matrix.hstack(NS, gvec.subs(X, sp.Rational(9, 4))).rank() == len(ns)
    check("C2", len(ns) == 3 and tt_dim == 2 and g_in and sp.simplify(Mx * gvec) == sp.zeros(10, 1),
          "at X = p^2/4 the null space is 3-dimensional: the transverse traceless pair (u = 0, no rotation) plus the gauge "
          "vector (p p^T, u = 2 alpha X/K), which is null at every X: the gradient relabelling with the multiplier")



# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[0], texts[1]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the member, its kinetic family and the relabellings are supplied)")
    needle = "built with the metric alone" if not mut("landed_quote_forged") else "built with the frame alone"
    checks.check("A3", needle in texts[2], "landed block 124's premise: the kinetic term is a constant-coefficient ultralocal quadratic form in the frame's rate built with the metric alone")


def results():
    if not RES:
        run_probe_checks()
    return {tag: (ok, msg) for tag, ok, msg in RES}


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    r = results()
    ok = r["A1"][0] and r["A2"][0] and r["A3"][0]
    checks.check("B1", ok, "gradient relabelling in time: a symmetry iff (M1, M2, M3) = (0, c, -c) with u -> u + (c/K) zeta'' (change d(c zeta' R1)/dt); transverse: iff (M, 2M, 0), N = 0, no shift (Lagrangian unchanged); both: only zero")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    r = results()
    ok = r["B1"][0] and r["B2"][0] and r["B3"][0]
    checks.check("C1", ok, "the frame's full rate: exactly four cube-invariant quadratic numbers (trace, traceless diagonal, symmetric off-diagonal, antisymmetric); blindness to coin rotations in time removes the antisymmetric one and leaves three, so block 124's count of two uses its metric premise; rotation blindness with the gradient demand leaves block 62's member at beta = -alpha")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    r = results()
    ok = r["C1"][0] and r["C2"][0]
    checks.check("D1", ok, "the survivor (0, c, -c), c = -2 alpha: the (h, u) pencil has normal rank 6, the gcd of its maximal minors has the double root X = p^2/4 (the transverse traceless pair) and X = 0; the gradient gauge vector is null at every X; the rotation block decouples with det (2 N X)^3")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 62, 101 and 124 as landed on main (the member, its kinetic family, the rate as a multiplier and blindness to coin rotations in time); it reports which kinetic terms of the cube family the relabellings in time allow, and how many numbers the frame's full rate carries; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at four numbers."}
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
    "per_element: executed - the Euler-operator conditions of both relabellings for every field",
    "per_site: executed - the cube-invariant quadratic forms in the nine rate components",
    "per_mode: executed - the survivor's pencil at two rational wave vectors; the null space at X = p^2/4",
    "per_block: executed - the union of both demands; rotation blindness with each",
    "lattice_wide: checked and not executed - orders beyond the second in the strain, and a field for the drifting transverse relabellings",
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
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: block 62's cube kinetic family: gradient relabellings in time need (0, c, -c) with shift (c/K) zeta'', transverse need (M, 2M, 0), both only zero; the frame's full rate has four cube numbers, blindness removes one; harvest of #9225 (confirmed by #9312); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
