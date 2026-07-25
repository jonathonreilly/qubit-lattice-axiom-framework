#!/usr/bin/env python3
"""Exact support-side A1 center-excess law plus bounded tensor consequence.

This runner advances the post-blindness gravity route on the microscopic
support block rather than the shell side.

Exact content:
  1. On the seven-site star support, the exact A1 support block at fixed total
     charge retains one scalar datum after charge normalization:
         delta_A1 = (phi_support(center) - phi_support(arm_mean)) / Q.
  2. For the canonical Q=1 projective A1 family
         q_A1(r) = (e0 + r s) / (1 + sqrt(6) r),
     that exact datum is
         delta_A1(r) = 1 / (6 (1 + sqrt(6) r)).
  3. That closed form holds for every r >= 0, not only at sampled r: the map
     q -> G_S q is linear and every family member carries total charge Q=1, so
     delta_A1 is the corresponding combination of its two endpoint values
     1/6 and 0. The runner checks the linearity directly and sweeps r densely.

Bounded content (conditional on the current chosen tensor observable):
  4. The tensor coefficients gamma_E, gamma_T are central finite differences,
     with step EPS = 0.005, of the eta floor returned by tensor_metrics in
     frontier_tensor_boundary_drive_two_channel.py, normalized by anchor_per_Q
     from frontier_one_parameter_reduced_shell_law.py. An affine law in
     delta_A1 is fitted from the two A1 endpoint backgrounds, not derived.
  5. That fitted law is evaluated at exactly eight backgrounds: the six
     canonical A1 samples r = 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, the exact local
     O_h A1 baseline, and the finite-rank A1 baseline. The reported ~1e-8 and
     few-e-6 error levels are observed maxima over those eight points only,
     and are not claimed at any other background or for any other observable.
"""

from __future__ import annotations


# Heavy compute / sweep runner — `AUDIT_TIMEOUT_SEC = 1800`
# means the audit-lane precompute and live audit runner allow up to
# 30 min of wall time before recording a timeout. The 120 s default
# ceiling is too tight under concurrency contention; see
# `docs/audit/RUNNER_CACHE_POLICY.md`.
AUDIT_TIMEOUT_SEC = 1800

from dataclasses import dataclass
from _frontier_loader import load_frontier

import numpy as np


EPS = 0.005
R_TEST = [0.25, 0.5, 0.75, 1.0, 1.5, 2.0]


same = load_frontier("same_source_metric", "frontier_same_source_metric_ansatz_scan.py")
finite_rank = load_frontier("finite_rank_metric", "frontier_finite_rank_gravity_residual.py")
two = load_frontier("tensor_two_channel", "frontier_tensor_boundary_drive_two_channel.py")
shell = load_frontier("one_parameter_shell", "frontier_one_parameter_reduced_shell_law.py")


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    status: str


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str, status: str = "EXACT") -> None:
    CHECKS.append(Check(name=name, ok=ok, detail=detail, status=status))
    tag = "PASS" if ok else "FAIL"
    print(f"[{status}] {tag}: {name}")
    if detail:
        print(f"    {detail}")


H0, INTERIOR = same.build_neg_laplacian_sparse(15)
CENTER = INTERIOR // 2
SUPPORT = [
    same.flat_idx(CENTER + v[0], CENTER + v[1], CENTER + v[2], INTERIOR)
    for v in same.SUPPORT_COORDS
]
G0P = same.solve_columns(H0, SUPPORT)
GS = G0P[SUPPORT, :]


def phi_from_q(q: np.ndarray) -> np.ndarray:
    phi = np.zeros((15, 15, 15), dtype=float)
    phi[1:-1, 1:-1, 1:-1] = (G0P @ q).reshape((INTERIOR, INTERIOR, INTERIOR))
    return phi


def support_potential(q: np.ndarray) -> np.ndarray:
    return GS @ q


def support_delta(q: np.ndarray) -> float:
    vals = support_potential(q)
    q_total = float(np.sum(q))
    return float(vals[0] / q_total - np.mean(vals[1:]) / q_total)


def eta_floor(q: np.ndarray) -> float:
    return float(two.tensor_metrics(phi_from_q(q))[0])


def gamma_pair(q: np.ndarray, ex: np.ndarray, t1x: np.ndarray) -> tuple[float, float]:
    beta_e = float((eta_floor(q + EPS * ex) - eta_floor(q - EPS * ex)) / (2.0 * EPS))
    beta_t = float((eta_floor(q + EPS * t1x) - eta_floor(q - EPS * t1x)) / (2.0 * EPS))
    red = shell.reduced_data(phi_from_q(q))
    a_aniso = float(red["anchor_per_Q"]) * float(np.sum(q))
    return beta_e / a_aniso, beta_t / a_aniso


