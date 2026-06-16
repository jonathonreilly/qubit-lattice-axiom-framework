#!/usr/bin/env python3
"""Rung-ten Weyl-determinant assembly sufficiency checker.

This runner witnesses the source note's conditional assembly result. It
checks the exact note hygiene, verifies the finite determinant multilinearity
bound used in the note, recomputes true SU(3) Bessel-determinant coefficient
rows, and prints wrong-structure falsifiers.

The numerical rows are consistency witnesses only. They are not fitted into a
proof constant and are not used as a proof of the scalar local-CLT hypothesis.
"""

from __future__ import annotations

from itertools import product
from math import ceil, exp, pi, sqrt
from pathlib import Path
import sys

import numpy as np
from scipy.special import ive


AUDIT_TIMEOUT_SEC = 540

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_WEYL_DETERMINANT_ASSEMBLY_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md"
)
HSCALAR_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_UNIFORM_BESSEL_LOCAL_CLT_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md"
)
OP_REMAINDER_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md"
)
CHAR_NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md"
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


def note_text() -> str:
    return NOTE_PATH.read_text(encoding="utf-8")


def highest_weight_triple(p: int, q: int) -> list[int]:
    return [p + q, q, 0]


def determinant_size(matrix: np.ndarray) -> float:
    return float(np.linalg.det(matrix))


def mode_cap(beta: float, p: int, q: int) -> int:
    t = beta / 3.0
    lam = highest_weight_triple(p, q)
    return int(ceil(10.0 * sqrt(t) + max(abs(x) for x in lam) + 20.0))


def coefficient_scaled(
    p: int,
    q: int,
    beta: float,
    *,
    size: int = 3,
    lam_override: list[int] | None = None,
) -> float:
    """Return e^(-size*t) times the determinant-mode coefficient.

    For size=3 this common exponential cancels in c_(p,q)/c_(0,0).
    Wrong-size calls are used only as falsifiers.
    """
    t = beta / 3.0
    lam = lam_override if lam_override is not None else highest_weight_triple(p, q)
    cap = mode_cap(beta, p, q)
    total = 0.0
    for mode in range(-cap, cap + 1):
        mat = np.array(
            [
                [ive(abs(mode + lam[j] + i - j), t) for j in range(size)]
                for i in range(size)
            ],
            dtype=float,
        )
        total += determinant_size(mat)
    return total


def ratio_exact(
    p: int,
    q: int,
    beta: float,
    *,
    size: int = 3,
    lam_override: list[int] | None = None,
) -> float:
    return coefficient_scaled(p, q, beta, size=size, lam_override=lam_override) / coefficient_scaled(
        0, 0, beta, size=size, lam_override=([0, 0, 0] if lam_override else None)
    )


def dim_su3(p: int, q: int) -> float:
    return (p + 1) * (q + 1) * (p + q + 2) / 2.0


def casimir_su3(p: int, q: int) -> float:
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def saddle_ratio(p: int, q: int, beta: float, *, n_color: float = 3.0, dim: bool = True) -> float:
    prefactor = dim_su3(p, q) if dim else 1.0
    return prefactor * exp(-n_color * casimir_su3(p, q) / beta)


def scaled(value: float, beta: float) -> float:
    return beta ** (-1.5) * value


def gaussian_matrix(p: int, q: int, beta: float, mode: int) -> np.ndarray:
    t = beta / 3.0
    lam = highest_weight_triple(p, q)
    return np.array(
        [
            [
                (2.0 * pi * t) ** -0.5
                * exp(-((mode + lam[j] + i - j) ** 2) / (2.0 * t))
                for j in range(3)
            ]
            for i in range(3)
        ],
        dtype=float,
    )


def determinant_multilinear_bound(matrix: np.ndarray, p_sup: float, c_sup: float, t: float) -> float:
    """Hadamard-column bound for determinant terms beyond first P_1 order."""
    eta = p_sup / t + c_sup / (t * t)
    theta = (1.0 + eta) ** 3 - 1.0 - 3.0 * p_sup / t
    column_product = float(np.prod(np.linalg.norm(matrix, axis=0)))
    return column_product * theta


