#!/usr/bin/env python3
"""Native gauge-transfer large-beta gap rung-six bounded runner.

This runner stays on the repo-native SU(3) dominant-weight packet tower.
It computes the true half-slice block ratio at large beta with shell
stability checks, then compares that numerical extrapolation to an
independent saddle-reduced large-beta operator.

No continuum Yang-Mills, physical beta=6 environment, external comparator,
or audit status is asserted by this runner.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, log
from pathlib import Path
import sys
import time

import numpy as np
from scipy.sparse import csr_matrix, identity
from scipy.sparse.linalg import LinearOperator, eigsh, expm_multiply


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve as src_existing


AUDIT_TIMEOUT_SEC = 540

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md"
)
CHARACTER_NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md"
)

MODE_MAX = 360
TRUE_TOL = 2.0e-8
ASYM_TOL = 2.0e-9

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class RatioRow:
    beta: int
    shells: tuple[int, int]
    values: tuple[float, float]

    @property
    def final_shell(self) -> int:
        return self.shells[-1]

    @property
    def final_value(self) -> float:
        return self.values[-1]

    @property
    def spread(self) -> float:
        return max(self.values) - min(self.values)


@dataclass(frozen=True)
class FitResult:
    powers: tuple[int, ...]
    coeffs: tuple[float, ...]
    max_residual: float

    @property
    def limit(self) -> float:
        return self.coeffs[0]


SHIFTED_J_CACHE: dict[tuple[int, float], tuple[csr_matrix, list[tuple[int, int]]]] = {}
COEFF_CACHE: dict[tuple[int, int, int], dict[tuple[int, int], float]] = {}


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


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_su3(p: int, q: int) -> float:
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def weights_box(shell: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(shell + 1) for q in range(shell + 1)]


def recurrence_neighbors(p: int, q: int) -> list[tuple[int, int]]:
    return src_existing.recurrence_neighbors(p, q)


def shifted_j(shell: int, edge_scale: float = 1.0 / 6.0) -> tuple[csr_matrix, list[tuple[int, int]]]:
    """Return J - rho_edge I, with rho_edge = 6 * edge_scale.

    The scalar exp((beta/2) rho_edge) cancels in lambda_1/lambda_0. Scaling it
    out keeps the large-beta half-slice action numerically conditioned.
    """

    key = (shell, edge_scale)
    cached = SHIFTED_J_CACHE.get(key)
    if cached is not None:
        return cached

    weights = weights_box(shell)
    index = {w: i for i, w in enumerate(weights)}
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    for p, q in weights:
        col = index[(p, q)]
        for nb in recurrence_neighbors(p, q):
            row = index.get(nb)
            if row is not None:
                rows.append(row)
                cols.append(col)
                data.append(edge_scale)
    j = csr_matrix((data, (rows, cols)), shape=(len(weights), len(weights)))
    out = (j - (6.0 * edge_scale) * identity(len(weights), format="csr"), weights)
    SHIFTED_J_CACHE[key] = out
    return out


def deterministic_v0(n: int) -> np.ndarray:
    idx = np.arange(n, dtype=float)
    return 1.0 + 1.0e-3 * ((idx % 17.0) / 17.0)


def top_ratio_from_diagonal(
    beta: int,
    shell: int,
    diagonal: np.ndarray,
    *,
    edge_scale: float = 1.0 / 6.0,
    tol: float = TRUE_TOL,
) -> float:
    shifted, weights = shifted_j(shell, edge_scale)
    n = len(weights)
    tau = beta / 2.0
    diag = np.array(diagonal, dtype=float)
    diag = diag / float(np.max(diag))

    def matvec(v: np.ndarray) -> np.ndarray:
        y = expm_multiply(tau * shifted, v, traceA=0.0)
        y = diag * y
        return expm_multiply(tau * shifted, y, traceA=0.0)

    op = LinearOperator((n, n), matvec=matvec, dtype=float)
    eigvals = eigsh(
        op,
        k=2,
        which="LA",
        tol=tol,
        return_eigenvectors=False,
        ncv=24,
        maxiter=500,
        v0=deterministic_v0(n),
    )
    eigvals.sort()
    return float(eigvals[-2] / eigvals[-1])


def coefficient_table(beta: int, max_shell: int, mode_max: int = MODE_MAX) -> dict[tuple[int, int], float]:
    key = (beta, max_shell, mode_max)
    cached = COEFF_CACHE.get(key)
    if cached is not None:
        return cached

    arg = beta / 3.0
    started = time.time()
    table: dict[tuple[int, int], float] = {}
    for p, q in weights_box(max_shell):
        table[(p, q)] = src_existing.wilson_character_coefficient(p, q, mode_max, arg)
    print(
        f"coeff_table beta={beta:>3} shell={max_shell:>2} "
        f"states={(max_shell + 1) ** 2} mode_max={mode_max} "
        f"elapsed={time.time() - started:.2f}s"
    )
    COEFF_CACHE[key] = table
    return table


def true_diagonal_from_table(
    beta: int, shell: int, table: dict[tuple[int, int], float]
) -> np.ndarray:
    c00 = table[(0, 0)]
    return np.array([table[(p, q)] / c00 for p, q in weights_box(shell)], dtype=float)


def true_ratio_rows() -> list[RatioRow]:
    plan = [
        (50, (30, 36)),
        (60, (36, 42)),
        (80, (42, 50)),
        (100, (50, 60)),
        (140, (60, 70)),
        (200, (70, 80)),
    ]
    rows: list[RatioRow] = []
    print("TRUE LARGE-BETA HALF-SLICE RATIOS")
    for beta, shells in plan:
        table = coefficient_table(beta, shells[-1])
        vals: list[float] = []
        for shell in shells:
            value = top_ratio_from_diagonal(
                beta,
                shell,
                true_diagonal_from_table(beta, shell, table),
                tol=TRUE_TOL,
            )
            vals.append(value)
        row = RatioRow(beta=beta, shells=shells, values=(vals[0], vals[1]))
        rows.append(row)
        print(
            f"true beta={beta:>3} "
            f"s{shells[0]}={vals[0]:.12f} "
            f"s{shells[1]}={vals[1]:.12f} "
            f"spread={row.spread:.3e}"
        )
    print()
    return rows


def fit_inverse_beta(betas: list[float], values: list[float], powers: tuple[int, ...]) -> FitResult:
    x = np.array(betas, dtype=float)
    y = np.array(values, dtype=float)
    design = np.column_stack([x ** (-p) for p in powers])
    coeffs = np.linalg.lstsq(design, y, rcond=None)[0]
    residual = design @ coeffs - y
    return FitResult(
        powers=powers,
        coeffs=tuple(float(c) for c in coeffs),
        max_residual=float(np.max(np.abs(residual))),
    )


def asymptotic_diagonal(beta: int, shell: int, saddle_constant: float = 3.0) -> np.ndarray:
    return np.array(
        [
            dim_su3(p, q) * exp(-saddle_constant * casimir_su3(p, q) / beta)
            for p, q in weights_box(shell)
        ],
        dtype=float,
    )


def asymptotic_ratio_rows() -> list[RatioRow]:
    plan = [
        (100, (60, 60)),
        (200, (80, 80)),
        (400, (120, 120)),
        (800, (180, 180)),
    ]
    rows: list[RatioRow] = []
    print("SADDLE-REDUCED LARGE-BETA OPERATOR RATIOS")
    for beta, shells in plan:
        value = top_ratio_from_diagonal(
            beta,
            shells[-1],
            asymptotic_diagonal(beta, shells[-1]),
            tol=ASYM_TOL,
        )
        rows.append(RatioRow(beta=beta, shells=shells, values=(value, value)))
        print(f"analytic_reduced beta={beta:>3} shell={shells[-1]:>3} value={value:.12f}")
    print()
    return rows


def saddle_constant_samples() -> list[float]:
    beta = 400
    arg = beta / 3.0
    c00 = src_existing.wilson_character_coefficient(0, 0, MODE_MAX, arg)
    samples: list[float] = []
    for p, q in [(1, 0), (2, 0), (1, 1), (5, 0), (5, 5), (10, 0), (10, 10)]:
        coeff = src_existing.wilson_character_coefficient(p, q, MODE_MAX, arg)
        ratio = coeff / c00
        samples.append(-beta * log(ratio / dim_su3(p, q)) / casimir_su3(p, q))
    return samples


def falsifier_rows() -> tuple[float, float, float]:
    beta = 200
    shell = 80
    correct = top_ratio_from_diagonal(
        beta, shell, asymptotic_diagonal(beta, shell), tol=ASYM_TOL
    )
    wrong_nc_like = top_ratio_from_diagonal(
        beta, shell, asymptotic_diagonal(beta, shell, saddle_constant=2.0), tol=ASYM_TOL
    )
    wrong_j_norm = top_ratio_from_diagonal(
        beta,
        shell,
        asymptotic_diagonal(beta, shell),
        edge_scale=1.0 / 5.0,
        tol=ASYM_TOL,
    )
    print("FALSIFIER ROWS ON THE REDUCED OPERATOR")
    print(f"falsifier beta=200 shell=80 correct={correct:.12f}")
    print(f"falsifier beta=200 shell=80 saddle_constant_2={wrong_nc_like:.12f}")
    print(f"falsifier beta=200 shell=80 J_adjacency_scale_1_over_5={wrong_j_norm:.12f}")
    print()
    return correct, wrong_nc_like, wrong_j_norm


def note_text() -> str:
    return NOTE_PATH.read_text(encoding="utf-8")


def main() -> int:
    print("Native gauge-transfer large-beta gap rung-six bounded runner")
    print(f"MODE_MAX={MODE_MAX}, TRUE_TOL={TRUE_TOL}, ASYM_TOL={ASYM_TOL}")
    print("Half-slice scalar exp(beta/2) factors are scaled out in eigen-ratio computations.")
    print()

    char_text = CHARACTER_NOTE_PATH.read_text(encoding="utf-8")
    check(
        "character authority states the six-neighbor source recurrence",
        "X = (chi_(1,0) + chi_(0,1)) / 6" in char_text
        and "Exact `SU(3)` dominant-weight recurrence" in char_text,
        "checked source-character note markers",
    )

    harmonic_samples = [(0, 0), (1, 0), (0, 1), (2, 3), (7, 0), (4, 4)]
    harmonic_ok = all(
        sum(dim_su3(*nb) for nb in recurrence_neighbors(p, q)) == 6 * dim_su3(p, q)
        for p, q in harmonic_samples
    )
    check(
        "dimension function is the exact spectral-edge harmonic function",
        harmonic_ok,
        "checked 6 d_(p,q) = sum_neighbors d_neighbor on boundary and interior samples",
    )

    saddle_constants = saddle_constant_samples()
    check(
        "Wilson coefficient saddle constant is numerically the SU(3) value 3",
        max(abs(x - 3.0) for x in saddle_constants) < 0.014,
        "samples=" + ", ".join(f"{x:.6f}" for x in saddle_constants),
    )

    true_rows = true_ratio_rows()
    true_betas = [float(r.beta) for r in true_rows]
    true_values = [r.final_value for r in true_rows]
    true_fit_2 = fit_inverse_beta(true_betas, true_values, (0, 1, 2))
    true_fit_3 = fit_inverse_beta(true_betas, true_values, (0, 1, 2, 3))
    true_estimate = 0.5 * (true_fit_2.limit + true_fit_3.limit)
    true_error = max(
        abs(true_fit_2.limit - true_fit_3.limit),
        true_fit_2.max_residual,
        true_fit_3.max_residual,
        max(r.spread for r in true_rows),
    )
    print(
        "true_extrapolation "
        f"fit_1_over_beta2={true_fit_2.limit:.12f} "
        f"fit_1_over_beta3={true_fit_3.limit:.12f} "
        f"estimate={true_estimate:.12f} "
        f"error_proxy={true_error:.3e}"
    )
    print()

    check(
        "requested true-ratio beta grid is shell-stable",
        max(r.spread for r in true_rows) < 6.0e-9,
        f"max shell spread={max(r.spread for r in true_rows):.3e}",
    )
    check(
        "true large-beta grid decreases from beta=50 through beta=200",
        all(true_values[i] > true_values[i + 1] for i in range(len(true_values) - 1)),
        "values=" + ", ".join(f"{v:.12f}" for v in true_values),
    )
    check(
        "true Richardson estimate lies below the beta=200 true ratio and below one",
        true_estimate < true_rows[-1].final_value and true_estimate < 1.0,
        f"estimate={true_estimate:.12f}, beta200={true_rows[-1].final_value:.12f}",
    )

    asym_rows = asymptotic_ratio_rows()
    asym_betas = [float(r.beta) for r in asym_rows]
    asym_values = [r.final_value for r in asym_rows]
    asym_fit_2 = fit_inverse_beta(asym_betas, asym_values, (0, 1, 2))
    asym_fit_3 = fit_inverse_beta(asym_betas, asym_values, (0, 1, 2, 3))
    asym_estimate = 0.5 * (asym_fit_2.limit + asym_fit_3.limit)
    asym_error = max(
        abs(asym_fit_2.limit - asym_fit_3.limit),
        asym_fit_2.max_residual,
        asym_fit_3.max_residual,
    )
    print(
        "analytic_reduced_extrapolation "
        f"fit_1_over_beta2={asym_fit_2.limit:.12f} "
        f"fit_1_over_beta3={asym_fit_3.limit:.12f} "
        f"estimate={asym_estimate:.12f} "
        f"error_proxy={asym_error:.3e}"
    )
    print()

    check(
        "saddle-reduced operator ratios decrease on the analytic grid",
        all(asym_values[i] > asym_values[i + 1] for i in range(len(asym_values) - 1)),
        "values=" + ", ".join(f"{v:.12f}" for v in asym_values),
    )
    check(
        "numerical and saddle-reduced limit estimates agree",
        abs(true_estimate - asym_estimate) < 2.0e-7,
        f"true={true_estimate:.12f}, analytic={asym_estimate:.12f}, "
        f"discrepancy={abs(true_estimate - asym_estimate):.3e}",
    )

    correct_f, wrong_nc, wrong_j = falsifier_rows()
    check(
        "wrong saddle constant changes the reduced limit row visibly",
        abs(wrong_nc - correct_f) > 0.05,
        f"correct={correct_f:.12f}, saddle_constant_2={wrong_nc:.12f}",
    )
    check(
        "wrong six-neighbor J normalization changes the reduced limit row visibly",
        abs(wrong_j - correct_f) > 0.02,
        f"correct={correct_f:.12f}, J_scale_1/5={wrong_j:.12f}",
    )

    text = note_text()
    required_note_strings = [
        "**Status authority:** independent audit lane only.",
        "T_beta = exp((beta/2) J) D_beta exp((beta/2) J)",
        "r_(p,q)(beta) = c_(p,q)(beta) / c_(0,0)(beta)",
        "lambda_1/lambda_0 -> 0.1938058",
        "The uniform half-line bound is not proved here.",
        "missing lemma",
        "scripts/native_gauge_transfer_large_beta_gap_rung_six_bounded_2026_06_12.py",
        "logs/runner-cache/native_gauge_transfer_large_beta_gap_rung_six_bounded_2026_06_12.txt",
    ]
    check(
        "note contains status, object, limit, runner, cache, and caveat markers",
        all(s in text for s in required_note_strings),
        "checked required note markers",
    )

    required_links = [
        "[GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)",
        "[GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)",
        "[WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md](WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md)",
    ]
    check(
        "one-hop authorities are canonical markdown links with no scratch dependency",
        all(link in text for link in required_links)
        and ".claude/tmp/refs" not in text
        and "no scratch-work rung\nfile is a dependency" in text,
        "checked authority-link forms and scratch-free scope",
    )

    banned_phrases = [
        " ".join(parts)
        for parts in [
            ("only", "route"),
            ("last", "route"),
            ("exhau", "sted"),
            ("closes", "the", "program"),
            ("Clay", "Yang-Mills", "mass", "gap", "problem", "is", "solved"),
            ("beta", "=", "6", "physical"),
        ]
    ]
    lower_text = text.lower()
    check(
        "note avoids overreach and forbidden physical-scope phrases",
        not any(phrase.lower() in lower_text for phrase in banned_phrases),
        "scanned banned phrase set",
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
