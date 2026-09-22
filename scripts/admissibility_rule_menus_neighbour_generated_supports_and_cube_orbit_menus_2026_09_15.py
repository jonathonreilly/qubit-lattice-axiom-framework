#!/usr/bin/env python3
"""Exact finite controls for covariant frames, cube-orbit examples,
supplied antipodal sign patterns, and aligned/tilted overlap evaluations.
Authority and prose predicates are distinct from mathematical controls.
No exhaustive support/minimality or physical probability selection is certified.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_COVARIANT_FRAME_CONSTRUCTIONS_CUBE_ORBITS_AND_ANTIPODAL_KERNEL_PROPAGATION_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_covariant_frame_constructions_cube_orbits_and_antipodal_kernel_propagation_bounded_theorem_note_2026-09-15"
PARENT_CLAIM_ID = "possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14"
PARENT_FRAGMENT = "Empty-neighbourhood sphere laws"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "No possibility is privileged.",
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
)

MUTATION_GATE = {
    "rotation_orbit_finite_claimed": "B",
    "frame_not_equivariant_claimed": "B",
    "orbit_sizes_wrong": "C",
    "mixed_set_invariant_claimed": "C",
    "record_off_seed_axis_claimed": "D",
    "aligned_overlap_values_corrupted": "D",
    "finite_menu_unsoldered_claimed": "F",
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
        self.failed_families: list[str] = []

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        if not ok:
            self.failed_families.append(label[0])
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize_text(text: str) -> str:
    return " ".join(text.split())


F = Fraction


def rotations():
    mats = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            Mx = [[0] * 3 for _ in range(3)]
            for i in range(3):
                Mx[perm[i]][i] = signs[i]
            if sp.Matrix(Mx).det() == 1:
                mats.append(tuple(tuple(r) for r in Mx))
    return mats


def apply(Mx, v):
    return tuple(sum(Mx[i][j] * v[j] for j in range(3)) for i in range(3))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, parent = texts
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 3,
                 "the three declared inputs exist (this note, the axiom memo, the possibility-covariance note on main)")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the five axiom sentences used are present verbatim in the axiom memo")
    fp = normalize_text(parent)
    checks.check("A3", PARENT_CLAIM_ID in fp and PARENT_FRAGMENT in fp, "the parent's claim id and its empty-neighbourhood sphere-law section are present")
    flat = normalize_text(note)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    c, s_ = sp.Rational(3, 5), sp.Rational(4, 5)
    Rz = sp.Matrix([[c, -s_, 0], [s_, c, 0], [0, 0, 1]])
    pt = sp.Matrix([sp.Rational(3, 5), 0, sp.Rational(4, 5)])
    seen = set()
    cur = pt
    for _ in range(12):
        seen.add(tuple(cur))
        cur = Rz * cur
    pole_fixed = Rz * sp.Matrix([0, 0, 1]) == sp.Matrix([0, 0, 1])
    unit = sp.simplify(pt.dot(pt)) == 1 and sp.simplify((Rz.T * Rz - sp.eye(3))) == sp.zeros(3, 3)
    ok = len(seen) == 12 and pole_fixed and unit
    if mut("rotation_orbit_finite_claimed"):
        ok = len(seen) == 1
    checks.check("B1", ok, "M1: a rational rotation about the pole (cosine 3/5) fixes the pole and moves the unit point (3/5, 0, 4/5) through 12 distinct positions in 12 steps; this finite witness is not an infinite-orbit proof")
    q1 = sp.Matrix([1, 0, 0])
    q2 = sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5), 0])
    def frame(a, b):
        e1 = a
        e2 = b - (a.dot(b)) * a
        e2 = e2 / sp.sqrt(e2.dot(e2))
        return sp.Matrix.hstack(e1, e2, e1.cross(e2))
    g = sp.Matrix([[c, 0, s_], [0, 1, 0], [-s_, 0, c]])
    ok2 = sp.simplify(frame(g * q1, g * q2) - g * frame(q1, q2)) == sp.zeros(3, 3) and sp.simplify(frame(q1, q2).T * frame(q1, q2) - sp.eye(3)) == sp.zeros(3, 3)
    t = q1.dot(q2)
    displayed = sp.Matrix.hstack(q1, (q2 - t*q1)/sp.sqrt(1-t*t), q1.cross(q2)/sp.sqrt(1-t*t))
    ok2 = ok2 and sp.simplify(displayed-frame(q1,q2)) == sp.zeros(3,3) and displayed.det() == 1
    if mut("frame_not_equivariant_claimed"):
        ok2 = not ok2
    checks.check("B2", ok2, "M2: the frame F(q_1, q_2) is a rotation matrix and F(g q_1, g q_2) = g F(q_1, q_2) for a rational rotation about y")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    R = rotations()
    samples = {"axis": (1, 0, 0), "diagonal": (1, 1, 1), "edge": (1, 1, 0), "generic": (1, 2, 3), "mirror-plane generic": (1, 1, 2)}
    sizes = {}
    stabs = {}
    for name, v in samples.items():
        sizes[name] = len({apply(Mx, v) for Mx in R})
        stabs[name] = sum(1 for Mx in R if apply(Mx, v) == v)
    expected = {"axis": (6, 4), "diagonal": (8, 3), "edge": (12, 2), "generic": (24, 1), "mirror-plane generic": (24, 1)}
    if mut("orbit_sizes_wrong"):
        expected["edge"] = (8, 3)
    ok = len(R) == 24 and all((sizes[k], stabs[k]) == expected[k] for k in samples) and all(sizes[k] * stabs[k] == 24 for k in samples)
    checks.check("C1", ok, "M3: the 24 proper rotations of the cube; orbit sizes and stabilizer orders (6,4), (8,3), (12,2), (24,1), (24,1) for the axis, diagonal, edge, generic and mirror-plane sample directions; size times stabilizer = 24")
    axes = {apply(Mx, (1, 0, 0)) for Mx in R}
    diags = {apply(Mx, (1, 1, 1)) for Mx in R}
    edges = {apply(Mx, (1, 1, 0)) for Mx in R}
    def invariant(S):
        return all(apply(Mx, v) in S for Mx in R for v in S)
    mixed = set(list(axes)[:3]) | {(1, 1, 1)}
    inv_ok = invariant(axes) and invariant(diags) and invariant(edges) and invariant(axes | diags) and not invariant(mixed)
    if mut("mixed_set_invariant_claimed"):
        inv_ok = invariant(mixed)
    checks.check("C2", inv_ok and len(axes) == 6 and len(diags) == 8 and len(edges) == 12, "M3: the six axes, the eight diagonals, the twelve edge directions and their unions are invariant; three axes plus one diagonal are not")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
    seed = sp.Matrix([s1, s2, s3])
    # the antipodal support: each site after the first takes +seed or -seed; enumerate all 2^5 patterns of a path of five
    on_axis = True
    for pat in product((1, -1), repeat=5):
        for sign in pat:
            v = sign * seed
            on_axis = on_axis and (sp.simplify(v.cross(seed)) == sp.zeros(3, 1))
    if mut("record_off_seed_axis_claimed"):
        on_axis = False
    checks.check("D1", on_axis, "M4: on a path of five with the antipodal support every record is +/- the symbolic seed (32 patterns), i.e. on the seed's axis")
    t = sp.symbols("t")
    f = (1 + t) / 2
    born = (f.subs(t, 1), f.subs(t, -1))
    tilted = (f.subs(t, sp.Rational(3, 5)), f.subs(t, -sp.Rational(3, 5)))
    ok = born == (1, 0) and tilted == (sp.Rational(4, 5), sp.Rational(1, 5))
    if mut("aligned_overlap_values_corrupted"):
        ok = born == (sp.Rational(1, 2), sp.Rational(1, 2))
    checks.check("D2", ok, "M5: the supplied overlap gives aligned values 1,0 and tilted values 4/5,1/5; it does not choose record probabilities")


# ============================================================================================ family F
FENCES = ('This note retains covariant constructions and finite witnesses; exhaustive support classification and minimality certification are deferred, and no menu, kernel, covariance reading or physical probability law is selected.', 'No plane, bridge, Born-weight or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'The sphere, reference supports and weights, formation order and overlap function are explicitly supplied mathematical inputs.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical menu", "for every coupling", "selects the", "fires wake condition", "the Bridge weights",
    "the Bridge conjecture", "certified", "converge", "emergent", "washes out", "toward the plane", "the trend", "a finite site-independent menu is covariant under the unsoldered reading",
)
CLAIM_INJECTIONS = {"finite_menu_unsoldered_claimed": "Hence a finite site-independent menu is covariant under the unsoldered reading."}
CLASSICAL_NAMES = ("Klein", "Toom", "Peierls", "Fourier", "Dobrushin", "Kolmogorov", "Gillespie", "Eden", "Haar")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    flat = normalize_text(text)
    checks.check("F1", all(f in flat for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    numeric = "N" + "("  # float-scan-marker-line
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln]
    checks.check("F3", not bad and len(scan) > 150, f"runner source: no floating-point literal or conversion call ({len(bad)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for i, sec in enumerate(sections):
        title = sec.splitlines()[0].strip() if i > 0 else "(front matter)"
        body = sec
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem M3"):
            body = body + " (Klein's classification)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the classical names appear only under Prior art, Imports and the Premises' file citation ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — a rational rotation's twelve-point orbit; the frame's equivariance; the 24 rotations; the Born values",
    "per_site: executed — the five sample directions' orbits and stabilizers",
    "per_mode: executed — the invariance of the axis, diagonal and edge sets and of a union; the non-invariance of a mixed set",
    "per_block: executed — the path of five with the antipodal support and a symbolic seed",
    "lattice_wide: checked and not executed — finite algebra controls and supplied-kernel induction; no whole-lattice process or exhaustive support certification",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5 and all(len(l) >= 40 for l in N5_LINES), "the five N5 resolution lines are printed")


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
    checks = Checks()
    texts = [(ROOT / pth).read_text(encoding="utf-8") if (ROOT / pth).is_file() else "" for pth in AUDIT_INPUT_PATHS]
    print("AUDIT_INPUT_PATHS:")
    for pth in AUDIT_INPUT_PATHS:
        print(f"  {pth}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: supplied covariant frames, five cube-orbit examples, antipodal symbolic patterns, aligned and tilted overlap values; exhaustive classification deferred")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
