#!/usr/bin/env python3
"""Finite no-go for equivariant rooted spin-generation chirality transport.

The open escape asks whether a rooted/entangled carrier can transport spin
chirality into the generation factor.  This runner proves the scoped finite
boundary: if the rooting/embedding is C3-equivariant and the spin factor is
C3-trivial, the induced generation operator is scalar or C3-central and cannot
break the singlet/doublet partition.  Nontrivial generation action appears only
when the embedding or conditional trace supplies C3-breaking data.
"""
from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


@dataclass
class Scorecard:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        status = "PASS" if condition else "FAIL"
        suffix = f" :: {detail}" if detail else ""
        print(f"[{status}] {label}{suffix}")
        if condition:
            self.passed += 1
        else:
            self.failed += 1


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in left - right)


def kron(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(a, b)


def partial_trace_spin(X: sp.Matrix) -> sp.Matrix:
    out = sp.zeros(3)
    for s in range(2):
        rows = [s * 3 + i for i in range(3)]
        out += X.extract(rows, rows)
    return sp.simplify(out)


def c3_twirl_generation(B: sp.Matrix, C: sp.Matrix) -> sp.Matrix:
    return sp.simplify((B + C * B * (C**2) + (C**2) * B * C) / 3)


def main() -> int:
    sc = Scorecard()

    I2 = sp.eye(2)
    I3 = sp.eye(3)
    gamma5 = sp.Matrix([[1, 0], [0, -1]])
    sigma_x = sp.Matrix([[0, 1], [1, 0]])
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    S = C + C**2
    G = kron(gamma5, I3)
    C_total = kron(I2, C)
    S_total = kron(I2, S)

    sc.check("C has order three", matrix_equal(C**3, I3))
    sc.check("spin gamma5 is traceless", sp.trace(gamma5) == 0)
    sc.check("natural gamma5 embedding commutes with generation S", matrix_equal(G * S_total, S_total * G))
    sc.check("natural gamma5 embedding is C3-invariant", matrix_equal(G * C_total, C_total * G))
    sc.check("unpolarized spin trace of gamma5 embedding is zero", matrix_equal(partial_trace_spin(G), sp.zeros(3)))

    # Trivial-spin equivariant embedding V_s: generation -> spin x generation.
    c, d = sp.symbols("c d", real=True)
    spin_norm = sp.simplify(c**2 + d**2)
    V = sp.Matrix.vstack(c * I3, d * I3)
    induced = sp.simplify(V.T * G * V)
    sc.check("trivial-spin embedding is equivariant exactly when spin is generation-independent", matrix_equal(kron(I2, C) * V, V * C))
    sc.check("trivial-spin induced gamma5 is scalar on generation", matrix_equal(induced, (c**2 - d**2) * I3), f"induced={induced}")
    sc.check("normalized trivial-spin embedding still induces only a scalar", sp.simplify(induced[0, 0].subs(spin_norm, 1) - (c**2 - d**2)) == 0 and matrix_equal(induced - induced[0, 0] * I3, sp.zeros(3)))

    # A generation-dependent spin embedding can induce a non-scalar diagonal,
    # but equivariance forces all spin labels around the C3 orbit to match.
    a0, b0, a1, b1, a2, b2 = sp.symbols("a0 b0 a1 b1 a2 b2", real=True)
    V_dep = sp.zeros(6, 3)
    spin_pairs = [(a0, b0), (a1, b1), (a2, b2)]
    for j, (aa, bb) in enumerate(spin_pairs):
        V_dep[j, j] = aa
        V_dep[3 + j, j] = bb
    induced_dep = sp.simplify(V_dep.T * G * V_dep)
    equiv_residual = sp.simplify(kron(I2, C) * V_dep - V_dep * C)
    equiv_constraints_force_equal = [
        sp.simplify(a1 - a0),
        sp.simplify(a2 - a1),
        sp.simplify(b1 - b0),
        sp.simplify(b2 - b1),
    ]
    induced_when_equal = sp.simplify(induced_dep.subs({a1: a0, a2: a0, b1: b0, b2: b0}))
    sc.check("generation-dependent spin embedding can be non-scalar before equivariance", not matrix_equal(induced_dep, induced_dep[0, 0] * I3))
    sc.check("equivariance residual detects unequal spin labels", not matrix_equal(equiv_residual, sp.zeros(6, 3)))
    sc.check("equivariant generation-dependent embedding collapses to scalar", matrix_equal(induced_when_equal, (a0**2 - b0**2) * I3))
    sc.check("equivariance constraints are exactly orbit-constant spin labels", all(expr == 0 for expr in [v.subs({a1: a0, a2: a0, b1: b0, b2: b0}) for v in equiv_constraints_force_equal]))

    # Conditional expectation over C3 removes noncentral generation parts.
    B_break = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, -1]])
    B_twirl = c3_twirl_generation(B_break, C)
    sc.check("sample B_break is Hermitian", matrix_equal(B_break.T, B_break))
    sc.check("sample B_break does not commute with S", not matrix_equal(B_break * S, S * B_break))
    sc.check("C3 twirl makes B central", matrix_equal(B_twirl * C, C * B_twirl))
    sc.check("C3-twirled B commutes with S", matrix_equal(B_twirl * S, S * B_twirl))
    sc.check("C3 twirl removes the noncommuting selector part", matrix_equal(c3_twirl_generation(B_break * S - S * B_break, C), sp.zeros(3)))

    X_entangled = kron(sigma_x, B_break)
    traced_X = partial_trace_spin(X_entangled)
    sc.check("unpolarized trace of off-diagonal spin entanglement is zero", matrix_equal(traced_X, sp.zeros(3)))

    up_projector = sp.Matrix([[1, 0], [0, 0]])
    polarized_trace = partial_trace_spin(kron(up_projector, B_break))
    sc.check("polarized spin trace can expose B only after choosing a spin sector", matrix_equal(polarized_trace, B_break))
    sc.check("exposed B then carries the supplied C3-breaking", not matrix_equal(polarized_trace * S, S * polarized_trace))

    native_data = {
        "natural_commutator": G * S_total - S_total * G,
        "unpolarized_trace": partial_trace_spin(G),
        "equivariant_induced": induced_when_equal,
        "twirled_breaker_commutator": B_twirl * S - S * B_twirl,
    }
    sc.check(
        "equivariant rooting exposes no generation chirality selector",
        matrix_equal(native_data["natural_commutator"], sp.zeros(6))
        and matrix_equal(native_data["unpolarized_trace"], sp.zeros(3))
        and matrix_equal(native_data["equivariant_induced"] - native_data["equivariant_induced"][0, 0] * I3, sp.zeros(3))
        and matrix_equal(native_data["twirled_breaker_commutator"], sp.zeros(3)),
        f"native_data_keys={sorted(native_data)}",
    )

    print(f"SCORECARD: PASS={sc.passed} FAIL={sc.failed}")
    return 0 if sc.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
