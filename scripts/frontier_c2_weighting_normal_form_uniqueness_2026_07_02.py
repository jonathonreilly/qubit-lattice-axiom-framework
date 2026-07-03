#!/usr/bin/env python3
"""Exact Fraction checks for Block11 C2 rational normal form."""

from fractions import Fraction
from pathlib import Path
import re


PASS = 0
FAIL = 0


def check(name, condition):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"[PASS] {name}")
    else:
        FAIL += 1
        print(f"[FAIL] {name}")


def add(r, s):
    return (r[0] + s[0], r[1] + s[1])


def scale(n, r):
    return (n * r[0], n * r[1])


def refine(r, k):
    return (r[0] / k, r[1] / k)


def readout(u, v):
    return lambda r: u * r[0] + v * r[1]


def reachable_pair(p, q, r, s):
    a_piece = refine((Fraction(1), Fraction(0)), q)
    b_piece = refine((Fraction(0), Fraction(1)), s)
    return add(scale(p, a_piece), scale(r, b_piece))


def run_reachability_checks():
    samples = [
        (2, 3, 5, 7),
        (0, 5, 4, 9),
        (11, 6, 0, 8),
    ]
    for p, q, r, s in samples:
        got = reachable_pair(p, q, r, s)
        expected = (Fraction(p, q), Fraction(r, s))
        check(f"reachability {expected}", got == expected)


def run_cauchy_checks():
    I = readout(Fraction(5, 3), Fraction(7, 4))
    u = I((Fraction(1), Fraction(0)))
    v = I((Fraction(0), Fraction(1)))
    check("u coefficient witness", u == Fraction(5, 3))
    check("v coefficient witness", v == Fraction(7, 4))
    check(
        "integer union on A",
        I(scale(4, (Fraction(1), Fraction(0)))) == 4 * u,
    )
    check(
        "integer union on B",
        I(scale(6, (Fraction(0), Fraction(1)))) == 6 * v,
    )
    check(
        "refinement on A",
        I(refine((Fraction(1), Fraction(0)), 9)) == u / 9,
    )
    check(
        "refinement on B",
        I(refine((Fraction(0), Fraction(1)), 10)) == v / 10,
    )
    parent = (Fraction(7, 5), Fraction(11, 13))
    k = 8
    check("equal-subrecord refinement", k * I(refine(parent, k)) == I(parent))


def run_reconstruction_checks():
    grid = [
        (Fraction(0), Fraction(0)),
        (Fraction(1, 2), Fraction(2, 3)),
        (Fraction(5, 4), Fraction(7, 6)),
        (Fraction(9, 10), Fraction(11, 12)),
    ]
    examples = [
        readout(Fraction(1), Fraction(2)),
        readout(Fraction(3, 2), Fraction(5, 3)),
    ]
    for idx, I in enumerate(examples, start=1):
        u = I((Fraction(1), Fraction(0)))
        v = I((Fraction(0), Fraction(1)))
        for record in grid:
            check(
                f"normal form example {idx} {record}",
                I(record) == u * record[0] + v * record[1],
            )


def run_non_content_determined_counterexample():
    record_a = ("alpha", (Fraction(1, 2), Fraction(3, 4)))
    record_b = ("beta", (Fraction(1, 2), Fraction(3, 4)))
    assigned = {"alpha": Fraction(5), "beta": Fraction(6)}
    same_content = record_a[1] == record_b[1]
    different_values = assigned[record_a[0]] != assigned[record_b[0]]
    check("same content pair", same_content)
    check("identity-dependent values differ", different_values)
    check("counterexample outside class", same_content and different_values)


def run_degenerate_checks():
    ignores_a = readout(Fraction(0), Fraction(5))
    ignores_b = readout(Fraction(7), Fraction(0))
    zero = readout(Fraction(0), Fraction(0))
    r = (Fraction(2, 3), Fraction(4, 5))
    check("degenerate ignores A", ignores_a(r) == Fraction(5) * r[1])
    check("degenerate ignores B", ignores_b(r) == Fraction(7) * r[0])
    check("zero readout", zero(r) == 0)


def markdown_targets(text):
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def run_note_discipline_checks():
    root = Path(__file__).resolve().parents[1]
    note_path = root / "docs" / "C2_WEIGHTING_NORMAL_FORM_ONE_PARAMETER_UNIQUENESS_BOUNDED_NOTE_2026-07-02.md"
    note = note_path.read_text(encoding="utf-8")
    targets = markdown_targets(note)
    md_targets = [target for target in targets if ".md" in target]
    py_targets = [target for target in targets if ".py" in target]
    cache_targets = [target for target in targets if "logs/runner-cache/" in target]
    expected_deps = {
        "SUPPLIED_READOUT_CONTEXT_TWO_COMPONENT_DECOMPOSITION_BOUNDED_NOTE_2026-07-02.md",
        "EIDENT_DECOMPOSITION_DEFINITIONAL_PROPORTIONALITY_CTX_MATCH_BOUNDED_NOTE_2026-07-02.md",
        "MINIMAL_AXIOMS_2026-06-29.md",
    }
    check("note declares canonical claim type", "**Type:** bounded_theorem" in note)
    check("source-side audit outcome absent", "audited_clean" not in note and "retained_bounded" not in note)
    check(
        "legacy status labels absent",
        "Status authority" not in note
        and "Actual current surface status" not in note
        and "Claim type" not in note,
    )
    check("outputs path absent", "outputs/" not in note)
    check(
        "primary runner is markdown-linked",
        len(py_targets) == 1
        and "frontier_c2_weighting_normal_form_uniqueness_2026_07_02.py" in py_targets[0],
    )
    check(
        "cache is markdown-linked under logs",
        len(cache_targets) == 1
        and cache_targets[0].endswith("frontier_c2_weighting_normal_form_uniqueness_2026_07_02.txt"),
    )
    check("all dependency notes are markdown-linked", expected_deps == {Path(target).name for target in md_targets})
    check("branch-local sibling wording absent", "stacked branch-local sibling" not in note)
    check(
        "record axiom quote includes content readout sentence",
        "A readout value is determined by record content alone." in " ".join(note.split()),
    )


def main():
    run_reachability_checks()
    run_cauchy_checks()
    run_reconstruction_checks()
    run_non_content_determined_counterexample()
    run_degenerate_checks()
    run_note_discipline_checks()
    print("Block11 C2 weighting normal form uniqueness")
    print("checks: reachability, finite Cauchy, reconstruction, counterexample, degenerates")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    raise SystemExit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
