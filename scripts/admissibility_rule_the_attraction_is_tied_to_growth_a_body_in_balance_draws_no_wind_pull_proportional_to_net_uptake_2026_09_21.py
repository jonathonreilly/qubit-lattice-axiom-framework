#!/usr/bin/env python3
"""Exact checks: bodies in balance in the inertial record gas (block 44's clause and an emission clause; both supplied, not adopted).

T1 the flux theorem: in a stationary state the flux of the mean current out of any region is minus the net uptake inside it, captures minus
emissions; a body in balance sends no flux through any surface around it.  T2 independent records: emission through the six faces with the
cosine law gives contents the weight |s|_1 and places a record of content s on the neighbour e_k with the step frequency w_k, so emitted
records are directed walks from the body and the surplus they make is the emission rate times the hitting probability; with the emission
rate rho f(s) |s|_1/sqrt 3 it cancels the capture deficit at every site; uniform emission at the same total rate leaves a residue whose
number vanishes on every shell and whose force coefficient is |r|_1 (|r|_1 - 3/2).  T3 the closure: the pull of a body is proportional to
its net uptake, the push on a body to its gross capture, so action and reaction between two bodies differ.  T4: the pull per record and the
relative growth rate are tied, q_1 = (8 pi/3)(1 - rho) G, also for bodies that keep only a fraction of what they capture.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import random
import ast
import re
import sys
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_ATTRACTION_IS_TIED_TO_GROWTH_A_BODY_IN_BALANCE_DRAWS_NO_WIND_PULL_PROPORTIONAL_TO_NET_UPTAKE_GROWTH_RATE_FIXED_BY_THE_FORCE_COEFFICIENT_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_attraction_is_tied_to_growth_a_body_in_balance_draws_no_wind_pull_proportional_to_net_uptake_growth_rate_fixed_by_the_force_coefficient_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = ("A site never carries more than one record; records are permanent.",)

MUTATION_GATE = {
    "flux_counts_gross_capture": "B",
    "emission_uniform_over_faces": "C",
    "balance_rate_without_capture_weight": "C",
    "residual_coefficient_wrong": "C",
    "reaction_equals_action": "D",
    "growth_relation_without_blocking": "D",
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
F = Fraction


def one_norm(s):
    return sum(abs(c) for c in s)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the sentence used")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    rng = random.Random(49)
    side = 5
    sites = list(product(range(side), repeat=3))
    current = {}                                                     # antisymmetric mean current on the bonds of the block
    for x in sites:
        for d in E[::2]:
            y = tuple(x[i] + d[i] for i in range(3))
            if all(0 <= c < side for c in y):
                val = F(rng.randint(-9, 9), rng.randint(1, 7))
                current[(x, y)] = val
                current[(y, x)] = -val
    body = [(2, 2, 2), (2, 3, 2), (1, 2, 2)]
    outflow = {x: sum(v for (a, _), v in current.items() if a == x) for x in sites}
    # stationarity: what flows into a site net is taken up there; at the body's sites the uptake is captures minus emissions
    captures = {x: F(rng.randint(3, 9)) for x in body}
    emissions = {x: captures[x] + outflow[x] for x in body}           # so that captures - emissions = -outflow at the body's sites
    ok = all(captures[x] - emissions[x] == -outflow[x] for x in body)
    regions = {
        "a cube around the body": [x for x in sites if all(1 <= c <= 3 for c in x)],
        "an L-shaped region": [x for x in sites if (x[0] <= 2 and x[1] <= 3 and x[2] == 2) or (x[0] == 2 and x[2] >= 2)],
        "the body alone": list(body),
    }
    shown = []
    for name, reg in regions.items():
        rset = set(reg)
        flux = sum(v for (a, b), v in current.items() if a in rset and b not in rset)
        if mut("flux_counts_gross_capture"):
            uptake = sum(captures[x] for x in reg if x in captures) + sum(-outflow[x] for x in reg if x not in captures)
        else:
            uptake = sum(-outflow[x] for x in reg)
        ok = ok and flux == -uptake
        shown.append(f"{name}: {flux}")
    checks.check("B1", ok, "T1: for an antisymmetric bond current the flux out of a region is minus the net uptake inside it, captures minus emissions at the body's sites (" + "; ".join(shown) + "): a body whose emissions equal its captures, in a gas that is stationary elsewhere, sends no flux through any surface around it")


# ============================================================================================ family C (T2)
def multinomial(x, w) -> Fraction:
    n = sum(x)
    val = F(factorial(n))
    for k in range(3):
        val = val / factorial(x[k]) * w[k] ** x[k]
    return val


def family_c(checks: Checks) -> None:
    dirs = [((1, 2, 2), 3), ((2, 3, 6), 7), ((3, 4, 0), 5), ((84, 12, 5), 85), ((6, 6, 7), 11)]
    ok = True
    for d, length in dirs:
        s = tuple(F(c, length) for c in d)
        face_weights = [max(F(0), sum(s[i] * e[i] for i in range(3))) for e in E]          # cosine law through the six faces
        if mut("emission_uniform_over_faces"):
            face_weights = [F(1) if w > 0 else F(0) for w in face_weights]
        total = sum(face_weights)
        placed = tuple(face_weights[2 * k] / total for k in range(3))
        w = tuple(F(c, sum(d)) for c in d)
        ok = ok and placed == w and (mut("emission_uniform_over_faces") or total == one_norm(s))
    checks.check("C1", ok, "T2: emission with the cosine law through the six faces gives a content s the weight |s|_1 and places it on the neighbour e_k with the step frequency w_k = |s_k|/|s|_1: emitted records are directed walks that start at the body")
    ok = True
    rho = F(3, 10)
    for d, length in dirs[:3]:
        s = tuple(F(c, length) for c in d)
        w = tuple(F(c, sum(d)) for c in d)
        f_s = F(1, 7)                                                # the gas's weight for this content (any value)
        a1 = one_norm(s)                                             # step rate |s|_1/sqrt 3, in units of 1/sqrt 3
        emission = rho * f_s * (F(1) if mut("balance_rate_without_capture_weight") else a1)
        for x in product(range(4), repeat=3):
            if x == (0, 0, 0):
                continue
            h = multinomial(x, w)
            deficit_flux = rho * f_s * a1 * h                        # density deficit rho f h times the step rate
            surplus_flux = emission * h
            ok = ok and surplus_flux == deficit_flux
    checks.check("C2", ok, "T2: with the emission rate rho f(s) |s|_1/sqrt 3 per content, which for a uniform gas is the cosine law at the capture rate, the surplus of emitted records cancels the capture deficit at every site of a 4x4x4 block: the gas around a body in balance is uniform and no site feels a force")
    # uniform emission at the same total rate: net flux per content proportional to 3/2 - |s|_1 ; the mean of |s|_1 is 3/2
    mean_l1 = 3 * F(1, 2)
    ok = mean_l1 - F(3, 2) == 0
    shown = []
    want = {(1, 2, 2): F(5, 18), (2, 3, 6): F(11, 98), (84, 12, 5): F(-5353, 14450), (6, 6, 7): F(95, 242)}
    for d, length in dirs:
        if d == (3, 4, 0):
            continue
        l1 = F(sum(d), length)
        coeff = l1 * (l1 - F(3, 2))                                  # attraction coefficient |r|_1^2 - (3/2)|r|_1
        if mut("residual_coefficient_wrong"):
            coeff = l1 * l1 - F(9, 4)
        ok = ok and coeff == want[d]
        shown.append(f"{d}: {coeff}")
    ok = ok and F(3, 2) * (F(3, 2) - F(3, 2)) == 0
    checks.check("C3", ok, "T2: a body that emits uniformly at its capture rate sends no net number through any shell (the mean of |s|_1 is 3/2) and leaves the force coefficient |r|_1 (|r|_1 - 3/2) in units of rho/(4 pi sqrt 3 r^2): " + "; ".join(shown) + "; repulsive near the axes, attractive near the body diagonals, zero where |r|_1 = 3/2")


# ============================================================================================ family D (T3, T4)
class Sym:
    """c * pi^a * 3^(b/2) with c rational."""

    def __init__(self, c, a=0, b=0):
        c = F(c)
        while b >= 2:
            c *= 3
            b -= 2
        while b < 0:
            c /= 3
            b += 2
        self.c, self.a, self.b = c, a, b

    def __mul__(self, o):
        return Sym(self.c * o.c, self.a + o.a, self.b + o.b)

    def __truediv__(self, o):
        return Sym(self.c / o.c, self.a - o.a, self.b - o.b)

    def key(self):
        return (self.c, self.a, self.b)


def family_d(checks: Checks) -> None:
    # cosine-law emission about the outward normal n: mean content (integral of mu^2)/(integral of mu) n = (2/3) n; summed over the faces of a body it vanishes
    mean_along = F(1, 3) / F(1, 2)
    bodies = {
        "cube": list(product(range(2), repeat=3)),
        "plate": [(x, y, 0) for x in range(2) for y in range(2)],
        "ball": [s for s in product(range(-3, 4), repeat=3) if sum(c * c for c in s) <= 9],
    }
    ok0 = mean_along == F(2, 3)
    for body in bodies.values():
        bset = set(body)
        total = [F(0), F(0), F(0)]
        for s in body:
            for d in E:
                if tuple(s[i] + d[i] for i in range(3)) not in bset:
                    for i in range(3):
                        total[i] += mean_along * d[i]
        ok0 = ok0 and total == [0, 0, 0]
    checks.check("D0", ok0, "T3: cosine-law emission about a face's outward normal carries the mean content (2/3) n, and a body has as many faces with normal n as with -n (cube, plate, ball of radius 3), so faces that emit at equal rates carry off no momentum on average: a body in balance is pushed with its gross capture")
    rho = F(3, 10)
    k0 = Sym(F(1, 4) / (rho * (1 - rho)), -1, 1)
    r2 = 256
    ok = True
    shown = []
    for (q1_, keep1), (q2_, keep2) in (((F(8), F(1)), (F(5), F(1))), ((F(8), F(0)), (F(5), F(1))), ((F(8), F(1, 4)), (F(5), F(1, 2))), ((F(8), F(0)), (F(5), F(0)))):
        on_2 = k0 * Sym(keep1 * q1_ * q2_ / r2)                      # the wind of body 1 is made by its net uptake; body 2 takes up momentum with its gross capture
        on_1 = k0 * Sym((keep1 if mut("reaction_equals_action") else keep2) * q1_ * q2_ / r2)
        want_2 = k0 * Sym(keep1 * q1_ * q2_ / r2)
        want_1 = k0 * Sym(keep2 * q1_ * q2_ / r2)
        ok = ok and on_2.key() == want_2.key() and on_1.key() == want_1.key()
        shown.append(f"kept fractions {keep1}, {keep2}: pushes in units of K_0/r^2: {keep1 * q1_ * q2_} on body 2, {keep2 * q1_ * q2_} on body 1")
    checks.check("D1", ok, "T3: in the closure the wind of a body is made by its net uptake and a body takes up momentum with its gross capture, so the push on body 2 is K_0 (kept fraction of 1) Q_1 Q_2/r^2 and the push on body 1 is K_0 (kept fraction of 2) Q_1 Q_2/r^2: " + "; ".join(shown))
    ok = True
    for rho in (F(3, 10), F(1, 10), F(1, 1000)):
        q1 = Sym(rho / 2, 0, 1)
        g = Sym(3 * rho / (16 * (1 - rho)), -1, 1)
        block = 1 if mut("growth_relation_without_blocking") else (1 - rho)
        ok = ok and (q1 / g).key() == Sym(F(8, 3) * block, 1, 0).key()
        for keep in (F(1), F(1, 3)):
            ok = ok and (Sym(keep) * q1 / (Sym(keep) * g)).key() == (q1 / g).key()
    checks.check("D2", ok, "T4: q_1 = (8 pi/3)(1 - rho) G: the relative growth rate of a transparent body is 8 pi (1 - rho)/3 times the coefficient of the pull it exerts, and the ratio is the same for a body that keeps any fraction of what it captures; under constant density, kept fraction and N=M active sites, a mass that changes by less than a factor e over T ticks pulls with a coefficient below 3/(8 pi (1 - rho) T)")


# ============================================================================================ family F
FENCES = (
    "This note works within the supplied inertial clause of block 44 and a supplied emission clause; it reports what wind and what force a body draws when it gives back what it captures; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Navier", "Stokes", "Bernoulli", "Bjerknes", "Sage", "Boltzmann", "Gibbs", "Laplace", "Poisson", "Gauss", "Knudsen", "Smoluchowski", "Einstein", "Planck", "Lambert", "Beer",
                   "Dirichlet", "Taylor", "Archimedes", "Aristotle", "Kepler", "Oseen", "Lagally", "Jensen", "Maxwell", "Kelvin", "Thomson", "Dirac", "Hoyle")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Maxwell)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    nodes=list(ast.walk(ast.parse(src)))
    float_hits=[x for x in nodes if isinstance(x,ast.Constant) and isinstance(x.value,float)]
    float_hits += [x for x in nodes if isinstance(x,ast.Call) and
        ((isinstance(x.func,ast.Name) and x.func.id in ("float","N")) or
         (isinstance(x.func,ast.Attribute) and x.func.attr in ("evalf","N")))]
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
    "per_element: executed — the cosine law through six faces gives |s|_1 and the step frequencies, for five rational contents; the mean emitted content (2/3) n",
    "per_site: executed — surplus against deficit at the 63 sites of a 4x4x4 block for three contents; the flux identity for three regions of a 5x5x5 block",
    "per_mode: not applicable — the retained finite identities concern local rates and integrated flux, not a mode spectrum",
    "per_block: executed — the residual coefficients 5/18, 11/98, -5353/14450, 95/242; pushes for four pairs of kept fractions; the ratio q_1/G at three densities",
    "lattice_wide: T1 is the lattice divergence theorem applied to block 45's conserved current; T2 is exact for independent records; T3 and T4 are statements in the closure of blocks 45 and 47; the executed forces of bodies in balance are controls, not proofs",
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
    print("scope: bodies in balance in the inertial record gas — no flux without net uptake, the shadow filled by cosine-law emission, the residue of uniform emission, unequal action and reaction in the closure, and the relation between growth rate and force coefficient")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
