#!/usr/bin/env python3
"""Exact checks: forming one record keeps the ledger only at a price - a feasible price is site-independent when g_yy is constant, the seven-site star's price does not see the walls, and a source in two places separates the two readings of what
sources the clock field (a harvest block from two Grok-refereed probes attempts; blocks 55, 56 and 58 as landed supplied; not
adopted).

B (T1): the static ledger of a moving amplitude is sum e phi; the price Lambda/(1 - k Lambda g_yy); the weak-field price.
C (T2): the price depends on the formation site in a held box; a specified low-self-potential target gives a lighter record in the executed example.
D (T3): the seven-site star is a point charge off its centre and its price does not see the walls; the ball and the cross do.
E (T4): a source in two places: the first-order kicks under the two readings.
Exact rational and symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_FORMING_ONE_RECORD_KEEPS_THE_LEDGER_ONLY_AT_A_PRICE_ONE_PRICE_SERVES_EVERY_SITE_ONLY_WITH_THE_AMBIENT_AT_INFINITY_AND_A_SOURCE_IN_TWO_PLACES_SEPARATES_THE_READINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_WHAT_A_FORMATION_EVENT_DOES_TO_THE_LEDGER_AND_TO_THE_FAR_FIELD_THE_MONOPOLE_NEVER_JUMPS_THE_DIPOLE_DOES_BOUNDED_THEOREM_NOTE_2026-09-21.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_forming_one_record_keeps_the_ledger_only_at_a_price_one_price_serves_every_site_only_with_the_ambient_at_infinity_and_a_source_in_two_places_separates_the_readings_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "Records form.",
    "A state is a configuration of records.",
    "Its domain is a supplied condition, and at every state where the condition holds it gives exactly one answer.",
    "source/action and physical-observable identification",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "moving_ledger_forged": "B",
    "site_blind_price_in_box": "C",
    "star_price_forged": "D",
    "unformed_source_kick_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: records form; a state is a configuration of records; a law gives one answer at every state of its supplied condition; source/action lies outside the axioms; Admissibility is not a dynamics axiom (the clock law, the amplitude and the formation event are supplied clauses)")


# ============================================================================================ lattice machinery
DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
ORIGIN = (0, 0, 0)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def interior(h):
    """interior sites of the box of side 2h + 1 centred at the origin; its boundary layer |coordinate| = h is the held wall."""
    r = range(-h + 1, h)
    return [(x, y, z) for x in r for y in r for z in r]


def inside(s, h):
    return all(abs(c) <= h - 1 for c in s)


def act(el, s):
    p, sg = el
    return (sg[0] * s[p[0]], sg[1] * s[p[1]], sg[2] * s[p[2]])


def group_full():
    return [(p, sg) for p in permutations(range(3)) for sg in product((1, -1), repeat=3)]


def group_fixing(*pts):
    return [el for el in group_full() if all(act(el, pt) == pt for pt in pts)]


def solve_sparse(rows, rhs_list):
    """exact Gaussian elimination on sparse rows (dicts col -> Fraction); several right-hand sides."""
    n = len(rows)
    a = [dict(r) for r in rows]
    b = [list(col) for col in rhs_list]
    for k in range(n):
        piv = next(i for i in range(k, n) if a[i].get(k, 0) != 0)
        if piv != k:
            a[k], a[piv] = a[piv], a[k]
            for col in b:
                col[k], col[piv] = col[piv], col[k]
        pk = a[k][k]
        for i in range(k + 1, n):
            f = a[i].get(k, 0)
            if f == 0:
                continue
            f = f / pk
            for j, v in a[k].items():
                if j < k:
                    continue
                nv = a[i].get(j, 0) - f * v
                if nv == 0:
                    a[i].pop(j, None)
                else:
                    a[i][j] = nv
            for col in b:
                col[i] = col[i] - f * col[k]
    out = []
    for col in b:
        x = [Fr(0)] * n
        for i in range(n - 1, -1, -1):
            s = col[i]
            for j, v in a[i].items():
                if j > i:
                    s -= v * x[j]
            x[i] = s / a[i][i]
        out.append(x)
    return out


def reduced_solve(h, group, diag, srcs):
    """((1 - A) + D) psi = s inside, psi = 0 on the wall, for group-invariant diagonal D and sources, on the orbit space."""
    sites = interior(h)
    rep = {s: min(act(el, s) for el in group) for s in sites}
    reps = sorted(set(rep.values()))
    idx = {r: i for i, r in enumerate(reps)}
    rows = []
    for r in reps:
        row = {idx[r]: Fr(1) + diag.get(r, Fr(0))}
        for d in DIRS:
            y = add(r, d)
            if inside(y, h):
                j = idx[rep[y]]
                row[j] = row.get(j, Fr(0)) - Fr(1, 6)
        rows.append({j: v for j, v in row.items() if v != 0})
    sols = solve_sparse(rows, [[src.get(r, Fr(0)) for r in reps] for src in srcs])
    return [{s: x[idx[rep[s]]] for s in sites} for x in sols]


def group_preserving(src):
    return [el for el in group_full() if all(src.get(act(el, s)) == v for s, v in src.items())]


def green(h, y):
    return reduced_solve(h, group_fixing(y), {}, [{y: Fr(1)}])[0]


def ledger_rest(h, masses, k, group):
    """bodies at rest: ((1 - A) + k diag m) psi = k m; the static ledger sum m phi (block 56), phi = 1 - psi."""
    psi = reduced_solve(h, group, {s: k * m for s, m in masses.items()}, [{s: k * m for s, m in masses.items()}])[0]
    return sum((m * (1 - psi[s]) for s, m in masses.items()), Fr(0)), psi


def price(lam, k, gyy):
    return lam / (1 - k * lam * gyy)


def dec(q, n=6):
    """a truncated decimal string of a rational, by integer arithmetic."""
    sign = "-" if q < 0 else ""
    q = abs(q)
    whole = q.numerator // q.denominator
    frac = ((q - whole) * 10 ** n).numerator // ((q - whole) * 10 ** n).denominator
    return f"{sign}{whole}.{str(frac).zfill(n)}"


# ============================================================================================ family B
def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


C0, C1, CI = (Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(0), Fr(1))
PAULI = (((C0, C1), (C1, C0)), ((C0, (Fr(0), Fr(-1))), (CI, C0)), ((C1, C0), (C0, (Fr(-1), Fr(0)))))


def hblock(x, y, mu):
    """the witness walk: H_xx = mu sigma_3, H_{x, x +- e_j} = -+ (i/2) sigma_j (Hermitian)."""
    d = (y[0] - x[0], y[1] - x[1], y[2] - x[2])
    if d == ORIGIN:
        return [[cmul((mu, Fr(0)), PAULI[2][i][j]) for j in range(2)] for i in range(2)]
    for j in range(3):
        ej = tuple(1 if t == j else 0 for t in range(3))
        for sgn in (1, -1):
            if d == tuple(sgn * t for t in ej):
                c = (Fr(0), Fr(-sgn, 2))
                return [[cmul(c, PAULI[j][a][b]) for b in range(2)] for a in range(2)]
    return None


def moving_witness():
    """a four-site spinor amplitude with a phase ((3 + 4i)/5)^n along the x axis; K_xy = Re chi_x^dag H_xy chi_y."""
    mu = Fr(3, 2)
    step = (Fr(3, 5), Fr(4, 5))
    amps, cur = {}, C1
    for s in ((-1, 0, 0), (0, 0, 0), (1, 0, 0)):
        amps[s] = (cmul(cur, (Fr(1, 2), Fr(0))), cmul(cur, (Fr(1, 4), Fr(1, 4))))
        cur = cmul(cur, step)
    amps[(0, 1, 0)] = ((Fr(1, 4), Fr(0)), (Fr(0), Fr(-1, 4)))
    supp = sorted(amps)
    kmat = {}
    for x in supp:
        for y in supp:
            hb = hblock(x, y, mu)
            if hb is None:
                continue
            tot = C0
            for a in range(2):
                for b in range(2):
                    tot = cadd(tot, cmul((amps[x][a][0], -amps[x][a][1]), cmul(hb[a][b], amps[y][b])))
            if tot[0] != 0:
                kmat[(x, y)] = tot[0]
    return supp, kmat


def solve_moving(h, supp, kmat, e, k):
    sites = interior(h)
    idx = {s: i for i, s in enumerate(sites)}
    rows = []
    for s in sites:
        row = {idx[s]: Fr(1)}
        for d in DIRS:
            y = add(s, d)
            if inside(y, h):
                row[idx[y]] = row.get(idx[y], Fr(0)) - Fr(1, 6)
        for t in supp:
            if (s, t) in kmat:
                row[idx[t]] = row.get(idx[t], Fr(0)) + k * kmat[(s, t)]
        rows.append(row)
    psi = solve_sparse(rows, [[k * e.get(s, Fr(0)) for s in sites]])[0]
    return {s: 1 - psi[idx[s]] for s in sites}


def ledger_from_definition(h, phi, kmat, gam):
    quad = sum((phi[x] * v * phi[y] for (x, y), v in kmat.items()), Fr(0))
    bonds = Fr(0)
    for s in phi:
        for d in DIRS:
            t = add(s, d)
            if inside(t, h):
                if s < t:
                    bonds += (phi[s] - phi[t]) ** 2
            else:
                bonds += (phi[s] - 1) ** 2
    return quad + (2 / gam) * bonds


def family_b(checks: Checks) -> None:
    """T1: the price of one record, for a moving amplitude."""
    h = 3
    supp, kmat = moving_witness()
    sym = all(kmat.get((y, x), 0) == v for (x, y), v in kmat.items())
    e = {x: sum((kmat.get((x, y), Fr(0)) for y in supp), Fr(0)) for x in supp}
    energy = sum(e.values(), Fr(0))
    hopping = sum((v for (x, y), v in kmat.items() if x != y), Fr(0))
    g0 = green(h, ORIGIN)
    gam = Fr(1)
    k = gam / 12
    phi = solve_moving(h, supp, kmat, e, k)
    lam = ledger_from_definition(h, phi, kmat, gam)
    weight = 2 if mut("moving_ledger_forged") else 1
    lam_sum = sum((e[x] * phi[x] ** weight for x in supp), Fr(0))
    pr = price(lam, k, g0[ORIGIN])
    rec_lam, _ = ledger_rest(h, {ORIGIN: pr}, k, group_full())
    ro = price(energy, k, g0[ORIGIN])
    ok1 = (sym and energy == Fr(21, 20) and hopping == Fr(39, 80) and all(v > 0 for v in phi.values()) and lam == lam_sum
           and 0 < k * lam * g0[ORIGIN] < 1 and rec_lam == lam)
    checks.check("B1", ok1,
                 f"T1(a),(b): a moving amplitude (four sites, phase ((3+4i)/5)^n, E = {energy}, hopping part {hopping}) in the box of side 7 at gamma = 1: every rate positive; the ledger from its definition equals sum_x e_x phi_x exactly (Lambda = {dec(lam)}); the record at the centre keeps it at E' = Lambda/(1 - k Lambda g_yy) = {dec(pr)} (its own static ledger is Lambda exactly); under records only the same record needs E/(1 - k E g_yy) = {dec(ro)}")
    gcols = {y: green(h, y) for y in supp}
    ege = sum((e[x] * gcols[y][x] * e[y] for x in supp for y in supp), Fr(0))
    ok2, shown = True, []
    for g_small in (Fr(1, 10 ** 4), Fr(1, 10 ** 5)):
        ks = g_small / 12
        ph = solve_moving(h, supp, kmat, e, ks)
        lam_s = ledger_from_definition(h, ph, kmat, g_small)
        ratio = (price(lam_s, ks, g0[ORIGIN]) - energy) / (ks * (energy ** 2 * g0[ORIGIN] - ege))
        ratio_ro = (price(energy, ks, g0[ORIGIN]) - energy) / (ks * energy ** 2 * g0[ORIGIN])
        ok2 = ok2 and 0 < ratio - 1 < ks and 0 < ratio_ro - 1 < 2 * ks
        shown.append(f"gamma = {g_small}: ratio - 1 = {dec((ratio - 1) / ks, 4)} k")
    checks.check("B2", ok2 and ege > 0,
                 "T1(c): at weak field E' - E = k(E^2 g_yy - e.g.e) + O(k^2) and, under records only, k E^2 g_yy + O(k^2): the exact ratios exceed 1 by less than k and 2k (" + "; ".join(shown) + ")")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: where the record forms, in a held box."""
    h, k = 3, Fr(1, 12)
    cube = {x: Fr(1, 27) for x in interior(2)}
    lam, _ = ledger_rest(h, cube, k, group_full())
    kinds = ((1, 1, 1), (1, 1, 0), (1, 0, 0), ORIGIN)
    gdiag = {y: green(h, y)[y] for y in kinds}
    if mut("site_blind_price_in_box"):
        gdiag = {y: gdiag[ORIGIN] for y in kinds}
    prices = [price(lam, k, gdiag[y]) for y in kinds]
    ok1 = all(prices[i] < prices[i + 1] for i in range(3)) and gdiag[ORIGIN] == Fr(136, 99)
    checks.check("C1", ok1,
                 f"T2(a): the uniform 3^3 cube at rest (E = 1, gamma = 1) in the box of side 7 has Lambda = {dec(lam)} and needs {dec(prices[0])} at its corners, {dec(prices[1])} at edge midpoints, {dec(prices[2])} at face centres and {dec(prices[3])} at its centre (g at the centre = 136/99): in a held box the price depends on the formation site")
    corner = (2, 2, 2)
    rho = {ORIGIN: Fr(99, 100), corner: Fr(1, 100)}
    gc, gk = green(h, ORIGIN), green(h, corner)
    ege = rho[ORIGIN] ** 2 * gc[ORIGIN] + 2 * rho[ORIGIN] * rho[corner] * gc[corner] + rho[corner] ** 2 * gk[corner]
    lam2, _ = ledger_rest(h, rho, k, group_fixing(corner))
    p_corner, p_centre = price(lam2, k, gk[corner]), price(lam2, k, gc[ORIGIN])
    maxp = all(gc[x] <= gc[ORIGIN] for x in gc) and all(gk[x] <= gk[corner] for x in gk)
    ok2 = gk[corner] - ege < 0 < gc[ORIGIN] - ege and p_corner < 1 < p_centre and maxp
    checks.check("C2", ok2,
                 f"T2(b): 99/100 of E = 1 at the centre of the box of side 7 and 1/100 at the interior corner: first-order price at the corner {dec(gk[corner] - ege)} < 0 < {dec(gc[ORIGIN] - ege)} at the centre; exactly at gamma = 1 the corner needs E' = {dec(p_corner)} < 1 and the centre {dec(p_centre)} > 1; g(x, y) <= g(y, y) at every interior x for y the centre and the corner (the maximum principle behind the statement on Z^3)")


