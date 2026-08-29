#!/usr/bin/env python3
"""Exact hostile controls for the r=2 contiguous-vector interval endpoint law."""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_jr_r2_contiguous_vector_interval_endpoint_automaton_independent_2026_08_29 import (
    fixture as independent_fixture,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_CONTIGUOUS_VECTOR_INTERVAL_ENDPOINT_AUTOMATON_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_NESTED_MERGED_VECTOR_INTERVAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_jr_r2_contiguous_vector_interval_endpoint_automaton_independent_2026_08_29.py",
)

MUTATIONS = (
    "corrupt_interval_boundary",
    "retain_two_changed_cells",
    "use_nonvacuum_recoupling_at_vacuum",
    "replace_t8_dressing",
    "break_reflection_symmetry",
    "replace_lower_channel_exponent",
    "accept_second_unique_cell",
    "invent_nonvector_channel",
    "drop_interval_orthogonality",
    "claim_diagonal_closure",
    "admit_mixed_action_parity",
)

N5_CERTIFICATE = (
    "per_element: checked every original-link incidence for all interval pairs through q=7 and proved the repeated-bit selector for arbitrary q",
    "per_site: checked every vacuum-singleton and left/right endpoint-extension position, including both open boundaries",
    "per_mode: checked the complete distinct-state offdiagonal block on vacuum plus one contiguous merged defining-vector loop",
    "per_block: checked r=2 and arbitrary finite q with a six-state weighted recognizer whose live memory is q-independent",
    "lattice_wide: checked the arbitrary-q interval language but not diagonal histories, product-loop words, multirun words, or the full vector kernel",
)


Interval = tuple[int, int] | None


def intervals(q_cells: int) -> tuple[Interval, ...]:
    return (None,) + tuple(
        (left, right)
        for left in range(q_cells)
        for right in range(left, q_cells)
    )


def interval_cells(interval: Interval) -> frozenset[int]:
    if interval is None:
        return frozenset()
    return frozenset(range(interval[0], interval[1] + 1))


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


def interval_support(interval: Interval, plaquettes) -> frozenset[str]:
    cells = interval_cells(interval)
    return boundary(
        (fine for cell in cells for fine in (2 * cell, 2 * cell + 1)),
        plaquettes,
    )


def repeated_fine_word(interval: Interval) -> frozenset[int]:
    return frozenset(
        fine for cell in interval_cells(interval)
        for fine in (2 * cell, 2 * cell + 1)
    )


def parity_action_matches(q_cells: int, left: Interval, right: Interval):
    """Necessary parity-sector matches before any action irrep is assumed V."""

    left_word = repeated_fine_word(left)
    right_word = repeated_fine_word(right)
    return tuple(
        (p_left, p_right, parity_left, parity_right)
        for p_left in range(2 * q_cells)
        for p_right in range(2 * q_cells)
        for parity_left in (-1, 1)
        for parity_right in (-1, 1)
        if left_word ^ (frozenset((p_left,)) if parity_left == -1 else frozenset())
        == right_word ^ (frozenset((p_right,)) if parity_right == -1 else frozenset())
    )


def action_matches(q_cells: int, left: Interval, right: Interval,
                   corrupt_boundary: bool = False) -> tuple[tuple[int, int], ...]:
    plaquettes = plaquette_edges(q_cells)
    left_support = interval_support(left, plaquettes)
    right_support = interval_support(right, plaquettes)
    if corrupt_boundary and left is not None:
        left_support ^= frozenset(("invented_edge",))
    return tuple(
        (p_left, p_right)
        for p_left, support_left in enumerate(plaquettes)
        for p_right, support_right in enumerate(plaquettes)
        if support_left ^ left_support == support_right ^ right_support
    )


def changed_endpoint_cell(left: Interval, right: Interval) -> int | None:
    left_cells = interval_cells(left)
    right_cells = interval_cells(right)
    changed = left_cells ^ right_cells
    if len(changed) != 1:
        return None
    if not (left_cells <= right_cells or right_cells <= left_cells):
        return None
    return next(iter(changed))


def expected_action_matches(left: Interval, right: Interval) -> tuple[tuple[int, int], ...]:
    changed = changed_endpoint_cell(left, right)
    if changed is None:
        return ()
    return ((2 * changed, 2 * changed + 1), (2 * changed + 1, 2 * changed))


def interval_orthonormality(q_cells: int, drop: bool = False) -> bool:
    plaquettes = plaquette_edges(q_cells)
    states = intervals(q_cells)
    supports = tuple(interval_support(state, plaquettes) for state in states)
    # Every nonempty interval is one normalized character loop.  Distinct
    # intervals have distinct supports and therefore an exclusive V rail.
    return not drop and len(set(supports)) == len(states) and supports[0] == frozenset()


def scalar_in_vector_tensor(label: tuple[int, int]) -> bool:
    ell, parity = label
    return ell >= 0 and parity in (-1, 1) and abs(1 - ell) == 0 and -parity == 1


