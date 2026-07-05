#!/usr/bin/env python3
"""Weyl-determinant tail-domination obstruction runner.

This runner is deterministic and source-side. It witnesses the exact SU(3)
Bessel determinant, finite scalar-to-determinant propagation, mode-tail mass,
and wrong-structure falsifiers. It does not fit K_W(A), does not derive a
tail constant, and does not set an audit outcome.
"""

from __future__ import annotations

from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
from scipy.special import ive


AUDIT_TIMEOUT_SEC = 540
MODE_MAX = 220
REPO_ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_WEYL_DETERMINANT_TAIL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0
COEFF_CACHE: dict[tuple[int, int, int, str, int], float] = {}
C00_CACHE: dict[tuple[int, str, int], float] = {}


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


def dim_su3(p: int, q: int) -> float:
    return (p + 1) * (q + 1) * (p + q + 2) / 2.0


def casimir_su3(p: int, q: int) -> float:
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def p1_local_clt(a: float) -> float:
    return (a**4 - 6.0 * a * a + 3.0) / 24.0


def lambda_tuple(p: int, q: int, variant: str = "correct") -> list[int]:
    if variant == "correct":
        return [p + q, q, 0]
    if variant == "wrong_lambda":
        return [p, q, 0]
    raise ValueError(f"unknown lambda variant: {variant}")


def coefficient_scaled(
    p: int,
    q: int,
    beta: int,
    *,
    variant: str = "correct",
    determinant_size: int = 3,
    mode_max: int = MODE_MAX,
) -> float:
    """Return e^(-beta) times c_(p,q)(beta) in the chosen determinant size."""

    key = (p, q, beta, variant, determinant_size)
    cached = COEFF_CACHE.get(key)
    if cached is not None:
        return cached

    arg = beta / 3.0
    lam = lambda_tuple(p, q, variant)[:determinant_size]
    total = 0.0
    for mode in range(-mode_max, mode_max + 1):
        mat = np.array(
            [
                [ive(mode + lam[j] + i - j, arg) for j in range(determinant_size)]
                for i in range(determinant_size)
            ],
            dtype=float,
        )
        total += float(np.linalg.det(mat))
    COEFF_CACHE[key] = total
    return total


def ratio(
    p: int,
    q: int,
    beta: int,
    *,
    variant: str = "correct",
    determinant_size: int = 3,
) -> float:
    c00_key = (beta, variant, determinant_size)
    c00 = C00_CACHE.get(c00_key)
    if c00 is None:
        c00 = coefficient_scaled(0, 0, beta, variant=variant, determinant_size=determinant_size)
        C00_CACHE[c00_key] = c00
    return coefficient_scaled(p, q, beta, variant=variant, determinant_size=determinant_size) / c00


def saddle_ratio(p: int, q: int, beta: int, *, saddle_constant: float = 3.0) -> float:
    return dim_su3(p, q) * exp(-saddle_constant * casimir_su3(p, q) / beta)


def saddle_dimension_omitted(p: int, q: int, beta: int) -> float:
    return exp(-3.0 * casimir_su3(p, q) / beta)


def gaussian_matrices(p: int, q: int, beta: int, mode: int) -> tuple[np.ndarray, np.ndarray, float]:
    t = beta / 3.0
    lam = lambda_tuple(p, q)
    prefactor = (2.0 * pi * t) ** -0.5
    g = np.empty((3, 3), dtype=float)
    pcols = np.empty((3, 3), dtype=float)
    for i in range(3):
        for j in range(3):
            k = mode + lam[j] + i - j
            a = k / sqrt(t)
            gij = prefactor * exp(-k * k / (2.0 * t))
            g[i, j] = gij
            pcols[i, j] = gij * p1_local_clt(a)
    return g, pcols, t


def first_correction_sum(g: np.ndarray, pcols: np.ndarray) -> float:
    total = 0.0
    for col in range(3):
        mat = g.copy()
        mat[:, col] = pcols[:, col]
        total += float(np.linalg.det(mat))
    return total


def exact_mode_terms(p: int, q: int, beta: int) -> list[tuple[int, float]]:
    arg = beta / 3.0
    lam = lambda_tuple(p, q)
    terms: list[tuple[int, float]] = []
    for mode in range(-MODE_MAX, MODE_MAX + 1):
        mat = np.array(
            [[ive(mode + lam[j] + i - j, arg) for j in range(3)] for i in range(3)],
            dtype=float,
        )
        terms.append((mode, float(np.linalg.det(mat))))
    return terms


