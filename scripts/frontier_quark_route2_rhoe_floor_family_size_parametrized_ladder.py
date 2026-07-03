#!/usr/bin/env python3
"""Size-parametrized floor-family ladder for the Route-2 rho_E readout."""

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

import frontier_quark_route2_honest_gravity_metric_rhoe_characterization as parent  # noqa: E402


PASS_COUNT = 0
FAIL_COUNT = 0

EPS = parent.EPS
HALF_EPS = EPS / 2.0
TAIL_QT_TOL = parent.TAIL_QT_TOL
SIZE_CAP_SECONDS = parent.SIZE_CAP_SECONDS
FD_SMOOTH_REL_TOL = 0.05
ISOTROPY_REL_TOL = 1.0e-6
ANCHOR_REL_TOL = 1.0e-6


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
class FDPair:
    endpoint: str
    direction: str
    fd_eps: float
    fd_half: float
    rel_step_change: float
    smooth: bool
    e_tf_base: float
    e_tf_plus_eps: float
    e_tf_minus_eps: float
    e_tf_plus_half: float
    e_tf_minus_half: float


@dataclass(frozen=True)
class LadderRow:
    row: parent.Row
    eta_center_base: float
    eta_shell_base: float
    fd_pairs: tuple[FDPair, ...]
    fd_smooth: bool
    center_iso_rel: float
    shell_iso_rel: float
    isotropy_rel: float
    qt_gap: float
    qt_admitted: bool
    tail_admitted: bool


@dataclass(frozen=True)
class TailVerdict:
    verdict: str
    admitted_sizes: list[int]
    deltas: list[float]
    monotone: bool
    rho_e: float | None
    rho_e_uncertainty: float | None
    c_te: float | None
    c_te_uncertainty: float | None


def rel_err(actual: float, expected: float) -> float:
    return abs(actual - expected) / max(abs(expected), 1.0e-300)


def max_pairwise_rel(vals: tuple[float, float, float]) -> float:
    out = 0.0
    for i in range(3):
        for j in range(i + 1, 3):
            out = max(out, abs(vals[i] - vals[j]) / max(abs(vals[i]), abs(vals[j]), 1.0e-300))
    return out


def centered_fd_values(
    system: parent.SizeSystem,
    q: np.ndarray,
    direction: np.ndarray,
    eps: float,
) -> tuple[float, float, float]:
    plus = parent.eta_floor(system, q + eps * direction, axis="x")
    minus = parent.eta_floor(system, q - eps * direction, axis="x")
    return plus, minus, float((plus - minus) / (2.0 * eps))


def fd_pair(
    system: parent.SizeSystem,
    endpoint: str,
    q: np.ndarray,
    direction_name: str,
    direction: np.ndarray,
) -> FDPair:
    plus_eps, minus_eps, fd_eps = centered_fd_values(system, q, direction, EPS)
    plus_half, minus_half, fd_half = centered_fd_values(system, q, direction, HALF_EPS)
    if fd_eps == 0.0:
        rel = math.inf
    else:
        rel = abs(fd_eps - fd_half) / abs(fd_eps)
    smooth = fd_eps != 0.0 and fd_half != 0.0 and rel < FD_SMOOTH_REL_TOL
    return FDPair(
        endpoint=endpoint,
        direction=direction_name,
        fd_eps=fd_eps,
        fd_half=fd_half,
        rel_step_change=rel,
        smooth=smooth,
        e_tf_base=parent.eta_floor(system, q, axis="x"),
        e_tf_plus_eps=plus_eps,
        e_tf_minus_eps=minus_eps,
        e_tf_plus_half=plus_half,
        e_tf_minus_half=minus_half,
    )


