#!/usr/bin/env python3
"""Source-domain guard for the beta=6 plaquette evaluation-seam note.

This companion checker targets the 2026-06-12 conditional audit blocker on
the seam-reduction source note: normalized rho statements need an explicit
nonzero denominator domain, and inner-product notation must type the
Peter-Weyl evaluation input as a Riesz representative rather than an
ambiguous functional/vector.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "GAUGE_VACUUM_PLAQUETTE_BETA6_EVALUATION_SEAM_REDUCTION_"
    "SCIENCE_ONLY_NOTE_2026-04-17.md"
)

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def main() -> int:
    text = NOTE.read_text(encoding="utf-8")

    check(
        "top status restricts normalized rho to z_(0,0) != 0",
        "statements are made only on" in text and "`z_(0,0) != 0`" in text,
    )
    check(
        "formal lemma defines rho only on the nonzero-denominator domain",
        "z_(p,q)/z_(0,0)` **only on the domain `z_(0,0) != 0`**" in text,
    )
    check(
        "zero denominator case keeps only unnormalized z and Z statements",
        "If `z_(0,0) = 0`, the formal lemma retains the unnormalized `z`"
        in text
        and "makes no `" in text
        and "claim" in text,
    )
    check(
        "beta=6 normalized rho statement carries z_(0,0)^env(6) domain",
        "domain `z_(0,0)^env(6) != 0`" in text
        and "no normalized `rho_(p,q)(6)` statement" in text
        and "is made" in text,
    )
    check(
        "evaluation functional is typed separately from its Riesz vector",
        "`ell_W: H -> C`" in text
        and "`k(W)" in text
        and "denotes the Riesz" in text
        and "representative of `ell_W`" in text
        and "`ell_W(v) =" in text,
    )
    check(
        "compressed rim-evaluation theorem uses ell_W and k(W)",
        "`Z_6^env(W) = ell_W(v_6) = <k(W), v_6>`" in text
        and "where `k(W)`" in text,
    )
    check(
        "legacy ambiguous <K(W), v> notation is absent",
        "<K(W), v" not in text and "<K(W)," not in text,
    )
    check(
        "remaining explicit-rho nonclosure is domain-qualified",
        "explicit normalized `rho_(p,q)(6)` outside" in text
        and "denominator domain `z_(0,0)^env(6) != 0`" in text,
    )

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
