#!/usr/bin/env python3
"""Exact checks: one record per site keeps the books only at leading order - for two records of block 54's walk under
block 78's compression, the total energy current is kept on a line and for free pairs in every dimension, but not in two or
three dimensions; the member's identity with a local stress needs it kept, so with block 121's compressed source (or block
135's average, which has the same first moment) no finite-range zero-vacuum stress with the same energy first moment gives this identity for all two-record states; conditional small-offset free-channel changes have a cubic expansion; no collision dynamics is proved (the supervisor's own derivation; blocks 54, 78 and 121 as landed or placed; blocks 135 and 136 placed; not adopted).

B (T1): the current is not kept in 2D and 3D under exclusion (open lattice and the 5 x 5 torus).
C (T2): where it is kept.
D (T3): the member's identity keeps the total current; the average keeps first moments.
E (T4): slow records.
Exact rational and Gaussian-rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_KEEPS_THE_BOOKS_ONLY_AT_LEADING_ORDER_TWO_EXCLUDED_RECORDS_LOSE_THEIR_ENERGY_CURRENT_IN_TWO_AND_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_IS_AN_INTERACTION_NOT_A_FREE_SEA_TWO_RECORDS_UNDER_EXCLUSION_AGAINST_FREE_ANTISYMMETRIC_AND_SYMMETRIC_PAIRS_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/ADMISSIBILITY_RULE_UNDER_ONE_RECORD_PER_SITE_THE_SOURCE_IS_THE_COMPRESSED_DENSITY_ON_A_CHAIN_TWO_RECORDS_ARE_TWO_FREE_FERMIONS_OF_THE_CHARGE_BAND_AND_ACTION_EQUALS_REACTION_SURVIVES_BOUNDED_THEOREM_NOTE_2026-09-24.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_one_record_per_site_keeps_the_books_only_at_leading_order_two_excluded_records_lose_their_energy_current_in_two_and_three_dimensions_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "exclusion_dropped": "B",
    "line_excluded_forged": "C",
    "first_moment_forged": "D",
    "cubic_order_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its exclusion, the currents and their placements, the member and the source link are supplied; the memo does not define a time metric)")


# ============================================================================================ two records, exact over Q(i)
GZ = (Fr(0), Fr(0))


def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


SIGC = ({(0, 1): (Fr(1), Fr(0)), (1, 0): (Fr(1), Fr(0))}, {(0, 1): (Fr(0), Fr(-1)), (1, 0): (Fr(0), Fr(1))}, {(0, 0): (Fr(1), Fr(0)), (1, 1): (Fr(-1), Fr(0))})


class Pair:
    """two records of block 54's walk H = sum_{a < dim} sigma_a S_a on Z^dim (or the torus Z_L^dim), as dict vectors over the
    (anti)symmetric pair basis; exclusion removes every state with both records on one site (block 78's compression)."""

    def __init__(self, dim, sign, excl, L=None):
        self.dim, self.sign, self.excl, self.L = dim, sign, excl, L

    def wrap(self, y):
        return tuple(v % self.L for v in y) if self.L else tuple(y)

    def h1(self, s):
        x, c = s
        out = []
        for a in range(self.dim):
            for sg in (1, -1):
                y = list(x)
                y[a] -= sg
                y = self.wrap(y)
                for (d, c2), v in SIGC[a].items():
                    if c2 == c:
                        out.append(((y, d), gmul((Fr(0), Fr(-sg, 2)), v)))
        return out

    def canon(self, s1, s2):
        if s1 == s2:
            return None, None
        if s1 < s2:
            return (s1, s2), (Fr(1), Fr(0))
        return (s2, s1), (Fr(self.sign), Fr(0))

    @staticmethod
    def vadd(v, k, a):
        nv = gadd(v.get(k, GZ), a)
        if nv == GZ:
            v.pop(k, None)
        else:
            v[k] = nv

    def proj(self, v):
        if not self.excl:
            return v
        return {k: a for k, a in v.items() if k[0][0] != k[1][0]}

    def hop(self, v, weight=None):
        """H_f = H x 1 + 1 x H, or with weight(t, s) the dipole D = sum over records of (X H + H X)/2"""
        out = {}
        for (s1, s2), a in v.items():
            for t, amp in self.h1(s1):
                k, sg = self.canon(t, s2)
                if k:
                    w = amp if weight is None else gmul(amp, weight(t, s1))
                    self.vadd(out, k, gmul(gmul(a, w), sg))
            for t, amp in self.h1(s2):
                k, sg = self.canon(s1, t)
                if k:
                    w = amp if weight is None else gmul(amp, weight(t, s2))
                    self.vadd(out, k, gmul(gmul(a, w), sg))
        return out

    def H2(self, v):
        return self.proj(self.hop(self.proj(v)))

    def D2(self, v, comp):
        return self.proj(self.hop(self.proj(v), lambda t, s: (Fr(t[0][comp] + s[0][comp], 2), Fr(0))))

    @staticmethod
    def sub(a, b):
        out = dict(a)
        for k, x in b.items():
            Pair.vadd(out, k, (-x[0], -x[1]))
        return out

    def J(self, v, comp):
        """the total energy current i[H2, D2] (open lattice)"""
        r = self.sub(self.H2(self.D2(v, comp)), self.D2(self.H2(v), comp))
        return {k: gmul(x, (Fr(0), Fr(1))) for k, x in r.items()}

    def dJ(self, v, comp):
        """[H2, J] v"""
        return self.sub(self.H2(self.J(v, comp)), self.J(self.H2(v), comp))


def adjacent_pairs(p):
    o = tuple([0] * p.dim)
    e1 = tuple([1] + [0] * (p.dim - 1))
    out = []
    for c1 in (0, 1):
        for c2 in (0, 1):
            k, sg = p.canon((o, c1), (e1, c2))
            out.append({k: sg})
    return out


def current_kept(dim, sign, excl):
    p = Pair(dim, sign, excl)
    return all(not p.dJ(v, comp) for v in adjacent_pairs(p) for comp in range(dim))


def torus_current_kept(L, dim, sign, excl, every=False):
    """on the L^dim torus: build J = (1/2) sum_{x,y} (x - y)_min i[h_y, h_x] from the compressed densities h_x and test [H2, J] on the pair basis"""
    p = Pair(dim, sign, excl, L)
    sites = list(product(range(L), repeat=dim))
    states = [(x, c) for x in sites for c in (0, 1)]
    basis = []
    for i in range(len(states)):
        for j in range(i + 1, len(states)):
            if excl and states[i][0] == states[j][0]:
                continue
            basis.append((states[i], states[j]))

    def e_site(v, x):
        """h_x = P(e_x x 1 + 1 x e_x)P, e_x = (Pi_x H + H Pi_x)/2"""
        pv = p.proj(v)
        a = {k: amp for k, amp in pv.items()}
        out = {}
        # H then project on x (Pi_x H) and project on x then H (H Pi_x), for each record
        for (s1, s2), amp in a.items():
            for slot in (0, 1):
                s = (s1, s2)[slot]
                other = (s1, s2)[1 - slot]
                for t, hv in p.h1(s):
                    k, sg = p.canon(t, other) if slot == 0 else p.canon(other, t)
                    if not k:
                        continue
                    fac = Fr(int(t[0] == x) + int(s[0] == x), 2)
                    if fac:
                        Pair.vadd(out, k, gmul(gmul(amp, hv), gmul(sg, (fac, Fr(0)))))
        return p.proj(out)
    offsets = [d for d in product(range(-2, 3), repeat=dim) if any(d)]
    kept = True
    for bv in (basis if every else basis[:: max(1, len(basis) // 12)]):
        v = {bv: (Fr(1), Fr(0))}
        for comp in range(dim):
            def Jv(w):
                out = {}
                for x in sites:
                    hx = e_site(w, x)
                    for d in offsets:
                        if d[comp] == 0:
                            continue
                        y = tuple((x[k] + d[k]) % L for k in range(dim))
                        term = Pair.sub(e_site(hx, y), e_site(e_site(w, y), x))
                        for kk, val in term.items():
                            Pair.vadd(out, kk, gmul(val, (Fr(0), Fr(-d[comp], 2))))
                return out
            r = Pair.sub(p.H2(Jv(v)), Jv(p.H2(v)))
            if r:
                kept = False
                break
        if not kept:
            break
    return kept


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: under one record per site the total energy current of two records is not kept in 2D and 3D."""
    excl = not mut("exclusion_dropped")
    broken = []
    for dim in (2, 3):
        for sign in (-1, 1):
            broken.append(not current_kept(dim, sign, excl))
    torus_broken = [not torus_current_kept(5, 2, sign, excl) for sign in (-1, 1)]
    checks.check("B1", all(broken) and all(torus_broken),
                 "T1: for two records of block 54's walk under one record per site (block 78's compression), both exchange signs: on Z^2 and Z^3, [H2, J] v != 0 for adjacent pairs, where J = i[H2, D2] is the total energy current of the compressed densities (exact over Q(i), open lattice); on the 5 x 5 torus, with J built from the site densities by minimal image, the same holds")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: where the books hold - free pairs in every dimension, excluded pairs on a line and on a ring."""
    free_kept = all(current_kept(dim, -1, False) for dim in (1, 2, 3))
    line_kept = all(current_kept(1, sign, True) for sign in (-1, 1))
    if mut("line_excluded_forged"):
        line_kept = not line_kept
    ring_kept = all(torus_current_kept(7, 1, sign, True, every=True) for sign in (-1, 1))
    free_torus = torus_current_kept(5, 2, -1, False)
    checks.check("C1", free_kept and line_kept and ring_kept and free_torus,
                 "T2: the total energy current is kept for free antisymmetric pairs on Z, Z^2 and Z^3 (and on the 5 x 5 torus), where two records may share a site with opposite coins; and for excluded pairs of both signs on the line and on the ring of 7 sites (every basis state)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the member's identity with a local stress keeps the total current; placements with the same first moment."""
    t = sp.symbols("t")
    # sum_x x_k (dbar_i dbar_j Theta_ij)(x) = 0 for any finitely supported Theta: exact on a random rational Theta in Z^3
    pts = list(product(range(-2, 3), repeat=3))
    theta = {}
    for n, x in enumerate(pts):
        for i in range(3):
            for j in range(3):
                theta[(x, i, j)] = Fr((7 * n + 3 * i + 5 * j) % 11 - 5, 1 + (n + i + j) % 4)

    def th(x, i, j):
        return theta.get((x, i, j), Fr(0))

    def dd(x):
        tot = Fr(0)
        for i in range(3):
            for j in range(3):
                xi = tuple(x[k] - (1 if k == i else 0) for k in range(3))
                xj = tuple(x[k] - (1 if k == j else 0) for k in range(3))
                xij = tuple(xi[k] - (1 if k == j else 0) for k in range(3))
                tot += th(x, i, j) - th(xi, i, j) - th(xj, i, j) + th(xij, i, j)
        return tot
    box = list(product(range(-4, 5), repeat=3))
    moments = [sum(x[k] * dd(x) for x in box) for k in range(3)]
    ok_moment = all(m == 0 for m in moments) and any(dd(x) != 0 for x in box)
    # the body-diagonal average keeps the first moment: sum_x x (C1C2C3 f)(x) = sum_x x f(x)
    f = {x: Fr((3 * sum(x) + x[0] * x[1] + 5) % 7 - 3, 2) for x in pts}
    shifts = list(product((1, -1), repeat=3))
    if mut("first_moment_forged"):
        shifts = [s for s in shifts if s[0] == 1] * 2
    favg = {}
    for x, val in f.items():
        for s in shifts:
            y = tuple(x[k] + s[k] for k in range(3))
            favg[y] = favg.get(y, Fr(0)) + val / 8
    ok_avg = all(sum(y[k] * v for y, v in favg.items()) == sum(x[k] * v for x, v in f.items()) for k in range(3))
    checks.check("D1", ok_moment and ok_avg,
                 "T3: for any finitely supported stress, sum_x x_k sum_ij dbar_i dbar_j Theta_ij (x) = 0 (exact on a rational Theta on 5^3), so the member's identity e_u'' = sum dbar dbar Theta forces the total current d/dt sum_x x e_u(x) to be kept; the body-diagonal average keeps every first moment, so block 121's compressed source and block 135's average carry the same total current: with either, T1 excludes the stated finite-range number-conserving zero-vacuum stress class with this first moment")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: slow records keep the books at leading order: collisions change the two-step momentum by O(kappa^3)."""
    kap = sp.symbols("kappa", real=True)
    j_smooth = sp.sin(2 * kap) / 2
    j_refl = sp.sin(2 * (sp.pi + kap)) / 2
    order = 3 if not mut("cubic_order_forged") else 2
    ser = sp.series(j_smooth - kap, kap, 0, order + 2).removeO()
    ok_series = sp.expand(ser + sp.Rational(2, 3) * kap ** 3) == 0 if order == 3 else sp.expand(ser) == 0
    ok_species = sp.simplify(j_refl - j_smooth) == 0
    # a collision keeps the crystal momentum sum k (translation), so the change of the total two-step momentum is the change of sum (j(k) - k)
    k1, k2, q1, q2 = sp.symbols("k1 k2 q1 q2", real=True)
    change = (j_smooth.subs(kap, q1) + j_smooth.subs(kap, q2)) - (j_smooth.subs(kap, k1) + j_smooth.subs(kap, k2))
    tt = sp.symbols("tau", positive=True)
    scaled = change.subs({q2: k1 + k2 - q1}).subs({k1: tt, k2: 2 * tt, q1: 3 * tt})
    lead = sp.series(scaled, tt, 0, 4).removeO()
    ok_scale = sp.expand(lead - sp.Rational(-2, 3) * ((3 * tt) ** 3 + (0 * tt) ** 3 - tt ** 3 - (2 * tt) ** 3)) == 0
    checks.check("E1", ok_series and ok_species and ok_scale,
                 "T4: free one-record j(k)=sin(2k)/2 has expansion k-2k^3/3+O(k^5) and period pi. For assumed free incoming/outgoing channels all within epsilon < pi/4 of corners and equal total crystal momentum, the offset sums agree and current changes have the stated cubic expansion. The tested tuple is only kinematic: no scattering existence, energy-conserving collision, or bound during interaction is established.")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54 and 78 as landed on main (the walk and one record per site), with blocks 121, 135 and 136 placed; it reports whether two records under exclusion keep the books that the member's identity needs; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - [H2, J] on adjacent pairs over Q(i), open Z, Z^2, Z^3, both exchange signs, with and without exclusion",
    "per_site: executed - the 5 x 5 torus from site densities by minimal image; the ring of 7 sites on every basis state",
    "per_mode: executed - the first moment of a double divergence of a rational stress on 5^3; the body-diagonal average's first moments",
    "per_block: executed - the two-step current's series and species blindness; the third-order change under a kept crystal momentum",
    "lattice_wide: exact for two records; many records and other placements open; the walk, exclusion, member and link supplied",
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
    print('scope: Exact excluded-pair current nonconservation; conditional free-channel expansion is not a scattering theorem. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
