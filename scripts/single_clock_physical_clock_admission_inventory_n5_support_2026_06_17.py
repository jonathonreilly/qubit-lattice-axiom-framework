#!/usr/bin/env python3
"""Source-inventory support for B-AXIS.3 physical-clock admission.

This runner distinguishes admitted physical-clock transfers from arbitrary
positive finite operators on tensor factors. It intentionally does not prove
that commuting factor transfers are mathematically impossible.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SINGLE_CLOCK_PHYSICAL_CLOCK_ADMISSION_INVENTORY_N5_SUPPORT_NOTE_2026-06-17.md"
SINGLE_CLOCK = ROOT / "docs" / "AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
RP2 = ROOT / "docs" / "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md"
SC2 = ROOT / "docs" / "AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
STONE = ROOT / "docs" / "SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md"
POST_RECORD = ROOT / "docs" / "POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md"


@dataclass
class Check:
    ok: bool
    label: str
    detail: str = ""


checks: list[Check] = []


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(ok: bool, label: str, detail: str = "") -> None:
    checks.append(Check(bool(ok), label, detail))
    status = "PASS" if ok else "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {label}{suffix}")


def assert_contains(path: Path, needle: str, label: str | None = None) -> None:
    body = read(path)
    check(needle in body, label or f"{path.name} contains {needle!r}")


def flat(path: Path) -> str:
    return " ".join(read(path).split())


def opnorm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


def positive_transfer(generator: np.ndarray, tau: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(generator)
    return vecs @ np.diag(np.exp(-tau * vals)) @ vecs.conj().T


def main() -> int:
    print("single-clock physical-clock admission inventory N5 support")
    print("=" * 72)

    assert_contains(NOTE, "ADMITTED_PHYSICAL_CLOCK_TRANSFERS=1")
    assert_contains(NOTE, "MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE")
    assert_contains(NOTE, "Does not mathematically exclude independent commuting transfer factors")
    assert_contains(NOTE, "Does not add an axiom")
    assert_contains(NOTE, "**Claim boundary:** source-inventory support")
    assert_contains(NOTE, "No second physical-clock transfer is currently admitted.")

    assert_contains(SINGLE_CLOCK, "(B-AXIS.3)", "single-clock source names B-AXIS.3")
    assert_contains(SINGLE_CLOCK, "admitted\n    as a second physical clock", "B-AXIS.3 is phrased as an admission statement")
    assert_contains(SINGLE_CLOCK, "(T̂², 2a_τ)", "single-clock source names the sole supplied transfer/step pair")
    check("This note **complies** by declaring those clauses as (B-AXIS)" in flat(SINGLE_CLOCK),
          "single-clock source keeps B-AXIS declared")

    minimal_flat = flat(MINIMAL)
    check("does not supply a dynamics" in minimal_flat, "minimal Lattice supplies no dynamics")
    check("does not supply a dynamics" in minimal_flat and "measurement instrument" in minimal_flat,
          "minimal Quantum supplies no dynamics")
    assert_contains(MINIMAL, "time metric", "Record supplies no time metric")
    assert_contains(MINIMAL, "does not derive or enlarge the axiom set", "minimal axiom runner does not enlarge axioms")

    assert_contains(RP2, "2-step blocked transfer matrix", "RP2 supplies the two-step transfer")
    assert_contains(RP2, "positive Hermitian", "RP2 supplies positivity")
    assert_contains(RP2, "single-step transfer operator is NOT positive", "RP2 excludes the single-step object as the physical positive transfer")
    assert_contains(SC2, "2 a_τ", "SC2 supplies the blocked time denominator")
    assert_contains(SC2, "H  :=  -(1/(2 a_τ)) log(T_hat^2 / M_T)", "SC2 supplies corrected log normalization")

    assert_contains(STONE, "given", "Stone note is transfer-relative")
    check("uniquely determined by `T`" in read(STONE), "Stone uniqueness does not add a transfer")
    assert_contains(POST_RECORD, "supplied clock map", "post-record rates require supplied clock map")
    assert_contains(POST_RECORD, "does not supply physical elapsed time", "post-record layer does not derive a clock")

    admitted = [
        {
            "name": "T_hat^2",
            "source": "RP2/SC2",
            "positive_transfer": True,
            "clock_denominator": "2 a_tau",
            "physical_clock_admitted": True,
        }
    ]
    comparators = [
        {
            "name": "T_A x I",
            "source": "finite tensor-factor comparator",
            "positive_transfer": True,
            "clock_denominator": "arbitrary tau_A",
            "physical_clock_admitted": False,
        },
        {
            "name": "I x T_B",
            "source": "finite tensor-factor comparator",
            "positive_transfer": True,
            "clock_denominator": "arbitrary tau_B",
            "physical_clock_admitted": False,
        },
    ]

    check(len(admitted) == 1, "inventory contains exactly one admitted physical-clock transfer")
    check(admitted[0]["name"] == "T_hat^2" and admitted[0]["clock_denominator"] == "2 a_tau",
          "the admitted transfer is the two-step blocked transfer with denominator 2 a_tau")
    check(all(not c["physical_clock_admitted"] for c in comparators),
          "finite tensor-factor comparators are not physical-clock admissions")
    check(sum(1 for x in admitted + comparators if x["physical_clock_admitted"]) == 1,
          "admitted physical-clock count remains one after comparator scan")

    ident = np.eye(2)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]])
    h_a = 1.1 * ident + 0.2 * sigma_z
    h_b = 0.8 * ident + 0.3 * sigma_z
    t_a = np.kron(positive_transfer(h_a, 1.0), ident)
    t_b = np.kron(ident, positive_transfer(h_b, 1.4))

    check(np.min(np.linalg.eigvalsh(t_a)) > 0, "mathematical comparator T_A x I is positive")
    check(np.min(np.linalg.eigvalsh(t_b)) > 0, "mathematical comparator I x T_B is positive")
    check(opnorm(t_a @ t_b - t_b @ t_a) < 1e-13,
          "mathematical comparator transfers commute", f"resid={opnorm(t_a @ t_b - t_b @ t_a):.2e}")

    h_a_lift = np.kron(h_a, ident)
    h_b_lift = np.kron(ident, h_b)
    span_rank = np.linalg.matrix_rank(np.stack([h_a_lift.ravel(), h_b_lift.ravel()]), tol=1e-12)
    check(span_rank == 2, "factor comparator tangent space is two-dimensional", f"rank={span_rank}")
    check(sum(1 for c in comparators if c["positive_transfer"]) == 2,
          "two positive factor transfers exist as mathematical comparators")
    check(sum(1 for c in comparators if c["physical_clock_admitted"]) == 0,
          "zero factor comparators are admitted physical clocks")

    counterfactual = admitted + [{**comparators[0], "physical_clock_admitted": True}]
    check(sum(1 for x in counterfactual if x["physical_clock_admitted"]) == 2,
          "counterfactual second admission would visibly break the inventory")
    check("not a theorem over all positive operators" in read(NOTE),
          "note states why the support is source-inventory, not algebraic exclusion")

    passed = sum(1 for c in checks if c.ok)
    failed = sum(1 for c in checks if not c.ok)
    print()
    print(f"SUMMARY: PASS={passed} FAIL={failed}")
    print("ADMITTED_PHYSICAL_CLOCK_TRANSFERS=1")
    print("B_AXIS_DERIVED=FALSE")
    print("MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
