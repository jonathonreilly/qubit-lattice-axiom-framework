#!/usr/bin/env python3
"""Finite C3 generation Berry/holonomy selector no-go.

This runner tests the scoped route:

    native C3 generation mass carrier
      -> Berry / holonomy readout
      -> K-reality or block-count selector.

For the C3-circulant carrier the central-sector projectors are constant
Fourier projectors.  Their Berry connection and curvature vanish exactly, so
holonomy has no native data with which to select K-reality, r=1/2, or an active
source branch.  Nontrivial projector motion can be introduced, but the sample
check shows it leaves the C3-central carrier and therefore supplies the missing
selector as extra structure.
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


def is_zero_matrix(mat: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in mat)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return is_zero_matrix(left - right)


def character_projector(k: int, C: sp.Matrix) -> sp.Matrix:
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    eye = sp.eye(3)
    return sp.simplify((eye + omega ** (-k) * C + omega ** (-2 * k) * (C**2)) / 3)


def main() -> int:
    sc = Scorecard()

    a, x, y = sp.symbols("a x y", real=True)
    eye = sp.eye(3)
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    C2 = C**2
    J = sp.ones(3)
    S = C + C2
    A = sp.I * (C - C2)
    H = a * eye + x * S + y * A

    P0 = character_projector(0, C)
    P1 = character_projector(1, C)
    P2 = character_projector(2, C)
    Pd = sp.simplify(P1 + P2)

    sc.check("C has order three", matrix_equal(C**3, eye), f"C^3={(C**3).tolist()}")
    sc.check("character projectors sum to identity", matrix_equal(P0 + P1 + P2, eye))
    sc.check("P0 is the singlet projector J/3", matrix_equal(P0, J / 3))
    sc.check("P1 and P2 fuse to the doublet projector", matrix_equal(Pd, eye - P0))
    sc.check(
        "character projectors are idempotent and orthogonal",
        matrix_equal(P0 * P0, P0)
        and matrix_equal(P1 * P1, P1)
        and matrix_equal(P2 * P2, P2)
        and matrix_equal(P0 * P1, sp.zeros(3))
        and matrix_equal(P1 * P2, sp.zeros(3)),
    )

    sc.check("native mass carrier is Hermitian", matrix_equal(H.H, H))
    sc.check("native mass carrier is C3-equivariant", matrix_equal(H * C, C * H))
    sc.check("all character projectors commute with H", matrix_equal(H * P0, P0 * H) and matrix_equal(H * P1, P1 * H) and matrix_equal(H * P2, P2 * H))
    sc.check("two-block singlet/doublet projector commutes with H", matrix_equal(H * Pd, Pd * H))

    zero = sp.zeros(3)
    derivs = {
        "P0_a": P0.diff(a),
        "P0_x": P0.diff(x),
        "P0_y": P0.diff(y),
        "Pd_a": Pd.diff(a),
        "Pd_x": Pd.diff(x),
        "Pd_y": Pd.diff(y),
        "P1_x": P1.diff(x),
        "P2_y": P2.diff(y),
    }
    sc.check(
        "central-sector projectors are parameter-constant",
        all(matrix_equal(mat, zero) for mat in derivs.values()),
        f"derivative_keys={sorted(derivs)}",
    )

    def berry_curvature(P: sp.Matrix, u: sp.Symbol, v: sp.Symbol) -> sp.Matrix:
        dpu = P.diff(u)
        dpv = P.diff(v)
        return sp.simplify(P * (dpu * dpv - dpv * dpu) * P)

    sc.check("singlet Berry curvature is zero", matrix_equal(berry_curvature(P0, x, y), zero))
    sc.check("doublet Wilczek-Zee curvature is zero", matrix_equal(berry_curvature(Pd, x, y), zero))
    sc.check("faithful-band Berry curvatures are zero", matrix_equal(berry_curvature(P1, x, y), zero) and matrix_equal(berry_curvature(P2, x, y), zero))

    lambda_0 = a + 2 * x
    lambda_1 = a - x + sp.sqrt(3) * y
    lambda_2 = a - x - sp.sqrt(3) * y
    split = sp.simplify(lambda_1 - lambda_2)
    sc.check("faithful-band split is 2 sqrt(3) y", sp.simplify(split - 2 * sp.sqrt(3) * y) == 0, f"split={split}")
    sc.check("K-real degeneracy condition is independent of x and a", sp.diff(split, x) == 0 and sp.diff(split, a) == 0)

    r = sp.simplify((x**2 + y**2) / a**2)
    r_conjugated = r.subs(y, -y)
    sc.check("K/CPT conjugation preserves r", sp.simplify(r - r_conjugated) == 0, f"r={r}")
    sc.check(
        "K-real line leaves the weight dial free",
        sp.simplify(r.subs(y, 0) - x**2 / a**2) == 0 and sp.diff(r.subs(y, 0), x) != 0,
        f"r|y=0={sp.simplify(r.subs(y, 0))}",
    )

    curvature_at_kreal = berry_curvature(Pd, x, y).subs({a: 2, x: 1, y: 0})
    curvature_off_kreal = berry_curvature(Pd, x, y).subs({a: 2, x: 1, y: 1})
    sc.check(
        "Berry curvature cannot distinguish K-real from non-K-real samples",
        matrix_equal(curvature_at_kreal, curvature_off_kreal) and matrix_equal(curvature_at_kreal, zero),
    )

    # A nontrivial moving-projector holonomy can be purchased by rotating the
    # carrier, but a generic rotation no longer commutes with the C3 shift.
    U = sp.Matrix(
        [
            [sp.Rational(3, 5), -sp.Rational(4, 5), 0],
            [sp.Rational(4, 5), sp.Rational(3, 5), 0],
            [0, 0, 1],
        ]
    )
    H_sample = H.subs({a: 3, x: 1, y: 1})
    H_rot = sp.simplify(U * H_sample * U.T)
    comm_rot = sp.simplify(H_rot * C - C * H_rot)
    sc.check("sample moving-projector rotation is orthogonal", matrix_equal(U.T * U, eye))
    sc.check(
        "sample moving-projector rotation leaves the C3-central carrier",
        not matrix_equal(comm_rot, zero),
        f"commutator_norm_sq={sp.simplify(sum(entry * sp.conjugate(entry) for entry in comm_rot))}",
    )

    # C3-preserving changes are polynomials in C on this multiplicity-free
    # carrier; they preserve the same central projectors and hence remain flat.
    q0, q1, q2 = sp.symbols("q0 q1 q2")
    U_central = q0 * eye + q1 * C + q2 * C2
    sc.check("central changes commute with C", matrix_equal(U_central * C, C * U_central))
    sc.check("central changes preserve P0", matrix_equal(U_central * P0, P0 * U_central))
    sc.check("central changes preserve Pd", matrix_equal(U_central * Pd, Pd * U_central))

    native_selector_data = {
        "berry_curvature": berry_curvature(Pd, x, y),
        "r_under_K": sp.simplify(r - r_conjugated),
        "kreal_split": split,
        "weight_on_kreal": sp.simplify(r.subs(y, 0)),
    }
    sc.check(
        "native Berry/holonomy data expose no r-half selector",
        matrix_equal(native_selector_data["berry_curvature"], zero)
        and native_selector_data["r_under_K"] == 0
        and sp.diff(native_selector_data["weight_on_kreal"], x) != 0,
        f"native_data={native_selector_data}",
    )

    print(f"eigenvalues: lambda0={lambda_0}, lambda1={lambda_1}, lambda2={lambda_2}")
    print(f"SCORECARD: PASS={sc.passed} FAIL={sc.failed}")
    return 0 if sc.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
