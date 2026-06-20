#!/usr/bin/env python3
"""Bounded half-action algebra core for the meron/fractional-instanton gate."""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "MERON_HALF_ACTION_CORE_FROM_TOPOLOGICAL_INFRASTRUCTURE_BOUNDED_NOTE_2026-06-18.md"
PARENT = ROOT / "docs" / "MERON_HALF_INSTANTON_4PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md"
INFRA = ROOT / "docs" / "TOPOLOGICAL_INSTANTON_TEXTBOOK_INFRASTRUCTURE_IMPORT_NOTE_2026-05-17.md"
INFRA_CACHE = ROOT / "logs" / "runner-cache" / "topological_instanton_bounded_certificate.txt"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"  [{status}] {label}")
    if detail:
        print(f"         {detail}")


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalized(path: Path) -> str:
    return " ".join(text(path).split())


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def test_status_firewall() -> None:
    section("T0: source status and citation firewalls")
    note = text(NOTE)
    norm = " ".join(note.split())
    check("claim type is bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("actual status is bounded-support", "**Actual current-surface status:** bounded-support" in note)
    check("trace class is upstream_support", "**Trace class:** upstream_support" in note)
    check("bare retained is barred", "**Bare retained allowed:** false" in note)
    check("proposal is barred", "**Proposal allowed:** false" in note)
    check(
        "firewall forbids meron/fractional-instanton existence citation",
        "retained meron existence" in norm
        and "retained fractional-instanton existence" in norm,
    )
    check(
        "firewall forbids framework hierarchy/scale-ratio use",
        "closure of `alpha_LM^16`, `v/M_Pl`, hierarchy formulas" in norm,
    )


def test_symbolic_half_action() -> None:
    section("T1: symbolic half-action algebra")
    g = sp.symbols("g", positive=True, real=True)
    q = sp.Rational(1, 2)
    s_bound = 8 * sp.pi**2 / g**2 * q
    s_half = 4 * sp.pi**2 / g**2
    check(
        "(8*pi^2/g^2)*(1/2) = 4*pi^2/g^2",
        sp.simplify(s_bound - s_half) == 0,
        f"simplified difference = {sp.simplify(s_bound - s_half)}",
    )
    s_inst = 8 * sp.pi**2 / g**2
    check(
        "S_half / S_inst = 1/2",
        sp.simplify(s_half / s_inst) == sp.Rational(1, 2),
        f"ratio = {sp.simplify(s_half / s_inst)}",
    )


def test_numerical_half_action() -> None:
    section("T2: numerical half-action values")
    expected = {
        Fraction(1, 2): 8 * math.pi**2,
        Fraction(1, 1): 4 * math.pi**2,
        Fraction(2, 1): 2 * math.pi**2,
    }
    ok_all = True
    detail = []
    for g2, target in expected.items():
        got = 4 * math.pi**2 / float(g2)
        ok = abs(got - target) < 1e-12
        ok_all = ok_all and ok
        detail.append(f"g^2={g2}: {got:.12f}")
    check("g^2 in {1/2,1,2} gives {8,4,2}*pi^2", ok_all, "; ".join(detail))
    canonical = 4 * math.pi**2
    check(
        "canonical g^2=1 value is 4*pi^2 ~= 39.4784176044",
        abs(canonical - 39.47841760435743) < 1e-12,
        f"4*pi^2 = {canonical:.13f}",
    )


def test_infrastructure_dependency() -> None:
    section("T3: bounded infrastructure dependency")
    infra = text(INFRA)
    cache = text(INFRA_CACHE)
    check("infrastructure states bounded certificate status", "bounded algebraic instanton-infrastructure certificate" in infra)
    check("infrastructure includes Bogomolny bound normalization", "S_E >= (8 pi^2/g^2) |Q|" in infra)
    check("infrastructure includes BPST 8 pi^2 normalization", "BPST radial `8 pi^2` normalization" in infra or "8 pi^2" in infra)
    check("infrastructure includes twisted T4 fractional charge arithmetic", "twisted `T^4` `k/N` charge arithmetic" in infra or "twisted T4 k/N charge arithmetic" in cache)
    check("infrastructure runner cache passed", "status: ok" in cache and "PASS=3 FAIL=0" in cache)


def test_parent_wiring() -> None:
    section("T4: parent row cites core split and preserves open gate")
    parent = text(PARENT)
    norm = " ".join(parent.split())
    check(
        "parent cites new half-action core split",
        "MERON_HALF_ACTION_CORE_FROM_TOPOLOGICAL_INFRASTRUCTURE_BOUNDED_NOTE_2026-06-18.md" in parent,
    )
    check(
        "parent says boundary construction remains open",
        "regulator/twist/patching construction remains open" in norm
        or "regulator, cap, twist, or patching construction remains open" in norm,
    )
    check(
        "parent does not claim upstream authority for regulator/twist/patching construction",
        "Provides the one-hop authority for the regulator / twist / patching construction" not in parent,
    )


def main() -> int:
    print("# Meron half-action algebra core split runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_status_firewall()
    test_symbolic_half_action()
    test_numerical_half_action()
    test_infrastructure_dependency()
    test_parent_wiring()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
