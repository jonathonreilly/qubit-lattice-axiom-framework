#!/usr/bin/env python3
"""Exact bounded-surface check for the g_bare rescaling bridge repair.

This runner checks the narrowed source row:

  CN + rescaling by c => Gram -> c^2 Gram.
  CN + supplied Wilson matching + compensating T'_a = c T_a, g' T'_a = g T_a
      => beta' = c^2 beta.

It does not derive Wilson action-surface selection, beta=6, g_bare=1,
or any audit verdict.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md"
WM_NOTE = ROOT / "docs" / "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md"
WGT_NOTE = ROOT / "docs" / "WILSON_GENERATOR_RESCALING_BETA_TRANSFORMATION_NARROW_THEOREM_NOTE_2026-06-16.md"


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    msg = f"[{tag}] {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return cond


def canonical_gram(n: int = 8) -> list[list[Fraction]]:
    return [
        [Fraction(1, 2) if i == j else Fraction(0) for j in range(n)]
        for i in range(n)
    ]


def scale_gram(gram: list[list[Fraction]], c_squared: Fraction) -> list[list[Fraction]]:
    return [[c_squared * entry for entry in row] for row in gram]


def beta(n_c: Fraction, g_squared: Fraction) -> Fraction:
    return Fraction(2) * n_c / g_squared


def main() -> int:
    note_text = NOTE.read_text(encoding="utf-8")
    gram = canonical_gram()

    check("consumer note exists", NOTE.exists(), NOTE.relative_to(ROOT).as_posix())
    check("Wilson matching note exists", WM_NOTE.exists(), WM_NOTE.relative_to(ROOT).as_posix())
    check("Wilson generator-rescaling bridge note exists", WGT_NOTE.exists(), WGT_NOTE.relative_to(ROOT).as_posix())

    required_markers = [
        "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md",
        "WILSON_GENERATOR_RESCALING_BETA_TRANSFORMATION_NARROW_THEOREM_NOTE_2026-06-16.md",
        "beta' = c^2 beta",
        "g' T'_a = g T_a",
        "does not select the Wilson action surface",
        "does not select `beta = 6`",
        "does not derive `g_bare = 1`",
    ]
    flat = " ".join(note_text.split())
    for marker in required_markers:
        check(f"note contains scoped bridge marker: {marker[:60]}", marker in note_text or marker in flat)

    for c_squared in [Fraction(1, 4), Fraction(2), Fraction(4), Fraction(9)]:
        scaled = scale_gram(gram, c_squared)
        expected_diag = c_squared * Fraction(1, 2)
        diag_ok = all(scaled[i][i] == expected_diag for i in range(8))
        off_diag_ok = all(
            scaled[i][j] == 0
            for i in range(8)
            for j in range(8)
            if i != j
        )
        check(
            f"Gram scales by c^2 = {c_squared}",
            diag_ok and off_diag_ok,
            f"new diagonal = {expected_diag}",
        )
        check(
            f"nontrivial c^2 = {c_squared} leaves canonical Gram only when c^2 = 1",
            c_squared != 1 and expected_diag != Fraction(1, 2),
            "canonical diagonal is 1/2",
        )

    for n_c, g_squared in [
        (Fraction(3), Fraction(1)),
        (Fraction(3), Fraction(5, 7)),
        (Fraction(2), Fraction(3, 5)),
        (Fraction(7, 2), Fraction(9, 4)),
    ]:
        beta_old = beta(n_c, g_squared)
        check(
            f"Wilson matching product beta g^2 = 2 N_c for N={n_c}, g^2={g_squared}",
            beta_old * g_squared == 2 * n_c,
            f"beta={beta_old}",
        )
        for c in [Fraction(1, 3), Fraction(1, 2), Fraction(2), Fraction(5, 2), Fraction(3)]:
            c_squared = c * c
            g_squared_new = g_squared / c_squared
            beta_new = beta(n_c, g_squared_new)
            check(
                f"beta scales by c^2 for N={n_c}, g^2={g_squared}, c={c}",
                beta_new == c_squared * beta_old,
                f"beta'={beta_new}; c^2 beta={c_squared * beta_old}",
            )
            check(
                f"matched product invariant after compensating rescale c={c}",
                beta_new * g_squared_new == beta_old * g_squared == 2 * n_c,
            )

    forbidden_markers = [
        "effective_status: retained",
        "audit_status: audited_clean",
        "Wilson action-surface selection is derived",
        "g_bare=1 is derived",
    ]
    for marker in forbidden_markers:
        check(f"forbidden overclaim absent: {marker}", marker not in note_text)

    print(f"SUMMARY: PASS = {PASS}, FAIL = {FAIL}")
    if FAIL:
        print("Scoped g_bare rescaling bridge check failed.")
        return 1

    print("Scoped g_bare rescaling bridge check passed; no retained status is asserted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
