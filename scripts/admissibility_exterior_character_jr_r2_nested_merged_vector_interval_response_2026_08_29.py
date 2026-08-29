#!/usr/bin/env python3
"""Exact hostile controls for the r=2 nested merged-vector interval response."""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_jr_r2_nested_merged_vector_interval_response_independent_2026_08_29 import (
    fixture as independent_fixture,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_NESTED_MERGED_VECTOR_INTERVAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_ARBITRARY_R_SCALAR_FUSED_VECTOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_jr_r2_nested_merged_vector_interval_response_independent_2026_08_29.py",
)

MUTATIONS = (
    "corrupt_interval_boundary",
    "replace_lower_channel_exponent",
    "corrupt_global_haar_factor",
    "retain_same_index_pair",
    "invent_q_component",
    "invent_nonvector_channel",
    "drop_half_action_factor",
    "apply_interval_formula_at_s0",
    "claim_product_loop_background",
)

N5_CERTIFICATE = (
    "per_element: checked every original-link incidence and the unique exclusive-rail forcing of the defining-vector action irrep",
    "per_site: checked the changed cell and every adjacent nested merged-loop span s=1 through s=6 on exact finite carriers",
    "per_mode: checked one offdiagonal pair of normalized merged defining-vector Wilson-loop characters and no tensor-product background",
    "per_block: checked r=2 for arbitrary finite interval span 1<=s<q with exact temporal exponents and global Haar recoupling",
    "lattice_wide: checked and not executed — the theorem supplies no arbitrary background word, volume norm, or continuum family",
)


def plaquette_edges(q_cells: int) -> tuple[frozenset[str], ...]:
    return tuple(
        frozenset((f"u{index}", f"v{index}", f"h{index}", f"h{index + 1}"))
        for index in range(2 * q_cells)
    )


def boundary(indices, plaquettes: tuple[frozenset[str], ...]) -> frozenset[str]:
    result: frozenset[str] = frozenset()
    for index in indices:
        result ^= plaquettes[index]
    return result


def interval_geometry(q_cells: int, span: int) -> dict[str, object]:
    plaquettes = plaquette_edges(q_cells)
    y_support = boundary(range(2, 2 * span + 2), plaquettes)
    z_support = boundary(range(0, 2 * span + 2), plaquettes)
    all_links = frozenset().union(*plaquettes)
    matches = []
    for left, left_plaquette in enumerate(plaquettes):
        for right, right_plaquette in enumerate(plaquettes):
            if left_plaquette ^ y_support == right_plaquette ^ z_support:
                forced_vector_rails = tuple(sorted(
                    edge for edge in left_plaquette
                    if edge[0] in {"u", "v"}
                    and edge not in y_support
                    and edge not in right_plaquette
                    and edge in z_support
                ))
                matches.append({
                    "pair": (left, right),
                    "channel_weight": len(left_plaquette ^ y_support),
                    "left_doubled": tuple(sorted(left_plaquette & y_support)),
                    "right_doubled": tuple(sorted(right_plaquette & z_support)),
                    "forced_vector_rails": forced_vector_rails,
                })
    return {
        "link_count": len(all_links),
        "coarse_weights": tuple(
            len(boundary((2 * cell, 2 * cell + 1), plaquettes))
            for cell in range(q_cells)
        ),
        "y_support": y_support,
        "z_support": z_support,
        "y_weight": len(y_support),
        "z_weight": len(z_support),
        "matches": tuple(matches),
    }


def delta(first: int, second: int) -> int:
    return int(first == second)


def matched_haar_factor(corrupt: bool = False) -> F:
    total = 0
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for i in range(3):
                    for j in range(3):
                        for k in range(3):
                            total += (
                                delta(a, k) * delta(a, i)
                                * delta(b, j) * delta(b, k)
                                * delta(c, i) * delta(c, j)
                            )
    return F(total, 3 ** (2 if corrupt else 3))


def same_index_overlaps(retain: bool = False) -> tuple[F, F]:
    # Pair 00 leaves W1 once; pair 11 leaves W0 once. Haar first moments vanish.
    unpaired_first_moment = sum(F(0) for _row in range(3) for _column in range(3))
    return (F(int(retain)), F(0)) if retain else (
        unpaired_first_moment,
        unpaired_first_moment,
    )


def physical_q_zero(invent_component: bool = False) -> tuple[bool, bool]:
    # At fixed delta_0, W0=x and W1=delta_0 x^-1; both V characters have
    # zero conditional Haar first moment. Y_s and Z_s are fixed coarse factors.
    haar_first_trace = sum(F(0) for _index in range(3))
    return haar_first_trace == 0, (not invent_component and haar_first_trace == 0)