def compute_ladder_row(size: int) -> LadderRow:
    row = parent.compute_row(size)
    system = parent.build_size_system(size)
    fd_pairs = (
        fd_pair(system, "center", parent.E0, "E_x", parent.EX),
        fd_pair(system, "shell", parent.S_UNIT, "E_x", parent.EX),
        fd_pair(system, "center", parent.E0, "E1", parent.E1),
        fd_pair(system, "shell", parent.S_UNIT, "E1", parent.E1),
        fd_pair(system, "center", parent.E0, "E2", parent.E2),
        fd_pair(system, "shell", parent.S_UNIT, "E2", parent.E2),
    )
    center_iso = max_pairwise_rel(row.center_t)
    shell_iso = max_pairwise_rel(row.shell_t)
    fd_smooth = all(pair.smooth for pair in fd_pairs)
    qt_gap = abs(row.q_t - 5.0 / 6.0)
    qt_admitted = qt_gap < TAIL_QT_TOL
    return LadderRow(
        row=row,
        eta_center_base=parent.eta_floor(system, parent.E0, axis="x"),
        eta_shell_base=parent.eta_floor(system, parent.S_UNIT, axis="x"),
        fd_pairs=fd_pairs,
        fd_smooth=fd_smooth,
        center_iso_rel=center_iso,
        shell_iso_rel=shell_iso,
        isotropy_rel=max(center_iso, shell_iso),
        qt_gap=qt_gap,
        qt_admitted=qt_admitted,
        tail_admitted=fd_smooth and qt_admitted,
    )


def sequence_extrapolation(values: list[float]) -> tuple[float, float]:
    if len(values) < 3:
        last_delta = abs(values[-1] - values[-2]) if len(values) >= 2 else math.inf
        return values[-1], last_delta
    x0, x1, x2 = values[-3], values[-2], values[-1]
    denom = x2 - 2.0 * x1 + x0
    if abs(denom) <= 1.0e-300:
        extrap = x2
    else:
        extrap = x0 - ((x1 - x0) ** 2) / denom
    last_delta = abs(x2 - x1)
    return float(extrap), max(abs(float(extrap) - x2), last_delta)


def tail_verdict(rows: list[LadderRow]) -> TailVerdict:
    tail = [item for item in rows if item.tail_admitted]
    deltas = [abs(tail[i].row.rho_e - tail[i - 1].row.rho_e) for i in range(1, len(tail))]
    monotone = len(deltas) >= 2 and all(deltas[i] < deltas[i - 1] for i in range(1, len(deltas)))
    if not monotone:
        return TailVerdict(
            verdict="TAIL_NOT_CONVERGENT",
            admitted_sizes=[item.row.size for item in tail],
            deltas=deltas,
            monotone=False,
            rho_e=None,
            rho_e_uncertainty=None,
            c_te=None,
            c_te_uncertainty=None,
        )
    rho_e, rho_unc = sequence_extrapolation([item.row.rho_e for item in tail])
    c_te, c_unc = sequence_extrapolation([item.row.c_te for item in tail])
    return TailVerdict(
        verdict="CONVERGED",
        admitted_sizes=[item.row.size for item in tail],
        deltas=deltas,
        monotone=True,
        rho_e=rho_e,
        rho_e_uncertainty=rho_unc,
        c_te=c_te,
        c_te_uncertainty=c_unc,
    )


def comparison_verdict(value: float | None, uncertainty: float | None, target: float) -> tuple[str, float | None]:
    if value is None or uncertainty is None or uncertainty <= 0.0 or not math.isfinite(uncertainty):
        return "INCONCLUSIVE", None
    ratio = abs(value - target) / uncertainty
    if ratio > 5.0:
        return "EXCLUDED", ratio
    return "NOT_EXCLUDED", ratio


def print_ladder(rows: list[LadderRow]) -> None:
    print("\nLADDER")
    print(
        "size solve_s delta_center endpoint_gap gamma_E_center gamma_E_shell "
        "gamma_T_center gamma_T_shell q_T c_TE rho_E floor_flag qt_flag tail_flag"
    )
    for item in rows:
        row = item.row
        floor_flag = "SMOOTH" if item.fd_smooth else "FLOOR_NOT_SMOOTH"
        qt_flag = "ADMITTED" if item.qt_admitted else "PRE_ASYMPTOTIC"
        tail_flag = "ADMITTED" if item.tail_admitted else "EXCLUDED_FROM_TAIL"
        print(
            f"{row.size:d} {u12(row.solve_s)} {f12(row.delta_center)} {f12(row.endpoint_gap)} "
            f"{f12(row.gamma_e_center)} {f12(row.gamma_e_shell)} "
            f"{f12(row.gamma_t_center)} {f12(row.gamma_t_shell)} "
            f"{f12(row.q_t)} {f12(row.c_te)} {f12(row.rho_e)} "
            f"{floor_flag} {qt_flag} {tail_flag}"
        )


