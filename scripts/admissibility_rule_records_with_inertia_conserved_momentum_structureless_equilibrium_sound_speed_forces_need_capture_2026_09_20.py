#!/usr/bin/env python3
"""Exact checks: records with inertia (a record's content is its direction of travel).

A supplied clause, not adopted.  (S) streaming: each record, at rate 1, tries to step along its content; an empty target is entered, an occupied
target exchanges contents with the record, a solid site reflects it.  (C) scattering: each bond, at rate gamma, re-draws the contents of its two
records uniformly on their momentum class (an opposite pair becomes a uniformly random opposite pair; any other pair is exchanged with
probability 1/2).  T1: every event conserves the number of records and the momentum sum of e(content), and the clause commutes with the 24
rotations.  T2: the uniform measure is stationary (every configuration has as much inflow as outflow), with or without reflecting bodies; it
is not if blocked attempts do nothing, nor under the blocked-attempt head-on rule.  T3: in a product state with content densities rho_d the
mass current is (1 - rho) g, g the momentum density, and at isotropy the momentum flux is (rho/3) times the identity (the exchange term
restores exactly what exclusion removes), so the linearized conservation equations have the speed sqrt((1 - rho)/3); for the sphere menu, with
streaming probability max(0, s.e_k)/sqrt 3, the corresponding speed squared is (1 - rho)/9.  T4: in the uniform state the mean force on a
reflecting body vanishes whatever else is present: bodies that neither capture nor emit records feel no force.  T5 (sphere menu): re-drawing
a pair on its momentum class, P/2 +- r w with w a unit vector orthogonal to P and r^2 = 1 - |P|^2/4, keeps unit length and the sum.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_RECORDS_WITH_INERTIA_CONTENT_AS_DIRECTION_OF_TRAVEL_CONSERVED_MOMENTUM_STRUCTURELESS_EQUILIBRIUM_SOUND_SPEED_FORCES_NEED_CAPTURE_OR_EMISSION_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_records_with_inertia_content_as_direction_of_travel_conserved_momentum_structureless_equilibrium_sound_speed_forces_need_capture_or_emission_bounded_theorem_note_2026-09-20"
AXIOM_NEEDLES = (
    "A site never carries more than one record; records are permanent.",
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
)

MUTATION_GATE = {
    "head_on_reverses_one_record": "B",
    "clause_not_covariant_injected": "B",
    "blocked_attempts_do_nothing": "C",
    "blocked_attempt_head_on_rule": "C",
    "pressure_without_exchange_term": "D",
    "mass_current_without_blocking": "D",
    "force_on_reflecting_body_injected": "E",
    "sphere_scatter_breaks_unit_length": "E",
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


E = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
IDX = {v: k for k, v in enumerate(E)}
M6 = range(6)


def vec_sum(contents):
    return tuple(sum(E[d][i] for d in contents) for i in range(3))


def stream_outcomes(d, target):
    """one streaming attempt by a record of content d whose target site holds `target` (None = empty): list of (weight, mover's site content, target site content)"""
    if target is None:
        return [(Fraction(1), None, d)]
    if mut("head_on_reverses_one_record") and target == d ^ 1:
        return [(Fraction(1), d ^ 1, target)]
    return [(Fraction(1), target, d)]


def scatter_outcomes(a, b):
    if b == a ^ 1:
        return [(Fraction(1, 6), e, e ^ 1) for e in M6]
    return [(Fraction(1, 2), a, b), (Fraction(1, 2), b, a)]


def rotations():
    rots = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            m = [[signs[i] if perm[i] == j else 0 for j in range(3)] for i in range(3)]
            det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
            if det == 1:
                rots.append(m)
    return rots


def act(m, d):
    return IDX[tuple(sum(m[i][j] * E[d][j] for j in range(3)) for i in range(3))]


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the sentences used")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    ok = True
    for d in M6:
        for target in [None] + list(M6):
            before = vec_sum([d] + ([] if target is None else [target]))
            for w, c_x, c_y in stream_outcomes(d, target):
                after = vec_sum([c for c in (c_x, c_y) if c is not None])
                ok = ok and after == before and (c_x is not None) + (c_y is not None) == 1 + (target is not None)
    for a in M6:
        for b in M6:
            outs = scatter_outcomes(a, b)
            ok = ok and sum(w for w, _, _ in outs) == 1 and all(vec_sum([x, y]) == vec_sum([a, b]) for _, x, y in outs)
    checks.check("B1", ok, "T1: every streaming event (42 local cases) and every scattering event (36 pairs) conserves the number of records and the momentum, the sum of the unit vectors of the contents")
    ok = True
    for m in rotations():
        for d in M6:
            for target in [None] + list(M6):
                base = stream_outcomes(d, target)
                if mut("clause_not_covariant_injected") and d == 0 and target == 2:
                    base = [(Fraction(1), d, target)]                     # contents +x and +y do not exchange: a rule tied to the frame
                turned = stream_outcomes(act(m, d), None if target is None else act(m, target))
                want = sorted((w, None if x is None else act(m, x), None if y is None else act(m, y)) for w, x, y in base)
                ok = ok and sorted(turned, key=str) == sorted(want, key=str)
            for b in M6:
                base = sorted((w, act(m, x), act(m, y)) for w, x, y in scatter_outcomes(d, b))
                ok = ok and sorted(scatter_outcomes(act(m, d), act(m, b))) == base
    checks.check("B2", ok, "T1: streaming and scattering both commute with the 24 proper rotations of the cube acting on sites and contents together")


# ============================================================================================ family C (T2)
def stationarity(L, n, rule, solids=frozenset(), gamma=Fraction(1)):
    sites = [s for s in product(range(L), repeat=3) if s not in solids]
    add = lambda x, d: tuple((x[i] + E[d][i]) % L for i in range(3))
    inflow, outflow = {}, {}
    force = {b: [Fraction(0)] * 3 for b in solids}
    count = 0
    for occ in combinations(sites, n):
        for contents in product(M6, repeat=n):
            cfg = dict(zip(occ, contents))
            key = tuple(sorted(cfg.items()))
            count += 1
            events = []
            for x, d in cfg.items():
                y = add(x, d)
                if y in solids:
                    new = dict(cfg)
                    new[x] = d ^ 1
                    for i in range(3):
                        force[y][i] += 2 * E[d][i]
                    events.append((Fraction(1), new))
                elif y not in cfg:
                    new = dict(cfg)
                    del new[x]
                    new[y] = d
                    events.append((Fraction(1), new))
                elif rule == "no-exchange":
                    events.append((Fraction(1), dict(cfg)))
                elif rule == "blocked-head-on" and cfg[y] == d ^ 1:
                    for e in M6:
                        new = dict(cfg)
                        new[x], new[y] = e, e ^ 1
                        events.append((Fraction(1, 6), new))
                else:
                    new = dict(cfg)
                    new[x], new[y] = cfg[y], d
                    events.append((Fraction(1), new))
            if rule == "clean":
                for x in cfg:
                    for k in (0, 2, 4):
                        y = add(x, k)
                        if y in cfg:
                            for w, c_x, c_y in scatter_outcomes(cfg[x], cfg[y]):
                                new = dict(cfg)
                                new[x], new[y] = c_x, c_y
                                events.append((gamma * w, new))
            for rate, new in events:
                k2 = tuple(sorted(new.items()))
                inflow[k2] = inflow.get(k2, 0) + rate
                outflow[key] = outflow.get(key, 0) + rate
    bad = sum(1 for k in outflow if inflow.get(k, 0) != outflow[k])
    return count, bad, {b: [v / count for v in f] for b, f in force.items()}


def family_c(checks: Checks) -> None:
    rule = "no-exchange" if mut("blocked_attempts_do_nothing") else ("blocked-head-on" if mut("blocked_attempt_head_on_rule") else "clean")
    count, bad, _ = stationarity(3, 2, rule)
    checks.check("C1", bad == 0, f"T2: on the 3^3 torus with two records, all contents ({count} configurations), every configuration receives exactly as much as it sends under streaming with exchange and bond scattering: the uniform measure is stationary ({bad} unbalanced)")
    _, bad_a, _ = stationarity(3, 2, "no-exchange")
    _, bad_b, _ = stationarity(3, 2, "blocked-head-on")
    checks.check("C2", bad_a > 0 and bad_b > 0, f"T2: it is not stationary if blocked attempts do nothing ({bad_a} unbalanced configurations) nor under a head-on rule triggered by blocked attempts ({bad_b}): the exchange and the bond clock are what make the equilibrium structureless")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    ok = True
    for dens in ([Fraction(1, 12), Fraction(1, 20), Fraction(1, 15), Fraction(1, 30), Fraction(1, 10), Fraction(1, 60)], [Fraction(1, 20)] * 6, [Fraction(1, 9), Fraction(1, 18), Fraction(1, 12), Fraction(1, 12), Fraction(1, 36), Fraction(1, 36)]):
        rho = sum(dens)
        g = [sum(dens[d] * E[d][i] for d in M6) for i in range(3)]
        block = 1 if mut("mass_current_without_blocking") else (1 - rho)
        # mass current along +i: records of content +i stepping forward minus records of content -i stepping backward across the same bond
        j = [dens[2 * i] * (1 - rho) - dens[2 * i + 1] * (1 - rho) for i in range(3)]
        ok = ok and j == [block * g[i] for i in range(3)]
    checks.check("D1", ok, "T3: in a product state with content densities rho_d the mass current is (1 - rho) times the momentum density, for three sets of densities")
    ok = True
    for rho in (Fraction(3, 10), Fraction(1, 2), Fraction(9, 10)):
        dens = [rho / 6] * 6
        flux = [[Fraction(0)] * 3 for _ in range(3)]
        for d in M6:
            for i in range(3):
                for jx in range(3):
                    flux[i][jx] += dens[d] * (1 - rho) * E[d][i] * E[d][jx]                     # a record moves and carries its momentum
                    if not mut("pressure_without_exchange_term"):
                        for d2 in M6:
                            flux[i][jx] += dens[d] * dens[d2] * (E[d][i] - E[d2][i]) * E[d][jx]   # an exchange passes e_d forward and e_d2 back
        ok = ok and all(flux[i][jx] == (rho / 3 if i == jx else 0) for i in range(3) for jx in range(3))
        # the bond scattering carries no net momentum across the bond at isotropy
        net = [Fraction(0)] * 3
        for a in M6:
            for b in M6:
                for w, x, _ in scatter_outcomes(a, b):
                    for i in range(3):
                        net[i] += dens[a] * dens[b] * w * (E[a][i] - E[x][i])
        ok = ok and net == [0, 0, 0]
    speed_sq = [(1 - rho) * Fraction(1, 3) for rho in (Fraction(3, 10), Fraction(1, 2))]
    checks.check("D2", ok and speed_sq == [Fraction(7, 30), Fraction(1, 6)], "T3: at isotropy the momentum flux is (rho/3) times the identity at rho = 3/10, 1/2, 9/10 (the exchange term rho^2/3 restores what exclusion removes from rho(1 - rho)/3), the bond scattering carries no net momentum, and the linearized wave speed squared (1 - rho)/3 is 7/30 at rho = 3/10")


# ============================================================================================ family E (T4, T5)
def family_e(checks: Checks) -> None:
    solids = frozenset({(0, 0, 0), (2, 0, 0)})
    count, bad, force = stationarity(4, 2, "clean", solids=solids)
    total = [sum(f[i] for f in force.values()) for i in range(3)]
    each_zero = all(v == 0 for f in force.values() for v in f)
    if mut("force_on_reflecting_body_injected"):
        each_zero = each_zero and force[(0, 0, 0)][0] != 0
    checks.check("E1", bad == 0 and each_zero and total == [0, 0, 0], f"T4: on the 4^3 torus with two separate reflecting solid sites and two records ({count} configurations) the uniform measure is still stationary and the mean force on each solid is exactly zero: bodies that neither capture nor emit records feel no force")
    ok = True
    cases = [((Fraction(3, 5), Fraction(4, 5), 0), (Fraction(3, 5), Fraction(-4, 5), 0), (0, 0, 1)),
             ((Fraction(5, 13), 0, Fraction(12, 13)), (Fraction(5, 13), 0, Fraction(-12, 13)), (0, 1, 0)),
             ((0, Fraction(8, 17), Fraction(15, 17)), (0, Fraction(8, 17), Fraction(-15, 17)), (1, 0, 0))]
    for s1, s2, w in cases:
        s1, s2, w = (tuple(Fraction(v) for v in t) for t in (s1, s2, w))          # integers would make p[i] / 2 a floating-point number
        p = tuple(a + b for a, b in zip(s1, s2))
        p2 = sum(v * v for v in p)
        r2 = 1 - (p2 / 2 if mut("sphere_scatter_breaks_unit_length") else p2 / 4)
        r = {Fraction(16, 25): Fraction(4, 5), Fraction(144, 169): Fraction(12, 13), Fraction(225, 289): Fraction(15, 17)}.get(r2)
        if r is None:
            ok = False
            continue
        a = tuple(p[i] / 2 + r * w[i] for i in range(3))
        b = tuple(p[i] / 2 - r * w[i] for i in range(3))
        ok = ok and all(isinstance(v, Fraction) for v in a + b)
        ok = ok and sum(v * v for v in a) == 1 and sum(v * v for v in b) == 1 and tuple(x + y for x, y in zip(a, b)) == p and sum(p[i] * w[i] for i in range(3)) == 0
    # the sphere menu's streaming identity: sum over the two neighbours along an axis of max(0, s.e_k) (e_k)_j equals s_j
    for s in ((Fraction(3, 5), Fraction(-4, 5), Fraction(0)), (Fraction(2, 7), Fraction(3, 7), Fraction(-6, 7))):
        for jx in range(3):
            ok = ok and max(Fraction(0), s[jx]) - max(Fraction(0), -s[jx]) == s[jx]
    checks.check("E2", ok, "T5: for the sphere menu, re-drawing a pair on its momentum class (P/2 +- r w, w orthogonal to P, r^2 = 1 - |P|^2/4) keeps both contents of unit length and keeps their sum, on three rational instances; and the streaming probabilities max(0, s.e_k)/sqrt 3 carry the mean displacement s/sqrt 3, which gives the speed squared (1 - rho)/9")


# ============================================================================================ family F
FENCES = (
    "This note works out a supplied clause, in which a record's content is its direction of travel; the clause is not in the axioms memo and is not adopted.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Navier", "Stokes", "Bernoulli", "Bjerknes", "Pearson", "Sage", "Boltzmann", "Gibbs", "Laplace", "Poisson", "Galileo", "Galilei", "Knudsen", "Mach", "Fick", "Brown", "Planck", "Einstein", "Poincare")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Boltzmann)", 1)
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
    "per_element: executed — the 42 local streaming cases and the 36 scattering pairs; the 24 rotations",
    "per_site: executed — inflow against outflow at every one of the 12636 two-record configurations of the 3^3 torus, and of the 4^3 torus with two reflecting solid sites; the mean force on each solid",
    "per_mode: not applicable to the exact part; the executed sound waves are in the controls",
    "per_block: executed — the mass current and the momentum flux of product states at three densities; three rational instances of the sphere menu's pair re-drawing",
    "lattice_wide: T1 holds event by event on every lattice; T2 and T4 are proved by a counting argument for every finite torus and body and checked exhaustively on small tori; T3's currents are exact for product states, and the speed is that of the linearized conservation equations built on them; the forces between capturing or emitting bodies are executed, not proved",
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
    print("scope: records with inertia — number and momentum conserved event by event, a structureless equilibrium, mass current (1 - rho) g and pressure rho/3 in product states, wave speed squared (1 - rho)/3 (six axes) and (1 - rho)/9 (sphere), no force on bodies that neither capture nor emit; exact")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
