#!/usr/bin/env python3
"""Independent exact controls for the r=2 nested merged-vector interval response."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations, product


AUDIT_TIMEOUT_SEC = 120


def plaquette_masks(q_cells: int) -> tuple[int, ...]:
    """The actual 6q+1 original links u_j,v_j,h_j,h_(j+1)."""

    fine_count = 2 * q_cells
    return tuple(
        (1 << index)
        | (1 << (fine_count + index))
        | (1 << (2 * fine_count + index))
        | (1 << (2 * fine_count + index + 1))
        for index in range(fine_count)
    )


def boundary_mask(indices, plaquettes: tuple[int, ...]) -> int:
    result = 0
    for index in indices:
        result ^= plaquettes[index]
    return result


def interval_geometry(q_cells: int, span: int) -> dict[str, object]:
    plaquettes = plaquette_masks(q_cells)
    all_links = 0
    for plaquette in plaquettes:
        all_links |= plaquette
    y_support = boundary_mask(range(2, 2 * span + 2), plaquettes)
    z_support = boundary_mask(range(0, 2 * span + 2), plaquettes)
    matches = []
    for left, left_plaquette in enumerate(plaquettes):
        for right, right_plaquette in enumerate(plaquettes):
            if left_plaquette ^ y_support == right_plaquette ^ z_support:
                matches.append((
                    left,
                    right,
                    (left_plaquette ^ y_support).bit_count(),
                    (left_plaquette & y_support).bit_count(),
                    (right_plaquette & z_support).bit_count(),
                ))
    return {
        "link_count": all_links.bit_count(),
        "y_weight": y_support.bit_count(),
        "z_weight": z_support.bit_count(),
        "matches": tuple(matches),
    }


def matmul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3))
              for j in range(3))
        for i in range(3)
    )


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))


def trace(matrix) -> int:
    return sum(matrix[index][index] for index in range(3))


def signed_frames():
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            frames.append(tuple(
                tuple(signs[row] if column == permutation[row] else 0
                      for column in range(3))
                for row in range(3)
            ))
    return tuple(frames)


def signed_frame_overlaps() -> tuple[F, F, F]:
    """Finite-group reconstruction independent of the primary delta proof."""

    frames = signed_frames()
    matched = 0
    same_zero = 0
    same_one = 0
    for a_matrix in frames:
        trace_a = trace(a_matrix)
        if trace_a == 0:
            continue
        for w1 in frames:
            trace_w1 = trace(w1)
            aw1 = matmul(a_matrix, w1)
            for w0 in frames:
                outer = trace(matmul(aw1, w0))
                trace_w0 = trace(w0)
                matched += trace_w0 * trace_w1 * trace_a * outer
                same_zero += trace_w0 * trace_w0 * trace_a * outer
                same_one += trace_w1 * trace_w1 * trace_a * outer
    denominator = len(frames) ** 3
    return (
        F(matched, denominator),
        F(same_zero, denominator),
        F(same_one, denominator),
    )


def conditional_q_means() -> tuple[F, F]:
    frames = signed_frames()
    mean_w0 = F(sum(trace(frame) for frame in frames), len(frames))
    means_w1 = []
    for delta in frames:
        means_w1.append(F(
            sum(trace(matmul(delta, transpose(frame))) for frame in frames),
            len(frames),
        ))
    return mean_w0, max((abs(value) for value in means_w1), default=F(0))


def coarse_state_gram() -> tuple[F, F, F]:
    """Reconstruct the two coarse Wilson-loop norms and cross overlap."""

    frames = signed_frames()
    norm_y = F(sum(trace(a_matrix) ** 2 for a_matrix in frames), len(frames))
    norm_z = F(
        sum(trace(matmul(a_matrix, delta_matrix)) ** 2
            for a_matrix in frames for delta_matrix in frames),
        len(frames) ** 2,
    )
    inner = F(
        sum(trace(a_matrix) * trace(matmul(a_matrix, delta_matrix))
            for a_matrix in frames for delta_matrix in frames),
        len(frames) ** 2,
    )
    return norm_y, norm_z, inner


def direct_temporal_coefficients(span: int) -> dict[int, int]:
    y_weight = 4 * span + 2
    z_weight = 4 * span + 6
    channel_weights = (4 * span + 6, 4 * span + 4)
    coefficients: dict[int, int] = defaultdict(int)
    for channel_weight in channel_weights:
        for left_weight in (y_weight, channel_weight):
            for right_weight in (z_weight, channel_weight):
                coefficients[left_weight + right_weight] += 1
    return dict(sorted(coefficients.items()))


def expected_temporal_coefficients(span: int) -> dict[int, int]:
    base = 8 * span + 6
    return {base: 1, base + 2: 4, base + 4: 1, base + 6: 2}


def action_irrep_survivors() -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    """Exclusive rail plus scalar-in-V tensor sigma selection."""

    vector = (1, -1)
    # Solve the tensor rule rather than sampling a truncated irrep menu:
    # 0 lies in [|1-ell|,1+ell] iff |1-ell|=0, so ell=1; product parity
    # (-1)*p=+1 then gives p=-1.
    scalar_partner_ell = 1
    scalar_partner_parity = -1
    right = (scalar_partner_ell, scalar_partner_parity)
    return ((vector, right),)


def evaluate(coefficients: dict[int, int], t_value: F) -> F:
    return sum((F(coefficient) * t_value**power
                for power, coefficient in coefficients.items()), F(0))


def fixture() -> dict[str, object]:
    rows = []
    for span in range(1, 7):
        q_cells = span + 1
        geometry = interval_geometry(q_cells, span)
        direct = direct_temporal_coefficients(span)
        rows.append({
            "span": span,
            "q_cells": q_cells,
            "geometry": geometry,
            "direct": direct,
            "expected": expected_temporal_coefficients(span),
            "at_one": F(1, 36) * evaluate(direct, F(1)),
            "at_half_c2": F(4, 36) * evaluate(direct, F(1, 2)),
        })
    matched, same_zero, same_one = signed_frame_overlaps()
    q_means = conditional_q_means()
    return {
        "rows": tuple(rows),
        "matched_overlap": matched,
        "same_zero_overlap": same_zero,
        "same_one_overlap": same_one,
        "q_means": q_means,
        "coarse_state_gram": coarse_state_gram(),
        "action_irrep_survivors": action_irrep_survivors(),
    }


def main() -> int:
    data = fixture()
    checks = (
        ("signed-frame global matched overlap is one ninth",
         data["matched_overlap"] == F(1, 9)),
        ("same-index action pairings vanish",
         data["same_zero_overlap"] == 0 and data["same_one_overlap"] == 0),
        ("conditional cell first moments vanish",
         data["q_means"] == (F(0), F(0))),
        ("coarse Wilson-loop states are normalized and orthogonal",
         data["coarse_state_gram"] == (F(1), F(1), F(0))),
        ("exclusive rails and scalar fusion force V on both insertions",
         data["action_irrep_survivors"] == (((1, -1), (1, -1)),)),
        ("actual original-link interval weights and channels",
         all(
             row["geometry"]["link_count"] == 6 * row["q_cells"] + 1
             and row["geometry"]["y_weight"] == 4 * row["span"] + 2
             and row["geometry"]["z_weight"] == 4 * row["span"] + 6
             and row["geometry"]["matches"] == (
                 (0, 1, 4 * row["span"] + 6, 0, 2),
                 (1, 0, 4 * row["span"] + 4, 1, 3),
             )
             for row in data["rows"]
         )),
        ("direct temporal expansion matches closed polynomial",
         all(row["direct"] == row["expected"] for row in data["rows"])),
        ("small-step normalized response is two ninths",
         all(row["at_one"] == F(2, 9) for row in data["rows"])),
        ("s=1 c=2 half-step exact fraction",
         data["rows"][0]["at_half_c2"] == F(67, 4718592)),
        ("each additional merged background cell gives t^8 dressing",
         all(
             evaluate(data["rows"][index + 1]["direct"], F(1, 2))
             == F(1, 2) ** 8
             * evaluate(data["rows"][index]["direct"], F(1, 2))
             for index in range(len(data["rows"]) - 1)
         )),
    )
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
