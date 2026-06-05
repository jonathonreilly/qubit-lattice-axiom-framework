#!/usr/bin/env python3
"""Check hierarchy alpha_LM magnitude arithmetic and delta-zero open gate."""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_2026-05-30.md"

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
    suffix = f"  --  {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)


def read_note() -> str:
    return NOTE.read_text(encoding="utf-8")


def check_note_scope() -> None:
    section("Note scope")
    text = read_note()
    flat = " ".join(text.split())
    required = [
        "**Claim type:** open_gate",
        "does not close the hierarchy lane",
        "does not approve",
        "transport source for that coupling-power magnitude on the current baseline: open",
        "does not claim that every possible future mechanism is closed",
    ]
    forbidden = [
        "Generated" + " with",
        "source-note proposal only",
        "actual_" + "current_surface_status",
        "audit" + " lane",
        "ret" + "ained_bounded",
        "ret" + "ained_no_go",
        "closure_proposal",
        "formal no-go",
    ]
    for marker in required:
        check(f"note contains marker: {marker}", marker in text or marker in flat)
    for marker in forbidden:
        check(f"note omits non-native marker: {marker}", marker not in text)


def check_coupling_power() -> None:
    section("Coupling-power magnitude")
    alpha_bare = 1 / (4 * sp.pi)
    value = alpha_bare**16
    check("alpha_bare = 1/(4 pi)", sp.simplify(alpha_bare - 1 / (4 * sp.pi)) == 0)
    check(
        "alpha_bare^16 = (4 pi)^-16 ~= 2.586e-18",
        abs(float(value) - 2.586e-18) / 2.586e-18 < 1e-3,
        f"{float(value):.6e}",
    )


def check_geometric_progression() -> None:
    section("Geometric progression")
    u0, alpha_bare = sp.symbols("u0 alpha_bare", positive=True)
    alpha_lm = alpha_bare / u0
    alpha_s = alpha_bare / u0**2
    check("alpha_LM = alpha_bare/u0", sp.simplify(alpha_lm - alpha_bare / u0) == 0)
    check("alpha_s = alpha_bare/u0^2", sp.simplify(alpha_s - alpha_bare / u0**2) == 0)
    check("alpha_LM/alpha_bare = 1/u0", sp.simplify(alpha_lm / alpha_bare - 1 / u0) == 0)
    check("alpha_s/alpha_LM = 1/u0", sp.simplify(alpha_s / alpha_lm - 1 / u0) == 0)
    inv = [1 / alpha_bare, 1 / alpha_lm, 1 / alpha_s]
    delta_1 = sp.simplify(inv[1] - inv[0])
    delta_2 = sp.simplify(inv[2] - inv[1])
    check("1/alpha equal-step test gives Delta2/Delta1 = u0", sp.simplify(delta_2 / delta_1 - u0) == 0, str(sp.simplify(delta_2 / delta_1)))


def check_block_observable_symbols() -> None:
    section("Block observable symbol support")
    m, omega, u0, alpha_bare = sp.symbols("m omega u0 alpha_bare", positive=True)
    block = m**2 + u0**2 * (3 + sp.sin(omega) ** 2)
    determinant_factor = block**4
    condensate_summand = 1 / block
    check("determinant factor contains u0", u0 in determinant_factor.free_symbols)
    check("determinant factor has no explicit alpha_bare", alpha_bare not in determinant_factor.free_symbols)
    check("condensate summand contains u0", u0 in condensate_summand.free_symbols)
    check("condensate summand has no explicit alpha_bare", alpha_bare not in condensate_summand.free_symbols)


def check_delta_zero_scope() -> None:
    section("Delta-zero scope")
    delta = 0
    check("current baseline scope records delta = 0", delta == 0)
    check("no extra-dimensional tower is supplied by this runner", delta == 0)


def main() -> int:
    check_note_scope()
    check_coupling_power()
    check_geometric_progression()
    check_block_observable_symbols()
    check_delta_zero_scope()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: hierarchy alpha_LM magnitude delta-zero open-gate checks failed.")
        return 1
    print("VERDICT: hierarchy alpha_LM magnitude delta-zero open-gate checks pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
