#!/usr/bin/env python3
"""Exact checks: the fields of the record layer arrive by diffusion.

Scope.  The two fields found in the record layer under the supplied readings of blocks 39-42 are (i) the mean occupancy under symmetric
transit with a source (block 41, T5) and (ii) the linearized self-consistent odds (block 42, T2).  Both are driven by the same operator:
one tick replaces a field by W = 1 + h Lap applied to it (h the hop probability per neighbour, 6h <= 1; for the odds on the massless
surface h = 1/6, for the odds elsewhere W is multiplied by 6 l1 < 1).  T1: a wave of wavevector k is multiplied by 1 - h E(k) per tick;
by (1 - x)^n >= 1 - n x the slowest mode of a torus of side L keeps more than half its deviation for n < 1/(2 h E_min) ticks, and
E_min = 2(1 - cos(2 pi/L)) <= (2 pi/L)^2.  T2: the s-tick kernel of the walk has total weight 1, vanishes beyond s steps, and has
mean-square reach exactly 6 h s, so the share of what a source has emitted that lies beyond distance R after s ticks is at most
6 h s/R^2, and the response to a source switched on at tick 0 is the sum of the kernels.  T3: one linearized iteration of the odds map
of block 42 is one step of this walk, weighted by 6 l1 (exactly 1 on the surface 5p = 7q + 4r).  T4: with a mass term the factor is
(1 - h m^2)(...) and a mode with E(k) <= m^2 keeps more than half its deviation for n < 1/(4 h m^2) ticks: a range of 1/m costs of the
order of (range)^2/h ticks.  Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_RECORD_LAYER_FIELDS_ARRIVE_BY_DIFFUSION_ESTABLISHMENT_TIME_GROWS_AS_THE_SQUARE_OF_THE_RANGE_TRANSIT_HALO_AND_MASSLESS_ODDS_FIELD_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_record_layer_fields_arrive_by_diffusion_establishment_time_grows_as_the_square_of_the_range_transit_halo_and_massless_odds_field_bounded_theorem_note_2026-09-20"
AXIOM_NEEDLES = (
    "A site never carries more than one record; records are permanent.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
)

MUTATION_GATE = {
    "mode_factor_wrong": "B",
    "slowest_mode_bound_wrong": "B",
    "mean_square_reach_ballistic_injected": "C",
    "tail_bound_dropped_factor": "C",
    "odds_step_not_the_walk_injected": "D",
    "mass_term_trade_off_wrong": "E",
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


M6 = range(6)
AXIS = {0: (0, 0, 1), 1: (0, 0, -1), 2: (1, 0, 0), 3: (-1, 0, 0), 4: (0, 1, 0), 5: (0, -1, 0)}
STEPS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
COS = {4: (Fraction(1), Fraction(0), Fraction(-1), Fraction(0)), 6: (Fraction(1), Fraction(1, 2), Fraction(-1, 2), Fraction(-1), Fraction(-1, 2), Fraction(1, 2))}
PI_SQ_LOW = Fraction(98696, 10000)                  # a rational lower bound for pi squared


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the sentences used")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    ok = True
    for L in (4, 6):
        cosv = COS[L]
        for h in (Fraction(1, 6), Fraction(1, 12)):
            for k in ((1, 0, 0), (1, 1, 0), (2, 1, 3 % L), (L // 2, L // 2, L // 2)):
                e_k = 6 - 2 * sum(cosv[c % L] for c in k)
                for x in ((0, 0, 0), (1, 2, 3), (3, 1, 2)):
                    wave = lambda y: cosv[sum(k[i] * y[i] for i in range(3)) % L]
                    stepped = wave(x) + h * (sum(wave(tuple(x[i] + s[i] for i in range(3))) for s in STEPS) - 6 * wave(x))
                    factor = (1 - 2 * h * e_k) if mut("mode_factor_wrong") else (1 - h * e_k)
                    ok = ok and stepped == factor * wave(x)
    checks.check("B1", ok, "T1: on the tori of side 4 and 6 one tick of W = 1 + h Lap multiplies a cosine wave of wavevector k by 1 - h E(k), for h = 1/6 and 1/12")
    ok = True
    shown = []
    for L in (4, 6):
        e_min = 2 * (1 - COS[L][1])
        bound = 4 * PI_SQ_LOW / (L * L)
        ok = ok and ((e_min >= bound) if mut("slowest_mode_bound_wrong") else (e_min <= bound))
        for h in (Fraction(1, 6), Fraction(1, 12)):
            x = h * e_min
            n_max = int(1 / (2 * x))
            for n in range(0, n_max + 1):
                ok = ok and (1 - x) ** n >= 1 - n * x and ((1 - x) ** n >= Fraction(1, 2) if n * x <= Fraction(1, 2) else True)
        shown.append(f"side {L}: E_min = {e_min}")
    ok=ok and 1-Fraction(1,6)*12==-1
    checks.check("B2", ok, f"T1: the slowest mode has E_min = 2(1 - cos(2 pi/L)) <= (2 pi/L)^2 ({'; '.join(shown)}), and by (1 - x)^n >= 1 - n x it keeps at least half its deviation for every n <= 1/(2 h E_min): half the relaxation of a torus of side L costs at least L^2/(8 pi^2 h) ticks")


# ============================================================================================ family C (T2)
def kernels(s_max):
    """integer path counts N_s(x) of the simple walk (h = 1/6) for s = 0..s_max"""
    cur = {(0, 0, 0): 1}
    out = [cur]
    for _ in range(s_max):
        nxt = {}
        for x, n in cur.items():
            for st in STEPS:
                y = (x[0] + st[0], x[1] + st[1], x[2] + st[2])
                nxt[y] = nxt.get(y, 0) + n
        cur = nxt
        out.append(cur)
    return out


def family_c(checks: Checks) -> None:
    s_max = 12
    ks = kernels(s_max)
    ok = True
    for s, ker in enumerate(ks):
        total = sum(ker.values())
        msd = sum(n * (x[0] ** 2 + x[1] ** 2 + x[2] ** 2) for x, n in ker.items())
        want = (s * s if mut("mean_square_reach_ballistic_injected") else s) * 6 ** s
        ok = ok and total == 6 ** s and msd == want and all(abs(x[0]) + abs(x[1]) + abs(x[2]) <= s for x in ker)
    checks.check("C1", ok, "T2: the s-tick kernel of the walk, s = 0..12, by exact path counts: total weight 1, nothing beyond s steps, mean-square reach exactly s (6 h s at h = 1/6): what a source emits travels the square root of the time")
    ok = True
    for s, ker in enumerate(ks):
        for big_r in (2, 3, 4, 5, 6):
            beyond = sum(n for x, n in ker.items() if x[0] ** 2 + x[1] ** 2 + x[2] ** 2 >= big_r ** 2)
            cap = Fraction(s, (2 * big_r * big_r) if mut("tail_bound_dropped_factor") else (big_r * big_r))
            ok = ok and Fraction(beyond, 6 ** s) <= cap
    # response to a source switched on at tick 0: u_{t+1} = W u_t + delta equals the sum of the kernels
    u = {}
    for t in range(s_max):
        nxt = {}
        for x, v in u.items():
            for st in STEPS:
                y = (x[0] + st[0], x[1] + st[1], x[2] + st[2])
                nxt[y] = nxt.get(y, 0) + v / 6
        nxt[(0, 0, 0)] = nxt.get((0, 0, 0), 0) + Fraction(1)
        u = nxt
    summed = {}
    for s in range(s_max):
        for x, n in ks[s].items():
            summed[x] = summed.get(x, 0) + Fraction(n, 6 ** s)
    ok = ok and u == summed
    checks.check("C2", ok, "T2: the share of the kernel at distance R or more after s ticks is at most s/R^2 (R = 2..6, s = 0..12), and the response to a source switched on at tick 0 is the sum of the kernels: for a given share of what was emitted to lie beyond R, at least that share times R^2 ticks must pass")


# ============================================================================================ family D (T3)
class Dual:
    def __init__(self, a, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    @staticmethod
    def lift(o):
        return o if isinstance(o, Dual) else Dual(o)

    def __add__(self, o):
        o = Dual.lift(o)
        return Dual(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __mul__(self, o):
        o = Dual.lift(o)
        return Dual(self.a * o.a, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = Dual.lift(o)
        return Dual(self.a / o.a, (self.b * o.a - self.a * o.b) / (o.a * o.a))


def odds_at(om, nbr_fields):
    n = []
    for s in M6:
        t = 1
        for f in nbr_fields:
            t = t * sum((om[s][b] * f[b] for b in M6[1:]), om[s][0] * f[0])
        n.append(t)
    tot = sum(n[1:], n[0])
    return [v / tot for v in n]


def family_d(checks: Checks) -> None:
    ok = True
    shown = []
    for (p, q, r) in ((3, 1, 2), (5, 2, 4)):
        om = [[Fraction(p if a == b else q if a == (b ^ 1) else r) for b in M6] for a in M6]
        l1 = Fraction(p - q, p + q + 4 * r)
        # a unit lean along z at one neighbour: departure (e_z(b))/2 ; read the lean it induces at the site
        fl = [[Dual(Fraction(1, 6), Fraction(AXIS[b][2], 2) if i == 0 else 0) for b in M6] for i in range(6)]
        out = odds_at(om, fl)
        lean = sum(out[s].b * AXIS[s][2] for s in M6)
        want = Fraction(1, 6) if (p, q, r) == (3, 1, 2) or mut("odds_step_not_the_walk_injected") else l1
        ok = ok and lean == want and all(sum(out[s].b * AXIS[s][i] for s in M6) == 0 for i in (0, 1))
        shown.append(f"({p},{q},{r}): {lean}")
    checks.check("D1", ok, f"T3: by exact differentiation of block 42's odds map, a unit lean at one neighbour induces the lean l1 at the site ({'; '.join(shown)}): one linearized iteration of the odds is one step of the walk of T2 weighted by 6 l1, exactly the walk on the surface 5p = 7q + 4r")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    ok = True
    for h in (Fraction(1, 6), Fraction(1, 12)):
        for m2 in (Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)):
            for e_k in (m2, m2 / 2, m2 / 10):
                x = 1 - (1 - h * m2) * (1 - h * e_k)               # one tick: removal at rate h m^2, then the walk
                denom = (2 if mut("mass_term_trade_off_wrong") else 4) * h * m2
                n_max = int(1 / denom)
                ok = ok and x <= 2 * h * m2
                ok = ok and (1 - x) ** n_max >= 1 - n_max * x and 1 - n_max * x >= Fraction(1, 2)
    # Sequential killing and hopping changes the static mass parameter.
    for h,m2,e in ((Fraction(1,6),Fraction(1,10),Fraction(2)),(Fraction(1,12),Fraction(1,2),Fraction(1))):
        mu2=m2/(1-h*m2)
        ok=ok and 1-(1-h*m2)*(1-h*e)==h*(1-h*m2)*(mu2+e)
    checks.check("E1", ok, "T4: with removal at the rate h m^2 per tick (a mass term m^2) a mode with E(k) <= m^2 loses at most 2 h m^2 of its deviation per tick and keeps at least half of it for every n <= 1/(4 h m^2): the stated modes have a lower bound 1/(4hm^2), with effective squared mass m^2/(1-hm^2)")


# ============================================================================================ family F
FENCES = (
    "This note analyzes supplied walk updates associated with the record-layer fields of blocks 39 to 42; its tail and mode bounds do not prove general settling, and it adopts nothing.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Yukawa", "Goldstone", "Gibbs", "Boltzmann", "Laplace", "Poisson", "Coulomb", "Cauchy", "Schwarz", "Bayes", "Bernoulli", "Markov", "Chebyshev", "Fick", "Fourier", "Planck", "Einstein", "Brown", "Helmholtz")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Fick)", 1)
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
    "per_element: executed — the lean induced at a site by a unit lean at one neighbour, by exact differentiation, at two triples",
    "per_site: executed — cosine waves under one tick at sample sites of the tori of side 4 and 6; the response to a switched-on source against the sum of the kernels at every site reached in 12 ticks",
    "per_mode: executed — the factor 1 - h E(k) for four wavevectors, two sides, two hop probabilities; the slowest mode and its half-life bound",
    "per_block: executed — exact path counts of the walk for 0 to 12 ticks: weight, light cone, mean-square reach, tail shares beyond R = 2..6",
    "lattice_wide: T1 holds on every torus, T2 on the infinite lattice for every number of ticks (weight, light cone and mean-square reach by induction on the tick), T3 derivative for positive triples, killed-walk interpretation only for 0<=6*l1<=1, T4 for 0<hm^2<1 and hE<=1; nothing is claimed about carriers whose dynamics is not of this first-order kind",
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
    print("scope: the record layer's two fields (the transit halo and the linearized odds) are driven by one walk operator and settle by diffusion: half-life of a torus at least L^2/(8 pi^2 h) ticks, reach the square root of the time, the retained damping result is a low-mode lower bound with effective mass m^2/(1-hm^2); exact")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
