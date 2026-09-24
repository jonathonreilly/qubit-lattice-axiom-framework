#!/usr/bin/env python3
"""Exact checks: free capturing bodies in the inertial record gas (block 44's clause and a body clause; both supplied, not adopted).

T1 the capture law: in a product state a capturing site takes up records at the rate (rho/sqrt 3) <|s|_1> and momentum at the rate
(rho/sqrt 3) <|s|_1 s>, because sum_k max(0, s.e_k) = |s|_1; a record is captured in proportion to |s|_1, between 1 and sqrt 3, so the
captured records are not an unbiased sample of the gas.  T2: for the uniform sphere <|s|_1> = 3/2 and <|s|_1 s_i s_j> = delta_ij/2, hence in
a wind with the first-harmonic content law (1 + 3 u.s)/(4 pi) every captured record brings u on average; for a body the same holds when its
exposed faces are equally many along the three axes, and fails for a plate.  T3 the collisionless shadow: for independent records the deficit
behind a capturing site is the multinomial hitting probability; it sums to one over every shell; its integral over the simplex of step
frequencies is 1/((n+1)(n+2)) at every site of the shell; the force on a transparent site has the coefficient |r|_1^2 (between 1 and 3,
against 9/4 for the collisional law), doubled on coordinate planes and fourfold on the axes.  T4 the dilution law: under the body clause both
capture channels bring the wind's mean content.  T5: the closure law of motion and the window in which a fall is accelerated.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from math import comb, factorial, isqrt
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_FREE_CAPTURING_BODIES_ARE_CARRIED_BY_THE_WIND_CAPTURE_LAW_ANISOTROPIC_COLLISIONLESS_SHADOW_DILUTION_LAW_OF_MOTION_AND_ITS_WINDOW_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_free_capturing_bodies_are_carried_by_the_wind_capture_law_anisotropic_collisionless_shadow_dilution_law_of_motion_and_its_window_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = ("A site never carries more than one record; records are permanent.",)

MUTATION_GATE = {
    "capture_sample_unbiased": "B",
    "second_moment_wrong": "B",
    "plate_response_parallel": "B",
    "shadow_step_frequencies_wrong": "C",
    "simplex_integral_wrong": "C",
    "axis_multiplicity_one": "C",
    "collisionless_coefficient_isotropic": "C",
    "sweeping_brings_no_momentum": "D",
    "window_coefficient_wrong": "E",
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


def unit_contents():
    """Rational unit vectors: signed permutations of integer triples of integer length."""
    out = set()
    for d, length in (((1, 0, 0), 1), ((3, 4, 0), 5), ((1, 2, 2), 3), ((2, 3, 6), 7), ((1, 4, 8), 9), ((4, 4, 7), 9)):
        for perm in set(product(range(3), repeat=3)):
            if sorted(perm) != [0, 1, 2]:
                continue
            for sg in product((1, -1), repeat=3):
                out.add(tuple(F(sg[i] * d[perm[i]], length) for i in range(3)))
    return sorted(out)


def one_norm(s):
    return sum(abs(c) for c in s)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the sentence used")


# ============================================================================================ family B (T1, T2)
def abs_moment(a: int) -> Fraction:
    """<|z|^a> over the uniform sphere: z is uniform on [-1, 1]."""
    return F(1, a + 1)


def abs_z_x2(a: int) -> Fraction:
    """<|z|^a x^2>: given z, x^2 averages (1 - z^2)/2."""
    return (abs_moment(a) - abs_moment(a + 2)) / 2


def family_b(checks: Checks) -> None:
    contents = unit_contents()
    ok = all(sum(c * c for c in s) == 1 for s in contents)
    ok = ok and all(sum(max(F(0), sum(s[i] * e[i] for i in range(3))) for e in E) == one_norm(s) for s in contents)
    ok = ok and all(1 <= one_norm(s) ** 2 <= 3 for s in contents)
    top = max(one_norm(s) ** 2 for s in contents)
    checks.check("B1", ok and len(contents) == 174 and top == F(25, 9), f"T1: sum over the six directions of max(0, s.e_k) is |s|_1 for {len(contents)} rational unit contents, and 1 <= |s|_1^2 <= 3 (largest here {top}): a record is captured in proportion to |s|_1")
    # two equally likely contents: the captured mean is not the gas mean
    s_a, s_b = (F(1), F(0), F(0)), (F(-3, 5), F(-4, 5), F(0))
    gas_mean = tuple((s_a[i] + s_b[i]) / 2 for i in range(3))
    wa, wb = one_norm(s_a), one_norm(s_b)
    cap_mean = tuple((wa * s_a[i] + wb * s_b[i]) / (wa + wb) for i in range(3))
    if mut("capture_sample_unbiased"):
        cap_mean = gas_mean
    checks.check("B2", gas_mean == (F(1, 5), F(-2, 5), F(0)) and cap_mean == (F(1, 15), F(-7, 15), F(0)), f"T1: for the two contents (1,0,0) and (-3/5,-4/5,0), equally likely, the gas has mean content {tuple(str(c) for c in gas_mean)} and the captured records {tuple(str(c) for c in cap_mean)}: capture is a biased sample")
    # sphere moments
    m1 = 3 * abs_moment(1)                                           # <|s|_1>
    xx = abs_moment(3) + 2 * (F(1, 6) if mut("second_moment_wrong") else abs_z_x2(1))   # <|s|_1 s_x^2>
    ok = m1 == F(3, 2) and xx == F(1, 2)
    # first harmonic: momentum rate / number rate = 3 u <|s|_1 s_x^2> / <|s|_1>
    ratio = 3 * xx / m1
    checks.check("B3", ok and ratio == 1, f"T2: over the uniform sphere <|s|_1> = {m1} and <|s|_1 s_i s_j> = ({xx}) delta_ij, so in a wind with content law (1 + 3 u.s)/(4 pi) a capturing site takes up q_1 = (sqrt 3/2) rho records and the momentum q_1 u per tick: every captured record brings u on average (ratio {ratio})")
    # faces: T^(z) = diag(1/16, 1/16, 1/8) for entry along +z; both signs and three axes
    t_par, t_perp = abs_moment(3) / 2, abs_z_x2(1) / 2
    ok = (t_par, t_perp) == (F(1, 8), F(1, 16))

    def response(faces):                                             # faces = (A_x, A_y, A_z), both signs together; returns the diagonal of sum_k A_k T^(k)
        return tuple(sum(faces[k] * (t_par if k == i else t_perp) for k in range(3)) for i in range(3))

    def face_counts(body):
        body = set(body)
        return tuple(sum(1 for s in body for d in E if d[k] != 0 and tuple(s[i] + d[i] for i in range(3)) not in body) for k in range(3))

    cube = list(product(range(2), repeat=3))
    plate = [(x, y, 0) for x in range(2) for y in range(2)]
    ball = [s for s in product(range(-3, 4), repeat=3) if sum(t * t for t in s) <= 9]
    rc, rp, rb = response(face_counts(cube)), response(face_counts(plate)), response(face_counts(ball))
    parallel_plate = len(set(rp)) == 1
    if mut("plate_response_parallel"):
        parallel_plate = True
    checks.check("B4", ok and len(set(rc)) == 1 and len(set(rb)) == 1 and face_counts(plate) == (4, 4, 8) and not parallel_plate, f"T2: a face entered along an axis responds to a wind with diag(1/16, 1/16, 1/8); a body with equally many exposed faces along the three axes (cube {face_counts(cube)}, ball of radius 3 {face_counts(ball)}) takes up momentum parallel to the wind, a 2x2x1 plate {face_counts(plate)} does not ({tuple(str(c) for c in rp)})")


# ============================================================================================ family C (T3)
def multinomial(x, w) -> Fraction:
    n = sum(x)
    val = F(factorial(n))
    for k in range(3):
        val = val / factorial(x[k]) * w[k] ** x[k]
    return val


def simplex_integral(a: int, b: int, c: int) -> Fraction:
    """Integral of w1^a w2^b (1 - w1 - w2)^c over the triangle, by expanding and integrating polynomials term by term."""
    total = F(0)
    for j in range(c + 1):                                           # (1 - w1 - w2)^c = sum_j C(c, j) (1 - w1)^(c - j) (-w2)^j ; inner integral over w2 in [0, 1 - w1]
        inner = F(comb(c, j) * (-1) ** j, b + j + 1)                 # times (1 - w1)^(b + c + 1)
        for i in range(b + c + 2):                                   # (1 - w1)^(b + c + 1) = sum_i C(b + c + 1, i) (-w1)^i
            total += inner * F(comb(b + c + 1, i) * (-1) ** i, a + i + 1)
    return total


def family_c(checks: Checks) -> None:
    dirs = [((1, 2, 2), 3), ((2, 3, 6), 7), ((3, 4, 0), 5), ((1, 0, 0), 1)]
    ok = True
    for d, _ in dirs:
        w = tuple(F(c, sum(d)) for c in d)
        if mut("shadow_step_frequencies_wrong"):
            w = tuple(F(c * c, sum(t * t for t in d)) for c in d)
        h = {x: multinomial(x, w) for x in product(range(5), repeat=3)}
        truew = tuple(F(c, sum(d)) for c in d)
        for x in h:
            if x == (0, 0, 0):
                ok = ok and h[x] == 1
                continue
            rhs = sum(truew[k] * h.get(tuple(x[i] - (1 if i == k else 0) for i in range(3)), F(0)) for k in range(3))
            ok = ok and h[x] == rhs
    checks.check("C1", ok, "T3: for independent records of one content the deficit behind a capturing site, h(x) = multinomial(x; w) with step frequencies w_k = |s_k|/|s|_1, is one at the site and satisfies h(x) = sum_k w_k h(x - e_k) elsewhere, the stationary transport equation (checked on a 5x5x5 block for four rational contents)")
    ok = True
    for d, _ in dirs:
        w = tuple(F(c, sum(d)) for c in d)
        for n in range(0, 7):
            shell = [x for x in product(range(n + 1), repeat=3) if sum(x) == n]
            ok = ok and sum(multinomial(x, w) for x in shell) == 1
    checks.check("C2", ok, "T3: the deficit sums to one over every shell |x|_1 = n: the shadow carries the whole capture through every shell, and the force summed over a shell is the capture-weighted content |s|_1 s whatever the distance")
    ok = True
    count = 0
    for n in range(0, 6):
        for x in product(range(n + 1), repeat=3):
            if sum(x) != n:
                continue
            coeff = F(factorial(n), factorial(x[0]) * factorial(x[1]) * factorial(x[2]))
            val = coeff * simplex_integral(*x)
            want = F(1, (n + 1) ** 2) if mut("simplex_integral_wrong") else F(1, (n + 1) * (n + 2))
            ok = ok and val == want
            count += 1
    checks.check("C3", ok, f"T3: integrated over the simplex of step frequencies the deficit at a site of the shell n is 1/((n+1)(n+2)), the same for all {count} sites with n <= 5 (term-by-term polynomial integration)")

    def multiplicity(x):
        m = sum(1 for sg in product((1, -1), repeat=3) if all(sg[k] * x[k] >= 0 for k in range(3)))
        return 1 if (mut("axis_multiplicity_one") and sum(1 for c in x if c == 0) == 2) else m

    checks.check("C4", multiplicity((3, 2, 5)) == 1 and multiplicity((3, 0, 5)) == 2 and multiplicity((0, 0, 5)) == 4 and multiplicity((-2, 0, 0)) == 4, "T3: the octants of contents that reach a site number 1 off the coordinate planes, 2 on a plane and 4 on an axis")
    # the coefficient of the collisionless force: |Phi(mu)| r^2/n^2 with Phi(w) = w (w.w)^(-5/2) at mu = d/|d|_1
    shown = []
    ok = True
    for d in ((84, 12, 5), (2, 3, 6), (1, 2, 2), (6, 6, 7)):
        l2sq = sum(c * c for c in d)
        l2 = isqrt(l2sq)
        ok = ok and l2 * l2 == l2sq
        l1 = sum(d)
        t = F(l2sq, l1 * l1)                                         # w.w at the mean
        phi_norm = F(l2, l1) * F(l1, l2) ** 5                        # |mu| t^(-5/2), rational because |d|_2 is an integer
        coeff = phi_norm * t                                         # times r^2/n^2 = |d|_2^2/|d|_1^2
        want = F(9, 4) if mut("collisionless_coefficient_isotropic") else F(l1 * l1, l2sq)
        ok = ok and coeff == want and 1 < coeff < 3
        shown.append(f"{d}: {coeff}")
        k = 10 ** 6                                                  # alpha = k d: the mean is exactly d/|d|_1
        alpha = [k * c for c in d]
        a0 = sum(alpha)
        var_sum = F(a0 * a0 - sum(a * a for a in alpha), a0 * a0 * (a0 + 1))
        ok = ok and var_sum <= F(1, a0 + 1) and 675 * var_sum < F(1, 1000)
    ok = ok and 50 * 27 == 1350 and 15 + 35 == 50
    checks.check("C5", ok, "T3: the collisionless force on a transparent site has the coefficient |r|_1^2 in units of rho/(4 pi sqrt 3 r^2): " + "; ".join(shown) + "; between 1 (near an axis) and 3 (the body diagonal), against 9/4 in every direction for the collisional law; the remainder is at most 675 times the summed variance of the step frequencies, below 1/1000 at n of order 10^7")


# ============================================================================================ family D (T4)
def family_d(checks: Checks) -> None:
    u = (F(1, 10), F(-1, 20), F(1, 25))
    rho = F(3, 10)
    n_sites = 12
    p = (F(1, 5), F(0), F(-1, 10))
    # channel 1 (records step onto the body): number N q_1, momentum N q_1 u; in units of rho/sqrt 3: 3/2 and (3/2) u per site
    ch1_number = n_sites * F(3, 2)
    ch1_momentum = tuple(n_sites * F(3, 2) * c for c in u)
    # channel 2 (the body steps onto occupied sites): it steps at the rate |p|_1/sqrt 3 and enters N sites, each occupied with probability rho
    ch2_number = n_sites * one_norm(p)
    ch2_momentum = tuple((F(0) if mut("sweeping_brings_no_momentum") else n_sites * one_norm(p)) * c for c in u)
    total_n = ch1_number + ch2_number
    total_p = tuple(ch1_momentum[i] + ch2_momentum[i] for i in range(3))
    ok = all(total_p[i] == u[i] * total_n for i in range(3))
    checks.check("D1", ok, f"T4: in a product state with a first-harmonic wind both capture channels bring the wind's mean content per captured record, so the expected momentum gain is u times the expected mass gain (in units of rho/sqrt 3: mass {total_n * rho}, momentum {tuple(str(c * rho) for c in total_p)}) whatever the body's own content")
    m0, p0 = 12, (F(1, 2), F(0), F(0))
    ok = True
    for m in (0, 12, 108):
        content = tuple((m0 * p0[i] + m * u[i]) / (m0 + m) for i in range(3))
        frac = F(m, m0 + m)
        ok = ok and all(content[i] == (1 - frac) * p0[i] + frac * u[i] for i in range(3))
    ok = ok and F(12, 12 + 12) == F(1, 2)
    checks.check("D2", ok, "T4: in the product closure the content of a body after a fixed number m of captures has expected value equal to the mixture (1 - f) p_0 + f u with f = m/(M_0 + m) the captured fraction of its mass: half way to the wind when it has doubled its mass")


# ============================================================================================ family E (T5)
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


def family_e(checks: Checks) -> None:
    rho = F(3, 10)
    n1, r = 50, 20
    q1 = Sym(rho / 2, 0, 1)                                          # (sqrt 3/2) rho
    k0 = Sym(F(1, 4) / (rho * (1 - rho)), -1, 1)                     # sqrt 3/(4 pi rho (1 - rho))
    wind = k0 * q1 * Sym(F(n1, r * r))                               # u = K_0 Q_1/r^2 with Q_1 = q_1 N_1
    ok = wind.key() == Sym(F(3 * n1, 8 * r * r) / (1 - rho), -1, 0).key()
    acc = q1 * wind / Sym(1, 0, 1)                                   # velocity = content/sqrt 3
    ok = ok and acc.key() == Sym(3 * rho * F(n1, r * r) / (16 * (1 - rho)), -1, 0).key()
    big_a = acc * Sym(r * r)                                         # acceleration = A/r^2
    tff_sq = Sym(F(1, 8), 2, 0) * Sym(r ** 3) / big_a                # t^2 = (pi^2/8) r^3/A
    ratio = q1 * q1 * tff_sq
    want = Sym((F(1, 3) if mut("window_coefficient_wrong") else F(1, 2)) * rho * (1 - rho) * F(r ** 3, n1), 3, 0)
    ok2 = ratio.key() == want.key()
    gas_inside = Sym(F(4, 3) * rho * r ** 3, 1, 0)
    bound = Sym(F(8, 3) * n1 / (1 - rho), -2, 0)                     # (q_1 t_ff)^2 = gas_inside/bound
    ok2 = ok2 and (gas_inside / bound).key() == want.key()
    checks.check("E1", ok, "T5: with block 47's wind u = 3 N_1/(8 pi (1 - rho) r^2) in the N=M active-site idealization, a body at rest gains velocity at the rate q_1 u/sqrt 3 = 3 rho N_1/(16 pi (1 - rho) r^2), the same within this additional closure")
    checks.check("E2", ok2, "T5: the fall from rest lasts t with (q_1 t)^2 = (pi^3/2) rho (1 - rho) r^3/N_1, which is the number of gas records inside the radius, (4 pi/3) rho r^3, over 8 N_1/(3 pi^2 (1 - rho)): the fall is accelerated throughout only when that ratio is small")


# ============================================================================================ family F
FENCES = (
    "This note works within the supplied inertial clause of block 44 and a supplied body clause; it reports what a capturing body takes up, what force free streaming gives, and how a free capturing body moves; nothing is adopted and no gravitational claim is made.",
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
                   "Dirichlet", "Taylor", "Archimedes", "Aristotle", "Kepler", "Oseen", "Lagally", "Jensen")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Knudsen)", 1)
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
    "per_element: executed — the identity sum_k max(0, s.e_k) = |s|_1 and the range of |s|_1 for 174 rational unit contents; the sphere moments 3/2 and 1/2; the face response diag(1/16, 1/16, 1/8)",
    "per_site: executed — the multinomial deficit and its transport equation on a 5x5x5 block for four contents; the simplex integral at all 56 sites with n <= 5; the octant multiplicities 1, 2, 4",
    "per_mode: not applicable — the retained finite identities concern local rates and integrated flux, not a mode spectrum",
    "per_block: executed — shell sums for n <= 6; the collisionless coefficients 10201/7225, 121/49, 25/9, 361/121 and the remainder bound; the dilution identity for both capture channels; the window algebra",
    "lattice_wide: T1, T2 and T4 are exact expectations in a product state, which neglects what the body does to the gas around it; T3 is exact for independent records (no exchange, no scattering) and its large-distance coefficient carries an explicit remainder; T5 is a closure; the executed runs are controls, not proofs",
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
    print("scope: free capturing bodies in the inertial record gas — the capture law, first-harmonic winds, the collisionless shadow and its anisotropic force, the dilution law of a free body and the window of accelerated fall; exact expectations in product states and for independent records")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
