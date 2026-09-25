#!/usr/bin/env python3
"""Exact checks: under one record per site the source of two records is their compressed density - on a chain the compressed
pair generator is two free spinless fermions of the charge band times the coin sequence, so exclusion adds no failure of action
and reaction, and in a uniform gradient the pair's passive mass equals its compressed energy; the additive source over the
original one-record states would miss by an exact factor (a harvest block from two Grok-refereed probes attempts; blocks 54, 55, 78
and 80 as landed supplied; not adopted).

B (T1): the fixed-state source identity on block 78's ring of 6, and its difference from the one-record densities.
C (T2): the chain reduction - every matrix element of the compressed generator in the ordered, gauged basis.
D (T3): the compressed density as the charge band's one-particle trace.
E (T4): the scaling identity of the excluded pair in a uniform gradient, and the additive source's ratio.
Exact rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_UNDER_ONE_RECORD_PER_SITE_THE_SOURCE_IS_THE_COMPRESSED_DENSITY_ON_A_CHAIN_TWO_RECORDS_ARE_TWO_FREE_FERMIONS_OF_THE_CHARGE_BAND_AND_ACTION_EQUALS_REACTION_SURVIVES_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_under_one_record_per_site_the_source_is_the_compressed_density_on_a_chain_two_records_are_two_free_fermions_of_the_charge_band_and_action_equals_reaction_survives_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "A site never carries more than one record; records are permanent.",
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "ledger_density_forged": "B",
    "gauge_forged": "C",
    "charge_trace_forged": "D",
    "scaling_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: a site never carries more than one record (the exclusion P); each site has a domain of local possibilities (the coin); Admissibility is not a dynamics axiom (the walk and the moving records are supplied clauses)")


# ============================================================================================ the reduced walk and two records
CZ, C1 = (Fr(0), Fr(0)), (Fr(1), Fr(0))


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cconj(a):
    return (a[0], -a[1])


def one_body(phi, ring):
    """H_w = phi sigma_3 D phi on modes (x, c), (D psi)(x) = (psi(x+1) - psi(x-1))/(2i); a ring or an open chain."""
    size = len(phi)
    h = {}
    for x in range(size):
        for c in range(2):
            s = 1 if c == 0 else -1
            for step, amp in ((1, (Fr(0), Fr(-1, 2))), (-1, (Fr(0), Fr(1, 2)))):
                y = x + step
                if ring:
                    y %= size
                elif not 0 <= y < size:
                    continue
                v = cmul((Fr(s) * phi[x] * phi[y], Fr(0)), amp)
                h[((x, c), (y, c))] = cadd(h.get(((x, c), (y, c)), CZ), v)
    return h


def apply_one(h, vec):
    out = {}
    for (a, b), v in h.items():
        if b in vec:
            out[a] = cadd(out.get(a, CZ), cmul(v, vec[b]))
    return out


def inner(u, v):
    tot = CZ
    for k, x in u.items():
        if k in v:
            tot = cadd(tot, cmul(cconj(x), v[k]))
    return tot


def pair_state(psi1, psi2, sign):
    """Psi(m, n) = psi1(m) psi2(n) + sign psi2(m) psi1(n), projected off coincident sites (P)."""
    out = {}
    for m, a in psi1.items():
        for n, b in psi2.items():
            if m[0] == n[0]:
                continue
            out[(m, n)] = cadd(out.get((m, n), CZ), cmul(a, b))
            out[(n, m)] = cadd(out.get((n, m), CZ), cmul((Fr(sign), Fr(0)), cmul(a, b)))
    return {k: v for k, v in out.items() if v != CZ}


def apply_two(h, big):
    """P H2 P: H_w on either slot, then drop coincident sites."""
    out = {}
    rows = {}
    for (a, b), v in h.items():
        rows.setdefault(b, []).append((a, v))
    for (m, n), amp in big.items():
        for a, v in rows.get(m, ()):
            if a[0] != n[0]:
                out[(a, n)] = cadd(out.get((a, n), CZ), cmul(v, amp))
        for a, v in rows.get(n, ()):
            if a[0] != m[0]:
                out[(m, a)] = cadd(out.get((m, a), CZ), cmul(v, amp))
    return out


def ring78_states():
    """block 78's ring of 6 (its runner's D1): rates and two orthogonal complex states."""
    size = 6
    phi = [1 + Fr((3 * x * x + x) % 5, 7) for x in range(size)]
    modes = [(x, c) for x in range(size) for c in range(2)]
    u1 = [Fr((x * x + 1) % 4, 3) if c == 0 else Fr((2 * x + 1) % 5, 4) for x, c in modes]
    v1 = [Fr(x % 3, 2) if c == 0 else Fr((x * x) % 3 - 1, 3) for x, c in modes]
    u2r = [Fr((x + 2) % 4, 5) if c == 0 else Fr(1, 2) for x, c in modes]
    v2r = [Fr((x * x + x) % 3, 2) if c == 0 else Fr((3 * x) % 4 - 2, 3) for x, c in modes]
    ip = lambda a, b: sum((p * q for p, q in zip(a, b)), Fr(0))
    n1 = ip(u1, u1) + ip(v1, v1)
    cr, ci = (ip(u1, u2r) + ip(v1, v2r)) / n1, (ip(u1, v2r) - ip(v1, u2r)) / n1
    u2 = [ur - (cr * p - ci * q) for ur, p, q in zip(u2r, u1, v1)]
    v2 = [vr - (cr * q + ci * p) for vr, p, q in zip(v2r, u1, v1)]
    psi1 = {m: (a, b) for m, a, b in zip(modes, u1, v1)}
    psi2 = {m: (a, b) for m, a, b in zip(modes, u2, v2)}
    return phi, psi1, psi2


def pair_energy_and_density(phi, psi1, psi2, sign, ring=True):
    h = one_body(phi, ring)
    big = pair_state(psi1, psi2, sign)
    norm = inner(big, big)[0]
    hb = apply_two(h, big)
    energy = inner(big, hb)[0] / norm
    size = len(phi)
    dens = []
    for x in range(size):
        tot = Fr(0)
        slot1 = {}
        slot2 = {}
        rows = {}
        for (a, b), v in h.items():
            rows.setdefault(b, []).append((a, v))
        for (m, n), amp in big.items():
            for a, v in rows.get(m, ()):
                if a[0] == x and a[0] != n[0]:
                    slot1[(a, n)] = cadd(slot1.get((a, n), CZ), cmul(v, amp))
            for a, v in rows.get(n, ()):
                if a[0] == x and a[0] != m[0]:
                    slot2[(m, a)] = cadd(slot2.get((m, a), CZ), cmul(v, amp))
        tot = (inner(big, slot1)[0] + inner(big, slot2)[0]) / norm
        dens.append(tot)
    return energy, dens


def one_record(phi, psi, ring=True):
    h = one_body(phi, ring)
    hp = apply_one(h, psi)
    norm = inner(psi, psi)[0]
    energy = inner(psi, hp)[0] / norm
    dens = []
    for x in range(len(phi)):
        dens.append(sum((cmul(cconj(psi[(x, c)]), hp.get((x, c), CZ))[0] for c in range(2) if (x, c) in psi), Fr(0)) / norm)
    return energy, dens


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the source of two records under exclusion is the compressed density (block 80's identity, on block 78's ring)."""
    phi, psi1, psi2 = ring78_states()
    e_hc, dens = pair_energy_and_density(phi, psi1, psi2, -1)
    ok_d = True
    for x in range(len(phi)):
        up = [p * (Fr(11, 10) if y == x else 1) for y, p in enumerate(phi)]
        dn = [p * (Fr(9, 10) if y == x else 1) for y, p in enumerate(phi)]
        e_up, _ = pair_energy_and_density(up, psi1, psi2, -1)
        e_dn, _ = pair_energy_and_density(dn, psi1, psi2, -1)
        slope = (e_up - e_dn) / (Fr(2, 10) * phi[x]) * phi[x] / 2
        if mut("ledger_density_forged") and x == 0:
            slope += Fr(1, 1000)
        ok_d = ok_d and slope == dens[x]
    e1, d1 = one_record(phi, psi1)
    e2, d2 = one_record(phi, psi2)
    differs = all(dens[x] != d1[x] + d2[x] for x in range(len(phi)))
    checks.check("B1", ok_d and sum(dens, Fr(0)) == e_hc and e_hc == Fr(12349656, 122046701) and e1 + e2 == Fr(16169964, 134909593) and differs,
                 f"T1: on block 78's ring of 6 (its rates and two orthogonal states), for the antisymmetric pair under exclusion: (phi_x/2) dE/dphi_x (exact, E is linear in each bond factor at fixed state) equals the compressed density at every site, the densities sum to E_hc = {e_hc}, and they differ from the one-record densities e1 + e2 (total {e1 + e2}) at all six sites")


