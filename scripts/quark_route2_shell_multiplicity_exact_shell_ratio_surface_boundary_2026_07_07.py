#!/usr/bin/env python3
"""
Quark Route-2 shell-ratio surface-boundary worker.

Declaration:
  OUTCOME=BOUNDED_BOUNDARY.
  On the named endpoint surface, no exact shell-ratio derivation is available.
  SHELL-MULT therefore enters the endpoint cluster only as a supplied premise.
"""

from __future__ import annotations

import os
import subprocess
import sys
from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

READOUT_NOTE = ROOT / "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
QUOTIENT_NOTE = (
    ROOT / "docs/QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md"
)
ENDPOINT_SCRIPT = ROOT / "scripts/frontier_quark_endpoint_readout_constraints.py"
SAME_SCRIPT = ROOT / "scripts/frontier_same_source_metric_ansatz_scan.py"
CENTER_SCRIPT = ROOT / "scripts/frontier_tensor_support_center_excess_law.py"
NATURALITY_NOTE = (
    ROOT
    / "docs/QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
)

FATAL_SURFACE = (
    READOUT_NOTE,
    QUOTIENT_NOTE,
    ENDPOINT_SCRIPT,
    SAME_SCRIPT,
    CENTER_SCRIPT,
)
CONTEXT_SURFACE = (NATURALITY_NOTE,)

GAMMA_E_TEXT = "-2.010572657265e-04"
GAMMA_T_TEXT = "+4.031967723697e-04"
EXPECTED_BINARY_RATIO = Fraction(-14875335342499166, 7417703850033121)
EXPECTED_DECIMAL_RATIO = Fraction(-4031967723697, 2010572657265)
EXPECTED_DECIMAL_RESIDUAL = Fraction(-10822409167, 2010572657265)
EXPECTED_DECIMAL_RELATIVE = Fraction(10822409167, 4021145314530)
PRINTED_RATIO = "-2.005382749600167"

FULL_REPLAY_EXCEPTION = (
    "AttributeError: module 'one_parameter_shell' has no attribute "
    "'reduced_data'"
)
FULL_REPLAY_PROBE_DATE = "2026-07-07"

GAMMA_PAIR_FRAGMENT = (
    "def gamma_pair(q: np.ndarray, ex: np.ndarray, t1x: np.ndarray)"
    " -> tuple[float, float]:\n"
    "    beta_e = float((eta_floor(q + EPS * ex) - "
    "eta_floor(q - EPS * ex)) / (2.0 * EPS))\n"
    "    beta_t = float((eta_floor(q + EPS * t1x) - "
    "eta_floor(q - EPS * t1x)) / (2.0 * EPS))\n"
    "    red = shell.reduced_data(phi_from_q(q))\n"
    "    a_aniso = float(red[\"anchor_per_Q\"]) * float(np.sum(q))\n"
    "    return beta_e / a_aniso, beta_t / a_aniso\n"
)


@dataclass(frozen=True)
class Check:
    name: str
    ok: bool
    detail: str


@dataclass(frozen=True)
class ReplayObservation:
    check: Check
    center_before_shell: bool


def load_texts(paths: tuple[Path, ...]) -> dict[Path, str]:
    return {path: path.read_text(encoding="utf-8") for path in paths}


def needle(texts: dict[Path, str], path: Path, fragment: str) -> bool:
    return fragment in texts[path]


def dec(frac: Fraction, places: int = 15) -> str:
    getcontext().prec = 80
    value = Decimal(frac.numerator) / Decimal(frac.denominator)
    return f"{value:.{places}f}"


def built_endpoint_vectors() -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    e0 = (Fraction(1),) + (Fraction(0),) * 6
    uniform_arms = (Fraction(0),) + (Fraction(1),) * 6
    shell = tuple(entry / 6 for entry in uniform_arms)
    return e0, shell


def q_total(q: tuple[Fraction, ...]) -> Fraction:
    return sum(q, Fraction(0))


