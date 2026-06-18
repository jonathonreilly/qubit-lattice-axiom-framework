#!/usr/bin/env python3
"""Native gauge transfer H_det Gaussian-core support runner.

This runner isolates a source-side support piece for the `H_det(A)` wall named
by the native gauge Weyl-determinant assembly row.  It replaces each Bessel
entry by the scalar local-CLT Gaussian core, sums the exact 3x3 determinant
modes, normalizes by the `(0,0)` determinant, and compares that determinant
core with the SU(3) saddle diagonal.

The output is upstream support only.  It does not fit or derive the full
Wilson-to-saddle constant K_W(A), and it does not prove the reduced spectral
ingredient H_spec.
"""

from __future__ import annotations

from functools import lru_cache
from math import ceil, exp, pi, sqrt
from pathlib import Path

import numpy as np
from scipy.special import ive


AUDIT_TIMEOUT_SEC = 240

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_HDET_GAUSSIAN_CORE_SUPPORT_NOTE_2026-06-18.md"
)
ASSEMBLY_NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_WEYL_DETERMINANT_ASSEMBLY_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md"
)
HSCALAR_NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_UNIFORM_BESSEL_LOCAL_CLT_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md"
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


def highest_weight(p: int, q: int) -> tuple[int, int, int]:
    return (p + q, q, 0)


def dim_su3(p: int, q: int) -> float:
    return (p + 1) * (q + 1) * (p + q + 2) / 2.0


def casimir_su3(p: int, q: int) -> float:
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def saddle_ratio(p: int, q: int, beta: int, *, n_color: float = 3.0, dim: bool = True) -> float:
    prefactor = dim_su3(p, q) if dim else 1.0
    return prefactor * exp(-n_color * casimir_su3(p, q) / beta)


def mode_cap(beta: int, p: int, q: int, extra: int = 20) -> int:
    t = beta / 3.0
    lam = highest_weight(p, q)
    return int(ceil(10.0 * sqrt(t) + max(abs(x) for x in lam) + extra))


def gaussian_entry(index: int, beta: int) -> float:
    t = beta / 3.0
    return (2.0 * pi * t) ** -0.5 * exp(-(index * index) / (2.0 * t))


def determinant_value(matrix: np.ndarray) -> float:
    return float(np.linalg.det(matrix))


@lru_cache(maxsize=None)
def gaussian_coeff(p: int, q: int, beta: int, extra: int = 20) -> float:
    lam = highest_weight(p, q)
    total = 0.0
    for mode in range(-mode_cap(beta, p, q, extra), mode_cap(beta, p, q, extra) + 1):
        mat = np.array(
            [
                [gaussian_entry(mode + lam[j] + i - j, beta) for j in range(3)]
                for i in range(3)
            ],
            dtype=float,
        )
        total += determinant_value(mat)
    return total


@lru_cache(maxsize=None)
def exact_coeff(p: int, q: int, beta: int, extra: int = 20) -> float:
    t = beta / 3.0
    lam = highest_weight(p, q)
    total = 0.0
    for mode in range(-mode_cap(beta, p, q, extra), mode_cap(beta, p, q, extra) + 1):
        mat = np.array(
            [
                [ive(abs(mode + lam[j] + i - j), t) for j in range(3)]
                for i in range(3)
            ],
            dtype=float,
        )
        total += determinant_value(mat)
    return total


def gaussian_ratio(p: int, q: int, beta: int) -> float:
    return gaussian_coeff(p, q, beta) / gaussian_coeff(0, 0, beta)


def exact_ratio(p: int, q: int, beta: int) -> float:
    return exact_coeff(p, q, beta) / exact_coeff(0, 0, beta)


def scaled_diag_difference(a: float, b: float, beta: int) -> float:
    return sqrt(beta) * abs(beta ** -1.5 * (a - b))


