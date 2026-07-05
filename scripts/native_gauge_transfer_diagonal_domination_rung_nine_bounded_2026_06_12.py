#!/usr/bin/env python3
"""Rung-nine diagonal-domination obstruction runner.

This runner checks the source-side obstruction note for W86. It derives the
available saddle-derivative identities, recomputes finite Hellmann witness
rows, and verifies that fitted constants are not promoted to proof inputs.
"""

from __future__ import annotations

from math import isclose, sqrt
from pathlib import Path
import sys

import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import native_gauge_transfer_block_hellmann_monotonicity_rung_eight_bounded_2026_06_12 as h8


AUDIT_TIMEOUT_SEC = 540

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md"
)
BLOCK_HELLMANN_NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_BLOCK_HELLMANN_MONOTONICITY_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md"
)
CHARACTER_NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md"
)
OP_REMAINDER_NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md"
)
WILSON_TO_SADDLE_NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_WILSON_TO_SADDLE_UNIFORM_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md"
)

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


def q_form(x: float, y: float) -> float:
    return x * x + x * y + y * y


def scaled_l_operator_on_poly(x: float, y: float) -> float:
    # For f=x^2+x*y+2y^2, f_xx=2, f_xy=1, f_yy=4.
    return (2.0 - 1.0 + 4.0) / 3.0


def poly(x: float, y: float) -> float:
    return x * x + x * y + 2.0 * y * y


def j_average_scaled_poly(beta: int, p: int, q: int) -> float:
    root = sqrt(beta)
    vals = []
    for a, b in [
        (p + 1, q),
        (p - 1, q + 1),
        (p, q - 1),
        (p, q + 1),
        (p + 1, q - 1),
        (p - 1, q),
    ]:
        vals.append(poly(a / root, b / root))
    return sum(vals) / 6.0


def finite_witness_rows() -> list[tuple[int, int, float, float, float, float]]:
    rows = []
    for beta, shell in [(20, 12), (30, 16), (40, 18), (50, 22)]:
        row = h8.hellmann_row(float(beta), shell)
        c_j = beta * (-row.jdiff)
        c_d = beta * row.ddiff
        rows.append((beta, shell, c_j, c_d, c_j - c_d, c_d / c_j))
    return rows


