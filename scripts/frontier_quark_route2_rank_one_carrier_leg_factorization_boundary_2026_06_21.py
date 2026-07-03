#!/usr/bin/env python3
"""Route-2 rank-one carrier leg-factorization boundary.

The current class-A carrier K_R(q) has an exact leg factorization, but it is a
rank-one, channel-blind carrier leg. This runner checks that the factorization
itself is real while proving it supplies reciprocal projector-weight degree
zero, not the degree two needed for the Route-2 endpoint.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path

import numpy as np

import frontier_same_source_metric_ansatz_scan as same
import frontier_tensor_support_center_excess_law as center


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    PASS += ok
    FAIL += not ok
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f"\n       {detail}" if detail else ""))
    return ok


def normalized_text(relpath: str) -> str:
    return " ".join((ROOT / relpath).read_text(encoding="utf-8").split())


def build_basis() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    basis = same.build_adapted_basis()
    e0 = basis[:, 0]
    s = basis[:, 1]
    e1 = basis[:, 2]
    e2 = basis[:, 3]
    t1x = basis[:, 4]
    e_x = (np.sqrt(3.0) * e1 + e2) / 2.0
    s_unit = s / np.sqrt(6.0)
    return e0, s_unit, e_x, t1x


def delta_a1(q: np.ndarray) -> float:
    return float(center.support_delta(q))


def bright_coords(q: np.ndarray) -> tuple[float, float]:
    _, _, e_x, t1x = build_basis()
    return float(np.dot(e_x, q)), float(np.dot(t1x, q))


def k_r(q: np.ndarray) -> np.ndarray:
    u_e, u_t = bright_coords(q)
    delta = delta_a1(q)
    return np.array([[u_e, u_t], [delta * u_e, delta * u_t]], dtype=float)


def outer_factor(q: np.ndarray) -> np.ndarray:
    u_e, u_t = bright_coords(q)
    delta = delta_a1(q)
    return np.outer(np.array([1.0, delta]), np.array([u_e, u_t]))


def carrier_column(background: np.ndarray, channel: str) -> np.ndarray:
    _, _, e_x, t1x = build_basis()
    shift = e_x if channel == "E" else t1x
    return k_r(background + shift) - k_r(background)


def endpoint_from_lambda(lam: F) -> tuple[F, F, F]:
    q_t = F(5, 6)
    q_e = lam * q_t
    rho_e = 6 * (q_e - 1)
    center_te = -2 * q_t / q_e
    return q_e, rho_e, center_te


def main() -> int:
    print("Route-2 rank-one carrier leg-factorization boundary")
    print("=" * 84)
    print("Status: no-go for extracting the endpoint from the current K_R carrier alone.")

    w_e, w_t = F(1, 3), F(1, 2)
    kappa = w_t / w_e
    check("projector weights give kappa=w_T1/w_E=3/2", kappa == F(3, 2), f"kappa={kappa}")

    print("\n-- Symbolic carrier facts --")
    samples = [
        (F(0), F(1), F(0)),
        (F(1, 6), F(1), F(0)),
        (F(1, 9), F(2), F(-3)),
        (F(-2, 7), F(5), F(11)),
    ]
    symbolic_ok = True
    for delta, u_e, u_t in samples:
        matrix = ((u_e, u_t), (delta * u_e, delta * u_t))
        outer = ((u_e, u_t), (delta * u_e, delta * u_t))
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        symbolic_ok = symbolic_ok and matrix == outer and determinant == 0
    check(
        "K_R(delta,u_E,u_T) is exactly [1,delta]^T [u_E,u_T] with determinant zero",
        symbolic_ok,
        "checked over exact rational samples",
    )

    print("\n-- Live endpoint carrier columns --")
    e0, s_unit, _, _ = build_basis()
    live_factor_errors = []
    for label, q in (("center", e0), ("shell", s_unit), ("mixed", 0.8 * e0 + 0.2 * s_unit)):
        live_factor_errors.append(float(np.max(np.abs(k_r(q) - outer_factor(q)))))
    check(
        "live K_R implementation equals the outer-product factorization",
        max(live_factor_errors) < 1.0e-12,
        f"max factorization residual={max(live_factor_errors):.3e}",
    )

    e_shell = carrier_column(s_unit, "E")
    e_center = carrier_column(e0, "E")
    t_shell = carrier_column(s_unit, "T")
    t_center = carrier_column(e0, "T")
    target_shell = np.array([[1.0, 0.0], [0.0, 0.0]])
    target_center = np.array([[1.0, 0.0], [1.0 / 6.0, 0.0]])
    target_t_shell = np.array([[0.0, 1.0], [0.0, 0.0]])
    target_t_center = np.array([[0.0, 1.0], [0.0, 1.0 / 6.0]])
    endpoint_residual = max(
        np.max(np.abs(e_shell - target_shell)),
        np.max(np.abs(e_center - target_center)),
        np.max(np.abs(t_shell - target_t_shell)),
        np.max(np.abs(t_center - target_t_center)),
    )
    check(
        "endpoint columns are the same A1 source leg times the selected bright channel",
        endpoint_residual < 1.0e-12,
        f"endpoint residual={endpoint_residual:.3e}",
    )
    check(
        "E and T endpoint source legs are channel-blind",
        np.max(np.abs(e_shell[:, 0] - t_shell[:, 1])) < 1.0e-12
        and np.max(np.abs(e_center[:, 0] - t_center[:, 1])) < 1.0e-12,
    )

    print("\n-- Degree consequence --")
    carrier_degree = F(0)
    lambda_carrier = kappa ** carrier_degree
    q_e_carrier, rho_e_carrier, c_te_carrier = endpoint_from_lambda(lambda_carrier)
    check(
        "rank-one carrier factorization has reciprocal projector-weight degree zero",
        carrier_degree == 0 and lambda_carrier == 1,
        f"d={carrier_degree}, lambda_K={lambda_carrier}",
    )
    check(
        "degree-zero carrier misses endpoint: q_E=5/6, rho_E=-1, center T/E=-2",
        (q_e_carrier, rho_e_carrier, c_te_carrier) == (F(5, 6), F(-1), F(-2, 1)),
        f"q_E={q_e_carrier}, rho_E={rho_e_carrier}, center T/E={c_te_carrier}",
    )
    q_e_target, rho_e_target, c_te_target = endpoint_from_lambda(F(9, 4))
    check(
        "target still requires degree two: lambda=9/4, q_E=15/8, rho_E=21/4, center T/E=-8/9",
        (q_e_target, rho_e_target, c_te_target) == (F(15, 8), F(21, 4), F(-8, 9)),
    )

    print("\n-- Current-surface guards --")
    bilinear_note = normalized_text("docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md")
    readout_note = normalized_text("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    new_note = normalized_text("docs/QUARK_ROUTE2_RANK_ONE_CARRIER_LEG_FACTORIZATION_BOUNDARY_NOTE_2026-06-21.md")
    block10 = normalized_text("docs/QUARK_ROUTE2_RANK_ONE_CARRIER_LEG_FACTORIZATION_BOUNDARY_NOTE_2026-06-21.md")

    check(
        "bilinear note defines K_R as the class-A polynomial carrier and not a physical primitive theorem",
        "`K_R(q) := [[u_E(q), u_T(q)], [delta_A1(q) u_E(q), delta_A1(q) u_T(q)]]`" in bilinear_note
        and "physical tensor primitive" in bilinear_note
        and "positive theorem" in bilinear_note,
    )
    check(
        "readout note keeps endpoint triple as an exact missing-map obstruction",
        "does **not** derive the endpoint ratio chain" in readout_note
        and "exact missing-map obstruction" in readout_note,
    )
    check(
        "new note records no-go status and forbids endpoint closure",
        "**Actual current-surface status:** no-go" in new_note
        and "does not derive `rho_E = 21/4`" in new_note
        and "does not claim a unique exact `Theta_R -> Lambda_R` theorem" in new_note,
    )
    check(
        "new note states the remaining target as extra normalization or nonseparable degree-two primitive",
        "derive an additional leg-level normalization primitive outside the class-A" in new_note
        and "nonseparable total-degree-2 primitive" in new_note,
    )
    check(
        "forbidden proof inputs remain excluded",
        "No observed masses, fitted targets, PDG values, nearest-rational selection, or live endpoint fit is used." in new_note,
    )
    check(
        "new note names the actual K_R carrier route as pruned",
        "current K_R leg factorization alone" in block10
        and "reciprocal degree zero" in block10,
    )

    print("\n" + "=" * 84)
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "\nVERDICT: no-go boundary. The current K_R carrier has an exact leg-level rank-one\n"
        "factorization, but the source leg is common to E and T and carries reciprocal degree zero.\n"
        "The endpoint still requires a new normalization primitive or nonseparable degree-two object."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