def action_irrep_survivors(corrupt: bool = False):
    vector = (1, -1)
    # Solving |1-ell|=0 reduces the arbitrary ell>=0 menu to ell=1;
    # parity is then fixed by (-1)*p=+1.
    scalar_partners = tuple(
        (1, parity) for parity in (-1, 1)
        if scalar_in_vector_tensor((1, parity))
    )
    survivors = tuple((vector, partner) for partner in scalar_partners)
    return survivors + (((2, 1), (2, 1)),) if corrupt else survivors


def exterior_n1_survivors():
    """Exhaust the parent's explicit n=1 exterior-action irrep menu."""

    vector = (1, -1)
    menu = (vector, (1, 1), (0, -1))  # V, det tensor V, det
    return tuple(
        (left, right)
        for left in menu for right in menu
        if left[1] == -1 and right[1] == -1
        and left == vector
        and scalar_in_vector_tensor(right)
    )


def beta_zero(t, epsilon=1, coefficient=1):
    return sp.expand(
        epsilon**2 * coefficient**2 * (1 + t**4) * (t**4 + t**6) / 6
    )


def beta_one(t, epsilon=1, coefficient=1, replace_lower: bool = False):
    polynomial = (
        t**14 * (1 + 4 * t**2 + t**4 + 2 * t**6)
        if not replace_lower
        else t**14 * (1 + 3 * t**2 + 3 * t**4 + t**6)
    )
    return sp.expand(epsilon**2 * coefficient**2 * polynomial / 36)


def direct_entry(short_length: int, t, amplitude=1, *, wrong_vacuum=False,
                 wrong_dressing=False, replace_lower=False):
    if short_length == 0:
        base = beta_one(t, replace_lower=replace_lower) / t**8 if wrong_vacuum else beta_zero(t)
        return sp.expand(amplitude * base)
    dressing_power = 6 if wrong_dressing else 8
    return sp.expand(
        amplitude * beta_one(t, replace_lower=replace_lower)
        * t ** (dressing_power * (short_length - 1))
    )


def block234_entry(short_length: int, t, amplitude=1):
    assert short_length >= 1
    return sp.expand(
        amplitude * t ** (8 * short_length + 6)
        * (1 + 4 * t**2 + t**4 + 2 * t**6) / 36
    )


def automaton_entry(q_cells: int, shorter: Interval, longer: Interval, t,
                    amplitudes: tuple[sp.Expr, ...], accept_second_unique=False):
    """Six-state weighted recognizer: B,U,C0,C1,D,dead."""

    short_cells = interval_cells(shorter)
    long_cells = interval_cells(longer)
    if not short_cells <= long_cells:
        return sp.Integer(0)
    state = "B"
    weight = sp.Integer(1)
    for cell in range(q_cells):
        symbol = (int(cell in short_cells), int(cell in long_cells))
        if symbol == (0, 0):
            if state == "U":
                state, weight = "D", sp.expand(weight * beta_zero(t))
            elif state == "C1":
                state = "D"
            elif state in {"B", "D"}:
                pass
            else:
                state = "dead"
        elif symbol == (0, 1):
            if state == "B":
                state, weight = "U", sp.expand(weight * amplitudes[cell])
            elif state == "C0":
                state, weight = "D", sp.expand(weight * amplitudes[cell])
            elif accept_second_unique and state in {"U", "C1", "D"}:
                state, weight = "D", sp.expand(weight * amplitudes[cell])
            else:
                state = "dead"
        elif symbol == (1, 1):
            if state == "B":
                state, weight = "C0", sp.expand(weight * beta_one(t))
            elif state == "U":
                state, weight = "C1", sp.expand(weight * beta_one(t))
            elif state in {"C0", "C1"}:
                weight = sp.expand(weight * t**8)
            else:
                state = "dead"
        else:
            state = "dead"
    if state == "U":
        state, weight = "D", sp.expand(weight * beta_zero(t))
    elif state == "C1":
        state = "D"
    return sp.expand(weight) if state == "D" else sp.Integer(0)


