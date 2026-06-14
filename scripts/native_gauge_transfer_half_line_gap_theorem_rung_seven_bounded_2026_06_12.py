#!/usr/bin/env python3
"""Native gauge-transfer half-line gap rung-seven bounded attempt runner.

This runner verifies the rung-seven note surface and recomputes small
deterministic diagnostics used in the note. The diagnostics are finite-block
checks only; they do not promote a fitted monotonicity or operator-norm
remainder proof.
"""

from __future__ import annotations

from functools import lru_cache
from math import exp, sqrt
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
    / "NATIVE_GAUGE_TRANSFER_HALF_LINE_GAP_THEOREM_RUNG_SEVEN_BOUNDED_NOTE_2026-06-12.md"
)
RUNG_SIX_PATH = REPO_ROOT / ".claude" / "tmp" / "refs" / "RUNG_SIX_NOTE.md"
RUNG_FIVE_PATH = REPO_ROOT / ".claude" / "tmp" / "refs" / "RUNG_FIVE_NOTE.md"
CHARACTER_NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md"
)

MODE_MAX = 120
PASS = 0
FAIL = 0


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


def note_text() -> str:
    return NOTE_PATH.read_text(encoding="utf-8")


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_su3(p: int, q: int) -> float:
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def weights_box(shell: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(shell + 1) for q in range(shell + 1)]


def shifted_j_dense(shell: int, edge_scale: float = 1.0 / 6.0) -> tuple[np.ndarray, list[tuple[int, int]]]:
    weights = weights_box(shell)
    index = {w: i for i, w in enumerate(weights)}
    j = np.zeros((len(weights), len(weights)), dtype=float)
    for p, q in weights:
        col = index[(p, q)]
        for nb in src_existing.recurrence_neighbors(p, q):
            row = index.get(nb)
            if row is not None:
                j[row, col] += edge_scale
    return j - (6.0 * edge_scale) * np.eye(len(weights)), weights


@lru_cache(maxsize=None)
def wilson_coeff(beta_key: int, p: int, q: int) -> float:
    beta = beta_key / 1_000_000.0
    return src_existing.wilson_character_coefficient(p, q, MODE_MAX, beta / 3.0)


def coeff(beta: float, p: int, q: int) -> float:
    return wilson_coeff(int(round(beta * 1_000_000.0)), p, q)


def true_diagonal(beta: float, shell: int) -> np.ndarray:
    c00 = coeff(beta, 0, 0)
    return np.array([coeff(beta, p, q) / c00 for p, q in weights_box(shell)], dtype=float)


def saddle_diagonal(beta: float, shell: int, saddle_constant: float = 3.0) -> np.ndarray:
    return np.array(
        [
            dim_su3(p, q) * exp(-saddle_constant * casimir_su3(p, q) / beta)
            for p, q in weights_box(shell)
        ],
        dtype=float,
    )


def top_ratio_from_diagonal(
    beta: float,
    shell: int,
    diagonal: np.ndarray,
    *,
    edge_scale: float = 1.0 / 6.0,
) -> float:
    shifted, _weights = shifted_j_dense(shell, edge_scale=edge_scale)
    half_slice = expm((beta / 2.0) * shifted)
    diag = np.array(diagonal, dtype=float)
    diag = diag / float(np.max(diag))
    matrix = half_slice @ np.diag(diag) @ half_slice
    eigvals = np.linalg.eigvalsh(matrix)
    return float(eigvals[-2] / eigvals[-1])


def normalized_true_operator(beta: float, shell: int) -> np.ndarray:
    shifted, _weights = shifted_j_dense(shell)
    half_slice = expm((beta / 2.0) * shifted)
    diag = true_diagonal(beta, shell)
    diag = diag / float(np.max(diag))
    return half_slice @ np.diag(diag) @ half_slice


def finite_ratio(beta: float, shell: int = 10) -> float:
    return top_ratio_from_diagonal(beta, shell, true_diagonal(beta, shell))


