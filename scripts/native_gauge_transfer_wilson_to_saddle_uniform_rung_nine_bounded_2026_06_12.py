#!/usr/bin/env python3
"""Wilson-to-saddle uniform obstruction runner.

This runner is deterministic and source-side. It does not fit K_W(a), does not
derive a replacement constant, and does not set an audit outcome. Its job is to
check the exact Bessel-determinant object, witness the leading saddle trend,
and make the resisting uniform-remainder term visible.
"""

from __future__ import annotations

from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
from scipy.special import ive


AUDIT_TIMEOUT_SEC = 540
MODE_MAX = 160
REPO_ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_WILSON_TO_SADDLE_UNIFORM_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0
COEFF_CACHE: dict[tuple[int, int, int, str], float] = {}
C00_CACHE: dict[tuple[int, str], float] = {}


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


def dim_wrong_missing_a2_factor(p: int, q: int) -> float:
    return (p + 1) * (q + 1)


def casimir_su3(p: int, q: int) -> float:
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def coefficient_scaled(
    p: int, q: int, beta: int, *, variant: str = "correct", mode_max: int = MODE_MAX
) -> float:
    """Return e^(-beta) times c_(p,q)(beta).

    The common exponential scale cancels in c_(p,q)/c_(0,0). The exact
    coefficient convention is the repo Bessel determinant with arg=beta/3.
    """

    key = (p, q, beta, variant)
    cached = COEFF_CACHE.get(key)
    if cached is not None:
        return cached

    arg = beta / 3.0
    if variant == "correct":
        lam = [p + q, q, 0]
    elif variant == "wrong_lambda":
        lam = [p, q, 0]
    else:
        raise ValueError(f"unknown variant: {variant}")

    total = 0.0
    for mode in range(-mode_max, mode_max + 1):
        mat = np.array(
            [
                [ive(mode + lam[j] + i - j, arg) for j in range(3)]
                for i in range(3)
            ],
            dtype=float,
        )
        total += float(np.linalg.det(mat))
    COEFF_CACHE[key] = total
    return total


def ratio(p: int, q: int, beta: int, *, variant: str = "correct") -> float:
    c00_key = (beta, variant)
    c00 = C00_CACHE.get(c00_key)
    if c00 is None:
        c00 = coefficient_scaled(0, 0, beta, variant=variant)
        C00_CACHE[c00_key] = c00
    return coefficient_scaled(p, q, beta, variant=variant) / c00


def saddle_ratio(
    p: int, q: int, beta: int, *, saddle_constant: float = 3.0, wrong_dim: bool = False
) -> float:
    d = dim_wrong_missing_a2_factor(p, q) if wrong_dim else dim_su3(p, q)
    return d * exp(-saddle_constant * casimir_su3(p, q) / beta)


def h_exp_q(p: int, q: int, beta: int) -> float:
    x = p / sqrt(beta)
    y = q / sqrt(beta)
    return (x * y * (x + y) / 2.0) * exp(-(x * x + x * y + y * y))


def fixed_index_obstruction() -> None:
    z = 100.0
    nu = 20
    actual = ive(nu, z) * sqrt(2.0 * pi * z)
    fixed_next = 1.0 - (4.0 * nu * nu - 1.0) / (8.0 * z)
    gaussian = exp(-(nu * nu) / (2.0 * z))
    print("FIXED-INDEX BESSEL TERM CHECK")
    print(
        f"z={z:.1f} nu={nu} normalized_actual={actual:.12f} "
        f"fixed_next={fixed_next:.12f} gaussian_local={gaussian:.12f}"
    )
    check(
        "fixed-index next term is not a positive uniform entry approximation",
        fixed_next < 0.0 < actual and abs(actual - gaussian) < 4.0e-4,
        "with nu=2*sqrt(z), the fixed-index correction is O(1) and negative",
    )


