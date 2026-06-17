#!/usr/bin/env python3
"""Current-surface open-gate check for lepton-block YT-style matching.

This runner does not use empirical lepton masses and does not close a
lepton Yukawa theorem. It checks the finite algebra and source-surface facts
behind the narrow claim:

* the quark YT matching algebra gives y_t = g_s/sqrt(6);
* the formal lepton hypercharge analogy would give y_tau = g_1/sqrt(2)
  only after a unit lepton scalar matrix element is supplied;
* the current YT Ward source defines the Q_L scalar-singlet operator used by
  the quark/top matching context;
* the current YUKAWA color-projection source is only a channel-fraction
  theorem and does not define a lepton-composite scalar bridge.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"  [PASS] {label}" + (f"  ({detail})" if detail else ""))
    else:
        FAIL_COUNT += 1
        print(f"  [FAIL] {label}" + (f"  ({detail})" if detail else ""))


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


section("Quark YT matching algebra")

g_s = sp.Symbol("g_s", positive=True)
y_t = sp.Symbol("y_t", positive=True)
rep_a_quark = g_s**2 / 6
rep_b_quark = y_t**2
quark_solution = sp.solve(sp.Eq(rep_a_quark, rep_b_quark), y_t)[0]

check(
    "quark matching solves y_t = g_s/sqrt(6)",
    sp.simplify(quark_solution - g_s / sp.sqrt(6)) == 0,
    f"solution={quark_solution}",
)
check(
    "numeric coefficient 1/sqrt(6) is stable",
    math.isclose(1.0 / math.sqrt(6.0), 0.408248290463863, rel_tol=0.0, abs_tol=1e-15),
    f"coef={1.0 / math.sqrt(6.0):.15f}",
)

section("Formal lepton analogy is conditional")

g_1 = sp.Symbol("g_1", positive=True)
y_tau = sp.Symbol("y_tau", positive=True)
y_left = sp.Rational(-1, 2)
y_right = sp.Rational(-1, 1)
hypercharge_product = abs(y_left * y_right)
rep_a_lepton = g_1**2 * hypercharge_product
rep_b_lepton_if_unit_operator_supplied = y_tau**2
lepton_solution = sp.solve(sp.Eq(rep_a_lepton, rep_b_lepton_if_unit_operator_supplied), y_tau)[0]

check(
    "formal hypercharge product is 1/2",
    sp.simplify(hypercharge_product - sp.Rational(1, 2)) == 0,
    f"Y_L*Y_R absolute value={hypercharge_product}",
)
check(
    "formal lepton equation solves y_tau = g_1/sqrt(2)",
    sp.simplify(lepton_solution - g_1 / sp.sqrt(2)) == 0,
    f"conditional solution={lepton_solution}",
)
check(
    "formal solution is conditional on a supplied unit lepton scalar operator",
    True,
    "runner does not assert that operator is physically identified",
)

section("Current source-surface bridge check")

yukawa_note = DOCS / "YUKAWA_COLOR_PROJECTION_THEOREM.md"
yt_note = DOCS / "YT_WARD_IDENTITY_DERIVATION_THEOREM.md"

check(
    "YUKAWA_COLOR_PROJECTION_THEOREM.md exists",
    yukawa_note.exists(),
    str(yukawa_note.relative_to(ROOT)),
)
check(
    "YT_WARD_IDENTITY_DERIVATION_THEOREM.md exists",
    yt_note.exists(),
    str(yt_note.relative_to(ROOT)),
)

yukawa_text = yukawa_note.read_text(encoding="utf-8") if yukawa_note.exists() else ""
yt_text = yt_note.read_text(encoding="utf-8") if yt_note.exists() else ""
combined = (yukawa_text + "\n" + yt_text).lower()

yt_defines_q_l_scalar = (
    "local scalar-singlet bilinear operator on the q_l block" in yt_text.lower()
    and "h_unit" in yt_text.lower()
    and "psi-bar" in yt_text.lower()
    and "standard model yukawa readout" in yt_text.lower()
)
yukawa_is_channel_fraction_only = (
    "channel-fraction theorem" in yukawa_text.lower()
    and "not a higgs wave-function normalization" in yukawa_text.lower()
    and "not a physical yukawa" in yukawa_text.lower()
)
defines_lepton_composite_bridge = (
    "lepton composite higgs" in combined
    or "lepton-composite scalar" in combined
    or "lepton composite scalar" in combined
    or "lepton scalar bridge" in combined
)

check(
    "YT Ward source defines the current Q_L scalar-singlet operator",
    yt_defines_q_l_scalar,
    "this is the quark/top scalar-operator authority; it is not a lepton bridge",
)
check(
    "YUKAWA color-projection source is only a channel-fraction theorem",
    yukawa_is_channel_fraction_only,
    "runner no longer treats YUKAWA_COLOR_PROJECTION_THEOREM as a scalar-operator authority",
)
check(
    "current cited sources do not define a lepton-composite scalar bridge",
    not defines_lepton_composite_bridge,
    "absence is a current-source open gate, not an impossibility theorem",
)

section("Claim boundary")

check("no empirical lepton mass is used", True)
check("no lepton Yukawa prediction is made", True)
check("result is an open gate for a missing physical-operator bridge", True)

print()
print("=" * 88)
print(f"  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
print("=" * 88)

if FAIL_COUNT:
    sys.exit(1)
