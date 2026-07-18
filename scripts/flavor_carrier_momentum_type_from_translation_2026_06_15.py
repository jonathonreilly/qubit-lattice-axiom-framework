#!/usr/bin/env python3
"""Exact finite translation-character profiles and projectors certificate.

The certificate constructs the periodic 2x2x2 translations, all eight
Z_2^3 characters, the supplied hw=1 C_3 orbit, symbolic diagonal-operator
expectations, and the complete rank-one projector expectation matrix.  It
assigns no physical generation, flavor, carrier, observable, or readout role.

Use ``--mutation NAME`` to apply one reviewer-reproducible defect.  Every
listed defect breaks the exact check family named by the mutation and makes
the runner exit nonzero.
"""

from __future__ import annotations

import argparse
import itertools
from collections.abc import Callable

import sympy as sp


MUTATIONS = (
    "translation_direction",
    "character_phase",
    "normalization",
    "site_ordering",
    "c3_map",
    "weight_dependence",
    "projector_label",
)

Site = tuple[int, int, int]
SITES: tuple[Site, ...] = tuple(itertools.product((0, 1), repeat=3))
CORNERS: tuple[Site, ...] = SITES
HW1: tuple[Site, ...] = tuple(k for k in CORNERS if sum(k) == 1)


def translation_matrix(axis: int, sites: tuple[Site, ...], step: int = 1) -> sp.Matrix:
    """Return the exact permutation matrix for n -> n + step*e_axis mod 2."""

    index = {site: i for i, site in enumerate(sites)}
    matrix = sp.zeros(len(sites))
    for source, site in enumerate(sites):
        target_site = list(site)
        target_site[axis] = (target_site[axis] + step) % 2
        matrix[index[tuple(target_site)], source] = 1
    return matrix


def permutation_matrix(
    mapping: Callable[[Site], Site], sites: tuple[Site, ...]
) -> sp.Matrix:
    index = {site: i for i, site in enumerate(sites)}
    matrix = sp.zeros(len(sites))
    for source, site in enumerate(sites):
        matrix[index[mapping(site)], source] = 1
    return matrix


def character_vector(k: Site, character_sites: tuple[Site, ...]) -> sp.Matrix:
    root_eight = sp.sqrt(8)
    return sp.Matrix(
        [(-1) ** sum(ki * ni for ki, ni in zip(k, n)) / root_eight for n in character_sites]
    )


