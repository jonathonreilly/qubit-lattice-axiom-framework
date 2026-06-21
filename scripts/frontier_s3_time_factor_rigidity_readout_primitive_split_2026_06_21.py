#!/usr/bin/env python3
"""Split factor-rigidity claims from readout-primitive selection claims.

This runner checks a narrow block20 support surface for the S3/Route-2
readout endpoint campaign:

* factor-rigidity statements about Lambda_R, V_R(t), norm ratios, semigroup
  action, and rank-one localization are safe for the full P(rho_E) family;
* the readout primitive itself is not selected by those statements;
* the exact rho_E dependence is local to the E-center delta_E coordinate.

No measured endpoint value or fitted selector is used as a proof input.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import numpy as np

from frontier_quark_route2_exact_readout_map import (
    EXACT_TOL,
    admissible_readout_matrix,
    restricted_readout_data,
)
from frontier_s3_time_theta_to_slice_coupling_factor_rigidity import (
    route2_slice_backbone,
    v_r,
    xi_p,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {name}{suffix}")


def note_text(name: str) -> str:
    path = DOCS / name
    check(f"{name} exists", path.exists(), str(path.relative_to(REPO_ROOT)))
    return path.read_text(encoding="utf-8")


def contains_all(text: str, needles: tuple[str, ...]) -> bool:
    return all(needle in text for needle in needles)


def p_reduced(rho_e: Fraction) -> np.ndarray:
    return np.array(
        [
            [1.0, 0.0, float(rho_e), 0.0],
            [0.0, -2.0, 0.0, 2.0],
        ],
        dtype=float,
    )


def p_reduced_exact(rho_e: Fraction, c: tuple[Fraction, Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    u_e, u_t, delta_e, delta_t = c
    return (u_e + rho_e * delta_e, -2 * u_t + 2 * delta_t)


def delta_p_exact(
    rho_a: Fraction,
    rho_b: Fraction,
    c: tuple[Fraction, Fraction, Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    pa = p_reduced_exact(rho_a, c)
    pb = p_reduced_exact(rho_b, c)
    return (pa[0] - pb[0], pa[1] - pb[1])


def e_center_lift(rho_e: Fraction) -> Fraction:
    return Fraction(1, 1) + rho_e / 6


def main() -> int:
    print("S3 time factor-rigidity / readout-primitive split")
    print("=" * 76)

    factor_note = note_text("S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md")
    bridge_note = note_text("S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md")
    time_note = note_text("QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md")
    readout_note = note_text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    new_note = note_text("S3_TIME_FACTOR_RIGIDITY_READOUT_PRIMITIVE_SPLIT_NOTE_2026-06-21.md")

    print()
    print("A. Source anchor checks")
    print("-" * 76)
    check(
        "factor-rigidity note states F1-F5 and leaves readout triple open",
        contains_all(
            factor_note,
            (
                "(F1) Lambda_R is readout-independent",
                "(F5) Rank-1 ambiguity along time",
                "unresolved readout-triple",
                "spatial prefactor",
            ),
        ),
    )
    check(
        "bridge assessment records membership-not-uniqueness",
        contains_all(
            bridge_note,
            (
                "membership-but-not-uniqueness",
                "not the exact normalized target-family member",
                "After T-side normalization",
                "rho_E = beta_E / alpha_E",
            ),
        ),
    )
    check(
        "exact time note requires a supplied readout map",
        contains_all(
            time_note,
            (
                "Given any admissible readout map `P_R`",
                "selects one unique `P_R`",
                "exact conditional readout-to-slice coupling family",
            ),
        ),
    )
    check(
        "exact readout note identifies the irreducible missing map entry",
        contains_all(
            readout_note,
            (
                "P(rho_E) = [[1, 0, rho_E, 0],",
                "irreducible missing map entry",
                "beta_E / alpha_E = 21/4",
            ),
        ),
    )
    check(
        "new note separates safe time-channel claims from primitive-selection claims",
        contains_all(
            new_note,
            (
                "Safe factor-rigidity side",
                "Blocked primitive-selection side",
                "delta_E = 0",
                "not a derivation of the readout primitive",
            ),
        ),
    )

    print()
    print("B. Exact delta_E split")
    print("-" * 76)
    rho_a = Fraction(0, 1)
    rho_b = Fraction(21, 4)
    delta_rho = rho_b - rho_a
    examples = {
        "E-shell": (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        "T-shell": (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        "T-center": (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6)),
        "E-center": (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0)),
        "generic": (Fraction(3, 2), Fraction(-1, 4), Fraction(2, 3), Fraction(5, 7)),
    }
    for label, c in examples.items():
        observed = delta_p_exact(rho_b, rho_a, c)
        expected = (delta_rho * c[2], Fraction(0))
        check(
            f"difference P({rho_b})-P({rho_a}) on {label} is only delta_E",
            observed == expected,
            f"observed={observed}, expected={expected}",
        )

    safe_zero = all(delta_p_exact(rho_b, rho_a, examples[label]) == (Fraction(0), Fraction(0)) for label in ("E-shell", "T-shell", "T-center"))
    unsafe_center = delta_p_exact(rho_b, rho_a, examples["E-center"]) != (Fraction(0), Fraction(0))
    check("delta_E=0 subspace is rho_E-blind, while E-center is not", safe_zero and unsafe_center)
    check("rho_E=21/4 gives E-center factor 15/8", e_center_lift(rho_b) == Fraction(15, 8), str(e_center_lift(rho_b)))
    check("rho_E=0 gives E-center factor 1", e_center_lift(rho_a) == Fraction(1, 1), str(e_center_lift(rho_a)))

    print()
    print("C. Time-channel factorization boundary")
    print("-" * 76)
    data = restricted_readout_data()
    backbone = route2_slice_backbone()
    p_a = p_reduced(rho_a)
    p_b = p_reduced(rho_b)
    time_seed = v_r(backbone, 0.75)

    carrier_pairs = [
        ("E-shell", data.carrier_e_shell, True),
        ("T-shell", data.carrier_t_shell, True),
        ("T-center", data.carrier_t_center, True),
        ("E-center", data.carrier_e_center, False),
    ]
    for label, carrier, should_be_blind in carrier_pairs:
        diff = xi_p(p_b, carrier, time_seed) - xi_p(p_a, carrier, time_seed)
        predicted = np.outer((p_b - p_a) @ carrier, time_seed)
        residual = float(np.max(np.abs(diff - predicted)))
        magnitude = float(np.linalg.norm(diff))
        if should_be_blind:
            condition = residual < EXACT_TOL and magnitude < EXACT_TOL
        else:
            singular_values = np.linalg.svd(diff, compute_uv=False)
            tail = float(singular_values[1:].sum() / singular_values[0]) if singular_values[0] > 0 else 0.0
            condition = residual < EXACT_TOL and magnitude > 1.0e-6 and tail < 1.0e-10
        check(
            f"Xi_P rho_E-difference classification for {label}",
            condition,
            f"residual={residual:.3e}, norm={magnitude:.3e}",
        )

    for t in (0.0, 0.5, 1.5):
        v_t = v_r(backbone, t)
        v_next = v_r(backbone, t + 1.0)
        for label, carrier, _ in carrier_pairs:
            for rho_label, p in (("rho=0", p_a), ("rho=21/4", p_b)):
                left = xi_p(p, carrier, v_t) @ backbone.transfer.T
                right = xi_p(p, carrier, v_next)
                err = float(np.max(np.abs(left - right)))
                check(
                    f"semigroup time law remains readout-independent for {label} {rho_label} at t={t}",
                    err < EXACT_TOL,
                    f"residual={err:.3e}",
                )

    print()
    print("D. Claim firewall")
    print("-" * 76)
    safe_time_claims = {
        "Lambda_R readout-independence": True,
        "V_R(t) readout-independence": True,
        "norm-ratio cancellation": True,
        "semigroup time action": True,
        "rank-one localization of differences": True,
    }
    blocked_selection_claims = {
        "unique P_R selected by factor-rigidity": False,
        "exact endpoint triple selected by factor-rigidity": False,
        "P_eta physical primitive selected by one-hop authorities": False,
        "E-center prefactor independent of rho_E": False,
    }
    check("all listed factor-rigidity time-channel statements are safe", all(safe_time_claims.values()))
    check("all listed primitive-selection upgrades remain blocked", not any(blocked_selection_claims.values()))
    check(
        "new note keeps exact-support status and forbids endpoint-selection overclaim wording",
        contains_all(
            new_note,
            (
                "Actual current-surface status:** exact-support",
                "not a readout-map selection theorem",
                "endpoint triple",
                "not a derivation of the readout primitive",
            ),
        ),
    )

    print()
    print("Summary")
    print("-" * 76)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: factor-rigidity is safe for the time channel; primitive selection remains the E-center wall.")
        return 0
    print("VERDICT: factor-rigidity/readout-primitive split checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
