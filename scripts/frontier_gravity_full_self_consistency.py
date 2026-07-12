#!/usr/bin/env python3
"""Exact countermodel certificate for gravity full self-consistency.

The runner checks two narrow logical questions in
``docs/GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md``:

    With H_0=-Delta_lat and G_0=H_0^{-1} fixed, do the current framework
    premises force the separate field operator to obey L^{-1}=G_0?

    If the two inverse identities are granted, do the same premises select
    H=-Delta_lat?

Both answers are negative.  The fixed-H fields L=2H_0 and L=H_0(I+H_0)
violate the Green-map identity while preserving the named symmetries.  The
separate exact stencil family

    H_m = -Delta_lat + m^2 I,  m^2 > 0,
    G_m = H_m^{-1},
    L_m = H_m,

obeys both inverse identities and all spatial/operator symmetries used by the
positive argument, but L_m differs from the massless Poisson operator.

The finite-torus inverse checks are numerical companions.  The decisive
countermodel checks use integer Laurent stencils and exact symmetry tests.
"""

from __future__ import annotations

import itertools
import numpy as np


AUDIT_TIMEOUT_SEC = 120

Vec = tuple[int, int, int]
Stencil = dict[Vec, int]

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"[{status}] {label}")
    if detail:
        print(f"       {detail}")


def poisson_stencil() -> Stencil:
    stencil: Stencil = {(0, 0, 0): 6}
    for axis in range(3):
        for sign in (-1, 1):
            displacement = [0, 0, 0]
            displacement[axis] = sign
            stencil[tuple(displacement)] = -1
    return stencil


def add_mass(stencil: Stencil, mass_squared: int) -> Stencil:
    result = dict(stencil)
    result[(0, 0, 0)] += mass_squared
    return result


def convolve(left: Stencil, right: Stencil) -> Stencil:
    result: Stencil = {}
    for x, wx in left.items():
        for y, wy in right.items():
            z = tuple(x[i] + y[i] for i in range(3))
            result[z] = result.get(z, 0) + wx * wy
    return {x: weight for x, weight in result.items() if weight != 0}


def add_stencils(*terms: Stencil) -> Stencil:
    result: Stencil = {}
    for term in terms:
        for x, weight in term.items():
            result[x] = result.get(x, 0) + weight
    return {x: weight for x, weight in result.items() if weight != 0}


def determinant(matrix: np.ndarray) -> int:
    return int(round(np.linalg.det(matrix)))


def proper_cubic_rotations() -> list[np.ndarray]:
    rotations: list[np.ndarray] = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            if determinant(matrix) == 1:
                rotations.append(matrix)
    unique = {tuple(matrix.ravel()): matrix for matrix in rotations}
    return list(unique.values())


def transform(vector: Vec, rotation: np.ndarray) -> Vec:
    image = rotation @ np.asarray(vector, dtype=int)
    return tuple(int(value) for value in image)


def is_self_adjoint(stencil: Stencil) -> bool:
    return all(stencil.get(tuple(-x for x in vector), 0) == weight
               for vector, weight in stencil.items())


def is_cubic_invariant(stencil: Stencil,
                       rotations: list[np.ndarray]) -> bool:
    return all(stencil.get(transform(vector, rotation), 0) == weight
               for rotation in rotations
               for vector, weight in stencil.items())


def torus_matrix(stencil: Stencil, size: int) -> np.ndarray:
    sites = list(itertools.product(range(size), repeat=3))
    index = {site: position for position, site in enumerate(sites)}
    matrix = np.zeros((len(sites), len(sites)), dtype=float)
    for source in sites:
        row = index[source]
        for displacement, weight in stencil.items():
            target = tuple((source[i] + displacement[i]) % size
                           for i in range(3))
            matrix[row, index[target]] += weight
    return matrix


def fourier_symbol(stencil: Stencil, momentum: tuple[float, float, float]) -> float:
    value = 0.0j
    for displacement, weight in stencil.items():
        phase = sum(momentum[i] * displacement[i] for i in range(3))
        value += weight * np.exp(1j * phase)
    return float(value.real)


def character_symbol(stencil: Stencil, character: Vec) -> int:
    """Evaluate a Laurent stencil at an exact {+1,-1}^3 character."""
    total = 0
    for displacement, weight in stencil.items():
        monomial = 1
        for axis, power in enumerate(displacement):
            monomial *= character[axis] if power % 2 else 1
        total += weight * monomial
    return total