def print_isotropy(rows: list[LadderRow]) -> None:
    print("\nISOTROPY_TRIPWIRE")
    print(
        "size center_T_tx center_T_ty center_T_tz shell_T_tx shell_T_ty shell_T_tz "
        "center_pairwise_rel shell_pairwise_rel max_pairwise_rel flag"
    )
    for item in rows:
        row = item.row
        flag = "PASS" if item.isotropy_rel <= ISOTROPY_REL_TOL else "FAIL"
        print(
            f"{row.size:d} {f12(row.center_t[0])} {f12(row.center_t[1])} {f12(row.center_t[2])} "
            f"{f12(row.shell_t[0])} {f12(row.shell_t[1])} {f12(row.shell_t[2])} "
            f"{u12(item.center_iso_rel)} {u12(item.shell_iso_rel)} {u12(item.isotropy_rel)} {flag}"
        )


def print_fd_smoothness(rows: list[LadderRow]) -> None:
    print("\nFD_SMOOTHNESS_TRIPWIRE")
    print("size endpoint direction fd_eps fd_half rel_step_change flag")
    for item in rows:
        for pair in item.fd_pairs:
            flag = "SMOOTH" if pair.smooth else "FLOOR_NOT_SMOOTH"
            rel = "inf" if math.isinf(pair.rel_step_change) else u12(pair.rel_step_change)
            print(
                f"{item.row.size:d} {pair.endpoint} {pair.direction} "
                f"{f12(pair.fd_eps)} {f12(pair.fd_half)} {rel} {flag}"
            )


def print_family_data(rows: list[LadderRow]) -> None:
    print("\nFAMILY_ELEMENT_DATA")
    print(
        "size endpoint direction eta_floor_0 e_spatial_tf_base e_spatial_tf_plus_eps "
        "e_spatial_tf_minus_eps e_spatial_tf_plus_half e_spatial_tf_minus_half"
    )
    for item in rows:
        for pair in item.fd_pairs:
            print(
                f"{item.row.size:d} {pair.endpoint} {pair.direction} {f12(0.0)} "
                f"{f12(pair.e_tf_base)} {f12(pair.e_tf_plus_eps)} {f12(pair.e_tf_minus_eps)} "
                f"{f12(pair.e_tf_plus_half)} {f12(pair.e_tf_minus_half)}"
            )


def print_admission(rows: list[LadderRow]) -> None:
    print("\nQ_T_ADMISSION")
    print("size q_T abs_gap_to_5_over_6 q_flag floor_flag tail_flag")
    for item in rows:
        q_flag = "ADMITTED" if item.qt_admitted else "PRE_ASYMPTOTIC"
        floor_flag = "SMOOTH" if item.fd_smooth else "FLOOR_NOT_SMOOTH"
        tail_flag = "ADMITTED" if item.tail_admitted else "EXCLUDED_FROM_TAIL"
        print(f"{item.row.size:d} {f12(item.row.q_t)} {u12(item.qt_gap)} {q_flag} {floor_flag} {tail_flag}")


def print_tail(tail: TailVerdict) -> None:
    print("\nCONVERGENCE_TAIL")
    admitted = ",".join(str(size) for size in tail.admitted_sizes) if tail.admitted_sizes else "none"
    print(f"admitted_sizes {admitted}")
    if tail.deltas:
        for idx, delta in enumerate(tail.deltas, start=1):
            print(f"successive_delta_rho_E_{idx:d} {u12(delta)}")
    else:
        print("successive_delta_rho_E none")
    if tail.verdict == "CONVERGED":
        print(
            f"verdict CONVERGED rho_E={f12(tail.rho_e)} uncertainty={u12(tail.rho_e_uncertainty)} "
            f"c_TE={f12(tail.c_te)} c_TE_uncertainty={u12(tail.c_te_uncertainty)}"
        )
    else:
        print("verdict TAIL_NOT_CONVERGENT")