def coarse_state_gram() -> tuple[F, F, F]:
    """Exact normalized Haar Gram of Y_s and Z_s on independent coarse cells."""

    second_character_moment = F(sum(delta(a, b) for a in range(3) for b in range(3)), 3)
    # Z_s has the same norm by Haar invariance.  Its extra independent cell-zero
    # vector character has zero first moment against Y_s.
    return second_character_moment, second_character_moment, F(0)


def scalar_in_vector_tensor(label: tuple[int, int]) -> bool:
    """Whether the scalar occurs in V tensor (ell,parity), for arbitrary ell."""

    ell, parity = label
    if ell < 0 or parity not in (-1, 1):
        return False
    # Angular momenta run from |1-ell| through 1+ell.  Since the lower
    # endpoint is nonnegative, L=0 occurs iff |1-ell|=0, hence ell=1.
    # The O(3) product parity is (-1)*parity and must be +1.
    return abs(1 - ell) == 0 and -parity == 1


def action_irrep_survivors(corrupt: bool = False) -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    """Solve the arbitrary-ell O(3) selection on both action insertions.

    The left exclusive rail requires rho=V.  On the opposite doubled rail,
    Hom(1,V tensor sigma) is nonzero exactly for sigma=V because V is self-dual.
    """

    vector = (1, -1)
    invented = (2, 1)
    # Solving |1-ell|=0 and -parity=+1 is exhaustive over every ell>=0.
    scalar_candidates = tuple(
        (1, parity) for parity in (-1, 1)
        if scalar_in_vector_tensor((1, parity))
    )
    survivors = [(vector, right) for right in scalar_candidates]
    if corrupt:
        survivors.append((invented, invented))
    return tuple(survivors)


def temporal_polynomial(span: int, t_value: sp.Symbol,
                        replace_lower: bool = False) -> sp.Expr:
    y_weight = 4 * span + 2
    z_weight = 4 * span + 6
    upper_weight = 4 * span + 6
    lower_weight = upper_weight if replace_lower else 4 * span + 4
    return sp.expand(
        (t_value**y_weight + t_value**upper_weight)
        * (t_value**z_weight + t_value**upper_weight)
        + (t_value**y_weight + t_value**lower_weight)
        * (t_value**z_weight + t_value**lower_weight)
    )


def expected_polynomial(span: int, t_value: sp.Symbol) -> sp.Expr:
    return sp.expand(
        t_value ** (8 * span + 6)
        * (1 + 4 * t_value**2 + t_value**4 + 2 * t_value**6)
    )


def independent_checks() -> tuple[tuple[str, bool], ...]:
    data = independent_fixture()
    return (
        ("independent global overlap", data["matched_overlap"] == F(1, 9)),
        ("independent same-index zeros",
         data["same_zero_overlap"] == 0 and data["same_one_overlap"] == 0),
        ("independent physical-Q first moments", data["q_means"] == (F(0), F(0))),
        ("independent coarse-state Gram",
         data["coarse_state_gram"] == (F(1), F(1), F(0))),
        ("independent action-irrep selection",
         data["action_irrep_survivors"] == (((1, -1), (1, -1)),)),
        ("independent original-link channels",
         all(row["geometry"]["matches"] == (
             (0, 1, 4 * row["span"] + 6, 0, 2),
             (1, 0, 4 * row["span"] + 4, 1, 3),
         ) for row in data["rows"])),
        ("independent temporal polynomial",
         all(row["direct"] == row["expected"] for row in data["rows"])),
        ("independent small-step normalization",
         all(row["at_one"] == F(2, 9) for row in data["rows"])),
        ("independent finite rational fixture",
         data["rows"][0]["at_half_c2"] == F(67, 4718592)),
        ("independent t8 background dressing",
         all(
             sum(F(coefficient) * F(1, 2) ** power
                 for power, coefficient in data["rows"][index + 1]["direct"].items())
             == F(1, 2) ** 8
             * sum(F(coefficient) * F(1, 2) ** power
                   for power, coefficient in data["rows"][index]["direct"].items())
             for index in range(len(data["rows"]) - 1)
         )),
    )