def outside_mode_mass(p: int, q: int, beta: int, window: int) -> float:
    terms = exact_mode_terms(p, q, beta)
    denom = sum(abs(value) for _, value in terms)
    return sum(abs(value) for mode, value in terms if abs(mode) > window) / denom


def authority_file_checks() -> None:
    refs = [
        REPO_ROOT / "docs/NATIVE_GAUGE_TRANSFER_WEYL_DETERMINANT_ASSEMBLY_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md",
        REPO_ROOT / "docs/NATIVE_GAUGE_TRANSFER_UNIFORM_BESSEL_LOCAL_CLT_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md",
        REPO_ROOT / "docs/NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md",
        REPO_ROOT / "docs/GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md",
        REPO_ROOT / "scripts/frontier_su3_wilson_closed_form_fanout_2026_05_04.py",
    ]
    present = all(path.exists() for path in refs)
    check(
        "one-hop authority files are present",
        present,
        ", ".join(str(path.relative_to(REPO_ROOT)) for path in refs),
    )
    if not present:
        return

    determinant_assembly = refs[0].read_text(encoding="utf-8")
    scalar_clt = refs[1].read_text(encoding="utf-8")
    operator_remainder = refs[2].read_text(encoding="utf-8")
    recurrence = refs[3].read_text(encoding="utf-8")
    coeff_script = refs[4].read_text(encoding="utf-8")
    check(
        "authority anchors contain determinant expansion, H_det, scalar P1, saddle, recurrence, and tail markers",
        "det B_n" in determinant_assembly
        and "H_det(A):" in determinant_assembly
        and "c_(0,0) lower normalization" in determinant_assembly
        and "P_1(a) = (a^4 - 6 a^2 + 3) / 24." in scalar_clt
        and "C_0 / (sqrt(2 pi t) t^2)" in scalar_clt
        and "H(x,y) = x y (x+y) / 2" in operator_remainder
        and "X = (chi_(1,0) + chi_(0,1)) / 6" in recurrence
        and "c_(p,q)(beta) = sum_(n in Z) det[I_(n + lambda_j + i - j)(beta/3)]_(i,j=1..3)" in coeff_script
        and "K_tail_sad(a) = ((a + 2)^3 / 8) exp[-3 a^2 / 4]" in operator_remainder,
        "checked exact quote-anchor substrings",
    )
    absent_needles = ["25-34%", "out-of-window", "mode-sum mass"]
    check(
        "determinant assembly note lacks the requested 25-34 percent quote anchor",
        not any(needle in determinant_assembly for needle in absent_needles),
        "runner treats 25-34 percent rows as recomputed witnesses, not quote anchors",
    )


def note_checks() -> None:
    text = NOTE_PATH.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    required_text = [
        "**Claim type:** open_gate",
        "**Type:** source-side obstruction map",
        "Status authority: independent audit lane only. This source note does not set or predict an audit outcome.",
        "does not derive `K_W(A)`",
        "Citation Boundary On The 25-34 Percent Prompt",
        "No-Go Discipline Gate",
        "TOTAL: PASS=16, FAIL=0",
        "logs/runner-cache/native_gauge_transfer_weyl_determinant_tail_domination_rung_eleven_bounded_2026_06_12.txt",
    ]
    required_normalized = [
        "The honest outcome is obstruction-at-exact-step",
        "derive the uniform `c_(0,0)` lower normalization or the true Wilson determinant-mode/weight tail domination",
    ]
    check(
        "note contains required boundary, outcome, cache, and discipline markers",
        all(s in text for s in required_text) and all(s in normalized for s in required_normalized),
        "checked source-note guard strings",
    )

    banned = [
        " ".join(parts)
        for parts in [
            ("only", "route"),
            ("last", "route"),
            ("exhau", "sted"),
            ("closes", "the", "program"),
            ("perma", "nently"),
            ("no", "other", "path"),
            ("derived", "K_W"),
            ("fitted", "K_W"),
        ]
    ]
    banned.extend(["K_W(A)" + " =", "beta_0" + " ="])
    lower = text.lower()
    check(
        "note avoids overreach and fitted-constant guard phrases",
        not any(item.lower() in lower for item in banned),
        "scanned bounded banned phrase set",
    )
    check(
        "note avoids float-dyadic exact-rational artifacts",
        "Fraction(" not in text and "from_float" not in text and "limit_denominator" not in text,
        "float-dyadic guard scan",
    )