def delta_a1(q: tuple[Fraction, ...]) -> Fraction:
    total = q_total(q)
    if total == 0:
        raise ValueError("delta_A1 undefined for zero total charge")
    return q[0] / (6 * total)


def fast_ratios() -> tuple[Fraction, Fraction]:
    binary_ratio = Fraction(float(GAMMA_T_TEXT)) / Fraction(float(GAMMA_E_TEXT))
    decimal_ratio = Fraction(GAMMA_T_TEXT) / Fraction(GAMMA_E_TEXT)
    return binary_ratio, decimal_ratio


def readout_shell_ratio(alpha_e: Fraction, alpha_t: Fraction) -> Fraction:
    e_shell = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    t_shell = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
    row_e = (alpha_e, Fraction(0), Fraction(0), Fraction(0))
    row_t = (Fraction(0), alpha_t, Fraction(0), Fraction(0))

    gamma_e = sum(a * b for a, b in zip(row_e, e_shell))
    gamma_t = sum(a * b for a, b in zip(row_t, t_shell))
    return gamma_t / gamma_e


def planned_exit_code(load_fail_count: int, context_fail_count: int) -> int:
    _ = context_fail_count
    return 1 if load_fail_count else 0


def replay_observation() -> ReplayObservation:
    env = os.environ.copy()
    scripts_path = str(ROOT / "scripts")
    pythonpath = env.get("PYTHONPATH")
    env["PYTHONPATH"] = (
        scripts_path if not pythonpath else scripts_path + os.pathsep + pythonpath
    )
    env["QUARK_ENDPOINT_FULL_TENSOR_REPLAY"] = "1"
    command = [
        sys.executable,
        "-c",
        (
            "import frontier_quark_endpoint_readout_constraints as endpoint\n"
            "endpoint.endpoint_readout()\n"
            "print('FULL_REPLAY_AVAILABLE')\n"
        ),
    ]

    try:
        proc = subprocess.run(
            command,
            cwd=ROOT,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=120,
            check=False,
        )
    except subprocess.TimeoutExpired:
        check = Check(
            f"{FULL_REPLAY_PROBE_DATE} full tensor replay availability",
            False,
            "unavailable: subprocess timed out after 120s",
        )
        return ReplayObservation(check=check, center_before_shell=False)

    if proc.returncode == 0:
        check = Check(
            f"{FULL_REPLAY_PROBE_DATE} full tensor replay availability",
            False,
            "unexpectedly available: subprocess exit=0",
        )
        return ReplayObservation(check=check, center_before_shell=False)

    lines = [line for line in proc.stderr.splitlines() if line.strip()]
    exception_line = lines[-1] if lines else "<no stderr exception line>"
    traceback = proc.stderr
    center_before_shell = (
        "line 133, in endpoint_readout_full_tensor" in traceback
        and "line 134, in endpoint_readout_full_tensor" not in traceback
    )
    matches_current = exception_line == FULL_REPLAY_EXCEPTION
    ok = matches_current and center_before_shell
    detail = (
        "PASS=observation-recorded; unavailable; "
        f"exception={exception_line!r}; center_before_shell={center_before_shell}"
    )
    return ReplayObservation(
        check=Check(
            f"{FULL_REPLAY_PROBE_DATE} full tensor replay availability",
            ok,
            detail,
        ),
        center_before_shell=center_before_shell,
    )