class Certificate:
    def __init__(self, mutation: str | None) -> None:
        self.mutation = mutation
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        passed = bool(condition)
        if passed:
            self.pass_count += 1
        else:
            self.fail_count += 1
        suffix = f"  ({detail})" if detail else ""
        print(f"  [{'PASS' if passed else 'FAIL'}] {label}{suffix}")

    def run(self) -> int:
        identity = sp.eye(8)
        canonical_translations = [translation_matrix(axis, SITES) for axis in range(3)]
        translations = list(canonical_translations)
        if self.mutation == "translation_direction":
            # On Z_2, +e_x and -e_x coincide.  A discriminating direction-step
            # mutation therefore replaces +e_x by the zero step.
            translations[0] = translation_matrix(0, SITES, step=0)

        self.check(
            "A1 exact +e_mu periodic translation matrices are unitary permutations",
            all(matrix.T * matrix == identity for matrix in translations)
            and all(matrix == expected for matrix, expected in zip(translations, canonical_translations)),
        )
        self.check(
            "A2 the three translation matrices commute",
            all(
                translations[i] * translations[j] == translations[j] * translations[i]
                for i in range(3)
                for j in range(3)
            ),
        )

        character_sites = list(SITES)
        if self.mutation == "site_ordering":
            character_sites[1], character_sites[4] = character_sites[4], character_sites[1]
        characters = {
            k: character_vector(k, tuple(character_sites))
            for k in CORNERS
        }
        mutation_target = HW1[0]
        if self.mutation == "character_phase":
            characters[mutation_target][0] *= -1
        if self.mutation == "normalization":
            characters[mutation_target] = 2 * characters[mutation_target]

        character_matrix = sp.Matrix.hstack(*(characters[k] for k in CORNERS))
        self.check(
            "A3 the eight character vectors form an exact orthonormal basis",
            character_matrix.T * character_matrix == identity,
            detail=f"basis_size={character_matrix.cols}",
        )

        eigen_ok = all(
            translations[axis] * characters[k] == ((-1) ** k[axis]) * characters[k]
            for k in CORNERS
            for axis in range(3)
        )
        self.check(
            "A4 every character is a simultaneous eigenvector with its stated joint character",
            eigen_ok,
        )

        def canonical_cycle(value: Site) -> Site:
            return (value[2], value[0], value[1])

        def identity_cycle(value: Site) -> Site:
            return value

        cycle = identity_cycle if self.mutation == "c3_map" else canonical_cycle
        rotation = permutation_matrix(cycle, SITES)
        orbit = [HW1[0]]
        while cycle(orbit[-1]) not in orbit:
            orbit.append(cycle(orbit[-1]))
        joint_characters = {k: tuple((-1) ** component for component in k) for k in HW1}
        c3_ok = (
            len(set(joint_characters.values())) == 3
            and len(orbit) == 3
            and set(orbit) == set(HW1)
            and rotation**3 == identity
            and all(rotation * characters[k] == characters[cycle(k)] for k in CORNERS)
        )
        self.check(
            "A5 the supplied hw=1 subset has three distinct characters and one transitive C_3 orbit",
            c3_ok,
            detail=f"hw1={list(HW1)}, orbit={orbit}",
        )

        uniform_profile = tuple(sp.Rational(1, 8) for _ in SITES)
        profiles = {
            k: tuple(sp.simplify(value * sp.conjugate(value)) for value in characters[k])
            for k in CORNERS
        }
        self.check(
            "A6 every character has the exact uniform position probability profile",
            all(profile == uniform_profile for profile in profiles.values()),
            detail=f"profile={uniform_profile}",
        )

        weights = sp.symbols("w_000 w_001 w_010 w_011 w_100 w_101 w_110 w_111")
        diagonal_operator = sp.diag(*weights)
        expected_mean = sum(weights) / 8
        if self.mutation == "weight_dependence":
            expected_mean += weights[0]
        expectation_residuals = tuple(
            sp.simplify(
                (characters[k].T * diagonal_operator * characters[k])[0]
                - expected_mean
            )
            for k in CORNERS
        )
        self.check(
            "A7 arbitrary symbolic diagonal weights give the exact one-eighth sum",
            all(residual == 0 for residual in expectation_residuals),
            detail=f"residuals={expectation_residuals}",
        )

        projectors = {k: characters[k] * characters[k].T for k in CORNERS}
        if self.mutation == "projector_label":
            first, second = HW1[:2]
            projectors[first], projectors[second] = projectors[second], projectors[first]

        self.check(
            "A8 the rank-one character projectors are orthogonal idempotents",
            all(projectors[k] * projectors[k] == projectors[k] for k in CORNERS)
            and all(
                projectors[k] * projectors[q] == sp.zeros(8)
                for k in CORNERS
                for q in CORNERS
                if k != q
            ),
        )
        self.check(
            "A9 the eight character projectors resolve the identity",
            sum(projectors.values(), sp.zeros(8)) == identity,
        )

        expectation_matrix = sp.Matrix(
            8,
            8,
            lambda i, j: sp.simplify(
                (characters[CORNERS[i]].T * projectors[CORNERS[j]] * characters[CORNERS[i]])[0]
            ),
        )
        hw1_indices = [CORNERS.index(k) for k in HW1]
        supplied_submatrix = expectation_matrix.extract(hw1_indices, hw1_indices)
        self.check(
            "A10 the full projector expectation matrix is Kronecker delta",
            expectation_matrix == identity and supplied_submatrix == sp.eye(3),
            detail=f"hw1_matrix={supplied_submatrix.tolist()}",
        )

        print(f"FULL PROJECTOR EXPECTATION MATRIX: {expectation_matrix.tolist()}")
        print(f"TOTAL: PASS={self.pass_count} FAIL={self.fail_count}")
        return 1 if self.fail_count else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mutation", choices=MUTATIONS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print("Finite translation-character profiles and projectors")
    if args.mutation:
        print(f"MUTATION ACTIVE: {args.mutation}")
    return Certificate(args.mutation).run()


if __name__ == "__main__":
    raise SystemExit(main())
