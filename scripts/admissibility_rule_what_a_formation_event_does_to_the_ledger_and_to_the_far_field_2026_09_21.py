#!/usr/bin/env python3
"""Exact checks: what a formation event does to the ledger and to the far field (supplied clauses on Z^3; not adopted).

SETTING (blocks 53-56, open PRs; supplied): rates w = phi^2; the simplest bond energy; a box whose walls are held at the ambient rate; block 56's
exact static law ((1 - A) + (gamma/12) M) phi = 0.  An amplitude AT REST spread over sites with weights |chi_x|^2 is, for that law, a set of
bodies at rest with bare energies m_x = m |chi_x|^2 (block 55: e_x = m w_x |chi_x|^2).  A FORMATION EVENT replaces it by one record at a site y,
a body at rest with a bare energy m'.  No rule for where or when records form is assumed.
T1 (the ledger through the event): the ledger before is E = sum m_x phi_x; after, m'/(1 + (gamma/12) g_y m').  It is kept iff
   m' = E/(1 - (gamma/12) g_y E), which exists iff E < 12/(gamma g_y): an amplitude whose ledger exceeds what one site can show cannot form one
   record with the ledger kept.  Keeping the bare energy instead (m' = m) lowers the ledger.
T2 (the outside): the ledger is the sum over wall sites of dF/du, so with the ledger kept the total flux through the walls does not change:
   the monopole never jumps.  More: for every discrete-harmonic h, sum over wall bonds of (1 - phi_inside) h_wall = 6 sum_x q_x h_x with
   q_x = (gamma/12) m_x phi_x; with h = a coordinate, the first moment of the wall flux is six times the dipole P = sum q_x x.
T3 (the dipole jumps): P goes from Q Xbar to Q y, Q = (gamma/12) E, Xbar the centre weighted by q_x (that is by |chi_x|^2 phi_x).  For ANY odds
   p_y of forming at y the mean jump is Q (sum_y p_y y - Xbar): zero for every amplitude if p is proportional to q; for p proportional to
   |chi|^2 it is Q (probability centre - Xbar), not zero once the rates differ across the amplitude (its own field suffices).
T4 (records only): if the amplitude sources nothing, the flux through the walls is zero before and m' phi'_y after: a monopole from nothing.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_WHAT_A_FORMATION_EVENT_DOES_TO_THE_LEDGER_AND_TO_THE_FAR_FIELD_THE_MONOPOLE_NEVER_JUMPS_THE_DIPOLE_DOES_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_what_a_formation_event_does_to_the_ledger_and_to_the_far_field_the_monopole_never_jumps_the_dipole_does_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)
RECORD_NEEDLES = (
    "permanent",
)

MUTATION_GATE = {
    "record_keeps_the_bare_energy_and_the_ledger": "B",
    "any_ledger_fits_on_one_site": "B",
    "outside_sees_the_formation": "C",
    "wall_flux_moment_is_not_the_dipole": "C",
    "dipole_does_not_jump": "D",
    "probability_odds_hold_the_centre": "D",
    "records_only_leaves_the_outside_unchanged": "E",
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


F = Fraction
ZERO = F(0)
ONE = F(1)
E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
SIDE = 7                                                     # sites 0..6; walls at 0 and 6; 125 interior sites
INTERIOR = [s for s in product(range(1, SIDE - 1), repeat=3)]
INDEX = {s: i for i, s in enumerate(INTERIOR)}
GAMMA = F(3, 5)


def about(v) -> str:
    """A rational to three decimal places, by integer rounding (descriptive only; every comparison in this runner is exact)."""
    k = round(v * 1000)
    sign = "-" if k < 0 else ""
    k = abs(k)
    return f"{sign}{k // 1000}.{k % 1000:03d}"


def solve_multi(a, rhs_list):
    """Solve a x = b exactly for several right-hand sides at once; the matrix must be non-singular."""
    n = len(a)
    k = len(rhs_list)
    rows = [[F(c) for c in a[i]] + [F(r[i]) for r in rhs_list] for i in range(n)]
    for col in range(n):
        piv = next((i for i in range(col, n) if rows[i][col] != 0), None)
        if piv is None:
            raise ValueError("singular")
        rows[col], rows[piv] = rows[piv], rows[col]
        pv = rows[col][col]
        rows[col] = [c / pv for c in rows[col]]
        for i in range(n):
            if i != col and rows[i][col] != 0:
                fac = rows[i][col]
                rows[i] = [x - fac * y for x, y in zip(rows[i], rows[col])]
    return [[rows[i][n + j] for i in range(n)] for j in range(k)]


def operator(masses):
    """Matrix of (1 - A) + (gamma/12) M on the interior, and the right-hand side from walls held at phi = 1."""
    n = len(INTERIOR)
    a = [[ZERO] * n for _ in range(n)]
    b = [ZERO] * n
    for s in INTERIOR:
        i = INDEX[s]
        a[i][i] = ONE + GAMMA / 12 * masses.get(s, ZERO)
        for e in E6:
            t = (s[0] + e[0], s[1] + e[1], s[2] + e[2])
            if t in INDEX:
                a[i][INDEX[t]] -= F(1, 6)
            else:
                b[i] += F(1, 6)
    return a, b


def rates(masses):
    a, b = operator(masses)
    sol = solve_multi(a, [b])[0]
    return {s: sol[INDEX[s]] for s in INTERIOR}


def value(phi, t):
    return phi[t] if t in phi else ONE                       # walls at the ambient rate


def ledger_parts(phi, masses):
    matter = sum((m * phi[s] ** 2 for s, m in masses.items()), ZERO)
    bonds = ZERO
    for s in product(range(SIDE), repeat=3):
        for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            t = (s[0] + e[0], s[1] + e[1], s[2] + e[2])
            if max(t) >= SIDE:
                continue
            bonds += (value(phi, s) - value(phi, t)) ** 2
    return matter, 2 / GAMMA * bonds


def wall_term(phi):
    """sum over wall sites of dF/du_x = (2/gamma) phi_x sum_y (phi_x - phi_y), phi = 1 on the walls."""
    tot = ZERO
    for s in product(range(SIDE), repeat=3):
        if s in INDEX:
            continue
        for e in E6:
            t = (s[0] + e[0], s[1] + e[1], s[2] + e[2])
            if t in INDEX:
                tot += ONE - phi[t]
    return 2 / GAMMA * tot



# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES) and all(n in axioms for n in RECORD_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, Admissibility does not define a time metric, and a record is permanent")


def flux_moment(phi, h):
    """sum over bonds from a wall site y to an interior site x of (1 - phi_x) h(y)."""
    tot = ZERO
    for s in product(range(SIDE), repeat=3):
        if s in INDEX:
            continue
        for e in E6:
            t = (s[0] + e[0], s[1] + e[1], s[2] + e[2])
            if t in INDEX:
                tot += (ONE - phi[t]) * h(s)
    return tot


def potential_at(y):
    a, _ = operator({})
    r = [ZERO] * len(INTERIOR)
    r[INDEX[y]] = ONE
    return solve_multi(a, [r])[0][INDEX[y]]


CENTRE = (3, 3, 3)
BARE = F(4)
WEIGHTS = {(2, 3, 3): F(1, 2), (3, 3, 3): F(1, 8), (4, 3, 3): F(1, 8), (4, 4, 3): F(1, 8), (3, 3, 4): F(1, 8)}       # |chi_x|^2, summing to one


def spread():
    masses = {s: BARE * p for s, p in WEIGHTS.items()}
    phi = rates(masses)
    return masses, phi, sum((m * phi[s] for s, m in masses.items()), ZERO)


# ============================================================================================ family B
def family_b(checks: Checks):
    masses, phi, ledger = spread()
    g_y = potential_at(CENTRE)
    m_rec = ledger / (1 - GAMMA / 12 * g_y * ledger)
    phi_after = rates({CENTRE: m_rec})
    claimed = BARE if mut("record_keeps_the_bare_energy_and_the_ledger") else m_rec          # the mutation claims the bare energy itself keeps the ledger
    kept = claimed * rates({CENTRE: claimed})[CENTRE] == ledger
    phi_same_bare = rates({CENTRE: BARE})
    drop = ledger - BARE * phi_same_bare[CENTRE]
    checks.check("B1", kept and m_rec > BARE and drop > 0, f"T1: an amplitude at rest of bare energy 4 spread over five sites (weights 1/2 and four times 1/8) has the ledger about {about(ledger)}; a record at the centre keeps it iff its bare energy is E/(1 - (gamma/12) g_y E) = about {about(m_rec)} (more than 4: a point slows its own clock more than a spread does); with the bare energy kept at 4 the ledger would fall by about {about(drop)}")
    cross = [CENTRE] + [(3 + e[0], 3 + e[1], 3 + e[2]) for e in E6]
    heavy = {s: F(60) for s in cross}
    phi_h = rates(heavy)
    ledger_h = sum((m * phi_h[s] for s, m in heavy.items()), ZERO)
    bound = 12 / (GAMMA * g_y)
    fits = ledger_h < bound
    if mut("any_ledger_fits_on_one_site"):
        fits = True
    checks.check("B2", (not fits) and all(F(10) ** k / (1 + GAMMA / 12 * g_y * F(10) ** k) < bound for k in range(1, 9)), f"T1: an amplitude of bare energy 420 spread over a site and its six neighbours has the ledger about {about(ledger_h)}, above 12/(gamma g_y) = {bound}, the most one site can show whatever its bare energy: no single record keeps that ledger")
    return masses, phi, ledger, g_y, m_rec, phi_after


# ============================================================================================ family C
def family_c(checks: Checks, state) -> None:
    masses, phi, ledger, g_y, m_rec, phi_after = state
    before, after = wall_term(phi), wall_term(phi_after)
    unchanged = before == after == ledger
    if mut("outside_sees_the_formation"):
        unchanged = before != after
    checks.check("C1", unchanged, "T2: the sum over wall sites of dF/du equals the ledger before and after the event: with the ledger kept, the total flux through the walls does not change when the record forms, wherever it forms: the monopole never jumps")
    ok = True
    for phi_k, ms in ((phi, masses), (phi_after, {CENTRE: m_rec})):
        for j in range(3):
            lhs = flux_moment(phi_k, lambda s, j=j: F(s[j]))
            dip = sum((GAMMA / 12 * m * phi_k[s] * s[j] for s, m in ms.items()), ZERO)
            if mut("wall_flux_moment_is_not_the_dipole"):
                dip = dip + F(1, 100)
            ok = ok and lhs == 6 * dip
    checks.check("C2", ok, "T2: the first moment of the wall flux, sum over wall bonds of (1 - phi_inside) x_wall, equals six times the dipole sum_x q_x x, q_x = (gamma/12) m_x phi_x, exactly, for each coordinate, before and after (a coordinate is a discrete-harmonic function): the dipole is something the walls see")


# ============================================================================================ family D
def family_d(checks: Checks, state) -> None:
    masses, phi, ledger, g_y, m_rec, phi_after = state
    q = {s: GAMMA / 12 * m * phi[s] for s, m in masses.items()}
    big_q = sum(q.values(), ZERO)
    xbar = [sum((v * s[j] for s, v in q.items()), ZERO) / big_q for j in range(3)]
    prob_centre = [sum((p * s[j] for s, p in WEIGHTS.items()), ZERO) for j in range(3)]
    jump = [GAMMA / 12 * m_rec * phi_after[CENTRE] * CENTRE[j] - sum((v * s[j] for s, v in q.items()), ZERO) for j in range(3)]
    want = [big_q * (CENTRE[j] - xbar[j]) for j in range(3)]
    jumps = jump == want and any(v != 0 for v in jump)
    if mut("dipole_does_not_jump"):
        jumps = all(v == 0 for v in jump)
    checks.check("D1", jumps and GAMMA / 12 * ledger == big_q, f"T3: the dipole goes from Q Xbar to Q y: it jumps by Q (y - Xbar) = ({', '.join(about(v) for v in jump)}) here, with Q = (gamma/12) E unchanged and Xbar the centre weighted by q_x, that is by |chi_x|^2 phi_x; no choice of the bare energy of the record avoids it unless y = Xbar")
    mean_charge = [sum((q[s] / big_q * s[j] for s in q), ZERO) - xbar[j] for j in range(3)]
    mean_prob = [prob_centre[j] - xbar[j] for j in range(3)]
    energy = {s: m * phi[s] ** 2 for s, m in masses.items()}
    mean_energy = [sum((v * s[j] for s, v in energy.items()), ZERO) / sum(energy.values(), ZERO) - xbar[j] for j in range(3)]
    holds = all(v == 0 for v in mean_charge) and any(v != 0 for v in mean_prob) and any(v != 0 for v in mean_energy) and mean_prob[0] * mean_energy[0] < 0
    if mut("probability_odds_hold_the_centre"):
        holds = all(v == 0 for v in mean_prob)
    lo, hi = min(phi[s] for s in masses), max(phi[s] for s in masses)
    checks.check("D2", holds, f"T3: for any odds p_y the mean jump is Q (sum p_y y - Xbar).  Odds proportional to q_x = |chi_x|^2 phi_x give exactly zero; odds proportional to |chi_x|^2 give Q times ({', '.join(about(v * 1000) for v in mean_prob)}) thousandths of a site here and odds proportional to the energy density |chi_x|^2 phi_x^2 give ({', '.join(about(v * 1000) for v in mean_energy)}) thousandths, on the other side, neither zero: the field of the amplitude itself makes the rate differ across it (phi from about {about(lo)} to {about(hi)} on its support), so the probability centre is not the centre the walls see.  No rule of formation is assumed or proposed")


# ============================================================================================ family E
def family_e(checks: Checks, state) -> None:
    masses, phi, ledger, g_y, m_rec, phi_after = state
    empty = rates({})
    before = wall_term(empty)
    after = wall_term(phi_after)
    appears = before == 0 and after == ledger and after > 0
    if mut("records_only_leaves_the_outside_unchanged"):
        appears = before == after
    checks.check("E1", appears and all(v == 1 for v in empty.values()), f"T4: if the amplitude sources nothing, the rates are ambient and the flux through the walls is zero before the event, and about {about(after)} after: under the records-only reading every formation event makes a monopole appear from nothing; under the reading of block 55 with the ledger kept the monopole never changes")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for local tick rates, for amplitudes timed by them and for a kept ledger, with the simplest bond energy of weight one; it reports what the replacement of a spread amplitude at rest by one record does to the ledger and to what the walls see; no rule of formation is assumed; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "event horizon", "horizon",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Hellmann", "Feynman", "Dirichlet", "Watson", "Lowner", "Stieltjes", "Kelvin", "Ghirardi", "Rimini", "Weber", "Pearle", "Diosi", "Penrose", "Bohr", "Neumann")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Green)", 1)
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
    "per_element: executed — the exact rates of a five-site amplitude at rest and of the record that replaces it, in a 7x7x7 box with walls at the ambient rate",
    "per_site: executed — the bare energy of the record that keeps the ledger; the fall of the ledger when the bare energy is kept; a seven-site amplitude whose ledger no single site can show",
    "per_mode: executed — the total flux through the walls and its three first moments, before and after the event, against the ledger and six times the dipole",
    "per_block: executed — the jump of the dipole against Q (y - Xbar); the mean jump for odds proportional to the charge density and to the probability density; the records-only flux before and after",
    "lattice_wide: T1 to T3 hold for any amplitude at rest and any site of formation in any box with walls at the ambient rate, for the simplest bond energy; the flux identities of T2 hold for every discrete-harmonic weight; the statement about odds is a statement about ANY odds and assumes none; whether an amplitude that has formed no record sources anything, whether a formation event keeps the ledger, and where records form are not decided; bodies at rest are supplied; nothing moves in this note",
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
    state = family_b(checks)
    family_c(checks, state)
    family_d(checks, state)
    family_e(checks, state)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: a formation event under the exact static law — the ledger is kept iff the bare energy of the record is E/(1 - (gamma/12) g_y E), possible only below what one site can show; the monopole seen at the walls never jumps, the dipole jumps by Q (y - Xbar), and its mean over any odds vanishes for odds proportional to the charge density; with records as the only sources a monopole appears from nothing")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