# ============================================================================================ family C
def ordered_basis(size):
    return [((xl, sl), (xr, sr)) for xl in range(size) for xr in range(xl + 1, size) for sl in range(2) for sr in range(2)]


def family_c(checks: Checks) -> None:
    """T2: on a chain, the compressed pair generator is two free spinless fermions of the up-coin hop, times the coin sequence."""
    size = 7
    phi = [Fr(3 + (5 * x * x + 2 * x) % 7, 4) for x in range(size)]
    h = one_body(phi, ring=False)
    up_hop = {}
    for x in range(size):
        for step, amp in ((1, (Fr(0), Fr(-1, 2))), (-1, (Fr(0), Fr(1, 2)))):
            y = x + step
            if 0 <= y < size:
                up_hop[(x, y)] = cmul((phi[x] * phi[y], Fr(0)), amp)
    ok, count = True, 0
    for sign in (-1, 1):
        for (ml, mr) in ordered_basis(size):
            big = {(ml, mr): C1, (mr, ml): (Fr(sign), Fr(0))}
            out = apply_two(h, big)
            for ((a, b), v) in out.items():
                if a[0] > b[0]:
                    continue
                count += 1
                moved_left = a != ml
                src, dst = (ml, a) if moved_left else (mr, b)
                gauge = 1
                for (pos, coin), (pos2, coin2) in ((ml, a), (mr, b)):
                    if coin == 1:
                        gauge *= (-1) ** (pos + pos2)
                want = up_hop.get((dst[0], src[0]), CZ)
                if mut("gauge_forged"):
                    gauge = 1
                keep_coins = a[1] == ml[1] and b[1] == mr[1]
                one_step = (a == ml and abs(b[0] - mr[0]) == 1) or (b == mr and abs(a[0] - ml[0]) == 1)
                ok = ok and keep_coins and one_step and cmul((Fr(gauge), Fr(0)), v) == want
    checks.check("C1", ok and count > 0,
                 f"T2: on an open chain of 7 with generic rational rates, in the ordered basis (x_L < x_R, coins in order) with the gauge (-1)^x on down coins, every nonzero matrix element of P H2 P ({count}, both exchange signs) keeps the coin sequence, moves one record by one site, and equals the up-coin hop times phi_x phi_y: the compressed generator is the free two-fermion hop of the charge band times the identity on the coin sequence, and records never pass")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the compressed density is the charge band's one-particle trace."""
    size = 7
    phi = [Fr(3 + (5 * x * x + 2 * x) % 7, 4) for x in range(size)]
    h = one_body(phi, ring=False)
    up = {(x, y): v for ((x, c), (y, d)), v in h.items() if c == 0}
    amp = {}
    for xl in range(size):
        for xr in range(xl + 1, size):
            amp[(xl, xr)] = (Fr((3 * xl + 5 * xr) % 7 - 3, 5), Fr((xl * xr + 1) % 5 - 2, 3))
    big = {}
    for (xl, xr), v in amp.items():
        g = (-1) ** xr
        big[((xl, 0), (xr, 1))] = cmul((Fr(g), Fr(0)), v)
        big[((xr, 1), (xl, 0))] = cmul((Fr(-g), Fr(0)), v)
    norm = inner(big, big)[0]
    rows = {}
    for (a, b), v in h.items():
        rows.setdefault(b, []).append((a, v))
    dens = []
    for x in range(size):
        slot = {}
        for (m, n), a in big.items():
            for t, v in rows.get(m, ()):
                if t[0] == x and t[0] != n[0]:
                    slot[(t, n)] = cadd(slot.get((t, n), CZ), cmul(v, a))
            for t, v in rows.get(n, ()):
                if t[0] == x and t[0] != m[0]:
                    slot[(m, t)] = cadd(slot.get((m, t), CZ), cmul(v, a))
        dens.append(inner(big, slot)[0] / norm)
    cfull = {}
    for (xl, xr), v in amp.items():
        cfull[(xl, xr)] = v
        cfull[(xr, xl)] = cmul((Fr(-1), Fr(0)), v)
    cnorm = sum((cmul(cconj(v), v)[0] for v in cfull.values()), Fr(0))
    charge = []
    for x in range(size):
        tot = Fr(0)
        for z in range(size):
            if (x, z) not in cfull:
                continue
            for b in (x - 1, x + 1):
                if (b, z) in cfull and (x, b) in up:
                    tot += cmul(cconj(cfull[(x, z)]), cmul(up[(x, b)], cfull[(b, z)]))[0]
        charge.append(2 * tot / cnorm)
    if mut("charge_trace_forged"):
        charge[0] += Fr(1, 1000)
    checks.check("D1", dens == charge,
                 "T3: for a generic antisymmetric charge amplitude on the chain of 7 (coin sector up, down), the compressed density of the record pair equals the charge band's one-particle trace 2 Re sum_z sum_b c(x,z)* h(x,b) c(b,z)/|c|^2 at every site, exactly: under exclusion the source is additive over the charge orbitals")


