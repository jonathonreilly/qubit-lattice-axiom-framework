#!/usr/bin/env python3
"""Formal generator/coupling label-rescaling coefficient theorem.

This runner checks the finite algebra behind the scoped bridge:

  defined coefficient equality beta = 2 n / g^2
  + compensating generator rescaling T' = c T, g' = g / c
    => beta' = c^2 beta
    => beta' g'^2 = beta g^2 = 2 N_c.

It does not infer an action, physical coupling, normalization point, or audit
verdict.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "WILSON_GENERATOR_RESCALING_BETA_TRANSFORMATION_NARROW_THEOREM_NOTE_2026-06-16.md"
WM_NOTE = ROOT / "docs" / "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md"
GBARE_RESCALING_NOTE = ROOT / "docs" / "G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def beta(n_c: Fraction, g_sq: Fraction) -> Fraction:
    return Fraction(2) * n_c / g_sq


def gram_diag(c_sq: Fraction) -> Fraction:
    return c_sq * Fraction(1, 2)


def part0_source_boundaries() -> None:
    print("Part 0: source boundaries")
    check("bridge note exists", NOTE.exists(), NOTE.relative_to(ROOT).as_posix())
    check("defined matrix coefficient note exists", WM_NOTE.exists(), WM_NOTE.relative_to(ROOT).as_posix())
    check("g_bare rescaling consumer note exists", GBARE_RESCALING_NOTE.exists(), GBARE_RESCALING_NOTE.relative_to(ROOT).as_posix())
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "**Claim type:** positive_theorem",
        "No Wilson action or physical coupling is part of the theorem",
        "T'_a = c T_a",
        "g'   = g/c",
        "beta' = c^2 beta",
        "beta' g'^2 = beta g^2 = 2n",
        "does not claim:",
        "the paired label transformation is induced on any Wilson",
        "A downstream physical use must separately prove the dictionary",
    ]
    flat = " ".join(text.split())
    for marker in required:
        check(f"bridge note contains marker: {marker[:60]}", marker in text or marker in flat)
    audit_verdict_marker = "audit" + "_status: " + "audited" + "_clean"
    effective_marker = "effective" + "_status: " + "retained"
    forbidden = [
        ("audit verdict marker", audit_verdict_marker),
        ("effective-status marker", effective_marker),
        ("Wilson surface overclaim", "Wilson action-surface selection is derived"),
        ("g_bare closure overclaim", "g_bare=1 is derived"),
    ]
    for label, marker in forbidden:
        check(f"forbidden overclaim absent: {label}", marker not in text)


def part1_wilson_matching_note() -> None:
    print()
    print("Part 1: formal coefficient authority surface")
    text = WM_NOTE.read_text(encoding="utf-8")
    required = [
        "beta = 2n/g^2",
        "beta g^2 = 2n",
        "C_left = C_right",
        "They may not cite it as authority for an action surface",
    ]
    flat = " ".join(text.split())
    for marker in required:
        check(f"formal note contains marker: {marker[:60]}", marker in text or marker in flat)


def part2_exact_transform() -> None:
    print()
    print("Part 2: exact beta transform under compensating generator rescaling")
    samples = [
        (Fraction(3), Fraction(1)),
        (Fraction(3), Fraction(5, 7)),
        (Fraction(2), Fraction(3, 5)),
        (Fraction(7, 2), Fraction(9, 4)),
    ]
    c_values = [Fraction(1, 3), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(5, 2), Fraction(3)]
    for n_c, g_sq in samples:
        beta_old = beta(n_c, g_sq)
        check(f"formal product before rescaling n={n_c}, g^2={g_sq}", beta_old * g_sq == 2 * n_c, f"beta={beta_old}")
        for c in c_values:
            c_sq = c * c
            g_sq_new = g_sq / c_sq
            beta_new = beta(n_c, g_sq_new)
            check(
                f"beta scales by c^2 for N={n_c}, g^2={g_sq}, c={c}",
                beta_new == c_sq * beta_old,
                f"beta'={beta_new}; c^2 beta={c_sq * beta_old}",
            )
            check(
                f"product invariant after compensating rescale c={c}",
                beta_new * g_sq_new == beta_old * g_sq == 2 * n_c,
            )


def part3_canonical_surface_exclusion() -> None:
    print()
    print("Part 3: fixed-beta and half-trace definitions change for nontrivial c")
    beta_old = Fraction(6)
    g_sq = Fraction(1)
    n_c = Fraction(3)
    check("test point satisfies beta g^2 = 2 N_c", beta_old * g_sq == 2 * n_c)
    for c in [Fraction(1, 2), Fraction(2), Fraction(3)]:
        c_sq = c * c
        beta_new = c_sq * beta_old
        check(
            f"nontrivial c={c} changes the defined beta label",
            beta_new != beta_old,
            f"beta'={beta_new}; beta={beta_old}",
        )
        check(
            f"nontrivial c={c} changes canonical trace Gram",
            gram_diag(c_sq) != Fraction(1, 2),
            f"Tr(T'_a T'_a)={gram_diag(c_sq)}",
        )


def main() -> int:
    print("Formal generator/coupling label-rescaling coefficient theorem")
    print("=" * 72)
    part0_source_boundaries()
    part1_wilson_matching_note()
    part2_exact_transform()
    part3_canonical_surface_exclusion()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