def note_checks() -> None:
    text = NOTE_PATH.read_text(encoding="utf-8")
    assembly_text = ASSEMBLY_NOTE_PATH.read_text(encoding="utf-8")
    required = [
        "**Claim type:** bounded_theorem",
        "Gaussian determinant-core support for `H_det(A)`",
        "does not derive `K_W(A)`",
        "not prove `H_spec`",
        "native_gauge_transfer_hdet_gaussian_core_support_2026_06_18.py",
    ]
    check("source note exists", NOTE_PATH.is_file(), str(NOTE_PATH.relative_to(REPO_ROOT)))
    check("source note contains the required boundary markers", all(s in text for s in required))
    check(
        "one-hop source notes exist",
        ASSEMBLY_NOTE_PATH.is_file() and HSCALAR_NOTE_PATH.is_file(),
        "assembly and scalar local-CLT notes are present",
    )
    check(
        "downstream assembly note wires H_det_core without closing H_det",
        "NATIVE_GAUGE_TRANSFER_HDET_GAUSSIAN_CORE_SUPPORT_NOTE_2026-06-18.md" in assembly_text
        and "H_det_core" in assembly_text
        and "H_det_remainder(A)" in assembly_text,
    )
    banned = [
        " ".join(parts)
        for parts in [
            ("derives", "K_W(A)"),
            ("proves", "H_det(A)"),
            ("closes", "H_spec"),
            ("all", "remaining", "native", "gauge", "blockers", "are", "closed"),
            ("effective", "retained"),
            ("retained", "branch-local"),
        ]
    ]
    check(
        "source note avoids closure/promotional wording",
        not any(fragment.lower() in text.lower() for fragment in banned),
        "scanned closure/promotional fragments",
    )


def denominator_and_symmetry_checks() -> None:
    rows = []
    for beta, p, q in [(48, 4, 3), (96, 6, 5), (192, 10, 8)]:
        c00 = gaussian_coeff(0, 0, beta)
        rpq = gaussian_ratio(p, q, beta)
        rqp = gaussian_ratio(q, p, beta)
        diff = abs(rpq - rqp)
        rows.append((c00, diff))
        print(
            f"gaussian_core_symmetry beta={beta:3d} pair=({p:2d},{q:2d}) "
            f"c00={c00:.12e} r_pq={rpq:.12f} r_qp={rqp:.12f} diff={diff:.3e}"
        )
    check(
        "Gaussian determinant denominator is positive on witness rows",
        min(c00 for c00, _ in rows) > 0.0,
    )
    check(
        "Gaussian determinant ratio is conjugation symmetric on witness rows",
        max(diff for _, diff in rows) < 2.0e-12,
        f"max diff={max(diff for _, diff in rows):.3e}",
    )


def selected_saddle_rows() -> None:
    print("selected_gaussian_core_to_saddle_rows")
    rels = []
    scaled = []
    for beta, p, q in [(48, 4, 3), (96, 6, 5), (192, 10, 8), (384, 12, 10)]:
        core = gaussian_ratio(p, q, beta)
        saddle = saddle_ratio(p, q, beta)
        rel = core / saddle - 1.0
        diag = scaled_diag_difference(core, saddle, beta)
        rels.append(abs(rel))
        scaled.append(diag)
        print(
            f"  beta={beta:3d} (p,q)=({p:2d},{q:2d}) "
            f"core={core:.12f} saddle={saddle:.12f} "
            f"rel={rel:+.6e} sqrt_beta_scaled_diff={diag:.6e}"
        )
    check(
        "selected Gaussian-core rows approach the saddle diagonal",
        rels[0] > rels[1] > rels[2] > rels[3] and max(scaled) < 2.0e-2,
        "sampled support only; no K_W(A) is fitted",
    )


def active_window_checks() -> None:
    print("active_window_gaussian_core_rows")
    max_rows = []
    for beta in [48, 96, 192]:
        cap = int(1.25 * sqrt(beta))
        max_diag = 0.0
        max_rel = 0.0
        max_row = None
        for p in range(cap + 1):
            for q in range(cap + 1):
                core = gaussian_ratio(p, q, beta)
                saddle = saddle_ratio(p, q, beta)
                diag = scaled_diag_difference(core, saddle, beta)
                rel = abs(core / saddle - 1.0) if saddle != 0.0 else 0.0
                if diag > max_diag:
                    max_diag = diag
                    max_row = (p, q, core, saddle, rel)
                max_rel = max(max_rel, rel)
        max_rows.append(max_diag)
        p, q, core, saddle, rel = max_row
        print(
            f"  beta={beta:3d} cap={cap:2d} max_sqrt_beta_scaled_diff={max_diag:.6e} "
            f"at=({p},{q}) rel={rel:.6e} core={core:.12f} saddle={saddle:.12f}"
        )
        print(f"    max_relative_error_on_window={max_rel:.6e}")
    check(
        "active-window Gaussian-core saddle error decreases on sampled windows",
        max_rows[0] > max_rows[1] > max_rows[2] and max(max_rows) < 2.0e-2,
        "finite active-window certificate, not a global theorem",
    )


