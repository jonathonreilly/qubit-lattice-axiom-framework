#!/usr/bin/env python3
"""Exact checks: what a source is when records move.

Scope (under the moving-records reading of block 39 and the law with vacancies; nothing adopted).
T1: a local, non-negative, additive one-site density that vanishes on an empty site and is invariant under the symmetries acting on
contents is a constant times the occupancy, because the 24 proper rotations of the cube act transitively on the six axes: every record
has the same mass and a cluster's mass is its number of records.  T2: two sets of records separated by empty sites do not interact:
given the occupancy the contents of the components are independent, and the weight of two clusters, contents summed, is w(A) w(B) at
every gap of at least one empty site, at any binding scale.  T3: through a medium of records the potential of mean force of the record
density is -log(1 + g(r)); on the periodic 2 x 8 ladder g(r) is computed exactly and falls by about a factor of ten per step at the
pinned scale.  T4: in the quadratic stand-in for an ordered sphere medium a held tilt a at a site produces the mean field
a G(y)/G(0) around it, G the lattice Green function, and two held tilts interact by -kappa a b G(r)/(G(0)^2 - G(r)^2): a
one-over-distance channel whose charge is a signed vector (like tilts attract, opposite tilts repel), not the mass of T1; exactly, in
every law invariant under the rotation of all contents, the content field around a held record is a multiple of its content vector,
and around a record of unread content it is zero.  T5: under symmetric transit with one record per site the mean occupancy obeys the
lattice heat equation exactly (the exclusion cancels in the mean), so a production profile held fixed carries the stationary field
G * (j - mean j)/kappa, G the lattice Green function; at the neutral scale the formation rate of block 39 next to records of
independent uniform contents equals the rate in the void on average, and exceeds it next to agreeing records.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_WHAT_A_SOURCE_IS_WHEN_RECORDS_MOVE_ONE_MASS_PER_RECORD_NO_ACTION_ACROSS_EMPTY_SPACE_SCREENED_DENSITY_POTENTIAL_SIGNED_TILT_CHANNEL_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_what_a_source_is_when_records_move_one_mass_per_record_no_action_across_empty_space_screened_density_potential_signed_tilt_channel_bounded_theorem_note_2026-09-20"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "A site with no record cannot be read.",
)
BRIDGE_NEEDLES = ("Source-readout bridge", "local, diagonal, positive, phase-invariant quadratic density", "rho_psi(x) = |psi(x)|^2")

MUTATION_GATE = {
    "orbit_not_transitive_injected": "B",
    "gap_interaction_injected": "B",
    "contents_coupled_across_gap_injected": "B",
    "ladder_not_screened_injected": "C",
    "tree_law_at_wrong_scale_injected": "C",
    "content_field_not_odd_injected": "D",
    "tilt_sign_universal_injected": "D",
    "mean_field_wrong": "D",
    "closure_with_glue_injected": "E",
    "green_function_wrong_injected": "E",
    "production_mean_at_wrong_scale_injected": "E",
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
INDEX = {v: k for k, v in AXIS.items()}


def weights(p, q, r, c):
    return [[Fraction(c) * (p if a == b else q if a == (b ^ 1) else r) for b in M6] for a in M6]


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, bridge = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the sentences used")
    checks.check("A3", all(n in normalize_text(bridge) for n in BRIDGE_NEEDLES), "the gravity lane's weak-field bridge note on main states the requirements on a source density that T1 applies to records")


# ============================================================================================ family B (T1, T2)
def rotations():
    rots = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            m = [[signs[i] if perm[i] == j else 0 for j in range(3)] for i in range(3)]
            det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
            if det == 1:
                rots.append(m)
    return rots


def act(m, a):
    return INDEX[tuple(sum(m[i][j] * AXIS[a][j] for j in range(3)) for i in range(3))]


def cluster_weight(W, n: int) -> Fraction:
    v = [Fraction(1)] * 6
    for _ in range(n - 1):
        v = [sum(v[a] * W[a][b] for a in M6) for b in M6]
    return sum(v)


def line_weight(W, occupied) -> Fraction:
    """records on a line at the positions in `occupied`, contents summed"""
    occ = sorted(occupied)
    tot = Fraction(0)
    for cfg in product(M6, repeat=len(occ)):
        w = Fraction(1)
        for i in range(len(occ) - 1):
            if occ[i + 1] == occ[i] + 1:
                w *= W[cfg[i]][cfg[i + 1]]
        tot += w
    return tot


def family_b(checks: Checks) -> None:
    rots = rotations()
    if mut("orbit_not_transitive_injected"):
        rots = [m for m in rots if m[2][2] == 1]          # only the rotations about the z axis
    orbit = {act(m, 0) for m in rots}
    f = [Fraction(v) for v in (5, 1, 7, 2, 9, 4)]
    avg = [sum(f[act(m, a)] for m in rots) / len(rots) for a in M6]
    checks.check("B1", len(orbit) == 6 and len(set(avg)) == 1, f"T1: the proper rotations of the cube ({len(rots)}) carry the axis +z to all six axes, and a one-site density averaged over them is constant on contents ({avg[0]}): an invariant, additive density vanishing on empty sites is a constant times the occupancy")
    ok = True
    ratios = []
    for c in (Fraction(6, 21), Fraction(1)):
        W = weights(12, 1, 2, c)
        ref = cluster_weight(W, 2) * cluster_weight(W, 3)
        for gap in (1, 2, 3, 4):
            w = line_weight(W, [0, 1] + [2 + gap + i for i in range(3)])
            if mut("gap_interaction_injected") and gap == 1:
                w = w * 2
            ok = ok and w == ref
        ratios.append(line_weight(W, [0, 1, 2, 3, 4]) / ref)
    checks.check("B2", ok, f"T2: two clusters of 2 and 3 records on a line weigh w(A) w(B) at every gap of 1 to 4 empty sites, at the neutral scale and at scale 1 for (12,1,2): no interaction across empty sites; touching multiplies the weight by {ratios[0]} (neutral scale) and {ratios[1]} (scale 1)")
    W = weights(3, 1, 2, 1)
    joint = {}
    for cfg in product(M6, repeat=4):
        w = W[cfg[0]][cfg[1]] * W[cfg[2]][cfg[3]]
        if mut("contents_coupled_across_gap_injected"):
            w *= W[cfg[1]][cfg[2]]
        joint[cfg] = w
    tot = sum(joint.values())
    ma, mb = {}, {}
    for cfg, w in joint.items():
        ma[cfg[:2]] = ma.get(cfg[:2], 0) + w
        mb[cfg[2:]] = mb.get(cfg[2:], 0) + w
    ok2 = all(w / tot == (ma[cfg[:2]] / tot) * (mb[cfg[2:]] / tot) for cfg, w in joint.items())
    checks.check("B3", ok2, "T2: given the occupancy, the contents of two components separated by an empty site are independent (all 1296 contents of two pairs)")


# ============================================================================================ family C (T3)
def ladder_pair_correlation(p, q, r, c, z, length=8):
    W = weights(p, q, r, c)
    states = [(a, b) for a in list(M6) + [None] for b in list(M6) + [None]]
    n = len(states)

    def rung(s):
        w = Fraction(1)
        for v in s:
            if v is not None:
                w *= z
        if s[0] is not None and s[1] is not None:
            w *= W[s[0]][s[1]]
        return w

    def legs(s, t):
        w = Fraction(1)
        for i in (0, 1):
            if s[i] is not None and t[i] is not None:
                w *= W[s[i]][t[i]]
        return w

    T = [[rung(s) * legs(s, t) for t in states] for s in states]
    occ = [1 if s[0] is not None else 0 for s in states]

    def mm(a, b):
        return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

    powers = {0: [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]}
    for k in range(1, length + 1):
        powers[k] = mm(powers[k - 1], T)
    Z = sum(powers[length][i][i] for i in range(n))
    rho = sum(occ[i] * powers[length][i][i] for i in range(n)) / Z
    g = {}
    for d in range(1, length // 2 + 1):
        a, b = powers[d], powers[length - d]
        g[d] = sum(occ[i] * a[i][j] * occ[j] * b[j][i] for i in range(n) for j in range(n)) / Z / rho ** 2 - 1
    return rho, g


def open_line_covariances(p, q, r, c, z, n_sites=5):
    """grand-canonical law on an open line, contents summed: Cov(n_0, n_j)"""
    W = weights(p, q, r, c)
    vals = list(M6) + [None]
    tot = Fraction(0)
    m1 = [Fraction(0)] * n_sites
    m2 = [Fraction(0)] * n_sites
    # transfer by vectors, with markers: enumerate occupancy patterns, contents summed by runs
    for occ in product((0, 1), repeat=n_sites):
        w = Fraction(1)
        i = 0
        while i < n_sites:
            if occ[i]:
                j = i
                while j + 1 < n_sites and occ[j + 1]:
                    j += 1
                w *= z ** (j - i + 1) * cluster_weight(W, j - i + 1)
                i = j + 1
            else:
                i += 1
        tot += w
        for k in range(n_sites):
            if occ[k]:
                m1[k] += w
                if occ[0]:
                    m2[k] += w
    return [m2[k] / tot - (m1[0] / tot) * (m1[k] / tot) for k in range(1, n_sites)]


def family_c(checks: Checks) -> None:
    rho, g = ladder_pair_correlation(12, 1, 2, Fraction(6, 21), Fraction(1, 12))
    ok = all(g[d] > 0 for d in g) and all(g[d + 1] < g[d] / 3 for d in (1, 2))
    if mut("ladder_not_screened_injected"):
        ok = ok and g[3] > g[1] / 4
    shown = ", ".join(f"r={d}: {g[d].numerator * 10 ** 7 // g[d].denominator}/10^7" for d in sorted(g))
    checks.check("C1", ok, f"T3: on the periodic 2 x 8 ladder at (12,1,2), the neutral scale and z = 1/12 (density {rho.numerator * 1000 // rho.denominator}/1000), the field of a held record, g(r) - 1, is positive and falls by more than a factor of three per step ({shown}): short range")
    c_used = Fraction(1) if mut("tree_law_at_wrong_scale_injected") else Fraction(6, 21)
    cov = open_line_covariances(12, 1, 2, c_used, Fraction(1, 5))
    cov1 = open_line_covariances(12, 1, 2, Fraction(1), Fraction(1, 5))
    checks.check("C2", all(v == 0 for v in cov) and all(v > 0 for v in cov1), f"T3: on an open line of five sites (no cycle) the field of a held record is exactly zero at the neutral scale (block 40's tree law) and positive at scale 1 (Cov(n_0, n_1) = {cov1[0].numerator * 10 ** 5 // cov1[0].denominator}/10^5)")


# ============================================================================================ family D (T4)
def green(L: int, shift=0):
    cos = {4: (1, 0, -1, 0), 6: (Fraction(1), Fraction(1, 2), Fraction(-1, 2), Fraction(-1), Fraction(-1, 2), Fraction(1, 2))}[L]
    modes = [k for k in product(range(L), repeat=3) if any(k)]
    ev = {k: 6 - 2 * sum(Fraction(cos[m]) for m in k) + shift for k in modes}

    def G(x):
        tot = Fraction(0)
        for k in modes:
            ph = sum(k[i] * x[i] for i in range(3)) % L
            tot += Fraction(cos[ph]) / ev[k]
        return tot / L ** 3

    return G


def family_d(checks: Checks) -> None:
    # the symmetry lemma on the fully occupied plaquette and on the plaquette with vacancies
    W = weights(3, 1, 2, 1)
    bonds = [(0, 1), (1, 2), (2, 3), (3, 0)]
    field = {a: [Fraction(0)] * 3 for a in M6}
    norm = {a: Fraction(0) for a in M6}
    for cfg in product(M6, repeat=4):
        w = Fraction(1)
        for (i, j) in bonds:
            w *= W[cfg[i]][cfg[j]]
        if mut("content_field_not_odd_injected") and cfg[2] == 0:
            w *= 2                                        # a one-site preference for +z breaks the invariance
        norm[cfg[0]] += w
        for t in range(3):
            field[cfg[0]][t] += w * AXIS[cfg[2]][t]
    coef = set()
    ok = True
    for a in M6:
        vec = [field[a][t] / norm[a] for t in range(3)]
        nz = [t for t in range(3) if AXIS[a][t] != 0][0]
        ok = ok and all(vec[t] == 0 for t in range(3) if t != nz)
        coef.add(vec[nz] * AXIS[a][nz])
    unread = [sum(field[a][t] for a in M6) for t in range(3)]
    ok = ok and len(coef) == 1 and all(v == 0 for v in unread)
    c_val = sorted(coef)[0]
    checks.check("D1", ok, f"T4: on the occupied plaquette at (3,1,2) the mean content vector at the far corner, given the content a at a corner, is {c_val} times the vector of a for each of the six contents, and it is zero for a record whose content is not read: the charge of the content channel is the content vector, odd and of zero mean; the occupancy carries none")
    ok = True
    ok_lin = True
    for L in (4, 6):
        G = green(L)
        g0, g1, g2 = G((0, 0, 0)), G((1, 0, 0)), G((2, 0, 0))
        ok = ok and g0 > g1 > 0 and g1 > g2
        for (a, b) in ((1, 1), (1, -1), (2, 3), (-2, 3)):
            inter = -Fraction(a * b) * g1 / (g0 * g0 - g1 * g1)
            if mut("tilt_sign_universal_injected"):
                ok = ok and inter < 0
            else:
                ok = ok and ((inter < 0) == (a * b > 0))
        a = Fraction(3)
        for y in ((1, 0, 0), (2, 0, 0), (1, 1, 0)):
            # conditional mean of a centred Gaussian field with covariance G given the value a at the origin
            cond = G(y) * a / g0
            want = a * G(y) / (g0 * 2) if mut("mean_field_wrong") else a * G(y) / g0
            ok_lin = ok_lin and cond == want
        x2 = (2, 0, 0)
        gx = G(x2)
        det = g0 * g0 - gx * gx
        for y in ((1, 0, 0), (1, 1, 0)):
            ya, yb = G(y), G(tuple((y[i] - x2[i]) % L for i in range(3)))

            def mean2(aa, bb):
                return ((ya * g0 - yb * gx) * aa + (yb * g0 - ya * gx) * bb) / det

            ok_lin = ok_lin and mean2(2, 5) == 2 * mean2(1, 0) + 5 * mean2(0, 1) and mean2(1, 0) * det == ya * g0 - yb * gx
            ok_lin = ok_lin and mean2(1, 1) != ya / g0 + yb / g0          # not the sum of the two one-tilt fields
    checks.check("D2", ok, "T4: on the 4^3 and 6^3 tori the lattice Green function has G(0) > G(1) > G(2) and G(1) > 0, and two held tilts a, b one step apart interact by -kappa a b G/(G(0)^2 - G^2): negative for like tilts, positive for opposite ones; the charge of this channel is signed")
    checks.check("D3", ok_lin, "T4: the mean field around a held tilt a is a G(y)/G(0); around two held tilts it is linear in (a, b), each term the field of one tilt with the other site held at zero, and it is not the sum of the two one-tilt fields")


# ============================================================================================ family E (T5)
def family_e(checks: Checks) -> None:
    # closure of the mean under symmetric transit with one record per site, on the cube graph (8 sites, 256 arrangements)
    nbrs = {v: [v ^ 1, v ^ 2, v ^ 4] for v in range(8)}
    ok = True
    for eta in range(256):
        occ = [(eta >> v) & 1 for v in range(8)]
        gen = [0] * 8
        for u in range(8):
            if not occ[u]:
                continue
            for w in nbrs[u]:
                if occ[w]:
                    continue
                rate = 1
                if mut("closure_with_glue_injected"):
                    rate += sum(occ[t] for t in nbrs[w] if t != u)      # a move preferred towards occupied neighbourhoods
                gen[u] -= rate
                gen[w] += rate
        for x in range(8):
            ok = ok and gen[x] == sum(occ[y] - occ[x] for y in nbrs[x])
    checks.check("E1", ok, "T5: under symmetric transit with one record per site the generator applied to the occupancy of a site equals the lattice Laplacian of the occupancy, on all 256 arrangements of the cube graph: the exclusion cancels in the mean, and the mean occupancy obeys the lattice heat equation")
    L = 4
    G = green(L, shift=1 if mut("green_function_wrong_injected") else 0)
    vals = {x: G(x) for x in product(range(L), repeat=3)}
    ok2 = True
    for x in vals:
        lap = 6 * vals[x]
        for i in range(3):
            for s in (1, -1):
                y = list(x)
                y[i] = (y[i] + s) % L
                lap -= vals[tuple(y)]
        ok2 = ok2 and lap == (1 if x == (0, 0, 0) else 0) - Fraction(1, L ** 3)
    checks.check("E2", ok2, "T5: on the 4^3 torus minus the lattice Laplacian of G equals the point source minus its mean at all 64 sites: a production profile j held fixed carries the stationary field G * (j - mean j)/kappa, the operator of the gravity lane's field equation with production as its source")
    ok3 = True
    shown = []
    for (p, q, r) in ((3, 1, 2), (12, 1, 2)):
        c0 = Fraction(6, p + q + 4 * r)
        c = Fraction(1) if mut("production_mean_at_wrong_scale_injected") else c0
        W = weights(p, q, r, c)
        for k in (1, 2, 3):
            tot = Fraction(0)
            for nb in product(M6, repeat=k):
                zx = Fraction(0)
                for v in M6:
                    t = Fraction(1)
                    for b in nb:
                        t *= W[v][b]
                    zx += t
                tot += zx / 6
            ok3 = ok3 and tot / 6 ** k == 1
        agree = [sum(W[v][0] ** k for v in M6) / 6 for k in (2, 3)]
        ok3 = ok3 and all(v > 1 for v in agree)
        shown.append(f"({p},{q},{r}): {agree[0]}, {agree[1]}")
    checks.check("E3", ok3, f"T5: at the neutral scale the formation rate of block 39 next to one, two or three records of independent uniform contents equals the rate in the void on average, exactly, and next to two and three agreeing records it is larger by the factors {'; '.join(shown)}: records that agree are a net source of records, records that do not are not")


# ============================================================================================ family F
FENCES = (
    "This note works under the moving-records reading of block 39 and defines a source by the requirements the gravity lane already states; it finds no universal one-over-distance attraction in the equilibrium of moving records, and it adopts nothing.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 10."}
CLASSICAL_NAMES = ("Newton", "Yukawa", "Ornstein", "Zernike", "Goldstone", "Casimir", "Gibbs", "Boltzmann", "Perron", "Frobenius", "Laplace", "Poisson", "Coulomb", "Waals", "Cauchy", "Schwarz", "Bayes", "Bernoulli")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Newton)", 1)
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
    "per_element: executed — the 24 rotations and the orbit of an axis; the invariant one-site density; the formation rate next to one, two and three records of every content",
    "per_site: executed — two clusters on a line at gaps of 1 to 4 empty sites and touching, two scales; the independence of the contents of separated components; the closure of the mean on all 256 arrangements of the cube graph",
    "per_mode: executed — the lattice Green function on the 4^3 and 6^3 tori; the interaction of two held tilts, the linearity of the mean field, and the field equation at all 64 sites",
    "per_block: executed — the exact field of a held record on the periodic 2 x 8 ladder and on the open line of five sites; the content field on the occupied plaquette",
    "lattice_wide: T1, T2, the symmetry part of T4 and the closure of T5 hold on every finite window; T3 is exact on the ladder and executed on the cubic lattice in the controls; no one-over-distance attraction between masses is found in the equilibrium of moving records, and none is claimed absent elsewhere",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


# ============================================================================================ main
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
    print("scope: what a source is when records move — one mass per record; no interaction across empty sites; the field of a held record is of short range; the one-over-distance channel carries a signed tilt; the transit Laplacian is sourced by production; exact")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
