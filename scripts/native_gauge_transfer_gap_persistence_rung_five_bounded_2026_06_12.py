#!/usr/bin/env python3
"""Native gauge-transfer gap persistence rung-five bounded runner.

This runner stays on the repo-native SU(3) dominant-weight packet tower.
It separates the measured finite-block gap from the fixed-shell certificate
tail slack and extends the certified shell from B_14 to B_16.

No continuum limit, physical beta=6 environment claim, comparator import, or
audit status is asserted by this runner.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import factorial, isqrt
from pathlib import Path
import sys

import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve as src_existing


AUDIT_TIMEOUT_SEC = 540

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_GAP_PERSISTENCE_RUNG_FIVE_BOUNDED_NOTE_2026-06-12.md"
)
RUNG_FOUR_NOTE_PATH = REPO_ROOT / ".claude" / "tmp" / "refs" / "RUNG_FOUR_NOTE.md"

COEFF_ORDER = 80
M_ORDER = 60
EXP_BOUND_ORDER = 120
SQRT_SCALE = 10**24
CERT_SHELL = 16
TRUE_MODE_MAX = 360
WITNESS_MODE_MAX = 280
WITNESS_OUTER_SHELL = 30

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ShellPathCache:
    shell: int
    weights: list[tuple[int, int]]
    path_layers: list[list[list[tuple[int, int]]]]
    outside_counts: list[list[int]]


@dataclass(frozen=True)
class CertificateRow:
    beta: Fraction
    shell: int
    states: int
    lambda0_lower: Fraction
    block_lambda1_upper: Fraction
    tail_radius: Fraction
    ratio_upper: Fraction
    margin: Fraction
    certified: bool
    block_ratio_float: float
    block_bound_ratio: Fraction
    tail_ratio: Fraction
    slack_vs_true: float


RUNG_FOUR_REFERENCE_UPPERS = {
    Fraction(1, 1): "0.425322926519",
    Fraction(2, 1): "0.903165127752",
    Fraction(3, 1): "0.932262113427",
    Fraction(4, 1): "0.770614016905",
    Fraction(117, 25): "0.682850428785",
    Fraction(5, 1): "0.650581920096",
    Fraction(6, 1): "0.578349810928",
    Fraction(7, 1): "0.534543550803",
    Fraction(8, 1): "0.506636535527",
    Fraction(9, 1): "0.488408514518",
    Fraction(10, 1): "0.477091133117",
    Fraction(11, 1): "0.471684682651",
    Fraction(12, 1): "0.472127555693",
    Fraction(14, 1): "0.495103555972",
    Fraction(16, 1): "0.558463006608",
    Fraction(18, 1): "0.676608455810",
    Fraction(20, 1): "0.863200446467",
    Fraction(21, 1): "0.986423897977",
    Fraction(22, 1): "0.962964963029",
}

RUNG_FOUR_FAILURE_UPPERS = {
    Fraction(45, 2): Fraction(1213174568154, 10**12),
    Fraction(23, 1): Fraction(1300701461804, 10**12),
}


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def fmt_beta(beta: Fraction) -> str:
    if beta.denominator == 1:
        return str(beta.numerator)
    return f"{beta.numerator}/{beta.denominator}"


def fmt_dec(x: Fraction | float, digits: int = 12) -> str:
    return f"{float(x):.{digits}f}"


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def recurrence_neighbors(p: int, q: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for a, b in [
        (p + 1, q),
        (p - 1, q + 1),
        (p, q - 1),
        (p, q + 1),
        (p + 1, q - 1),
        (p - 1, q),
    ]:
        if a >= 0 and b >= 0:
            out.append((a, b))
    return out


def weights_box(shell: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(shell + 1) for q in range(shell + 1)]


def multiplicity_layers(order: int) -> list[dict[tuple[int, int], int]]:
    layers: list[dict[tuple[int, int], int]] = []
    layer: dict[tuple[int, int], int] = {(0, 0): 1}
    for _n in range(order + 1):
        layers.append(dict(layer))
        nxt: dict[tuple[int, int], int] = defaultdict(int)
        for weight, mult in layer.items():
            for nb in recurrence_neighbors(*weight):
                nxt[nb] += mult
        layer = dict(nxt)
    return layers


LAYERS = multiplicity_layers(COEFF_ORDER)
COEFF_CACHE: dict[Fraction, dict[tuple[int, int], Fraction]] = {}
EXP_SUM_CACHE: dict[Fraction, Fraction] = {}


def exp_tail_after(x: Fraction, order: int) -> Fraction:
    first = (x ** (order + 1)) / factorial(order + 1)
    ratio = x / Fraction(order + 2, 1)
    if ratio >= 1:
        raise ValueError("geometric exponential tail bound needs x < order + 2")
    return first / (1 - ratio)


def exp_sum_upper(x: Fraction) -> Fraction:
    cached = EXP_SUM_CACHE.get(x)
    if cached is not None:
        return cached
    total = Fraction(0, 1)
    term = Fraction(1, 1)
    for n in range(EXP_BOUND_ORDER + 1):
        if n == 0:
            term = Fraction(1, 1)
        elif n == 1:
            term = x
        else:
            term *= x / n
        total += term
    out = total + exp_tail_after(x, EXP_BOUND_ORDER)
    EXP_SUM_CACHE[x] = out
    return out


def sqrt_upper(x: Fraction, scale: int = SQRT_SCALE) -> Fraction:
    if x < 0:
        raise ValueError("sqrt_upper expects a nonnegative Fraction")
    if x == 0:
        return Fraction(0, 1)
    target_num = x.numerator * scale * scale
    target_den = x.denominator
    q = target_num // target_den
    root = isqrt(q)
    while root * root * target_den < target_num:
        root += 1
    return Fraction(root, scale)


def coefficient_partials(beta: Fraction) -> dict[tuple[int, int], Fraction]:
    cached = COEFF_CACHE.get(beta)
    if cached is not None:
        return cached
    coeffs: dict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for n, layer in enumerate(LAYERS):
        factor = (beta**n) / (factorial(n) * (6**n))
        for weight, mult in layer.items():
            coeffs[weight] += mult * factor
    out = dict(coeffs)
    COEFF_CACHE[beta] = out
    return out


def ratio_bounds_for_shell(
    beta: Fraction, shell: int
) -> tuple[list[Fraction], list[Fraction], Fraction, Fraction]:
    weights = weights_box(shell)
    coeffs = coefficient_partials(beta)
    c00_lower = coeffs[(0, 0)]
    tail = exp_tail_after(beta, COEFF_ORDER)
    c00_upper = c00_lower + tail

    lower: list[Fraction] = []
    upper: list[Fraction] = []
    for p, q in weights:
        partial = coeffs.get((p, q), Fraction(0, 1))
        lower.append(partial / c00_upper)
        upper.append((partial + tail / dim_su3(p, q)) / c00_lower)

    tail_sup = Fraction(0, 1)
    for (p, q), partial in coeffs.items():
        if p > shell or q > shell:
            row_upper = (partial + tail / dim_su3(p, q)) / c00_lower
            if row_upper > tail_sup:
                tail_sup = row_upper
    far_dim_min = (COEFF_ORDER + 2) * (COEFF_ORDER + 3) // 2
    tail_sup = max(tail_sup, (tail / far_dim_min) / c00_lower)

    return lower, upper, tail_sup, max(upper)


def precompute_shell_path_data(shell: int, order: int) -> ShellPathCache:
    weights = weights_box(shell)
    index = {w: i for i, w in enumerate(weights)}
    path_layers: list[list[list[tuple[int, int]]]] = []
    outside_counts: list[list[int]] = []
    for start_weight in weights:
        layer: dict[tuple[int, int], int] = {start_weight: 1}
        start_layers: list[list[tuple[int, int]]] = []
        start_outside: list[int] = []
        for _n in range(order + 1):
            entries: list[tuple[int, int]] = []
            outside_total = 0
            for weight, mult in layer.items():
                row = index.get(weight)
                if row is None:
                    outside_total += mult
                else:
                    entries.append((row, mult))
            start_layers.append(entries)
            start_outside.append(outside_total)
            nxt: dict[tuple[int, int], int] = defaultdict(int)
            for weight, mult in layer.items():
                for nb in recurrence_neighbors(*weight):
                    nxt[nb] += mult
            layer = dict(nxt)
        path_layers.append(start_layers)
        outside_counts.append(start_outside)
    return ShellPathCache(shell, weights, path_layers, outside_counts)


def half_slice_matrix_partial(beta: Fraction, cache: ShellPathCache) -> list[list[Fraction]]:
    size = len(cache.weights)
    tau = beta / 2
    factors: list[Fraction] = []
    factor = Fraction(1, 1)
    for n in range(M_ORDER + 1):
        if n == 0:
            factor = Fraction(1, 1)
        elif n == 1:
            factor = tau / 6
        else:
            factor *= tau / (6 * n)
        factors.append(factor)

    matrix = [[Fraction(0, 1) for _ in range(size)] for _ in range(size)]
    for col, by_n in enumerate(cache.path_layers):
        for n, entries in enumerate(by_n):
            f = factors[n]
            for row, mult in entries:
                matrix[row][col] += mult * f
    return matrix


def matvec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def rayleigh_lower(
    matrix: list[list[Fraction]], r_lower: list[Fraction], vector: np.ndarray
) -> Fraction:
    scale = 10**12
    if float(np.sum(vector)) < 0.0:
        vector = -vector
    v = [Fraction(max(float(x), 1.0e-30)).limit_denominator(scale) for x in vector]
    y = matvec(matrix, v)
    z = [r_lower[i] * y[i] for i in range(len(y))]
    av = matvec(matrix, z)
    numerator = sum(v[i] * av[i] for i in range(len(v)))
    denominator = sum(x * x for x in v)
    return numerator / denominator


def trace_upper(
    matrix: list[list[Fraction]], r_upper: list[Fraction], m_tail: Fraction
) -> Fraction:
    total = Fraction(0, 1)
    size = len(matrix)
    for k in range(size):
        col_sum = Fraction(0, 1)
        for i in range(size):
            entry_upper = matrix[i][k] + m_tail
            col_sum += entry_upper * entry_upper
        total += r_upper[k] * col_sum
    return total


def float_block_spectrum(
    matrix: list[list[Fraction]], r_mid: list[Fraction]
) -> tuple[np.ndarray, np.ndarray]:
    m = np.array([[float(x) for x in row] for row in matrix], dtype=float)
    r = np.array([float(x) for x in r_mid], dtype=float)
    transfer = (m * r[None, :]) @ m
    eigvals, eigvecs = np.linalg.eigh(transfer)
    return eigvals, eigvecs


def outside_ratio_mass_upper(beta: Fraction, shell: int) -> Fraction:
    coeffs = coefficient_partials(beta)
    c00_lower = coeffs[(0, 0)]
    outside_partial = sum(
        partial for (p, q), partial in coeffs.items() if p > shell or q > shell
    )
    return (outside_partial + exp_tail_after(beta, COEFF_ORDER)) / c00_lower


def leak_l1_upper_from_counts(beta: Fraction, counts: list[int]) -> Fraction:
    tau = beta / 2
    total = Fraction(0, 1)
    factor = Fraction(1, 1)
    for n, outside_count in enumerate(counts):
        if n == 0:
            factor = Fraction(1, 1)
        elif n == 1:
            factor = tau / 6
        else:
            factor *= tau / (6 * n)
        total += outside_count * factor
    return total + exp_tail_after(tau, M_ORDER)


def sharp_delta2(beta: Fraction, cache: ShellPathCache, r_upper: list[Fraction]) -> Fraction:
    p_to_q = sum(
        r_upper[k] * leak_l1_upper_from_counts(beta, cache.outside_counts[k]) ** 2
        for k in range(len(cache.weights))
    )
    q_rows = exp_sum_upper(beta) * outside_ratio_mass_upper(beta, cache.shell)
    return p_to_q + q_rows


def escape_radius_from_delta2(
    beta: Fraction, r_sup: Fraction, delta2: Fraction
) -> Fraction:
    exp_tau = exp_sum_upper(beta / 2)
    delta = sqrt_upper(delta2)
    return 2 * exp_tau * sqrt_upper(r_sup) * delta + delta2


def certify_beta(beta: Fraction, cache: ShellPathCache) -> CertificateRow:
    r_lower, r_upper, tail_sup, r_sup = ratio_bounds_for_shell(beta, cache.shell)
    matrix = half_slice_matrix_partial(beta, cache)
    m_tail = exp_tail_after(beta / 2, M_ORDER)
    r_mid = [(lo + hi) / 2 for lo, hi in zip(r_lower, r_upper)]
    eigvals, eigvecs = float_block_spectrum(matrix, r_mid)
    lambda0_lower = rayleigh_lower(matrix, r_lower, eigvecs[:, -1])
    trace_hi = trace_upper(matrix, r_upper, m_tail)
    block_bound = trace_hi - lambda0_lower

    d2 = sharp_delta2(beta, cache, r_upper)
    escape = escape_radius_from_delta2(beta, r_sup, d2)
    diagonal_tail = exp_sum_upper(beta) * tail_sup
    tail_radius = escape + diagonal_tail
    ratio_upper = (block_bound + tail_radius) / lambda0_lower
    block_ratio = float(eigvals[-2] / eigvals[-1])
    block_bound_ratio = block_bound / lambda0_lower
    tail_ratio = tail_radius / lambda0_lower
    margin = Fraction(1, 1) - ratio_upper
    return CertificateRow(
        beta=beta,
        shell=cache.shell,
        states=len(cache.weights),
        lambda0_lower=lambda0_lower,
        block_lambda1_upper=block_bound,
        tail_radius=tail_radius,
        ratio_upper=ratio_upper,
        margin=margin,
        certified=margin > 0,
        block_ratio_float=block_ratio,
        block_bound_ratio=block_bound_ratio,
        tail_ratio=tail_ratio,
        slack_vs_true=float(ratio_upper) - block_ratio,
    )


def true_ratio_float(shell: int, beta: Fraction, mode_max: int = TRUE_MODE_MAX) -> float:
    beta_f = float(beta)
    j_op, weights, index = src_existing.build_J(shell)
    multiplier = src_existing.matrix_exp_symmetric(j_op, beta_f / 2.0)
    coeffs = np.array(
        [
            src_existing.wilson_character_coefficient(
                p, q, mode_max, beta_f / 3.0
            )
            for p, q in weights
        ],
        dtype=float,
    )
    ratios = coeffs / coeffs[index[(0, 0)]]
    transfer = (multiplier * ratios[None, :]) @ multiplier
    eigvals = np.linalg.eigvalsh(transfer)
    eigvals.sort()
    return float(eigvals[-2] / eigvals[-1])


def finite_outer_box_tail_witness(
    rows: list[CertificateRow], betas: list[Fraction], outer_shell: int
) -> tuple[bool, str]:
    row_by_beta = {row.beta: row for row in rows}
    j_op, weights, index = src_existing.build_J(outer_shell)
    p_indices = np.array(
        [
            idx
            for idx, (p, q) in enumerate(weights)
            if p <= CERT_SHELL and q <= CERT_SHELL
        ],
        dtype=int,
    )

    failures: list[str] = []
    min_op_factor = float("inf")
    min_fro_factor = float("inf")
    frontier_detail = ""
    for beta in betas:
        row = row_by_beta[beta]
        beta_f = float(beta)
        tail_radius = float(row.tail_radius)
        multiplier = src_existing.matrix_exp_symmetric(j_op, beta_f / 2.0)
        coeffs = np.array(
            [
                src_existing.wilson_character_coefficient(
                    p, q, WITNESS_MODE_MAX, beta_f / 3.0
                )
                for p, q in weights
            ],
            dtype=float,
        )
        ratios = coeffs / coeffs[index[(0, 0)]]
        transfer = (multiplier * ratios[None, :]) @ multiplier

        m_pp = multiplier[np.ix_(p_indices, p_indices)]
        r_p = ratios[p_indices]
        block = np.zeros_like(transfer)
        block[np.ix_(p_indices, p_indices)] = (m_pp * r_p[None, :]) @ m_pp
        diff_norm = float(np.max(np.abs(np.linalg.eigvalsh(transfer - block))))

        remainder = multiplier.copy()
        remainder[np.ix_(p_indices, p_indices)] = 0.0
        fro_sq = float(np.sum(ratios[:, None] * remainder * remainder))
        fro_norm = float(np.sqrt(max(fro_sq, 0.0)))

        if tail_radius < diff_norm or tail_radius < fro_norm:
            failures.append(
                f"beta={fmt_beta(beta)} tail_radius={tail_radius:.12e} "
                f"true_op_tail={diff_norm:.12e} weighted_fro={fro_norm:.12e}"
            )
        if diff_norm > 0.0:
            min_op_factor = min(min_op_factor, tail_radius / diff_norm)
        if fro_norm > 0.0:
            min_fro_factor = min(min_fro_factor, tail_radius / fro_norm)
        if beta == Fraction(26, 1):
            frontier_detail = (
                f"beta=26 S={outer_shell} true_op_tail={diff_norm:.12e}, "
                f"tail_radius={tail_radius:.12e}, "
                f"factor={tail_radius / diff_norm:.6f}"
            )
    if failures:
        return False, "; ".join(failures)
    return (
        True,
        f"S={outer_shell}; min tail/true_op_tail={min_op_factor:.6f}, "
        f"min tail/weighted_fro={min_fro_factor:.6f}; {frontier_detail}",
    )


def parse_rung_four_reference_rows() -> tuple[bool, str]:
    text = RUNG_FOUR_NOTE_PATH.read_text(encoding="utf-8")
    missing: list[str] = []
    for beta, upper in RUNG_FOUR_REFERENCE_UPPERS.items():
        row_token = f"| {fmt_beta(beta)} | {upper} |"
        if row_token not in text:
            missing.append(f"{fmt_beta(beta)}->{upper}")
    if missing:
        return False, "missing reference rows: " + ", ".join(missing)
    return True, f"checked {len(RUNG_FOUR_REFERENCE_UPPERS)} beta<=22 reference rows"


def note_text() -> str:
    return NOTE_PATH.read_text(encoding="utf-8")


def print_true_trajectory() -> dict[Fraction, float]:
    trajectory_betas = [
        Fraction(1, 1),
        Fraction(3, 2),
        Fraction(2, 1),
        Fraction(5, 2),
        Fraction(3, 1),
        Fraction(4, 1),
        Fraction(8, 1),
        Fraction(12, 1),
        Fraction(16, 1),
        Fraction(20, 1),
        Fraction(24, 1),
        Fraction(30, 1),
        Fraction(40, 1),
        Fraction(50, 1),
    ]
    out: dict[Fraction, float] = {}
    print("TRUE HALF-SLICE BLOCK RATIOS")
    for beta in trajectory_betas:
        shell = 30 if beta >= 40 else 22
        value = true_ratio_float(shell, beta)
        out[beta] = value
        print(f"true_ratio beta={fmt_beta(beta):>4} shell={shell:>2} value={value:.12f}")
    print()
    return out


def print_stability_rows() -> dict[tuple[Fraction, int], float]:
    out: dict[tuple[Fraction, int], float] = {}
    print("SHELL-STABILITY DIAGNOSTICS")
    for beta in [Fraction(8, 1), Fraction(22, 1), Fraction(30, 1)]:
        vals = []
        for shell in [14, 18, 22]:
            value = true_ratio_float(shell, beta)
            out[(beta, shell)] = value
            vals.append(value)
        print(
            f"stability beta={fmt_beta(beta):>4} "
            f"s14={vals[0]:.12f} s18={vals[1]:.12f} "
            f"s22={vals[2]:.12f} spread={max(vals) - min(vals):.3e}"
        )
    for beta in [Fraction(40, 1), Fraction(50, 1)]:
        vals = []
        for shell in [22, 26, 30]:
            value = true_ratio_float(shell, beta)
            out[(beta, shell)] = value
            vals.append(value)
        print(
            f"high_beta_stability beta={fmt_beta(beta):>4} "
            f"s22={vals[0]:.12f} s26={vals[1]:.12f} "
            f"s30={vals[2]:.12f} spread={max(vals) - min(vals):.3e}"
        )
    print()
    return out


def print_cert_rows(rows: list[CertificateRow]) -> None:
    print("B_16 EXACT-RATIONAL CERTIFICATE ROWS")
    for row in rows:
        print(
            f"cert beta={fmt_beta(row.beta):>4} states={row.states} "
            f"upper={fmt_dec(row.ratio_upper, 12)} "
            f"block_bound_ratio={fmt_dec(row.block_bound_ratio, 12)} "
            f"tail_ratio={fmt_dec(row.tail_ratio, 12)} "
            f"block_float={row.block_ratio_float:.12f} "
            f"slack_vs_true={row.slack_vs_true:.12f} "
            f"margin={fmt_dec(row.margin, 12)} "
            f"certified={'yes' if row.certified else 'no'}"
        )
    print()


def print_failure_decomposition(failure_true: dict[Fraction, float]) -> None:
    print("RUNG-FOUR FAILURE DECOMPOSITION")
    for beta, upper in RUNG_FOUR_FAILURE_UPPERS.items():
        true_ratio = failure_true[beta]
        failure = float(upper) - 1.0
        slack = float(upper) - true_ratio
        true_growth = true_ratio - 1.0
        print(
            f"r4_failure beta={fmt_beta(beta):>4} "
            f"upper={float(upper):.12f} true_ratio={true_ratio:.12f} "
            f"failure_above_1={failure:.12f} slack={slack:.12f} "
            f"slack_over_failure={slack / failure:.6f} "
            f"true_growth_over_failure={true_growth / failure:.6f}"
        )
    print()


def main() -> int:
    print("Native gauge-transfer gap persistence rung-five bounded runner")
    print(f"certified shell: B_{CERT_SHELL} ({(CERT_SHELL + 1) ** 2} states)")
    print(f"COEFF_ORDER={COEFF_ORDER}, M_ORDER={M_ORDER}, TRUE_MODE_MAX={TRUE_MODE_MAX}")
    print("HS deflation wall: exact trace-square at B_16 was runtime-capped, no HS row claimed")
    print()

    check(
        "exact SU(3) recurrence layers are integer and nonnegative",
        all(isinstance(v, int) and v >= 0 for layer in LAYERS for v in layer.values()),
        f"layers n=0..{COEFF_ORDER}, final states={len(LAYERS[-1])}",
    )

    leading_ok = True
    leading_details: list[str] = []
    for weight in [(1, 0), (0, 1), (1, 1), (2, 0), (4, 4), (7, 0)]:
        for n, layer in enumerate(LAYERS):
            mult = layer.get(weight, 0)
            if mult:
                p, q = weight
                coeff = Fraction(mult, factorial(n) * (6**n))
                expected = Fraction(1, factorial(p) * factorial(q) * (6 ** (p + q)))
                leading_ok = leading_ok and n == p + q and coeff == expected
                leading_details.append(f"{weight}: beta^{n} coeff={coeff}")
                break
    check(
        "leading coefficients reproduce the character recurrence",
        leading_ok,
        "; ".join(leading_details),
    )

    r4_ok, r4_detail = parse_rung_four_reference_rows()
    check("rung-four beta<=22 reference rows reproduce from one-hop note", r4_ok, r4_detail)

    true_trajectory = print_true_trajectory()
    stability = print_stability_rows()

    post_peak = [
        true_trajectory[b]
        for b in [
            Fraction(2, 1),
            Fraction(5, 2),
            Fraction(3, 1),
            Fraction(4, 1),
            Fraction(8, 1),
            Fraction(12, 1),
            Fraction(16, 1),
            Fraction(20, 1),
            Fraction(24, 1),
            Fraction(30, 1),
            Fraction(40, 1),
            Fraction(50, 1),
        ]
    ]
    check(
        "true-ratio trajectory stays bounded well below one on the tested grid",
        max(true_trajectory.values()) < 0.40,
        f"max={max(true_trajectory.values()):.12f}",
    )
    check(
        "true-ratio trajectory is nonincreasing after the beta=2 grid peak",
        all(post_peak[i] >= post_peak[i + 1] - 2.0e-6 for i in range(len(post_peak) - 1)),
        "checked beta in {2,5/2,3,4,8,12,16,20,24,30,40,50}",
    )

    low_spreads = []
    for beta in [Fraction(8, 1), Fraction(22, 1), Fraction(30, 1)]:
        vals = [stability[(beta, shell)] for shell in [14, 18, 22]]
        low_spreads.append(max(vals) - min(vals))
    high_spreads = []
    for beta in [Fraction(40, 1), Fraction(50, 1)]:
        vals = [stability[(beta, shell)] for shell in [22, 26, 30]]
        high_spreads.append(max(vals) - min(vals))
    check(
        "s14/s18/s22 shell-stability holds on the beta<=30 diagnostic rows",
        max(low_spreads) < 1.3e-3,
        f"max spread={max(low_spreads):.3e}",
    )
    check(
        "larger float shells stabilize the beta 40 and 50 diagnostic rows",
        max(high_spreads) < 3.2e-5,
        f"max spread={max(high_spreads):.3e}",
    )

    failure_true = {
        Fraction(45, 2): true_ratio_float(22, Fraction(45, 2)),
        Fraction(23, 1): true_ratio_float(22, Fraction(23, 1)),
    }
    print_failure_decomposition(failure_true)
    check(
        "rung-four stop rows are tail-bound-limited against the measured true ratios",
        all(float(RUNG_FOUR_FAILURE_UPPERS[b]) - failure_true[b] > 1.0 for b in failure_true),
        "slack exceeds the full amount by which the rung-four upper crosses one",
    )

    cache = precompute_shell_path_data(CERT_SHELL, M_ORDER)
    cert_betas = [
        Fraction(22, 1),
        Fraction(24, 1),
        Fraction(26, 1),
        Fraction(27, 1),
        Fraction(30, 1),
    ]
    rows = [certify_beta(beta, cache) for beta in cert_betas]
    print_cert_rows(rows)
    row_by_beta = {row.beta: row for row in rows}

    check(
        "B_16 exact-rational certificate extends past the rung-four beta=22 frontier",
        row_by_beta[Fraction(24, 1)].certified and row_by_beta[Fraction(26, 1)].certified,
        (
            f"beta=24 margin={fmt_dec(row_by_beta[Fraction(24, 1)].margin, 12)}; "
            f"beta=26 margin={fmt_dec(row_by_beta[Fraction(26, 1)].margin, 12)}"
        ),
    )
    check(
        "B_16 checked integer frontier is beta=26 with beta=27 not certified",
        row_by_beta[Fraction(26, 1)].certified and not row_by_beta[Fraction(27, 1)].certified,
        (
            f"beta=26 margin={fmt_dec(row_by_beta[Fraction(26, 1)].margin, 12)}; "
            f"beta=27 margin={fmt_dec(row_by_beta[Fraction(27, 1)].margin, 12)}"
        ),
    )
    check(
        "B_16 beta=30 row reports the tail-bound stop side",
        not row_by_beta[Fraction(30, 1)].certified,
        f"beta=30 slack_vs_true={row_by_beta[Fraction(30, 1)].slack_vs_true:.12f}",
    )
    check(
        "float diagnostics sit inside certified B_16 upper brackets",
        all(
            row.block_ratio_float <= float(row.ratio_upper)
            for row in rows
            if row.certified
        ),
        "checked certified rows beta in {22,24,26}",
    )
    check(
        "B_16 certified-row slack is dominated by certificate tail and block-bound slack, not true-gap growth",
        all(row.block_ratio_float < 0.21 and row.slack_vs_true > 0.40 for row in rows),
        "checked beta in {22,24,26,27,30}",
    )

    witness_ok, witness_detail = finite_outer_box_tail_witness(
        rows, [Fraction(24, 1), Fraction(26, 1)], WITNESS_OUTER_SHELL
    )
    check(
        "B_16 finite outer-box true-operator witness is dominated on certified extension rows",
        witness_ok,
        witness_detail,
    )

    text = note_text()
    required_note_strings = [
        "**Status authority:** independent audit lane only.",
        "No continuum limit",
        "No R^4 construction",
        "true discrete gap shows no sign of closing across the tested beta range",
        "certified frontier is tail-bound-limited",
        "scripts/native_gauge_transfer_gap_persistence_rung_five_bounded_2026_06_12.py",
        "logs/runner-cache/native_gauge_transfer_gap_persistence_rung_five_bounded_2026_06_12.txt",
        "TOTAL: PASS=",
    ]
    check(
        "note contains scope, status-authority, bounded framing, and runner markers",
        all(s in text for s in required_note_strings),
        "checked required note markers",
    )

    required_links = [
        "[RUNG_FOUR_NOTE.md](../.claude/tmp/refs/RUNG_FOUR_NOTE.md)",
        "[rung_four_runner.py](../.claude/tmp/refs/rung_four_runner.py)",
        "[GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)",
        "[GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)",
        "[WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md](WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md)",
    ]
    check(
        "one-hop authorities are present as markdown links",
        all(link in text for link in required_links),
        "checked authority-link forms",
    )

    banned_phrases = [
        " ".join(parts)
        for parts in [
            ("only", "route"),
            ("last", "route"),
            ("exhau", "sted"),
            ("closes", "the", "program"),
        ]
    ]
    check(
        "note avoids overreach phrases banned for this lane",
        not any(phrase in text.lower() for phrase in banned_phrases),
        "scanned banned phrase set",
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
