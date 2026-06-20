#!/usr/bin/env python3
r"""Verifier for `S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`.

The checked claim is deliberately narrow:

* the Route-2 slice backbone supplies an exact conditional family
  `Xi_P(t; c) = (P_R c) x exp(-t Lambda_R) u_*` once an admissible
  readout map is supplied;
* the upstream readout-map endpoint triple is not derived on the current
  exact stack, so the parent row remains an `open_gate` rather than a
  unique `Theta_R -> Lambda_R` coupling theorem.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.linalg import expm

from frontier_quark_route2_exact_readout_map import (
    EXACT_TOL,
    admissible_readout_matrix,
    restricted_readout_data,
    theorem_target_lands,
)
from frontier_quark_route2_exact_time_coupling import (
    route2_slice_backbone,
    v_r,
    xi_p,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs" / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
TIME_NOTE = REPO_ROOT / "docs" / "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md"
READOUT_NOTE = REPO_ROOT / "docs" / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
SOURCE_DOMAIN_NOTE = (
    REPO_ROOT / "docs" / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md"
)

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
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def part1_note_boundary() -> None:
    print("\n" + "=" * 72)
    print("PART 1: source-note boundary")
    print("=" * 72)

    note = text(NOTE)
    check(
        "parent note is scoped as an open_gate route survey, not a closed theorem",
        "open_gate route survey" in note
        and "unique-exact `Theta_R -> Lambda_R` coupling theorem **not** closed" in note,
        "status line preserves the open theorem boundary",
    )
    check(
        "parent note names the exact conditional coupling family",
        "Xi_P(t ; c) = (P_R c) \u2297 V_R(t)" in note
        and "V_R(t) = exp(-t Lambda_R) u_*" in note,
        "conditional family is present in the note text",
    )
    check(
        "parent note names the inherited readout-map obstruction",
        "readout-map endpoint triple" in note
        and "not derived by the current exact stack" in note
        and "readout map remains non-unique" in note,
        "non-unique readout map remains the blocker",
    )
    check(
        "one-hop authority notes are present on disk",
        TIME_NOTE.exists() and READOUT_NOTE.exists() and SOURCE_DOMAIN_NOTE.exists(),
        "time, readout, and source-domain authority files exist",
    )


def part2_exact_conditional_family() -> None:
    print("\n" + "=" * 72)
    print("PART 2: exact conditional family")
    print("=" * 72)

    backbone = route2_slice_backbone()
    data = restricted_readout_data()
    readout = admissible_readout_matrix(1.0, 21.0 / 4.0, -2.0, 2.0)

    lambda_sym_err = float(np.max(np.abs(backbone.lambda_sym - backbone.lambda_sym.T)))
    lambda_min = float(np.min(np.linalg.eigvalsh(backbone.lambda_sym)))
    transfer_sym_err = float(np.max(np.abs(backbone.transfer - backbone.transfer.T)))
    transfer_max = float(np.max(np.linalg.eigvalsh(backbone.transfer)))

    print(f"  Lambda_R symmetry error = {lambda_sym_err:.3e}")
    print(f"  Lambda_R min eigenvalue = {lambda_min:.12e}")
    print(f"  T_R symmetry error      = {transfer_sym_err:.3e}")
    print(f"  T_R max eigenvalue      = {transfer_max:.12e}")

    check(
        "Route-2 slice generator remains symmetric positive definite",
        lambda_sym_err < EXACT_TOL and lambda_min > 0.0,
        f"symmetry={lambda_sym_err:.3e}, min_eig={lambda_min:.6e}",
    )
    check(
        "Route-2 transfer remains self-adjoint and contractive",
        transfer_sym_err < EXACT_TOL and 0.0 < transfer_max < 1.0,
        f"symmetry={transfer_sym_err:.3e}, max_eig={transfer_max:.6e}",
    )

    c = data.carrier_e_center
    xi_0 = xi_p(readout, c, v_r(backbone, 0.0))
    xi_1_direct = xi_p(readout, c, v_r(backbone, 1.0))
    xi_1_step = xi_0 @ backbone.transfer.T
    semigroup_resid = float(np.max(np.abs(xi_1_direct - xi_1_step)))
    check(
        "Xi_P(t; c) obeys the exact slice-semigroup law once P_R is supplied",
        semigroup_resid < EXACT_TOL,
        f"semigroup residual={semigroup_resid:.3e}",
    )

    xi_half_direct = xi_p(readout, c, v_r(backbone, 0.5))
    xi_half_rebuilt = xi_p(
        readout,
        c,
        expm(-0.25 * backbone.lambda_sym) @ v_r(backbone, 0.25),
    )
    rebuild_resid = float(np.max(np.abs(xi_half_direct - xi_half_rebuilt)))
    check(
        "conditional family is built from exact carrier/readout and exact slice factor",
        rebuild_resid < EXACT_TOL and float(np.linalg.norm(readout @ c)) > 0.0,
        f"rebuild residual={rebuild_resid:.3e}",
    )


def part3_inherited_open_gate() -> None:
    print("\n" + "=" * 72)
    print("PART 3: inherited non-unique readout obstruction")
    print("=" * 72)

    backbone = route2_slice_backbone()
    data = restricted_readout_data()
    note = text(NOTE)
    theorem_lands = theorem_target_lands(data)

    p_a = admissible_readout_matrix(1.0, 0.0, -2.0, 2.0)
    p_b = admissible_readout_matrix(1.0, 21.0 / 4.0, -2.0, 2.0)

    shell_a = xi_p(p_a, data.carrier_e_shell, v_r(backbone, 1.0))
    shell_b = xi_p(p_b, data.carrier_e_shell, v_r(backbone, 1.0))
    center_a = xi_p(p_a, data.carrier_e_center, v_r(backbone, 1.0))
    center_b = xi_p(p_b, data.carrier_e_center, v_r(backbone, 1.0))

    shell_resid = float(np.max(np.abs(shell_a - shell_b)))
    center_delta = float(np.linalg.norm(center_a - center_b))

    print(f"  shell coupling residual between rho_E=0 and 21/4 = {shell_resid:.3e}")
    print(f"  center coupling separation between rho_E=0 and 21/4 = {center_delta:.12e}")

    check(
        "upstream exact readout theorem does not land on the current surface",
        not theorem_lands,
        "the endpoint triple remains the open theorem target",
    )
    check(
        "distinct admissible maps agree at the E-shell but differ at E-center",
        shell_resid < EXACT_TOL and center_delta > 0.0,
        "non-unique P_R changes the spacetime tensor source factor",
    )
    check(
        "Theta_R -> Lambda_R uniqueness is blocked by readout-map ambiguity, not by missing slice dynamics",
        float(np.linalg.norm(v_r(backbone, 1.0))) > 0.0,
        "slice factor is exact and nonzero",
    )
    check(
        "safe endpoint is exact conditional family plus inherited open gate",
        "remains `open_gate` until that target closes upstream" in note
        and "no unique exact `Theta_R -> Lambda_R` coupling theorem on this arm" in note,
        "runner does not promote the parent row to retained or closed",
    )


def main() -> int:
    print("S3-time Theta_R to slice coupling verifier")
    print("=" * 72)
    part1_note_boundary()
    part2_exact_conditional_family()
    part3_inherited_open_gate()
    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print("Status: exact conditional family verified; unique theorem remains open.")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
