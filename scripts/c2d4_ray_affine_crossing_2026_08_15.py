#!/usr/bin/env python3
"""Exact checks for the displayed c2d4 same-k affine-crossing theorems.

Arithmetic is performed on the displayed six-row table only. No path search
is executed and no cache is written.
"""

from __future__ import annotations

import ast
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/C2D4_RAY_AFFINE_CROSSING_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/C2D4_RAY_AFFINE_CROSSING_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

# Displayed c2d4 same-k table (computed lattice input; not adopted).
DISPLAYED_TABLE = (
    (14, 30, 46),
    (15, 31, 49),
    (16, 32, 52),
    (17, 33, 55),
    (18, 34, 58),
    (19, 35, 61),
)

N5_LINES = (
    "per_element: each displayed same-k row is checked against the affine forms and the reverse quadratic comparison",
    "per_site: checked and not executed — no site-wise path search is performed",
    "per_mode: checked and not executed — no spectral or harmonic mode is asserted",
    "per_block: intercept extras with locked slopes (1,3) are checked as a family through the leading -6 k^2 coefficient",
    "lattice_wide: checked and not executed — no lattice-wide search or path listing is claimed",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def reverse_holds(t_axis: int, t_body: int) -> bool:
    return 3 * t_axis * t_axis > t_body * t_body


def reverse_polynomial(beta: int, delta: int, k: int) -> int:
    return -6 * k * k + 6 * (beta - delta) * k + (3 * beta * beta - delta * delta)


def first_failure_after(k_star: sp.Expr, beta: int, delta: int) -> int:
    start = int(sp.floor(k_star)) + 1
    k = start
    while reverse_polynomial(beta, delta, k) > 0:
        k += 1
        if k > start + 10_000:
            raise RuntimeError("locked-slope extra did not fail reverse")
    return k


def literal_audit_paths(source: str) -> tuple[str, ...] | None:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue
        if node.targets[0].id != "AUDIT_INPUT_PATHS":
            continue
        try:
            value = ast.literal_eval(node.value)
        except (ValueError, TypeError):
            return None
        if isinstance(value, tuple) and all(isinstance(item, str) for item in value):
            return value
        return None
    return None


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    runner_source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: displayed six-row c2d4 same-k table only; "
        "no fitted, observational, or literature values are used"
    )
    print("measure_boundary: exact integer and radical algebra on the displayed table")
    print("negative_scope: locked-slope intercept extras cannot restore all-k reverse")

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the source note and current minimal axioms",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        AUDIT_INPUT_PATHS,
    )
    checks.check(
        "audit-input-literal",
        "AUDIT_INPUT_PATHS is a static tuple of path literals",
        literal_audit_paths(runner_source) == AUDIT_INPUT_PATHS,
        literal_audit_paths(runner_source),
    )

    ks = tuple(row[0] for row in DISPLAYED_TABLE)
    t_axis = tuple(row[1] for row in DISPLAYED_TABLE)
    t_body = tuple(row[2] for row in DISPLAYED_TABLE)
    d_k = tuple(ks[index + 1] - ks[index] for index in range(len(ks) - 1))
    d_axis = tuple(t_axis[index + 1] - t_axis[index] for index in range(len(t_axis) - 1))
    d_body = tuple(t_body[index + 1] - t_body[index] for index in range(len(t_body) - 1))

    checks.check(
        "first-diff-k",
        "consecutive displayed k values increase by 1",
        d_k == (1,) * (len(ks) - 1),
        d_k,
    )
    checks.check(
        "first-diff-axis",
        "consecutive first differences of t_axis are 1",
        d_axis == (1,) * (len(t_axis) - 1),
        d_axis,
    )
    checks.check(
        "first-diff-body",
        "consecutive first differences of t_body are 3",
        d_body == (3,) * (len(t_body) - 1),
        d_body,
    )

    alpha = d_axis[0] // d_k[0]
    gamma = d_body[0] // d_k[0]
    betas = tuple(axis - alpha * k for k, axis in zip(ks, t_axis))
    deltas = tuple(body - gamma * k for k, body in zip(ks, t_body))
    beta = betas[0]
    delta = deltas[0]
    checks.check(
        "locked-slopes",
        "the displayed table has locked slopes (alpha,gamma)=(1,3)",
        alpha == 1 and gamma == 3,
        (alpha, gamma),
    )
    checks.check(
        "constant-intercepts",
        "axis and body intercepts extracted from every row are constant",
        all(value == betas[0] for value in betas)
        and all(value == deltas[0] for value in deltas),
        (betas, deltas),
    )
    checks.check(
        "affine-recovery",
        "every displayed row equals t_axis=k+16 and t_body=3k+4",
        beta == 16
        and delta == 4
        and all(
            axis == k + beta and body == 3 * k + delta
            for k, axis, body in DISPLAYED_TABLE
        ),
        (beta, delta),
    )

    k = sp.symbols("k")
    sqrt3 = sp.sqrt(3)
    reverse_poly = sp.expand(3 * (k + beta) ** 2 - (3 * k + delta) ** 2)
    roots = sp.solve(sp.Eq(reverse_poly, 0), k)
    positive_roots = [root for root in roots if sp.simplify(root) > 0]
    k_star = sp.simplify(positive_roots[0]) if len(positive_roots) == 1 else None
    closed = sp.simplify((sqrt3 * beta - delta) / (3 - sqrt3))
    simplified = sp.simplify(6 + 22 * sqrt3 / 3)
    checks.check(
        "crossing-closed-form",
        "the unique positive reverse crossing equals (sqrt(3)*16-4)/(3-sqrt(3))",
        k_star is not None and sp.simplify(k_star - closed) == 0,
        (k_star, closed),
    )
    checks.check(
        "crossing-simplified",
        "that crossing equals 6+22*sqrt(3)/3",
        k_star is not None and sp.simplify(k_star - simplified) == 0,
        (k_star, simplified),
    )
    checks.check(
        "unique-positive-root",
        "the quadratic has exactly one positive root and one negative root",
        len(roots) == 2
        and len(positive_roots) == 1
        and sum(1 for root in roots if sp.simplify(root) < 0) == 1,
        roots,
    )
    k_star_float = float(sp.N(k_star, 20)) if k_star is not None else None
    checks.check(
        "crossing-decimal",
        "k_* is approximately 18.7017 and lies strictly between 18 and 19",
        k_star_float is not None
        and abs(k_star_float - 18.7017) < 5.0e-5
        and 18 < k_star_float < 19,
        k_star_float,
    )

    axis_18 = 18 + beta
    body_18 = 3 * 18 + delta
    axis_19 = 19 + beta
    body_19 = 3 * 19 + delta
    left_18 = 3 * axis_18 * axis_18
    right_18 = body_18 * body_18
    left_19 = 3 * axis_19 * axis_19
    right_19 = body_19 * body_19
    checks.check(
        "reverse-k18",
        "reverse holds at k=18 by 3*34^2=3468>58^2=3364",
        axis_18 == 34
        and body_18 == 58
        and left_18 == 3468
        and right_18 == 3364
        and reverse_holds(axis_18, body_18)
        and (18, axis_18, body_18) in DISPLAYED_TABLE,
        (left_18, right_18),
    )
    checks.check(
        "reverse-k19",
        "reverse fails at k=19 by 3*35^2=3675<61^2=3721",
        axis_19 == 35
        and body_19 == 61
        and left_19 == 3675
        and right_19 == 3721
        and not reverse_holds(axis_19, body_19)
        and (19, axis_19, body_19) in DISPLAYED_TABLE,
        (left_19, right_19),
    )

    extra_beta, extra_delta = sp.symbols("beta delta")
    extra_poly = sp.expand(
        3 * (k + extra_beta) ** 2 - (3 * k + extra_delta) ** 2
    )
    leading = extra_poly.coeff(k, 2)
    checks.check(
        "intercept-extra-leading",
        "every locked-slope intercept extra has reverse leading coefficient -6",
        sp.simplify(leading + 6) == 0,
        leading,
    )

    extras = (
        (beta, delta),
        (beta + 1, delta),
        (beta, delta - 1),
        (0, 0),
        (100, 0),
        (beta, -10),
    )
    extra_failures = []
    extra_all_after = True
    for extra in extras:
        failure = first_failure_after(k_star, extra[0], extra[1])
        extra_failures.append((extra, failure, reverse_polynomial(*extra, failure)))
        if failure <= float(k_star) or reverse_polynomial(*extra, failure) > 0:
            extra_all_after = False
        # infinitely many later integers also fail once the leading term dominates
        later = failure + 5
        if reverse_polynomial(*extra, later) >= 0:
            extra_all_after = False
    checks.check(
        "intercept-extra-all-k",
        "no tested intercept extra restores reverse for all integers k>k_*",
        extra_all_after and all(poly < 0 for _, _, poly in extra_failures),
        extra_failures,
    )
    failure_100 = first_failure_after(k_star, 100, 0)
    checks.check(
        "intercept-extra-postponement",
        "a large axis intercept can hold reverse at k=19 but still fails later",
        reverse_holds(19 + 100, 3 * 19 + 0)
        and failure_100 > 19
        and not reverse_holds(failure_100 + 100, 3 * failure_100),
        failure_100,
    )

    lattice_quote = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    checks.check(
        "source-lattice",
        "current minimal axioms still supply the cubic lattice sentence",
        lattice_quote in normalize(axiom),
    )
    required_note_phrases = (
        "Displayed, not adopted",
        "Do not write into Admissibility",
        "Uniqueness of any underlying hop realization is not required",
        "Δ t_axis=1",
        "Δ t_body=3",
        "t_axis=k+16",
        "t_body=3k+4",
        "k_* = (√3 · 16 - 4) / (3 - √3) = 6 + 22√3 / 3 ≈ 18.7017.",
        "3 · 34^2 = 3468 > 58^2 = 3364",
        "3 · 35^2 = 3675 < 61^2 = 3721",
        "claim_type: bounded_theorem",
        "actual_current_surface_status: bounded-support",
        "hypothetical_axiom_status: \"no edit\"",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "FAIL / DO NOT SHIP",
        "authors no audit verdict",
    )
    missing = [phrase for phrase in required_note_phrases if phrase not in note and phrase not in normalized_note]
    checks.check(
        "note-contract",
        "the note states the four theorems, displayed-not-adopted scope, and machine fields",
        not missing,
        missing,
    )
    checks.check(
        "no-go-packet",
        "the landed note contains the complete N1-N8 discipline record",
        "## No-Go Discipline Gate" in note
        and all(f"### N{index} " in note for index in range(1, 9))
        and note.count("| ATTEMPTED |") >= 5,
    )
    checks.check(
        "n5-certificate-source",
        "the note carries the exact five forensic resolution lines",
        all(line in note for line in N5_LINES),
    )
    forbidden = (
        "G_N",
        "1/r",
        "1/r^2",
        "Lattice-named",
        "not a TOE",
        "B_57",
        "path dump",
    )
    present_forbidden = [phrase for phrase in forbidden if phrase in note]
    checks.check(
        "forbidden-rhetoric",
        "the source avoids the forbidden phrases and does not attach a graph-length identification",
        not present_forbidden
        and "Manhattan" not in note
        and "graph-length functional" in note,
        present_forbidden,
    )
    checks.check(
        "admissibility-untouched",
        "the note quotes Admissibility only to refuse writing the table into it",
        "Do not write into Admissibility" in note
        and "The Admissibility axiom is not an input to the algebra and is not edited"
        in normalized_note
        and "new axiom" not in note.lower(),
    )
    checks.check(
        "claim-scope",
        "frontmatter reports affine forms and crossing of the displayed table only",
        'claim_scope: "Affine forms and crossing k_* of the displayed c2d4 same-k table are reported. No new Dijkstra. Displayed, not adopted."'
        in note,
    )

    for line in N5_LINES:
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
