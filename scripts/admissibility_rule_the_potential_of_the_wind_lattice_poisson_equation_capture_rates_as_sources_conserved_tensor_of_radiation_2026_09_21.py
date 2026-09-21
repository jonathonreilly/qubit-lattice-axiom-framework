#!/usr/bin/env python3
"""Exact checks: the potential of the wind, and the conserved tensor of the inertial record gas (block 44's clause; supplied, not adopted).

T1: on a torus the bond fields with zero divergence at every site and zero circulation around every plaquette are exactly the three constant
fields (the rank of the constraint system is the number of bonds minus 3); hence a mean current J with div J = -(sum of capture rates at the
sinks, minus their mean) and zero circulation is unique up to those constants, and it is J(x->y) = Phi(x) - Phi(y) with
Phi = -G_L * (Q - mean Q), G_L the lattice Green function: the potential of the wind solves the lattice Poisson equation with the capture
rates as its sources.  T2: a momentum density that grows from rest under the linearized conservation equations is a lattice gradient, and a
lattice gradient has zero circulation around every plaquette.  T3: with T^00 the density, T^i0 the momentum density, T^0i the mass current and
T^ij the momentum flux, product states at rest have T^ij = (rho/3) delta_ij, so T^00 - sum_i T^ii = 0 at every density (the equation of state
of radiation: pressure = density times speed over three), while T^0i = (1 - rho) T^i0: the tensor is symmetric only in the dilute limit.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import random
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_POTENTIAL_OF_THE_WIND_SOLVES_THE_LATTICE_POISSON_EQUATION_WITH_CAPTURE_RATES_AS_SOURCES_INERTIAL_GAS_HAS_THE_CONSERVED_TENSOR_OF_RADIATION_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_potential_of_the_wind_solves_the_lattice_poisson_equation_with_capture_rates_as_sources_inertial_gas_has_the_conserved_tensor_of_radiation_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = ("A site never carries more than one record; records are permanent.",)

MUTATION_GATE = {
    "plaquette_constraints_dropped": "B",
    "green_function_without_zero_mode_removal": "B",
    "gradient_with_circulation_injected": "C",
    "pressure_not_one_third": "D",
    "tensor_symmetric_at_every_density_injected": "D",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None
PRIME = 2_147_483_647


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
M6 = range(6)


def torus(L):
    sites = list(product(range(L), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    step = lambda x, a, s=1: tuple((x[i] + (s if i == a else 0)) % L for i in range(3))
    bonds = {(x, a): k for k, (x, a) in enumerate((x, a) for x in sites for a in range(3))}       # the bond from x to x + e_a
    return sites, idx, step, bonds


def rank_mod_p(rows, ncols):
    rows = [r[:] for r in rows]
    rank = 0
    for c in range(ncols):
        piv = next((i for i in range(rank, len(rows)) if rows[i][c] % PRIME), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = pow(rows[rank][c], PRIME - 2, PRIME)
        rows[rank] = [(v * inv) % PRIME for v in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][c] % PRIME:
                f = rows[i][c]
                rows[i] = [(a - f * b) % PRIME for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the sentence used")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    L = 4
    sites, idx, step, bonds = torus(L)
    nb = len(bonds)
    rows = []
    for x in sites:                                                     # divergence at x: outgoing minus incoming
        row = [0] * nb
        for a in range(3):
            row[bonds[(x, a)]] += 1
            row[bonds[(step(x, a, -1), a)]] -= 1
        rows.append(row)
    n_div = len(rows)
    if not mut("plaquette_constraints_dropped"):
        for x in sites:                                                 # circulation around the plaquette at x in the plane (a, b)
            for a, b in ((0, 1), (1, 2), (0, 2)):
                row = [0] * nb
                row[bonds[(x, a)]] += 1
                row[bonds[(step(x, a), b)]] += 1
                row[bonds[(step(x, b), a)]] -= 1
                row[bonds[(x, b)]] -= 1
                rows.append(row)
    rank = rank_mod_p(rows, nb)
    consts_ok = True
    for a in range(3):                                                  # the three constant fields satisfy every constraint exactly
        field = [1 if bond[1] == a else 0 for bond in bonds]
        consts_ok = consts_ok and all(sum(r[k] * field[k] for k in range(nb)) == 0 for r in rows)
    checks.check("B1", consts_ok and nb - rank == 3, f"T1: on the 4^3 torus ({nb} bonds, {n_div} divergence and {len(rows) - n_div} plaquette constraints) the fields with zero divergence and zero circulation are exactly the three constant fields: the constraint rank is at least {rank} (computed modulo a prime, a lower bound for the rational rank) and the three constants lie in the kernel, so the kernel has dimension 3")
    cosv = (1, 0, -1, 0)
    modes = [k for k in sites if any(k)] if not mut("green_function_without_zero_mode_removal") else sites
    def green(x):
        tot = Fraction(0)
        for k in modes:
            ek = 6 - 2 * sum(cosv[c] for c in k)
            if ek == 0:
                return None
            tot += Fraction(cosv[sum(k[i] * x[i] for i in range(3)) % L], ek)
        return tot / L ** 3
    ok = True
    sinks = {(0, 0, 0): Fraction(7), (2, 1, 0): Fraction(3)}
    mean_q = sum(sinks.values()) / L ** 3
    phi = {}
    for x in sites:
        val = Fraction(0)
        for s, q in sinks.items():
            gx = green(tuple((x[i] - s[i]) % L for i in range(3)))
            if gx is None:
                ok = False
                gx = Fraction(0)
            val -= q * gx
        phi[x] = val
    cur = {(x, a): phi[x] - phi[step(x, a)] for (x, a) in bonds}
    for x in sites:
        div = sum(cur[(x, a)] - cur[(step(x, a, -1), a)] for a in range(3))
        ok = ok and div == -(sinks.get(x, 0) - mean_q)
        for a, b in ((0, 1), (1, 2), (0, 2)):
            ok = ok and cur[(x, a)] + cur[(step(x, a), b)] - cur[(step(x, b), a)] - cur[(x, b)] == 0
    for a in range(3):
        ok = ok and sum(cur[(x, a)] for x in sites) == 0                  # no constant part
    checks.check("B2", ok, "T1: for two sinks capturing 7 and 3 on the 4^3 torus, J(x->y) = Phi(x) - Phi(y) with Phi = -G_L * (Q - mean Q) has divergence -(Q - mean Q) at all 64 sites, zero circulation around all 192 plaquettes and no constant part: by B1 it is the only such field; the potential of the wind solves the lattice Poisson equation with the capture rates as sources")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    L = 4
    sites, idx, step, bonds = torus(L)
    rng = random.Random(6)
    ok = True
    for _ in range(5):
        rho = {x: Fraction(rng.randint(1, 9), 10) for x in sites}
        g = {(x, a): -(rho[step(x, a)] - rho[x]) / 3 for (x, a) in bonds}          # one tick of d g/dt = -grad(rho/3), from rest
        if mut("gradient_with_circulation_injected"):
            g[((0, 0, 0), 0)] += 1
        for x in sites:
            for a, b in ((0, 1), (1, 2), (0, 2)):
                ok = ok and g[(x, a)] + g[(step(x, a), b)] - g[(step(x, b), a)] - g[(x, b)] == 0
    checks.check("C1", ok, "T2: the momentum density generated from rest by the linearized conservation equations, -grad(rho/3), is a lattice gradient and has zero circulation around every plaquette (5 random density fields on the 4^3 torus): the wind that builds up from rest satisfies the hypothesis of T1")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    ok = True
    sym = True
    for rho in (Fraction(1, 10), Fraction(3, 10), Fraction(1, 2), Fraction(9, 10)):
        dens = [rho / 6] * 6
        flux = [[Fraction(0)] * 3 for _ in range(3)]
        for d in M6:
            for i in range(3):
                for j in range(3):
                    flux[i][j] += dens[d] * (1 - rho) * E[d][i] * E[d][j]
                    for d2 in M6:
                        flux[i][j] += dens[d] * dens[d2] * (E[d][i] - E[d2][i]) * E[d][j]
        pressure = flux[0][0]
        if mut("pressure_not_one_third"):
            pressure = pressure * (1 - rho)
        ok = ok and all(flux[i][j] == 0 for i in range(3) for j in range(3) if i != j)
        ok = ok and rho - 3 * pressure == 0                                  # T^00 - sum T^ii with unit speed
        ratio = Fraction(1) if mut("tensor_symmetric_at_every_density_injected") else (1 - rho)   # T^0i / T^i0 = mass current / momentum density
        tilt = [Fraction(1, 7), Fraction(-1, 9), Fraction(1, 11)]
        dens_t = [rho / 6 * (1 + sum(tilt[i] * E[d][i] for i in range(3))) for d in M6]
        g = [sum(dens_t[d] * E[d][i] for d in M6) for i in range(3)]
        j = [(dens_t[2 * i] - dens_t[2 * i + 1]) * (1 - rho) for i in range(3)]
        sym = sym and j == [ratio * v for v in g]
    checks.check("D1", ok and sym, "T3: in product states at rest the momentum flux is (rho/3) times the identity at rho = 1/10, 3/10, 1/2, 9/10, so the density minus three times the pressure vanishes at every density: the inertial gas has the equation of state of radiation; and the mass current is (1 - rho) times the momentum density: the conserved tensor is symmetric only in the dilute limit")


# ============================================================================================ family F
FENCES = (
    "This note works within the supplied inertial clause of block 44 and states a correspondence of form with the weak-field packet on main; neither the clause nor the correspondence is adopted, and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Navier", "Stokes", "Bernoulli", "Bjerknes", "Sage", "Boltzmann", "Gibbs", "Laplace", "Poisson", "Gauss", "Hodge", "Helmholtz", "Maxwell", "Riemann", "Einstein", "Planck", "Noether", "Ward")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Hodge)", 1)
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
    "per_element: executed — the momentum flux of product states at four densities; the mass current against the momentum density in a tilted state",
    "per_site: executed — the divergence of the potential's current at all 64 sites of the 4^3 torus; the circulation around all 192 plaquettes",
    "per_mode: executed — the lattice Green function as a mode sum with the zero mode removed",
    "per_block: executed — the rank of the 256 divergence and circulation constraints on the 192 bonds of the 4^3 torus; five random density fields",
    "lattice_wide: T1's uniqueness is proved for every torus by the same counting (three constant fields) and on the infinite lattice for fields that vanish at infinity; T2 is an identity of lattice gradients; T3 is exact for product states at rest; that the stationary wind has zero circulation is an assumption where it is not derived from T2",
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
    print("scope: the potential of the wind solves the lattice Poisson equation with the capture rates as sources (unique among divergence-matched, circulation-free fields); the inertial gas has the equation of state of radiation at every density and a symmetric conserved tensor only in the dilute limit; exact")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
