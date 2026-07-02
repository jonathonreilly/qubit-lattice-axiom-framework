#!/usr/bin/env python3
"""Native gauge-transfer certified gap rung-four bounded runner.

This runner stays on the repo-native SU(3) dominant-weight packet tower.
It extends the rung-three fixed-shell half-slice certificate by replacing
the coarse escape tail with exact path-count leak majorants and by applying
an exact Hilbert-Schmidt deflation bound on the frontier rows.

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
import sympy as sp

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve as src_existing


AUDIT_TIMEOUT_SEC = 600

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_CERTIFIED_GAP_RUNG_FOUR_BOUNDED_NOTE_2026-06-12.md"
)

COEFF_ORDER = 80
M_ORDER = 60
EXP_BOUND_ORDER = 120
CERT_SHELL = 14
STURM_SHELL = 4
STURM_EPS = Fraction(1, 10**8)
SQRT_SCALE = 10**24
MODE_MAX = 280

RUNG_ONE_INTERVAL_BETAS = [
    Fraction(0, 1),
    Fraction(1, 10),
    Fraction(1, 2),
    Fraction(1, 1),
]

RUNG_THREE_SHARED_BETAS = [
    Fraction(1, 1),
    Fraction(2, 1),
    Fraction(3, 1),
    Fraction(4, 1),
    Fraction(117, 25),
    Fraction(5, 1),
    Fraction(6, 1),
    Fraction(7, 1),
    Fraction(8, 1),
    Fraction(9, 1),
]

EXTENSION_BETAS = [
    Fraction(10, 1),
    Fraction(11, 1),
    Fraction(12, 1),
    Fraction(14, 1),
    Fraction(16, 1),
    Fraction(18, 1),
    Fraction(20, 1),
    Fraction(21, 1),
    Fraction(22, 1),
    Fraction(45, 2),
    Fraction(23, 1),
]

CERT_TABLE_BETAS = RUNG_THREE_SHARED_BETAS + EXTENSION_BETAS

# Exact trace-square deflation is deliberately reserved for the frontier
# rows: it is rigorous but much heavier than the trace bracket.
HS_DEFLATION_BETAS = {
    Fraction(22, 1),
}

TAIL_WITNESS_BETAS = [
    Fraction(8, 1),
    Fraction(12, 1),
    Fraction(20, 1),
    Fraction(22, 1),
]

TRUE_OPERATOR_TAIL_WITNESS_BETAS = [
    Fraction(20, 1),
    Fraction(22, 1),
]

TRUE_OPERATOR_TAIL_WITNESS_SHELLS = [
    22,
    26,
]

STURM_BETAS = [
    Fraction(117, 25),
]

RUNG_THREE_UPPER_DECIMAL = {
    Fraction(1, 1): Fraction(425322926818, 10**12),
    Fraction(2, 1): Fraction(903165610450, 10**12),
    Fraction(3, 1): Fraction(932294829833, 10**12),
    Fraction(4, 1): Fraction(771135222181, 10**12),
    Fraction(117, 25): Fraction(685007013613, 10**12),
    Fraction(5, 1): Fraction(654539946383, 10**12),
    Fraction(6, 1): Fraction(598389567827, 10**12),
    Fraction(7, 1): Fraction(610545022422, 10**12),
    Fraction(8, 1): Fraction(729708870782, 10**12),
    Fraction(9, 1): Fraction(1030649803976, 10**12),
}

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class CertificateRow:
    beta: Fraction
    lambda0_lower: Fraction
    block_lambda1_upper: Fraction
    trace_block_lambda1_upper: Fraction
    hs_block_lambda1_upper: Fraction | None
    tail_radius: Fraction
    old_tail_radius: Fraction
    diagonal_tail_radius: Fraction
    escape_radius: Fraction
    sharp_delta2: Fraction
    ratio_upper: Fraction
    old_style_ratio_upper: Fraction
    margin: Fraction
    certified: bool
    block_method: str
    block_ratio_float: float
    t25_ratio_float: float
    improvement_vs_rung_three: Fraction | None


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
CERT_WEIGHTS = weights_box(CERT_SHELL)
CERT_INDEX = {w: i for i, w in enumerate(CERT_WEIGHTS)}


def precompute_half_slice_path_data(
    shell: int, order: int
) -> tuple[list[list[list[tuple[int, int]]]], list[list[int]]]:
    weights = weights_box(shell)
    index = {w: i for i, w in enumerate(weights)}
    inblock_layers: list[list[list[tuple[int, int]]]] = []
    outside_counts: list[list[int]] = []
    for start_weight in weights:
        layer: dict[tuple[int, int], int] = {start_weight: 1}
        start_inblock: list[list[tuple[int, int]]] = []
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
            start_inblock.append(entries)
            start_outside.append(outside_total)
            nxt: dict[tuple[int, int], int] = defaultdict(int)
            for weight, mult in layer.items():
                for nb in recurrence_neighbors(*weight):
                    nxt[nb] += mult
            layer = dict(nxt)
        inblock_layers.append(start_inblock)
        outside_counts.append(start_outside)
    return inblock_layers, outside_counts


CERT_INBLOCK_LAYERS, CERT_OUTSIDE_COUNTS = precompute_half_slice_path_data(
    CERT_SHELL, M_ORDER
)


def exp_tail_after(x: Fraction, order: int) -> Fraction:
    first = (x ** (order + 1)) / factorial(order + 1)
    ratio = x / Fraction(order + 2, 1)
    if ratio >= 1:
        raise ValueError("geometric exponential tail bound needs x < order + 2")
    return first / (1 - ratio)


def exp_sum_upper(x: Fraction) -> Fraction:
    total = Fraction(0, 1)
    term = Fraction(1, 1)
    for n in range(EXP_BOUND_ORDER + 1):
        if n == 0:
            term = Fraction(1, 1)
        elif n == 1:
            term = x
        elif n > 1:
            term *= x / n
        total += term
    return total + exp_tail_after(x, EXP_BOUND_ORDER)


def exp_tail_from(x: Fraction, start: int) -> Fraction:
    total = Fraction(0, 1)
    term = Fraction(1, 1)
    for n in range(EXP_BOUND_ORDER + 1):
        if n == 0:
            term = Fraction(1, 1)
        elif n == 1:
            term = x
        else:
            term *= x / n
        if n >= start:
            total += term
    return total + exp_tail_after(x, EXP_BOUND_ORDER)


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
    coeffs: dict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for n, layer in enumerate(LAYERS):
        factor = (beta**n) / (factorial(n) * (6**n))
        for weight, mult in layer.items():
            coeffs[weight] += mult * factor
    return dict(coeffs)


def ratio_interval_for_weight(
    beta: Fraction, weight: tuple[int, int]
) -> tuple[Fraction, Fraction]:
    coeffs = coefficient_partials(beta)
    c00_lower = coeffs[(0, 0)]
    c00_upper = c00_lower + exp_tail_after(beta, COEFF_ORDER)
    partial = coeffs.get(weight, Fraction(0, 1))
    p, q = weight
    return (
        partial / c00_upper,
        (partial + exp_tail_after(beta, COEFF_ORDER) / dim_su3(p, q))
        / c00_lower,
    )


def ratio_bounds_for_shell(
    beta: Fraction, shell: int
) -> tuple[list[Fraction], list[Fraction], Fraction, Fraction]:
    weights = weights_box(shell)
    coeffs = coefficient_partials(beta)
    c00_lower = coeffs[(0, 0)]
    c00_upper = c00_lower + exp_tail_after(beta, COEFF_ORDER)
    tail = exp_tail_after(beta, COEFF_ORDER)

    lower: list[Fraction] = []
    upper: list[Fraction] = []
    for weight in weights:
        p, q = weight
        partial = coeffs.get(weight, Fraction(0, 1))
        lower.append(partial / c00_upper)
        upper.append((partial + tail / dim_su3(p, q)) / c00_lower)

    tail_sup = Fraction(0, 1)
    for weight, partial in coeffs.items():
        p, q = weight
        if p > shell or q > shell:
            row_upper = (partial + tail / dim_su3(p, q)) / c00_lower
            if row_upper > tail_sup:
                tail_sup = row_upper

    far_dim_min = (COEFF_ORDER + 2) * (COEFF_ORDER + 3) // 2
    far_tail = (tail / far_dim_min) / c00_lower
    tail_sup = max(tail_sup, far_tail)

    return lower, upper, tail_sup, max(upper)


def half_slice_matrix_partial(beta: Fraction, shell: int) -> list[list[Fraction]]:
    if shell == CERT_SHELL:
        weights = CERT_WEIGHTS
        path_layers = CERT_INBLOCK_LAYERS
    else:
        weights = weights_box(shell)
        path_layers, _outside = precompute_half_slice_path_data(shell, M_ORDER)
    size = len(weights)
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
    for col, by_n in enumerate(path_layers):
        for n, entries in enumerate(by_n):
            f = factors[n]
            for row, mult in entries:
                matrix[row][col] += mult * f
    return matrix


def matvec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    out: list[Fraction] = []
    for row in matrix:
        total = Fraction(0, 1)
        for a, b in zip(row, vector):
            total += a * b
        out.append(total)
    return out


def rayleigh_lower(
    matrix: list[list[Fraction]], r_lower: list[Fraction], vector: np.ndarray
) -> Fraction:
    scale = 10**12
    if float(np.sum(vector)) < 0.0:
        vector = -vector
    v = [
        Fraction(max(float(x), 1.0e-30)).limit_denominator(scale)
        for x in vector
    ]
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


def trace_square_upper(
    matrix: list[list[Fraction]], r_upper: list[Fraction], m_tail: Fraction
) -> Fraction:
    """Exact rational upper bound for tr((P T_beta P)^2).

    All entries of M_beta and D_beta are nonnegative in this packet basis.
    Replacing each M entry by partial + m_tail and each diagonal ratio by
    r_upper gives an entrywise majorant U for the finite block, hence
    tr(A^2) = sum_ij A_ij^2 <= sum_ij U_ij^2.
    """
    total = Fraction(0, 1)
    size = len(matrix)
    for i in range(size):
        row_i = matrix[i]
        for j in range(i, size):
            row_j = matrix[j]
            entry = Fraction(0, 1)
            for k in range(size):
                entry += (row_i[k] + m_tail) * r_upper[k] * (row_j[k] + m_tail)
            sq = entry * entry
            if i == j:
                total += sq
            else:
                total += 2 * sq
    return total


def float_block_spectrum(
    matrix: list[list[Fraction]], r_mid: list[Fraction]
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    m = np.array([[float(x) for x in row] for row in matrix], dtype=float)
    r = np.array([float(x) for x in r_mid], dtype=float)
    transfer = m @ np.diag(r) @ m
    eigvals, eigvecs = np.linalg.eigh(transfer)
    return eigvals, eigvecs, transfer


def old_escape_delta2(
    beta: Fraction, shell: int, r_upper: list[Fraction]
) -> Fraction:
    weights = weights_box(shell)
    tau = beta / 2
    delta2 = Fraction(0, 1)
    tail_cache: dict[int, Fraction] = {}
    for k, (p, q) in enumerate(weights):
        distance = min(shell - p, shell - q) + 1
        if distance not in tail_cache:
            tail_cache[distance] = exp_tail_from(tau, distance)
        e = tail_cache[distance]
        delta2 += r_upper[k] * e * e
    return delta2


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


def sharp_delta2(beta: Fraction, r_upper: list[Fraction]) -> Fraction:
    p_to_q = sum(
        r_upper[k] * leak_l1_upper_from_counts(beta, CERT_OUTSIDE_COUNTS[k]) ** 2
        for k in range(len(CERT_WEIGHTS))
    )
    q_rows = exp_sum_upper(beta) * outside_ratio_mass_upper(beta, CERT_SHELL)
    return p_to_q + q_rows


def escape_radius_from_delta2(
    beta: Fraction, r_sup: Fraction, delta2: Fraction
) -> Fraction:
    exp_tau = exp_sum_upper(beta / 2)
    delta = sqrt_upper(delta2)
    return 2 * exp_tau * sqrt_upper(r_sup) * delta + delta2


def t25_ratio_float(beta: Fraction) -> float:
    beta_f = float(beta)
    shell = 4
    weights = weights_box(shell)
    coeffs = np.array(
        [
            src_existing.wilson_character_coefficient(p, q, MODE_MAX, beta_f / 3.0)
            for p, q in weights
        ],
        dtype=float,
    )
    index = {w: i for i, w in enumerate(weights)}
    ratios = coeffs / coeffs[index[(0, 0)]]
    j_op, _weights, _index = src_existing.build_J(shell)
    multiplier = src_existing.matrix_exp_symmetric(j_op, beta_f / 2.0)
    transfer = multiplier @ np.diag(ratios) @ multiplier
    eigvals = np.linalg.eigvalsh(transfer)
    eigvals.sort()
    return float(eigvals[-2] / eigvals[-1])


def certify_beta(beta: Fraction) -> CertificateRow:
    r_lower, r_upper, tail_sup, r_sup = ratio_bounds_for_shell(beta, CERT_SHELL)
    matrix = half_slice_matrix_partial(beta, CERT_SHELL)
    m_tail = exp_tail_after(beta / 2, M_ORDER)
    r_mid = [(lo + hi) / 2 for lo, hi in zip(r_lower, r_upper)]
    eigvals, eigvecs, _transfer = float_block_spectrum(matrix, r_mid)
    lambda0_lower = rayleigh_lower(matrix, r_lower, eigvecs[:, -1])

    trace_hi = trace_upper(matrix, r_upper, m_tail)
    trace_block = trace_hi - lambda0_lower
    block_bound = trace_block
    hs_bound: Fraction | None = None
    block_method = "trace"
    if beta in HS_DEFLATION_BETAS:
        trace2_hi = trace_square_upper(matrix, r_upper, m_tail)
        rem = trace2_hi - lambda0_lower * lambda0_lower
        if rem < 0:
            rem = Fraction(0, 1)
        hs_bound = sqrt_upper(rem)
        # sqrt_upper rounds UP and lambda0_lower is an exact Rayleigh lower bound on the symmetric PSD block, so hs_bound >= true lambda_1 (correct majorant direction)
        if hs_bound < block_bound:
            block_bound = hs_bound
            block_method = "hs-deflation"

    old_delta2 = old_escape_delta2(beta, CERT_SHELL, r_upper)
    old_escape = escape_radius_from_delta2(beta, r_sup, old_delta2)
    diag_tail = exp_sum_upper(beta) * tail_sup
    old_tail_radius = old_escape + diag_tail

    d2 = sharp_delta2(beta, r_upper)
    escape = escape_radius_from_delta2(beta, r_sup, d2)
    tail_radius = escape + diag_tail
    ratio_upper = (block_bound + tail_radius) / lambda0_lower
    old_style_ratio = (trace_block + old_tail_radius) / lambda0_lower
    margin = Fraction(1, 1) - ratio_upper
    rung_three_old = RUNG_THREE_UPPER_DECIMAL.get(beta)
    improvement = None
    if rung_three_old is not None:
        improvement = rung_three_old - ratio_upper

    return CertificateRow(
        beta=beta,
        lambda0_lower=lambda0_lower,
        block_lambda1_upper=block_bound,
        trace_block_lambda1_upper=trace_block,
        hs_block_lambda1_upper=hs_bound,
        tail_radius=tail_radius,
        old_tail_radius=old_tail_radius,
        diagonal_tail_radius=diag_tail,
        escape_radius=escape,
        sharp_delta2=d2,
        ratio_upper=ratio_upper,
        old_style_ratio_upper=old_style_ratio,
        margin=margin,
        certified=margin > 0,
        block_method=block_method,
        block_ratio_float=float(eigvals[-2] / eigvals[-1]),
        t25_ratio_float=t25_ratio_float(beta),
        improvement_vs_rung_three=improvement,
    )


def sturm_interval_check_s4(beta: Fraction) -> tuple[bool, str]:
    r_lower, r_upper, _tail_sup, _r_sup = ratio_bounds_for_shell(beta, STURM_SHELL)
    matrix = half_slice_matrix_partial(beta, STURM_SHELL)
    r_mid = [(lo + hi) / 2 for lo, hi in zip(r_lower, r_upper)]
    eigvals, _eigvecs, transfer_float = float_block_spectrum(matrix, r_mid)
    rational_transfer: list[list[sp.Rational]] = []
    size = len(matrix)
    for i in range(size):
        row: list[sp.Rational] = []
        for j in range(size):
            entry = Fraction(0, 1)
            for k in range(size):
                entry += matrix[i][k] * r_mid[k] * matrix[k][j]
            row.append(sp.Rational(entry.numerator, entry.denominator))
        rational_transfer.append(row)
    mat = sp.Matrix(rational_transfer)
    poly = mat.charpoly().as_poly()
    intervals = poly.intervals(
        eps=sp.Rational(STURM_EPS.numerator, STURM_EPS.denominator)
    )
    if len(intervals) != size:
        return False, f"beta={fmt_beta(beta)} interval_count={len(intervals)} size={size}"
    sorted_float = sorted(float(x) for x in eigvals)
    for value, interval in zip(sorted_float, intervals):
        (lo, hi), multiplicity = interval
        if multiplicity != 1:
            return False, f"beta={fmt_beta(beta)} non-simple interval multiplicity={multiplicity}"
        lo_f = float(lo)
        hi_f = float(hi)
        if not (lo_f - 1.0e-7 <= value <= hi_f + 1.0e-7):
            return False, (
                f"beta={fmt_beta(beta)} float={value:.12e} "
                f"outside [{lo_f:.12e},{hi_f:.12e}]"
            )
    asym = float(np.max(np.abs(transfer_float - transfer_float.T)))
    if asym > 1.0e-10:
        return False, f"beta={fmt_beta(beta)} float transfer asymmetry={asym:.3e}"
    return True, f"beta={fmt_beta(beta)} checked {size} Sturm intervals on B_4"


def s14_float_lambda1_below_exact_deflation_check(
    rows: list[CertificateRow],
) -> tuple[bool, str]:
    """Check the s=14 float lambda_1 sits inside the certified HS window.

    This is not a characteristic-polynomial Sturm isolation for all 225 roots.
    It is the runner's bounded frontier cross-check: on each HS row, the float
    lambda_1 is below the exact rational Hilbert-Schmidt deflation upper.
    """
    failures: list[str] = []
    checked = 0
    for row in rows:
        if row.hs_block_lambda1_upper is None:
            continue
        checked += 1
        float_l1_upper = row.block_ratio_float * float(row.lambda0_lower)
        if not float_l1_upper <= float(row.hs_block_lambda1_upper) * (1.0 + 1.0e-10):
            failures.append(f"beta={fmt_beta(row.beta)} float lambda1 exceeds HS bracket")
    if failures:
        return False, "; ".join(failures)
    return True, f"checked {checked} s=14 HS deflation intervals against float lambda_1"


def finite_outer_box_tail_witness(
    rows: list[CertificateRow], shells: list[int], betas: list[Fraction]
) -> tuple[bool, str]:
    row_by_beta = {row.beta: row for row in rows}
    missing = [fmt_beta(beta) for beta in betas if beta not in row_by_beta]
    if missing:
        return False, f"missing certified rows for beta in {{{', '.join(missing)}}}"

    failures: list[str] = []
    min_op_factor = float("inf")
    min_fro_factor = float("inf")
    beta22_s26_op = None
    beta22_s26_factor = None
    beta22_s26_tail = None

    for shell in shells:
        j_op, weights, index = src_existing.build_J(shell)
        p_indices = np.array(
            [
                idx
                for idx, (p, q) in enumerate(weights)
                if p <= CERT_SHELL and q <= CERT_SHELL
            ],
            dtype=int,
        )
        for beta in betas:
            tail_radius = float(row_by_beta[beta].tail_radius)
            multiplier = src_existing.matrix_exp_symmetric(j_op, float(beta) / 2.0)
            coeffs = np.array(
                [
                    src_existing.wilson_character_coefficient(
                        p, q, MODE_MAX, float(beta) / 3.0
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

            op_ok = tail_radius >= diff_norm
            fro_ok = tail_radius >= fro_norm
            if not (op_ok and fro_ok):
                failures.append(
                    f"S={shell}, beta={fmt_beta(beta)} tail_radius={tail_radius:.12e} "
                    f"true_op_tail={diff_norm:.12e} true_weighted_fro={fro_norm:.12e}"
                )
            if diff_norm > 0.0:
                min_op_factor = min(min_op_factor, tail_radius / diff_norm)
            if fro_norm > 0.0:
                min_fro_factor = min(min_fro_factor, tail_radius / fro_norm)
            if beta == Fraction(22, 1) and shell == 26:
                beta22_s26_op = diff_norm
                beta22_s26_factor = tail_radius / diff_norm if diff_norm > 0.0 else float("inf")
                beta22_s26_tail = tail_radius

    if failures:
        return False, "; ".join(failures)
    detail = (
        f"finite outer boxes S in {{{', '.join(str(s) for s in shells)}}}, "
        f"beta in {{{', '.join(fmt_beta(b) for b in betas)}}}; "
        f"min tail/true_op_tail={min_op_factor:.6f}, "
        f"min tail/weighted_fro={min_fro_factor:.6f}"
    )
    if beta22_s26_op is not None and beta22_s26_factor is not None and beta22_s26_tail is not None:
        detail += (
            f"; beta=22 S=26 true_op_tail={beta22_s26_op:.12e}, "
            f"tail_radius={beta22_s26_tail:.12e}, factor={beta22_s26_factor:.6f}"
        )
    return True, detail


def rung_one_checks() -> tuple[bool, str]:
    failures: list[str] = []
    for beta in RUNG_ONE_INTERVAL_BETAS:
        _lo, hi = ratio_interval_for_weight(beta, (1, 0))
        if hi > Fraction(2, 3):
            failures.append(f"beta={fmt_beta(beta)} fundamental ratio upper={fmt_dec(hi)}")
    return (not failures), "; ".join(failures) if failures else "beta in {0,1/10,1/2,1} <= 2/3"


def analytic_tail_sharpening_check(betas: list[Fraction]) -> tuple[bool, str]:
    failures: list[str] = []
    for beta in betas:
        _r_lower, r_upper, _tail_sup, _r_sup = ratio_bounds_for_shell(
            beta, CERT_SHELL
        )
        old_d2 = old_escape_delta2(beta, CERT_SHELL, r_upper)
        new_d2 = sharp_delta2(beta, r_upper)
        if new_d2 > old_d2:
            failures.append(f"beta={fmt_beta(beta)} new delta2 exceeds old delta2")
    if failures:
        return False, "; ".join(failures)
    return True, "exact path-count delta2 is <= rung-three scalar delta2 on witness rows"


def note_text() -> str:
    return NOTE_PATH.read_text(encoding="utf-8")


def table_line(row: CertificateRow) -> str:
    old = "n/a"
    if row.improvement_vs_rung_three is not None:
        old = fmt_dec(row.improvement_vs_rung_three, 12)
    return (
        f"beta={fmt_beta(row.beta):>5} | "
        f"upper={fmt_dec(row.ratio_upper, 12)} | "
        f"tail_radius={fmt_dec(row.tail_radius, 12)} | "
        f"margin={fmt_dec(row.margin, 12)} | "
        f"certified={'yes' if row.certified else 'no'} | "
        f"block={row.block_method} | "
        f"improvement_vs_r3={old} | "
        f"block_float={row.block_ratio_float:.12f} | "
        f"T25_float={row.t25_ratio_float:.12f}"
    )


def main() -> int:
    print("Native gauge-transfer certified gap rung-four bounded runner")
    print(f"certified packet shell: 0<=p,q<={CERT_SHELL} ({(CERT_SHELL + 1) ** 2} states)")
    print(f"COEFF_ORDER={COEFF_ORDER}, M_ORDER={M_ORDER}, MODE_MAX={MODE_MAX}")
    print(f"HS deflation betas: {', '.join(fmt_beta(b) for b in sorted(HS_DEFLATION_BETAS))}")
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
        "leading coefficients reproduce rung-one/rung-two character recurrence",
        leading_ok,
        "; ".join(leading_details),
    )

    rung_one_ok, rung_one_detail = rung_one_checks()
    check(
        "rung-one [0,1] coefficient-ratio checks reproduce the 2/3 bound",
        rung_one_ok,
        rung_one_detail,
    )

    rows: list[CertificateRow] = []
    for beta in CERT_TABLE_BETAS:
        row = certify_beta(beta)
        rows.append(row)
        print(table_line(row))
        sys.stdout.flush()
    print()

    shared_cert_rows = [row for row in rows if row.beta in RUNG_THREE_SHARED_BETAS and row.beta <= 8]
    check(
        "rung-three certified rows beta<=8 still certify under rung-four tail machinery",
        all(row.certified for row in shared_cert_rows),
        "checked beta in {1,2,3,4,117/25,5,6,7,8}",
    )

    shared_improvement_rows = [
        row for row in rows if row.improvement_vs_rung_three is not None
    ]
    check(
        "shared rows do not exceed rung-three printed upper bounds",
        all(row.improvement_vs_rung_three is not None and row.improvement_vs_rung_three >= 0 for row in shared_improvement_rows),
        "compared against rung-three deliverable table decimals",
    )

    beta_22 = next(row for row in rows if row.beta == 22)
    beta_mid = next(row for row in rows if row.beta == Fraction(45, 2))
    beta_23 = next(row for row in rows if row.beta == 23)
    check(
        "integer frontier advances past beta=8 and certifies beta=22",
        beta_22.certified and beta_22.block_method == "hs-deflation",
        f"beta=22 margin={fmt_dec(beta_22.margin, 12)}",
    )
    check(
        "bisection probe at beta=45/2 reports the fixed-shell stop side",
        not beta_mid.certified,
        f"beta=45/2 margin={fmt_dec(beta_mid.margin, 12)}",
    )
    check(
        "next integer probe beta=23 is not certified by this fixed-shell bound",
        not beta_23.certified,
        f"beta=23 margin={fmt_dec(beta_23.margin, 12)}",
    )

    beta_21 = next(row for row in rows if row.beta == 21)
    beta_22_trace_sharp = (
        beta_22.trace_block_lambda1_upper + beta_22.tail_radius
    ) / beta_22.lambda0_lower
    check(
        "old trace bracket plus sharp tail stops before beta=22",
        beta_21.certified and beta_22_trace_sharp > 1,
        (
            f"beta=21 trace+sharp margin={fmt_dec(beta_21.margin, 12)}; "
            f"beta=22 trace+sharp upper={fmt_dec(beta_22_trace_sharp, 12)}"
        ),
    )

    tail_sharp_ok, tail_sharp_detail = analytic_tail_sharpening_check(
        TAIL_WITNESS_BETAS
    )
    check(
        "path-count tail majorant is no larger than rung-three scalar tail on witnesses",
        tail_sharp_ok,
        tail_sharp_detail,
    )

    finite_witness_ok, finite_witness_detail = finite_outer_box_tail_witness(
        rows, TRUE_OPERATOR_TAIL_WITNESS_SHELLS, TRUE_OPERATOR_TAIL_WITNESS_BETAS
    )
    check(
        "finite outer-box true-operator tail witness is dominated by rung-four tail radius",
        finite_witness_ok,
        finite_witness_detail,
    )

    sturm_results = [sturm_interval_check_s4(beta) for beta in STURM_BETAS]
    check(
        "exact characteristic-polynomial Sturm brackets still contain every float eigenvalue on the B_4 check block",
        all(ok for ok, _detail in sturm_results),
        "; ".join(detail for _ok, detail in sturm_results),
    )

    s14_ok, s14_detail = s14_float_lambda1_below_exact_deflation_check(rows)
    check(
        "s=14 block float lambda_1 lies inside the exact deflation intervals on HS rows",
        s14_ok,
        s14_detail,
    )

    check(
        "T25 float diagnostics sit below certified full-operator uppers on certified rows",
        all(row.t25_ratio_float <= float(row.ratio_upper) for row in rows if row.certified),
        "compared T25 float ratios against certified full upper rows",
    )

    text = note_text()
    required_note_strings = [
        "**Claim type:** bounded_theorem",
        "**Status authority:** independent audit lane only.",
        "No continuum limit",
        "No R^4 construction",
        "beta = 22",
        "beta = 23",
        "Hilbert-Schmidt deflation",
        "path-count tail",
        "Tail Witness",
        "scripts/native_gauge_transfer_certified_gap_rung_four_bounded_2026_06_12.py",
        "logs/runner-cache/native_gauge_transfer_certified_gap_rung_four_bounded_2026_06_12.txt",
        "No branch-local scratch note or scratch runner is a source authority",
        "TOTAL: PASS=",
    ]
    check(
        "note contains scope, status-authority, table, frontier, and runner markers",
        all(s in text for s in required_note_strings),
        "checked required note markers",
    )

    required_links = [
        "[GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)",
        "[GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)",
        "[WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md](WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md)",
    ]
    check(
        "one-hop authorities are present as markdown links",
        all(link in text for link in required_links),
        "checked authority-link forms",
    )

    check(
        "note keeps scratch rung-three refs out of the dependency graph",
        ".claude/tmp" not in text and "RUNG_THREE_NOTE.md" not in text and "rung_three_runner.py" not in text,
        "scanned for branch-local scratch authority refs",
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