def coefficient_symmetry_check() -> None:
    rows = []
    for beta, p, q in [(48, 4, 3), (96, 6, 5), (192, 10, 8)]:
        cpq = ratio(p, q, beta)
        cqp = ratio(q, p, beta)
        rows.append(abs(cpq - cqp))
        print(
            f"symmetry beta={beta} pair=({p},{q}) "
            f"r_pq={cpq:.12f} r_qp={cqp:.12f} diff={abs(cpq-cqp):.3e}"
        )
    check(
        "Bessel determinant ratio is conjugation-symmetric on witness rows",
        max(rows) < 2.0e-12,
        f"max symmetry diff={max(rows):.3e}",
    )


def leading_saddle_witness() -> None:
    samples = [(48, 4, 3), (96, 6, 5), (192, 10, 8)]
    rels = []
    scaled_diffs = []
    print("LEADING SADDLE WITNESS ROWS")
    for beta, p, q in samples:
        exact = ratio(p, q, beta)
        saddle = saddle_ratio(p, q, beta)
        rel = exact / saddle - 1.0
        scaled_diff = abs((beta ** -1.5) * (exact - saddle)) * sqrt(beta)
        rels.append(abs(rel))
        scaled_diffs.append(scaled_diff)
        print(
            f"beta={beta:3d} p={p:2d} q={q:2d} "
            f"r_exact={exact:.12f} r_saddle={saddle:.12f} "
            f"rel={rel:+.6e} sqrt_beta_scaled_diag_diff={scaled_diff:.6e}"
        )
    check(
        "leading saddle witness improves on the selected active-window rows",
        rels[0] > rels[1] > rels[2] and max(scaled_diffs) < 3.0e-2,
        "witness only; no K_W is inferred from these rows",
    )


def active_grid_witness() -> None:
    print("ACTIVE-GRID WITNESS ROWS")
    max_rows = []
    for beta in [48, 96]:
        cap = int(1.25 * sqrt(beta))
        max_diag = 0.0
        max_profile = 0.0
        for p in range(cap + 1):
            for q in range(cap + 1):
                exact = ratio(p, q, beta)
                sad = saddle_ratio(p, q, beta)
                exact_profile = (beta ** -1.5) * exact
                max_diag = max(max_diag, abs(exact_profile - (beta ** -1.5) * sad) * sqrt(beta))
                max_profile = max(max_profile, abs(exact_profile - h_exp_q(p, q, beta)) * sqrt(beta))
        max_rows.append((max_diag, max_profile))
        print(
            f"beta={beta:3d} cap={cap:2d} "
            f"max_sqrt_diag_diff={max_diag:.6e} "
            f"max_sqrt_profile_diff={max_profile:.6e}"
        )
    check(
        "active-grid witness remains finite without fitting a bound",
        all(np.isfinite(v) for row in max_rows for v in row)
        and max(row[0] for row in max_rows) < 6.0e-2,
        "grid witness reports margins but is not a proof of K_W",
    )


def falsifier_rows() -> None:
    beta, p, q = 96, 6, 5
    exact = ratio(p, q, beta)
    correct_saddle = saddle_ratio(p, q, beta)
    wrong_nc2 = saddle_ratio(p, q, beta, saddle_constant=2.0)
    wrong_nc4 = saddle_ratio(p, q, beta, saddle_constant=4.0)
    wrong_dim = saddle_ratio(p, q, beta, wrong_dim=True)
    wrong_lam = ratio(p, q, beta, variant="wrong_lambda")
    scale = beta ** -1.5
    print("FALSIFIER ROWS beta=96 p=6 q=5")
    print(f"correct exact beta^-3/2 r                 = {scale * exact:.12f}")
    print(f"correct saddle beta^-3/2 d exp[-3C2/beta] = {scale * correct_saddle:.12f}")
    print(f"wrong N_c=2 saddle                         = {scale * wrong_nc2:.12f}")
    print(f"wrong N_c=4 saddle                         = {scale * wrong_nc4:.12f}")
    print(f"wrong dimension saddle                     = {scale * wrong_dim:.12f}")
    print(f"wrong lambda determinant                   = {scale * wrong_lam:.12f}")
    check(
        "wrong N_c substitutions visibly move the witness value",
        abs(scale * wrong_nc2 - scale * correct_saddle) > 4.0e-2
        and abs(scale * wrong_nc4 - scale * correct_saddle) > 2.0e-2,
        "N_c=2 and N_c=4 both separate from the correct saddle row",
    )
    check(
        "wrong dimension and wrong Bessel index visibly move the witness value",
        abs(scale * wrong_dim - scale * correct_saddle) > 6.0e-2
        and abs(scale * wrong_lam - scale * exact) > 4.0e-2,
        "dimension and lambda-index falsifiers are not small perturbations",
    )