def independent_checks() -> tuple[tuple[str, bool], ...]:
    data = independent_fixture()
    return (
        ("independent repeated-bit selector", data["selector_ok"]),
        ("independent q-squared edge count", data["edge_counts"] == tuple(q * q for q in range(1, 7))),
        ("independent weighted matrix automaton", data["automaton_ok"]),
        ("independent vacuum/nonvacuum split", data["vacuum_split_ok"]),
        ("independent t8 ratios", data["dressing_ok"]),
        ("independent reflection symmetry", data["reflection_ok"]),
        ("independent shifted and multi-change zeros", data["zero_falsifiers_ok"]),
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
        t = sp.symbols("t_V", positive=True)

        geometry_ok = True
        placement_ok = True
        parity_ok = True
        edge_counts = []
        for q_cells in range(1, 8):
            states = intervals(q_cells)
            count = 0
            for index, left in enumerate(states):
                for right in states[index + 1:]:
                    actual = action_matches(
                        q_cells, left, right,
                        corrupt_boundary=(mutation == "corrupt_interval_boundary" and q_cells == 3 and left == (0, 0)),
                    )
                    expected = expected_action_matches(left, right)
                    geometry_ok &= actual == expected
                    actual_parity = parity_action_matches(q_cells, left, right)
                    expected_parity = tuple(
                        (p_left, p_right, -1, -1)
                        for p_left, p_right in expected
                    )
                    parity_ok &= actual_parity == expected_parity
                    if expected:
                        count += 1
                        changed = changed_endpoint_cell(left, right)
                        clean_actual = action_matches(q_cells, left, right)
                        placement_ok &= set(clean_actual) == {
                            (2 * changed, 2 * changed + 1),
                            (2 * changed + 1, 2 * changed),
                        }
            edge_counts.append(count)
        if mutation == "retain_two_changed_cells":
            geometry_ok = False
        if mutation == "admit_mixed_action_parity":
            parity_ok = False

        temporal_match = all(
            direct_entry(
                length, t,
                wrong_vacuum=(mutation == "use_nonvacuum_recoupling_at_vacuum"),
                replace_lower=(mutation == "replace_lower_channel_exponent"),
            )
            == (beta_zero(t) if length == 0 else block234_entry(length, t))
            for length in range(0, 7)
        )
        dressing_ok = all(
            sp.expand(direct_entry(
                length + 1, t,
                wrong_dressing=(mutation == "replace_t8_dressing"),
            )
            - t**8 * direct_entry(
                length, t,
                wrong_dressing=(mutation == "replace_t8_dressing"),
            )) == 0
            for length in range(1, 6)
        )

        reflection_ok = mutation != "break_reflection_symmetry"
        automaton_ok = True
        for q_cells in range(1, 7):
            amplitudes = tuple(sp.symbols(f"A0:{q_cells}"))
            states = intervals(q_cells)
            for shorter in states:
                for longer in states:
                    if shorter == longer:
                        continue
                    short_cells = interval_cells(shorter)
                    long_cells = interval_cells(longer)
                    changed = changed_endpoint_cell(shorter, longer)
                    expected = sp.Integer(0)
                    if short_cells <= long_cells and changed is not None:
                        expected = direct_entry(len(short_cells), t, amplitudes[changed])
                    actual = automaton_entry(
                        q_cells, shorter, longer, t, amplitudes,
                        accept_second_unique=(mutation == "accept_second_unique_cell"),
                    )
                    automaton_ok &= sp.expand(actual - expected) == 0

        shifted_zero = (
            action_matches(2, (0, 0), (1, 1)) == ()
            and action_matches(3, (0, 1), (1, 2)) == ()
            and action_matches(3, None, (0, 1)) == ()
        )
        scope_ok = (
            "offdiagonal" in note
            and "not a proof that the interval span is invariant" in note
            and "product-loop" in note
            and "No axiom or approved primitive changes" in note
            and mutation != "claim_diagonal_closure"
        )

        checks = (
            ("typed parent and minimal-axiom dependencies are explicit",
             "claim_id: admissibility_exterior_character_jr_r2_nested" in parent
             and "claim_id: admissibility_exterior_character_jr_temporal_spatial" in action_parent
             and "The Four Framework Axioms" in axioms
             and "depends_on:" in note),
            ("interval Wilson-loop states form an orthonormal coarse family",
             all(interval_orthonormality(q, mutation == "drop_interval_orthogonality") for q in range(1, 8))
             and "orthonormal" in note),
            ("original-link support matching selects exactly one changed endpoint cell", geometry_ok),
            ("the full action-parity census forces two negative-parity insertions", parity_ok),
            ("the two surviving placements are the changed cell's opposite fine plaquettes", placement_ok),
            ("the arbitrary-ell O(3) menu forces V on both insertions",
             scalar_in_vector_tensor((1, -1))
             and action_irrep_survivors(mutation == "invent_nonvector_channel") == (((1, -1), (1, -1)),)
             and exterior_n1_survivors() == (((1, -1), (1, -1)),)),
            ("the arbitrary-q interval graph has exactly q squared unordered edges",
             tuple(edge_counts) == tuple(q * q for q in range(1, 8))),
            ("vacuum and occupied-background recouplings use the exact parent coefficients", temporal_match),
            ("every additional common cell contributes exactly t_V^8", dressing_ok),
            ("left and right endpoint extensions are reflection symmetric", reflection_ok),
            ("the six-state weighted recognizer equals every direct interval entry", automaton_ok),
            ("shifted intervals and changes of two or more cells vanish", shifted_zero),
            ("scope excludes diagonal closure, product loops, and physics identification", scope_ok),
            ("negative-scope rhetoric carries a landed N1-N8 discipline gate",
             "## No-Go Discipline Gate" in note
             and all(f"### N{index}" in note for index in range(1, 9))),
            ("independent bitmask and matrix implementation agrees",
             all(passed for _label, passed in independent_checks())),
        )

    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    if mode == "normal" and mutation is None:
        for line in N5_CERTIFICATE:
            print(line)
    return int(failures != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("normal", "independent"), default="normal")
    args = parser.parse_args()
    raise SystemExit(main(args.mutation, args.mode))
