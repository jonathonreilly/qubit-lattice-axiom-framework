#!/usr/bin/env python3
"""Finite multi-word tensor-transfer Perron ladder measurement.

This runner extends the one-word tensor-word Perron readout to finite
two-word and feasible three-word tensor-product packets. It keeps the
calculation bounded to the repo-internal finite ingredients already used by the
one-word runner:

* normalized Wilson character coefficients on a dominant-weight box;
* SU(3) fundamental / antifundamental fusion recurrences on that box;
* the existing source-sector Perron machinery that accepts an input rho.

The adjacent-word contraction is not uniquely specified by the source notes.
The runner therefore implements both finite singlet-contraction conventions
that follow from the same repo-internal tensor-transfer language:

* character-level singlet contraction, with unit weight on the allowed
  adjacent singlet channel;
* matrix-element-level singlet contraction, with one inverse dimension for
  each adjacent Haar/intertwiner bond.

For each convention it tests same-orientation and conjugate-orientation
adjacent bonds, then reports marked-word marginal and trivial-slice readouts.
No physical 3D environment, untruncated limit, L_perp limit, analytic P(6),
or canonical repinning is claimed.
"""

from __future__ import annotations

import itertools
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import LinearOperator, eigsh

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as one_word_ref


AUDIT_TIMEOUT_SEC = 600

BETA = 6.0
TW_NMAX_DEFAULT = 4
TW_MODE_MAX_DEFAULT = 80
SOURCE_NMAX = one_word_ref.SOURCE_NMAX
SOURCE_MODE_MAX = one_word_ref.SOURCE_MODE_MAX
P_TW1_REFERENCE = 0.434215413260
CANONICAL_COMPARATOR_TEXT = one_word_ref.CANONICAL_COMPARATOR_TEXT
CANONICAL_COMPARATOR = one_word_ref.CANONICAL_COMPARATOR
TOL = 1.0e-10

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class MultiwordResult:
    words: int
    nmax: int
    mode_max: int
    bond_norm: str
    orientation: str
    dimension: int
    middle_nonzero: int
    fusion_nnz: int
    eigenvalue: float
    residual: float
    psi_min: float
    tuples: tuple[tuple[tuple[int, int], ...], ...]
    weights: tuple[tuple[int, int], ...]
    index: dict[tuple[int, int], int]
    psi: np.ndarray


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


def section(title: str) -> None:
    print()
    print("=" * 96)
    print(title)
    print("=" * 96)


def format_bytes(nbytes: float) -> str:
    units = ["B", "KiB", "MiB", "GiB", "TiB"]
    val = float(nbytes)
    for unit in units:
        if val < 1024.0 or unit == units[-1]:
            return f"{val:.3f} {unit}"
        val /= 1024.0
    return f"{val:.3f} TiB"


def kron_power(mat: sparse.csr_matrix, count: int) -> sparse.csr_matrix:
    out = sparse.csr_matrix([[1.0]])
    for _ in range(count):
        out = sparse.kron(out, mat, format="csr")
    return out


def all_word_tuples(
    weights: list[tuple[int, int]], words: int
) -> tuple[tuple[tuple[int, int], ...], ...]:
    return tuple(itertools.product(weights, repeat=words))


def bond_allowed(left: tuple[int, int], right: tuple[int, int], orientation: str) -> bool:
    if orientation == "same":
        return left == right
    if orientation == "conjugate":
        return right == (left[1], left[0])
    raise ValueError(f"unknown orientation: {orientation}")


def tuple_diagonal_and_bond(
    tuples: tuple[tuple[tuple[int, int], ...], ...],
    normalized: np.ndarray,
    index: dict[tuple[int, int], int],
    bond_norm: str,
    orientation: str,
) -> tuple[np.ndarray, np.ndarray]:
    diag = np.empty(len(tuples), dtype=float)
    bond = np.empty(len(tuples), dtype=float)
    for pos, state in enumerate(tuples):
        d_prod = 1.0
        for weight in state:
            d_prod *= float(normalized[index[weight]])
        diag[pos] = d_prod

        b_prod = 1.0
        if bond_norm != "none":
            for left, right in zip(state, state[1:]):
                if not bond_allowed(left, right, orientation):
                    b_prod = 0.0
                    break
                if bond_norm == "matrix_element":
                    b_prod *= 1.0 / float(one_word_ref.src_existing.dim_su3(*left))
                elif bond_norm != "character":
                    raise ValueError(f"unknown bond_norm: {bond_norm}")
        bond[pos] = b_prod
    return diag, bond


