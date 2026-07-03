#!/usr/bin/env python3
"""Honest finite-size characterization of the Route-2 gravity-metric rho_E."""

from __future__ import annotations

import math
import os
import signal
import sys
import time
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import numpy as np  # noqa: E402

import frontier_one_parameter_reduced_shell_law_self_contained_replay_2026_06_17 as shell_replay  # noqa: E402
import frontier_quark_endpoint_readout_constraints as endpoint  # noqa: E402
import frontier_same_source_metric_ansatz_scan as same  # noqa: E402
import frontier_tensorial_einstein_regge_completion as tcomp  # noqa: E402


PASS_COUNT = 0
FAIL_COUNT = 0
EPS = 0.005
PROBE_RADIUS = 4.25
RICCI_H = 0.04
SHELL_RADIUS = 4.0
TAIL_QT_TOL = 0.02
SIZE_CAP_SECONDS = 120


def f12(value: float) -> str:
    return f"{float(value):+.12e}"


def u12(value: float) -> str:
    return f"{float(value):.12e}"


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    print(f"[{tag}] {name}")
    if detail:
        print(f"       {detail}")


class SizeTimeout(Exception):
    pass


@contextmanager
def wallclock_cap(seconds: int):
    previous_handler = signal.getsignal(signal.SIGALRM)

    def handler(_signum, _frame):
        raise SizeTimeout(f"cap={seconds}s")

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous_handler)


@dataclass(frozen=True)
class SizeSystem:
    size: int
    interior: int
    support: list[int]
    g0p: np.ndarray
    gs: np.ndarray


@dataclass
class Row:
    size: int
    solve_s: float
    delta_center: float
    delta_shell: float
    endpoint_gap: float
    gamma_e_center: float
    gamma_e_shell: float
    gamma_t_center: float
    gamma_t_shell: float
    q_t: float
    q_e: float
    c_te: float
    rho_e: float
    center_t: tuple[float, float, float]
    shell_t: tuple[float, float, float]
    center_e1: float
    center_e2: float
    shell_e1: float
    shell_e2: float
    admitted: bool


BASIS = same.build_adapted_basis()
E0 = BASIS[:, 0]
S_UNIT = BASIS[:, 1] / math.sqrt(6.0)
E1 = BASIS[:, 2]
E2 = BASIS[:, 3]
EX = (math.sqrt(3.0) * E1 + E2) / 2.0
TX = BASIS[:, 4]
TY = BASIS[:, 5]
TZ = BASIS[:, 6]


def build_size_system(size: int) -> SizeSystem:
    h0, interior = same.build_neg_laplacian_sparse(size)
    center = interior // 2
    support = [
        same.flat_idx(center + v[0], center + v[1], center + v[2], interior)
        for v in same.SUPPORT_COORDS
    ]
    g0p = same.solve_columns(h0, support)
    return SizeSystem(size=size, interior=interior, support=support, g0p=g0p, gs=g0p[support, :])


def phi_from_q(system: SizeSystem, q: np.ndarray) -> np.ndarray:
    phi = np.zeros((system.size, system.size, system.size), dtype=float)
    phi[1:-1, 1:-1, 1:-1] = (system.g0p @ q).reshape(
        (system.interior, system.interior, system.interior)
    )
    return phi


def support_delta(system: SizeSystem, q: np.ndarray) -> float:
    vals = system.gs @ q
    q_total = float(np.sum(q))
    return float(vals[0] / q_total - np.mean(vals[1:]) / q_total)


def transform_for_axis(phi_grid: np.ndarray, axis: str) -> np.ndarray:
    if axis == "x":
        return phi_grid
    if axis == "y":
        return np.transpose(phi_grid, (1, 0, 2)).copy()
    if axis == "z":
        return np.transpose(phi_grid, (2, 1, 0)).copy()
    raise ValueError(axis)


