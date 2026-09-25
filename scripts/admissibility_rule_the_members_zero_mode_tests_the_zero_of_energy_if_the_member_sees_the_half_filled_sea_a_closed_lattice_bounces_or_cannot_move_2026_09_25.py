#!/usr/bin/env python3
"""Exact checks: the member's zero mode tests the zero of energy - within block 146's zero-mode constraint (open) on block 60's
homogeneous model, with blocks 139 and 101 as landed: the walk's spectrum is symmetric about the books' zero, so the half-filled
sea has negative energy; on a uniformly stretched lattice it is -I/l per site for the massless walk (I = (3 + sqrt 3 + 3 sqrt 2)/8
on the 4^3 torus) and -<sqrt(mu^2 + s^2/l^2)> with the staggered mass; per unit volume it never stays constant. If the member sees
the sea, a closed lattice holding only the sea has no uniform motion; with rest content m0 and the massless sea it turns at
l = I/m0 (a bounce), with an exact history; with the massive sea it can reach large lengths only if m0 > mu. If the member sees
energy above the sea, block 146 holds unchanged (the supervisor's own derivation; not adopted).

B (T1): the sea's energy: the spectrum's symmetry, the massless sum on a torus, the stretched spectra.
C (T2): the member sees the sea: the sea alone; the massless sea with rest content (the turn and its history).
D (T2): the massive sea with rest content: monotonic net energy; the threshold m0 > mu.
E (T1): the sea per unit volume never stays constant.
Exact symbolic and rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_MEMBERS_ZERO_MODE_TESTS_THE_ZERO_OF_ENERGY_IF_THE_MEMBER_SEES_THE_HALF_FILLED_SEA_A_CLOSED_LATTICE_BOUNCES_OR_CANNOT_MOVE_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "sea_sign_flipped": "B",
    "hardcore_parity_forged": "B",
    "turn_length_forged": "C",
    "bounce_history_forged": "C",
    "mass_threshold_forged": "D",
    "constant_density_forged": "E",
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
HALF = sp.Rational(1, 2)
QUARTER = sp.Rational(1, 4)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the member, its kinetic term, the walk, its sea and the zero of energy the member sees are supplied; the memo does not define a time metric)")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    import itertools
    L = 4
    ks = [sp.Rational(2 * j, L) * sp.pi for j in range(L)]
    total = 0
    for k in itertools.product(ks, repeat=3):
        total += sp.sqrt(sp.nsimplify(sum(sp.sin(x) ** 2 for x in k)))
    I4 = sp.nsimplify(total) / L ** 3
    sign = -1 if mut("sea_sign_flipped") else 1
    I4_ok = sp.simplify(sign * I4 - (3 + sp.sqrt(3) + 3 * sp.sqrt(2)) / 8) == 0
    s = sp.symbols("s1:4", real=True)
    l, mu = sp.symbols("l mu", positive=True)
    sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    ss = sum((sig[a] * s[a] for a in range(3)), sp.zeros(2, 2)) / l
    block = sp.Matrix(sp.BlockMatrix([[ss, mu * sp.eye(2)], [mu * sp.eye(2), -ss]]))
    sq = sp.simplify(block * block - (mu ** 2 + sum(x ** 2 for x in s) / l ** 2) * sp.eye(4)) == sp.zeros(4, 4)
    traceless = sp.simplify(block.trace()) == 0 and sp.simplify(ss.trace()) == 0
    checks.check("B1", I4_ok and sq and traceless,
                 "the walk's spectrum is traceless (symmetric about the books' zero), so the half-filled sea has negative energy: -I/l per site for the massless walk on a stretched lattice, I = (3 + sqrt 3 + 3 sqrt 2)/8 on the 4^3 torus; with the staggered mass mu the stretched block squares to (mu^2 + s^2/l^2), so the sea has -<sqrt(mu^2 + s^2/l^2)> per site")

    # one record per site: two hard-core walkers on the 4^3 torus; every hop moves one walker one step and flips its sublattice sign
    Lh = 4
    sites = list(itertools.product(range(Lh), repeat=3))
    sidx = {x: i for i, x in enumerate(sites)}
    sigq = [[[(Fr(0), Fr(0)), (Fr(1), Fr(0))], [(Fr(1), Fr(0)), (Fr(0), Fr(0))]],
            [[(Fr(0), Fr(0)), (Fr(0), Fr(-1))], [(Fr(0), Fr(1)), (Fr(0), Fr(0))]],
            [[(Fr(1), Fr(0)), (Fr(0), Fr(0))], [(Fr(0), Fr(0)), (Fr(-1), Fr(0))]]]

    def cmul(a, b):
        return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

    entries = {}
    for occ in itertools.combinations(range(len(sites)), 2):
        for cs in itertools.product((0, 1), repeat=2):
            for w in range(2):
                x = sites[occ[w]]
                other = occ[1 - w]
                for a in range(3):
                    for sgn in (1, -1):
                        y = list(x)
                        y[a] = (y[a] + sgn) % Lh
                        j = sidx[tuple(y)]
                        if j == other:
                            continue
                        for c2 in (0, 1):
                            e = cmul((Fr(0), Fr(-sgn, 2)), sigq[a][c2][cs[w]])
                            if e == (0, 0):
                                continue
                            no, nc = [occ[0], occ[1]], [cs[0], cs[1]]
                            no[w], nc[w] = j, c2
                            pair = sorted(zip(no, nc))
                            dst = (tuple(q[0] for q in pair), tuple(q[1] for q in pair))
                            old = entries.get((dst, (occ, cs)), (Fr(0), Fr(0)))
                            entries[(dst, (occ, cs))] = (old[0] + e[0], old[1] + e[1])
    entries = {k: v for k, v in entries.items() if v != (0, 0)}

    def parity(state):
        if mut("hardcore_parity_forged"):
            return (-1) ** sum(sites[state[0][0]])
        return (-1) ** sum(sum(sites[q]) for q in state[0])

    anti = all(parity(d) == -parity(src) for (d, src) in entries)
    herm = all(entries.get((src, d), (0, 0)) == (v[0], -v[1]) for (d, src), v in entries.items())
    checks.check("B2", anti and herm and len(entries) > 0,
                 "one record per site: the compressed hopping of two walkers on the 4^3 torus (8064 states) is hermitian, nonzero and anticommutes with the product of sublattice signs over occupied sites; each hop moves one walker one step, so for any number of walkers the spectrum is symmetric and the hard-core sea's energy is negative too")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    al, m0, I, l = sp.symbols("alpha m0 I l", positive=True)
    ldot2 = (m0 * l - I) / (24 * al * l ** 2)
    alone = sp.simplify((-I / l) / (24 * al * l ** 3)) < 0
    lmin = sp.solve(sp.Eq(m0 * l - I, 0), l)[0]
    target_min = (2 * I / m0) if mut("turn_length_forged") else I / m0
    lamdd = sp.simplify(-(I / l) / (2 * (-24 * al) * l ** 3)).subs(l, lmin)
    turn_ok = sp.simplify(lmin - target_min) == 0 and sp.simplify(lamdd - m0 ** 4 / (48 * al * I ** 3)) == 0
    checks.check("C1", alone and turn_ok, "if the member sees the sea: with the sea alone the constraint 24 alpha l^3 lamdot^2 = m has m < 0, no uniform motion; with rest content m0 and the massless sea (m = m0 - I/l) the lattice turns at l = I/m0, where lambda-ddot = m0^4/(48 alpha I^3) > 0: a bounce")
    coef = 3 if mut("bounce_history_forged") else sp.Rational(2, 3)
    tl = sp.sqrt(24 * al) / m0 ** 2 * (coef * (m0 * l - I) ** sp.Rational(3, 2) + 2 * I * sp.sqrt(m0 * l - I))
    hist = sp.simplify(sp.diff(tl, l) ** 2 - 1 / ldot2) == 0 and sp.simplify(tl.subs(l, lmin)) == 0
    checks.check("C2", hist, "the exact history from the bounce: t(l) = +-(sqrt(24 alpha)/m0^2)[(2/3)(m0 l - I)^(3/2) + 2 I (m0 l - I)^(1/2)]")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    mu, l, s2 = sp.symbols("mu l s2", positive=True)
    mode = sp.sqrt(mu ** 2 + s2 / l ** 2)
    decreasing = sp.simplify(sp.diff(mode, l) + s2 / (l ** 3 * mode)) == 0
    lim_large = sp.limit(mode, l, sp.oo) == mu
    small = sp.limit(mode * l, l, 0) == sp.sqrt(s2)
    m0 = sp.Symbol("m0", positive=True)
    threshold = mu + 1 if mut("mass_threshold_forged") else mu
    net_large = sp.limit(m0 - mode, l, sp.oo) - (m0 - threshold)
    checks.check("D1", decreasing and lim_large and small and sp.simplify(net_large) == 0,
                 "each massive mode's sea energy sqrt(mu^2 + s^2/l^2) falls with l, from s/l at small l to mu at large l; so the net energy m0 - <sqrt(mu^2 + s^2/l^2)> rises with l to m0 - mu: the lattice reaches large lengths only if m0 > mu, turning once where the net energy vanishes, and has no uniform motion at all if m0 <= mu")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    I, mu, s2, lam = sp.symbols("I mu s2 lam", positive=True)
    l = sp.exp(lam)
    massless = -I / l / l ** 3
    massive = -sp.sqrt(mu ** 2 + s2 / l ** 2) / l ** 3
    const = sp.Symbol("rho0")
    d1 = sp.simplify(sp.diff(massless, lam))
    d2 = sp.simplify(sp.diff(massive, lam))
    forged = mut("constant_density_forged")
    ok = (d1 != 0 and sp.simplify(d1 - 4 * I / l ** 4) == 0 and sp.simplify(d2 * l ** 3 - (3 * sp.sqrt(mu ** 2 + s2 / l ** 2) + s2 / (l ** 2 * sp.sqrt(mu ** 2 + s2 / l ** 2)))) == 0)
    if forged:
        ok = ok and sp.diff(const, lam) != 0
    checks.check("E1", ok, "per unit volume the sea's energy is -I/l^4 (massless) or -<sqrt(mu^2 + s^2/l^2)>/l^3 (massive); both change with l at every length, so on this lattice the sea never acts as a constant energy per unit volume")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 60, 101 and 139 as landed on main (the homogeneous kinetic model, the static clock law and the staggered mass with the books' zero of energy), with block 146 placed; it reports what the member's zero mode says about the zero of energy the member sees; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Dirac", "Bergmann", "Lorentz", "Kato", "Rosenblum", "Ruelle", "Amrein", "Georgescu", "Enss", "Lebesgue", "Levinson", "Birman", "Krein", "Schwarz", "Liouville", "Morse", "Infeld", "Hoffmann", "Fierz", "Darwin", "Laue", "Poincare", "Poincaré", "Grommer", "Belinfante", "Rosenfeld", "Lemaitre", "Lemaître", "Robertson", "Hubble", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the walk's spectrum about the books' zero; the massless sea's energy on the 4^3 torus",
    "per_site: executed - the stretched spectra, massless and with the staggered mass",
    "per_mode: executed - each massive mode's sea energy as the lattice stretches",
    "per_block: executed - the zero-mode constraint with the sea: no motion, the bounce and its exact history, the threshold m0 > mu",
    "lattice_wide: uniform content on a closed lattice; block 146's zero-mode constraint on block 60's homogeneous model",
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
    print("scope: the half-filled sea has negative energy relative to the books zero; per unit volume it scales as -I/l^4 or -<sqrt(mu^2 + s^2/l^2)>/l^3, never constant; if the member sees it, a closed lattice with only the sea cannot move, with rest content m0 it bounces at l = I/m0 (massless sea) or needs m0 > mu (massive sea); if the member sees energy above the sea block 146 holds; supervisor derivation, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