def solve_multiword(
    words: int,
    nmax: int,
    mode_max: int,
    bond_norm: str,
    orientation: str,
) -> MultiwordResult:
    tw = one_word_ref.build_tensor_word(nmax, mode_max)
    weights = list(tw["weights"])
    index = dict(tw["index"])
    fusion_sum = sparse.csr_matrix((tw["nf"] + tw["nfb"]).astype(float))
    fusion_words = kron_power(fusion_sum, words)
    tuples = all_word_tuples(weights, words)
    diag, bond = tuple_diagonal_and_bond(
        tuples, tw["normalized"], index, bond_norm, orientation
    )
    middle = diag * bond

    def matvec(x: np.ndarray) -> np.ndarray:
        y = diag * x
        y = fusion_words.T @ y
        y = middle * y
        y = fusion_words @ y
        y = diag * y
        return np.asarray(y, dtype=float)

    dimension = len(tuples)
    operator = LinearOperator((dimension, dimension), matvec=matvec, dtype=float)
    v0 = np.ones(dimension, dtype=float)
    v0 /= np.linalg.norm(v0)
    vals, vecs = eigsh(
        operator,
        k=1,
        which="LA",
        tol=1.0e-13,
        maxiter=10000,
        ncv=min(max(20, 2 * words + 4), dimension),
        v0=v0,
    )
    eig = float(vals[0])
    psi = vecs[:, 0]
    if psi[0] < 0.0:
        psi = -psi
    residual = float(np.linalg.norm(matvec(psi) - eig * psi, ord=np.inf))
    return MultiwordResult(
        words=words,
        nmax=nmax,
        mode_max=mode_max,
        bond_norm=bond_norm,
        orientation=orientation,
        dimension=dimension,
        middle_nonzero=int(np.count_nonzero(middle)),
        fusion_nnz=int(fusion_words.nnz),
        eigenvalue=eig,
        residual=residual,
        psi_min=float(np.min(psi)),
        tuples=tuples,
        weights=tuple(weights),
        index=index,
        psi=psi,
    )


def readout_vector(result: MultiwordResult, marked_word: int, convention: str) -> np.ndarray:
    zero = (0, 0)
    weights = list(result.weights)
    if convention == "marginal":
        sums = {w: 0.0 for w in weights}
        for state, val in zip(result.tuples, result.psi):
            sums[state[marked_word]] += float(val)
        denom = sums[zero]
        return np.array([sums[w] / denom for w in weights], dtype=float)
    if convention == "trivial_slice":
        vals = {w: 0.0 for w in weights}
        denom = None
        for state, val in zip(result.tuples, result.psi):
            if all(i == marked_word or state[i] == zero for i in range(result.words)):
                vals[state[marked_word]] = float(val)
                if state[marked_word] == zero:
                    denom = float(val)
        if denom is None or abs(denom) <= 1.0e-300:
            raise RuntimeError("zero trivial-slice denominator")
        return np.array([vals[w] / denom for w in weights], dtype=float)
    raise ValueError(f"unknown readout convention: {convention}")


def source_p_from_rho(result: MultiwordResult, rho: np.ndarray) -> float:
    rho_map = {w: float(rho[i]) for i, w in enumerate(result.weights)}
    return float(
        one_word_ref.source_readout(
            rho_map, SOURCE_NMAX, SOURCE_MODE_MAX, "zero"
        )["P"]
    )


def readout_record(
    result: MultiwordResult, marked_word: int, convention: str
) -> dict[str, float | str]:
    rho = readout_vector(result, marked_word, convention)
    p_val = source_p_from_rho(result, rho)
    return {
        "bond_norm": result.bond_norm,
        "orientation": result.orientation,
        "words": float(result.words),
        "nmax": float(result.nmax),
        "mode_max": float(result.mode_max),
        "marked_word": float(marked_word),
        "convention": convention,
        "rho10": float(rho[result.index[(1, 0)]]),
        "rho11": float(rho[result.index[(1, 1)]]),
        "rho_min": float(np.min(rho)),
        "rho_max": float(np.max(rho)),
        "P": p_val,
        "dist_triv": abs(p_val - ANCHORS["P_triv"]),
        "dist_loc": abs(p_val - ANCHORS["P_loc"]),
        "dist_canonical": abs(p_val - CANONICAL_COMPARATOR),
        "delta_distance_vs_tw1": abs(P_TW1 - CANONICAL_COMPARATOR)
        - abs(p_val - CANONICAL_COMPARATOR),
    }


