#!/usr/bin/env python3
"""Active-branch derivative of the Route-2 eta-floor max-abs endpoint form."""

from __future__ import annotations

# This runner differentiates the nested tensor stencil at the four endpoint
# source-direction probes. The live chain is slow because it also builds the
# tensor-kernel side channels; allow audit/cache runs enough headroom.
AUDIT_TIMEOUT_SEC = 900

from dataclasses import dataclass
import math

import mpmath as mp
import numpy as np
from scipy.ndimage import map_coordinates

import frontier_one_parameter_reduced_shell_law_self_contained_replay_2026_06_17 as shell
import frontier_same_source_metric_ansatz_scan as same
import frontier_tensor_support_center_excess_law as center


EPS_MODULE = 0.005
FD_STEPS = (1.0e-3, 5.0e-4)
T_BALANCE_FD_STABLE_BAND = (1.0000260, 1.0000319)

POINTS = (
    np.array([0.0, 4.25, 0.0, 0.0], dtype=float),
    np.array([0.3, 4.25 / math.sqrt(2.0), 4.25 / math.sqrt(2.0), 0.0], dtype=float),
    np.array([0.6, 4.25 / math.sqrt(3.0), 4.25 / math.sqrt(3.0), 4.25 / math.sqrt(3.0)], dtype=float),
)
AXES = ("x", "y", "z")

PASS_COUNT = 0
FAIL_COUNT = 0


@dataclass(frozen=True)
class EntryRow:
    abs_value: float
    value: float
    derivative: float
    point_idx: int
    row: int
    col: int

    @property
    def entry_id(self) -> tuple[int, int, int]:
        return (self.point_idx, self.row, self.col)


@dataclass(frozen=True)
class ProbeResult:
    q_label: str
    direction_label: str
    beta: float
    gamma: float
    anchor: float
    top_rows: list[EntryRow]
    minus_top: EntryRow
    plus_top: EntryRow
    fd_rows: list[tuple[float, float, float, float, bool]]


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    if detail:
        print(f"{tag}: {name} -- {detail}")
    else:
        print(f"{tag}: {name}")


def phi_from_q(q: np.ndarray) -> np.ndarray:
    return center.phi_from_q(q)


def dphi_from_v(v: np.ndarray) -> np.ndarray:
    dphi = np.zeros((15, 15, 15), dtype=float)
    dphi[1:-1, 1:-1, 1:-1] = (center.G0P @ v).reshape(
        (center.INTERIOR, center.INTERIOR, center.INTERIOR)
    )
    return dphi


def interpolate_grid(grid: np.ndarray, xyz: np.ndarray) -> float:
    center_coord = (grid.shape[0] - 1) / 2.0
    coords = np.array(
        [[center_coord + xyz[0]], [center_coord + xyz[1]], [center_coord + xyz[2]]],
        dtype=float,
    )
    return float(map_coordinates(grid, coords, order=3, mode="nearest")[0])


def adm_metric_value(phi_grid: np.ndarray, point: np.ndarray) -> np.ndarray:
    phi = interpolate_grid(phi_grid, np.asarray(point[1:], dtype=float))
    psi = 1.0 + phi
    alpha = (1.0 - phi) / (1.0 + phi)

    g = np.zeros((4, 4), dtype=float)
    g[0, 0] = -alpha * alpha
    g[1, 1] = psi**4
    g[2, 2] = psi**4
    g[3, 3] = psi**4
    return g


