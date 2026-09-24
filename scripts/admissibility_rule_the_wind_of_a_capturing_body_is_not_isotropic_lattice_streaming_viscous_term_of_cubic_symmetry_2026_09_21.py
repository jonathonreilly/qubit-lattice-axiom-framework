#!/usr/bin/env python3
"""Exact checks: the wind of a capturing body is not isotropic (block 44's inertial clause, sphere menu; supplied, not adopted).

T1: a record of content s steps to x + sign(s_k) e_k at the rate |s_k|/sqrt 3; on a field that is a polynomial of degree two in the site the
streaming operator is exactly (1/sqrt 3) [ -s.grad + (1/2) sum_k |s_k| d_k^2 ].  T2: over the uniform sphere <|s_k|> = 1/2, <s_i^2 |s_i|> = 1/4,
<s_i^2 |s_k|> = 1/8 for k different from i, mixed moments vanish; so in local equilibrium (content law (1 + 3 u.s)/(4 pi)) the second-order
term gives the number equation D_lat Laplacian n with D_lat = 1/(4 sqrt 3) and the momentum equation nu_lat (Laplacian g_i + d_i^2 g_i) with
nu_lat = sqrt 3/16: the second part has cubic symmetry only, and its coefficient equals the isotropic one.  T3: for a harmonic potential chi the
field (d_x^3 chi, d_y^3 chi, d_z^3 chi) is in general not a gradient (its curl is 240 y for chi = x^5 - 10 x^3 y^2 + 5 x y^4, and non-zero for
chi = 1/r at (1, 2, 2)), so pressure cannot balance it and the potential inflow does not solve the creeping equations.  T4: in Fourier space
the creeping inflow towards a sink is g_i = -i k_i P/(k^2 + eta k_i^2), P = S / sum_i k_i^2/(k^2 + eta k_i^2): it satisfies both equations,
is homogeneous of degree -1 (so the inflow is f(direction)/r^2 at every distance) and has k x g different from zero unless eta = 0.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import random
import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_WIND_OF_A_CAPTURING_BODY_IS_NOT_ISOTROPIC_LATTICE_STREAMING_GIVES_A_VISCOUS_TERM_OF_CUBIC_SYMMETRY_DIRECTION_DEPENDENCE_DOES_NOT_DECAY_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_wind_of_a_capturing_body_is_not_isotropic_lattice_streaming_gives_a_viscous_term_of_cubic_symmetry_direction_dependence_does_not_decay_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = ("A site never carries more than one record; records are permanent.",)

MUTATION_GATE = {
    "second_order_term_without_half": "B",
    "fourth_moment_isotropic": "C",
    "lattice_viscosity_coefficient_wrong": "C",
    "cubic_term_is_a_gradient": "D",
    "inflow_is_potential_flow": "E",
    "inflow_not_homogeneous": "E",
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


def unit_contents():
    out = set()
    for d, length in (((1, 0, 0), 1), ((3, 4, 0), 5), ((1, 2, 2), 3), ((2, 3, 6), 7), ((1, 4, 8), 9)):
        for perm in set(product(range(3), repeat=3)):
            if sorted(perm) != [0, 1, 2]:
                continue
            for sg in product((1, -1), repeat=3):
                out.add(tuple(F(sg[i] * d[perm[i]], length) for i in range(3)))
    return sorted(out)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the sentence used")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    rng = random.Random(51)
    ok = True
    count = 0
    for s in unit_contents():
        a0 = F(rng.randint(-5, 5))
        b = [F(rng.randint(-5, 5), rng.randint(1, 4)) for _ in range(3)]
        m = [[F(rng.randint(-4, 4), rng.randint(1, 3)) for _ in range(3)] for _ in range(3)]
        m = [[(m[i][j] + m[j][i]) / 2 for j in range(3)] for i in range(3)]

        def field(x):
            return a0 + sum(b[i] * x[i] for i in range(3)) + sum(m[i][j] * x[i] * x[j] for i in range(3) for j in range(3))

        x = tuple(F(rng.randint(-3, 3)) for _ in range(3))
        # the record now at x came from x - sign(s_k) e_k: gain minus loss, in units of 1/sqrt 3
        stream = F(0)
        for k in range(3):
            if s[k] == 0:
                continue
            sg = 1 if s[k] > 0 else -1
            prev = tuple(x[i] - (sg if i == k else 0) for i in range(3))
            stream += abs(s[k]) * (field(prev) - field(x))
        grad = [b[i] + 2 * sum(m[i][j] * x[j] for j in range(3)) for i in range(3)]
        half = F(1) if mut("second_order_term_without_half") else F(1, 2)
        expansion = -sum(s[i] * grad[i] for i in range(3)) + half * sum(abs(s[k]) * 2 * m[k][k] for k in range(3))
        ok = ok and stream == expansion
        count += 1
    checks.check("B1", ok, f"T1: on a field of degree two the streaming operator of a record of content s is exactly (1/sqrt 3)[-s.grad + (1/2) sum_k |s_k| d_k^2] ({count} rational unit contents, random rational fields and sites)")


# ============================================================================================ family C (T2)
def abs_moment(a: int) -> Fraction:
    """<|z|^a> over the uniform sphere: z is uniform on [-1, 1]."""
    return F(1, a + 1)


def family_c(checks: Checks) -> None:
    first = abs_moment(1)                                            # <|s_k|>
    same = abs_moment(3)                                             # <s_i^2 |s_i|>
    other = (abs_moment(1) - abs_moment(3)) / 2                      # <s_i^2 |s_k|>, k != i: given z, x^2 averages (1 - z^2)/2
    if mut("fourth_moment_isotropic"):
        same = other
    ok = first == F(1, 2) and same == F(1, 4) and other == F(1, 8)
    # the three moments sum to <|s_k|> (since s.s = 1): 1/4 + 1/8 + 1/8 = 1/2
    ok = ok and same + 2 * other == first
    checks.check("C1", ok, f"T2: over the uniform sphere <|s_k|> = {first}, <s_i^2 |s_i|> = {same}, <s_i^2 |s_k|> = {other} for k different from i (and they add up to <|s_k|>); moments with an odd power of a coordinate vanish by reflection")
    # local equilibrium: momentum equation term (1/(2 sqrt 3)) * 3 * [other * Laplacian g_i + (same - other) d_i^2 g_i]
    iso_sq = (F(3, 2) * other) ** 2 / 3                              # nu_lat^2 with nu_lat = (3/2) other / sqrt 3
    cub_sq = (F(3, 2) * (same - other)) ** 2 / 3
    dlat_sq = (first / 2) ** 2 / 3
    want = F(3, 128) if mut("lattice_viscosity_coefficient_wrong") else F(3, 256)
    ok = iso_sq == want and cub_sq == iso_sq and dlat_sq == F(1, 48)
    checks.check("C2", ok, f"T2: in local equilibrium the second-order streaming term gives the momentum equation nu_lat (Laplacian g_i + d_i^2 g_i) with nu_lat = sqrt 3/16 (nu_lat^2 = {iso_sq}), the part of cubic symmetry having the same coefficient as the isotropic part, and the number equation D_lat Laplacian n with D_lat = 1/(4 sqrt 3) (D_lat^2 = {dlat_sq})")

    # the damping of a longitudinal wave along the unit vector n under nu_lat (Laplacian g_i + d_i^2 g_i) is nu_lat q^2 (1 + sum_i n_i^4)
    vals = []
    for d in ((1, 0, 0), (1, 1, 0), (1, 1, 1)):
        n2 = sum(c * c for c in d)
        vals.append(1 + F(sum(c ** 4 for c in d), n2 * n2))
    if mut("fourth_moment_isotropic"):
        vals = [vals[0]] * 3
    checks.check("C3", vals == [F(2), F(3, 2), F(4, 3)], f"T2: a longitudinal wave is damped at the rate nu_lat q^2 times {', '.join(str(v) for v in vals)} along an axis, a face diagonal and a body diagonal; an isotropic viscous operator damps it equally in every direction")


# ============================================================================================ family D (T3)
def poly_diff(p, var):
    out = {}
    for mono, c in p.items():
        if mono[var] == 0:
            continue
        new = list(mono)
        new[var] -= 1
        out[tuple(new)] = out.get(tuple(new), 0) + c * mono[var]
    return out


def poly_mul(p, q):
    out = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            mono = tuple(m1[i] + m2[i] for i in range(3))
            out[mono] = out.get(mono, 0) + c1 * c2
    return out


def poly_add(p, q, sign=1):
    out = dict(p)
    for mono, c in q.items():
        out[mono] = out.get(mono, 0) + sign * c
    return {mono: c for mono, c in out.items() if c != 0}


def poly_eval(p, x):
    return sum(c * x[0] ** m[0] * x[1] ** m[1] * x[2] ** m[2] for m, c in p.items())


R2 = {(2, 0, 0): 1, (0, 2, 0): 1, (0, 0, 2): 1}
XI = [{(1, 0, 0): 1}, {(0, 1, 0): 1}, {(0, 0, 1): 1}]


def radial_diff(num, power, var):
    """d/dx_var of num / r^power = (r^2 d num - power x_var num) / r^(power + 2)."""
    return poly_add(poly_mul(R2, poly_diff(num, var)), {m: power * c for m, c in poly_mul(XI[var], num).items()}, sign=-1), power + 2


def family_d(checks: Checks) -> None:
    # a harmonic polynomial of degree five
    chi = {(5, 0, 0): 1, (3, 2, 0): -10, (1, 4, 0): 5}
    lap = {}
    for v in range(3):
        lap = poly_add(lap, poly_diff(poly_diff(chi, v), v))
    third = [poly_diff(poly_diff(poly_diff(chi, v), v), v) for v in range(3)]
    curl_z = poly_add(poly_diff(third[1], 0), poly_diff(third[0], 1), sign=-1)
    ok = lap == {} and curl_z == {(0, 1, 0): 240}
    # chi = 1/r at the point (1, 2, 2), where r = 3
    third_r = []
    for v in range(3):
        num, power = {(0, 0, 0): 1}, 1
        for _ in range(3):
            num, power = radial_diff(num, power, v)
        third_r.append((num, power))
    n_yx, p_yx = radial_diff(*third_r[1], 0)                          # d_x (d_y^3 1/r)
    n_xy, p_xy = radial_diff(*third_r[0], 1)                          # d_y (d_x^3 1/r)
    point = (1, 2, 2)
    curl_val = F(poly_eval(n_yx, point), 3 ** p_yx) - F(poly_eval(n_xy, point), 3 ** p_xy)
    if mut("cubic_term_is_a_gradient"):
        curl_val = F(0)
    ok = ok and p_yx == p_xy == 9 and curl_val == F(70,2187)
    checks.check("D1", ok, f"T3: for the harmonic potential x^5 - 10 x^3 y^2 + 5 x y^4 the field (d_x^3, d_y^3, d_z^3) chi has the curl 240 y along z; for chi = 1/r its curl along z at (1, 2, 2) is {curl_val}: the part of cubic symmetry acting on a potential flow is not a gradient, so pressure cannot balance it and the potential inflow does not solve the creeping equations")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    ok_eq = True
    ok_hom = True
    ok_curl = True
    shown = []
    for eta in (F(0), F(1, 2), F(1)):
        for k in ((1, 2, 0), (1, 2, 3), (2, -1, 5), (1, 1, 1), (1, 0, 0)):
            kv = [F(c) for c in k]

            def solve(kvec):
                k2 = sum(c * c for c in kvec)
                den = [k2 + eta * c * c for c in kvec]
                s = sum(kvec[i] * kvec[i] / den[i] for i in range(3))
                p_hat = -1 / s                                       # unit sink
                return [kvec[i] * p_hat / den[i] for i in range(3)], p_hat, den   # g_i = -i * (returned value)

            g, p_hat, den = solve(kv)
            ok_eq = ok_eq and sum(kv[i] * g[i] for i in range(3)) == -1 and all(kv[i] * p_hat - den[i] * g[i] == 0 for i in range(3))
            lam = F(7, 3)
            g2, _, _ = solve([lam * c for c in kv])
            scale = F(1) if mut("inflow_not_homogeneous") else lam
            ok_hom = ok_hom and all(g2[i] * scale == g[i] for i in range(3))
            cross = [kv[1] * g[2] - kv[2] * g[1], kv[2] * g[0] - kv[0] * g[2], kv[0] * g[1] - kv[1] * g[0]]
            vortical = any(c != 0 for c in cross)
            generic = len({abs(c) for c in k if c != 0}) > 1
            want = (eta != 0 and generic) and not mut("inflow_is_potential_flow")
            ok_curl = ok_curl and vortical == want
            if eta == F(1, 2) and k == (1, 2, 0):
                shown.append(f"eta = 1/2, k = (1, 2, 0): g = -i {tuple(str(c) for c in g)}, k x g = -i {tuple(str(c) for c in cross)}")
    checks.check("E1", ok_eq, "T4: g_i = -i k_i P/(k^2 + eta k_i^2) with P = -S/sum_i k_i^2/(k^2 + eta k_i^2) satisfies the divergence condition and the creeping momentum equation exactly (three values of eta, five wave vectors)")
    checks.check("E2", ok_hom, "T4: the solution is homogeneous of degree -1 in the wave vector, so the inflow towards a sink is a function of direction over r^2: its dependence on direction does not decay with distance")
    checks.check("E3", ok_curl, "T4: k x g vanishes for eta = 0 (potential flow) and along the symmetry directions, and is non-zero at generic wave vectors for eta > 0: the creeping inflow has circulation (" + "; ".join(shown) + ")")


# ============================================================================================ family F
FENCES = (
    "This note works within the supplied inertial clause of block 44; it reports that the streaming of records along lattice axes gives the gas a viscous term of cubic symmetry and what that does to the wind of a capturing body; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Navier", "Stokes", "Bernoulli", "Bjerknes", "Sage", "Boltzmann", "Gibbs", "Laplace", "Poisson", "Gauss", "Knudsen", "Einstein", "Planck", "Fourier", "Taylor", "Reynolds", "Chapman", "Enskog",
                   "Frisch", "Hasslacher", "Pomeau", "Hardy", "Pazzis", "Archimedes", "Helmholtz", "Hodge", "Oseen")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Stokes)", 1)
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
    "per_element: executed — the streaming operator on fields of degree two for 150 rational unit contents; the sphere moments 1/2, 1/4, 1/8",
    "per_site: not applicable — the retained calculation is a continuum gradient expansion, not a sitewise microscopic evolution theorem",
    "per_mode: executed — the creeping solution at five wave vectors and three values of eta: both equations, homogeneity of degree -1, k x g",
    "per_block: executed — nu_lat^2 = 3/256 for both parts, D_lat^2 = 1/48; the curl 240 y for a harmonic polynomial of degree five and the curl of the cubic term for 1/r at (1, 2, 2)",
    "lattice_wide: T1 is exact on fields of degree two and is the second-order term of an expansion in gradients otherwise; T2 is a statement in local equilibrium at small density; T3 and T4 are exact statements about the creeping equations with a term of cubic symmetry; the winds by direction and the angular function are executed controls, not proofs",
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
    print("scope: the wind of a capturing body in the inertial record gas is not isotropic — the second-order streaming term, its sphere moments, the lattice viscosity of cubic symmetry, the failure of the potential inflow, and the creeping solution with its direction dependence at every distance")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