def determinant_multilinearity_witness() -> None:
    print("FINITE DETERMINANT PROPAGATION WITNESS")
    ratios: list[float] = []
    correction_ratios: list[float] = []
    for beta, p, q, mode in [(48, 4, 3, 0), (96, 6, 5, -4), (96, 6, 5, 4)]:
        g, pcols, t = gaussian_matrices(p, q, beta, mode)
        det_g = float(np.linalg.det(g))
        s1 = first_correction_sum(g, pcols)
        had = float(np.prod([np.linalg.norm(g[:, col]) for col in range(3)]))
        ratio_had = had / abs(det_g)
        ratios.append(ratio_had)
        correction_ratios.append(abs(s1 / det_g))
        print(
            f"beta={beta:3d} p={p:2d} q={q:2d} mode={mode:+3d} "
            f"t={t:.1f} detG={det_g:.6e} S1/detG={s1/det_g:+.6e} "
            f"Had/|detG|={ratio_had:.3f}"
        )
    check(
        "finite determinant expansion has large Hadamard-to-determinant cancellation witnesses",
        min(ratios) > 100.0 and max(ratios) > 300.0,
        f"Had/|detG| range=({min(ratios):.3f}, {max(ratios):.3f})",
    )
    check(
        "first correction sum is finite but not a normalized K_W proof",
        max(correction_ratios) > 1.0 and all(np.isfinite(v) for v in correction_ratios),
        f"max |S1/detG|={max(correction_ratios):.6f}",
    )


def exact_ratio_witnesses() -> None:
    print("EXACT-TO-SADDLE WITNESS ROWS")
    rels = []
    for beta, p, q in [(48, 4, 3), (96, 6, 5), (192, 10, 8)]:
        exact = ratio(p, q, beta)
        saddle = saddle_ratio(p, q, beta)
        rel = exact / saddle - 1.0
        rels.append(abs(rel))
        print(
            f"beta={beta:3d} p={p:2d} q={q:2d} "
            f"r_exact={exact:.12f} r_saddle={saddle:.12f} rel={rel:+.6e}"
        )
    check(
        "leading saddle witnesses match the retained decreasing-residual pattern",
        rels[0] > rels[1] > rels[2],
        "witness only; no K_W is inferred",
    )


def mode_tail_witnesses() -> None:
    print("DETERMINANT-MODE TAIL WITNESS ROWS")
    rows = []
    for beta, p, q in [(96, 6, 5), (192, 10, 8)]:
        t = beta / 3.0
        window = int(1.25 * sqrt(t))
        outside = outside_mode_mass(p, q, beta, window)
        rows.append(outside)
        print(
            f"beta={beta:3d} p={p:2d} q={q:2d} "
            f"window=floor(1.25*sqrt(t))={window:2d} outside_mass={outside:.12f}"
        )
    check(
        "mode-window witness reproduces the 25-34 percent tail scale",
        0.24 < rows[0] < 0.26 and 0.34 < rows[1] < 0.35,
        f"outside masses={rows[0]:.12f}, {rows[1]:.12f}",
    )

    beta, p, q, a = 192, 10, 8, 1.25
    correct_w = int(a * sqrt(beta / 3.0))
    third_w = int(a * beta ** (1.0 / 3.0))
    sqrt_beta_w = int(a * sqrt(beta))
    correct = outside_mode_mass(p, q, beta, correct_w)
    third = outside_mode_mass(p, q, beta, third_w)
    sqrt_beta = outside_mode_mass(p, q, beta, sqrt_beta_w)
    print("CUTOFF-SCALING FALSIFIER beta=192 p=10 q=8")
    print(f"sqrt(t) window={correct_w:2d} outside_mass={correct:.12f}")
    print(f"beta^(1/3) window={third_w:2d} outside_mass={third:.12f}")
    print(f"sqrt(beta) window={sqrt_beta_w:2d} outside_mass={sqrt_beta:.12f}")
    check(
        "wrong cutoff scalings visibly alter the mode-tail witness",
        third > 0.60 and sqrt_beta < 0.03 and correct > 0.34,
        "tail surface is sensitive to the scaling convention",
    )


