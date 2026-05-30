#!/usr/bin/env python3
"""Exact-rational companion for the R_conn vertex-color singlet projection note."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "RCONN_VERTEX_COLOR_SINGLET_PROJECTION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md"
FIERZ = ROOT / "docs" / "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md"

PASS = 0
FAIL = 0


Matrix = list[list[Fraction]]


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def eye(n: int) -> Matrix:
    return [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]


def add(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]


def scale(a: Matrix, s: Fraction) -> Matrix:
    n = len(a)
    return [[s * a[i][j] for j in range(n)] for i in range(n)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


def trace(a: Matrix) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def is_symmetric(a: Matrix) -> bool:
    n = len(a)
    return all(a[i][j] == a[j][i] for i in range(n) for j in range(n))


def lambda_3() -> Matrix:
    return [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(-1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0)],
    ]


def su3_symmetric_generators() -> list[Matrix]:
    lam1 = [
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0)],
    ]
    lam4 = [
        [Fraction(0), Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(0)],
    ]
    lam6 = [
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(1), Fraction(0)],
    ]
    return [scale(m, Fraction(1, 2)) for m in (lam1, lam4, lam6)] + [
        scale(lambda_3(), Fraction(1, 2))
    ]


def singlet_fraction(m: Matrix) -> Fraction:
    n = len(m)
    tr_m = trace(m)
    norm = trace(matmul(m, m))
    if norm == 0:
        raise ValueError("zero-norm insertion")
    return (tr_m * tr_m / Fraction(n)) / norm


def adjoint_fraction(m: Matrix) -> Fraction:
    return Fraction(1) - singlet_fraction(m)


def main() -> int:
    print("=" * 78)
    print("R_conn vertex-color singlet projection bounded theorem companion")
    print("Exact rational checks; no matching-rule coefficient is derived here.")
    print("=" * 78)

    print("\nPart 0: source anchors")
    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    check("source note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    check("Fierz convention note exists", FIERZ.exists(), str(FIERZ.relative_to(ROOT)))
    check("source note declares bounded_theorem", "**Type:** bounded_theorem" in note_text)
    check(
        "source note keeps kappa identification out of scope",
        "does **not** assert" in note_text and "kappa_EW = rho_singlet" in note_text,
    )
    check("source note has primary runner link", "audit_companion_rconn_vertex_color_singlet_projection_bounded_2026_05_17.py" in note_text)

    print("\nPart 1: identity insertion")
    for n in (2, 3, 4, 5):
        m = eye(n)
        rho_s = singlet_fraction(m)
        rho_a = adjoint_fraction(m)
        check(f"N_c={n}: rho_singlet(I)=1", rho_s == Fraction(1), f"rho={rho_s}")
        check(f"N_c={n}: rho_adjoint(I)=0", rho_a == Fraction(0), f"rho={rho_a}")

    print("\nPart 2: exact SU(3) traceless generator witnesses")
    for idx, gen in enumerate(su3_symmetric_generators(), 1):
        norm = trace(matmul(gen, gen))
        check(f"generator {idx}: symmetric rational witness", is_symmetric(gen))
        check(f"generator {idx}: traceless", trace(gen) == 0, f"Tr={trace(gen)}")
        check(f"generator {idx}: normalized Tr[t^2]=1/2", norm == Fraction(1, 2), f"norm={norm}")
        check(f"generator {idx}: rho_singlet=0", singlet_fraction(gen) == 0)
        check(f"generator {idx}: rho_adjoint=1", adjoint_fraction(gen) == 1)

    print("\nPart 3: rational Hermitian witnesses")
    witnesses: list[Matrix] = [
        [
            [Fraction(2), Fraction(0), Fraction(0)],
            [Fraction(0), Fraction(-3, 2), Fraction(0)],
            [Fraction(0), Fraction(0), Fraction(5, 4)],
        ],
        [
            [Fraction(1, 3), Fraction(2, 5), Fraction(-1, 7)],
            [Fraction(2, 5), Fraction(0), Fraction(3, 11)],
            [Fraction(-1, 7), Fraction(3, 11), Fraction(-2)],
        ],
        [
            [Fraction(3, 2), Fraction(1, 4), Fraction(0)],
            [Fraction(1, 4), Fraction(3, 2), Fraction(0)],
            [Fraction(0), Fraction(0), Fraction(3, 2)],
        ],
    ]
    for idx, m in enumerate(witnesses, 1):
        rho_s = singlet_fraction(m)
        rho_a = adjoint_fraction(m)
        check(f"witness {idx}: symmetric", is_symmetric(m))
        check(f"witness {idx}: rho_singlet + rho_adjoint = 1", rho_s + rho_a == 1)
        check(f"witness {idx}: rho_singlet in [0,1]", 0 <= rho_s <= 1, f"rho={rho_s}")

    print("\nPart 4: zero singlet fraction iff trace zero")
    for alpha_num in (-2, -1, 0, 1, 2):
        for beta_num in (-2, -1, 0, 1, 2):
            alpha = Fraction(alpha_num, 3)
            beta = Fraction(beta_num, 5)
            if alpha == 0 and beta == 0:
                continue
            m = add(scale(eye(3), alpha), scale(lambda_3(), beta))
            rho_zero = singlet_fraction(m) == 0
            trace_zero = trace(m) == 0
            check(
                f"alpha={alpha}, beta={beta}: rho_singlet=0 iff Tr=0",
                rho_zero == trace_zero,
                f"rho={singlet_fraction(m)}, Tr={trace(m)}",
            )

    print("\nPart 5: explicit non-claim boundary")
    forbidden_phrases = [
        "kappa_EW(M_color)  =",
        "kappa_EW is fixed exactly",
        "physical EW current realizes",
    ]
    for phrase in forbidden_phrases:
        check(f"source avoids overclaim phrase: {phrase}", phrase not in note_text)

    print()
    print("=" * 78)
    print(f"RESULT: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
