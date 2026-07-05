#!/usr/bin/env python3
"""Native gauge-transfer block-Hellmann monotonicity rung-eight runner.

This runner verifies the rung-eight bounded note surface and recomputes the
finite-block Hellmann split used there. The finite-block sign checks are
witnesses for the named derivative-inequality target; they are not promoted to
an all-beta proof or audit status.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from math import isfinite
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import expm


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve as src_existing


AUDIT_TIMEOUT_SEC = 540

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_BLOCK_HELLMANN_MONOTONICITY_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md"
)
CHARACTER_NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md"
)

MODE_MAX = 160
GRID_POST_PEAK = (3, 4, 8, 12, 16, 20, 24, 26, 30, 40, 50)
CERTIFIED_INTEGER_GRID = tuple(range(1, 27))

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class HellmannRow:
    beta: float
    shell: int
    ratio: float
    gap01: float
    gap12: float
    jdiff: float
    ddiff: float
    logdiff: float
    direct_logdiff: float


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


def weights_box(shell: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(shell + 1) for q in range(shell + 1)]


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_su3(p: int, q: int) -> float:
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def build_j_dense(shell: int, edge_scale: float = 1.0 / 6.0) -> tuple[np.ndarray, list[tuple[int, int]]]:
    weights = weights_box(shell)
    index = {w: i for i, w in enumerate(weights)}
    j = np.zeros((len(weights), len(weights)), dtype=float)
    for p, q in weights:
        col = index[(p, q)]
        for nb in src_existing.recurrence_neighbors(p, q):
            row = index.get(nb)
            if row is not None:
                j[row, col] += edge_scale
    return j, weights


@lru_cache(maxsize=None)
def wilson_coeff(beta_key: int, p: int, q: int) -> float:
    beta = beta_key / 1_000_000.0
    return src_existing.wilson_character_coefficient(p, q, MODE_MAX, beta / 3.0)


def coeff(beta: float, p: int, q: int) -> float:
    return wilson_coeff(int(round(beta * 1_000_000.0)), p, q)


def coefficient_table(beta: float, shell_plus: int) -> dict[tuple[int, int], float]:
    return {(p, q): coeff(beta, p, q) for p, q in weights_box(shell_plus)}


def coeff_prime_from_recurrence(
    table: dict[tuple[int, int], float],
    p: int,
    q: int,
    scale: float = 1.0 / 6.0,
) -> float:
    return scale * sum(table[nb] for nb in src_existing.recurrence_neighbors(p, q))


def diagonal_and_derivative(
    beta: float,
    shell: int,
    derivative_scale: float = 1.0 / 6.0,
) -> tuple[np.ndarray, np.ndarray]:
    table = coefficient_table(beta, shell + 1)
    c00 = table[(0, 0)]
    c00_prime = coeff_prime_from_recurrence(table, 0, 0, derivative_scale)

    diagonal: list[float] = []
    derivative: list[float] = []
    for p, q in weights_box(shell):
        c = table[(p, q)]
        c_prime = coeff_prime_from_recurrence(table, p, q, derivative_scale)
        diagonal.append(c / c00)
        derivative.append(c_prime / c00 - c * c00_prime / (c00 * c00))
    return np.array(diagonal, dtype=float), np.array(derivative, dtype=float)


def hellmann_row(
    beta: float,
    shell: int,
    *,
    edge_scale: float = 1.0 / 6.0,
    derivative_scale: float = 1.0 / 6.0,
) -> HellmannRow:
    j, weights = build_j_dense(shell, edge_scale=edge_scale)
    shifted_j = j - (6.0 * edge_scale) * np.eye(len(weights))
    e_half = expm((beta / 2.0) * shifted_j)
    diagonal, diagonal_prime = diagonal_and_derivative(
        beta, shell, derivative_scale=derivative_scale
    )
    matrix = e_half @ np.diag(diagonal) @ e_half
    derivative_diagonal_part = e_half @ np.diag(diagonal_prime) @ e_half
    derivative_matrix = (
        0.5 * (shifted_j @ matrix + matrix @ shifted_j) + derivative_diagonal_part
    )

    eigvals, eigvecs = np.linalg.eigh(matrix)
    lam0 = float(eigvals[-1])
    lam1 = float(eigvals[-2])
    lam2 = float(eigvals[-3])
    v0 = eigvecs[:, -1]
    v1 = eigvecs[:, -2]

    j0 = float(v0 @ j @ v0)
    j1 = float(v1 @ j @ v1)
    d0 = float(v0 @ derivative_diagonal_part @ v0) / lam0
    d1 = float(v1 @ derivative_diagonal_part @ v1) / lam1
    direct0 = float(v0 @ derivative_matrix @ v0) / lam0
    direct1 = float(v1 @ derivative_matrix @ v1) / lam1

    return HellmannRow(
        beta=beta,
        shell=shell,
        ratio=lam1 / lam0,
        gap01=lam0 - lam1,
        gap12=lam1 - lam2,
        jdiff=j1 - j0,
        ddiff=d1 - d0,
        logdiff=(j1 - j0) + (d1 - d0),
        direct_logdiff=direct1 - direct0,
    )


def finite_ratio(beta: float, shell: int) -> float:
    row = hellmann_row(beta, shell)
    return row.ratio


def finite_log_ratio_derivative(beta: float, shell: int, h: float = 1.0e-3) -> float:
    return (np.log(finite_ratio(beta + h, shell)) - np.log(finite_ratio(beta - h, shell))) / (
        2.0 * h
    )


def saddle_diagonal(beta: float, shell: int, saddle_constant: float = 3.0) -> np.ndarray:
    return np.array(
        [
            dim_su3(p, q) * np.exp(-saddle_constant * casimir_su3(p, q) / beta)
            for p, q in weights_box(shell)
        ],
        dtype=float,
    )


def ratio_from_diagonal(
    beta: float,
    shell: int,
    diagonal: np.ndarray,
    edge_scale: float = 1.0 / 6.0,
) -> float:
    j, weights = build_j_dense(shell, edge_scale=edge_scale)
    shifted_j = j - (6.0 * edge_scale) * np.eye(len(weights))
    e_half = expm((beta / 2.0) * shifted_j)
    diag = np.array(diagonal, dtype=float)
    diag = diag / float(np.max(diag))
    matrix = e_half @ np.diag(diag) @ e_half
    eigvals = np.linalg.eigvalsh(matrix)
    return float(eigvals[-2] / eigvals[-1])


def check_character_derivative() -> tuple[bool, str]:
    beta = 8.0
    h = 1.0e-5
    table = coefficient_table(beta, 6)
    samples = [(0, 0), (1, 0), (2, 1), (4, 3)]
    rel_errors: list[float] = []
    for p, q in samples:
        recurrence_value = coeff_prime_from_recurrence(table, p, q)
        finite_difference = (coeff(beta + h, p, q) - coeff(beta - h, p, q)) / (2.0 * h)
        denom = max(1.0, abs(finite_difference))
        rel_errors.append(abs(recurrence_value - finite_difference) / denom)
    return max(rel_errors) < 2.0e-8, "max relative error=" + f"{max(rel_errors):.3e}"


def main() -> int:
    print("Native gauge-transfer block-Hellmann monotonicity rung-eight runner")
    print(f"MODE_MAX={MODE_MAX}")
    print("Finite-block diagnostics witness the named inequality target; they are not a proof.")
    print()

    text = NOTE_PATH.read_text(encoding="utf-8")
    text_ws = " ".join(text.split())
    char_text = CHARACTER_NOTE_PATH.read_text(encoding="utf-8")

    check("note declares canonical bounded theorem claim type", "**Claim type:** bounded_theorem" in text)
    check(
        "note preserves independent audit-lane status authority",
        "**Status authority:** independent audit lane only." in text
        and "does not set or predict an audit outcome" in text_ws,
    )
    check(
        "note scope refuses half-line theorem assembly and physical-beta claims",
        "does not prove eventual monotonicity" in text_ws
        and "does not assemble the native discrete half-line gap theorem" in text_ws
        and "No continuum, Clay, or physical `beta = 6` claim is made" in text_ws,
    )
    check(
        "note states no new imports",
        "No literature value, new axiom, external citation, or new comparator number is used" in text_ws,
    )

    derivative_quote = """d/d beta log(lambda_i)
  = <u_i, (J-I) u_i>
    + <E_beta u_i, (d/d beta bar D_beta) E_beta u_i> / lambda_i."""
    check(
        "note states the exact finite-block derivative identity",
        derivative_quote in text,
    )
    target_quote = "d/d beta log(lambda_1) <= d/d beta log(lambda_0)"
    check(
        "note states the precise block-Hellmann inequality target",
        target_quote in text,
    )
    loewner_quote = (
        "The attempted shortcut was to seek a Loewner sign for `d bar T_beta / d beta`."
    )
    check(
        "note names the rejected Loewner shortcut without using it as proof",
        loewner_quote in text
        and "sign-indefinite" in text
        and "does not claim a Loewner-order proof" in text,
    )
    check(
        "note records the unshifted product-rule derivative and recurrence D prime",
        "dT_beta/dbeta = (1/2)(J T_beta + T_beta J) + E_beta D_beta' E_beta" in text
        and "c'_(p,q)(beta) = (1/6) sum_{nu in N(p,q)} c_nu(beta)" in text,
    )
    check(
        "note isolates the exact J-part contribution",
        "J-part contribution to d/dbeta log(lambda_i) is <v_i, J v_i>" in text
        and "Delta_J + Delta_D <= 0" in text,
    )
    check(
        "note states the simplicity and isolation hypothesis",
        "lambda_0 and lambda_1 must be simple and isolated" in text
        and "finite-grid witness, not an interval proof" in text,
    )
    check(
        "note restates finite-grid peak and certified-frontier scope",
        "local high point near beta `2`" in text
        and "certified the bounded `B_16` rows through beta `26`" in text_ws
        and "not an all-beta persistence theorem" in text_ws,
    )

    authority_links = [
        "[GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)",
        "[GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)",
        "[WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md](WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md)",
    ]
    check("one-hop authorities are markdown links", all(link in text for link in authority_links))
    check(
        "runner and cache are portable markdown links",
        "[scripts/native_gauge_transfer_block_hellmann_monotonicity_rung_eight_bounded_2026_06_12.py](../scripts/native_gauge_transfer_block_hellmann_monotonicity_rung_eight_bounded_2026_06_12.py)" in text
        and "[logs/runner-cache/native_gauge_transfer_block_hellmann_monotonicity_rung_eight_bounded_2026_06_12.txt](../logs/runner-cache/native_gauge_transfer_block_hellmann_monotonicity_rung_eight_bounded_2026_06_12.txt)" in text,
    )
    check(
        "note and runner avoid branch-local temp references",
        ("." + "claude" + "/tmp") not in text
        and ("tmp" + "/refs") not in text
        and ("." + "claude" + "/tmp") not in Path(__file__).read_text(encoding="utf-8"),
    )

    status_tokens = [
        "audit " + "status:",
        "retained/" + "no" + "_go",
        "no" + "_go",
        "audited_" + "clean",
        "audited_" + "conditional",
        "clean " + "prediction",
        "conditional " + "prediction",
    ]
    lower_text = text.lower()
    check(
        "note does not write audit-status tokens",
        not any(token in lower_text for token in status_tokens),
    )
    banned_phrases = [
        "only " + "route",
        "last " + "route",
        "exhau" + "sted",
        "closes " + "the program",
        "closes " + "the half-line",
        "closes " + "the native discrete",
    ]
    check(
        "note avoids overreach phrases",
        not any(phrase in lower_text for phrase in banned_phrases),
    )
    gate_markers = [f"N{i} -" for i in range(1, 9)]
    check(
        "negative-claim discipline gate is visible and narrowed",
        all(marker in text for marker in gate_markers)
        and "partial narrowing with named residuals" in text,
    )

    harmonic_samples = [(0, 0), (1, 0), (0, 1), (2, 3), (7, 0), (4, 4)]
    harmonic_ok = all(
        sum(dim_su3(*nb) for nb in src_existing.recurrence_neighbors(p, q))
        == 6 * dim_su3(p, q)
        for p, q in harmonic_samples
    )
    check(
        "dimension function remains exact six-neighbor harmonic on samples",
        harmonic_ok and "X = (chi_(1,0) + chi_(0,1)) / 6" in char_text,
    )
    derivative_ok, derivative_detail = check_character_derivative()
    check(
        "character recurrence differentiates Wilson coefficients",
        derivative_ok,
        derivative_detail,
    )

    certified_rows = [hellmann_row(float(beta), 16) for beta in CERTIFIED_INTEGER_GRID]
    min_gap01 = min(row.gap01 for row in certified_rows)
    min_gap12 = min(row.gap12 for row in certified_rows)
    check(
        "top two finite-block eigenvalues are simple on certified integer grid",
        min_gap01 > 1.0e-14 and min_gap12 > 1.0e-14,
        f"shell=16 beta=1..26 min_gap01={min_gap01:.3e}, min_gap12={min_gap12:.3e}",
    )

    post_peak_rows = [hellmann_row(float(beta), 22) for beta in GRID_POST_PEAK]
    split_error = max(abs(row.logdiff - row.direct_logdiff) for row in post_peak_rows)
    check(
        "product-rule Hellmann split matches direct derivative matrix",
        split_error < 5.0e-11,
        f"max split error={split_error:.3e}",
    )
    fd_rows = [(beta, hellmann_row(float(beta), 12)) for beta in (8, 20)]
    fd_errors = [
        abs(row.logdiff - finite_log_ratio_derivative(float(beta), 12))
        for beta, row in fd_rows
    ]
    check(
        "Hellmann log-ratio derivative matches central finite difference",
        max(fd_errors) < 2.0e-5,
        "errors=" + ", ".join(f"beta={beta}: {err:.3e}" for (beta, _row), err in zip(fd_rows, fd_errors)),
    )

    beta2_row = hellmann_row(2.0, 22)
    check(
        "beta=2 row is not in the decreasing derivative regime",
        beta2_row.logdiff > 0.05,
        f"logdiff={beta2_row.logdiff:.6e}",
    )
    check(
        "J-expectation ordering is witnessed on post-peak grid",
        all(row.jdiff < -1.0e-5 for row in post_peak_rows),
        "values=" + ", ".join(f"beta={int(row.beta)}:{row.jdiff:.3e}" for row in post_peak_rows),
    )
    check(
        "diagonal derivative part has the opposing positive sign on post-peak grid",
        all(row.ddiff > 0.0 for row in post_peak_rows),
        "values=" + ", ".join(f"beta={int(row.beta)}:{row.ddiff:.3e}" for row in post_peak_rows),
    )
    check(
        "finite-block derivative inequality is witnessed on post-peak grid",
        all(row.logdiff < -1.0e-5 for row in post_peak_rows),
        "values=" + ", ".join(f"beta={int(row.beta)}:{row.logdiff:.3e}" for row in post_peak_rows),
    )
    tightness = max(row.ddiff / (-row.jdiff) for row in post_peak_rows)
    check(
        "diagonal domination is the load-bearing unresolved margin",
        0.90 < tightness < 1.0,
        f"max Delta_D/(-Delta_J)={tightness:.6f}",
    )

    wrong_rows = [hellmann_row(float(beta), 12, derivative_scale=1.0 / 4.0) for beta in (8, 20)]
    check(
        "wrong character-derivative normalization breaks the domination witness",
        any(row.logdiff > 0.0 for row in wrong_rows),
        "wrong-scale logdiffs="
        + ", ".join(f"beta={int(row.beta)}:{row.logdiff:.3e}" for row in wrong_rows),
    )
    correct_reduced = ratio_from_diagonal(20.0, 12, saddle_diagonal(20.0, 12, 3.0))
    wrong_saddle = ratio_from_diagonal(20.0, 12, saddle_diagonal(20.0, 12, 2.0))
    wrong_j_scale = ratio_from_diagonal(
        20.0,
        12,
        saddle_diagonal(20.0, 12, 3.0),
        edge_scale=1.0 / 5.0,
    )
    check(
        "wrong reduced-operator constants visibly change the ratio row",
        abs(wrong_saddle - correct_reduced) > 0.04
        and abs(wrong_j_scale - correct_reduced) > 0.02,
        f"correct={correct_reduced:.12f}, saddle2={wrong_saddle:.12f}, j1/5={wrong_j_scale:.12f}",
    )
    check(
        "note verification section names the expected runner total",
        "TOTAL: PASS=30, FAIL=0" in text,
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