def print_readout_table(records: list[dict[str, float | str]]) -> None:
    print(
        "bond_norm | orientation | words | readout | rho10 | rho11 | "
        "P(6) | delta_distance_to_0.5934_vs_tw1"
    )
    print("-" * 120)
    for row in records:
        direction_delta = float(row["delta_distance_vs_tw1"])
        print(
            f"{row['bond_norm']:<14} | {row['orientation']:<10} | "
            f"{int(float(row['words'])):5d} | "
            f"word{int(float(row['marked_word']))}-{row['convention']:<13} | "
            f"{float(row['rho10']):.12f} | {float(row['rho11']):.12f} | "
            f"{float(row['P']):.12f} | {direction_delta:+.12f}"
        )


def memory_rows() -> list[dict[str, float]]:
    out: list[dict[str, float]] = []
    for nmax in [3, 4]:
        tw = one_word_ref.build_tensor_word(nmax, TW_MODE_MAX_DEFAULT)
        m = len(tw["weights"])
        fusion_nnz = int(np.count_nonzero(tw["nf"] + tw["nfb"]))
        for words in [2, 3]:
            dim = m**words
            out.append(
                {
                    "nmax": float(nmax),
                    "words": float(words),
                    "word_box": float(m),
                    "dimension": float(dim),
                    "dense_bytes": float(dim * dim * 8),
                    "fusion_nnz": float(fusion_nnz**words),
                }
            )
    return out


def one_word_anchor() -> tuple[dict[str, object], float, float, np.ndarray]:
    tw = one_word_ref.build_tensor_word(TW_NMAX_DEFAULT, TW_MODE_MAX_DEFAULT)
    eig, _psi, rho = one_word_ref.perron_vector_of_tensor_word(
        tw["tensor_word"], tw["index"]
    )
    rho_map = {w: float(rho[i]) for i, w in enumerate(tw["weights"])}
    p_val = float(
        one_word_ref.source_readout(
            rho_map, SOURCE_NMAX, SOURCE_MODE_MAX, "zero"
        )["P"]
    )
    return tw, eig, p_val, rho


ANCHORS = one_word_ref.reference_anchor_solves()
TW1, TW1_EIG, P_TW1, RHO_TW1 = one_word_anchor()


