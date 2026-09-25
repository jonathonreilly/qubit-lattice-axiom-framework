#!/usr/bin/env python3
"""Exact checks: one light cone from the source link - at the closing ratio beta = -alpha the member's equations demand
e'' = -(K wbar^2/(4 alpha)) p.Theta.p; for the walker's smooth states every beat of two waves obeys e'' = -wbar^2 p.Theta.p at
leading order; so the walker can be the member's long-wave content iff alpha = K/4, the member's disturbances then moving at
the walker's top speed; lattice corrections are of relative order |k|^2, and the six partly reflected species fail (the
supervisor's own derivation; blocks 54, 62 and 101 as landed; blocks 112 and 124 placed; not adopted).

B (T1): the identity, re-derived from block 101's action and block 62's coupling.
C (T2): the walker's beats at leading order, near k = 0 and near pi(1,1,1).
D (T3): the lattice corrections.
E (T4): one light cone, and the other six species.
Exact symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_FROM_THE_SOURCE_LINK_THE_WALKERS_SMOOTH_STATES_MEET_THE_MEMBERS_IDENTITY_AT_LEADING_ORDER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_one_light_cone_from_the_source_link_the_walkers_smooth_states_meet_the_members_identity_at_leading_order_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "closing_ratio_forged": "B",
    "leading_ratio_forged": "C",
    "lattice_correction_forged": "D",
    "light_cone_forged": "E",
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
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, the member, its kinetic term and the source link are supplied; the memo does not define a time metric)")


# ============================================================================================ the member's identity and the walker's beats
S1M = sp.Matrix([[0, 1], [1, 0]])
S2M = sp.Matrix([[0, -sp.I], [sp.I, 0]])
S3M = sp.Matrix([[1, 0], [0, -1]])
PAIRS = (((1, 2, 2), (2, 3, 6)), ((4, 4, 7), (2, 6, 9)), ((1, 2, 2), (2, 6, 9)))


def lead_ratio(kap, kapp, sg, br=(1, 1)):
    """leading-order ratio (l - l')^2 (l + l') u'^dag u / [(q.M)(q.(s + s'))] for two eigen-waves of the walker near the species
    corner pi n (coin signs sg_a = cos(pi n_a)), with small offsets kap, kapp (rational norms) and energies l = br_0 E, l' = br_1 E'
    (either branch); u = (l + s_3, s_1 + i s_2) is the eigenvector of sigma.s for l, and M_a = u'^dag sigma_a u."""
    s = [sg[i] * kap[i] for i in range(3)]
    s_p = [sg[i] * kapp[i] for i in range(3)]
    q = [kap[i] - kapp[i] for i in range(3)]
    lam = br[0] * sp.sqrt(sum(v ** 2 for v in s))
    lam_p = br[1] * sp.sqrt(sum(v ** 2 for v in s_p))
    uu = sp.Matrix([lam + s[2], s[0] + sp.I * s[1]])
    up = sp.Matrix([lam_p + s_p[2], s_p[0] + sp.I * s_p[1]])
    mm = [(up.H * sg_m * uu)[0] for sg_m in (S1M, S2M, S3M)]
    num = (lam - lam_p) ** 2 * (lam + lam_p) * (up.H * uu)[0]
    den = sum(q[i] * mm[i] for i in range(3)) * sum(q[i] * (s[i] + s_p[i]) for i in range(3))
    return sp.nsimplify(sp.simplify(num / den))


