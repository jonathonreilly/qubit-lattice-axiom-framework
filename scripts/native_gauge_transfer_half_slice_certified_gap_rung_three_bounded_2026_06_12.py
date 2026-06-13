#!/usr/bin/env python3
"""Native gauge-transfer half-slice certified gap rung-three runner.

This runner stays inside the repo-native SU(3) dominant-weight packet tower.
It certifies bounded spectral-ratio rows for the half-slice transfer

    T_beta = exp((beta/2) J) D_beta exp((beta/2) J),

where J is the exact six-neighbor character recurrence and D_beta is the
one-link Wilson coefficient-ratio diagonal inherited from rungs one/two.

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
    / "NATIVE_GAUGE_TRANSFER_HALF_SLICE_CERTIFIED_GAP_RUNG_THREE_BOUNDED_NOTE_2026-06-12.md"
)

COEFF_ORDER = 80
M_ORDER = 60
EXP_BOUND_ORDER = 120
CERT_SHELL = 14
STURM_SHELL = 4
STURM_EPS = Fraction(1, 10**8)
SQRT_SCALE = 10**24
MODE_MAX = 240

REQUESTED_GRID_BETAS = [
    Fraction(1, 1),
    Fraction(2, 1),
    Fraction(3, 1),
    Fraction(4, 1),
    Fraction(117, 25),
    Fraction(5, 1),
    Fraction(6, 1),
    Fraction(7, 1),
    Fraction(8, 1),
]

FRONTIER_PROBE_BETAS = [
    Fraction(9, 1),
]

CERT_TABLE_BETAS = REQUESTED_GRID_BETAS + FRONTIER_PROBE_BETAS
STURM_BETAS = [
    Fraction(117, 25),
]
TAIL_WITNESS_BETAS = [
    Fraction(1, 1),
    Fraction(2, 1),
    Fraction(4, 1),
    Fraction(8, 1),
]
TAIL_WITNESS_SHELLS = [22, 30]

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class CertificateRow:
    beta: Fraction
    lambda0_lower: Fraction
    block_lambda1_upper: Fraction
    tail_radius: Fraction
    diagonal_tail_radius: Fraction
    escape_radius: Fraction
    ratio_upper: Fraction
    margin: Fraction
    certified: bool
    block_ratio_float: float
    t25_ratio_float: float
    trace_bound_ratio: Fraction
    tail_sup: Fraction


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
    weights = weights_box(shell)
    index = {w: i for i, w in enumerate(weights)}
    size = len(weights)
    tau = beta / 2
    matrix = [[Fraction(0, 1) for _ in range(size)] for _ in range(size)]
    for col, start_weight in enumerate(weights):
        layer: dict[tuple[int, int], int] = {start_weight: 1}
        factor = Fraction(1, 1)
        for n in range(M_ORDER + 1):
            if n == 0:
                factor = Fraction(1, 1)
            elif n == 1:
                factor = tau / 6
            else:
                factor *= tau / (6 * n)
            for weight, mult in layer.items():
                row = index.get(weight)
                if row is not None:
                    matrix[row][col] += mult * factor
            nxt: dict[tuple[int, int], int] = defaultdict(int)
            for weight, mult in layer.items():
                for nb in recurrence_neighbors(*weight):
                    nxt[nb] += mult
            layer = dict(nxt)
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


def float_block_spectrum(
    matrix: list[list[Fraction]], r_mid: list[Fraction]
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    m = np.array([[float(x) for x in row] for row in matrix], dtype=float)
    r = np.array([float(x) for x in r_mid], dtype=float)
    transfer = m @ np.diag(r) @ m
    eigvals, eigvecs = np.linalg.eigh(transfer)
    return eigvals, eigvecs, transfer


def escape_delta2(beta: Fraction, shell: int, r_upper: list[Fraction]) -> Fraction:
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


def escape_radius(
    beta: Fraction,
    shell: int,
    r_upper: list[Fraction],
    r_sup: Fraction,
) -> Fraction:
    tau = beta / 2
    exp_tau = exp_sum_upper(tau)
    delta2 = escape_delta2(beta, shell, r_upper)
    delta = sqrt_upper(delta2)
    return 2 * exp_tau * sqrt_upper(r_sup) * delta + delta2


def outside_escape_counts(shell: int) -> list[list[int]]:
    """Exact n-hop path counts from each P label to rows outside P.

    The escape proof uses these counts to expose the factors that
    exp_tail_from intentionally drops: each n-hop matrix term carries
    1/(6^n n!), while the no-denominator tail keeps tau^n/n! after
    replacing the path count by the crude six-neighbor maximum 6^n.
    """
    counts: list[list[int]] = []
    for start_weight in weights_box(shell):
        layer: dict[tuple[int, int], int] = {start_weight: 1}
        start_counts: list[int] = []
        for _n in range(M_ORDER + 1):
            start_counts.append(
                sum(mult for (p, q), mult in layer.items() if p > shell or q > shell)
            )
            nxt: dict[tuple[int, int], int] = defaultdict(int)
            for weight, mult in layer.items():
                for nb in recurrence_neighbors(*weight):
                    nxt[nb] += mult
            layer = dict(nxt)
        counts.append(start_counts)
    return counts


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


def outside_ratio_mass_upper(beta: Fraction, shell: int) -> Fraction:
    coeffs = coefficient_partials(beta)
    c00_lower = coeffs[(0, 0)]
    outside_partial = sum(
        partial for (p, q), partial in coeffs.items() if p > shell or q > shell
    )
    # The omitted coefficient tail is bounded by the full scalar exponential
    # tail because sum_lambda m_lambda^(n) <= 6^n follows from the
    # dimension-weighted identity sum_lambda m_lambda^(n) d_lambda = 6^n.
    return (outside_partial + exp_tail_after(beta, COEFF_ORDER)) / c00_lower


def analytic_tail_dominance_check(betas: list[Fraction]) -> tuple[bool, str]:
    weights = weights_box(CERT_SHELL)
    escape_counts = outside_escape_counts(CERT_SHELL)
    failures: list[str] = []
    for beta in betas:
        _r_lower, r_upper, _tail_sup, _r_sup = ratio_bounds_for_shell(
            beta, CERT_SHELL
        )
        delta2 = escape_delta2(beta, CERT_SHELL, r_upper)
        p_to_q = sum(
            r_upper[k] * leak_l1_upper_from_counts(beta, escape_counts[k]) ** 2
            for k in range(len(weights))
        )
        q_rows = exp_sum_upper(beta) * outside_ratio_mass_upper(beta, CERT_SHELL)
        if p_to_q + q_rows > delta2:
            failures.append(
                f"beta={fmt_beta(beta)} delta2 failed exact P/Q dominance"
            )
    if failures:
        return False, "; ".join(failures)
    return (
        True,
        "exact rational delta2 dominance checked on table betas; includes P-Q and row-weighted Q rows",
    )


def finite_outer_box_tail_witness(
    shells: list[int], betas: list[Fraction]
) -> tuple[bool, str]:
    failures: list[str] = []
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

            _r_lower, r_upper, _tail_sup, r_sup = ratio_bounds_for_shell(
                beta, CERT_SHELL
            )
            escape = float(escape_radius(beta, CERT_SHELL, r_upper, r_sup))
            if not (escape >= diff_norm and escape >= fro_norm):
                failures.append(
                    f"S={shell}, beta={fmt_beta(beta)} finite witness breached"
                )
    if failures:
        return False, "; ".join(failures)
    return (
        True,
        "finite outer boxes S in {22,30}, beta in {1,2,4,8}; includes QMQ and row-r Frobenius terms",
    )


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
    block_lambda1_upper = trace_hi - lambda0_lower
    esc = escape_radius(beta, CERT_SHELL, r_upper, r_sup)
    diag_tail = exp_sum_upper(beta) * tail_sup
    tail_radius = esc + diag_tail
    ratio_upper = (block_lambda1_upper + tail_radius) / lambda0_lower
    margin = Fraction(1, 1) - ratio_upper
    return CertificateRow(
        beta=beta,
        lambda0_lower=lambda0_lower,
        block_lambda1_upper=block_lambda1_upper,
        tail_radius=tail_radius,
        diagonal_tail_radius=diag_tail,
        escape_radius=esc,
        ratio_upper=ratio_upper,
        margin=margin,
        certified=margin > 0,
        block_ratio_float=float(eigvals[-2] / eigvals[-1]),
        t25_ratio_float=t25_ratio_float(beta),
        trace_bound_ratio=block_lambda1_upper / lambda0_lower,
        tail_sup=tail_sup,
    )


def sturm_interval_check(beta: Fraction) -> tuple[bool, str]:
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
    intervals = poly.intervals(eps=sp.Rational(STURM_EPS.numerator, STURM_EPS.denominator))
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
    return True, f"beta={fmt_beta(beta)} checked {size} Sturm intervals"


def note_text() -> str:
    return NOTE_PATH.read_text(encoding="utf-8")


def table_line(row: CertificateRow) -> str:
    return (
        f"beta={fmt_beta(row.beta):>5} | "
        f"upper={fmt_dec(row.ratio_upper, 12)} | "
        f"tail_radius={fmt_dec(row.tail_radius, 12)} | "
        f"margin={fmt_dec(row.margin, 12)} | "
        f"certified={'yes' if row.certified else 'no'} | "
        f"block_float={row.block_ratio_float:.12f} | "
        f"T25_float={row.t25_ratio_float:.12f}"
    )


def main() -> int:
    print("Native gauge-transfer half-slice certified gap rung-three bounded runner")
    print(f"certified packet shell: 0<=p,q<={CERT_SHELL} ({(CERT_SHELL + 1) ** 2} states)")
    print(f"Sturm packet shell: 0<=p,q<={STURM_SHELL} ({(STURM_SHELL + 1) ** 2} states)")
    print(f"COEFF_ORDER={COEFF_ORDER}, M_ORDER={M_ORDER}, MODE_MAX={MODE_MAX}")
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

    rows = []
    for beta in CERT_TABLE_BETAS:
        row = certify_beta(beta)
        rows.append(row)
        print(table_line(row))
        sys.stdout.flush()
    print()

    grid_rows = [row for row in rows if row.beta in REQUESTED_GRID_BETAS]
    check(
        "requested beta grid is certified by the full half-slice bound",
        all(row.certified for row in grid_rows),
        "checked beta in {1,2,3,4,117/25,5,6,7,8}",
    )

    frontier_yes = Fraction(8, 1)
    frontier_no = Fraction(9, 1)
    yes_row = next(row for row in rows if row.beta == frontier_yes)
    no_row = next(row for row in rows if row.beta == frontier_no)
    check(
        "next probe after the requested grid reports the fixed-shell stop mechanism",
        yes_row.certified and not no_row.certified,
        (
            f"beta=8 margin={fmt_dec(yes_row.margin, 12)}; "
            f"beta=9 margin={fmt_dec(no_row.margin, 12)}"
        ),
    )

    rung_one_rows = [row for row in rows if row.beta == 1]
    check(
        "beta=1 endpoint stays inside the rung-one 2/3 ratio interval",
        rung_one_rows[0].ratio_upper <= Fraction(2, 3),
        (
            f"beta=1 full half-slice upper={fmt_dec(rung_one_rows[0].ratio_upper, 12)}; "
            "threshold=2/3"
        ),
    )

    tail_dominance_ok, tail_dominance_detail = analytic_tail_dominance_check(
        CERT_TABLE_BETAS
    )
    check(
        "exact delta2 dominance covers the infinite-tail Frobenius proof terms",
        tail_dominance_ok,
        tail_dominance_detail,
    )

    finite_witness_ok, finite_witness_detail = finite_outer_box_tail_witness(
        TAIL_WITNESS_SHELLS, TAIL_WITNESS_BETAS
    )
    check(
        "outer-box witness checks escape radius against full finite-emulation tails",
        finite_witness_ok,
        finite_witness_detail,
    )

    sturm_results = [sturm_interval_check(beta) for beta in STURM_BETAS]
    check(
        "exact characteristic-polynomial Sturm brackets contain every float eigenvalue on the 25-state check block",
        all(ok for ok, _detail in sturm_results),
        "; ".join(detail for _ok, detail in sturm_results),
    )

    check(
        "rung-two T25 float diagnostics sit below the new full-operator certified uppers",
        all(row.t25_ratio_float <= float(row.ratio_upper) for row in grid_rows),
        "compared requested-grid T25 float ratios against certified full upper rows",
    )

    tail_order_ok = all(
        row.tail_radius > 0
        and row.diagonal_tail_radius >= 0
        and row.escape_radius >= 0
        for row in rows
    )
    check(
        "tail radius decomposes into nonnegative diagonal-tail and half-slice escape terms",
        tail_order_ok,
        "tail_radius = diagonal_tail_radius + escape_radius for every row",
    )

    text = note_text()
    required_note_strings = [
        "**Status authority:** independent audit lane only.",
        "No continuum limit",
        "No R^4 construction",
        "CERTIFIED",
        "beta = 9",
        "Tail-Control Lemma",
        "finite-emulation witness",
        "scripts/native_gauge_transfer_half_slice_certified_gap_rung_three_bounded_2026_06_12.py",
        "TOTAL: PASS=",
    ]
    check(
        "note contains scope, status-authority, table, frontier, and runner markers",
        all(s in text for s in required_note_strings),
        "checked required note markers",
    )

    required_links = [
        "[RUNG_ONE_NOTE.md](../.claude/tmp/refs/RUNG_ONE_NOTE.md)",
        "[RUNG_TWO_NOTE.md](../.claude/tmp/refs/RUNG_TWO_NOTE.md)",
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