def exact_multilinear_remainder_bound_holds(matrix: np.ndarray, p_sup: float, c_sup: float, t: float) -> bool:
    """Check the finite algebra by enumerating determinant multilinear terms.

    The entry perturbations are deterministic signs at the allowed sup norms.
    The check is not a scalar-lemma proof; it verifies the determinant algebra
    used in the note.
    """
    rng = np.random.default_rng(20260612)
    p_shape = rng.choice([-1.0, 1.0], size=(3, 3)) * p_sup
    r_shape = rng.choice([-1.0, 1.0], size=(3, 3)) * c_sup / (t * t)
    base_cols = [matrix[:, j] for j in range(3)]
    p_cols = [matrix[:, j] * p_shape[:, j] / t for j in range(3)]
    r_cols = [matrix[:, j] * r_shape[:, j] for j in range(3)]

    actual = np.linalg.det(matrix + np.column_stack(p_cols) + np.column_stack(r_cols))
    first = np.linalg.det(matrix)
    for j in range(3):
        cols = list(base_cols)
        cols[j] = p_cols[j]
        first += np.linalg.det(np.column_stack(cols))

    remainder = abs(float(actual - first))

    enum_bound = 0.0
    for choices in product([0, 1, 2], repeat=3):
        # 0=base, 1=P column, 2=R column. Skip base and exactly one P.
        if choices == (0, 0, 0):
            continue
        if choices.count(1) == 1 and choices.count(2) == 0:
            continue
        cols = []
        for j, choice in enumerate(choices):
            if choice == 0:
                cols.append(base_cols[j])
            elif choice == 1:
                cols.append(p_cols[j])
            else:
                cols.append(r_cols[j])
        enum_bound += abs(float(np.linalg.det(np.column_stack(cols))))

    hadamard_bound = determinant_multilinear_bound(matrix, p_sup, c_sup, t)
    return remainder <= enum_bound + 1.0e-18 and enum_bound <= hadamard_bound + 1.0e-18


def max_grid_residual(beta: int, a: float) -> tuple[float, tuple[int, int, float, float]]:
    cap = int(a * sqrt(beta))
    best = -1.0
    best_row = (0, 0, 0.0, 0.0)
    for p in range(cap + 1):
        for q in range(cap + 1):
            exact = scaled(ratio_exact(p, q, beta), beta)
            saddle = scaled(saddle_ratio(p, q, beta), beta)
            residual = sqrt(beta) * abs(exact - saddle)
            if residual > best:
                best = residual
                best_row = (p, q, exact, saddle)
    return best, best_row


