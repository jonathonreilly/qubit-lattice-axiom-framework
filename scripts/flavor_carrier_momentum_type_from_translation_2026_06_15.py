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


def general_sites(extent: int) -> tuple[Site, ...]:
    """Return the lexicographic site list of the periodic ``extent^3`` cell."""
    return tuple(itertools.product(range(extent), repeat=3))


def general_character(k: Site, extent: int, sites: tuple[Site, ...]) -> sp.Matrix:
    """Return the exact Z_extent^3 translation character on the supplied cell."""
    root = sp.sqrt(len(sites))
    return sp.Matrix(
        [
            sp.exp(
                2
                * sp.pi
                * sp.I
                * sp.Rational(sum(ki * ni for ki, ni in zip(k, n)), extent)
            )
            / root
            for n in sites
        ]
    )


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
        self.discipline_packet(translations, characters, projectors)
        print(f"TOTAL: PASS={self.pass_count} FAIL={self.fail_count}")
        return 1 if self.fail_count else 0

    def discipline_packet(
        self,
        translations: list[sp.Matrix],
        characters: dict[Site, sp.Matrix],
        projectors: dict[Site, sp.Matrix],
    ) -> None:
        """Execute and print current-cycle N1-N8 route and resolution evidence."""
        weights = sp.symbols("w0:8")
        diagonal = sp.diag(*weights)
        uniform_value = sum(weights) / 8
        wall = "position-diagonal linear operator on the supplied finite-cell site basis"

        print("DISCIPLINE PACKET (current-cycle live evidence for N1-N8)")
        print(
            f"  N2 wall={wall}; walls=[{wall}]; collapsed_wall_set=[{wall}]; "
            "pairwise_checks=[] because the scoped result has one wall; unresolved=[]"
        )

        u, v, x = sp.symbols("u0:8"), sp.symbols("v0:8"), sp.symbols("x0:8")
        product_operator = sp.diag(*u) * sp.diag(*v) * sp.diag(*x)
        product_value = sum(u[i] * v[i] * x[i] for i in range(8)) / 8
        self.check(
            "A11 N1 route route_diagonal_operator_algebra",
            all(
                sp.expand(
                    (characters[k].T * product_operator * characters[k])[0] - product_value
                )
                == 0
                for k in CORNERS
            ),
            detail=(
                "route_class=algebraic_rearrangement; honesty_marker=ATTEMPTED; "
                "disposition=CLOSED; mechanism=diagonal operator algebra under products; "
                "attempt=evaluate diag(u)diag(v)diag(x) with independent symbolic weights "
                "in all eight characters; outcome=the value is (1/8)sum_n u_n v_n x_n "
                "for every label, so this algebraic route does not separate them"
            ),
        )

        signatures = {
            k: tuple(
                sp.expand((characters[k].T * translations[a] * characters[k])[0])
                for a in range(3)
            )
            for k in CORNERS
        }
        self.check(
            "A12 N1 route route_translation_observable",
            len(set(signatures.values())) == 8
            and all(
                signatures[k] == tuple(sp.Integer((-1) ** k[a]) for a in range(3))
                for k in CORNERS
            )
            and all(translations[a][i, i] == 0 for a in range(3) for i in range(8)),
            detail=(
                "route_class=alternate_observable_or_readout; honesty_marker=ATTEMPTED; "
                "disposition=CLOSED; mechanism=translation observable outside the diagonal "
                "operator class; attempt=evaluate T_x,T_y,T_z expectations in all eight "
                "characters; outcome=the eight eigenvalue triples separate the labels, but "
                "every T_mu has zero site-basis diagonal and therefore leaves the scoped class"
            ),
        )

        mixture = sp.symbols("p0:8")
        projector_mixture = sum(
            (mixture[i] * projectors[CORNERS[i]] for i in range(8)), sp.zeros(8)
        )
        self.check(
            "A13 N1 route route_projector_state_mixture",
            sp.expand(
                sp.trace(projector_mixture * diagonal)
                - sum(mixture) * uniform_value
            )
            == 0,
            detail=(
                "route_class=boundary_or_initial_condition; honesty_marker=ATTEMPTED; "
                "disposition=CLOSED; mechanism=state-side linear projector mixture "
                "(normalized nonnegative mixtures are a special case); attempt=evaluate "
                "tr[(sum_k p_k P_k)O] for eight free symbolic p_k; outcome=the value is "
                "(sum_k p_k)(1/8)sum_n w_n, so the state route adds no label separation"
            ),
        )

        def joint_dimension(generators: tuple[int, ...], k: Site) -> int:
            stacked = sp.Matrix.vstack(
                *[
                    translations[a] - sp.Integer((-1) ** k[a]) * sp.eye(8)
                    for a in generators
                ]
            )
            return 8 - stacked.rank()

        witness = (characters[(0, 0, 0)] + characters[(0, 0, 1)]) / sp.sqrt(2)
        witness_profile = tuple(sp.simplify(sp.conjugate(e) * e) for e in witness)
        self.check(
            "A14 N1 route route_generator_subset_degeneracy",
            {joint_dimension((0, 1, 2), k) for k in CORNERS} == {1}
            and {joint_dimension((0, 1), k) for k in CORNERS} == {2}
            and all(
                sp.expand(translations[a] * witness - witness) == sp.zeros(8, 1)
                for a in (0, 1)
            )
            and witness_profile == (sp.Rational(1, 4), sp.Integer(0)) * 4,
            detail=(
                "route_class=symmetry_or_representation; honesty_marker=ATTEMPTED; "
                "disposition=CLOSED; mechanism=character representation degeneracy after "
                "changing the generator subset; attempt=compare joint eigenspace dimensions "
                "for {T_x,T_y,T_z} and subgroup {T_x,T_y}; outcome=the full group has only "
                "one-dimensional joint spaces, while the subgroup admits the displayed "
                "nonuniform witness and therefore changes a theorem hypothesis"
            ),
        )

        extent_uniform, extent_expectation = True, True
        for extent in (2, 3, 4):
            sites = general_sites(extent)
            count = len(sites)
            profiles = {
                k: [sp.simplify(sp.conjugate(e) * e) for e in general_character(k, extent, sites)]
                for k in sites
            }
            if any(p != sp.Rational(1, count) for k in sites for p in profiles[k]):
                extent_uniform = False
            general_weights = sp.symbols(f"g0:{count}")
            probe = sites[1]
            combined = sum(general_weights[i] * profiles[probe][i] for i in range(count))
            if sp.expand(combined - sum(general_weights) / count) != 0:
                extent_expectation = False
            rejector = sp.zeros(count, 1)
            rejector[0] = sp.Integer(1)
            if all(
                sp.simplify(sp.conjugate(e) * e) == sp.Rational(1, count) for e in rejector
            ):
                extent_uniform = False
        self.check(
            "A15 N1 route route_periodic_extent_variation",
            extent_uniform and extent_expectation,
            detail=(
                "route_class=lattice_scale_or_limit; honesty_marker=ATTEMPTED; "
                "disposition=CLOSED; mechanism=finite lattice extent variation; "
                "attempt=rebuild every Z_L^3 character for L=2,3,4 and test all profiles plus "
                "a symbolic diagonal probe; outcome=each tested finite lattice has profile "
                "1/L^3 and expectation (1/L^3)sum_n w_n; other extents are outside this claim"
            ),
        )

        statement = (
            "Within the supplied finite cell, a position-diagonal linear operator cannot"
            " separate the eight character labels by expectation value."
        )
        print(
            "  N5 rhetoric audit; resolution_classes_checked="
            "[per_element, per_site, per_mode, per_block, lattice_wide]; "
            "untested_resolutions=[]"
        )
        print(f'  N5 statement S1 phrase: "{statement}"')

        site_operators = [
            sp.diag(*[sp.Integer(1) if i == j else sp.Integer(0) for i in range(8)])
            for j in range(8)
        ]
        self.check(
            "A16 N5 resolution class per_element",
            all(
                sp.expand(
                    (characters[k].T * site_operators[j] * characters[k])[0] - sp.Rational(1, 8)
                )
                == 0
                for k in CORNERS
                for j in range(8)
            ),
            detail=(
                "per_element: every matrix unit |n><n| has expectation 1/8 in every "
                "character, so each element has the same value for all eight labels"
            ),
        )
        self.check(
            "A17 N5 resolution class per_site",
            all(
                tuple(sp.simplify(sp.conjugate(e) * e) for e in characters[k])
                == (sp.Rational(1, 8),) * 8
                for k in CORNERS
            ),
            detail=(
                "per_site: every complete site profile is exactly (1/8,...,1/8), so the "
                "eight labels have identical site-resolved diagonal data"
            ),
        )
        modes = {
            k: sp.expand((characters[k].T * diagonal * characters[k])[0]) for k in CORNERS
        }
        self.check(
            "A18 N5 resolution class per_mode",
            len(set(modes.values())) == 1
            and all(sp.expand(modes[k] - uniform_value) == 0 for k in CORNERS),
            detail=(
                "per_mode: the arbitrary symbolic diagonal expectation is "
                "(1/8)sum_n w_n for each of all eight character modes"
            ),
        )
        block_resolution_ok = True
        for mask in range(1 << len(SITES)):
            indicator = tuple(
                sp.Integer(1) if mask & (1 << n) else sp.Integer(0)
                for n in range(len(SITES))
            )
            block_operator = sp.diag(*indicator)
            expected_block_value = sum(indicator) / 8
            if any(
                sp.expand(
                    (characters[k].T * block_operator * characters[k])[0]
                    - expected_block_value
                )
                != 0
                for k in CORNERS
            ):
                block_resolution_ok = False
                break
        self.check(
            "A19 N5 resolution class per_block",
            block_resolution_ok,
            detail=(
                "per_block: all 256 site-subset diagonal projectors have expectation "
                "|B|/8 in every character, exhausting the blocks of the supplied cell"
            ),
        )
        full_cell_operator = sum(site_operators, sp.zeros(8))
        self.check(
            "A20 N5 resolution class lattice_wide",
            full_cell_operator == sp.eye(8)
            and all(
                sp.expand(
                    (characters[k].T * full_cell_operator * characters[k])[0]
                    - 1
                )
                == 0
                for k in CORNERS
            ),
            detail=(
                "lattice_wide: summing all eight site projectors gives I_8 and expectation "
                "1 in every character on the entire supplied periodic cell; no larger-cell "
                "or infinite-lattice assertion is tested"
            ),
        )

        print(
            "  N3 hidden-wall scan: explicit scoped definitions are the finite cell, full "
            "character family, linear expectation, diagonal operator class, and supplied "
            "K_1; none is an unlisted wall, axiom, or physical bridge."
        )
        print(
            "  N4 residual matching: no prior residual witness is cited and no N1 route is "
            "marked RULED OUT BY PRIOR; witnesses=[]; unresolved=[]"
        )
        print(
            f"  N6 partial-closure handoff: the orchestrator must disposition every indexed "
            f"primitive, gate, convention, and scope reframe against {wall}. This runner "
            "establishes only the finite algebra, makes no new-axiom claim, and leaves the "
            "physical observable/readout bridge as a separate obligation."
        )
        print(
            "  N7 steelman route_translation_observable: if the physical observable algebra "
            "contains T_x,T_y,T_z, their joint signatures separate all labels. The note "
            "supplies the distinct resolution surface for the scoped N2 wall."
        )
        print(
            "  N8 cross-cycle echo: dynamic candidate comparison, universe count, digest, "
            "retirement state, and applicability are orchestrator-owned; this runner makes "
            "no static corpus-exhaustion claim."
        )


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