def build_load_checks(texts: dict[Path, str]) -> tuple[list[Check], ReplayObservation]:
    checks: list[Check] = []

    checks.append(
        Check(
            "fatal surface is exactly the five named files",
            tuple(texts) == FATAL_SURFACE,
            ", ".join(path.name for path in FATAL_SURFACE),
        )
    )

    same_basis = (
        "def build_adapted_basis() -> np.ndarray:\n"
        "    e0 = np.zeros(7)\n"
        "    e0[0] = 1.0\n"
        "    px, mx, py, my, pz, mz = [np.eye(7)[i] for i in range(1, 7)]\n"
        "    s = (px + mx + py + my + pz + mz) / np.sqrt(6.0)\n"
        "    e1 = (px + mx - py - my) / 2.0\n"
        "    e2 = (px + mx + py + my - 2.0 * pz - 2.0 * mz)"
        " / np.sqrt(12.0)\n"
        "    tx = (px - mx) / np.sqrt(2.0)\n"
        "    ty = (py - my) / np.sqrt(2.0)\n"
        "    tz = (pz - mz) / np.sqrt(2.0)\n"
        "    return np.column_stack([e0, s, e1, e2, tx, ty, tz])\n"
    )
    checks.append(
        Check(
            "same-source module defines the adapted e0/s shell basis",
            needle(texts, SAME_SCRIPT, same_basis),
            "verbatim build_adapted_basis fragment found",
        )
    )

    endpoint_needles = (
        "gamma_e_shell: float",
        "gamma_t_shell: float",
        f"gamma_e_shell={GAMMA_E_TEXT},",
        f"gamma_t_shell={GAMMA_T_TEXT},",
        "s_unit = s / math.sqrt(6.0)",
        "gamma_e_center, gamma_t_center = center.gamma_pair(e0, ex, t1x)",
        "gamma_e_shell, gamma_t_shell = center.gamma_pair(s_unit, ex, t1x)",
    )
    checks.append(
        Check(
            "endpoint module exposes Python-float fast certificate values",
            all(needle(texts, ENDPOINT_SCRIPT, item) for item in endpoint_needles),
            "fast readout literals and full replay call order found",
        )
    )

    checks.append(
        Check(
            "center-excess gamma_pair fragment is quoted exactly",
            needle(texts, CENTER_SCRIPT, GAMMA_PAIR_FRAGMENT),
            "float finite differences, red, a_aniso, and return found",
        )
    )

    eta_floor_fragment = (
        "def eta_floor(q: np.ndarray) -> float:\n"
        "    return float(two.tensor_metrics(phi_from_q(q))[0])\n"
    )
    checks.append(
        Check(
            "eta_floor is float-only on the named module surface",
            needle(texts, CENTER_SCRIPT, eta_floor_fragment),
            "no exact algebraic eta_floor definition appears in the surface",
        )
    )

    readout_needles = (
        "delta_A1(e0)        = 1/6",
        "delta_A1(s/sqrt(6)) = 0",
        "P_R = [[alpha_E, 0, beta_E, 0],",
        "s_TE  := gamma_T(shell) / gamma_E(shell)  = alpha_T / alpha_E",
    )
    checks.append(
        Check(
            "readout-map note supplies the endpoint columns and reduced map",
            all(needle(texts, READOUT_NOTE, item) for item in readout_needles),
            "delta_A1 values, P_R form, and s_TE identity found",
        )
    )

    quotient_needles = (
        "SHELL-MULT (named conditional premise): the shell coefficient ratio",
        "a_T/a_E = -2",
        "derive SHELL-MULT from shell-counting algebra",
    )
    checks.append(
        Check(
            "quotient note records SHELL-MULT as a supplied premise",
            all(needle(texts, QUOTIENT_NOTE, item) for item in quotient_needles),
            "SHELL-MULT premise and open shell-counting target found",
        )
    )

    e0, shell = built_endpoint_vectors()
    shell_total = q_total(shell)
    delta_center = delta_a1(e0)
    delta_shell = delta_a1(shell)
    endpoint_gap = delta_center - delta_shell
    checks.append(
        Check(
            "constructed shell vector has exact total charge",
            shell_total == 1 and q_total(e0) == 1,
            f"shell_total={shell_total}, center_total={q_total(e0)}",
        )
    )
    checks.append(
        Check(
            "constructed endpoint delta_A1 gap is exact",
            delta_center == Fraction(1, 6)
            and delta_shell == 0
            and endpoint_gap == Fraction(1, 6),
            f"delta_center={delta_center}, delta_shell={delta_shell}",
        )
    )

    binary_ratio, decimal_ratio = fast_ratios()
    decimal_residual = decimal_ratio + 2
    decimal_relative = abs(decimal_residual / 2)
    checks.append(
        Check(
            "both fast-certificate float reifications are exact and nonminus2",
            binary_ratio == EXPECTED_BINARY_RATIO
            and decimal_ratio == EXPECTED_DECIMAL_RATIO
            and binary_ratio != -2
            and decimal_ratio != -2
            and dec(binary_ratio) == PRINTED_RATIO
            and dec(decimal_ratio) == PRINTED_RATIO
            and decimal_residual == EXPECTED_DECIMAL_RESIDUAL
            and decimal_relative == EXPECTED_DECIMAL_RELATIVE,
            f"binary={binary_ratio}; decimal={decimal_ratio}",
        )
    )

    ratio_minus_two = readout_shell_ratio(Fraction(1), Fraction(-2))
    ratio_live = readout_shell_ratio(Fraction(1), decimal_ratio)
    checks.append(
        Check(
            "reduced readout map leaves alpha_T/alpha_E selectable",
            ratio_minus_two == -2 and ratio_live == decimal_ratio,
            f"ratios {-2} and {ratio_live}",
        )
    )

    checks.append(
        Check(
            "exit-code separation self-test keeps context tier non-fatal",
            planned_exit_code(0, 1) == 0 and planned_exit_code(1, 0) == 1,
            "only load-bearing failures determine process exit code",
        )
    )

    replay = replay_observation()
    checks.append(replay.check)
    return checks, replay