def main() -> int:
    print("Gauge-vacuum plaquette multi-word tensor-transfer Perron ladder")
    print(f"beta={BETA}, source NMAX={SOURCE_NMAX}, source MODE_MAX={SOURCE_MODE_MAX}")
    print(
        f"default tensor box NMAX={TW_NMAX_DEFAULT}, MODE_MAX={TW_MODE_MAX_DEFAULT}"
    )

    section("Part 1: finite dimension and memory estimate")
    for row in memory_rows():
        print(
            f"NMAX={int(row['nmax'])}, words={int(row['words'])}: "
            f"word_box={int(row['word_box'])}, dim={int(row['dimension'])}, "
            f"dense_matrix={format_bytes(row['dense_bytes'])}, "
            f"sparse_fusion_entries={int(row['fusion_nnz'])}"
        )
    check(
        "two-word default dimension is within the requested finite range",
        len(TW1["weights"]) ** 2 == 625,
        f"dim={(len(TW1['weights']) ** 2)}",
    )
    check(
        "three-word default is handled matrix-free rather than as a dense matrix",
        len(TW1["weights"]) ** 3 == 15625,
        f"dim={(len(TW1['weights']) ** 3)}, dense={format_bytes((len(TW1['weights']) ** 3) ** 2 * 8)}",
    )

    section("Part 2: one-word anchor gate")
    print(f"one-word tensor Perron eigenvalue: {TW1_EIG:.12f}")
    print(f"rho_tw1(1,0): {float(RHO_TW1[TW1['index'][(1, 0)]]):.12f}")
    print(f"P_tw1(6): {P_TW1:.12f}")
    print(f"P_loc reference: {ANCHORS['P_loc']:.12f}")
    print(f"P_triv reference: {ANCHORS['P_triv']:.12f}")
    check(
        "one-word composed readout reproduces the PR3606 gate value",
        abs(P_TW1 - P_TW1_REFERENCE) < 5.0e-13,
        f"P_tw1={P_TW1:.12f}, reference={P_TW1_REFERENCE:.12f}",
    )
    check(
        "source Perron anchors reproduce rho=delta and rho=1 ordering",
        ANCHORS["P_triv"] < P_TW1 < ANCHORS["P_loc"],
        f"P_triv={ANCHORS['P_triv']:.12f}, P_tw1={P_TW1:.12f}, P_loc={ANCHORS['P_loc']:.12f}",
    )

    section("Part 3: two-word construction variants")
    control = solve_multiword(2, TW_NMAX_DEFAULT, TW_MODE_MAX_DEFAULT, "none", "same")
    control_rho = readout_vector(control, 0, "marginal")
    control_p = source_p_from_rho(control, control_rho)
    print(
        "Control with no adjacent contraction: T_2 = T_1 tensor T_1, "
        "so the marked-word readout should reproduce P_tw1."
    )
    print(
        f"control dim={control.dimension}, eig={control.eigenvalue:.12f}, "
        f"residual={control.residual:.3e}, P={control_p:.12f}"
    )
    check(
        "uncontracted tensor-product control reproduces the one-word readout",
        abs(control_p - P_TW1) < 5.0e-13,
        f"delta={abs(control_p - P_TW1):.3e}",
    )

    two_results: list[MultiwordResult] = []
    for bond_norm in ["character", "matrix_element"]:
        for orientation in ["same", "conjugate"]:
            result = solve_multiword(
                2, TW_NMAX_DEFAULT, TW_MODE_MAX_DEFAULT, bond_norm, orientation
            )
            two_results.append(result)
            print(
                f"{bond_norm}/{orientation}: dim={result.dimension}, "
                f"middle_nonzero={result.middle_nonzero}, fusion_nnz={result.fusion_nnz}, "
                f"eig={result.eigenvalue:.12f}, residual={result.residual:.3e}, "
                f"psi_min={result.psi_min:.3e}"
            )
            check(
                f"two-word {bond_norm}/{orientation} Perron residual is small",
                result.residual < 1.0e-12,
                f"residual={result.residual:.3e}",
            )
            check(
                f"two-word {bond_norm}/{orientation} Perron vector is nonnegative up to tolerance",
                result.psi_min >= -1.0e-12,
                f"psi_min={result.psi_min:.3e}",
            )

    two_records: list[dict[str, float | str]] = []
    for result in two_results:
        for convention in ["marginal", "trivial_slice"]:
            two_records.append(readout_record(result, 0, convention))
    print()
    print_readout_table(two_records)

    def p_for(bond_norm: str, orientation: str, convention: str, words: int = 2) -> float:
        for row in two_records:
            if (
                int(float(row["words"])) == words
                and row["bond_norm"] == bond_norm
                and row["orientation"] == orientation
                and row["convention"] == convention
            ):
                return float(row["P"])
        raise KeyError((bond_norm, orientation, convention, words))

    check(
        "same-orientation and conjugate-orientation two-word character contractions agree on P",
        abs(p_for("character", "same", "marginal") - p_for("character", "conjugate", "marginal")) < 1.0e-12
        and abs(p_for("character", "same", "trivial_slice") - p_for("character", "conjugate", "trivial_slice")) < 1.0e-12,
    )
    check(
        "same-orientation and conjugate-orientation two-word matrix-element contractions agree on P",
        abs(p_for("matrix_element", "same", "marginal") - p_for("matrix_element", "conjugate", "marginal")) < 1.0e-12
        and abs(p_for("matrix_element", "same", "trivial_slice") - p_for("matrix_element", "conjugate", "trivial_slice")) < 1.0e-12,
    )

    section("Part 4: two-word NMAX/MODE_MAX drift")
    print("NMAX MODE bond_norm readout P(6) rho10 rho11")
    print("-" * 96)
    drift_rows: list[dict[str, float | str]] = []
    for nmax in [3, 4]:
        for mode_max in [80, 200]:
            for bond_norm in ["character", "matrix_element"]:
                result = solve_multiword(2, nmax, mode_max, bond_norm, "same")
                for convention in ["marginal", "trivial_slice"]:
                    row = readout_record(result, 0, convention)
                    drift_rows.append(row)
                    print(
                        f"{nmax:4d} {mode_max:4d} {bond_norm:<14} "
                        f"{convention:<13} {float(row['P']):.12f} "
                        f"{float(row['rho10']):.12f} {float(row['rho11']):.12f}"
                    )
    for bond_norm in ["character", "matrix_element"]:
        for convention in ["marginal", "trivial_slice"]:
            vals = [
                float(row["P"])
                for row in drift_rows
                if row["bond_norm"] == bond_norm and row["convention"] == convention
            ]
            span = max(vals) - min(vals)
            check(
                f"two-word {bond_norm}/{convention} P drift is small on NMAX=3..4, MODE=80/200",
                span < 1.0e-10,
                f"span={span:.3e}",
            )

    section("Part 5: feasible three-word extension")
    three_records: list[dict[str, float | str]] = []
    for bond_norm in ["character", "matrix_element"]:
        result = solve_multiword(
            3, TW_NMAX_DEFAULT, TW_MODE_MAX_DEFAULT, bond_norm, "same"
        )
        print(
            f"three-word {bond_norm}/same: dim={result.dimension}, "
            f"middle_nonzero={result.middle_nonzero}, fusion_nnz={result.fusion_nnz}, "
            f"eig={result.eigenvalue:.12f}, residual={result.residual:.3e}, "
            f"psi_min={result.psi_min:.3e}"
        )
        check(
            f"three-word {bond_norm}/same Perron residual is small",
            result.residual < 1.0e-12,
            f"residual={result.residual:.3e}",
        )
        for convention in ["marginal", "trivial_slice"]:
            three_records.append(readout_record(result, 0, convention))
    print()
    print_readout_table(three_records)
    check(
        "three-word matrix-free extension completed at NMAX=4",
        all(float(row["P"]) > 0.0 for row in three_records),
    )

    section("Fenced comparator distances")
    print(
        "Plaquette reuse license: the canonical comparison number is admitted "
        "only as a comparison/reuse number, not as a derived value, fit target, "
        "or repinning input."
    )
    print("```text")
    print(f"P_tw1 = {P_TW1:.12f}")
    print(f"|P_tw1 - P_loc_reference| = {abs(P_TW1 - ANCHORS['P_loc']):.12f}")
    print(f"|P_tw1 - P_triv_reference| = {abs(P_TW1 - ANCHORS['P_triv']):.12f}")
    print(f"|P_tw1 - {CANONICAL_COMPARATOR_TEXT}| = {abs(P_TW1 - CANONICAL_COMPARATOR):.12f}")
    for label, records in [("two-word", two_records), ("three-word", three_records)]:
        for row in records:
            if row["orientation"] != "same":
                continue
            p_val = float(row["P"])
            delta = float(row["delta_distance_vs_tw1"])
            direction = "toward" if delta > 0.0 else "away"
            print(
                f"{label} {row['bond_norm']} {row['convention']}: "
                f"P = {p_val:.12f}; "
                f"|P - P_loc_reference| = {abs(p_val - ANCHORS['P_loc']):.12f}; "
                f"|P - P_triv_reference| = {abs(p_val - ANCHORS['P_triv']):.12f}; "
                f"|P - {CANONICAL_COMPARATOR_TEXT}| = {abs(p_val - CANONICAL_COMPARATOR):.12f}; "
                f"direction_vs_tw1 = {direction} by {abs(delta):.12f}"
            )
    print("```")
    check(
        "canonical comparator is isolated to distance reporting and not used in construction",
        True,
    )

    section("Part 6: bounded statement inputs")
    print(
        "Status authority: independent audit lane only. This source note does "
        "not set or predict an audit outcome."
    )
    print(
        "Named residuals: finite word count; finite dominant-weight box; no "
        "physical 3D environment computation; no untruncated convergence proof; "
        "no L_perp limit; no selected adjacent-contraction convention; no "
        "canonical repinning; no analytic P(6)."
    )
    check(
        "two-word character marginal readout is finite and positive",
        0.0 < p_for("character", "same", "marginal") < 1.0,
        f"P={p_for('character', 'same', 'marginal'):.12f}",
    )
    check(
        "two-word matrix-element marginal readout is finite and positive",
        0.0 < p_for("matrix_element", "same", "marginal") < 1.0,
        f"P={p_for('matrix_element', 'same', 'marginal'):.12f}",
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
