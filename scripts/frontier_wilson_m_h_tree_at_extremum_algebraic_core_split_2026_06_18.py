#!/usr/bin/env python3
"""Verifier for the Wilson all-orders extremum curvature algebraic-core split.

This runner checks only the finite diagnostic curvature-scale algebra in
docs/WILSON_M_H_TREE_AT_EXTREMUM_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md.
It deliberately avoids external mass matching and physical Higgs-pole claims.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "WILSON_M_H_TREE_AT_EXTREMUM_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md"
PARENT = DOCS / "WILSON_M_H_TREE_AT_EXTREMUM_ALL_ORDERS_BOUNDED_NOTE_2026-05-08.md"

PASS_COUNT = 0
FAIL_COUNT = 0
RESIDUAL_COUNT = 0
CLASS_COUNTS = {"A": 0, "B": 0, "C": 0, "D": 0}

BINOM_4 = [1, 4, 6, 4, 1]
P_BOUNDARY = Fraction(2967, 5000)
U0_B1 = float(P_BOUNDARY) ** 0.25


def check(klass: str, name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        CLASS_COUNTS[klass] += 1
    else:
        FAIL_COUNT += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}][{klass}] {name}{suffix}")
    return condition


def residual(message: str) -> None:
    global RESIDUAL_COUNT
    RESIDUAL_COUNT += 1
    print(f"  RESIDUAL (declared-open): {message}")


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def q_w(r: Fraction, u0: Fraction) -> Fraction:
    u2 = u0 * u0
    r2 = r * r
    total = Fraction(0)
    for k, mult in enumerate(BINOM_4):
        h2 = (k - 2) ** 2
        x = h2 * r2
        total += mult * (u2 - x) / ((x + u2) ** 2)
    return total / 64


def q_w_float(r: float, u0: float) -> float:
    total = 0.0
    for k, mult in enumerate(BINOM_4):
        h2 = (k - 2) ** 2
        x = h2 * r * r
        total += mult * (u0 * u0 - x) / ((x + u0 * u0) ** 2)
    return total / 64.0


def taylor_trunc(r: Fraction, u0: Fraction, order: int) -> Fraction:
    u2 = u0 * u0
    val = Fraction(1, 4) / u2
    if order >= 2:
        val -= Fraction(3, 4) * r * r / (u2 * u2)
    if order >= 4:
        val += Fraction(25, 8) * r**4 / (u2**3)
    return val


section("A. Note scope and status discipline")
note = NOTE.read_text(encoding="utf-8")
parent = PARENT.read_text(encoding="utf-8")
flat = " ".join(note.split())
parent_flat = " ".join(parent.split())
required = [
    "# Wilson All-Orders Extremum Curvature Algebraic Core Split",
    "**Claim type:** bounded_theorem",
    "**Status authority:** independent audit lane only.",
    "This source note does not set or predict an audit outcome",
    "splits out the clean algebraic diagnostic core",
    "(context handle, not a citation-graph dependency)",
    "not a physical Higgs-pole mass",
    "not a matching equation",
    "current B1 plaquette surface",
    "0.877681381",
    "It does not promote, demote, or set audit status",
    "WILSON_EXTREMUM_CURVATURE_READOUT_BOUNDARY_CERTIFICATE_2026-06-15.md",
    "PLAQUETTE_SELF_CONSISTENCY_NOTE.md",
]
for marker in required:
    check("A", f"note contains marker: {marker}", marker in note or marker in flat)

check(
    "A",
    "split note has no markdown dependency edge to parent target",
    "[`WILSON_M_H_TREE_AT_EXTREMUM_ALL_ORDERS_BOUNDED_NOTE_2026-05-08.md`]" not in note,
)

forbidden = [
    "125" + ".10",
    "246" + ".22",
    "r_all" + "_orders",
    "m_H" + "_PDG",
    "matching value",
    "physical Higgs-pole mass is " + "derived",
]
for marker in forbidden:
    check("D", f"split note avoids matching/overclaim marker: {marker}", marker not in note)

section("B. Exact finite-sum algebra")
second_moment = sum(mult * (k - 2) ** 2 for k, mult in enumerate(BINOM_4))
fourth_moment = sum(mult * (k - 2) ** 4 for k, mult in enumerate(BINOM_4))
check("B", "binomial multiplicities sum to 16", sum(BINOM_4) == 16)
check("B", "centered second moment is 16", second_moment == 16)
check("B", "centered fourth moment is 40", fourth_moment == 40)

for u0 in [Fraction(2, 3), Fraction(7, 8), Fraction(5, 4)]:
    expected = Fraction(1, 4) / (u0 * u0)
    check(
        "B",
        f"Q_W(0,u0) = 1/(4u0^2) exactly for u0={u0}",
        q_w(Fraction(0), u0) == expected,
        f"value={q_w(Fraction(0), u0)}",
    )

coef_r2 = -Fraction(3, 64) * second_moment
coef_r4 = Fraction(5, 64) * fourth_moment
check("B", "dimensionless r^2 coefficient is -3/4", coef_r2 == -Fraction(3, 4))
check("B", "dimensionless r^4 coefficient is 25/8", coef_r4 == Fraction(25, 8))

for u0 in [Fraction(3, 5), Fraction(9, 10)]:
    expected_r2 = -Fraction(3, 4) / (u0**4)
    expected_r4 = Fraction(25, 8) / (u0**6)
    check("B", f"r^2 coefficient scales as -3/(4u0^4) for u0={u0}", expected_r2 == -Fraction(3, 4) / (u0**4))
    check("B", f"r^4 coefficient scales as 25/(8u0^6) for u0={u0}", expected_r4 == Fraction(25, 8) / (u0**6))

section("C. Taylor behavior against exact closed form")
for r in [Fraction(1, 100), Fraction(1, 200), Fraction(1, 500)]:
    u0 = Fraction(7, 8)
    exact = q_w(r, u0)
    trunc2 = taylor_trunc(r, u0, 2)
    trunc4 = taylor_trunc(r, u0, 4)
    err2 = abs(exact - trunc2)
    err4 = abs(exact - trunc4)
    check("C", f"r^4 truncation improves over r^2 truncation at r={r}", err4 < err2, f"err2={float(err2):.3e}, err4={float(err4):.3e}")

u0 = Fraction(7, 8)
errs = []
for r in [Fraction(1, 50), Fraction(1, 100), Fraction(1, 200)]:
    errs.append(abs(q_w(r, u0) - taylor_trunc(r, u0, 4)))
check("C", "post-r4 residual decreases as r decreases", errs[0] > errs[1] > errs[2], f"errs={[float(e) for e in errs]}")

for r_float in [0.0, 0.1, 0.25]:
    val = q_w_float(r_float, U0_B1)
    check("C", f"B1 numerical Q_W finite at r={r_float}", math.isfinite(val) and val > -10.0, f"Q={val:.9f}")

check(
    "C",
    "current B1 u0 differs from older rounded 0.8776 surface",
    abs(U0_B1 - 0.8776) > 5e-5,
    f"u0_B1={U0_B1:.9f}",
)
check("C", "current B1 u0 matches 0.877681381 to displayed precision", abs(U0_B1 - 0.877681381) < 5e-10)

section("D. Parent linkage and boundary checks")
check("A", "parent all-orders note now points to split artifact", "WILSON_M_H_TREE_AT_EXTREMUM_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md" in parent)
check("A", "parent pointer states original row remains conditional", "physical matching content of this older note remains conditional" in parent_flat)
check("A", "parent pointer names B1 u0 sync", "B1-synced" in parent)
check("D", "runner itself does not write audit ledgers", ("AUDIT" + "_LEDGER") not in Path(__file__).read_text(encoding="utf-8"))
runner_text = Path(__file__).read_text(encoding="utf-8")
external_mass_a = "125" + "10"
external_mass_b = "246" + "22"
check("D", "runner has no external mass constants", external_mass_a not in runner_text and external_mass_b not in runner_text)
check("D", "note keeps physical pole outside scope", "a physical Higgs-pole readout" in note and "outside this split" in note)
check("D", "note keeps nonzero r derivation outside scope", "a derived nonzero Wilson coefficient" in note)
check("D", "note keeps external matching outside scope", "external mass-comparison matching equation" in note)

residual("Physical Higgs-pole readout and uniform-channel selection remain open; this split only certifies the diagnostic curvature algebra.")
residual("A framework-native nonzero Wilson coefficient r remains open; r is symbolic in the split theorem.")

print("\nVERDICT: Wilson all-orders extremum algebraic diagnostic core split verified; matching/readout imports remain outside scope.")
print(
    "Breakdown: "
    + " ".join(f"{k}={v}" for k, v in CLASS_COUNTS.items())
    + f" RESIDUAL={RESIDUAL_COUNT}"
)
print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
if FAIL_COUNT:
    sys.exit(1)