def adm_metric_pair(phi_grid: np.ndarray, dphi_grid: np.ndarray, point: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    xyz = np.asarray(point[1:], dtype=float)
    phi = interpolate_grid(phi_grid, xyz)
    dphi = interpolate_grid(dphi_grid, xyz)
    psi = 1.0 + phi
    alpha = (1.0 - phi) / (1.0 + phi)
    dalpha = -2.0 * dphi / ((1.0 + phi) ** 2)
    dgamma_diag = 4.0 * psi**3 * dphi

    g = np.zeros((4, 4), dtype=float)
    dg = np.zeros((4, 4), dtype=float)
    g[0, 0] = -alpha * alpha
    dg[0, 0] = -2.0 * alpha * dalpha
    for idx in (1, 2, 3):
        g[idx, idx] = psi**4
        dg[idx, idx] = dgamma_diag
    return g, dg


def christoffel_value(phi_grid: np.ndarray, point: np.ndarray, h: float = 0.04) -> np.ndarray:
    g = adm_metric_value(phi_grid, point)
    g_inv = np.linalg.inv(g)
    dg_coord = np.zeros((4, 4, 4), dtype=float)
    for axis in range(4):
        p_plus = point.copy()
        p_minus = point.copy()
        p_plus[axis] += h
        p_minus[axis] -= h
        dg_coord[axis] = (
            adm_metric_value(phi_grid, p_plus) - adm_metric_value(phi_grid, p_minus)
        ) / (2.0 * h)

    gamma = np.zeros((4, 4, 4), dtype=float)
    for lam in range(4):
        for mu in range(4):
            for nu in range(4):
                total = 0.0
                for rho in range(4):
                    total += g_inv[lam, rho] * (
                        dg_coord[mu, rho, nu]
                        + dg_coord[nu, rho, mu]
                        - dg_coord[rho, mu, nu]
                    )
                gamma[lam, mu, nu] = 0.5 * total
    return gamma


def christoffel_pair(
    phi_grid: np.ndarray,
    dphi_grid: np.ndarray,
    point: np.ndarray,
    h: float = 0.04,
) -> tuple[np.ndarray, np.ndarray]:
    g, dg = adm_metric_pair(phi_grid, dphi_grid, point)
    g_inv = np.linalg.inv(g)
    dg_inv = -g_inv @ dg @ g_inv

    dg_coord = np.zeros((4, 4, 4), dtype=float)
    ddg_coord = np.zeros((4, 4, 4), dtype=float)
    for axis in range(4):
        p_plus = point.copy()
        p_minus = point.copy()
        p_plus[axis] += h
        p_minus[axis] -= h
        g_plus, dg_plus = adm_metric_pair(phi_grid, dphi_grid, p_plus)
        g_minus, dg_minus = adm_metric_pair(phi_grid, dphi_grid, p_minus)
        dg_coord[axis] = (g_plus - g_minus) / (2.0 * h)
        ddg_coord[axis] = (dg_plus - dg_minus) / (2.0 * h)

    gamma = np.zeros((4, 4, 4), dtype=float)
    dgamma = np.zeros((4, 4, 4), dtype=float)
    for lam in range(4):
        for mu in range(4):
            for nu in range(4):
                total = 0.0
                dtotal = 0.0
                for rho in range(4):
                    comb = (
                        dg_coord[mu, rho, nu]
                        + dg_coord[nu, rho, mu]
                        - dg_coord[rho, mu, nu]
                    )
                    dcomb = (
                        ddg_coord[mu, rho, nu]
                        + ddg_coord[nu, rho, mu]
                        - ddg_coord[rho, mu, nu]
                    )
                    total += g_inv[lam, rho] * comb
                    dtotal += dg_inv[lam, rho] * comb + g_inv[lam, rho] * dcomb
                gamma[lam, mu, nu] = 0.5 * total
                dgamma[lam, mu, nu] = 0.5 * dtotal
    return gamma, dgamma


def ricci_einstein_value(phi_grid: np.ndarray, point: np.ndarray, h: float = 0.04) -> np.ndarray:
    g = adm_metric_value(phi_grid, point)
    g_inv = np.linalg.inv(g)
    gamma = christoffel_value(phi_grid, point, h)

    dgamma_coord = np.zeros((4, 4, 4, 4), dtype=float)
    for axis in range(4):
        p_plus = point.copy()
        p_minus = point.copy()
        p_plus[axis] += h
        p_minus[axis] -= h
        dgamma_coord[axis] = (
            christoffel_value(phi_grid, p_plus, h) - christoffel_value(phi_grid, p_minus, h)
        ) / (2.0 * h)

    ricci = np.zeros((4, 4), dtype=float)
    for mu in range(4):
        for nu in range(4):
            term1 = term2 = term3 = term4 = 0.0
            for lam in range(4):
                term1 += dgamma_coord[lam, lam, mu, nu]
                term2 += dgamma_coord[nu, lam, mu, lam]
                trace_lam = sum(gamma[rho, lam, rho] for rho in range(4))
                term3 += gamma[lam, mu, nu] * trace_lam
                for rho in range(4):
                    term4 += gamma[rho, mu, lam] * gamma[lam, nu, rho]
            ricci[mu, nu] = term1 - term2 + term3 - term4

    scalar = float(np.sum(g_inv * ricci))
    return ricci - 0.5 * g * scalar


def ricci_einstein_pair(
    phi_grid: np.ndarray,
    dphi_grid: np.ndarray,
    point: np.ndarray,
    h: float = 0.04,
) -> tuple[np.ndarray, np.ndarray]:
    g, dg = adm_metric_pair(phi_grid, dphi_grid, point)
    g_inv = np.linalg.inv(g)
    dg_inv = -g_inv @ dg @ g_inv
    gamma, dgamma = christoffel_pair(phi_grid, dphi_grid, point, h)

    dgamma_coord = np.zeros((4, 4, 4, 4), dtype=float)
    ddgamma_coord = np.zeros((4, 4, 4, 4), dtype=float)
    for axis in range(4):
        p_plus = point.copy()
        p_minus = point.copy()
        p_plus[axis] += h
        p_minus[axis] -= h
        gamma_plus, dgamma_plus = christoffel_pair(phi_grid, dphi_grid, p_plus, h)
        gamma_minus, dgamma_minus = christoffel_pair(phi_grid, dphi_grid, p_minus, h)
        dgamma_coord[axis] = (gamma_plus - gamma_minus) / (2.0 * h)
        ddgamma_coord[axis] = (dgamma_plus - dgamma_minus) / (2.0 * h)

    ricci = np.zeros((4, 4), dtype=float)
    dricci = np.zeros((4, 4), dtype=float)
    for mu in range(4):
        for nu in range(4):
            term1 = term2 = term3 = term4 = 0.0
            dterm1 = dterm2 = dterm3 = dterm4 = 0.0
            for lam in range(4):
                term1 += dgamma_coord[lam, lam, mu, nu]
                dterm1 += ddgamma_coord[lam, lam, mu, nu]
                term2 += dgamma_coord[nu, lam, mu, lam]
                dterm2 += ddgamma_coord[nu, lam, mu, lam]
                trace_lam = sum(gamma[rho, lam, rho] for rho in range(4))
                dtrace_lam = sum(dgamma[rho, lam, rho] for rho in range(4))
                term3 += gamma[lam, mu, nu] * trace_lam
                dterm3 += dgamma[lam, mu, nu] * trace_lam + gamma[lam, mu, nu] * dtrace_lam
                for rho in range(4):
                    term4 += gamma[rho, mu, lam] * gamma[lam, nu, rho]
                    dterm4 += (
                        dgamma[rho, mu, lam] * gamma[lam, nu, rho]
                        + gamma[rho, mu, lam] * dgamma[lam, nu, rho]
                    )
            ricci[mu, nu] = term1 - term2 + term3 - term4
            dricci[mu, nu] = dterm1 - dterm2 + dterm3 - dterm4

    scalar = float(np.sum(g_inv * ricci))
    dscalar = float(np.sum(dg_inv * ricci + g_inv * dricci))
    einstein = ricci - 0.5 * g * scalar
    deinstein = dricci - 0.5 * (dg * scalar + g * dscalar)
    return einstein, deinstein


def spatial_tf(einstein: np.ndarray) -> np.ndarray:
    spatial = einstein[1:, 1:]
    return spatial - np.eye(3) * float(np.trace(spatial)) / 3.0


def tf_rows_value(phi_grid: np.ndarray) -> list[EntryRow]:
    rows: list[EntryRow] = []
    for point_idx, point in enumerate(POINTS):
        tf = spatial_tf(ricci_einstein_value(phi_grid, point))
        for row in range(3):
            for col in range(3):
                value = float(tf[row, col])
                rows.append(
                    EntryRow(
                        abs_value=abs(value),
                        value=value,
                        derivative=float("nan"),
                        point_idx=point_idx,
                        row=row,
                        col=col,
                    )
                )
    rows.sort(key=lambda item: (-item.abs_value, item.point_idx, item.row, item.col))
    return rows


def tf_rows_pair(phi_grid: np.ndarray, dphi_grid: np.ndarray) -> list[EntryRow]:
    rows: list[EntryRow] = []
    for point_idx, point in enumerate(POINTS):
        einstein, deinstein = ricci_einstein_pair(phi_grid, dphi_grid, point)
        tf = spatial_tf(einstein)
        dtf = spatial_tf(deinstein)
        for row in range(3):
            for col in range(3):
                value = float(tf[row, col])
                rows.append(
                    EntryRow(
                        abs_value=abs(value),
                        value=value,
                        derivative=float(dtf[row, col]),
                        point_idx=point_idx,
                        row=row,
                        col=col,
                    )
                )
    rows.sort(key=lambda item: (-item.abs_value, item.point_idx, item.row, item.col))
    return rows


def eta_value(q: np.ndarray) -> float:
    return tf_rows_value(phi_from_q(q))[0].abs_value


def entry_label(row: EntryRow) -> str:
    return f"probe{row.point_idx}:{AXES[row.row]}{AXES[row.col]}"


def margin_to_next(rows: list[EntryRow], idx: int = 0) -> tuple[float, float]:
    margin = rows[idx].abs_value - rows[idx + 1].abs_value
    rel = margin / max(rows[idx].abs_value, 1.0e-300)
    return margin, rel


def anchor_for_q(q: np.ndarray) -> float:
    red = shell.reduced_data(phi_from_q(q))
    return float(red["anchor_per_Q"]) * float(np.sum(q))


def probe_result(q_label: str, q: np.ndarray, direction_label: str, direction: np.ndarray) -> ProbeResult:
    phi = phi_from_q(q)
    rows = tf_rows_pair(phi, dphi_from_v(direction))
    active = rows[0]
    beta = math.copysign(1.0, active.value) * active.derivative
    anchor = anchor_for_q(q)

    minus_top = tf_rows_value(phi_from_q(q - EPS_MODULE * direction))[0]
    plus_top = tf_rows_value(phi_from_q(q + EPS_MODULE * direction))[0]

    f0 = rows[0].abs_value
    fd_rows = []
    for eps in FD_STEPS:
        f_plus = eta_value(q + eps * direction)
        f_minus = eta_value(q - eps * direction)
        backward = (f0 - f_minus) / eps
        forward = (f_plus - f0) / eps
        central = 0.5 * (backward + forward)
        bracket = min(backward, forward) - 1.0e-14 <= beta <= max(backward, forward) + 1.0e-14
        fd_rows.append((eps, backward, forward, central, bracket))

    return ProbeResult(
        q_label=q_label,
        direction_label=direction_label,
        beta=beta,
        gamma=beta / anchor,
        anchor=anchor,
        top_rows=rows,
        minus_top=minus_top,
        plus_top=plus_top,
        fd_rows=fd_rows,
    )


def print_top5(result: ProbeResult) -> None:
    print(f"\nTop-5 max-abs entries for q={result.q_label}, direction={result.direction_label}")
    for idx, row in enumerate(result.top_rows[:5]):
        margin, rel = margin_to_next(result.top_rows, idx)
        print(
            f"  {idx + 1}. {entry_label(row):9s} "
            f"value={row.value:+.12e} abs={row.abs_value:.12e} "
            f"dE/dt={row.derivative:+.12e} "
            f"margin_next={margin:.12e} rel_margin_next={rel:.12e}"
        )


def assemble_mp(
    gamma_e_center: float,
    gamma_e_shell: float,
    gamma_t_center: float,
    gamma_t_shell: float,
    delta_center: float,
    delta_shell: float,
) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    mp.mp.dps = 30
    gec = mp.mpf(repr(gamma_e_center))
    ges = mp.mpf(repr(gamma_e_shell))
    gtc = mp.mpf(repr(gamma_t_center))
    gts = mp.mpf(repr(gamma_t_shell))
    dc = mp.mpf(repr(delta_center))
    ds = mp.mpf(repr(delta_shell))
    gap = dc - ds
    slope_e = (gec - ges) / gap
    intercept_e = ges - slope_e * ds
    slope_t = (gtc - gts) / gap
    intercept_t = gts - slope_t * ds
    return abs(slope_e / slope_t), abs(intercept_t / intercept_e), abs(slope_t / intercept_t)


def main() -> int:
    print("Route-2 endpoint active-branch eta-floor derivative")
    print("=" * 78)

    basis = same.build_adapted_basis()
    e0 = basis[:, 0]
    s_unit = basis[:, 1] / math.sqrt(6.0)
    e1 = basis[:, 2]
    e2 = basis[:, 3]
    t1x = basis[:, 4]
    ex = (math.sqrt(3.0) * e1 + e2) / 2.0

    probes = [
        probe_result("center/e0", e0, "E_x", ex),
        probe_result("center/e0", e0, "T1x", t1x),
        probe_result("shell/s_sqrt6", s_unit, "E_x", ex),
        probe_result("shell/s_sqrt6", s_unit, "T1x", t1x),
    ]

    for result in probes:
        print_top5(result)

    print("\nArgmax stability at module EPS=0.005")
    for result in probes:
        base = result.top_rows[0]
        margin, rel = margin_to_next(result.top_rows, 0)
        print(
            f"  q={result.q_label:13s} dir={result.direction_label:3s} "
            f"base={entry_label(base)} minus={entry_label(result.minus_top)} plus={entry_label(result.plus_top)} "
            f"base_rel_margin={rel:.12e} base_abs_gap={margin:.12e}"
        )

    print("\nActive-branch source-direction slopes")
    for result in probes:
        print(
            f"  q={result.q_label:13s} dir={result.direction_label:3s} "
            f"beta={result.beta:+.12e} anchor={result.anchor:.12e} gamma={result.gamma:+.12e}"
        )

    print("\nFinite-difference cross-checks")
    max_central_diff = 0.0
    all_bracketed = True
    for result in probes:
        for eps, backward, forward, central, bracket in result.fd_rows:
            max_central_diff = max(max_central_diff, abs(central - result.beta))
            all_bracketed = all_bracketed and bracket
            print(
                f"  q={result.q_label:13s} dir={result.direction_label:3s} eps={eps:.1e} "
                f"back={backward:+.12e} fwd={forward:+.12e} "
                f"central={central:+.12e} beta={result.beta:+.12e} bracket={bracket}"
            )

    by_key = {(r.q_label, r.direction_label): r for r in probes}
    gamma_e_center = by_key[("center/e0", "E_x")].gamma
    gamma_t_center = by_key[("center/e0", "T1x")].gamma
    gamma_e_shell = by_key[("shell/s_sqrt6", "E_x")].gamma
    gamma_t_shell = by_key[("shell/s_sqrt6", "T1x")].gamma

    delta_center = center.support_delta(e0)
    delta_shell = center.support_delta(s_unit)
    endpoint_gap = delta_center - delta_shell
    slope_e = (gamma_e_center - gamma_e_shell) / endpoint_gap
    intercept_e = gamma_e_shell - slope_e * delta_shell
    slope_t = (gamma_t_center - gamma_t_shell) / endpoint_gap
    intercept_t = gamma_t_shell - slope_t * delta_shell
    slope_ratio = abs(slope_e / slope_t)
    shell_ratio = abs(intercept_t / intercept_e)
    t_balance = abs(slope_t / intercept_t)

    mp_slope_ratio, mp_shell_ratio, mp_t_balance = assemble_mp(
        gamma_e_center,
        gamma_e_shell,
        gamma_t_center,
        gamma_t_shell,
        delta_center,
        delta_shell,
    )
    mp_drift = max(
        abs(float(mp_slope_ratio) - slope_ratio),
        abs(float(mp_shell_ratio) - shell_ratio),
        abs(float(mp_t_balance) - t_balance),
    )

    print("\nEndpoint affine assembly from active-branch derivatives")
    print(f"  delta_center={delta_center:.12e}")
    print(f"  delta_shell ={delta_shell:.12e}")
    print(f"  endpoint_gap={endpoint_gap:.12e}")
    print(f"  gamma_E(delta) = {intercept_e:+.12e} + ({slope_e:+.12e}) delta_A1")
    print(f"  gamma_T(delta) = {intercept_t:+.12e} + ({slope_t:+.12e}) delta_A1")
    print(f"  |b_E/b_T| = {slope_ratio:.12f}")
    print(f"  |a_T/a_E| = {shell_ratio:.12f}")
    print(f"  |b_T/a_T| = {t_balance:.12f}")
    print(f"  mpmath30 final-assembly drift <= {mp_drift:.3e}")

    center_rows = by_key[("center/e0", "E_x")].top_rows
    shell_rows = by_key[("shell/s_sqrt6", "E_x")].top_rows
    center_margin, center_rel = margin_to_next(center_rows)
    shell_margin, shell_rel = margin_to_next(shell_rows)

    check(
        "center endpoint active max is unique",
        center_margin > 0.0 and center_rel > 1.0e-2,
        f"active={entry_label(center_rows[0])}, abs_gap={center_margin:.3e}, rel_gap={center_rel:.3e}",
    )
    check(
        "shell endpoint active max is unique",
        shell_margin > 0.0 and shell_rel > 1.0e-2,
        f"active={entry_label(shell_rows[0])}, abs_gap={shell_margin:.3e}, rel_gap={shell_rel:.3e}",
    )
    for result in probes:
        stable = (
            result.minus_top.entry_id == result.top_rows[0].entry_id
            and result.plus_top.entry_id == result.top_rows[0].entry_id
        )
        check(
            f"module-step argmax stability for q={result.q_label}, dir={result.direction_label}",
            stable,
            f"minus={entry_label(result.minus_top)}, base={entry_label(result.top_rows[0])}, plus={entry_label(result.plus_top)}",
        )
    check(
        "one-sided FD slopes at eps=1e-3 and 5e-4 bracket each active-branch derivative",
        all_bracketed,
        "all four endpoint-direction probes bracketed at both requested steps",
    )
    check(
        "central FD cross-checks stay within the observed tensor-stencil roundoff envelope",
        max_central_diff < 5.0e-11,
        f"max |central_fd-beta| = {max_central_diff:.3e}",
    )
    check(
        "endpoint support gap is the admitted 1/6 support scalar",
        abs(endpoint_gap - 1.0 / 6.0) < 1.0e-12,
        f"endpoint_gap = {endpoint_gap:.12e}",
    )
    check(
        "active-branch t_balance lies in the finite-difference stable band",
        T_BALANCE_FD_STABLE_BAND[0] <= t_balance <= T_BALANCE_FD_STABLE_BAND[1],
        (
            f"t_balance={t_balance:.12f}, "
            f"band=[{T_BALANCE_FD_STABLE_BAND[0]:.7f}, {T_BALANCE_FD_STABLE_BAND[1]:.7f}]"
        ),
    )
    check(
        "30-digit mpmath final assembly agrees with double final assembly",
        mp_drift < 1.0e-12,
        f"max ratio drift = {mp_drift:.3e}",
    )

    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