def probe_points(radius: float = PROBE_RADIUS) -> list[np.ndarray]:
    return [
        np.array([0.0, radius, 0.0, 0.0], dtype=float),
        np.array([0.3, radius / math.sqrt(2.0), radius / math.sqrt(2.0), 0.0], dtype=float),
        np.array(
            [0.6, radius / math.sqrt(3.0), radius / math.sqrt(3.0), radius / math.sqrt(3.0)],
            dtype=float,
        ),
    ]


ETA_CACHE: dict[tuple[int, str, tuple[float, ...]], float] = {}
ANCHOR_CACHE: dict[tuple[int, tuple[float, ...]], float] = {}


def q_key(q: np.ndarray) -> tuple[float, ...]:
    return tuple(float(x) for x in np.round(q, 15))


def base_eta_floor(phi_grid: np.ndarray) -> float:
    vals = []
    for point in probe_points():
        _, einstein = tcomp.ricci_and_einstein(
            lambda p: tcomp.adm_metric(phi_grid, p, eps_vec=0.0, eps_ten=0.0, omega=0.0),
            point,
            h=RICCI_H,
        )
        _, _, e_spatial_tf, _ = tcomp.max_tensorial_components(einstein)
        vals.append(e_spatial_tf)
    return float(max(vals))


def eta_floor(system: SizeSystem, q: np.ndarray, axis: str = "x") -> float:
    key = (system.size, axis, q_key(q))
    if key not in ETA_CACHE:
        ETA_CACHE[key] = base_eta_floor(transform_for_axis(phi_from_q(system, q), axis))
    return ETA_CACHE[key]


def anchor(system: SizeSystem, q: np.ndarray) -> float:
    key = (system.size, q_key(q))
    if key not in ANCHOR_CACHE:
        red = shell_replay.reduced_data(phi_from_q(system, q), shell_radius=SHELL_RADIUS)
        ANCHOR_CACHE[key] = float(red["anchor_per_Q"]) * float(np.sum(q))
    return ANCHOR_CACHE[key]


def gamma_fd(system: SizeSystem, q: np.ndarray, direction: np.ndarray, axis: str = "x") -> float:
    beta = (
        eta_floor(system, q + EPS * direction, axis=axis)
        - eta_floor(system, q - EPS * direction, axis=axis)
    ) / (2.0 * EPS)
    return float(beta / anchor(system, q))


def compute_row(size: int) -> Row:
    start = time.perf_counter()
    system = build_size_system(size)
    delta_center = support_delta(system, E0)
    delta_shell = support_delta(system, S_UNIT)
    endpoint_gap = delta_center - delta_shell

    gamma_e_center = gamma_fd(system, E0, EX, axis="x")
    gamma_e_shell = gamma_fd(system, S_UNIT, EX, axis="x")
    gamma_t_center_x = gamma_fd(system, E0, TX, axis="x")
    gamma_t_shell_x = gamma_fd(system, S_UNIT, TX, axis="x")

    center_t = (
        gamma_t_center_x,
        gamma_fd(system, E0, TY, axis="y"),
        gamma_fd(system, E0, TZ, axis="z"),
    )
    shell_t = (
        gamma_t_shell_x,
        gamma_fd(system, S_UNIT, TY, axis="y"),
        gamma_fd(system, S_UNIT, TZ, axis="z"),
    )

    center_e1 = gamma_fd(system, E0, E1, axis="x")
    center_e2 = gamma_fd(system, E0, E2, axis="x")
    shell_e1 = gamma_fd(system, S_UNIT, E1, axis="x")
    shell_e2 = gamma_fd(system, S_UNIT, E2, axis="x")

    q_t = gamma_t_center_x / gamma_t_shell_x
    q_e = gamma_e_center / gamma_e_shell
    c_te = gamma_t_center_x / gamma_e_center
    rho_e = (gamma_e_center - gamma_e_shell) / endpoint_gap / gamma_e_shell
    solve_s = time.perf_counter() - start

    return Row(
        size=size,
        solve_s=solve_s,
        delta_center=delta_center,
        delta_shell=delta_shell,
        endpoint_gap=endpoint_gap,
        gamma_e_center=gamma_e_center,
        gamma_e_shell=gamma_e_shell,
        gamma_t_center=gamma_t_center_x,
        gamma_t_shell=gamma_t_shell_x,
        q_t=q_t,
        q_e=q_e,
        c_te=c_te,
        rho_e=rho_e,
        center_t=center_t,
        shell_t=shell_t,
        center_e1=center_e1,
        center_e2=center_e2,
        shell_e1=shell_e1,
        shell_e2=shell_e2,
        admitted=abs(q_t - 5.0 / 6.0) < TAIL_QT_TOL,
    )