# ============================================================================================ family D
def star(m0, m1):
    d = {ORIGIN: m0}
    for dd in DIRS:
        d[dd] = m1
    return d


def family_d(checks: Checks) -> None:
    """T3: the seven-site star."""
    full = group_full()
    ok1, shown = True, []
    for m0, m1, gam, want in ((Fr(1, 7), Fr(1, 7), Fr(1), Fr(1188, 1091)), (Fr(1, 2), Fr(1, 12), Fr(7, 3), Fr(5436, 4631))):
        k = gam / 12
        c = (m0 + 6 * m1) if mut("star_price_forged") else m0 / (1 + k * m0) + 6 * m1
        closed = c / (1 - k * c)
        for h in (3, 4, 5):
            lam, psi = ledger_rest(h, star(m0, m1), k, full)
            g = reduced_solve(h, full, {}, [{ORIGIN: Fr(1)}])[0]
            q_total = k * lam
            q1 = k * m1 * (1 - psi[(1, 0, 0)])
            point = all(psi[x] == q_total * g[x] for x in psi if x != ORIGIN)
            centre = psi[ORIGIN] == q_total * g[ORIGIN] - 6 * q1
            ok1 = ok1 and point and centre and price(lam, k, g[ORIGIN]) == closed == want
        shown.append(f"m0 = {m0}, m1 = {m1}, gamma = {gam}: {want}")
    checks.check("D1", ok1,
                 "T3(a),(b): in the boxes of side 7, 9 and 11 the star's field equals Q g(x, y) at every interior site x != y (Q = k Lambda) and Q g_yy - 6 q1 at y, and its price is c/(1 - k c), c = m0/(1 + k m0) + 6 m1, in every box (" + "; ".join(shown) + ")")
    m0, m1, ks = sp.symbols("m0 m1 k", positive=True)
    cs = m0 / (1 + ks * m0) + 6 * m1
    first = sp.expand(sp.series(cs / (1 - ks * cs) - (m0 + 6 * m1), ks, 0, 2).removeO())
    checks.check("D2", sp.simplify(first - ks * (12 * m0 * m1 + 36 * m1 ** 2)) == 0,
                 "T3(c): at first order the star's price is E' - E = k(12 m0 m1 + 36 m1^2), the same in every box (symbolic)")
    k = Fr(1, 12)
    ball = star(Fr(1, 19), Fr(1, 19))
    for x in interior(3):
        if sorted(map(abs, x)) == [0, 1, 1]:
            ball[x] = Fr(1, 19)
    cross = {ORIGIN: Fr(1, 7)}
    for dd in DIRS:
        cross[(2 * dd[0], 2 * dd[1], 2 * dd[2])] = Fr(1, 7)
    ok3, shown = True, []
    for name, amp in (("19-site ball", ball), ("seven-site cross at distance two", cross)):
        vals = []
        for h in (3, 4, 5):
            lam, _ = ledger_rest(h, amp, k, full)
            vals.append(price(lam, k, green(h, ORIGIN)[ORIGIN]))
        ok3 = ok3 and len(set(vals)) == 3
        shown.append(f"{name}: " + ", ".join(dec(v) for v in vals))
    checks.check("D3", ok3,
                 "T3(d): larger uniform symmetric spreads at gamma = 1 have prices that change with the box (sides 7, 9, 11; exact, all distinct): " + "; ".join(shown))