def finite_ratio_derivative(beta: float, shell: int = 10, h: float = 1.0e-3) -> float:
    return (finite_ratio(beta + h, shell) - finite_ratio(beta - h, shell)) / (2.0 * h)


def main() -> int:
    print("Native gauge-transfer half-line gap rung-seven bounded attempt runner")
    print(f"MODE_MAX={MODE_MAX}")
    print("Finite diagnostics are not promoted to half-line proof constants.")
    print()

    text = note_text()
    text_ws = " ".join(text.split())
    rung_six = RUNG_SIX_PATH.read_text(encoding="utf-8")
    rung_five = RUNG_FIVE_PATH.read_text(encoding="utf-8")
    char_text = CHARACTER_NOTE_PATH.read_text(encoding="utf-8")

    check(
        "note declares independent audit-lane status authority",
        "**Status authority:** independent audit lane only." in text
        and "does not set or predict an audit outcome" in text_ws,
    )
    check(
        "note explicitly does not prove or assemble the half-line theorem",
        "does not prove a uniform half-line bound" in text_ws
        and "does not assemble a half-line gap theorem" in text_ws,
    )
    check(
        "note links primary runner and cache",
        "[native_gauge_transfer_half_line_gap_theorem_rung_seven_bounded_2026_06_12.py]"
        in text
        and "[native_gauge_transfer_half_line_gap_theorem_rung_seven_bounded_2026_06_12.txt]"
        in text,
    )
    check(
        "note states no new imports or fitted selector",
        "No literature value, new axiom, external citation, fitted selector, or new" in text,
    )

    missing_lemma = """large_beta_scaled_operator_remainder:
  after scaling out exp(beta) beta^(3/2), the true T_beta converges to
  T_infty in the block operator norm with an explicit decreasing remainder
  epsilon(beta), and the top two eigenvalues remain isolated with explicit
  perturbation margins."""
    check(
        "note quotes the exact rung-six missing lemma",
        missing_lemma in text and missing_lemma in rung_six,
    )
    saddle_markers = [
        "r_(p,q)(beta) = d_(p,q) exp[-3 C2(p,q)/beta] * (1 + lower-order terms).",
        "beta^(-3/2) r_(p,q)(beta)",
        "J - I -> beta^(-1) L",
        "T_infty = S_(1/2) M_[H exp(-Q)] S_(1/2)",
    ]
    check(
        "note quotes the rung-six saddle structure",
        all(marker in text and marker in rung_six for marker in saddle_markers),
    )
    check(
        "note quotes the large-beta limit as characterization, not uniform bound",
        "lambda_1/lambda_0 -> 0.1938058" in text
        and "not as a uniform bound" in text,
    )
    check(
        "note restates rung-five trajectory and certificate scope",
        "local high point near beta `2`" in text
        and "certified the bounded `B_16` rows through beta `26`" in text
        and "not an all-beta persistence theorem" in rung_five,
    )

    authority_links = [
        "[RUNG_SIX_NOTE.md](../.claude/tmp/refs/RUNG_SIX_NOTE.md)",
        "[RUNG_FIVE_NOTE.md](../.claude/tmp/refs/RUNG_FIVE_NOTE.md)",
        "[GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)",
        "[GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)",
        "[WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md](WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md)",
    ]
    check(
        "one-hop authorities are markdown links",
        all(link in text for link in authority_links),
    )
    disallowed_status_tokens = [
        "re" + "tained_" + "no" + "_go",
        "audited_" + "cl" + "ean",
        "audited_" + "cond" + "itional",
        "audit status: " + "cl" + "ean",
        "audit status: " + "cond" + "itional",
    ]
    check(
        "note does not write an audit-status token",
        not any(token in text.lower() for token in disallowed_status_tokens),
    )
    banned_phrases = [
        " ".join(("only", "route")),
        " ".join(("last", "route")),
        " ".join(("closes", "the", "program")),
        " ".join(("clay", "yang-mills", "mass", "gap", "problem", "is", "solved")),
        "physical " + "beta=6" + " environment claim",
    ]
    check(
        "note avoids overreach phrases",
        not any(phrase in text.lower() for phrase in banned_phrases),
    )
    gate_markers = ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]
    check(
        "negative-claim discipline gate is visible and demoted",
        all(marker in text for marker in gate_markers)
        and "demoted to a partial attempt with named residuals" in text,
    )

    harmonic_samples = [(0, 0), (1, 0), (0, 1), (2, 3), (7, 0), (4, 4)]
    harmonic_ok = all(
        sum(dim_su3(*nb) for nb in src_existing.recurrence_neighbors(p, q))
        == 6 * dim_su3(p, q)
        for p, q in harmonic_samples
    )
    check(
        "dimension function remains exact six-neighbor harmonic on samples",
        harmonic_ok
        and "X = (chi_(1,0) + chi_(0,1)) / 6" in char_text,
        "checked boundary and interior samples",
    )

    ratios = [(beta, finite_ratio(float(beta))) for beta in (2, 4, 8, 12)]
    ratio_decreases = all(ratios[i][1] > ratios[i + 1][1] for i in range(len(ratios) - 1))
    check(
        "small finite true-ratio diagnostic decreases after beta=2",
        ratio_decreases,
        ", ".join(f"beta={beta}: {value:.12f}" for beta, value in ratios),
    )

    derivs = [(beta, finite_ratio_derivative(float(beta))) for beta in (4, 8, 12)]
    check(
        "small finite ratio derivative diagnostic is negative at sampled beta",
        all(value < 0.0 for _beta, value in derivs),
        ", ".join(f"beta={beta}: d={value:.6e}" for beta, value in derivs),
    )

    h = 1.0e-3
    deriv_matrix = (normalized_true_operator(12.0 + h, 8) - normalized_true_operator(12.0 - h, 8)) / (2.0 * h)
    deriv_eigs = np.linalg.eigvalsh(deriv_matrix)
    check(
        "normalized finite-block operator derivative is sign-indefinite",
        deriv_eigs[0] < -1.0e-4 and deriv_eigs[-1] > 1.0e-4,
        f"min={deriv_eigs[0]:.6e}, max={deriv_eigs[-1]:.6e}",
    )

    beta = 50.0
    sample_weights = [(1, 0), (2, 0), (1, 1), (4, 2), (5, 5), (8, 0), (8, 8)]
    c00 = coeff(beta, 0, 0)
    scaled_residuals: list[float] = []
    for p, q in sample_weights:
        true_val = coeff(beta, p, q) / c00
        saddle_val = dim_su3(p, q) * exp(-3.0 * casimir_su3(p, q) / beta)
        scaled_residuals.append(beta * (true_val / saddle_val - 1.0))
    check(
        "Wilson saddle residual diagnostic is visible and nonzero",
        max(abs(x) for x in scaled_residuals) > 0.1,
        "beta*(true/saddle-1)=" + ", ".join(f"{x:.6f}" for x in scaled_residuals),
    )

    reduced_correct = top_ratio_from_diagonal(20.0, 12, saddle_diagonal(20.0, 12, 3.0))
    reduced_wrong_saddle = top_ratio_from_diagonal(20.0, 12, saddle_diagonal(20.0, 12, 2.0))
    reduced_wrong_j = top_ratio_from_diagonal(
        20.0,
        12,
        saddle_diagonal(20.0, 12, 3.0),
        edge_scale=1.0 / 5.0,
    )
    check(
        "finite reduced-operator falsifiers react to wrong structure",
        abs(reduced_wrong_saddle - reduced_correct) > 0.04
        and abs(reduced_wrong_j - reduced_correct) > 0.02,
        f"correct={reduced_correct:.12f}, saddle2={reduced_wrong_saddle:.12f}, j1/5={reduced_wrong_j:.12f}",
    )

    check(
        "note verification section names the expected runner total",
        "TOTAL: PASS=19, FAIL=0" in text,
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