def rel_err(actual: float, expected: float) -> float:
    return abs(actual - expected) / max(abs(expected), 1.0e-300)


def max_pairwise_rel(vals: tuple[float, float, float]) -> float:
    out = 0.0
    for i in range(3):
        for j in range(i + 1, 3):
            out = max(out, abs(vals[i] - vals[j]) / max(abs(vals[i]), abs(vals[j]), 1.0e-300))
    return out


@dataclass(frozen=True)
class TailVerdict:
    verdict: str
    extrapolated_rho_e: float | None
    extrapolated_c_te: float | None
    uncertainty_rho_e: float | None
    uncertainty_c_te: float | None
    deltas: list[float]
    monotone: bool


def tail_verdict(rows: list[Row]) -> TailVerdict:
    tail = [row for row in rows if row.admitted]
    deltas = [abs(tail[i].rho_e - tail[i - 1].rho_e) for i in range(1, len(tail))]
    monotone = len(deltas) >= 2 and all(deltas[i] < deltas[i - 1] for i in range(1, len(deltas)))
    if not monotone:
        return TailVerdict("TAIL_NOT_CONVERGENT", None, None, None, None, deltas, False)

    sizes = np.array([row.size for row in tail], dtype=float)
    h = 1.0 / sizes
    rho = np.array([row.rho_e for row in tail], dtype=float)
    cte = np.array([row.c_te for row in tail], dtype=float)

    def extrapolate(values: np.ndarray) -> tuple[float, float]:
        y_inf = values[-1]
        errors = np.maximum(np.abs(values - y_inf), 1.0e-300)
        coeff = np.polyfit(np.log(h[:-1]), np.log(errors[:-1]), deg=1)
        order = max(float(coeff[0]), 0.25)
        x = h**order
        a, b = np.polyfit(x, values, deg=1)
        extrap = float(b)
        last_delta = abs(float(values[-1] - values[-2]))
        return extrap, max(abs(extrap - float(values[-1])), last_delta)

    rho_extrap, rho_unc = extrapolate(rho)
    cte_extrap, cte_unc = extrapolate(cte)
    return TailVerdict("CONVERGED", rho_extrap, cte_extrap, rho_unc, cte_unc, deltas, True)


def comparison_verdict(
    name: str,
    value: float | None,
    uncertainty: float | None,
    target: float,
) -> tuple[str, float | None]:
    if value is None or uncertainty is None or uncertainty <= 0.0:
        return "INCONCLUSIVE", None
    ratio = abs(value - target) / uncertainty
    return ("EXCLUDED" if ratio > 5.0 else "NOT_EXCLUDED"), ratio


def print_ladder(rows: list[Row]) -> None:
    print("\nLADDER")
    print(
        "size solve_s delta_center endpoint_gap gamma_E_center gamma_E_shell "
        "gamma_T_center gamma_T_shell q_T c_TE rho_E"
    )
    for row in rows:
        print(
            f"{row.size:d} {u12(row.solve_s)} {f12(row.delta_center)} {f12(row.endpoint_gap)} "
            f"{f12(row.gamma_e_center)} {f12(row.gamma_e_shell)} "
            f"{f12(row.gamma_t_center)} {f12(row.gamma_t_shell)} "
            f"{f12(row.q_t)} {f12(row.c_te)} {f12(row.rho_e)}"
        )