def exact_vs_gaussian_remainder_checks() -> None:
    print("exact_bessel_to_gaussian_core_rows")
    max_rows = []
    for beta in [48, 96, 192]:
        cap = int(1.25 * sqrt(beta))
        max_diag = 0.0
        max_row = None
        for p in range(cap + 1):
            for q in range(cap + 1):
                exact = exact_ratio(p, q, beta)
                core = gaussian_ratio(p, q, beta)
                diag = scaled_diag_difference(exact, core, beta)
                if diag > max_diag:
                    max_diag = diag
                    max_row = (p, q, exact, core, abs(exact / core - 1.0))
        max_rows.append(max_diag)
        p, q, exact, core, rel = max_row
        print(
            f"  beta={beta:3d} cap={cap:2d} max_sqrt_beta_scaled_exact_minus_core={max_diag:.6e} "
            f"at=({p},{q}) rel={rel:.6e} exact={exact:.12f} core={core:.12f}"
        )
    check(
        "exact-to-Gaussian correction decreases but remains a separate H_scalar/remainder wall",
        max_rows[0] > max_rows[1] > max_rows[2] and max(max_rows) > 2.0e-2,
        "this is the remaining scalar/remainder contribution, not closed here",
    )


def tail_cap_checks() -> None:
    rows = []
    for beta, p, q in [(96, 6, 5), (192, 10, 8)]:
        base = gaussian_coeff(p, q, beta, extra=20)
        wider = gaussian_coeff(p, q, beta, extra=40)
        rel = abs(base - wider) / max(abs(wider), 1.0e-300)
        rows.append(rel)
        print(f"tail_cap_check beta={beta:3d} pair=({p},{q}) rel_change_extra20_to_40={rel:.3e}")
    check("Gaussian determinant mode cap is stable on witness rows", max(rows) < 1.0e-12)


def falsifier_checks() -> None:
    beta, p, q = 96, 6, 5
    scale = beta ** -1.5
    core = scale * gaussian_ratio(p, q, beta)
    saddle = scale * saddle_ratio(p, q, beta)
    wrong_n2 = scale * saddle_ratio(p, q, beta, n_color=2.0)
    wrong_n4 = scale * saddle_ratio(p, q, beta, n_color=4.0)
    wrong_dim = scale * saddle_ratio(p, q, beta, dim=False)
    print("falsifier_rows_beta_96_pair_6_5")
    print(f"  gaussian core normalized: {core:.12f}")
    print(f"  correct SU3 saddle:       {saddle:.12f}")
    print(f"  wrong N_c=2 saddle:       {wrong_n2:.12f}")
    print(f"  wrong N_c=4 saddle:       {wrong_n4:.12f}")
    print(f"  wrong no-dimension row:   {wrong_dim:.12f}")
    check(
        "wrong color constants visibly separate from the Gaussian core",
        abs(wrong_n2 - core) > 3.0e-2 and abs(wrong_n4 - core) > 2.0e-2,
    )
    check(
        "wrong dimension prefactor visibly separates from the Gaussian core",
        abs(wrong_dim - core) > 6.0e-2,
    )


def main() -> int:
    print("Native gauge transfer H_det Gaussian-core support runner")
    print("This is upstream support only: no fitted K_W(A), no proof of H_spec.")
    print()
    note_checks()
    denominator_and_symmetry_checks()
    selected_saddle_rows()
    active_window_checks()
    exact_vs_gaussian_remainder_checks()
    tail_cap_checks()
    falsifier_checks()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
