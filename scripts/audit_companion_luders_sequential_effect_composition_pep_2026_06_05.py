#!/usr/bin/env python3
"""Finite projection-compression trace identity for PEP.

This runner verifies the narrowed source theorem:

    P projection, E effect, rho density matrix
        -> PEP is a valid compressed effect
        -> Tr(rho PEP) = Tr(P rho P E)
        -> P(QFQ)P = (QP)^* F (QP)

It deliberately does not assert a Lueders measurement update, Born rule, or
probability interpretation for the trace scalar.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def is_zero_sym(M: sp.Matrix) -> bool:
    M = sp.simplify(M)
    return all(M[i, j] == 0 for i in range(M.rows) for j in range(M.cols))


def min_eig(M: np.ndarray) -> float:
    H = (M + M.conj().T) / 2.0
    return float(np.linalg.eigvalsh(H).min())


def random_density(d: int, rng: np.random.Generator) -> np.ndarray:
    A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    M = A @ A.conj().T
    return M / np.trace(M).real


def random_projection(d: int, rng: np.random.Generator) -> np.ndarray:
    A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    Q, _ = np.linalg.qr(A)
    rank = int(rng.integers(1, d + 1))
    V = Q[:, :rank]
    return V @ V.conj().T


def random_effect(d: int, rng: np.random.Generator) -> np.ndarray:
    B = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    H = (B + B.conj().T) / 2.0
    w, U = np.linalg.eigh(H)
    span = w.max() - w.min()
    w = (w - w.min()) / span if span > 1e-15 else np.zeros_like(w)
    return U @ np.diag(w) @ U.conj().T


def part0_note_boundary() -> None:
    print("\n=== Part 0: source-note boundary ===")
    check("companion note exists", NOTE.exists(), NOTE.relative_to(ROOT).as_posix())
    if not NOTE.exists():
        return
    text = NOTE.read_text(encoding="utf-8")
    check("note declares bounded-support source theorem", "bounded-support source theorem" in text)
    check("note does not claim Lueders/Born derivation", "does not obtain the Lüders state update, Born rule" in text)
    check("note states PEP trace identity", "Tr(rho P E P) = Tr(P rho P E)" in text)
    check("note marks measurement rows downstream only", "downstream context only" in text)


def part1_exact_d2() -> None:
    print("\n=== Part 1: exact d=2 compression identities ===")
    psi = sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5)])
    P = sp.simplify(psi * psi.T)
    U = sp.Matrix([[sp.Rational(5, 13), -sp.Rational(12, 13)], [sp.Rational(12, 13), sp.Rational(5, 13)]])
    E = sp.simplify(U * sp.diag(sp.Rational(3, 4), sp.Rational(1, 4)) * U.T)
    rho = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 5)], [sp.Rational(1, 5), sp.Rational(1, 3)]])
    I = sp.eye(2)
    PEP = sp.simplify(P * E * P)

    check("P is an orthogonal projection", is_zero_sym(P * P - P) and is_zero_sym(P - P.T))
    check("E is an effect with spectrum in [0,1]", all(0 <= ev <= 1 for ev in E.eigenvals().keys()))
    check("rho is a density matrix", sp.trace(rho) == 1 and all(ev >= 0 for ev in rho.eigenvals().keys()))
    check("PEP is Hermitian", is_zero_sym(PEP - PEP.T))
    check("PEP is positive", all(ev >= 0 for ev in PEP.eigenvals().keys()))
    check("P - PEP is positive", all(ev >= 0 for ev in sp.simplify(P - PEP).eigenvals().keys()))
    check("I - P is positive", all(ev >= 0 for ev in sp.simplify(I - P).eigenvals().keys()))
    check("trace identity Tr(rho PEP) = Tr(P rho P E)", sp.simplify(sp.trace(rho * PEP) - sp.trace(P * rho * P * E)) == 0)
    check("boundary PIP = P", is_zero_sym(P * I * P - P))
    check("boundary IEI = E", is_zero_sym(I * E * I - E))


def part2_numeric() -> None:
    print("\n=== Part 2: numeric d=2,3,4 compression checks ===")
    for d in (2, 3, 4):
        rng = np.random.default_rng(20260606 + d)
        trace_err = 0.0
        pep_floor = 0.0
        bound_floor = 0.0
        assoc_err = 0.0
        for _ in range(300):
            rho = random_density(d, rng)
            P = random_projection(d, rng)
            Q = random_projection(d, rng)
            E = random_effect(d, rng)
            F = random_effect(d, rng)
            PEP = P @ E @ P
            trace_err = max(trace_err, abs(np.trace(rho @ PEP) - np.trace(P @ rho @ P @ E)))
            pep_floor = min(pep_floor, min_eig(PEP))
            bound_floor = min(bound_floor, min_eig(P - PEP), min_eig(np.eye(d) - P))
            assoc_err = max(assoc_err, float(np.linalg.norm(P @ (Q @ F @ Q) @ P - (Q @ P).conj().T @ F @ (Q @ P))))
        check(f"d={d}: trace identity over 300 seeds", trace_err < 1e-9, f"max err={trace_err:.2e}")
        check(f"d={d}: PEP positive over 300 seeds", pep_floor > -1e-9, f"min eig={pep_floor:+.2e}")
        check(f"d={d}: 0 <= PEP <= P <= I over 300 seeds", bound_floor > -1e-9, f"min boundary eig={bound_floor:+.2e}")
        check(f"d={d}: nested compression identity over 300 seeds", assoc_err < 1e-9, f"max err={assoc_err:.2e}")


def part3_exact_nested_and_guard() -> None:
    print("\n=== Part 3: exact nested compression and Jordan guard ===")
    P = sp.diag(1, 1, 0)
    Q = sp.diag(1, 0, 0)
    F = sp.diag(sp.Rational(2, 3), sp.Rational(1, 2), sp.Rational(1, 5))
    E = sp.Matrix([[sp.Rational(1, 2), sp.Rational(2, 5)], [sp.Rational(2, 5), sp.Rational(1, 2)]])
    P2 = sp.Matrix([[1, 0], [0, 0]])
    rho2 = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 3)], [sp.Rational(1, 3), sp.Rational(1, 2)]])

    nested = sp.simplify(P * (Q * F * Q) * P)
    composed = sp.simplify((Q * P).T * F * (Q * P))
    check("exact nested identity P(QFQ)P = (QP)^*F(QP)", is_zero_sym(nested - composed))
    check("exact F=I boundary gives P Q P", is_zero_sym(P * (Q * sp.eye(3) * Q) * P - P * Q * P))
    check("nested compression is positive", all(ev >= 0 for ev in nested.eigenvals().keys()))

    pep = sp.simplify(P2 * E * P2)
    jordan = sp.simplify((P2 * E + E * P2) / 2)
    check("Jordan symmetrization differs from compression", not is_zero_sym(jordan - pep))
    check("Jordan guard: trace scalar differs on rho", sp.simplify(sp.trace(rho2 * jordan) - sp.trace(rho2 * pep)) != 0)


def main() -> int:
    print("FINITE PEP PROJECTION-COMPRESSION TRACE IDENTITY")
    part0_note_boundary()
    part1_exact_d2()
    part2_numeric()
    part3_exact_nested_and_guard()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