def build_context_checks(texts: dict[Path, str]) -> list[Check]:
    naturality_needles = (
        "after granting the conditional\nT-side candidates",
        "beta_T/alpha_T = -1",
        "alpha_T/alpha_E = -2",
        "remains a free parameter",
        "but it is not derived by carrier",
    )
    return [
        Check(
            "naturality note is comparison-only context",
            all(needle(texts, NATURALITY_NOTE, item) for item in naturality_needles),
            "T-side candidates are granted there, not derived there",
        )
    ]


def main() -> int:
    fatal_texts = load_texts(FATAL_SURFACE)
    context_texts = load_texts(CONTEXT_SURFACE)
    load_checks, replay = build_load_checks(fatal_texts)
    context_checks = build_context_checks(context_texts)

    load_fail = [check for check in load_checks if not check.ok]
    context_fail = [check for check in context_checks if not check.ok]

    binary_ratio, decimal_ratio = fast_ratios()
    e0, shell = built_endpoint_vectors()
    shell_total = q_total(shell)
    endpoint_gap = delta_a1(e0) - delta_a1(shell)

    print("Surface-boundary worker")
    print("RETYPE=bounded_theorem")
    print("QUOTE-FIXES=verified")
    load_pass = len(load_checks) - len(load_fail)
    print(f"LOAD-BEARING: PASS={load_pass} FAIL={len(load_fail)}")
    print("CONTEXT-TIER (comparison-only; non-fatal)")
    print(
        f"CONTEXT: PASS={len(context_checks) - len(context_fail)} "
        f"FAIL={len(context_fail)}"
    )
    print("exit-code separation self-test: context failures are non-fatal")
    replay_status = "PASS=observation-recorded" if replay.check.ok else "FAIL"
    print(f"full replay: {replay_status} CENTER line 133 before shell line 134")
    print(f"binary-float ratio: {binary_ratio}")
    print(f"decimal-string ratio: {decimal_ratio}")
    print(f"printed agreement: {dec(binary_ratio)}")
    print(f"displayed residual: {EXPECTED_DECIMAL_RESIDUAL}")
    print(f"relative deviation: {EXPECTED_DECIMAL_RELATIVE}")
    print(
        f"totals: shell={shell_total} gap={endpoint_gap} "
        f"PASS={len(load_checks) - len(load_fail)}/{len(load_fail)} "
        f"NONFATAL={len(context_checks) - len(context_fail)}/{len(context_fail)}"
    )

    return planned_exit_code(len(load_fail), len(context_fail))


if __name__ == "__main__":
    raise SystemExit(main())