def main() -> int:
    print("Native gauge-transfer Weyl-determinant assembly rung-ten runner")
    print("Numerical rows are witnesses only; no fitted K_W is promoted.")
    print()

    text = note_text()
    flat = " ".join(text.split())
    lower = text.lower()

    check("source note exists", NOTE_PATH.is_file(), str(NOTE_PATH.relative_to(REPO_ROOT)))
    required_status = (
        "Status authority: independent audit lane only. This source note does not set or predict an audit outcome."
    )
    check("note carries exact status-authority line", required_status in text)
    check(
        "note declares open_gate claim type",
        "**Claim type:** open_gate" in text
        and "partial-with-named-missing-link" in text,
    )
    check(
        "note states H_scalar is a dependency and not re-proved here",
        "`H_scalar` is supplied by the companion scalar note" in text
        and "it is not re-proved here" in text,
    )
    check(
        "repo-native one-hop authority files are present",
        all(path.is_file() for path in [HSCALAR_PATH, OP_REMAINDER_PATH, CHAR_NOTE_PATH]),
    )
    check(
        "note does not use .claude tmp refs as authority paths",
        ".claude/tmp" not in text,
    )
    check(
        "W85 and W86 are context-only route surfaces",
        "NATIVE_GAUGE_TRANSFER_WILSON_TO_SADDLE_UNIFORM_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md" in text
        and "NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md" in text
        and text.count("is route-target context only, not a proof dependency") >= 2,
    )
    check(
        "authority quote anchors are present",
        "wilson_to_saddle_uniform(a):" in text
        and "The requested domination would require `c_D <= c_J` plus a uniform subleading bound." in flat
        and "beta^(-3/2) r_(p,q)(beta)" in text
        and "X = (chi_(1,0) + chi_(0,1)) / 6" in text,
    )
    check(
        "note gives determinant propagation formulas",
        "Theta_R(t) = (1 + P_R/t + C_R/t^2)^3 - 1 - 3 P_R/t" in text
        and "E_lambda^trunc" in text
        and "Hadamard" in text,
    )
    check(
        "note refuses to promote the truncated determinant bound into K_W",
        "This is not yet K_W(a)." in text
        and "uniform Weyl-determinant cancellation/normalization lemma" in text,
    )
    check(
        "note names the Route A reduced spectral ingredient",
        "reduced A2 spectral-domination lemma" in text
        and "c_D <= c_J" in text,
    )
    check(
        "note gives both readings of H_scalar ambiguity",
        "Literal compact-window reading" in text and "Strengthened reading" in text,
    )
    check(
        "note differentiates new content from prior notes",
        "what is new here" in lower and "what is restated" in lower,
    )
    check(
        "note includes no-go discipline gate",
        "N1 - Alternative route enumeration:" in text
        and "N8 - Cross-cycle echo:" in text
        and "Steelman" in text,
    )
    forbidden = [
        "only " + "route",
        "last " + "route",
        "ex" + "hausted",
        "closes the " + "program",
        "per" + "manently",
        "no other " + "path",
        "audited" + "_clean",
        "audited" + "_conditional",
    ]
    check(
        "note avoids forbidden overreach and audit-grade phrases",
        not any(fragment in lower for fragment in forbidden),
        "scanned exact forbidden fragments",
    )
    check(
        "canonical comparator is absent from note and runner",
        ("0." + "5934") not in text
        and ("0." + "5934") not in Path(__file__).read_text(encoding="utf-8"),
    )
    check(
        "runner/cache paths are named in the note",
        "scripts/native_gauge_transfer_weyl_determinant_assembly_rung_ten_bounded_2026_06_12.py" in text
        and "logs/runner-cache/native_gauge_transfer_weyl_determinant_assembly_rung_ten_bounded_2026_06_12.txt" in text,
    )

    print("determinant_multilinearity_rows")
    for beta, p, q, mode in [(96, 6, 5, 0), (96, 6, 5, -5), (192, 10, 8, -8)]:
        matrix = gaussian_matrix(p, q, beta, mode)
        det_value = abs(float(np.linalg.det(matrix)))
        col_bound = float(np.prod(np.linalg.norm(matrix, axis=0)))
        ratio = col_bound / det_value if det_value > 0 else float("inf")
        ok = exact_multilinear_remainder_bound_holds(matrix, p_sup=7.0, c_sup=11.0, t=beta / 3.0)
        print(
            f"  beta={beta:3d} p={p:2d} q={q:2d} mode={mode:3d} "
            f"|detG|={det_value:.12e} hadamard_cols={col_bound:.12e} "
            f"cofactor_looseness={ratio:.6e}"
        )
        check(f"finite determinant multilinearity bound holds for beta={beta}, mode={mode}", ok)

    print("true_determinant_witness_rows")
    witness_rows = []
    for beta, p, q in [(48, 4, 3), (96, 6, 5), (192, 10, 8)]:
        exact = ratio_exact(p, q, beta)
        sad = saddle_ratio(p, q, beta)
        rel = (exact - sad) / sad
        witness_rows.append((beta, p, q, exact, sad, rel))
        print(
            f"  beta={beta:3d} (p,q)=({p:2d},{q:2d}) "
            f"exact_r={exact:.12f} saddle={sad:.12f} rel_diff={rel:.12e}"
        )
    check(
        "true determinant rows show decreasing relative exact-to-saddle residual",
        abs(witness_rows[2][5]) < abs(witness_rows[1][5]) < abs(witness_rows[0][5]),
        "finite consistency witness only",
    )

    print("active_grid_witness_rows")
    grid_rows = []
    for beta in [48, 96, 192]:
        max_resid, row = max_grid_residual(beta, 1.25)
        grid_rows.append((beta, max_resid, row))
        p, q, exact, saddle = row
        print(
            f"  beta={beta:3d} cap={int(1.25 * sqrt(beta)):2d} "
            f"max_sqrt_beta_scaled_resid={max_resid:.12e} "
            f"at=({p},{q}) exact={exact:.12e} saddle={saddle:.12e}"
        )
    check(
        "active-grid witness residual decreases across sampled beta rows",
        grid_rows[2][1] < grid_rows[1][1] < grid_rows[0][1],
        "finite consistency witness only",
    )

    beta = 96
    p, q = 6, 5
    falsifiers = {
        "correct exact determinant ratio": scaled(ratio_exact(p, q, beta), beta),
        "correct saddle N_c=3": scaled(saddle_ratio(p, q, beta, n_color=3.0), beta),
        "wrong N_c=2": scaled(saddle_ratio(p, q, beta, n_color=2.0), beta),
        "wrong N_c=4": scaled(saddle_ratio(p, q, beta, n_color=4.0), beta),
        "wrong dimension omitted": scaled(saddle_ratio(p, q, beta, dim=False), beta),
        "wrong determinant size 2x2": scaled(ratio_exact(p, q, beta, size=2), beta),
        "wrong lambda=(p,q,0)": scaled(ratio_exact(p, q, beta, lam_override=[p, q, 0]), beta),
    }
    print("falsifier_rows_beta_96_p_6_q_5")
    for label, value in falsifiers.items():
        print(f"  {label}: {value:.12f}")
    correct = falsifiers["correct exact determinant ratio"]
    check(
        "wrong N_c substitutions visibly differ from the true row",
        abs(falsifiers["wrong N_c=2"] - correct) > 0.03
        and abs(falsifiers["wrong N_c=4"] - correct) > 0.02,
    )
    check(
        "wrong determinant size and wrong highest weight visibly differ from the true row",
        abs(falsifiers["wrong determinant size 2x2"] - correct) > 0.05
        and abs(falsifiers["wrong lambda=(p,q,0)"] - correct) > 0.04,
    )
    check(
        "wrong dimension substitution visibly differs from the true row",
        abs(falsifiers["wrong dimension omitted"] - correct) > 0.07,
    )

    check(
        "final verdict is necessary-but-not-sufficient",
        "H_scalar is necessary but not sufficient for the two-route half-line assembly." in flat,
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