# ============================================================================================ family E
def kick(field):
    """the test body's transverse kick along (x, -1, 0), |x| <= 3: sum_x (psi(x, 0, 0) - psi(x, -2, 0))/2."""
    return sum(((field[(x, 0, 0)] - field[(x, -2, 0)]) / 2 for x in range(-3, 4)), Fr(0))


def family_e(checks: Checks) -> None:
    """T4: a source in two places, at first order."""
    h = 4
    left, right = (0, -2, 0), (0, 2, 0)
    g_left = green(h, left)
    g_right = {(x, y, z): g_left[(x, -y, z)] for (x, y, z) in g_left}
    d_left, d_right = kick(g_left), kick(g_right)
    ok, shown = d_left < 0 < d_right, []
    for p_left in (Fr(1, 2), Fr(1, 3)):
        p_right = 1 - p_left
        src = {left: p_left} if mut("unformed_source_kick_forged") else {left: p_left, right: p_right}
        unformed = kick(reduced_solve(h, group_preserving(src), {}, [src])[0])
        values = {Fr(0), d_left, d_right, unformed}
        ok = ok and unformed == p_left * d_left + p_right * d_right and len(values) == 4
        shown.append(f"p_L = {p_left}: {dec(unformed)}")
    checks.check("E1", ok,
                 f"T4: box of side 9, L = (0,-2,0), R = (0,2,0), the test line (x,-1,0), per unit k E_B: formed at L {dec(d_left)}, at R {dec(d_right)}; unformed under records only 0; unformed under amplitude sourcing, from one solve with both lobes, exactly p_L d_L + p_R d_R (" + "; ".join(shown) + "): four distinct values in each case, so the stipulated single-passage field-functional values differ; ensemble mean readouts alone do not distinguish the readings")