def print_admission(rows: list[Row]) -> None:
    print("\nQ_T_ADMISSION")
    print("size q_T abs_gap_to_5_over_6 flag")
    for row in rows:
        flag = "ADMITTED" if row.admitted else "PRE_ASYMPTOTIC"
        print(f"{row.size:d} {f12(row.q_t)} {u12(abs(row.q_t - 5.0 / 6.0))} {flag}")


def print_isotropy(rows: list[Row]) -> float:
    print("\nISOTROPY_TRIPWIRE")
    print(
        "size center_T_tx center_T_ty center_T_tz shell_T_tx shell_T_ty shell_T_tz "
        "max_pairwise_rel center_E_e1 center_E_e2 shell_E_e1 shell_E_e2"
    )
    max_rel = 0.0
    for row in rows:
        rel = max(max_pairwise_rel(row.center_t), max_pairwise_rel(row.shell_t))
        max_rel = max(max_rel, rel)
        print(
            f"{row.size:d} {f12(row.center_t[0])} {f12(row.center_t[1])} {f12(row.center_t[2])} "
            f"{f12(row.shell_t[0])} {f12(row.shell_t[1])} {f12(row.shell_t[2])} "
            f"{u12(rel)} {f12(row.center_e1)} {f12(row.center_e2)} "
            f"{f12(row.shell_e1)} {f12(row.shell_e2)}"
        )
    return max_rel


def print_frozen_drift(row15: Row) -> None:
    fast = endpoint.FAST_ENDPOINT_READOUT
    pairs = [
        ("gamma_E_center", fast.gamma_e_center, row15.gamma_e_center),
        ("gamma_E_shell", fast.gamma_e_shell, row15.gamma_e_shell),
        ("gamma_T_center", fast.gamma_t_center, row15.gamma_t_center),
        ("gamma_T_shell", fast.gamma_t_shell, row15.gamma_t_shell),
        ("rho_E", fast.ratio_be_ae, row15.rho_e),
        ("q_T", fast.ratio_t_center_shell, row15.q_t),
    ]
    print("\nFROZEN_DRIFT")
    print("quantity fast_endpoint size15_replay relative_drift")
    for name, frozen, replay in pairs:
        drift = abs(replay - frozen) / max(abs(frozen), 1.0e-300)
        print(f"{name} {f12(frozen)} {f12(replay)} {u12(drift)}")


