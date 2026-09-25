#!/usr/bin/env python3
"""Exact checks: the hard-core sea on a ring - under one record per site the records of block 78's reduced walk are one
spinless band with a twisted wrap bond, both exchange signs share one twist set, the sea is half filled, and its volume
term and clock stiffness are exactly half the free sea's, with the same sign: c0 = -1/pi, kappa = 1/(6 pi) (a harvest
block from a Grok-refereed probes attempt; blocks 54, 76 and 78 as landed; not adopted).

B (T1): packing, tracelessness and the chessboard.
C (T2): the reduction to one twisted spinless band, entry by entry.
D (T3): the twist sets of both exchange signs.
E (T4): the sea's energy, its volume term and its clock stiffness in closed form.
Exact arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_THE_HARD_CORE_SEA_ON_A_RING_IS_ONE_TWISTED_BAND_HALF_FILLED_WITH_HALF_THE_FREE_SEAS_VOLUME_TERM_AND_CLOCK_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_IS_AN_INTERACTION_NOT_A_FREE_SEA_TWO_RECORDS_UNDER_EXCLUSION_AGAINST_FREE_ANTISYMMETRIC_AND_SYMMETRIC_PAIRS_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_A_CHESSBOARD_OF_CLOCKS_IS_INVISIBLE_THE_SEA_INDUCES_A_CLOCK_STIFFNESS_NOT_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-22.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_hard_core_sea_on_a_ring_is_one_twisted_band_half_filled_with_half_the_free_seas_volume_term_and_clock_stiffness_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "A site never carries more than one record; records are permanent.",
    "Records form.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "packing_forged": "B",
    "wrap_sign_forged": "C",
    "twist_set_forged": "D",
    "stiffness_forged": "E",
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
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: one record per site (the hard-core compression; records never pass on a ring); records form (which states a sea fills is not given); Admissibility is not a dynamics axiom (the walk, the rates and the composition are supplied)")


# ============================================================================================ block 78's reduced walk, many records on a ring
def ring_hard_core(ll, nrec, weights, sign):
    """hard-core N-record generator of the clocked reduced walk sigma_3 S on a ring, as a dict {(new_cfg, old_cfg): (re, im)};
    a configuration is a tuple of (site, coin) sorted by site, coin +1 (up) or -1 (down); bond (x, x+1) carries weight
    weights[x]; the record at x+1 hops to x with amplitude (-i/2) s w, the record at x to x+1 with (+i/2) s w;
    sign = -1: fermionic order sign over modes 2 site + (0 up, 1 down); sign = +1: no sign."""
    out = {}
    for occ in combinations(range(ll), nrec):
        for coins in product((1, -1), repeat=nrec):
            cfg = tuple(zip(occ, coins))
            sites = set(occ)
            modes = sorted(2 * x + (0 if c == 1 else 1) for x, c in cfg)
            for r, (x, c) in enumerate(cfg):
                for step in (1, -1):
                    y = (x + step) % ll
                    if y in sites:
                        continue
                    bond = x if step == 1 else y
                    amp_im = Fraction(c, 2) * weights[bond] * (1 if step == 1 else -1)
                    m_old = 2 * x + (0 if c == 1 else 1)
                    m_new = 2 * y + (0 if c == 1 else 1)
                    rest = [m for m in modes if m != m_old]
                    sg = 1
                    if sign == -1:
                        sg = (-1) ** (sum(1 for m in modes if m < m_old) + sum(1 for m in rest if m < m_new))
                    new = tuple(sorted([(z, d) for (z, d) in cfg if z != x] + [(y, c)]))
                    out[(new, cfg)] = (Fraction(0), sg * amp_im)
    return out


def gauge(cfg):
    g = 1
    for (x, c) in cfg:
        if c == -1:
            g *= (-1) ** x
    return g


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: at one record per site nothing moves; below it the generator is traceless and nonzero; a chessboard of clocks is invisible."""
    ok = True
    w6 = [Fraction(k + 2, k + 3) for k in range(6)]
    for sign in (-1, 1):
        full = ring_hard_core(6, 6, w6, sign)
        half = ring_hard_core(6, 3, w6, sign)
        ok = ok and not full and half and all(k[0] != k[1] for k in half)
        herm = all(half.get((o, n), (0, 0)) == (v[0], -v[1]) for (n, o), v in half.items())
        ok = ok and herm
    cc = Fraction(3, 2)
    phi = [cc if x % 2 == 0 else 1 / cc for x in range(8)]
    ok_chess = all(phi[x] * phi[(x + 1) % 8] == 1 for x in range(8))
    ok_odd = not all(([cc if x % 2 == 0 else 1 / cc for x in range(7)][x] * [cc if x % 2 == 0 else 1 / cc for x in range(7)][(x + 1) % 7]) == 1 for x in range(7))
    if mut("packing_forged"):
        ok = ok and bool(ring_hard_core(6, 6, w6, 1) or {(0, 0): (0, 1)}) is False
    checks.check("B1", ok and ok_chess and ok_odd,
                 "T1: on the ring of six with generic rational bond weights, six records give the zero generator (every hop lands on an occupied site) and three give a nonzero, traceless (no diagonal entry), hermitian one, for both exchange signs, so the energy below one record per site is negative; the generator depends on the rates only through the bond products, which a chessboard phi = c^(+-1) makes exactly 1 on an even ring (and cannot on an odd one)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: on a ring the records are one spinless band whose wrap bond rotates the coin sequence."""
    ok = True
    count = 0
    for ll, nrec in ((8, 4), (7, 3), (8, 6)):
        wts = [Fraction(2 * k + 3, k + 5) for k in range(ll)]
        for sign in (-1, 1):
            gen = ring_hard_core(ll, nrec, wts, sign)
            for (new, old), val in gen.items():
                count += 1
                pos_o = [x for x, _ in old]
                pos_n = [x for x, _ in new]
                seq_o = [c for _, c in old]
                seq_n = [c for _, c in new]
                moved = [x for x in pos_o if x not in pos_n][0]
                target = [x for x in pos_n if x not in pos_o][0]
                wrap = {moved, target} == {0, ll - 1}
                step = 1 if (target - moved) % ll == 1 else -1
                bond = moved if step == 1 else target
                up_amp = Fraction(1, 2) * wts[bond] * (1 if step == 1 else -1)
                gauged = gauge(new) * val[1] * gauge(old)
                if not wrap:
                    want, want_seq = up_amp, seq_o
                else:
                    c_moved = [c for x, c in old if x == moved][0]
                    spinless = up_amp * (-1) ** (nrec - 1)
                    factor = 1 if sign == -1 else (-1) ** (nrec - 1)
                    if ll % 2 == 1 and c_moved == -1:
                        factor = -factor
                    want = spinless * factor
                    want_seq = [seq_o[-1]] + seq_o[:-1] if moved == ll - 1 else seq_o[1:] + [seq_o[0]]
                if mut("wrap_sign_forged") and wrap:
                    want = -want
                ok = ok and val[0] == 0 and gauged == want and seq_n == want_seq
    checks.check("C1", ok,
                 f"T2: on the rings 8 (4 and 6 records) and 7 (3 records), with generic rational bond weights and both exchange signs, every one of the {count} nonzero entries of the hard-core generator, after the gauge g = prod over down coins of (-1)^x, equals the up-coin spinless hop; a hop across the wrap bond also rotates the coin sequence and carries (-1)^(N-1) times the stated factor (fermions 1, bosons (-1)^(N-1), times -1 for a down coin on an odd ring): the records are one spinless band with the signed rotation R on the wrap bond")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: both exchange signs have one twist set."""
    ok = True
    for ll, nrec in ((8, 4), (8, 6), (7, 3), (7, 6)):
        sets = []
        for sign in (-1, 1):
            seen = set()
            roots = set()
            for seq in product((1, -1), repeat=nrec):
                if seq in seen:
                    continue
                orbit, cur, sgn = [], list(seq), 1
                while True:
                    orbit.append(tuple(cur))
                    moved = cur[-1]
                    f = 1 if sign == -1 else (-1) ** (nrec - 1)
                    if ll % 2 == 1 and moved == -1:
                        f = -f
                    sgn *= f
                    cur = [cur[-1]] + cur[:-1]
                    if tuple(cur) == seq:
                        break
                seen.update(orbit)
                per = len(orbit)
                half = Fraction(1, 2) if sgn == -1 else Fraction(0)
                for j in range(per):
                    roots.add((Fraction(j) + half) / per % 1)
            sets.append(roots)
        want = {Fraction(j, nrec) for j in range(nrec)} if ll % 2 == 0 else {Fraction(j, 2 * nrec) for j in range(2 * nrec)}
        if mut("twist_set_forged"):
            want = {Fraction(j, nrec) for j in range(nrec)}
        ok = ok and sets[0] == sets[1] == want
    checks.check("D1", ok,
                 "T3: counting the orbits of the signed rotation R on coin sequences, with their sign products, the twists (as fractions of a turn) are the same set for fermions and bosons: all N-th roots of unity on the even ring of 8 (N = 4, 6) and all 2N-th roots on the odd ring of 7 (N = 3, 6); so for every rate field both exchange signs have the same ground energy and the same second variation wherever it exists")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the half-filled sea, its volume term and its clock stiffness: exactly half the free sea's."""
    aa, dd = sp.symbols("a d", real=True)
    ok_window = True
    for mm in range(1, 9):
        lhs = sum(sp.sin(aa + j * dd) for j in range(mm))
        rhs = sp.sin(aa + (mm - 1) * dd / 2) * sp.sin(mm * dd / 2) / sp.sin(dd / 2)
        diff = sp.expand(sp.expand_trig(((lhs - rhs) * sp.sin(dd / 2)).rewrite(sp.exp)))
        ok_window = ok_window and sp.simplify(diff) == 0
    ok_sea = True
    for ll in (4, 8, 12, 16):
        neg = [sp.sin((2 * sp.pi * m + sp.pi) / ll) for m in range(ll)]
        tot = sum(v for v in neg if v.is_negative)
        ok_sea = ok_sea and sp.minimal_polynomial(tot + 1 / sp.sin(sp.pi / ll), sp.Symbol("z")) == sp.Symbol("z")
    k, q, t = sp.symbols("k q t", real=True)
    held = sp.integrate(sp.sin(k) * sp.cos(q / 2) ** 2 / 4, (k, -sp.pi, 0)) / (2 * sp.pi)
    ok_held = sp.simplify(held + sp.cos(q / 2) ** 2 / (4 * sp.pi)) == 0
    prim = sp.atanh(sp.sin(t)) - sp.sin(t)
    ok_prim = sp.simplify(sp.diff(prim, t) - sp.sin(t) ** 2 / sp.cos(t)) == 0
    relax = -(sp.cos(q / 2) ** 2 / (4 * sp.pi * sp.sin(q / 2))) * (prim.subs(t, q / 2) - prim.subs(t, -q / 2)) / 2
    total = sp.simplify(held + relax)
    closed = -sp.cos(q / 2) ** 2 * sp.atanh(sp.sin(q / 2)) / (4 * sp.pi * sp.sin(q / 2))
    ok_closed = sp.simplify(total - closed) == 0
    ser = sp.series(closed, q, 0, 4).removeO()
    want_c0, want_kappa = -1 / sp.pi, 1 / (6 * sp.pi)
    if mut("stiffness_forged"):
        want_kappa = 1 / (3 * sp.pi)
    ok_ser = sp.simplify(ser - (want_c0 / 4 + want_kappa / 4 * q ** 2)) == 0
    ok_free = sp.simplify(2 * want_c0 + 2 / sp.pi) == 0 and sp.simplify(2 * want_kappa - 1 / (3 * sp.pi)) == 0
    vert = sp.expand(sp.cos(q / 2) * sp.sin(k + q / 2) / 2)
    vertex_from_bonds = sp.cos(q/2) * (-sp.I*sp.exp(sp.I*(k+q/2)) + sp.I*sp.exp(-sp.I*(k+q/2))) / 4
    vertex_ok = sp.simplify(sp.expand_complex(vertex_from_bonds)-vert)==0
    ediff = sp.simplify(sp.sin(k) - sp.sin(k + q) + 2 * sp.cos(k + q / 2) * sp.sin(q / 2)) == 0
    checks.check("E1", ok_window and ok_sea and ok_held and ok_prim and ok_closed and ok_ser and ok_free and ediff and vertex_ok,
                 "T4: M consecutive terms sin(a + j d) sum to sin(a + (M-1) d/2) sin(M d/2)/sin(d/2) (symbolic, M = 1..8), so a window of M grid points 2 pi j/L sums to sin(centre) sin(pi M/L)/sin(pi/L), so with the twist pi the half-filled band's negative window gives the sea -1/sin(pi/L) (exact, L = 4, 8, 12, 16; the free sea is -2 cot(pi/L)); for the rate mode u = eps cos(qx) the held term is -cos^2(q/2)/(4 pi) and the relaxation integral uses int sin^2 t/cos t = ln(sec t + tan t) - sin t, giving Pi(q) = -cos^2(q/2) ln(sec(q/2) + tan(q/2))/(4 pi sin(q/2)) = -1/(4 pi) + q^2/(24 pi) + ...: volume term c0 = -1/pi and clock stiffness kappa = 1/(6 pi), exactly half the free sea's -2/pi and 1/(3 pi), with the same sign")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 76 and 78 as landed on main (the clocked walk, the sea's energy as a function of the rates, and the reduced ring walk with its hard-core compression); it reports the exact energy of the hard-core sea on a ring and its response to the rates; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Jordan", "Wigner", "Lanczos", "Luttinger", "Tomonaga", "Lieb", "Mattis", "Sakharov", "Fermi", "Bose", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - every captured nonzero entry of the hard-core generator on rings 8 and 7, both exchange signs, against the twisted spinless band",
    "per_site: executed - packing and tracelessness on the ring of six; the chessboard's bond products",
    "per_mode: executed - the twist sets of both exchange signs by orbit counting on rings 8 and 7",
    "per_block: executed - the window identity; the half-filled sea at L = 4, 8, 12, 16; the held and relaxation integrals and the series of the closed form",
    "lattice_wide: T1 on every connected lattice; T2-T3 on L>=3 rings; T4 small-amplitude first on uniform 4-divisible rings, then long rings at fixed 0<|q|<pi, then small q; two and three dimensions not treated",
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
    print('scope: Ring gauge/exterior-power reduction, twist set and ordered-limit stiffness; no higher-dimensional or uniform-gap claim. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
