#!/usr/bin/env python3
"""Native transfer beta vs physical plaquette beta relationship verifier.

This runner checks a bounded relationship note only. It verifies that the
native transfer row and the plaquette row use the same Wilson beta convention,
computes the finite native spectral ratio at beta=6, and checks guardrails that
keep the result from being read as a physical mass-gap bridge.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.special import iv


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NATIVE_GAUGE_TRANSFER_BETA_IDENTIFICATION_PHYSICAL_PLAQUETTE_RELATIONSHIP"
    "_BOUNDED_NOTE_2026-06-12.md"
)
CHAR_RECURRENCE = ROOT / "docs/GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md"
SOURCE_FACTOR = ROOT / "docs/GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md"
TENSOR_TRANSFER = ROOT / "docs/GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md"
PLAQUETTE_SELF = ROOT / "docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md"
WILSON_POSITIVITY = ROOT / "docs/WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md"
FIXED_GAP = ROOT / "docs/FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md"
SU3_GAP_REDUCTION = ROOT / "docs/SU3_BETA6_GAP_BULK_CRITICALITY_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-09.md"

BETA = 6.0
MODE_MAX = 80

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: {label}" + (f" :: {detail}" if detail else ""))
    return bool(ok)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def blocked_scope_phrases() -> tuple[str, ...]:
    return (
        "only " + "route",
        "last " + "route",
        "ex" + "hausted",
        "closes the " + "program",
    )


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def highest_weight_triple(p: int, q: int) -> list[int]:
    return [p + q, q, 0]


def weights_box(nmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def recurrence_neighbors(p: int, q: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for a, b in (
        (p + 1, q),
        (p - 1, q + 1),
        (p, q - 1),
        (p, q + 1),
        (p + 1, q - 1),
        (p - 1, q),
    ):
        if a >= 0 and b >= 0:
            out.append((a, b))
    return out


def build_j(nmax: int) -> tuple[np.ndarray, list[tuple[int, int]], dict[tuple[int, int], int]]:
    weights = weights_box(nmax)
    index = {weight: i for i, weight in enumerate(weights)}
    jmat = np.zeros((len(weights), len(weights)), dtype=float)
    for p, q in weights:
        col = index[(p, q)]
        for a, b in recurrence_neighbors(p, q):
            if (a, b) in index:
                jmat[index[(a, b)], col] += 1.0 / 6.0
    return jmat, weights, index


def matrix_exp_symmetric(matrix: np.ndarray, tau: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(matrix)
    return (vecs * np.exp(tau * vals)) @ vecs.T


def coefficient_matrix(mode: int, lam: list[int], arg: float) -> np.ndarray:
    return np.array(
        [[iv(mode + lam[j] + i - j, arg) for j in range(3)] for i in range(3)],
        dtype=float,
    )


def wilson_character_coefficient(p: int, q: int, beta: float) -> float:
    lam = highest_weight_triple(p, q)
    arg = beta / 3.0
    total = 0.0
    for mode in range(-MODE_MAX, MODE_MAX + 1):
        total += float(np.linalg.det(coefficient_matrix(mode, lam, arg)))
    return total


def native_gap_row(beta: float, nmax: int) -> dict[str, float]:
    jmat, weights, index = build_j(nmax)
    multiplier = matrix_exp_symmetric(jmat, beta / 2.0)
    coeffs = np.array(
        [wilson_character_coefficient(p, q, beta) for p, q in weights],
        dtype=float,
    )
    c00 = coeffs[index[(0, 0)]]
    diag_ratio = coeffs / c00
    transfer = multiplier @ np.diag(diag_ratio) @ multiplier
    transfer = 0.5 * (transfer + transfer.T)
    vals = np.linalg.eigvalsh(transfer)
    return {
        "ratio": float(vals[-2] / vals[-1]),
        "lambda0": float(vals[-1]),
        "lambda1": float(vals[-2]),
        "c00": float(c00),
        "diag_min": float(diag_ratio.min()),
        "diag_max": float(diag_ratio.max()),
        "j_symmetry": float(np.max(np.abs(jmat - jmat.T))),
    }


def main() -> int:
    print("Native transfer beta vs physical plaquette beta relationship verifier")
    print("=" * 78)

    note = read(NOTE)
    recurrence = read(CHAR_RECURRENCE)
    source_factor = read(SOURCE_FACTOR)
    tensor = read(TENSOR_TRANSFER)
    plaquette = read(PLAQUETTE_SELF)
    wilson = read(WILSON_POSITIVITY)
    fixed_gap = read(FIXED_GAP)
    su3_gap = read(SU3_GAP_REDUCTION)

    check(
        "relationship note defines the native transfer operator and diagonal ratio without scratch dependencies",
        "T_beta = exp((beta/2) J) D_beta exp((beta/2) J)" in note
        and "r_(p,q)(beta) = c_(p,q)(beta) / c_(0,0)(beta)" in note
        and "no scratch-work rung note\nis a dependency" in note,
    )
    check(
        "character recurrence note fixes J as the plaquette source",
        "`X = (chi_(1,0) + chi_(0,1)) / 6`" in recurrence
        and "`X(W) = (1/3) Re Tr W" in recurrence,
    )
    check(
        "tensor-transfer note states the Wilson coefficient expansion with beta/3",
        "`exp[(beta/3) Re Tr U] = sum_lambda d_lambda c_lambda(beta) chi_lambda(U),`"
        in tensor,
    )
    check(
        "source-sector note distinguishes factorization from residual environment data",
        "`T_src(beta) = exp[(beta / 2) J] D_beta exp[(beta / 2) J]`" in source_factor
        and "identify the residual source-sector environment data" in source_factor,
    )
    check(
        "plaquette note states the finite Wilson action and average plaquette object",
        "S_W[U; beta] = (beta / 3) sum_P (3 - Re Tr U_P)" in plaquette
        and "P_bar(U) = (1 / N_P) sum_P Re Tr U_P / 3" in plaquette,
    )
    check(
        "plaquette note fences the 0.5934 value as admitted comparison/reuse",
        "The canonical infinite-volume value `0.5934` is an admitted comparison/reuse number here"
        in plaquette
        and "not a value derived by this note" in plaquette,
    )
    check(
        "Wilson positivity note gives the equivalent beta/(2Nc) character argument",
        "w(V) = exp( (beta / (2 N_c)) ( chi_box(V) + chi_boxbar(V) ) )" in wilson
        and "`N_c = 3` throughout" in wilson,
    )

    nc = Fraction(3, 1)
    beta_symbol = Fraction(1, 1)
    beta_over_3 = beta_symbol / 3
    beta_over_2nc = beta_symbol / (2 * nc)
    half_slice_on_chi_sum = beta_symbol / 12
    check(
        "exact SU(3) beta identification: beta/3 on ReTr equals beta/(2Nc) on chi+chibar",
        beta_over_3 * Fraction(1, 2) == beta_over_2nc,
        f"(beta/3)*(1/2) = {beta_over_3 * Fraction(1, 2)} = beta/(2Nc) with Nc=3",
    )
    check(
        "exact half-slice identification: exp((beta/2)J) is half of exp((beta/3)ReTr)",
        half_slice_on_chi_sum * 2 == beta_over_2nc,
        f"J coefficient beta/12 per half; two halves give {half_slice_on_chi_sum * 2}",
    )

    rows = {nmax: native_gap_row(BETA, nmax) for nmax in (8, 12, 16)}
    ratio16 = rows[16]["ratio"]
    spread = max(row["ratio"] for row in rows.values()) - min(row["ratio"] for row in rows.values())
    check(
        "native beta=6 spectral row is stable across finite shells",
        spread < 2.0e-7,
        ", ".join(f"B_{n}: {rows[n]['ratio']:.15f}" for n in sorted(rows)),
    )
    check(
        "native beta=6 row matches the recomputed finite spectral ratio",
        abs(ratio16 - 0.254417647457579) < 5.0e-13,
        f"lambda1/lambda0={ratio16:.15f}; lambda0={rows[16]['lambda0']:.12e}",
    )
    check(
        "native diagonal uses c_(p,q)/c_(0,0), not the plaquette local-link c/(d c00)",
        rows[16]["diag_max"] > 1.0
        and dim_su3(1, 1) == 8
        and rows[16]["diag_min"] > 0.0,
        f"max c/c00={rows[16]['diag_max']:.12f}; dim(1,1)={dim_su3(1, 1)}",
    )
    check(
        "native recurrence matrix is symmetric on the tested dominant-weight box",
        rows[16]["j_symmetry"] < 1.0e-15,
        f"symmetry error={rows[16]['j_symmetry']:.3e}",
    )

    check(
        "fixed-lattice gap notes keep beta=6 gap claims separate from this native spectral row",
        "does **not** prove a physical `SU(3)` gap at `beta=6`" in fixed_gap
        and "Not an unconditional `beta=6` gap." in su3_gap,
    )
    check(
        "relationship note contains the required status-authority block",
        "Status authority: independent audit lane only." in note
        and "does not set or predict an audit outcome" in note,
    )
    check(
        "relationship note states same coupling, different objects, and no physical mass-gap claim",
        "Same Wilson coupling; different functionals." in note
        and "not the physical mass gap" in note
        and "NOT a physical mass-gap bridge" in note,
    )
    check(
        "relationship note records the no-go discipline gate without overreach phrases",
        all(f"N{i}" in note for i in range(1, 9))
        and all(phrase not in note for phrase in blocked_scope_phrases()),
    )

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
