#!/usr/bin/env python3
"""Exact checks: what fixes block 60's declared numbers - the time label fixes nothing; a rescaling of the lengths shows
no common weight for the ledger; speeds free of the unit of length force s = p + 2; positive content forces a negative
kinetic coefficient; the curvature's power of the length is d - 2 (a harvest block from a Grok-refereed probes attempt;
blocks 59, 60, 62 and 64 as landed; not adopted).

B (T1): weights under the time label and under a rescaling of the lengths.
C (T2): speeds free of the unit of length.
D (T3): the kinetic sign.
E (T4): the curvature's power, in d = 2, 3, 4.
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
    "docs/ADMISSIBILITY_RULE_BLOCK_60S_DECLARED_NUMBERS_UNIT_FREE_SPEEDS_FORCE_S_EQUALS_P_PLUS_TWO_POSITIVE_CONTENT_FORCES_THE_KINETIC_SIGN_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_block_60s_declared_numbers_unit_free_speeds_force_s_equals_p_plus_two_positive_content_forces_the_kinetic_sign_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
    "A choice not fixed by the supplied structure remains a named conditional or open dependency.",
)

MUTATION_GATE = {
    "rescaling_weight_forged": "B",
    "speed_power_forged": "C",
    "kinetic_sign_forged": "D",
    "curvature_power_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no site is privileged; Admissibility is not a dynamics axiom (the member, its powers and the kinetic term are supplied); a choice not fixed by the supplied structure remains a named conditional (K and alpha/K)")


# ============================================================================================ block 60's member and kinetic term on a ring
PP, SS, KK, CC, LL = sp.symbols("p s K C L", positive=True)
ALPHA, BETA = sp.symbols("alpha beta")


def ring_member(lams, ws, p, a, b):
    """block 60's member F = sum_x w_x K l_x^p (a Lap(lambda)_x + b q_x) on a ring, q_x = sum over the two bonds of (lambda_y - lambda_x)^2."""
    n = len(lams)
    tot = 0
    for x in range(n):
        lap = lams[(x + 1) % n] + lams[(x - 1) % n] - 2 * lams[x]
        q = (lams[(x + 1) % n] - lams[x]) ** 2 + (lams[(x - 1) % n] - lams[x]) ** 2
        tot += ws[x] * KK * sp.exp(p * lams[x]) * (a * lap + b * q)
    return tot


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the time label and the length rescaling - what weight each part of the ledger has."""
    n = 4
    lam = sp.symbols("l0:4")
    ws = sp.symbols("w0:4", positive=True)
    cb = sp.symbols("c0:4", positive=True)
    aa, bb = sp.symbols("a b")
    f0 = ring_member(lam, ws, PP, aa, bb)
    f_time = ring_member(lam, [LL * w for w in ws], PP, aa, bb)
    ok_time = sp.simplify(f_time - LL * f0) == 0
    lam_c = [l + sp.log(CC) for l in lam]
    f_resc = ring_member(lam_c, [CC * w for w in ws], PP, aa, bb)
    want = CC ** (1 + PP)
    if mut("rescaling_weight_forged"):
        want = CC ** PP
    ok_resc = sp.simplify(sp.powsimp(sp.expand_power_exp(f_resc / f0), force=True) - want) == 0
    lb = [sp.sqrt(ws[i] * ws[(i + 1) % n]) / cb[i] for i in range(n)]
    lb_c = [sp.sqrt(CC * ws[i] * CC * ws[(i + 1) % n]) / cb[i] for i in range(n)]
    ok_len = all(sp.simplify(lb_c[i] - CC * lb[i]) == 0 for i in range(n))
    ld, ww, lv = sp.symbols("lambdadot w ell", positive=True)
    kin = sp.symbols("c_k") * lv ** SS * ld ** 2 / ww
    ok_kin = sp.simplify(kin.subs({ld: LL * ld, ww: LL * ww}) - LL * kin) == 0 and sp.simplify(sp.powsimp(kin.subs({lv: CC * lv, ww: CC * ww}) / kin, force=True) - CC ** (SS - 1)) == 0
    hop, rest = sp.symbols("h r")
    content = hop + ww * rest
    ok_content = sp.expand(content.subs(ww, CC * ww)) == sp.expand(hop + CC * ww * rest)
    pq = sp.symbols("pq")
    no_common = sp.solve(sp.Eq(1 + pq, 0), pq) == [-1] and sp.solve(sp.Eq(1 + pq, 1), pq) == [0]
    checks.check("B1", ok_time and ok_resc and ok_len and ok_kin and ok_content and no_common,
                 "T1: on a ring with symbolic lambda_x and w_x, multiplying every rate by L multiplies block 60's member F = sum w K l^p (a Lap + b q) and the kinetic term c_k l^s lambdadot^2/w by L, for every p and s (weight one under the time label); a uniform rescaling l -> C l with the crossing rates held forces w -> C w (l_b = sqrt(w_x w_y)/c_b), and then F -> C^(1+p) F, the kinetic term -> C^(s-1), the hop energy -> itself and the rest energy -> C times itself: a common weight with the hop energy would need p = -1 and with the rest energy p = 0, neither block 60's p = 1: no single weight for the whole ledger, so the rescaling changes the unit of length that K carries")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: speeds free of the unit of length iff s = p + 2."""
    om2, wbar, lbar, pp2 = sp.symbols("omega2 wbar lbar P2", positive=True)
    mode = sp.solve(sp.Eq(ALPHA * lbar ** SS / wbar * om2, KK * wbar * lbar ** PP * pp2), om2)[0]
    scaled = mode.subs({lbar: CC * lbar, wbar: CC * wbar})
    ratio = sp.powsimp(sp.simplify(scaled / mode), force=True)
    want = CC ** (2 + PP - SS)
    if mut("speed_power_forged"):
        want = CC ** (1 + PP - SS)
    ok_ratio = sp.simplify(ratio - want) == 0
    ok_s = sp.solve(sp.Eq(2 + PP - SS, 0), SS) == [PP + 2]
    ok_three = (PP + 2).subs(PP, 1) == 3
    checks.check("C1", ok_ratio and ok_s and ok_three,
                 "T2: with the background powers kept, the field's mode equation (alpha lbar^s/wbar) omega^2 = K wbar lbar^p P^2 gives omega^2 proportional to wbar^2 lbar^(p-s), which the rescaling multiplies by C^(2+p-s), while the walker's frequencies (hop rates held) are unchanged: the ratio of the two speeds is free of the unit of length iff s = p + 2, and at p = 1 that is s = 3, the comparator's volume power")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: positive content on a closed lattice forces a negative kinetic coefficient."""
    ck, mm, ww, lv, ld, t, t0 = sp.symbols("c_k m w ell lambdadot t t0")
    stat = sp.solve(sp.diff(ck * lv ** SS * ld ** 2 / ww - mm * ww, ww), ck)
    want = [-mm * ww ** 2 / (lv ** SS * ld ** 2)]
    if mut("kinetic_sign_forged"):
        want = [mm * ww ** 2 / (lv ** SS * ld ** 2)]
    ok_sign = len(stat) == 1 and sp.simplify(stat[0] - want[0]) == 0
    lam_t = (2 / SS) * sp.log(1 + t / t0)
    ok_ell = sp.simplify(2 * sp.diff(lam_t, t, 2) + SS * sp.diff(lam_t, t) ** 2) == 0
    c_k = 12 * ALPHA + 36 * BETA
    ok_ratio = sp.solve(sp.Eq(c_k, 0), BETA) == [-ALPHA / 3] and sp.expand(c_k.subs(BETA, -ALPHA)) == -24 * ALPHA and sp.expand(c_k.subs({ALPHA: KK / 4, BETA: -KK / 4})) == -6 * KK
    checks.check("D1", ok_sign and ok_ratio and ok_ell,
                 "T3: stationarity in w of c_k l^s lambdadot^2/w - m w (block 60 T5(b) as landed) gives c_k = -m w^2/(l^s lambdadot^2), negative whenever the content m is positive, and then l = (1 + t/t0)^(2/s) solves 2 lambda'' + s lambda'^2 = 0; with the isotropic stretch's c_k = 12 alpha + 36 beta (block 124 T2, open) this needs beta < -alpha/3 for alpha > 0, met at beta = -alpha (c_k = -24 alpha) and at the comparator's (K/4, -K/4) (c_k = -6K)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the curvature member's power of the length is d - 2."""
    ok = True
    for d in (2, 3, 4):
        xs = sp.symbols(f"x1:{d + 1}")
        lam = sp.Function("lam")(*xs)
        g = sp.exp(2 * lam) * sp.eye(d)
        gi = sp.exp(-2 * lam) * sp.eye(d)
        gam = [[[sum(gi[a, e] * (sp.diff(g[e, b], xs[c]) + sp.diff(g[e, c], xs[b]) - sp.diff(g[b, c], xs[e])) for e in range(d)) / 2
                 for c in range(d)] for b in range(d)] for a in range(d)]

        def ric(b, c):
            return sum(sp.diff(gam[a][b][c], xs[a]) - sp.diff(gam[a][b][a], xs[c])
                       + sum(gam[a][a][e] * gam[e][b][c] - gam[a][c][e] * gam[e][b][a] for e in range(d)) for a in range(d))
        rs = sp.simplify(sum(gi[b, c] * ric(b, c) for b in range(d) for c in range(d)))
        lap = sum(sp.diff(lam, x, 2) for x in xs)
        grad2 = sum(sp.diff(lam, x) ** 2 for x in xs)
        power = d - 2
        if mut("curvature_power_forged"):
            power = d - 1
        want = sp.exp(power * lam) * (-2 * (d - 1) * lap - (d - 2) * (d - 1) * grad2)
        ok = ok and sp.simplify(sp.exp(d * lam) * rs - want) == 0
    checks.check("E1", ok,
                 "T4: for the stretched lattice g = l^2 delta, l = e^lambda, sqrt(g) R = l^(d-2) (-2(d-1) Lap(lambda) - (d-2)(d-1)|grad lambda|^2) exactly in d = 2, 3, 4 (Christoffel symbols computed symbolically): the curvature member's power is p = d - 2, so p = 1 in three dimensions, which block 64 as landed reaches from blindness to coin rotations within its ansatz; with T2, s = 3")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 59, 60, 62 and 64 as landed on main (lengths and rates, the member linear in the rates and its kinetic term, the frame's modes, and blindness to the coin's axes); it reports which of block 60's declared numbers are fixed by stated demands and which stay supplied; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Christoffel", "Ricci", "Friedmann", "Arnowitt", "Deser", "Misner", "DeWitt", "Einstein", "Hilbert", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the member on a ring with symbolic lengths and rates under the time label and under a rescaling of the lengths",
    "per_site: executed - the bond length's response to the rescaling; the weights of hop and rest energy",
    "per_mode: executed - the mode frequency's power of the rescaling and the condition s = p + 2",
    "per_block: executed - the kinetic sign from stationarity in the rates; the uniform motion; the Ricci scalar of the stretched lattice in d = 2, 3, 4",
    "lattice_wide: T1-T4 exact as stated; p = 1 rests on block 64's ansatz and s = 3 on the unit-free-speed demand; K, alpha/K and the existence of the kinetic term stay supplied",
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
    print("scope: block 60 declared numbers - no common weight under a rescaling of the lengths; unit-free speeds force s = p + 2; positive content forces c_k < 0; the curvature power is p = d - 2; K and alpha/K stay supplied; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
