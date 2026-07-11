#!/usr/bin/env python3
"""Bounded K/CPT orientation-invariance checks for the AC_phi_lambda gate.

The runner verifies the algebraic content of
docs/TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md
(orientation-only since 2026-06-10; the note states the lemma on the supplied
circulant class stipulated in-note; the determinant-character lemma moved to
THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md
with its own runner). It intentionally does not claim any premise-policy
change.
"""
from __future__ import annotations

import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md"
AXIOM_NOTE = DOCS / "MINIMAL_AXIOMS_2026-06-05.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"{tag} {label}" + (f" -- {detail}" if detail else ""))
    return ok


def flat(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    print("K/CPT orientation invariance checks for the AC_phi_lambda gate")
    print("=" * 76)

    note_text = NOTE.read_text(encoding="utf-8")
    note_flat = flat(note_text)
    axiom_text = AXIOM_NOTE.read_text(encoding="utf-8")
    axiom_flat = flat(axiom_text)

    # Source-boundary checks: the note must be conditional, not premise supply.
    check(
        "source states historical taxonomy has no authority",
        "historical provenance only" in note_flat
        and "supplies no premise" in note_flat
        and "open condition" in note_flat,
    )
    check(
        "source avoids the rejected theta shortcut",
        "theta_eff = theta_bare + 0" not in note_text
        and "P2 is discharged" not in note_text,
    )
    check(
        "source names the AC_phi_lambda conditional registrability bridge",
        "conditional on the registrable species surface being exactly the unordered mass multiset" in note_flat
        and "does not derive the magnitude `|delta| = 2/9`" in note_flat,
    )
    check(
        "source keeps audit status authority external",
        "independent audit lane only" in note_text
        and "No new axiom, primitive, admission" in note_text,
    )

    # The moved determinant lemma must be pointed at, not restated as load-bearing.
    check(
        "source points at the moved determinant-character lemma note",
        "THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md"
        in note_text
        and "not load-bearing here" in note_flat,
    )

    phi = sp.symbols("phi", real=True)  # noqa: F841 (kept for parity with prior versions)

    # AC_phi_lambda orientation algebra.
    a, B, delta = sp.symbols("a B delta", positive=True, real=True)
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    H_delta = (
        a * sp.eye(3)
        + B * sp.exp(sp.I * delta) * C
        + B * sp.exp(-sp.I * delta) * C.T
    )
    H_minus = (
        a * sp.eye(3)
        + B * sp.exp(-sp.I * delta) * C
        + B * sp.exp(sp.I * delta) * C.T
    )
    check(
        "conjugation maps the AC_phi_lambda circulant H(delta) exactly to H(-delta)",
        sp.simplify(H_delta.applyfunc(sp.conjugate) - H_minus) == sp.zeros(3, 3),
    )

    lambdas_plus = [
        a + 2 * B * sp.cos(delta + 2 * sp.pi * idx / 3)
        for idx in range(3)
    ]
    lambdas_minus = [
        a + 2 * B * sp.cos(-delta + 2 * sp.pi * idx / 3)
        for idx in range(3)
    ]
    e1_plus = sp.simplify(sum(lambdas_plus))
    e1_minus = sp.simplify(sum(lambdas_minus))
    e2_plus = sp.simplify(
        sum(lambdas_plus[i] * lambdas_plus[j] for i in range(3) for j in range(i + 1, 3))
    )
    e2_minus = sp.simplify(
        sum(lambdas_minus[i] * lambdas_minus[j] for i in range(3) for j in range(i + 1, 3))
    )
    e3_plus = sp.simplify(lambdas_plus[0] * lambdas_plus[1] * lambdas_plus[2])
    e3_minus = sp.simplify(lambdas_minus[0] * lambdas_minus[1] * lambdas_minus[2])
    symmetric_invariants_match = all(
        sp.simplify(sp.expand_trig(lhs - rhs)) == 0
        for lhs, rhs in ((e1_plus, e1_minus), (e2_plus, e2_minus), (e3_plus, e3_minus))
    )
    check(
        "elementary symmetric polynomials of the AC_phi_lambda spectrum match at +/-delta",
        symmetric_invariants_match,
    )

    label_flip_matches = all(
        sp.simplify(
            sp.expand_trig(
                (a + 2 * B * sp.cos(-delta + 2 * sp.pi * idx / 3))
                - (a + 2 * B * sp.cos(delta + 2 * sp.pi * ((-idx) % 3) / 3))
            )
        )
        == 0
        for idx in range(3)
    )
    check(
        "delta -> -delta permutes eigenvalue labels by k -> -k",
        label_flip_matches,
    )

    check(
        "source stipulates the supplied circulant class in-note",
        "supplied circulant class" in note_flat
        and "H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T" in note_flat,
    )
    check(
        "staggered gate is cited as context only, not a load-bearing markdown link",
        "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md" in note_text
        and "](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)" not in note_text,
    )

    # Markdown dependency hygiene for the source note.
    linked_paths = re.findall(r"\]\(([^)]+\.md)\)", note_text)
    missing = [path for path in linked_paths if not (DOCS / path).exists()]
    check(
        "all local markdown dependency links resolve",
        not missing,
        detail=", ".join(missing) if missing else "",
    )

    print("=" * 76)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