def main() -> int:
    print("Native gauge-transfer diagonal-domination obstruction runner")
    print("Finite rows are witnesses; no fitted c_J or c_D is promoted.")
    print()

    text = NOTE_PATH.read_text(encoding="utf-8")
    text_ws = " ".join(text.split())
    lower = text.lower()
    block_note = BLOCK_HELLMANN_NOTE_PATH.read_text(encoding="utf-8")
    character_note = CHARACTER_NOTE_PATH.read_text(encoding="utf-8")
    op_note = OP_REMAINDER_NOTE_PATH.read_text(encoding="utf-8")
    wilson_note = WILSON_TO_SADDLE_NOTE_PATH.read_text(encoding="utf-8")

    check(
        "note carries the exact required status-authority sentence",
        "Status authority: independent audit lane only. This source note does not set or predict an audit outcome."
        in text,
    )
    check(
        "note declares canonical open-gate claim type",
        "**Claim type:** open_gate" in text and "**Type:** source-side obstruction note" in text,
    )
    check(
        "note refuses imports and fitted constants",
        "No literature value, new axiom, external citation, fitted selector, fitted" in text
        and "prefactor, or new comparator number is used" in text
        and "using them as fitted constants would be a value-from-target step" in text,
    )

    authority_links = [
        "[NATIVE_GAUGE_TRANSFER_BLOCK_HELLMANN_MONOTONICITY_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_BLOCK_HELLMANN_MONOTONICITY_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md)",
        "[NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md)",
        "[GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)",
        "[NATIVE_GAUGE_TRANSFER_WILSON_TO_SADDLE_UNIFORM_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_WILSON_TO_SADDLE_UNIFORM_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md)",
    ]
    check("one-hop authorities are markdown links", all(link in text for link in authority_links))
    check(
        "quote anchors match the cited authorities",
        "Thus the derivative inequality is exactly equivalent, on the finite block, to" in block_note
        and "Delta_J + Delta_D <= 0" in block_note
        and "beta^(-3/2) r_(p,q)(beta)" in op_note
        and "E_beta = exp((beta/2)(J - I))" in op_note
        and "X(W) = (1/3) Re Tr W" in character_note
        and "No source-side value of K_W(a) is derived in this note." in wilson_note,
    )
    check(
        "note avoids branch-local temp references",
        ("." + "claude/tmp") not in text and ("tmp" + "/refs") not in text,
    )
    check(
        "note states exact finite-block Delta_J and Delta_D definitions",
        "Delta_J = <v_1, J v_1> - <v_0, J v_0>" in text
        and "Delta_D = <v_1, E_beta D_beta' E_beta v_1>/lambda_1" in text,
    )
    check(
        "note derives the saddle diagonal derivative multiplier",
        "beta * r_sad_(p,q)'(beta) / r_sad_(p,q)(beta)" in text
        and "= Q(x,y) + 3(x+y) beta^(-1/2)" in text
        and "leading diagonal-derivative multiplier supplied by the saddle" in text,
    )
    check(
        "note gives formal c_J and c_D expressions without numeric promotion",
        "c_J = A_0 - A_1" in text
        and "c_D = B_1/mu_1 - B_0/mu_0" in text
        and "The authorities above do not supply closed-form `Phi_i`" in text,
    )
    check(
        "note gives both ambiguity readings",
        "Reading 1: formal saddle-spectrum reading" in text
        and "Reading 2: finite-block trend reading" in text,
    )
    check(
        "note differentiates new material from prior notes",
        "New in this note: the derivative-side saddle identity" in text
        and "Restated from the block-Hellmann rung-eight note" in text
        and "Restated from the operator-remainder rung-eight note" in text,
    )
    banned = [
        "only " + "route",
        "last " + "route",
        "exhau" + "sted",
        "closes " + "the program",
        "perma" + "nently",
        "no other " + "path",
        "closes " + "route a",
    ]
    check("note avoids overreach phrases", not any(fragment in lower for fragment in banned))

    samples = [(20, 3, 4), (50, 5, 7), (80, 8, 6)]
    max_saddle_err = 0.0
    for beta, p, q in samples:
        x = p / sqrt(beta)
        y = q / sqrt(beta)
        beta_log_deriv = 3.0 * h8.casimir_su3(p, q) / beta
        rhs = q_form(x, y) + 3.0 * (x + y) / sqrt(beta)
        max_saddle_err = max(max_saddle_err, abs(beta_log_deriv - rhs))
    check(
        "saddle derivative identity is exact on sample weights",
        max_saddle_err < 1.0e-14,
        f"max_error={max_saddle_err:.3e}",
    )

    max_j_err = 0.0
    for beta, p, q in [(25, 10, 9), (40, 12, 11), (81, 20, 17)]:
        x = p / sqrt(beta)
        y = q / sqrt(beta)
        lhs = beta * (j_average_scaled_poly(beta, p, q) - poly(x, y))
        rhs = scaled_l_operator_on_poly(x, y)
        max_j_err = max(max_j_err, abs(lhs - rhs))
    check(
        "six-neighbor Taylor expansion gives beta(J-I) -> L on interior quadratic sample",
        max_j_err < 1.0e-12,
        f"max_error={max_j_err:.3e}",
    )

    rows = finite_witness_rows()
    print("finite_exact_witness_rows")
    for beta, shell, c_j, c_d, margin, ratio in rows:
        print(
            f"  beta={beta:3d} shell={shell:2d} "
            f"CJ_wit={c_j:.12f} CD_wit={c_d:.12f} "
            f"margin={margin:.12f} ratio={ratio:.12f}"
        )
    check(
        "finite witness rows have positive C_J margin over C_D",
        all(margin > 0.0 for _beta, _shell, _cj, _cd, margin, _ratio in rows),
    )
    tight = rows[-1][-1]
    check(
        "tight beta=50 finite row remains fenced evidence only",
        0.95 < tight < 0.97
        and "The last ratio restates the known tightness signal. It is evidence" in text,
        f"beta50_ratio={tight:.12f}",
    )
    check(
        "note witness table contains recomputed beta=50 row",
        "0.845980865746" in text and "0.810590301970" in text and "0.958166236131" in text,
    )

    wrong_deriv = h8.hellmann_row(20.0, 12, derivative_scale=1.0 / 5.0)
    wrong_j_zero = h8.hellmann_row(20.0, 12, edge_scale=0.0)
    check(
        "wrong derivative recurrence scale flips the finite domination sign",
        wrong_deriv.logdiff > 0.0,
        f"logdiff={wrong_deriv.logdiff:.12f}",
    )
    check(
        "wrong source scale J=0 flips the finite domination sign on the falsifier row",
        wrong_j_zero.logdiff > 0.0,
        f"logdiff={wrong_j_zero.logdiff:.12f}",
    )

    beta = 20.0
    shell = 12
    correct_reduced = h8.ratio_from_diagonal(beta, shell, h8.saddle_diagonal(beta, shell, 3.0))
    wrong_nc = h8.ratio_from_diagonal(beta, shell, h8.saddle_diagonal(beta, shell, 2.0))
    wrong_dim_diag = np.array(
        [np.exp(-3.0 * h8.casimir_su3(p, q) / beta) for p, q in h8.weights_box(shell)],
        dtype=float,
    )
    wrong_dim = h8.ratio_from_diagonal(beta, shell, wrong_dim_diag)
    wrong_source = h8.ratio_from_diagonal(
        beta, shell, h8.saddle_diagonal(beta, shell, 3.0), edge_scale=0.0
    )
    print("reduced_falsifier_rows")
    print(f"  correct_saddle_ratio={correct_reduced:.12f}")
    print(f"  wrong_Nc2_ratio={wrong_nc:.12f}")
    print(f"  wrong_dimension_omitted_ratio={wrong_dim:.12f}")
    print(f"  wrong_source_J0_ratio={wrong_source:.12f}")
    check(
        "wrong Nc, dimension, and source normalization visibly change reduced rows",
        abs(wrong_nc - correct_reduced) > 0.05
        and abs(wrong_dim - correct_reduced) > 0.04
        and abs(wrong_source - correct_reduced) > 0.7,
    )
    check(
        "note prints exact falsifier values",
        "0.002417102163" in text
        and "0.026142350801" in text
        and "0.273042774766" in text
        and "0.157783689333" in text
        and "0.943492137331" in text,
    )

    gate_markers = [f"N{i} -" for i in range(1, 9)]
    check(
        "negative-claim discipline gate is visible",
        all(marker in text for marker in gate_markers)
        and "repo-native no-go discipline instructions were read" in text,
    )
    check(
        "N1 names five distinct attack routes",
        all(
            route in text
            for route in [
                "Direct exact-Wilson differentiation",
                "Saddle diagonal derivative",
                "J-expectation asymptotics",
                "Finite trend extrapolation",
                "Operator-remainder transfer",
            ]
        ),
    )
    check(
        "N7 steelman names a concrete route that could break the obstruction",
        "hidden total-positivity or" in text and "oscillation structure" in text,
    )
    check(
        "runner and cache paths are named in the note",
        "scripts/native_gauge_transfer_diagonal_domination_rung_nine_bounded_2026_06_12.py" in text
        and "logs/runner-cache/native_gauge_transfer_diagonal_domination_rung_nine_bounded_2026_06_12.txt" in text,
    )
    check("note verification section names the expected total", "TOTAL: PASS=29, FAIL=0" in text)
    check(
        "formal constants are not silently assigned numeric fitted values",
        "c_J = 0." not in text and "c_D = 0." not in text and "c_J =" in text and "c_D =" in text,
    )
    check(
        "source notes loaded from expected repo refs",
        all(
            p.exists()
            for p in [
                BLOCK_HELLMANN_NOTE_PATH,
                CHARACTER_NOTE_PATH,
                OP_REMAINDER_NOTE_PATH,
                WILSON_TO_SADDLE_NOTE_PATH,
            ]
        ),
    )
    check(
        "witness ratios are finite and bounded",
        all(isclose(ratio, ratio, rel_tol=0.0) and 0.0 < ratio < 1.0 for *_rest, ratio in rows),
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