def scaling_3d():
    """the three-dimensional walk H_w = Phi (sum_a sigma_a S_a) Phi in an open 5x3x3 box, w = 4^(x1): the excluded pair's scaling identity."""
    dims = (5, 3, 3)
    sites = [(x, y, z) for x in range(dims[0]) for y in range(dims[1]) for z in range(dims[2])]
    phi = {s: Fr(2) ** s[0] for s in sites}
    pauli = {0: ((CZ, C1), (C1, CZ)), 1: ((CZ, (Fr(0), Fr(-1))), ((Fr(0), Fr(1)), CZ)), 2: ((C1, CZ), (CZ, (Fr(-1), Fr(0))))}
    h = {}
    for x in sites:
        for a in range(3):
            for step, amp in ((1, (Fr(0), Fr(-1, 2))), (-1, (Fr(0), Fr(1, 2)))):
                y = tuple(x[i] + (step if i == a else 0) for i in range(3))
                if y not in phi:
                    continue
                for c in range(2):
                    for d in range(2):
                        v = cmul(cmul((phi[x] * phi[y], Fr(0)), amp), pauli[a][c][d])
                        if v != CZ:
                            key = ((x, c), (y, d))
                            h[key] = cadd(h.get(key, CZ), v)
    interior = [s for s in sites if 1 <= s[0] <= dims[0] - 3]
    modes = [(s, c) for s in interior for c in range(2)]
    ok, cols = True, 0
    for i, m in enumerate(modes):
        for n in modes[i + 1:]:
            if m[0] == n[0]:
                continue
            big = {(m, n): C1, (n, m): (Fr(-1), Fr(0))}
            sh = lambda md: ((md[0][0] + 1, md[0][1], md[0][2]), md[1])
            moved = {(sh(m), sh(n)): C1, (sh(n), sh(m)): (Fr(-1), Fr(0))}
            lhs = apply_two(h, big)
            lhs_shift = {(sh(a), sh(b)): v for (a, b), v in lhs.items()}
            rhs = apply_two(h, moved)
            factor = 4 if not mut("scaling_forged") else 2
            ok = ok and all(rhs.get(k, CZ) == cmul((Fr(factor), Fr(0)), v) for k, v in lhs_shift.items()) and all(k in lhs_shift for k, v in rhs.items() if v != CZ)
            cols += 1
            if cols >= 400:
                return ok, cols
    return ok, cols


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the pair as one body - the scaling identity in a uniform gradient, and the additive source's mismatch."""
    size = 6
    phi = [Fr(2) ** x for x in range(size)]
    h = one_body(phi, ring=False)
    ok, cols = True, 0
    for (ml, mr) in ordered_basis(size):
        if ml[0] == 0 or mr[0] >= size - 2:
            continue
        big = {(ml, mr): C1, (mr, ml): (Fr(-1), Fr(0))}
        moved = {((ml[0] + 1, ml[1]), (mr[0] + 1, mr[1])): C1, ((mr[0] + 1, mr[1]), (ml[0] + 1, ml[1])): (Fr(-1), Fr(0))}
        lhs = apply_two(h, big)
        lhs_shift = {((a[0] + 1, a[1]), (b[0] + 1, b[1])): v for (a, b), v in lhs.items()}
        rhs = apply_two(h, moved)
        factor = 4 if not mut("scaling_forged") else 2
        ok = ok and all(rhs.get(k, CZ) == cmul((Fr(factor), Fr(0)), v) for k, v in lhs_shift.items()) and all(k in lhs_shift for k, v in rhs.items() if v != CZ)
        cols += 1
    ok3, cols3 = scaling_3d()
    phi78, psi1, psi2 = ring78_states()
    e_hc, _ = pair_energy_and_density(phi78, psi1, psi2, -1)
    e1, _ = one_record(phi78, psi1)
    e2, _ = one_record(phi78, psi2)
    ratio = (e1 + e2) / e_hc
    checks.check("E1", ok and cols > 0 and ok3 and cols3 > 0 and ratio == Fr(3356276805253, 2833481402466),
                 f"T4: on an open chain with w = 4^x ({cols} interior columns) and for the three-dimensional walk sum_a sigma_a S_a in a 5x3x3 box with w = 4^(x1) ({cols3} interior columns), translating both records by one step up the gradient multiplies P H2 P by 4, since every hop carries phi_x phi_y and exclusion is translation invariant (block 54's finite-power identity carried to the excluded pair, in every dimension); so, with block 54's conditional argument, the pair's passive mass is its compressed energy, equal to its active mass (T1): S/E = 1. The additive source e1 + e2 would instead give S/E = E_free/E_hc = {ratio} on block 78's ring")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 55, 78 and 80 as landed on main, with two records under one record per site moving by the reduced walk; it reports what sources the clock field for such a pair and whether exclusion breaks action and reaction; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Jordan", "Belinfante", "Rosenfeld", "Tonks", "Girardeau", "Lieb", "Liniger", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the energies E_hc and E_free on block 78's ring and their ratio, exactly",
    "per_site: executed - the fixed-state source identity at all six sites of block 78's ring; the compressed density against the charge trace at all seven sites of a chain",
    "per_mode: executed - every nonzero matrix element of the compressed generator in the ordered, gauged basis, both exchange signs",
    "per_block: executed - the scaling identity of the excluded pair on every interior column of a chain with w = 4^x and on 400 of the three-dimensional walk in a 5x3x3 box",
    "lattice_wide: T1 and T4 in every dimension (T4 checked on a chain and for the three-dimensional walk); T2-T3 on every chain (the reduction needs records that cannot pass, so not in two or three dimensions); T4's passive mass through block 54's conditional argument; the walk and the records are supplied",
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
    print("scope: two records under one record per site - the source is the compressed density; on a chain the compressed pair is two free fermions of the charge band times the coin sequence, so exclusion adds no failure of action and reaction; the additive source over the original states misses by an exact factor; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
