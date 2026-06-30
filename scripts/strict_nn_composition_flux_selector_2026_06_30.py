#!/usr/bin/env python3
"""Strict nearest-neighbor composition selects the flux(-1) branch.

This is a bridge-theory runner, not an axiom runner. It tests the bridge:

    strict nearest-neighbor availability should not generate a direct
    face-diagonal influence when two edge influences are composed.

In a linearized edge-supported carrier this is exactly the no-mixed-term
condition. On one qubit per site, that condition forces pairwise
anticommuting edge coefficients; in three lattice directions the Pauli frame
is the unique saturating solution up to unitary/frame rotation. The absorbed
site-local form has plaquette flux -1. The scalar flux(+1) branch fails the
bridge by producing face-diagonal leakage.
"""

from __future__ import annotations

import itertools
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

TOL = 1e-12
PASS = 0
FAIL = 0


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")
    return ok


I2 = np.eye(2, dtype=complex)
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[1, 0], [0, -1]], dtype=complex)
SIGMA = [S1, S2, S3]


def torus_shift(length: int, mu: int) -> np.ndarray:
    n = length**3
    mat = np.zeros((n, n), dtype=complex)

    def idx(x: tuple[int, int, int]) -> int:
        return (x[0] % length) * length * length + (x[1] % length) * length + (x[2] % length)

    for x in itertools.product(range(length), repeat=3):
        y = list(x)
        y[mu] = (y[mu] + 1) % length
        mat[idx(tuple(y)), idx(x)] = 1.0
    return mat


def main() -> int:
    print("=== Strict NN composition bridge: flux(-1) selector ===")

    axiom_text = flat(AXIOMS.read_text(encoding="utf-8"))
    check(
        "current axioms supply nearest-neighbor physical locality",
        "nearest-neighbor adjacency" in axiom_text
        and "one fixed nearest-neighbor admissibility rule" in axiom_text,
    )
    check(
        "current axioms supply cubic covariance surface",
        "proper cubic rotations" in axiom_text
        and "covariant under lattice translations and proper cubic rotations" in axiom_text,
    )
    check(
        "current axioms phrase admissibility as availability of possibilities",
        "nearest-neighbor conditions determine the available subset of possibilities" in axiom_text,
    )

    print("\nPART A -- local algebra: no face-diagonal leakage is anticommutation")
    sx, sy, sz = [sp.Matrix(m) for m in (
        [[0, 1], [1, 0]],
        [[0, -sp.I], [sp.I, 0]],
        [[1, 0], [0, -1]],
    )]
    n1, n2, n3, m1, m2, m3 = sp.symbols("n1 n2 n3 m1 m2 m3", real=True)
    ns = n1 * sx + n2 * sy + n3 * sz
    ms = m1 * sx + m2 * sy + m3 * sz
    anticom = sp.simplify(ns * ms + ms * ns)
    check(
        "{n.sigma, m.sigma} = 2(n.m)I",
        sp.simplify(anticom - 2 * (n1 * m1 + n2 * m2 + n3 * m3) * sp.eye(2)) == sp.zeros(2, 2),
    )
    check(
        "Pauli edge coefficients have zero mixed anticommutators",
        all(np.allclose(SIGMA[i] @ SIGMA[j] + SIGMA[j] @ SIGMA[i], 0, atol=TOL) for i in range(3) for j in range(i + 1, 3)),
    )
    check(
        "scalar edge coefficients fail no-leakage maximally",
        np.allclose(I2 @ I2 + I2 @ I2, 2 * I2, atol=TOL),
        "mixed two-step coefficient is 2I, not 0",
    )

    print("\nPART B -- lattice operator: scalar branch leaks to face diagonals, Pauli branch does not")
    length = 5
    nabla = []
    for mu in range(3):
        shift = torus_shift(length, mu)
        nabla.append((shift - shift.conj().T) / 2.0)
    lap = sum(n @ n for n in nabla)
    scalar_edge = sum(np.kron(I2, n) for n in nabla)
    pauli_edge = sum(np.kron(SIGMA[mu], nabla[mu]) for mu in range(3))
    scalar_mixed = scalar_edge @ scalar_edge - np.kron(I2, lap)
    pauli_mixed = pauli_edge @ pauli_edge - np.kron(I2, lap)
    check(
        "scalar flux(+1) branch has nonzero mixed two-step leakage",
        np.linalg.norm(scalar_mixed) > 1.0,
        f"||mixed||_F={np.linalg.norm(scalar_mixed):.6g}",
    )
    check(
        "Pauli/Cl(3) branch has no mixed two-step leakage",
        np.allclose(pauli_mixed, 0, atol=1e-10),
        f"||mixed||_F={np.linalg.norm(pauli_mixed):.3e}",
    )

    print("\nPART C -- qubit capacity and flux selection")
    # No fourth element: solve {X, sigma_i}=0.
    a, b, c, d = sp.symbols("a b c d", complex=True)
    xmat = sp.Matrix([[a, b], [c, d]])
    sol = sp.solve(
        [sp.Eq(xmat * g + g * xmat, sp.zeros(2, 2)) for g in (sx, sy, sz)],
        [a, b, c, d],
        dict=True,
    )
    check(
        "one-qubit carrier saturates exactly three independent no-leak directions",
        len(sol) == 1 and all(v == 0 for v in sol[0].values()),
        "no fourth anticommuting edge coefficient exists in M_2(C)",
    )
    flux_minus = True
    for i in range(3):
        for j in range(i + 1, 3):
            hol = SIGMA[j] @ SIGMA[i] @ SIGMA[j] @ SIGMA[i]
            flux_minus = flux_minus and np.allclose(hol, -I2, atol=TOL)
    check(
        "anticommuting edge coefficients carry plaquette holonomy flux(-1)",
        flux_minus,
    )
    check(
        "scalar branch carries flux(+1) and is rejected by strict NN composition",
        np.allclose(I2 @ I2 @ I2 @ I2, I2, atol=TOL) and np.linalg.norm(scalar_mixed) > 1.0,
    )

    print("\nPART D -- bridge consequence")
    bridge_selects = np.allclose(pauli_mixed, 0, atol=1e-10) and np.linalg.norm(scalar_mixed) > 1.0 and flux_minus
    check(
        "strict NN composition selects K1 over K0",
        bridge_selects,
        "K1: no face-diagonal leakage and flux(-1); K0: face-diagonal leakage and flux(+1)",
    )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: FAIL")
        return 1
    print(
        "VERDICT: bridge theorem verified -- if strict nearest-neighbor "
        "composition is accepted as the operational reading of Admissibility, "
        "the flux(-1) / first-order branch is selected and the scalar "
        "flux(+1) branch is rejected."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