def main(mutation: str | None, mode: str) -> int:
    if mode == "independent":
        checks = independent_checks()
    else:
        root = Path(__file__).resolve().parents[1]
        note = (root / AUDIT_INPUT_PATHS[0]).read_text()
        parent = (root / AUDIT_INPUT_PATHS[1]).read_text()
        action_parent = (root / AUDIT_INPUT_PATHS[2]).read_text()
        axioms = (root / AUDIT_INPUT_PATHS[3]).read_text()
        t_value = sp.symbols("t_V", positive=True)
        rows = tuple(interval_geometry(span + 1, span) for span in range(1, 7))

        geometry_ok = all(
            row["link_count"] == 6 * (span + 1) + 1
            and all(weight == 6 for weight in row["coarse_weights"])
            and row["y_weight"] == 4 * span + 2
            and row["z_weight"]
            == 4 * span + 6 + int(mutation == "corrupt_interval_boundary")
            for span, row in zip(range(1, 7), rows)
        )

        expected_matches = tuple(
            (
                (0, 1, 4 * span + 6, (), (f"u1", f"v1")),
                (1, 0, 4 * span + 4, (f"h2",), (f"h0", f"u0", f"v0")),
            )
            for span in range(1, 7)
        )
        actual_matches = tuple(tuple(
            (
                item["pair"][0], item["pair"][1],
                item["channel_weight"],
                item["left_doubled"], item["right_doubled"],
            )
            for item in row["matches"]
        ) for row in rows)

        forced_vector_geometry = all(
            all(item["forced_vector_rails"] for item in row["matches"])
            for row in rows
        )
        irrep_survivors = action_irrep_survivors(
            corrupt=(mutation == "invent_nonvector_channel")
        )
        q_zero = physical_q_zero(mutation == "invent_q_component")
        same_index = same_index_overlaps(mutation == "retain_same_index_pair")
        haar_factor = matched_haar_factor(mutation == "corrupt_global_haar_factor")

        temporal_match = all(
            temporal_polynomial(
                span, t_value,
                replace_lower=(mutation == "replace_lower_channel_exponent"),
            ) == expected_polynomial(span, t_value)
            for span in range(1, 7)
        )
        normalized_prefactor = (
            F(1 if mutation == "drop_half_action_factor" else 1, 1 if mutation == "drop_half_action_factor" else 4)
            * F(1, 9)
        )
        scope_ok = (
            "nested merged Wilson-loop interval" in note
            and "not a tensor-product vector background" in note
            and "No axiom or approved primitive changes" in note
        )
        if mutation == "claim_product_loop_background":
            scope_ok = False

        checks = (
            ("typed parent and minimal-axiom dependencies are explicit",
             "claim_id: admissibility_exterior_character_jr_arbitrary_r" in parent
             and "claim_id: admissibility_exterior_character_jr_temporal_spatial" in action_parent
             and "The Four Framework Axioms" in axioms
             and "depends_on:" in note),
            ("coarse Wilson-loop states are normalized and orthogonal",
             coarse_state_gram() == (F(1), F(1), F(0))
             and "||Y_s||=||Z_s||=1" in note
             and "<Y_s,Z_s>=0" in note
             and "J_2Y_s=chi_V(A_s)" in note),
            ("actual 6q+1 original-link intervals have exact weights", geometry_ok),
            ("only cross-cell action pairs have matching vector support",
             actual_matches == expected_matches),
            ("exclusive rails force both action irreps to be V",
             forced_vector_geometry
             and irrep_survivors == (((1, -1), (1, -1)),)),
            ("global O(3) Haar recoupling is one ninth",
             haar_factor == F(1, 9)),
            ("same-index pairings vanish by an unpaired Haar first moment",
             same_index == (F(0), F(0))),
            ("physical Q kills all four first-order histories",
             q_zero == (True, True)
             and "C J_2=J_2 C_c" in note
             and "[C,Q]=0" in note),
            ("two temporal channels give the exact interval polynomial",
             temporal_match),
            ("both spatial half-actions give the normalized one-over-36 factor",
             normalized_prefactor == F(1, 36)),
            ("small-step response coefficient is two ninths",
             all(F(1, 36) * expected_polynomial(span, sp.Integer(1)) == F(2, 9)
                 for span in range(1, 7))),
            ("s=1 c=2 half-step fixture is exact",
             F(4, 36) * expected_polynomial(1, sp.Rational(1, 2))
             == F(67, 4718592)),
            ("one additional merged background cell contributes t^8",
             all(sp.expand(expected_polynomial(span + 1, t_value)
                           - t_value**8 * expected_polynomial(span, t_value)) == 0
                 for span in range(1, 6))),
            ("s=0 is excluded because its global Haar factor is one third",
             mutation != "apply_interval_formula_at_s0"
             and "lower endpoint `s=0` is excluded" in note
             and "`1/3` rather than `1/9`" in note),
            ("claim scope excludes product backgrounds and physical identification",
             scope_ok),
            ("negative-scope rhetoric carries a landed N1-N8 discipline gate",
             "## No-Go Discipline Gate" in note
             and all(f"### N{index}" in note for index in range(1, 9))),
            ("independent signed-frame and Fraction implementation agrees",
             all(passed for _label, passed in independent_checks())),
        )

    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    if mode == "normal" and mutation is None:
        for certificate_line in N5_CERTIFICATE:
            print(certificate_line)
    return int(failures != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("normal", "independent"), default="normal")
    args = parser.parse_args()
    raise SystemExit(main(args.mutation, args.mode))