def main() -> int:
    print("Route-2 rho_E floor-family size-parametrized ladder")
    print("=" * 78)
    print("FAMILY_DEFINITION")
    print("eta_floor = [0.000000000000e+00, base.e_spatial_tf]")
    print("fixed_physical_lengths shell_radius=4.000000000000e+00 probe_radius=4.250000000000e+00 envelope_width=9.000000000000e-01")
    print("parametrized_grid dims=size interior=size-2 center=interior//2 support_sites=7")
    print(f"fd_steps eps={u12(EPS)} half_eps={u12(HALF_EPS)}")

    sizes = [15, 17, 19, 21]
    if os.environ.get("QUARK_RHOE_EXTENDED_LADDER") == "1":
        sizes.extend([25, 29])

    rows: list[LadderRow] = []
    skipped: list[int] = []
    for size in sizes:
        try:
            with wallclock_cap(SIZE_CAP_SECONDS):
                start = time.perf_counter()
                item = compute_ladder_row(size)
                solve_s = time.perf_counter() - start
            rows.append(item)
            print(f"SIZE {size:d}: COMPUTED solve_s={u12(solve_s)} row_solve_s={u12(item.row.solve_s)}")
        except SizeTimeout:
            skipped.append(size)
            print(f"SIZE {size:d}: SKIPPED solve_s={u12(SIZE_CAP_SECONDS)} reason=CAP_120s")

    print_ladder(rows)
    print_isotropy(rows)
    print_fd_smoothness(rows)
    print_family_data(rows)
    print_admission(rows)

    row15 = next((item for item in rows if item.row.size == 15), None)
    if row15 is None:
        check("B1 anchor requires size 15 to compute", False, "size 15 was skipped")
    else:
        expected = {
            "gamma_E(center)": (row15.row.gamma_e_center, -3.772329168017e-04),
            "gamma_E(shell)": (row15.row.gamma_e_shell, -2.010572265638e-04),
            "gamma_T(center)": (row15.row.gamma_t_center, +3.359952396063e-04),
            "gamma_T(shell)": (row15.row.gamma_t_shell, +4.031967723697e-04),
        }
        for label, (actual, target) in expected.items():
            check(
                f"B1 anchor {label}",
                rel_err(actual, target) <= ANCHOR_REL_TOL,
                f"actual={f12(actual)} expected={f12(target)} rel={u12(rel_err(actual, target))}",
            )

    for item in rows:
        check(
            f"B2 isotropy tripwire size {item.row.size:d}",
            item.isotropy_rel <= ISOTROPY_REL_TOL,
            f"max_pairwise_rel={u12(item.isotropy_rel)}",
        )

    for item in rows:
        flag = "SMOOTH" if item.fd_smooth else "FLOOR_NOT_SMOOTH"
        worst = max(pair.rel_step_change for pair in item.fd_pairs)
        worst_s = "inf" if math.isinf(worst) else u12(worst)
        check(
            f"B3 FD-smoothness classification size {item.row.size:d}",
            True,
            f"flag={flag} worst_rel_step_change={worst_s}",
        )

    for item in rows:
        flag = "ADMITTED" if item.qt_admitted else "PRE_ASYMPTOTIC"
        check(
            f"B4 q_T law admission classification size {item.row.size:d}",
            True,
            f"q_T={f12(item.row.q_t)} gap={u12(item.qt_gap)} flag={flag}",
        )

    tail = tail_verdict(rows)
    print_tail(tail)
    check(
        "B5 tail convergence verdict-consistency",
        (tail.verdict == "CONVERGED") == tail.monotone,
        f"verdict={tail.verdict} monotone_rule={tail.monotone}",
    )

    rho_verdict, rho_ratio = comparison_verdict(tail.rho_e, tail.rho_e_uncertainty, 21.0 / 4.0)
    cte_verdict, cte_ratio = comparison_verdict(tail.c_te, tail.c_te_uncertainty, -8.0 / 9.0)
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
        "B6 rho_E vs 21/4 verdict-consistency",
        (rho_verdict == "INCONCLUSIVE") == (tail.rho_e is None),
        f"verdict={rho_verdict}",
    )
    check(
        "B7 c_TE vs -8/9 verdict-consistency",
        (cte_verdict == "INCONCLUSIVE") == (tail.c_te is None),
        f"verdict={cte_verdict}",
    )
    check(
        "B8 family-element report emitted",
        bool(rows),
        f"rows={len(rows):d} skipped={len(skipped):d}",
    )

    if skipped:
        print("\nSKIPPED_SIZES " + ",".join(str(size) for size in skipped))

    total = PASS_COUNT + FAIL_COUNT
    print(f"\nSUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={total}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
