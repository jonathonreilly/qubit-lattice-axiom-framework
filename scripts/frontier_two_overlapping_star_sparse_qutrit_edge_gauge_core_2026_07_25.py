#!/usr/bin/env python3
"""Finite helpers for the two-overlapping-star sparse qutrit edge gauge.

The three lawful states are stored on two M2 sites as

    absent      = 00,
    incident-0  = 10,
    incident-1  = 01.

The fourth word 11 is outside the declared feature code.  The two bits are
the factor contribution to the shared outer-square X word and the factor's
own endpoint-tag auxiliary X word.  This module contains only exact finite
geometry, projectors, and the reversible sign circuit; the physical branch
census lives in the companion runner.
"""

from __future__ import annotations

from itertools import permutations, product

import numpy as np


Coord = tuple[int, int, int]
Frame = tuple[Coord, Coord, Coord]

LAWFUL_QUTRIT_WORDS = (0b00, 0b10, 0b01)
DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def negate(row: Coord) -> Coord:
    return tuple(-value for value in row)  # type: ignore[return-value]


def det3(frame: Frame) -> int:
    a, b, c = frame
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def matvec(frame: Frame, vector: Coord) -> Coord:
    return tuple(
        sum(frame[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def matmul(left: Frame, right: Frame) -> Frame:
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(3))
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def proper_cubic_frames() -> tuple[Frame, ...]:
    frames = set()
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            frame = tuple(
                tuple(signs[row] if column == order[row] else 0 for column in range(3))
                for row in range(3)
            )
            if det3(frame) == 1:
                frames.add(frame)
    return tuple(sorted(frames))


FRAMES = proper_cubic_frames()
FRAME_INDEX = {frame: index for index, frame in enumerate(FRAMES)}


def qutrit_bits(word: int) -> tuple[int, int]:
    if word not in LAWFUL_QUTRIT_WORDS:
        raise ValueError("the endpoint feature word must be one of 00, 10, 01")
    return (word >> 1) & 1, word & 1


def qutrit_word(outer_contribution: int, endpoint_tag: int) -> int:
    if outer_contribution not in (0, 1) or endpoint_tag not in (0, 1):
        raise ValueError("feature bits must be binary")
    word = (outer_contribution << 1) | endpoint_tag
    qutrit_bits(word)
    return word


def incidence_and_tag(word: int) -> tuple[int, int]:
    outer, tag = qutrit_bits(word)
    return outer | tag, tag


def branch_sign_bit(left_word: int, right_word: int) -> int:
    left_incidence, left_tag = incidence_and_tag(left_word)
    right_incidence, right_tag = incidence_and_tag(right_word)
    return left_incidence & right_incidence & (left_tag ^ right_tag)


def valid_qutrit_projector() -> np.ndarray:
    projector = np.zeros((4, 4), dtype=float)
    for word in LAWFUL_QUTRIT_WORDS:
        projector[word, word] = 1.0
    return projector


def equality_projector() -> np.ndarray:
    """Rank-three projector on two lawful two-M2 qutrit blocks."""
    projector = np.zeros((16, 16), dtype=float)
    for word in LAWFUL_QUTRIT_WORDS:
        basis = (word << 2) | word
        projector[basis, basis] = 1.0
    return projector


def four_copy_projectors() -> dict[str, object]:
    """Projector census for A-left,A-right,B-left,B-right copy blocks.

    The B-star view reverses the endpoint roles on the common edge.  Equality
    therefore ties A-left to B-right and A-right to B-left.  All matrices are
    materialized on the exact eight-M2 copy Hilbert space.
    """
    dimension = 1 << 8
    valid = np.zeros((dimension, dimension), dtype=float)
    left_equal = np.zeros_like(valid)
    right_equal = np.zeros_like(valid)
    valid_equal = np.zeros_like(valid)
    for basis in range(dimension):
        words = tuple((basis >> (2 * block)) & 0b11 for block in range(4))
        all_valid = all(word in LAWFUL_QUTRIT_WORDS for word in words)
        left_ok = words[0] == words[3] and words[0] in LAWFUL_QUTRIT_WORDS
        right_ok = words[1] == words[2] and words[1] in LAWFUL_QUTRIT_WORDS
        valid[basis, basis] = float(all_valid)
        left_equal[basis, basis] = float(left_ok)
        right_equal[basis, basis] = float(right_ok)
        valid_equal[basis, basis] = float(all_valid and left_ok and right_ok)
    left_with_valid = valid @ left_equal
    right_with_valid = valid @ right_equal
    return {
        "ambient_dimension": dimension,
        "valid_rank": int(np.linalg.matrix_rank(valid)),
        "left_equality_rank_with_validity": int(np.linalg.matrix_rank(left_with_valid)),
        "right_equality_rank_with_validity": int(np.linalg.matrix_rank(right_with_valid)),
        "joint_equality_rank": int(np.linalg.matrix_rank(valid_equal)),
        "delete_one_equality_rank": int(np.linalg.matrix_rank(left_with_valid)),
        "valid_left_commutator": float(np.linalg.norm(valid @ left_equal - left_equal @ valid)),
        "valid_right_commutator": float(np.linalg.norm(valid @ right_equal - right_equal @ valid)),
        "equality_commutator": float(
            np.linalg.norm(left_with_valid @ right_with_valid - right_with_valid @ left_with_valid)
        ),
        "joint_idempotence_residual": float(
            np.linalg.norm(valid_equal @ valid_equal - valid_equal)
        ),
    }


def cnot(basis: int, control: int, target: int) -> int:
    if (basis >> control) & 1:
        basis ^= 1 << target
    return basis


def sign_circuit(
    basis: int,
    left_start: int,
    right_start: int,
    scratch: int,
) -> tuple[int, int]:
    """Apply the exact local phase circuit and return ``(basis, phase)``.

    Within a qutrit block, ``start`` is the tag bit and ``start+1`` is the
    outer-contribution bit.  The circuit computes the tag XOR into one scratch
    M2, converts each lawful pair in-place from (outer,tag) to an incidence
    control, applies one three-controlled phase, then uncomputes everything.
    """
    left_tag, left_outer = left_start, left_start + 1
    right_tag, right_outer = right_start, right_start + 1
    source = basis
    basis = cnot(basis, left_tag, scratch)
    basis = cnot(basis, right_tag, scratch)
    basis = cnot(basis, left_outer, left_tag)
    basis = cnot(basis, right_outer, right_tag)
    phase = -1 if all((basis >> bit) & 1 for bit in (left_tag, right_tag, scratch)) else 1
    basis = cnot(basis, right_outer, right_tag)
    basis = cnot(basis, left_outer, left_tag)
    basis = cnot(basis, right_tag, scratch)
    basis = cnot(basis, left_tag, scratch)
    if basis != source:
        raise AssertionError("the sign circuit did not return its data and scratch")
    return basis, phase


def sign_circuit_census() -> dict[str, int]:
    failures = scratch_failures = cases = 0
    left_start, right_start, scratch = 0, 2, 4
    for left_word, right_word in product(LAWFUL_QUTRIT_WORDS, repeat=2):
        basis = left_word | (right_word << 2)
        target, phase = sign_circuit(basis, left_start, right_start, scratch)
        failures += phase != (-1 if branch_sign_bit(left_word, right_word) else 1)
        scratch_failures += bool((target >> scratch) & 1)
        cases += 1
    return {
        "lawful_truth_table_cases": cases,
        "phase_failures": failures,
        "returned_scratch_failures": scratch_failures,
    }


def edge_key(left: Coord, right: Coord) -> tuple[Coord, Coord]:
    return tuple(sorted((left, right)))  # type: ignore[return-value]


def patch_geometry(bond: Coord = (1, 0, 0)) -> dict[str, object]:
    if bond not in DIRECTIONS:
        raise ValueError("the center bond must be one oriented cubic unit vector")
    centers = ((0, 0, 0), bond)
    incidences = tuple(
        (star, direction, centers[star], add(centers[star], direction))
        for star in range(2)
        for direction in DIRECTIONS
    )
    edges = {edge_key(left, right) for _star, _direction, left, right in incidences}
    shared = edge_key(*centers)
    shared_rows = tuple(
        (star, direction)
        for star, direction, left, right in incidences
        if edge_key(left, right) == shared
    )
    return {
        "bond": bond,
        "centers": centers,
        "incidences": incidences,
        "edges": edges,
        "shared_edge": shared,
        "shared_rows": shared_rows,
        "cells": {cell for edge in edges for cell in edge},
    }


def covariance_census() -> dict[str, int]:
    frame_failures = product_failures = shared_failures = sign_failures = 0
    transport_cases = 0
    for frame in FRAMES:
        source = patch_geometry()
        target = patch_geometry(matvec(frame, source["bond"]))  # type: ignore[arg-type]
        mapped_edges = {
            edge_key(matvec(frame, edge[0]), matvec(frame, edge[1]))
            for edge in source["edges"]  # type: ignore[union-attr]
        }
        frame_failures += mapped_edges != target["edges"]
        mapped_shared = edge_key(
            matvec(frame, source["shared_edge"][0]),  # type: ignore[index]
            matvec(frame, source["shared_edge"][1]),  # type: ignore[index]
        )
        shared_failures += mapped_shared != target["shared_edge"]
        for left_word, right_word in product(LAWFUL_QUTRIT_WORDS, repeat=2):
            sign_failures += branch_sign_bit(left_word, right_word) != branch_sign_bit(
                right_word, left_word
            )
            transport_cases += 1
    for left in FRAMES:
        for right in FRAMES:
            product_failures += matmul(left, right) not in FRAME_INDEX
            for direction in DIRECTIONS:
                product_failures += matvec(left, matvec(right, direction)) != matvec(
                    matmul(left, right), direction
                )
    return {
        "proper_cubic_frames": len(FRAMES),
        "ordered_frame_products": len(FRAMES) ** 2,
        "frame_geometry_failures": frame_failures,
        "frame_product_failures": product_failures,
        "shared_edge_transport_failures": shared_failures,
        "feature_sign_covariance_cases": transport_cases,
        "feature_sign_covariance_failures": sign_failures,
    }