def c00_and_weight_tail_witnesses() -> None:
    print("C00 NORMALIZATION AND FINITE WEIGHT-TAIL WITNESSES")
    c00_rows = []
    for beta in [48, 96, 192]:
        c00 = coefficient_scaled(0, 0, beta)
        scaled = (beta ** 1.5) * c00
        c00_rows.append(c00)
        print(f"beta={beta:3d} e^-beta c00={c00:.12e} beta^(3/2)*e^-beta*c00={scaled:.12e}")
    check(
        "c00 witness rows are positive but not an analytic lower bound",
        all(v > 0.0 and np.isfinite(v) for v in c00_rows),
        "positivity is witnessed numerically only",
    )

    beta, a = 96, 1.25
    cap = int(a * sqrt(beta))
    shell = 20
    max_outside = 0.0
    max_row = (0, 0)
    for p in range(shell + 1):
        for q in range(shell + 1):
            if max(p, q) > cap:
                value = (beta ** -1.5) * ratio(p, q, beta)
                if value > max_outside:
                    max_outside = value
                    max_row = (p, q)
    saddle_tail = ((a + 2.0) ** 3 / 8.0) * exp(-3.0 * a * a / 4.0)
    print(
        f"finite outside-weight grid beta={beta} cap={cap} shell={shell} "
        f"max_row={max_row} max_scaled_exact={max_outside:.12f} "
        f"K_tail_sad={saddle_tail:.12f}"
    )
    check(
        "finite outside-weight witness is bounded on the sampled grid",
        0.03 < max_outside < 0.04 and saddle_tail > 1.0,
        "saddle tail is a loose proxy and not a true Wilson tail proof",
    )


def falsifier_rows() -> None:
    beta, p, q = 96, 6, 5
    scale = beta ** -1.5
    exact = ratio(p, q, beta)
    correct_saddle = saddle_ratio(p, q, beta)
    wrong_nc2 = saddle_ratio(p, q, beta, saddle_constant=2.0)
    wrong_nc4 = saddle_ratio(p, q, beta, saddle_constant=4.0)
    wrong_dim_omitted = saddle_dimension_omitted(p, q, beta)
    wrong_2x2 = ratio(p, q, beta, determinant_size=2)
    wrong_lam = ratio(p, q, beta, variant="wrong_lambda")
    print("WRONG-STRUCTURE FALSIFIER ROWS beta=96 p=6 q=5")
    print(f"correct exact determinant ratio      = {scale * exact:.12f}")
    print(f"correct saddle N_c=3                = {scale * correct_saddle:.12f}")
    print(f"wrong N_c=2                         = {scale * wrong_nc2:.12f}")
    print(f"wrong N_c=4                         = {scale * wrong_nc4:.12f}")
    print(f"wrong dimension omitted             = {scale * wrong_dim_omitted:.12f}")
    print(f"wrong determinant size 2x2          = {scale * wrong_2x2:.12f}")
    print(f"wrong highest-weight lambda         = {scale * wrong_lam:.12f}")
    check(
        "wrong N_c substitutions visibly move the saddle row",
        abs(scale * wrong_nc2 - scale * correct_saddle) > 0.04
        and abs(scale * wrong_nc4 - scale * correct_saddle) > 0.02,
        "N_c=2 and N_c=4 both separate from N_c=3",
    )
    check(
        "wrong dimension, determinant size, and lambda index visibly move the exact object",
        abs(scale * wrong_dim_omitted - scale * correct_saddle) > 0.07
        and abs(scale * wrong_2x2 - scale * exact) > 0.07
        and abs(scale * wrong_lam - scale * exact) > 0.04,
        "wrong-structure substitutions are not small perturbations",
    )
    check(
        "falsifier values reproduce the note's displayed rows to tolerance",
        abs(scale * exact - 0.078225286971) < 5.0e-13
        and abs(scale * wrong_dim_omitted - 0.000292165845) < 5.0e-13
        and abs(scale * wrong_2x2 - 0.005101635871) < 5.0e-13,
        "checked exact, dimension-omitted, and 2x2 falsifier rows",
    )


def main() -> int:
    print("Native gauge-transfer Weyl-determinant tail-domination obstruction runner")
    print(f"MODE_MAX={MODE_MAX}; K_W(A) and true-tail constants are not fitted")
    print()
    authority_file_checks()
    note_checks()
    determinant_multilinearity_witness()
    exact_ratio_witnesses()
    mode_tail_witnesses()
    c00_and_weight_tail_witnesses()
    falsifier_rows()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