def note_checks() -> None:
    text = NOTE_PATH.read_text(encoding="utf-8")
    required = [
        "**Claim type:** open_gate",
        "Status authority: independent audit lane only. This source note does not set or predict an audit outcome.",
        "Honest outcome: obstruction-at-exact-step",
        "No source-side value of K_W(a) is derived in this note.",
        "Both readings of the Bessel-asymptotic instruction",
        "## No-Go Discipline Gate",
        "TOTAL: PASS=",
        "logs/runner-cache/native_gauge_transfer_wilson_to_saddle_uniform_rung_nine_bounded_2026_06_12.txt",
    ]
    check(
        "note contains required boundary, outcome, runner, and discipline markers",
        all(s in text for s in required),
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
            ("fitted", "K_W"),
        ]
    ]
    banned.extend(["K_W(a)" + " =", "derive K_W by" + " fit"])
    lower = text.lower()
    check(
        "note avoids overreach phrases and fitted-K_W forms",
        not any(item.lower() in lower for item in banned),
        "scanned bounded banned phrase set",
    )
    check(
        "note does not promote decimal witnesses to exact rationals",
        "Fraction(" not in text and "from_float" not in text and "limit_denominator" not in text,
        "float-dyadic guard scan",
    )
    check(
        "note avoids branch-local temp references",
        "." + "claude" + "/tmp" not in text and "tmp" + "/refs" not in text,
        "portable-source guard scan",
    )


def authority_file_checks() -> None:
    refs = [
        REPO_ROOT
        / "docs/NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md",
        REPO_ROOT / "docs/GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md",
        REPO_ROOT / "docs/GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md",
        REPO_ROOT / "scripts/frontier_su3_wilson_closed_form_fanout_2026_05_04.py",
    ]
    present = all(p.exists() for p in refs)
    check(
        "one-hop authority files are present",
        present,
        ", ".join(str(p.relative_to(REPO_ROOT)) for p in refs),
    )
    if not present:
        return
    texts = [p.read_text(encoding="utf-8") for p in refs]
    check(
        "authority files contain K_W target, saddle profile, recurrence, and Bessel determinant markers",
        "wilson_to_saddle_uniform(a):" in texts[0]
        and "K_geom(a) = 6 a^4 + 3 a^2 + 3 a + 1" in texts[0]
        and "H(x,y) = x y (x+y) / 2" in texts[0]
        and "If a later operator estimate supplies" in texts[0]
        and "X = (chi_(1,0) + chi_(0,1)) / 6" in texts[1]
        and "a_(p,q)(beta) = sum_(n in Z) det[I_(n + lambda_j + i - j)(beta/3)]" in texts[2]
        and "c_(p,q)(beta) = sum_(n in Z) det[I_(n + lambda_j + i - j)(beta/3)]_(i,j=1..3)" in texts[3],
        "checked exact authority quote anchors",
    )


def main() -> int:
    print("Native gauge-transfer Wilson-to-saddle uniform obstruction runner")
    print(f"MODE_MAX={MODE_MAX}; K_W is not computed from grid residuals")
    print()
    authority_file_checks()
    note_checks()
    fixed_index_obstruction()
    coefficient_symmetry_check()
    leading_saddle_witness()
    active_grid_witness()
    falsifier_rows()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
