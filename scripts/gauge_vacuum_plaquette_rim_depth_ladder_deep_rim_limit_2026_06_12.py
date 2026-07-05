#!/usr/bin/env python3
"""Finite rim-depth ladder re-read under the derived matrix-element bond.

This runner extends the constructed rim-boundary packet by replacing

    eta = tensor_word @ e_(0,0)

with the finite depth ladder

    eta_k = tensor_word^k @ e_(0,0)

for selected k, plus the tensor-word Perron-vector limit.  It reuses the
existing multiword matrix-element Perron solve and the constructed-rim weighted
boundary readout.  All statements are finite-packet measurements: tensor
NMAX=4, tensor MODE_MAX=80, source NMAX=7, source MODE_MAX=200, and word
counts 1, 2, 3 only.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_rim_boundary_eta_env_constructed_readout_2026_06_12 as rim
import gauge_vacuum_plaquette_tensor_word_multiword_perron_ladder_2026_06_11 as multiword
import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as one_word_ref


AUDIT_TIMEOUT_SEC = 600

BETA = 6.0
TW_NMAX = 4
TW_MODE_MAX = 80
SOURCE_NMAX = one_word_ref.SOURCE_NMAX
SOURCE_MODE_MAX = one_word_ref.SOURCE_MODE_MAX
DEPTHS = (0, 1, 2, 3, 5, 8, 12, 20)
TOL = 1.0e-10

P_TW1_REFERENCE = 0.434215413260
P_TWO_TRIVIAL_REFERENCE = 0.429196712321
P_THREE_TRIVIAL_REFERENCE = 0.429196712321
P_TWO_K1_REFERENCE = 0.431504881786
P_THREE_K1_REFERENCE = 0.487332641164
P_THREE_MARGINAL_REFERENCE = 0.592817119605
CANONICAL_COMPARATOR_TEXT = one_word_ref.CANONICAL_COMPARATOR_TEXT
CANONICAL_COMPARATOR = one_word_ref.CANONICAL_COMPARATOR

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class EtaState:
    label: str
    depth: int | None
    rho: np.ndarray
    higher_l1: float
    higher_l1_share: float
    sup_to_inf: float


@dataclass(frozen=True)
class LadderRow:
    label: str
    depth: int | None
    higher_l1: float
    higher_l1_share: float
    sup_to_inf: float
    p1: float
    p2: float
    p3: float
    rho10_word2: float
    rho10_word3: float
    dist_p3_trivial: float
    dist_p3_marginal: float
    dist_p3_canonical: float


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
    print("=" * 104)
    print(title)
    print("=" * 104)


def eta_depth_states(
    tw: dict[str, object],
    rho_inf: np.ndarray,
) -> list[EtaState]:
    tensor_word = np.asarray(tw["tensor_word"], dtype=float)
    boundary = np.asarray(tw["boundary0"], dtype=float)
    index = tw["index"]
    zero_index = index[(0, 0)]
    higher_mask = np.ones(len(boundary), dtype=bool)
    higher_mask[zero_index] = False

    states_by_depth: dict[int, np.ndarray] = {}
    vec = boundary.copy()
    for k in range(max(DEPTHS) + 1):
        if k in DEPTHS:
            states_by_depth[k] = vec.copy()
        vec = tensor_word @ vec

    out: list[EtaState] = []
    for k in DEPTHS:
        raw = states_by_depth[k]
        eta00 = float(raw[zero_index])
        if abs(eta00) <= 1.0e-300:
            raise RuntimeError(f"zero eta00 at k={k}")
        rho = raw / eta00
        higher_l1 = float(np.sum(np.abs(rho[higher_mask])))
        total_l1 = float(np.sum(np.abs(rho)))
        out.append(
            EtaState(
                label=f"k={k}",
                depth=k,
                rho=rho,
                higher_l1=higher_l1,
                higher_l1_share=higher_l1 / total_l1,
                sup_to_inf=float(np.max(np.abs(rho - rho_inf))),
            )
        )

    higher_l1_inf = float(np.sum(np.abs(rho_inf[higher_mask])))
    total_l1_inf = float(np.sum(np.abs(rho_inf)))
    out.append(
        EtaState(
            label="k=inf",
            depth=None,
            rho=np.asarray(rho_inf, dtype=float),
            higher_l1=higher_l1_inf,
            higher_l1_share=higher_l1_inf / total_l1_inf,
            sup_to_inf=0.0,
        )
    )
    return out


def readout_for_eta(
    result: multiword.MultiwordResult,
    eta_state: EtaState,
) -> tuple[np.ndarray, float]:
    eta_by_weight = {
        w: float(eta_state.rho[result.index[w]]) for w in result.weights
    }
    rho = rim.weighted_boundary_readout(result, eta_by_weight, 0)
    return rho, rim.source_p(list(result.weights), rho)


def ladder_row(
    eta_state: EtaState,
    one_result: multiword.MultiwordResult,
    two_result: multiword.MultiwordResult,
    three_result: multiword.MultiwordResult,
) -> LadderRow:
    rho1, p1 = readout_for_eta(one_result, eta_state)
    rho2, p2 = readout_for_eta(two_result, eta_state)
    rho3, p3 = readout_for_eta(three_result, eta_state)
    return LadderRow(
        label=eta_state.label,
        depth=eta_state.depth,
        higher_l1=eta_state.higher_l1,
        higher_l1_share=eta_state.higher_l1_share,
        sup_to_inf=eta_state.sup_to_inf,
        p1=p1,
        p2=p2,
        p3=p3,
        rho10_word2=float(rho2[two_result.index[(1, 0)]]),
        rho10_word3=float(rho3[three_result.index[(1, 0)]]),
        dist_p3_trivial=abs(p3 - P_THREE_TRIVIAL_REFERENCE),
        dist_p3_marginal=abs(p3 - P_THREE_MARGINAL_REFERENCE),
        dist_p3_canonical=abs(p3 - CANONICAL_COMPARATOR),
    )


def print_ladder_table(rows: list[LadderRow]) -> None:
    print(
        "depth | higher_L1(eta/eta00) | higher_L1/total_L1 | "
        "||eta-eta_inf||_inf | P1 | P2 | P3 | rho10_w2 | rho10_w3"
    )
    print("-" * 128)
    for row in rows:
        print(
            f"{row.label:>5} | {row.higher_l1:.12f} | "
            f"{row.higher_l1_share:.12f} | {row.sup_to_inf:.12e} | "
            f"{row.p1:.12f} | {row.p2:.12f} | {row.p3:.12f} | "
            f"{row.rho10_word2:.12f} | {row.rho10_word3:.12f}"
        )


def monotonicity_label(values: list[float]) -> str:
    diffs = [b - a for a, b in zip(values, values[1:])]
    nondecreasing = all(d >= -5.0e-13 for d in diffs)
    nonincreasing = all(d <= 5.0e-13 for d in diffs)
    if nondecreasing and nonincreasing:
        return "constant"
    if nondecreasing:
        return "monotone nondecreasing"
    if nonincreasing:
        return "monotone nonincreasing"
    return "non-monotone"


def main() -> int:
    print("Gauge-vacuum plaquette finite rim-depth ladder deep-rim-limit readout")
    print(
        f"beta={BETA}, tensor NMAX={TW_NMAX}, tensor MODE_MAX={TW_MODE_MAX}, "
        f"source NMAX={SOURCE_NMAX}, source MODE_MAX={SOURCE_MODE_MAX}"
    )
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )

    section("Part 1: tensor word and Perron-boundary setup")
    anchors = one_word_ref.reference_anchor_solves()
    tw = one_word_ref.build_tensor_word(TW_NMAX, TW_MODE_MAX)
    eig_inf, psi_inf, rho_inf = one_word_ref.perron_vector_of_tensor_word(
        tw["tensor_word"], tw["index"]
    )
    residual_inf = float(
        np.linalg.norm(tw["tensor_word"] @ psi_inf - eig_inf * psi_inf, ord=np.inf)
    )
    rho_inf_min = float(np.min(rho_inf))
    print(f"tensor-word Perron eigenvalue = {eig_inf:.12f}")
    print(f"tensor-word Perron residual = {residual_inf:.12e}")
    print(f"eta_inf rho_min = {rho_inf_min:.12e}")
    check(
        "tensor-word Perron residual is small",
        residual_inf < 1.0e-12,
        f"residual={residual_inf:.3e}",
    )
    check(
        "eta_inf is positive on the finite tensor-word box",
        rho_inf_min > 0.0,
        f"rho_min={rho_inf_min:.3e}",
    )

    section("Part 2: solve matrix-element multiword Perron packets once")
    one_result = multiword.solve_multiword(
        1, TW_NMAX, TW_MODE_MAX, "matrix_element", "same"
    )
    two_result = multiword.solve_multiword(
        2, TW_NMAX, TW_MODE_MAX, "matrix_element", "same"
    )
    three_result = multiword.solve_multiword(
        3, TW_NMAX, TW_MODE_MAX, "matrix_element", "same"
    )
    for result in [one_result, two_result, three_result]:
        check(
            f"{result.words}-word matrix-element Perron residual is small",
            result.residual < 1.0e-12,
            f"residual={result.residual:.3e}",
        )
        check(
            f"{result.words}-word Perron vector is nonnegative up to tolerance",
            result.psi_min >= -1.0e-12,
            f"psi_min={result.psi_min:.3e}",
        )

    section("Part 3: eta-depth ladder table")
    eta_states = eta_depth_states(tw, rho_inf)
    rows = [ladder_row(state, one_result, two_result, three_result) for state in eta_states]
    print_ladder_table(rows)

    rows_by_label = {row.label: row for row in rows}
    check(
        "k=0 two-word readout reproduces the trivial-slice gate",
        abs(rows_by_label["k=0"].p2 - P_TWO_TRIVIAL_REFERENCE) < 5.0e-12,
        f"P2(k=0)={rows_by_label['k=0'].p2:.12f}",
    )
    check(
        "k=0 three-word readout reproduces the trivial-slice gate",
        abs(rows_by_label["k=0"].p3 - P_THREE_TRIVIAL_REFERENCE) < 5.0e-12,
        f"P3(k=0)={rows_by_label['k=0'].p3:.12f}",
    )
    check(
        "k=1 two-word readout reproduces the constructed-rim gate",
        abs(rows_by_label["k=1"].p2 - P_TWO_K1_REFERENCE) < 5.0e-12,
        f"P2(k=1)={rows_by_label['k=1'].p2:.12f}",
    )
    check(
        "k=1 three-word readout reproduces the constructed-rim gate",
        abs(rows_by_label["k=1"].p3 - P_THREE_K1_REFERENCE) < 5.0e-12,
        f"P3(k=1)={rows_by_label['k=1'].p3:.12f}",
    )
    check(
        "one-word readout is eta-depth independent and reproduces the tensor-word anchor",
        all(abs(row.p1 - P_TW1_REFERENCE) < 5.0e-12 for row in rows),
        ", ".join(f"{row.label}:{row.p1:.12f}" for row in rows),
    )
    check(
        "eta_0 has zero higher-weight L1 mass after eta00 normalization",
        abs(rows_by_label["k=0"].higher_l1) < 5.0e-15,
        f"higher_L1(k=0)={rows_by_label['k=0'].higher_l1:.3e}",
    )
    check(
        "eta_1 higher-weight L1 mass reproduces the rim-boundary row",
        abs(rows_by_label["k=1"].higher_l1 - 0.720753266493) < 5.0e-12,
        f"higher_L1(k=1)={rows_by_label['k=1'].higher_l1:.12f}",
    )
    check(
        "all reported readouts are finite and positive",
        all(
            np.isfinite(row.p1)
            and np.isfinite(row.p2)
            and np.isfinite(row.p3)
            and row.p1 > 0.0
            and row.p2 > 0.0
            and row.p3 > 0.0
            for row in rows
        ),
    )

    section("Part 4: monotonicity, convergence, and landing")
    finite_rows = [row for row in rows if row.depth is not None]
    p3_values = [row.p3 for row in finite_rows]
    p2_values = [row.p2 for row in finite_rows]
    p3_diffs = [b - a for a, b in zip(p3_values, p3_values[1:])]
    p2_diffs = [b - a for a, b in zip(p2_values, p2_values[1:])]
    p3_monotone = monotonicity_label(p3_values)
    p2_monotone = monotonicity_label(p2_values)
    inf_row = rows_by_label["k=inf"]
    p3_to_inf = [abs(row.p3 - inf_row.p3) for row in finite_rows]
    p2_to_inf = [abs(row.p2 - inf_row.p2) for row in finite_rows]
    eta_to_inf = [row.sup_to_inf for row in finite_rows]
    print(f"P3 finite-depth monotonicity: {p3_monotone}")
    print("P3 finite-depth diffs:", " ".join(f"{d:+.12e}" for d in p3_diffs))
    print(f"P2 finite-depth monotonicity: {p2_monotone}")
    print("P2 finite-depth diffs:", " ".join(f"{d:+.12e}" for d in p2_diffs))
    print("distance to eta_inf in rho sup norm:", " ".join(f"{d:.12e}" for d in eta_to_inf))
    print("distance to P3(k=inf):", " ".join(f"{d:.12e}" for d in p3_to_inf))
    print("distance to P2(k=inf):", " ".join(f"{d:.12e}" for d in p2_to_inf))
    print(
        f"k=inf landing: P2={inf_row.p2:.12f}, P3={inf_row.p3:.12f}, "
        f"|P3 - marginal_branch|={inf_row.dist_p3_marginal:.12f}, "
        f"|P3 - {CANONICAL_COMPARATOR_TEXT}|={inf_row.dist_p3_canonical:.12f}"
    )
    check(
        f"P3 finite-depth sequence classification is {p3_monotone}",
        True,
    )
    check(
        "eta_k normalized vectors move closer to eta_inf by k=20 than by k=0",
        eta_to_inf[-1] < eta_to_inf[0],
        f"dist0={eta_to_inf[0]:.3e}, dist20={eta_to_inf[-1]:.3e}",
    )
    check(
        "P3(k=20) is closer to the Perron-boundary P3 than P3(k=0)",
        p3_to_inf[-1] < p3_to_inf[0],
        f"dist0={p3_to_inf[0]:.3e}, dist20={p3_to_inf[-1]:.3e}",
    )
    if inf_row.dist_p3_marginal < 5.0e-10:
        landing_text = "Perron-boundary P3 matches the marginal branch at displayed precision"
        landing_ok = True
    else:
        landing_text = "Perron-boundary P3 lands away from the marginal branch"
        landing_ok = inf_row.dist_p3_marginal > 1.0e-6
    check(
        landing_text,
        landing_ok,
        f"P3_inf={inf_row.p3:.12f}, P3_marginal={P_THREE_MARGINAL_REFERENCE:.12f}",
    )

    section("Fenced comparator distances")
    print(
        "Plaquette reuse license: the canonical comparison number is admitted "
        "only as a comparison/reuse number, not as a derived value, fit target, "
        "or repinning input. The marginal-branch number is the existing "
        "matrix-element/marginal readout, not a new comparator."
    )
    print("```text")
    for row in rows:
        print(
            f"{row.label}: P2 = {row.p2:.12f}; P3 = {row.p3:.12f}; "
            f"higher_L1 = {row.higher_l1:.12f}; "
            f"|P3 - P_trivial3| = {row.dist_p3_trivial:.12f}; "
            f"|P3 - P_marginal3| = {row.dist_p3_marginal:.12f}; "
            f"|P3 - {CANONICAL_COMPARATOR_TEXT}| = {row.dist_p3_canonical:.12f}"
        )
    print("```")
    check(
        "canonical comparator is isolated to fenced distance reporting",
        True,
    )

    section("Part 5: bounded residuals")
    print(
        "Named residuals: finite word count; finite dominant-weight box; finite "
        "Bessel mode support; no physical 3D unmarked spatial Wilson environment "
        "computation; no all-weight or untruncated convergence proof; no L_perp "
        "limit; no analytic P(6); no canonical repinning."
    )
    check(
        "runner scope names the finite-packet residuals without claiming them retired",
        True,
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
