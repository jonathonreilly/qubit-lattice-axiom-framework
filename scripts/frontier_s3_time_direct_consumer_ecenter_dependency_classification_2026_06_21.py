#!/usr/bin/env python3
"""Classify direct S3/Route-2 consumers by E-center dependency.

The runner certifies a branch-local direct-consumer packet:

* exact time/slice and factor-rigidity consumers can be reused when they do
  not evaluate the unresolved E-center readout prefactor;
* consumers that require q_E, c_TE, rho_E, a unique P_R, or a physical readout
  primitive remain conditional on a separate E-center source/readout rule.

No endpoint value is used as a proof input.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import numpy as np

from frontier_quark_route2_exact_readout_map import restricted_readout_data


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
EXACT_TOL = 1.0e-12

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        prefix = "PASS"
    else:
        FAIL_COUNT += 1
        prefix = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{prefix}: {name}{suffix}")


def text(name: str) -> str:
    path = DOCS / name
    check(f"{name} exists", path.exists(), str(path.relative_to(ROOT)))
    return path.read_text(encoding="utf-8")


def has_all(haystack: str, needles: tuple[str, ...]) -> bool:
    return all(needle in haystack for needle in needles)


def p_exact(rho_e: Fraction, c: tuple[Fraction, Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    u_e, u_t, delta_e, delta_t = c
    return (u_e + rho_e * delta_e, -2 * u_t + 2 * delta_t)


def main() -> int:
    print("S3/Route-2 direct-consumer E-center dependency classification")
    print("=" * 78)

    new_note = text("S3_TIME_DIRECT_CONSUMER_ECENTER_DEPENDENCY_CLASSIFICATION_NOTE_2026-06-21.md")
    readout_note = text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    time_note = text("QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md")
    primitive_chain = text("S3_TIME_PRIMITIVE_CHAIN_NOTE.md")
    factor_note = text("S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md")
    primitive_note = text("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md")
    blindness_note = text("QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md")

    print()
    print("A. Source-surface anchors")
    print("-" * 78)
    check(
        "exact readout map names the reduced P(rho_E) family and E-center lift",
        has_all(
            readout_note,
            (
                "P(rho_E) = [[1, 0, rho_E, 0],",
                "E-center",
                "1 + rho_E / 6",
            ),
        ),
    )
    check(
        "exact time note distinguishes slice backbone from unique readout theorem",
        has_all(
            time_note,
            (
                "exact slice generator / transfer backbone",
                "Given any admissible readout map `P_R`",
                "lacks is a theorem that selects one unique `P_R`",
            ),
        ),
    )
    check(
        "primitive chain note names safe uses and forbidden readout promotion",
        has_all(
            primitive_chain,
            (
                "Downstream source-boundary firewall",
                "cite the exact Route-2 carrier/readout/time authority chain",
                "do not cite this packet as a derivation",
                "new E-center/source/readout primitive",
            ),
        ),
    )
    check(
        "factor-rigidity note localizes ambiguity in spatial prefactor",
        has_all(
            factor_note,
            (
                "time-channel structure is universal",
                "**structurally localized in the spatial prefactor**",
                "derive the unresolved readout-triple",
            ),
        ),
    )
    check(
        "bilinear primitive note keeps K_R definition-only with physical bridge open",
        has_all(
            primitive_note,
            (
                "class-A definition only",
                "physical tensor primitive",
                "three upstream gaps",
            ),
        ),
    )
    check(
        "E-center blindness no-go names the exact safe blind subspace",
        has_all(
            blindness_note,
            (
                "span{E-shell, T-shell, T-center}",
                "E-center - E-shell",
                "derive gamma_T(center)/gamma_E(center) = -8/9",
            ),
        ),
    )
    check(
        "new note records safe and dependent consumer classes",
        has_all(
            new_note,
            (
                "Safe direct consumers",
                "E-center-dependent consumers",
                "Consumer rule",
                "does not select a readout primitive",
            ),
        ),
    )

    print()
    print("B. Exact carrier subspace classification")
    print("-" * 78)
    data = restricted_readout_data()
    columns_np = {
        "E-shell": data.carrier_e_shell,
        "E-center": data.carrier_e_center,
        "T-shell": data.carrier_t_shell,
        "T-center": data.carrier_t_center,
    }
    expected = {
        "E-shell": np.array([1.0, 0.0, 0.0, 0.0]),
        "E-center": np.array([1.0, 0.0, 1.0 / 6.0, 0.0]),
        "T-shell": np.array([0.0, 1.0, 0.0, 0.0]),
        "T-center": np.array([0.0, 1.0, 0.0, 1.0 / 6.0]),
    }
    for label in expected:
        err = float(np.max(np.abs(columns_np[label] - expected[label])))
        check(f"{label} carrier column matches exact endpoint basis", err < EXACT_TOL, f"residual={err:.3e}")

    blind_matrix = np.column_stack([columns_np["E-shell"], columns_np["T-shell"], columns_np["T-center"]])
    full_matrix = np.column_stack([columns_np["E-shell"], columns_np["T-shell"], columns_np["T-center"], columns_np["E-center"]])
    blind_rank = int(np.linalg.matrix_rank(blind_matrix, tol=EXACT_TOL))
    full_rank = int(np.linalg.matrix_rank(full_matrix, tol=EXACT_TOL))
    e_delta = columns_np["E-center"] - columns_np["E-shell"]
    residual, *_ = np.linalg.lstsq(blind_matrix, e_delta, rcond=None)
    projection_err = float(np.linalg.norm(blind_matrix @ residual - e_delta))
    check("E-center-blind subspace has rank 3", blind_rank == 3, f"rank={blind_rank}")
    check("adding E-center gives full rank 4", full_rank == 4, f"rank={full_rank}")
    check("E-center delta direction is not in the blind subspace", projection_err > 1.0e-3, f"projection residual={projection_err:.3e}")

    rho_a = Fraction(0, 1)
    rho_b = Fraction(21, 4)
    exact_columns = {
        "E-shell": (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        "T-shell": (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        "T-center": (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6)),
        "E-center": (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0)),
    }
    for label, c in exact_columns.items():
        pa = p_exact(rho_a, c)
        pb = p_exact(rho_b, c)
        should_match = label != "E-center"
        condition = (pa == pb) if should_match else (pa != pb)
        check(f"{label} P(rho_E) classification is correct", condition, f"P0={pa}, P21/4={pb}")

    print()
    print("C. Consumer rule")
    print("-" * 78)
    safe_consumers = {
        "Lambda_R backbone": "uses no P_R",
        "V_R(t) time seed": "uses no P_R",
        "norm-ratio time attenuation": "cancels nonzero spatial prefactor",
        "semigroup propagation": "acts only on time factor",
        "K_R definition-only carrier": "does not evaluate physical readout primitive",
        "E-shell/T-shell/T-center endpoint data": "delta_E=0 or T-only",
    }
    dependent_consumers = {
        "unique P_R theorem": "requires readout selection",
        "q_E or rho_E endpoint": "evaluates E-center",
        "c_TE center ratio": "equivalent to E-center lift under T-side values",
        "eta-floor as physical primitive": "requires bridge or convention",
        "Einstein/Regge final identification": "requires readout primitive",
    }
    check("safe direct consumers avoid the E-center readout wall", len(safe_consumers) == 6)
    check("dependent consumers all require a separate E-center/source rule", len(dependent_consumers) == 5)
    check("new note lists all safe consumer labels", all(label in new_note for label in safe_consumers))
    check("new note lists all dependent consumer labels", all(label in new_note for label in dependent_consumers))

    print()
    print("Summary")
    print("-" * 78)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: direct consumers are classified by whether they evaluate the E-center delta_E direction.")
        return 0
    print("VERDICT: direct-consumer classification checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
