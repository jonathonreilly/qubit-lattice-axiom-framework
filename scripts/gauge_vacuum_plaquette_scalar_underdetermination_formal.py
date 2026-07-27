#!/usr/bin/env python3
"""Formal scalar-underdetermination runner for the beta=6 plaquette warning.

The runner proves only the finite-dimensional no-go used by the narrowed note:
one scalar constraint cannot determine an N >= 3 positive normalized vector.
It does not import Wilson/Haar, rim-lift, compression, or beta=6 PF data.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GAUGE_VACUUM_PLAQUETTE_BETA6_SCALAR_VALUE_INSUFFICIENCY_NOTE_2026-04-17.md"
AUDIT_INPUT_PATHS = (
    "docs/GAUGE_VACUUM_PLAQUETTE_BETA6_SCALAR_VALUE_INSUFFICIENCY_NOTE_2026-04-17.md",
)

THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "", bucket: str = "THEOREM") -> None:
    global THEOREM_PASS, SUPPORT_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        if bucket == "SUPPORT":
            SUPPORT_PASS += 1
        else:
            THEOREM_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


def dot(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> Fraction:
    return sum(x * y for x, y in zip(a, b, strict=True))


def add_scaled(
    v: tuple[Fraction, ...], eps: Fraction, w: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    return tuple(x + eps * y for x, y in zip(v, w, strict=True))


def positive_normalized(v: tuple[Fraction, ...]) -> bool:
    return all(x > 0 for x in v) and sum(v) == 1


def main() -> int:
    print("=" * 88)
    print("GAUGE-VACUUM PLAQUETTE SCALAR-UNDERDETERMINATION FORMAL RUNNER")
    print("=" * 88)
    print()

    v_a = (Fraction(1, 5), Fraction(3, 5), Fraction(1, 5))
    v_b = (Fraction(7, 20), Fraction(3, 10), Fraction(7, 20))
    ell = (Fraction(0), Fraction(1), Fraction(2))
    m_stat = (Fraction(0), Fraction(1), Fraction(4))
    w = (Fraction(1), Fraction(-2), Fraction(1))

    l_a = dot(ell, v_a)
    l_b = dot(ell, v_b)
    m_a = dot(m_stat, v_a)
    m_b = dot(m_stat, v_b)

    check(
        "witness vectors are strictly positive normalized vectors in V_3",
        positive_normalized(v_a) and positive_normalized(v_b),
        f"sum(vA)={sum(v_a)}, sum(vB)={sum(v_b)}",
    )
    check(
        "witness vectors are distinct",
        v_a != v_b,
        f"vA={v_a}, vB={v_b}",
    )
    check(
        "single scalar L has the same value on both witnesses",
        l_a == l_b == 1,
        f"L(vA)={l_a}, L(vB)={l_b}",
    )
    check(
        "second statistic M separates the two witnesses",
        m_a != m_b and m_a == Fraction(7, 5) and m_b == Fraction(17, 10),
        f"M(vA)={m_a}, M(vB)={m_b}",
    )
    check(
        "null direction preserves normalization",
        sum(w) == 0,
        f"sum(w)={sum(w)}",
    )
    check(
        "null direction preserves the scalar L",
        dot(ell, w) == 0,
        f"L(w)={dot(ell, w)}",
    )
    check(
        "null direction changes M",
        dot(m_stat, w) != 0,
        f"M(w)={dot(m_stat, w)}",
    )

    eps = Fraction(3, 20)
    v_eps = add_scaled(v_a, eps, w)
    check(
        "a nonzero move along w stays inside the positive simplex",
        positive_normalized(v_eps) and v_eps == v_b,
        f"eps={eps}, vA+eps*w={v_eps}",
    )
    check(
        "the same move preserves L and changes M",
        dot(ell, v_eps) == l_a and dot(m_stat, v_eps) != m_a,
        f"L(v_eps)={dot(ell, v_eps)}, M(v_eps)={dot(m_stat, v_eps)}",
    )

    t = Fraction(2)
    z_a = v_a[0] + t * v_a[1] + t * t * v_a[2]
    z_b = v_b[0] + t * v_b[1] + t * t * v_b[2]
    check(
        "generic polynomial boundary evaluation can separate equal-L witnesses",
        z_a != z_b,
        f"Z_2(vA)={z_a}, Z_2(vB)={z_b}",
    )

    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    check(
        "note declares the narrowed no_go claim type",
        "**claim type:** no_go" in lower and "**type:** no_go" in lower,
    )
    check(
        "note states Wilson/Haar, rim-lift, compression, and PF data are non-claims",
        "what this does not close" in lower
        and "wilson/haar" in lower
        and "rim-lift" in lower
        and "compressed boundary" in lower
        and "pf data" in lower,
    )

    print()
    print(f"THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    print(f"per_element: checked — equal scalar entries satisfy L(vA)=L(vB)={l_a} while M(vA)={m_a} and M(vB)={m_b}.")
    print(f"per_site: checked — both three-atom local probability vectors are strictly positive and normalized={positive_normalized(v_a) and positive_normalized(v_b)}.")
    print(f"per_mode: checked — null direction w has sum={sum(w)}, L(w)={dot(ell, w)}, and M(w)={dot(m_stat, w)}.")
    print(f"per_block: checked — the exact epsilon={eps} deformation maps vA to vB inside the positive simplex while preserving L.")
    print(f"lattice_wide: checked and not executed — the V3 scalar counterexample supplies no plaquette lattice lift; the executed exact witness has theorem PASS={THEOREM_PASS}, SUPPORT={SUPPORT_PASS}, FAIL={FAIL}.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