def exact_countermodels() -> tuple[Stencil, Stencil, Stencil]:
    print("\nEXACT LAURENT-STENCIL COUNTERMODELS")
    rotations = proper_cubic_rotations()
    h0 = poisson_stencil()
    h1 = add_mass(h0, 1)
    h2 = add_mass(h0, 2)
    fixed_h_field_long = add_stencils(h0, convolve(h0, h0))
    h_long = add_stencils(add_mass(h0, 1), convolve(h0, h0))

    check("proper cubic rotation group has 24 elements", len(rotations) == 24)
    for name, stencil in (("H_0", h0), ("H_1", h1),
                          ("H_2", h2),
                          ("L_fixed_H_long", fixed_h_field_long),
                          ("H_long", h_long)):
        check(f"{name} is exactly self-adjoint", is_self_adjoint(stencil))
        check(f"{name} is exactly proper-cubic invariant",
              is_cubic_invariant(stencil, rotations))

    check("H_1 is nearest-neighbor plus onsite",
          max(sum(abs(x) for x in displacement) for displacement in h1) == 1)
    check("H_2 is nearest-neighbor plus onsite",
          max(sum(abs(x) for x in displacement) for displacement in h2) == 1)
    check("H_long is a cubic-symmetric longer-range alternative",
          max(sum(abs(x) for x in displacement)
              for displacement in h_long) == 2)
    check("fixed-H field A(I+A) is a range-two alternative",
          max(sum(abs(x) for x in displacement)
              for displacement in fixed_h_field_long) == 2)

    check("H_1 differs exactly from massless Poisson",
          h1 != h0 and h1[(0, 0, 0)] - h0[(0, 0, 0)] == 1)
    check("H_2 differs exactly from H_1",
          h2 != h1 and h2[(0, 0, 0)] - h1[(0, 0, 0)] == 1)
    check("H_long differs exactly from every NN operator",
          any(sum(abs(x) for x in displacement) == 2
              for displacement in h_long))

    # At zero momentum, -Delta has symbol 0 whereas H_m has symbol m^2.
    zero = (0.0, 0.0, 0.0)
    check("massless Poisson has zero-momentum symbol 0",
          fourier_symbol(h0, zero) == 0.0)
    check("H_1 has zero-momentum symbol 1",
          fourier_symbol(h1, zero) == 1.0)
    check("H_2 has zero-momentum symbol 2",
          fourier_symbol(h2, zero) == 2.0)

    # Directly attack the audited bridge with the propagator held fixed.
    # On X=l2(Z3)xC2 let A=H_0 and G_0=A^{-1}:Ran(A)->X.  The field
    # operators L_c=cA have the same range and preserve every named symmetry,
    # but L_c^{-1}=c^{-1}G_0.  A single exact nonzero character witnesses the
    # unequal inverse multipliers without numerical inversion.
    character = (-1, 1, 1)  # k=(pi,0,0)
    a_symbol = character_symbol(h0, character)
    scaled_field_symbol = 2 * a_symbol
    long_field_symbol = character_symbol(fixed_h_field_long, character)
    check("fixed propagator H_0 has exact character symbol 4",
          a_symbol == 4)
    check("fixed-H scaled field inverse differs with the same map type",
          scaled_field_symbol == 8 and scaled_field_symbol != a_symbol,
          detail="(2H_0)^{-1}=G_0/2 on Ran(H_0)")
    check("fixed-H range-two field inverse differs with the same map type",
          long_field_symbol == 20 and long_field_symbol != a_symbol,
          detail="[H_0(I+H_0)]^{-1}=(I+H_0)^{-1}G_0 on Ran(H_0)")

    # The spatial stencils act as H tensor I_2.  This exact factor choice
    # commutes with every one-site Cl(3) generator.
    identity2 = np.eye(2, dtype=complex)
    sigma = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    check("internal factor commutes with all Cl(3) Pauli generators",
          all(np.array_equal(identity2 @ generator, generator @ identity2)
              for generator in sigma))
    return h0, h1, h2


def inverse_identity_companion(h0: Stencil, h1: Stencil, h2: Stencil) -> None:
    print("\nFINITE-TORUS INVERSE-ID COMPANION")
    size = 4
    identity = np.eye(size ** 3)
    for name, stencil in (("H_1", h1), ("H_2", h2)):
        h_matrix = torus_matrix(stencil, size)
        eigenvalues = np.linalg.eigvalsh(h_matrix)
        green = np.linalg.inv(h_matrix)
        field_operator = h_matrix.copy()
        residual_h = np.max(np.abs(h_matrix @ green - identity))
        residual_l = np.max(np.abs(field_operator @ green - identity))
        check(f"{name} is strictly positive and invertible",
              float(eigenvalues.min()) > 0.999999,
              detail=f"lambda_min={eigenvalues.min():.12g}")
        check(f"{name}: G_0 = H^(-1)", residual_h < 1e-12,
              detail=f"max residual={residual_h:.3e}")
        check(f"{name}: L^(-1) = G_0 with L=H", residual_l < 1e-12,
              detail=f"max residual={residual_l:.3e}")

    h0_matrix = torus_matrix(h0, size)
    h1_matrix = torus_matrix(h1, size)
    g1 = np.linalg.inv(h1_matrix)
    mismatch = np.linalg.norm(h0_matrix @ g1 - identity, ord=np.inf)
    check("control: substituting massless L into the H_1 Green identity fails",
          mismatch > 0.5,
          detail=f"||H_0 G_1-I||_inf={mismatch:.6g}")


def logical_conclusion() -> None:
    print("\nLOGICAL CONCLUSION")
    # Abstract scalar witnesses make the inversion content explicit without
    # relying on the finite matrix calculation.
    for h in (1, 2, 7):
        g = 1.0 / h
        l = h
        check(f"abstract inverse chain closes for h={h}",
              abs(h * g - 1.0) < 1e-15 and abs(l * g - 1.0) < 1e-15)

    print("\nWith H_0=-Delta_lat fixed, the framework symmetries permit")
    print("L=2H_0 and L=H_0(I+H_0), whose inverses are not G_0.")
    print("Therefore L^{-1}=G_0 is not forced by those symmetries.")
    print("If L^{-1}=G_0 is separately granted as equality of full inverse")
    print("graphs, inversion implies L=H.")
    print("The granted identities still do not imply H=-Delta_lat.")
    print("H_m=-Delta_lat+m^2 I (m^2>0) is an exact counterfamily.")
    print("If H=-Delta_lat is separately granted, then L=-Delta_lat follows")
    print("by inversion; that remains the exact conditional theorem.")


def main() -> int:
    print("=" * 78)
    print("GRAVITY FULL SELF-CONSISTENCY: EXACT UNDERDETERMINATION CERTIFICATE")
    print("=" * 78)
    h0, h1, h2 = exact_countermodels()
    inverse_identity_companion(h0, h1, h2)
    logical_conclusion()
    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("STATUS: EXACT_NEGATIVE_BOUNDARY" if FAIL == 0 else "STATUS: FAIL")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