def oh_qeff() -> np.ndarray:
    w = same.build_commutant_operator(0.0698, 0.0499, -0.0070, 0.0642, 0.1056)
    m = same.build_invariant_source(0.8247, 0.2271)
    return np.linalg.solve(np.eye(7) - w @ GS, m)


def finite_rank_qeff() -> np.ndarray:
    _, _, _, _, _, gs, w, masses = finite_rank.finite_rank_setup()
    return np.linalg.solve(np.eye(7) - w @ gs, masses)


def a1_baseline(q_eff: np.ndarray, basis: np.ndarray) -> np.ndarray:
    coeff = basis.T @ q_eff
    return basis[:, :2] @ coeff[:2]


def main() -> int:
    print("Support-side A1 center-excess law for the tensor frontier")
    print("=" * 78)

    basis = same.build_adapted_basis()
    e0 = basis[:, 0]
    s = basis[:, 1]
    s_unit = s / np.sqrt(6.0)
    e1 = basis[:, 2]
    e2 = basis[:, 3]
    t1x = basis[:, 4]
    ex = (np.sqrt(3.0) * e1 + e2) / 2.0

    vals_e0 = support_potential(e0)
    vals_s = support_potential(s_unit)
    arm_diff = float(np.max(np.abs(vals_e0[1:] - vals_s[1:])))
    center_excess_diff = float(abs((vals_e0[0] - vals_s[0]) - (1.0 / 6.0)))

    print("Unit-charge A1 endpoint support potentials:")
    print(f"  e0      = {np.array2string(vals_e0, precision=12, floatmode='fixed')}")
    print(f"  s/sqrt6 = {np.array2string(vals_s, precision=12, floatmode='fixed')}")
    print(f"  max arm-site difference = {arm_diff:.3e}")
    print(f"  center-excess residual from 1/6 = {center_excess_diff:.3e}")

    record(
        "the two unit-charge A1 basis backgrounds induce the same arm-site support potential",
        arm_diff < 1e-12,
        f"max arm-site difference = {arm_diff:.3e}",
    )
    record(
        "the exact surviving A1 support datum is the center-excess scalar, with endpoint size 1/6",
        center_excess_diff < 1e-12,
        f"center-excess residual from 1/6 = {center_excess_diff:.3e}",
    )

    max_delta_formula_err = 0.0
    for r in R_TEST:
        q = (e0 + r * s) / (1.0 + np.sqrt(6.0) * r)
        delta = support_delta(q)
        delta_formula = 1.0 / (6.0 * (1.0 + np.sqrt(6.0) * r))
        max_delta_formula_err = max(max_delta_formula_err, abs(delta - delta_formula))
        print(
            f"r={r:.2f}: delta_A1={delta:.12e}, "
            f"formula={delta_formula:.12e}, err={abs(delta-delta_formula):.3e}"
        )

    record(
        "on the canonical Q=1 projective A1 family, the exact support-side scalar is delta_A1(r)=1/(6(1+sqrt(6)r))",
        max_delta_formula_err < 1e-12,
        f"max formula error = {max_delta_formula_err:.3e}",
    )

    gamma_e0 = gamma_pair(e0, ex, t1x)
    gamma_s = gamma_pair(s_unit, ex, t1x)
    delta_e0 = support_delta(e0)
    delta_s = support_delta(s_unit)
    slope_e = (gamma_e0[0] - gamma_s[0]) / (delta_e0 - delta_s)
    intercept_e = gamma_s[0] - slope_e * delta_s
    slope_t = (gamma_e0[1] - gamma_s[1]) / (delta_e0 - delta_s)
    intercept_t = gamma_s[1] - slope_t * delta_s

    print("\nEndpoint tensor coefficients:")
    print(f"  gamma_E(center) = {gamma_e0[0]:+.12e}")
    print(f"  gamma_E(shell)  = {gamma_s[0]:+.12e}")
    print(f"  gamma_T(center) = {gamma_e0[1]:+.12e}")
    print(f"  gamma_T(shell)  = {gamma_s[1]:+.12e}")
    print("\nAffine support law from exact A1 endpoints:")
    print(f"  gamma_E(delta) = {intercept_e:+.12e} + ({slope_e:+.12e}) delta")
    print(f"  gamma_T(delta) = {intercept_t:+.12e} + ({slope_t:+.12e}) delta")

    max_canonical_err_e = 0.0
    max_canonical_err_t = 0.0
    for r in R_TEST:
        q = (e0 + r * s) / (1.0 + np.sqrt(6.0) * r)
        delta = support_delta(q)
        g_e, g_t = gamma_pair(q, ex, t1x)
        pred_e = intercept_e + slope_e * delta
        pred_t = intercept_t + slope_t * delta
        max_canonical_err_e = max(max_canonical_err_e, abs(pred_e - g_e))
        max_canonical_err_t = max(max_canonical_err_t, abs(pred_t - g_t))
        print(
            f"canonical r={r:.2f}: "
            f"gamma_E err={abs(pred_e-g_e):.3e}, gamma_T err={abs(pred_t-g_t):.3e}"
        )

    q_oh = a1_baseline(oh_qeff(), basis)
    q_fr = a1_baseline(finite_rank_qeff(), basis)
    max_family_err_e = 0.0
    max_family_err_t = 0.0
    for label, q in [("exact local O_h", q_oh), ("finite-rank", q_fr)]:
        delta = support_delta(q)
        g_e, g_t = gamma_pair(q, ex, t1x)
        pred_e = intercept_e + slope_e * delta
        pred_t = intercept_t + slope_t * delta
        err_e = abs(pred_e - g_e)
        err_t = abs(pred_t - g_t)
        max_family_err_e = max(max_family_err_e, err_e)
        max_family_err_t = max(max_family_err_t, err_t)
        print(
            f"{label}: delta_A1={delta:.12e}, "
            f"gamma_E err={err_e:.3e}, gamma_T err={err_t:.3e}"
        )

    record(
        "the current bright tensor coefficients are nearly affine in the exact support-side center-excess scalar on the canonical A1 family",
        max_canonical_err_e < 1e-8 and max_canonical_err_t < 2e-8,
        (
            f"max canonical affine-law errors: "
            f"gamma_E={max_canonical_err_e:.3e}, gamma_T={max_canonical_err_t:.3e}"
        ),
        status="BOUNDED",
    )
    record(
        "the same support-side affine law tracks the exact local O_h and finite-rank A1 baselines",
        max_family_err_e < 5e-6 and max_family_err_t < 5e-6,
        (
            f"max audited-family affine-law errors: "
            f"gamma_E={max_family_err_e:.3e}, gamma_T={max_family_err_t:.3e}"
        ),
        status="BOUNDED",
    )

    from pathlib import Path

    def excess_numerator(vec: np.ndarray) -> float:
        vals = support_potential(vec)
        return float(vals[0] - np.mean(vals[1:]))

    rng = np.random.default_rng(20260725)
    max_linearity_err = 0.0
    for _ in range(12):
        alpha, beta = rng.normal(size=2)
        q1 = rng.normal(size=7)
        q2 = rng.normal(size=7)
        lhs = excess_numerator(alpha * q1 + beta * q2)
        rhs = alpha * excess_numerator(q1) + beta * excess_numerator(q2)
        max_linearity_err = max(max_linearity_err, abs(lhs - rhs))

    record(
        "the unnormalized center-excess numerator n(q)=(G_S q)[0]-mean((G_S q)[1:]) is exactly linear in q",
        max_linearity_err < 1e-13,
        f"max |n(a q1 + b q2) - a n(q1) - b n(q2)| over 12 seeded draws = {max_linearity_err:.3e}",
    )

    r_sweep = np.concatenate((np.zeros(1), np.geomspace(1e-3, 1e3, 200)))
    max_sweep_formula_err = 0.0
    max_decomposition_err = 0.0
    max_wrong_law_err = 0.0
    for r in r_sweep:
        q = (e0 + r * s) / (1.0 + np.sqrt(6.0) * r)
        delta = support_delta(q)
        t = np.sqrt(6.0) * r / (1.0 + np.sqrt(6.0) * r)
        closed_form = 1.0 / (6.0 * (1.0 + np.sqrt(6.0) * r))
        from_endpoints = (1.0 - t) * delta_e0 + t * delta_s
        wrong_law = 1.0 / (5.0 * (1.0 + np.sqrt(6.0) * r))
        max_sweep_formula_err = max(max_sweep_formula_err, abs(delta - closed_form))
        max_decomposition_err = max(max_decomposition_err, abs(delta - from_endpoints))
        max_wrong_law_err = max(max_wrong_law_err, abs(delta - wrong_law))

    record(
        "delta_A1(r)=1/(6(1+sqrt(6)r)) holds on a dense continuous sweep, not only at the six canonical samples",
        max_sweep_formula_err < 1e-12,
        f"max error {max_sweep_formula_err:.3e} over {len(r_sweep)} r values in [0, 1e3]",
    )

    endpoint_center_err = abs(delta_e0 - 1.0 / 6.0)
    endpoint_shell_err = abs(delta_s - 0.0)
    record(
        "the endpoint values delta_A1(e0)=1/6 and delta_A1(s/sqrt(6))=0 reproduce the sweep through linearity",
        endpoint_center_err < 1e-13
        and endpoint_shell_err < 1e-13
        and max_decomposition_err < 1e-12,
        (
            f"|delta_A1(e0)-1/6|={endpoint_center_err:.3e}, "
            f"|delta_A1(s/sqrt(6))|={endpoint_shell_err:.3e}, "
            f"max endpoint-decomposition error over the sweep = {max_decomposition_err:.3e}"
        ),
    )

    record(
        "the perturbed law 1/(5(1+sqrt(6)r)) is rejected on the same sweep, so the gate discriminates",
        max_wrong_law_err > 1e-3,
        f"max error of the perturbed law = {max_wrong_law_err:.3e} (rejection threshold 1e-3)",
    )

    note_path = (
        Path(__file__).resolve().parents[1]
        / "docs"
        / "TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md"
    )
    note_text = note_path.read_text(encoding="utf-8")
    note_lower = note_text.lower()

    required_scope = (
        "r = 0.25, 0.5, 0.75, 1.0, 1.5, 2.0",
        "exact local O_h",
        "finite-rank",
        "tensor_metrics",
        "scripts/frontier_tensor_boundary_drive_two_channel.py",
        "anchor_per_Q",
        "scripts/frontier_one_parameter_reduced_shell_law.py",
        "EPS = 0.005",
        "## Downstream hygiene (2026-07-25)",
    )
    forbidden_scope = (
        "inverse-square",
        "inverse square",
        "almost exactly",
        "almost entirely controlled by",
        "cleanest axiom-first gravity reduction",
        "this closes another false level of generality",
        "only route",
        "last route",
        "exhausted",
    )
    missing_scope = [tok for tok in required_scope if tok not in note_text]
    present_forbidden = [tok for tok in forbidden_scope if tok in note_lower]

    record(
        "the paired note states the sampled scope, names the tensor observable and its step, and carries the dated hygiene block",
        not missing_scope and not present_forbidden,
        (
            f"missing scope tokens = {missing_scope}; "
            f"forbidden tokens present = {present_forbidden}"
        ),
    )

    sibling_pins = (
        "phi_support(center) - phi_support(arm_mean) = 1/6",
        "delta_A1(r) = 1 / (6 (1 + sqrt(6) r))",
        "delta_A1(q) =",
        "survives the shell-blindness theorem",
        "exact tensor endpoint coefficients",
        "center excess",
        "1/6",
    )
    missing_pins = [tok for tok in sibling_pins if tok not in note_text]
    record(
        "every note string that sibling runners read out of this note is still present",
        not missing_pins,
        f"{len(sibling_pins) - len(missing_pins)}/{len(sibling_pins)} pinned strings present; missing = {missing_pins}",
    )

    print("\nVerdict:")
    print(
        "The shell-blindness pivot can now be sharpened again. After fixing total "
        "charge, the exact A1 support block retains one microscopic scalar datum, "
        "the support center-excess delta_A1, and that datum obeys the closed form "
        "1/(6(1+sqrt(6)r)) on the whole canonical family, by linearity of q -> G_S q "
        "at fixed total charge. The tensor-side statement is narrower and stays "
        "conditional: for the current chosen tensor observable (the eta floor of "
        "tensor_metrics, normalized by anchor_per_Q, differenced with EPS=0.005), the "
        "bright coefficients are numerically compatible with an endpoint-fitted affine "
        "law in delta_A1 at the six canonical samples and the two named baselines "
        "actually tested, and nowhere else. So the remaining exact gravity theorem is "
        "the derivation of the exact tensor endpoint coefficients at the two A1 "
        "support endpoints and the exact tensor observable they belong to."
    )

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    n_pass = sum(c.ok for c in CHECKS)
    n_fail = sum(not c.ok for c in CHECKS)
    print(f"PASS={n_pass} FAIL={n_fail} TOTAL={len(CHECKS)}")
    if n_fail == 0:
        print("All checks passed.")
        return 0
    print("Some checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