def lattice_ratio(kap, kapp):
    """the same ratio with the lattice's sin k, 2 sin(q/2) and eigenvectors, for k = t kap, k' = t kapp, scaled by t."""
    tt = sp.symbols("t", positive=True)
    f = [sp.sin(tt * v) / tt if v != 0 else sp.Integer(0) for v in kap]
    fp = [sp.sin(tt * v) / tt if v != 0 else sp.Integer(0) for v in kapp]
    pq = [2 * sp.sin(tt * (kap[i] - kapp[i]) / 2) / tt if kap[i] != kapp[i] else sp.Integer(0) for i in range(3)]
    ff = sp.sqrt(sum(v ** 2 for v in f))
    ffp = sp.sqrt(sum(v ** 2 for v in fp))
    uu = sp.Matrix([ff + f[2], f[0] + sp.I * f[1]])
    up = sp.Matrix([ffp + fp[2], fp[0] + sp.I * fp[1]])
    mm = [(up.H * sg_m * uu)[0] for sg_m in (S1M, S2M, S3M)]
    num = (ff - ffp) ** 2 * (ff + ffp) * (up.H * uu)[0]
    den = sum(pq[i] * mm[i] for i in range(3)) * sum(pq[i] * (f[i] + fp[i]) for i in range(3))
    return tt, num / den


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: at beta = -alpha the member's equations demand e'' = -(K wbar^2/(4 alpha)) p.Theta.p."""
    t = sp.symbols("t")
    al, kk, wb, p = sp.symbols("alpha K wbar p", positive=True)
    phi, a, b, cx, cy, xi, u = [sp.Function(n)(t) for n in ("phi", "a", "b", "cx", "cy", "xi", "u")]
    e = sp.Function("e")(t)
    th = sp.Matrix(3, 3, lambda i, j: sp.Function("Theta_%d%d" % (min(i, j) + 1, max(i, j) + 1))(t))
    h = sp.Matrix([[phi + a, b, cx], [b, phi - a, cy], [cx, cy, 2 * xi]])
    hd = h.diff(t)
    be = -al
    if mut("closing_ratio_forged"):
        be = -al / 3
    kin = (al * sum(hd[i, j] ** 2 for i in range(3) for j in range(3)) + be * hd.trace() ** 2) / wb
    pv = sp.Matrix([0, 0, p])
    hp = h * pv
    r1 = p ** 2 * h.trace() - (pv.T * h * pv)[0]
    r2 = -p ** 2 * (h.T * h).trace() / 4 + hp.dot(hp) / 2 - (pv.T * h * pv)[0] * h.trace() / 2 + p ** 2 * h.trace() ** 2 / 4
    src_term = sum(th[i, j] * h[i, j] for i in range(3) for j in range(3)) / 2
    lag = kin + kk * wb * (u * r1 + r2) - e * u + src_term
    ok_free = all(sp.expand(sp.diff(r2, v)) == 0 for v in (xi, cx, cy)) and sp.expand(r1 - 2 * p ** 2 * phi) == 0
    eq_u = sp.diff(lag, u)
    eq_xi = sp.diff(lag, xi) - sp.diff(sp.diff(lag, xi.diff(t)), t)
    phisol = sp.solve(eq_u, phi)[0]
    res = sp.simplify(eq_xi.subs(phi, phisol).doit())
    sol = sp.solve(res, e.diff(t, 2))
    thz = th[2, 2]
    ok = ok_free and len(sol) == 1 and sp.simplify(sol[0] + kk * wb ** 2 / (4 * al) * p ** 2 * thz) == 0
    checks.check("B1", ok,
                 "T1: along p = p z, block 101's quadratic action (R2 as block 62 declares it) at beta = -alpha with block 62's stress coupling (1/2) sum Theta_ij h_ij and the source -e u: R1 = 2p^2 phi and R2 do not involve xi, c_x, c_y, and the u-constraint 2K wbar p^2 phi = e with the longitudinal equation give exactly e'' = -(K wbar^2/(4 alpha)) p^2 Theta_zz = -(K wbar^2/(4 alpha)) p.Theta.p (symbolic functions of time)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: for the walker's smooth states the beat obeys e'' = -wbar^2 p.Theta.p at leading order."""
    ok = True
    vals = []
    for kap, kapp in PAIRS:
        for sg in ((1, 1, 1), (-1, -1, -1)):
            for br in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                r = lead_ratio(kap, kapp, sg, br)
                want = 1
                if mut("leading_ratio_forged"):
                    want = 2
                ok = ok and r == want
                vals.append(r)
    wb, dl, eq, pt = sp.symbols("wbar dl e_q pTp", positive=True)
    ok_scale = sp.simplify((-(wb * dl) ** 2 * (wb * eq)) / (-(wb * pt)) - wb ** 2 * (dl ** 2 * eq / pt)) == 0
    checks.check("C1", ok and ok_scale,
                 "T2: for any two eigen-waves of the walker (either branch, energies l and l') near k = 0 and near the all-reflected corner pi(1,1,1), with rational-norm offsets (three pairs, four branch pairs, both corners: 24 cases), the beat's ratio (l - l')^2 (l + l') u'^dag u / [(q.M)(q.(s + s'))] is exactly 1 at leading order: e''_q = -(l - l')^2 e_q and p.Theta.p at q agree, with Theta_q = (1/2) M_a (s_j + s'_j) and e_q = (1/2)(l + l') u'^dag u; a clock rate wbar multiplies energies, e and Theta, giving e'' = -wbar^2 p.Theta.p")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: on the lattice the ratio is 1 + O(|k|^2), with direction-dependent corrections."""
    ok = True
    wants = {((0, 0, 1), (0, 0, 2)): 1 - sp.Rational(9, 4) * sp.Symbol("t", positive=True) ** 2,
             ((1, 0, 0), (1, 0, 1)): 1 - sp.Rational(5, 12) * sp.Symbol("t", positive=True) ** 2}
    if mut("lattice_correction_forged"):
        wants[((0, 0, 1), (0, 0, 2))] = 1 - sp.Rational(5, 12) * sp.Symbol("t", positive=True) ** 2
    for (kap, kapp), want in wants.items():
        tt, r = lattice_ratio(kap, kapp)
        ser = sp.series(r, tt, 0, 3).removeO()
        ok = ok and sp.simplify(ser - want.subs(sp.Symbol("t", positive=True), tt)) == 0
    checks.check("D1", ok,
                 "T3: with the lattice's sin k, p = 2 sin(q/2) and eigenvectors, for k = t kappa and k' = t kappa' the ratio is 1 - 9t^2/4 for kappa = (0,0,1), kappa' = (0,0,2) and 1 - 5t^2/12 for kappa = (1,0,0), kappa' = (1,0,1); both beats run along the z axis, where the member's demand involves only the on-site component Theta_zz; exactly 1 at leading order, with lattice corrections of relative order |k|^2 that depend on the waves' directions (the walker is not exactly such content on the lattice, block 112 T4)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: one light cone, and the other six species."""
    al, kk, wb = sp.symbols("alpha K wbar", positive=True)
    sol = sp.solve(sp.Eq(kk * wb ** 2 / (4 * al), wb ** 2), al)
    want = [kk / 4]
    if mut("light_cone_forged"):
        want = [kk / 2]
    ok_cone = sol == want and sp.simplify((kk * wb ** 2 / (4 * al)).subs(al, kk / 4) - wb ** 2) == 0
    bad = []
    for sg in ((-1, 1, 1), (1, -1, 1), (-1, -1, 1)):
        rs = [lead_ratio(a, b, sg) for a, b in PAIRS]
        bad.append(len(set(rs)) > 1 and all(sp.im(r) != 0 for r in rs))
    checks.check("E1", ok_cone and all(bad),
                 "T4: the walker's smooth states are the member's content at leading order iff K wbar^2/(4 alpha) = wbar^2, i.e. alpha = K/4, when the member's travelling pair (speed^2 K wbar^2/(4 alpha)) moves at the walker's top speed wbar: one light cone; for the six partly reflected species (one or two corner signs negative) the leading ratio differs from pair to pair and is complex, so no single alpha serves them (the species problem of blocks 72, 74 and 120)")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 62 and 101 as landed on main (the walk, the frame's stress coupling and the member's quadratic action), with blocks 112 and 124 placed; it reports what the member demands of its content at the closing ratio and whether the walker's own states can meet it; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Dirac", "Bergmann", "Lorentz", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the member's mode equations at beta = -alpha with symbolic functions of time, re-deriving e'' = -(K wbar^2/(4 alpha)) p.Theta.p",
    "per_site: executed - the beat of two eigen-waves of either branch: energy density, stress and frequency, at leading order in 24 cases (three pairs, four branch pairs, two corners)",
    "per_mode: executed - the lattice ratio's series in the wave number for two beats along an axis (on-site stress only)",
    "per_block: executed - the light-cone condition; the leading ratio for the six partly reflected species",
    "lattice_wide: T1 exact at second order; T2 at leading order in the wave numbers; T3's corrections from series; the walk, member and source link supplied",
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
    print("scope: one light cone from the source link - the walker smooth states are the member content at leading order iff alpha = K/4; lattice corrections of order k^2; six partly reflected species fail; supervisor derivation, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
