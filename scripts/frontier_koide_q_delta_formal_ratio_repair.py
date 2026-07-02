#!/usr/bin/env python3
"""Formal-ratio repair runner for the Koide Q-delta linking row.

This runner checks the exact rational identity:

    Q_d = 2/d, Delta_d = 2/d^2  =>  Delta_d = Q_d/d,

plus the 2026-07-01 decoration corollary on the retained circulant
character bridge parent: with lambda_k = a + b w^k + bbar w^{-k}
(w = exp(2 pi i/3)), the spectral ratio functional
R = sum(lambda^2)/(sum(lambda))^2 equals 1/3 + (2/3)(|b|^2/a^2),
equals (a_0^2 + 2|z|^2)/(3 a_0^2) in character coefficients, and equals
Q_3 = 2/3 exactly on the parent's a_0^2 = 2|z|^2 locus (3a^2 = 6|b|^2).

It explicitly avoids the radian/Berry-holonomy bridge, equal-sector-norm
selector, PDG comparators, any physical charged-lepton claim, and any
selection principle for the parent's locus.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md"
TARGET_CITATION = "KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md"
CACHE_PATH = ROOT / "logs" / "runner-cache" / "frontier_koide_q_delta_formal_ratio_repair.txt"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def q_d(d: int) -> Fraction:
    return Fraction(2, d)


def delta_d(d: int) -> Fraction:
    return Fraction(2, d * d)


def q_alt(d: int) -> Fraction:
    return Fraction(d - 1, d)


def check_note_boundary() -> None:
    section("Source-note boundary")
    text = NOTE_PATH.read_text()
    required = [
        "bounded-support formal algebra",
        "No Berry-holonomy radian bridge",
        "That exact rational identity is the entire freestanding content of this",
        "This repair withdraws both from the binding claim.",
        "The bridge from this formal algebra to physical Koide/Brannen geometry remains a separate open science problem.",
        "Citation firewall (2026-06-18)",
        "Direct citations to this note are allowed only for the definition-level",
        "Decoration attachment (2026-07-01)",
        "KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md",
        "that the locus is selected",
        "never as a selection principle",
        "claim_type_author_hint: decoration",
        "koide_circulant_character_bridge_narrow_theorem_note_2026-05-09",
    ]
    for needle in required:
        check(f"note contains required boundary: {needle!r}", needle in text)

    forbidden = [
        "uses PDG",
        "matches observed",
        "observed charged-lepton",
        "retained selected-line",
        "Berry holonomy in radians is derived",
        "equal-sector-norm input is retained",
        "the locus is selected by the framework",
        "derives the selection principle",
    ]
    for needle in forbidden:
        check(f"note avoids overclaim/token: {needle!r}", needle not in text)


def is_source_scan_path(path: Path) -> bool:
    if path == NOTE_PATH or path == Path(__file__).resolve() or path == CACHE_PATH:
        return False
    rel = path.relative_to(ROOT)
    rel_s = rel.as_posix()
    if path.suffix not in {".md", ".py"}:
        return False
    if rel_s.startswith("docs/audit/"):
        return False
    if rel.name == "KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20_NOTE_2026-05-17.md":
        return False
    if rel_s.startswith("docs/publication/ci3_z3/") and rel.name.endswith("_EFFECTIVE_STATUS.md"):
        return False
    if rel_s.startswith(".claude/") or rel_s.startswith("logs/"):
        return False
    return rel_s.startswith("docs/") or rel_s.startswith("scripts/")


def check_direct_citation_firewall() -> None:
    section("Direct citation firewall")
    allowed_markers = [
        "formal identity",
        "formal-only",
        "definition-level",
        "decoration",
        "decoration-support",
        "corollary",
        "formal ratio",
        "formal q-delta identity",
        "formal q_d/delta_d identity",
        "formal delta_d = q_d/d",
        "context only",
        "reader context only",
        "not load-bearing",
        "not consumed",
        "does not close",
        "does not derive",
        "not derive",
        "remains open",
        "open",
        "conditional",
        "blocked",
        "no-go",
        "historical pre-repair",
        "historical/non-authority",
        "no retained physical",
        "current repaired note is formal-only",
        "under audit",
        "not promoted",
        "not closed",
    ]
    forbidden_patterns = [
        ("retained physical delta", re.compile(r"retained\s+(?:`?δ|delta)\s*=\s*2/9", re.I)),
        ("retained q-delta authority", re.compile(r"retained[^.\n]{0,80}q[-_ ]?delta", re.I)),
        ("partial physical closure", re.compile(r"partial closure", re.I)),
        ("PDG comparator", re.compile(r"matches observed|observed-mass comparator", re.I)),
        ("charged-lepton offset authority", re.compile(r"physical charged-lepton offset", re.I)),
        ("live radian-bridge authority", re.compile(r"original site naming|names primitive `?P`?|§4", re.I)),
    ]

    citation_count = 0
    for root in [ROOT / "docs", ROOT / "scripts"]:
        for path in sorted(root.rglob("*")):
            if not is_source_scan_path(path):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            if TARGET_CITATION not in text:
                continue
            rel = path.relative_to(ROOT).as_posix()
            lines = text.splitlines()
            for idx, line in enumerate(lines):
                if TARGET_CITATION not in line:
                    continue
                citation_count += 1
                lo = max(0, idx - 4)
                hi = min(len(lines), idx + 5)
                window = "\n".join(lines[lo:hi])
                lower = window.lower()
                has_allowed_marker = any(marker in lower for marker in allowed_markers)
                forbidden_hits = [label for label, pattern in forbidden_patterns if pattern.search(window)]
                check(
                    f"{rel}:{idx + 1} citation is explicitly formal/open/contextual",
                    has_allowed_marker,
                    "" if has_allowed_marker else "window lacks a formal/open/context marker",
                )
                check(
                    f"{rel}:{idx + 1} citation avoids forbidden authority language",
                    not forbidden_hits,
                    "" if not forbidden_hits else ", ".join(forbidden_hits),
                )
    check("at least one direct citation was scanned", citation_count > 0, f"citations={citation_count}")


def check_exact_identity() -> None:
    section("Exact rational identity")
    for d in [1, 2, 3, 4, 5, 7, 11, 17, 32]:
        q = q_d(d)
        delta = delta_d(d)
        check(f"d={d}: Delta_d = Q_d/d", delta == q / d, f"Delta={delta}, Q/d={q/d}")
        check(f"d={d}: Delta_d/Q_d = 1/d", delta / q == Fraction(1, d), f"ratio={delta/q}")


def check_d3_values() -> None:
    section("d=3 exact values")
    check("Q_3 = 2/3", q_d(3) == Fraction(2, 3), str(q_d(3)))
    check("Delta_3 = 2/9", delta_d(3) == Fraction(2, 9), str(delta_d(3)))
    check("Delta_3 / Q_3 = 1/3", delta_d(3) / q_d(3) == Fraction(1, 3), str(delta_d(3) / q_d(3)))


def check_negative_control() -> None:
    section("Negative control: alternative Q'_d=(d-1)/d")
    for d in [2, 4, 5, 7, 11, 17]:
        check(
            f"d={d}: alternative Q'_d/d does not equal Delta_d",
            delta_d(d) != q_alt(d) / d,
            f"Delta={delta_d(d)}, Q_alt/d={q_alt(d)/d}",
        )
    check("d=3 is the unique tested coincidence for Q'_d=2/d", q_alt(3) == q_d(3), f"Q_alt(3)={q_alt(3)}")


def ratio_from_squares(a_sq: Fraction, b_sq: Fraction) -> Fraction:
    """Exact R = (3a^2 + 6|b|^2) / (9a^2) from squared parameters."""
    return (3 * a_sq + 6 * b_sq) / (9 * a_sq)


def check_decoration_corollary_exact() -> None:
    section("Decoration corollary: exact ratio functional on the parent surface")
    # (C1)/(C2) rational form and (C3) on-locus value 2/3, in exact arithmetic
    # via the squared parameters (a^2, |b|^2). Parent T1/T2 give
    # a_0^2 = 3 a^2 and |z|^2 = 3 |b|^2.
    on_locus_pairs = [(Fraction(2), Fraction(1)), (Fraction(8), Fraction(4)), (Fraction(2, 9), Fraction(1, 9))]
    for a_sq, b_sq in on_locus_pairs:
        check(f"locus 3a^2=6|b|^2 holds for a^2={a_sq}, |b|^2={b_sq}", 3 * a_sq == 6 * b_sq)
        r = ratio_from_squares(a_sq, b_sq)
        check(f"(C3) on-locus R = 2/3 for a^2={a_sq}", r == Fraction(2, 3), f"R={r}")
        a0_sq, z_sq = 3 * a_sq, 3 * b_sq
        r_char = (a0_sq + 2 * z_sq) / (3 * a0_sq)
        check(f"(C2) character form matches for a^2={a_sq}", r_char == r, f"R_char={r_char}")
        check(f"(C3) companion Delta_3 = R/3 = 2/9 for a^2={a_sq}", r / 3 == Fraction(2, 9), f"R/3={r/3}")
    # Off-locus negative controls: r_weight = |b|^2/a^2 in {0, 1} give R in {1/3, 1}.
    check("off-locus |b|^2=0 gives R = 1/3", ratio_from_squares(Fraction(1), Fraction(0)) == Fraction(1, 3))
    check("off-locus |b|^2=a^2 gives R = 1", ratio_from_squares(Fraction(1), Fraction(1)) == Fraction(1))
    check(
        "off-locus |b|^2=a^2 does NOT give Q_3",
        ratio_from_squares(Fraction(1), Fraction(1)) != Fraction(2, 3),
    )
    # General rational-weight law (C1): R = 1/3 + (2/3) w for w = |b|^2/a^2.
    for w in [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(2), Fraction(7, 5)]:
        r = ratio_from_squares(Fraction(1), w)
        check(f"(C1) weight law R = 1/3 + (2/3)w at w={w}", r == Fraction(1, 3) + Fraction(2, 3) * w, f"R={r}")


def check_decoration_corollary_numeric() -> None:
    section("Decoration corollary: numeric eigenvalue-triple confirmation")
    import cmath
    import math

    w = cmath.exp(2j * cmath.pi / 3)
    tol = 1e-12
    # (a, b) pairs: two on-locus (a = sqrt(2)|b|), two off-locus; complex b phases.
    cases = [
        ("on-locus b=1", math.sqrt(2.0), 1.0 + 0.0j),
        ("on-locus b=exp(i*0.7)/3", math.sqrt(2.0) / 3.0, cmath.exp(0.7j) / 3.0),
        ("off-locus r_w=1", 1.0, cmath.exp(0.3j)),
        ("off-locus r_w=0.2", 1.0, math.sqrt(0.2) * cmath.exp(1.1j)),
    ]
    for label, a, b in cases:
        lam = [a + b * w**k + b.conjugate() * w**(-k) for k in range(3)]
        check(f"{label}: eigenvalues are real", all(abs(l.imag) < tol for l in lam))
        lam_r = [l.real for l in lam]
        s1 = sum(lam_r)
        s2 = sum(l * l for l in lam_r)
        check(f"{label}: sum(lambda) = 3a", abs(s1 - 3 * a) < tol, f"s1={s1:.15f}")
        check(
            f"{label}: sum(lambda^2) = 3a^2 + 6|b|^2",
            abs(s2 - (3 * a * a + 6 * abs(b) ** 2)) < tol,
            f"s2={s2:.15f}",
        )
        r_num = s2 / (s1 * s1)
        r_weight = abs(b) ** 2 / (a * a)
        check(
            f"{label}: R matches 1/3 + (2/3)|b|^2/a^2",
            abs(r_num - (1.0 / 3.0 + 2.0 / 3.0 * r_weight)) < tol,
            f"R={r_num:.15f}",
        )
        a0 = s1 / math.sqrt(3.0)
        zc = (lam_r[0] + lam_r[1] * w.conjugate() + lam_r[2] * w) / math.sqrt(3.0)
        check(
            f"{label}: character form (a_0^2+2|z|^2)/(3a_0^2) matches R",
            abs((a0 * a0 + 2 * abs(zc) ** 2) / (3 * a0 * a0) - r_num) < tol,
        )
        on_locus = abs(3 * a * a - 6 * abs(b) ** 2) < tol
        if on_locus:
            check(f"{label}: on-locus R = 2/3", abs(r_num - 2.0 / 3.0) < tol, f"R={r_num:.15f}")
        else:
            check(f"{label}: off-locus R != 2/3", abs(r_num - 2.0 / 3.0) > 1e-6, f"R={r_num:.15f}")


def main() -> int:
    print("Koide Q-delta formal ratio repair")
    check_note_boundary()
    check_direct_citation_firewall()
    check_exact_identity()
    check_d3_values()
    check_negative_control()
    check_decoration_corollary_exact()
    check_decoration_corollary_numeric()
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