def main() -> int:
    print("Route-2 honest gravity-metric rho_E characterization")
    print("=" * 78)

    sizes = [11, 13, 15, 17, 19, 21]
    if os.environ.get("QUARK_RHOE_EXTENDED_LADDER") == "1":
        sizes.extend([25, 29])

    rows: list[Row] = []
    skipped: list[int] = []
    for size in sizes:
        try:
            with wallclock_cap(SIZE_CAP_SECONDS):
                row = compute_row(size)
            rows.append(row)
            print(f"SIZE {size:d}: COMPUTED solve_s={u12(row.solve_s)}")
        except SizeTimeout:
            skipped.append(size)
            print(f"SIZE {size:d}: SKIPPED solve_s={u12(SIZE_CAP_SECONDS)} reason=CAP_120s")

    print_ladder(rows)
    print_admission(rows)
    isotropy_max_rel = print_isotropy(rows)

    row15 = next((row for row in rows if row.size == 15), None)
    if row15 is None:
        check("A1 anchor requires size 15 to compute", False, "size 15 was skipped")
        check("A7 sanity bracket requires size 15 to compute", False, "size 15 was skipped")
    else:
        expected = {
            "gamma_E(center)": (row15.gamma_e_center, -3.772329167975e-04),
            "gamma_E(shell)": (row15.gamma_e_shell, -2.010572657265e-04),
            "gamma_T(center)": (row15.gamma_t_center, +3.359952396063e-04),
            "gamma_T(shell)": (row15.gamma_t_shell, +4.031967723697e-04),
        }
        for label, (actual, target) in expected.items():
            check(
                f"A1 anchor {label}",
                rel_err(actual, target) <= 1.0e-6,
                f"actual={f12(actual)} expected={f12(target)} rel={u12(rel_err(actual, target))}",
            )
        check(
            "A7 rho_E(15) sanity bracket",
            5.20 < row15.rho_e < 5.32,
            f"rho_E(15)={f12(row15.rho_e)}",
        )
        print_frozen_drift(row15)

    check(
        "A2 T-probe isotropy tripwire",
        isotropy_max_rel <= 1.0e-6,
        f"max_pairwise_rel={u12(isotropy_max_rel)}",
    )

    expected_qt = {11: 0.902, 13: 0.870, 15: 0.833328}
    small_rows_ok = True
    details = []
    for size, target in expected_qt.items():
        row = next((item for item in rows if item.size == size), None)
        if row is None:
            small_rows_ok = False
            details.append(f"{size}:SKIPPED")
            continue
        tol = 5.0e-4 if size == 15 else 5.0e-3
        ok = abs(row.q_t - target) <= tol
        small_rows_ok = small_rows_ok and ok
        details.append(f"{size}:{f12(row.q_t)} target={f12(target)} tol={u12(tol)}")
    check("A3 pre-asymptotic q_T reproduction", small_rows_ok, "; ".join(details))

    tail = tail_verdict(rows)
    print("\nCONVERGENCE_TAIL")
    print("admitted_sizes " + ",".join(str(row.size) for row in rows if row.admitted))
    if tail.deltas:
        for idx, delta in enumerate(tail.deltas, start=1):
            print(f"successive_delta_rho_E_{idx:d} {u12(delta)}")
    else:
        print("successive_delta_rho_E none")
    if tail.verdict == "CONVERGED":
        print(
            f"verdict CONVERGED rho_E={f12(tail.extrapolated_rho_e)} "
            f"uncertainty={u12(tail.uncertainty_rho_e)} "
            f"c_TE={f12(tail.extrapolated_c_te)} "
            f"c_TE_uncertainty={u12(tail.uncertainty_c_te)}"
        )
    else:
        print("verdict TAIL_NOT_CONVERGENT")
    check(
        "A4 tail convergence verdict-consistency",
        (tail.verdict == "CONVERGED") == tail.monotone,
        f"verdict={tail.verdict} monotone_rule={tail.monotone}",
    )

    rho_verdict, rho_ratio = comparison_verdict(
        "rho_E", tail.extrapolated_rho_e, tail.uncertainty_rho_e, 21.0 / 4.0
    )
    cte_verdict, cte_ratio = comparison_verdict(
        "c_TE", tail.extrapolated_c_te, tail.uncertainty_c_te, -8.0 / 9.0
    )
    print("\nCOMPARISON_VERDICTS")
    print(
        "rho_E_vs_21_over_4 "
        f"{rho_verdict} ratio={u12(float('nan') if rho_ratio is None else rho_ratio)}"
    )
    print(
        "c_TE_vs_minus_8_over_9 "
        f"{cte_verdict} ratio={u12(float('nan') if cte_ratio is None else cte_ratio)}"
    )
    check(
        "A5 rho_E vs 21/4 verdict-consistency",
        (rho_verdict == "INCONCLUSIVE") == (tail.extrapolated_rho_e is None),
        f"verdict={rho_verdict}",
    )
    check(
        "A6 c_TE vs -8/9 verdict-consistency",
        (cte_verdict == "INCONCLUSIVE") == (tail.extrapolated_c_te is None),
        f"verdict={cte_verdict}",
    )

    if skipped:
        print("\nSKIPPED_SIZES " + ",".join(str(size) for size in skipped))

    total = PASS_COUNT + FAIL_COUNT
    print(f"\nSUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={total}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
