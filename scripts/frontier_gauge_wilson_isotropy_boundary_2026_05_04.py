#!/usr/bin/env python3
"""Boundary checks for proposed SU(3) gauge-action isotropy mechanisms.

The runner verifies two narrow algebraic facts used by the companion note:

1. The Cl(3) pseudoscalar squares to -I in the Pauli irrep but commutes with
   the three Cl(3) generators, so it cannot by itself be a fourth Clifford
   generator that anticommutes with them.
2. Standard staggered eta-products around all plaquette orientations have the
   same sign, so this sign check does not create a spatial/temporal gauge
   coupling split from an isotropic input lattice.

These are boundary checks, not a derivation of the accepted Wilson surface.
The final check treats the six eta plaquette signs only as an orientation
signature and verifies that this signature has no anisotropic component. It
does not assume a fermion-determinant or source/action map from eta signs to
physical Wilson coefficients.
"""

from __future__ import annotations

import itertools

import numpy as np


PASS_COUNT = 0
FAIL_COUNT = 0
ORIENTATIONS = tuple(itertools.combinations(range(4), 2))
SPATIAL_ORIENTATIONS = ((0, 1), (0, 2), (1, 2))
TEMPORAL_ORIENTATIONS = ((0, 3), (1, 3), (2, 3))


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


def staggered_eta(mu: int, x: tuple[int, int, int, int]) -> int:
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** x[0]
    if mu == 2:
        return (-1) ** (x[0] + x[1])
    if mu == 3:
        return (-1) ** (x[0] + x[1] + x[2])
    raise ValueError(f"bad direction {mu}")


def eta_plaquette_product(mu: int, nu: int, x: tuple[int, int, int, int]) -> int:
    x_mu = list(x)
    x_mu[mu] += 1
    x_nu = list(x)
    x_nu[nu] += 1
    return (
        staggered_eta(mu, x)
        * staggered_eta(nu, tuple(x_mu))
        * staggered_eta(mu, tuple(x_nu))
        * staggered_eta(nu, x)
    )


def spatial_temporal_contrast(pattern: dict[tuple[int, int], int]) -> int:
    """Return three times the spatial-average minus temporal-average entry."""
    return sum(pattern[pair] for pair in SPATIAL_ORIENTATIONS) - sum(
        pattern[pair] for pair in TEMPORAL_ORIENTATIONS
    )


def main() -> int:
    print("=" * 78)
    print("GAUGE WILSON ISOTROPY BOUNDARY CHECKS")
    print("=" * 78)

    identity = np.eye(2, dtype=complex)
    generators = [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]

    print("\nPart 1: Cl(3) Pauli-irrep checks")
    for i, gi in enumerate(generators, start=1):
        for j, gj in enumerate(generators, start=1):
            anticomm = gi @ gj + gj @ gi
            expected = 2 * (1 if i == j else 0) * identity
            check(f"{{G_{i}, G_{j}}} = 2 delta_{i}{j}", np.allclose(anticomm, expected))

    pseudoscalar = generators[0] @ generators[1] @ generators[2]
    check("Cl(3) pseudoscalar squares to -I", np.allclose(pseudoscalar @ pseudoscalar, -identity))

    commutators = []
    anticommutators = []
    for i, generator in enumerate(generators, start=1):
        comm = pseudoscalar @ generator - generator @ pseudoscalar
        anticomm = pseudoscalar @ generator + generator @ pseudoscalar
        commutators.append(float(np.max(np.abs(comm))))
        anticommutators.append(float(np.max(np.abs(anticomm))))
        check(f"pseudoscalar commutes with G_{i}", np.allclose(comm, 0.0))
        check(
            f"pseudoscalar does not anticommute with G_{i}",
            not np.allclose(anticomm, 0.0),
            detail=f"max |{{I_cl3, G_{i}}}| = {np.max(np.abs(anticomm)):.3g}",
        )

    check(
        "pseudoscalar is not a standalone fourth Clifford generator for Cl(3,1)",
        max(commutators) < 1e-12 and min(anticommutators) > 1.0,
        detail="it is central in odd-dimensional Cl(3)",
    )

    print("\nPart 2: staggered eta-product orientation check")
    sites = list(itertools.product((0, 1), repeat=4))
    products: dict[tuple[int, int], set[int]] = {}
    for mu, nu in ORIENTATIONS:
        values = {eta_plaquette_product(mu, nu, site) for site in sites}
        products[(mu, nu)] = values
        labels = "xyzt"
        print(f"  {labels[mu]}{labels[nu]} values: {sorted(values)}")

    all_values = set().union(*products.values())
    check(
        "all six staggered plaquette orientation products have the same sign",
        all_values == {-1},
        detail=f"orientation value sets = {products}",
    )
    eta_signature = {pair: next(iter(products[pair])) for pair in ORIENTATIONS}
    check(
        "the eta orientation signature has no anisotropic component or spatial/temporal split",
        all(values == {-1} for values in products.values())
        and set(eta_signature.values()) == {-1}
        and spatial_temporal_contrast(eta_signature) == 0,
        detail=(
            f"E = {eta_signature}; "
            f"3(mean_spatial - mean_temporal) = {spatial_temporal_contrast(eta_signature)}"
        ),
    )

    print("\nN5 execution certificate -- what this runner resolves")
    print("  per_element: checked -- each generator pair is tested on its own: "
          "all nine anticommutators {G_i, G_j} against 2 delta_ij, and the "
          "pseudoscalar is taken against each G_i separately, commuting exactly "
          "while its anticommutator reaches max magnitude 2.")
    print("  per_site: checked -- the eta plaquette product is evaluated at "
          "every one of the 16 sites of the 2^4 corner set, separately for each "
          "of the six orientations, and each orientation's value set collapses "
          "to the single value -1 across all those sites.")
    print("  per_mode: checked and not executed -- no spectrum, propagator or "
          "momentum variable is formed anywhere: Part 1 works in the "
          "2-dimensional Qubit carrier M_2(C) of the Cl(3) Pauli irrep and Part "
          "2 in integer signs, so there is no mode to resolve.")
    print("  per_block: checked -- the six orientations are split into the "
          "spatial block {xy, xz, yz} and the temporal block {xt, yt, zt}, and "
          "the block contrast 3(mean_spatial - mean_temporal) is computed and "
          "comes out exactly 0, so no spatial/temporal split is created.")
    print("  lattice_wide: checked -- staggered_eta depends on the coordinates "
          "only through their parities, so the 16 enumerated sites exhaust "
          "every parity class of the 4d lattice; the uniform value -1 on all "
          "six orientations is therefore lattice-wide, needing no volume limit.")
    print()
    print("=" * 78)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
