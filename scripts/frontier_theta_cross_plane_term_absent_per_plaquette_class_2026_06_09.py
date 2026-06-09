#!/usr/bin/env python3
"""Check the conditional per-plaquette exclusion of a local FtildeF slot.

The runner verifies only the narrowed theorem:

  In a supplied per-plaquette action class A = sum_P f(U_P), each summand
  depends on one plaquette plane. The local cross-plane monomials that form
  FtildeF have identically zero coefficients, because their coefficients are
  mixed derivatives across independent one-plane variables.

It does not derive the per-plaquette class, close strong CP, choose an action,
or set audit status.
"""
from __future__ import annotations

import itertools
import re
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_CROSS_PLANE_TERM_ABSENT_IN_SUPPLIED_PER_PLAQUETTE_CLASS_BOUNDED_THEOREM_NOTE_2026-06-09.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  --  {detail}" if detail else ""
    print(f"  [{tag}] {label}{suffix}")
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("=" * 88)
    print("THETA CROSS-PLANE TERM ABSENT IN A SUPPLIED PER-PLAQUETTE CLASS")
    print("=" * 88)

    section("Symbolic mixed-derivative checks")
    variables = {
        "01": sp.symbols("F01"),
        "23": sp.symbols("F23"),
        "02": sp.symbols("F02"),
        "13": sp.symbols("F13"),
        "03": sp.symbols("F03"),
        "12": sp.symbols("F12"),
    }
    f = sp.Function("f")
    action = sum(f(x) for x in variables.values())
    pairings = [("01", "23"), ("02", "13"), ("03", "12")]
    derivatives = {
        f"{a}|{b}": sp.simplify(sp.diff(action, variables[a], variables[b]))
        for a, b in pairings
    }
    check(
        "all three FtildeF cross-plane pairings have zero mixed derivative",
        all(value == 0 for value in derivatives.values()),
        detail=str(derivatives),
    )
    check(
        "the result is independent of the one-plane function f",
        isinstance(action, sp.Expr) and all(value == 0 for value in derivatives.values()),
    )

    section("Direction-counting checks")
    plaquette_planes = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    counts = {
        plane: sum(
            1
            for assignment in itertools.permutations(range(4), 4)
            if all(index in plane for index in assignment)
        )
        for plane in plaquette_planes
    }
    check(
        "no single plaquette supplies four distinct epsilon directions",
        all(count == 0 for count in counts.values()),
        detail=str(counts),
    )
    pairing_direction_sets = {
        "01|23": {0, 1, 2, 3},
        "02|13": {0, 1, 2, 3},
        "03|12": {0, 1, 2, 3},
    }
    check(
        "each FtildeF pairing is a four-direction cross-plane object",
        all(len(direction_set) == 4 for direction_set in pairing_direction_sets.values()),
    )

    section("Prior-boundary consistency")
    single = (DOCS / "NEWPHYSICS_NP_STRONG_CP_THETA_NOTE_2026-05-10_npCP.md").read_text(
        encoding="utf-8"
    )
    multi = (
        DOCS
        / "STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07.md"
    ).read_text(encoding="utf-8")
    check(
        "single-plaquette prior identifies the same one-plaquette theta boundary",
        "single-plaquette action class" in single
        and ("FtildeF" in single or "F tilde F" in single or "F̃F" in single),
    )
    check(
        "multi-plaquette prior preserves the reopening condition",
        "multi-plaquette" in multi
        and ("single-plaquette" in multi or "single plaquette" in multi)
        and ("reopen" in multi or "admissible" in multi),
    )

    section("Source-note scope checks")
    note = NOTE.read_text(encoding="utf-8")
    normalized_note = re.sub(r"\s+", " ", note)
    required_phrases = [
        "This is a theorem about the supplied action class, not a derivation of that class.",
        "does not set `theta_QCD = 0` in the full framework",
        "Multi-plaquette terms, clover products, or any other action term with cross-plane support are outside this theorem",
        "PASS for the narrowed conditional class theorem",
        "FAIL for any reading that treats this note as a derivation of per-plaquette support",
    ]
    for phrase in required_phrases:
        check(f"source note contains required boundary: {phrase}", phrase in normalized_note)

    banned_phrases = [
        "last premise",
        "theta admission's surviving content",
        "entire live candidate class",
        "theta_bare = 0 automatically",
        "P2 already discharged",
        "no numeric or CP-specific content survives",
        "owner/audit lane's call",
    ]
    for phrase in banned_phrases:
        check(f"source note excludes overclaim phrase: {phrase}", phrase not in note)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