# ============================================================================================ family F
FENCES = (
    "This note works within the static clock law of blocks 55, 56 and 58, as landed on main, with a supplied formation event that replaces an amplitude by one record at rest; it reports what the record's energy must be for the ledger to be kept, where the record forms, and what a source in two places does under the two readings of what sources the field; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Møller", "Rosenfeld", "Diósi", "Penrose", "Page", "Geilker", "Watson", "Sherman", "Morrison", "Cauchy", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the moving witness's ledger from its definition against sum e phi; the record's own ledger; the weak-field ratios at two couplings, under both readings",
    "per_site: executed - the cube's four prices in the box of side 7; the corner example on both sides of E; g(x, y) <= g(y, y) at every interior site for two sources",
    "per_mode: executed - the star's field against a point charge at every interior site of three boxes; the first-order price symbolically",
    "per_block: executed - the star's price, the 19-site ball's and the distance-two cross's in boxes of side 7, 9 and 11; the two-place kicks from one solve with both lobes",
    "lattice_wide: T1 algebraic for a static solution, with capacity/positivity needed for feasible formation; T2(a) on equal-diagonal targets and T3 for the interior star in symmetric domains; T2(b) on Z^3 for amplitudes at rest; T4 at first order for every linear kick; the clock law, the amplitude and the formation event are supplied, and the choice between the readings is not made",
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
    print('scope: Formation ledger identity with capacity/positivity constraints; equal-diagonal target condition and supplied readout conventions. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
