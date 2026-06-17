#!/usr/bin/env python3
"""Gamma-threshold obstruction for the interacting emergent-Lorentz lane.

This runner proves a narrow negative boundary for the conditional one-loop
velocity-attractor packet.  The supplied RG algebra gives

    delta_IR = delta_UV * (mu / M)^gamma,    gamma > 0.

Attraction alone does not certify a Lorentz-violation tolerance.  A fixed
tolerance epsilon < delta_UV requires a quantitative lower bound on gamma.
The current conditional packet supplies positivity, not that lower bound.
"""

from __future__ import annotations

import math
from pathlib import Path


PASS = 0
FAIL = 0
TOL = 1.0e-12


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{status}] {label}{suffix}")


def damped_residual(delta_uv: float, ratio: float, gamma: float) -> float:
    return delta_uv * ratio**gamma


def gamma_threshold(delta_uv: float, epsilon: float, ratio: float) -> float:
    if not (0.0 < ratio < 1.0):
        raise ValueError("ratio must satisfy 0 < mu/M < 1")
    if not (0.0 < epsilon < delta_uv):
        raise ValueError("epsilon must satisfy 0 < epsilon < delta_uv")
    return math.log(epsilon / delta_uv) / math.log(ratio)


def one_loop_matrix_eigenvalues(c_f: float, c_b: float, n_f: int, alpha: float) -> tuple[float, float]:
    """Eigenvalues of the 2x2 velocity RG matrix.

    dv_F/dl = C_F alpha (v_b - v_F)
    dv_b/dl = C_B alpha N_f (v_F - v_b)
    """
    lam = (c_f + c_b * n_f) * alpha
    return (0.0, -lam)


def main() -> int:
    print("Emergent-Lorentz gamma sufficiency threshold obstruction")

    delta_uv = 1.0
    epsilon = 1.0e-12
    ratio = 1.0e-16
    gamma_star = gamma_threshold(delta_uv, epsilon, ratio)

    check(
        "G1 threshold gamma is positive for 0 < epsilon/delta < 1 and 0 < mu/M < 1",
        gamma_star > 0.0,
        detail=f"gamma_*={gamma_star:.6f}",
    )
    check(
        "G2 threshold is exact: gamma_* lands exactly on epsilon",
        abs(damped_residual(delta_uv, ratio, gamma_star) - epsilon) / epsilon < 1.0e-12,
        detail=f"delta_IR={damped_residual(delta_uv, ratio, gamma_star):.3e}",
    )
    check(
        "G3 any smaller positive gamma can fail the tolerance",
        damped_residual(delta_uv, ratio, gamma_star / 2.0) > epsilon,
        detail=f"half-threshold residual={damped_residual(delta_uv, ratio, gamma_star / 2.0):.3e}",
    )
    check(
        "G4 any larger gamma succeeds for the same fixed tolerance",
        damped_residual(delta_uv, ratio, 2.0 * gamma_star) < epsilon,
        detail=f"double-threshold residual={damped_residual(delta_uv, ratio, 2.0 * gamma_star):.3e}",
    )

    c_f = 1.0
    c_b = 1.0
    n_f = 1
    alpha_small = gamma_star / (2.0 * (c_f + c_b * n_f))
    ev0, ev1 = one_loop_matrix_eigenvalues(c_f, c_b, n_f, alpha_small)
    check(
        "G5 supplied one-loop flow remains attractive for arbitrarily small positive alpha",
        ev0 == 0.0 and ev1 < 0.0,
        detail=f"alpha={alpha_small:.6f}, eigenvalues=({ev0:.1f},{ev1:.6f})",
    )
    check(
        "G6 attractive-but-small example still fails the fixed tolerance",
        damped_residual(delta_uv, ratio, (c_f + c_b * n_f) * alpha_small) > epsilon,
        detail="positivity alone gives no lower bound",
    )

    for local_ratio in (1.0e-3, 1.0e-9, 1.0e-30):
        local_star = gamma_threshold(delta_uv, epsilon, local_ratio)
        local_alpha = local_star / (4.0 * (c_f + c_b * n_f))
        local_gamma = (c_f + c_b * n_f) * local_alpha
        check(
            f"G7 no-positive-lower-bound obstruction at hierarchy ratio {local_ratio:g}",
            0.0 < local_gamma < local_star
            and damped_residual(delta_uv, local_ratio, local_gamma) > epsilon,
            detail=f"gamma={local_gamma:.6f} < gamma_*={local_star:.6f}",
        )

    shallow_star = gamma_threshold(delta_uv, epsilon, 1.0e-6)
    deep_star = gamma_threshold(delta_uv, epsilon, 1.0e-18)
    check(
        "G8 deeper hierarchy lowers but does not remove the positive gamma threshold",
        0.0 < deep_star < shallow_star,
        detail=f"gamma_*(1e-18)={deep_star:.6f} < gamma_*(1e-6)={shallow_star:.6f}",
    )

    note = Path("docs/EMERGENT_LORENTZ_GAMMA_SUFFICIENCY_THRESHOLD_NO_GO_NOTE_2026-06-17.md").read_text()
    parent = Path("docs/EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md").read_text()
    note_flat = " ".join(note.split())
    check(
        "G9 note records no audit-status change",
        "does not set or predict an audit outcome" in note_flat
        and "audit lane owns" in note_flat,
    )
    check(
        "G10 note names the exact parent blocker being pruned",
        "physical anomalous-dimension/sufficiency comparison" in note
        and "emergent_lorentz_interacting_velocity_rg_attractor_note_2026-06-06" in note,
    )
    check(
        "G11 parent row still declares the sufficiency bound open",
        "physical fixed-point anomalous dimension" in parent
        and "sufficiency bound" in parent,
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
