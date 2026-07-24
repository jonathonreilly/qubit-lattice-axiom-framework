#!/usr/bin/env python3
"""Independent finite check for the proper-cubic admission-table classifier.

This checker does not import the primary runner.  It reconstructs the 64-word
domain, the 24 signed-permutation frames, the five supplied shell tables, and
the held-corpus controls from the finite definitions below, then writes the
comparison grid consumed by the primary runner.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / (
    "finite_proper_cubic_admission_table_discriminator_"
    "independent_grid_2026_07_23.json"
)

DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
WORDS = tuple(itertools.product((0, 1), repeat=6))
LAW_ORDER = (
    "unique_quorum",
    "odd_shells",
    "nonempty",
    "low_density",
    "even_nonzero",
)
LAWS = {
    "unique_quorum": frozenset((1,)),
    "odd_shells": frozenset((1, 3, 5)),
    "nonempty": frozenset((1, 2, 3, 4, 5, 6)),
    "low_density": frozenset((1, 2)),
    "even_nonzero": frozenset((2, 4, 6)),
}


def det3(matrix):
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def matvec(matrix, vector):
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )


def frames():
    result = []
    direction_index = {direction: index for index, direction in enumerate(DIRECTIONS)}
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = [[0, 0, 0] for _ in range(3)]
            for row in range(3):
                matrix[row][permutation[row]] = signs[row]
            if det3(matrix) != 1:
                continue
            result.append(
                tuple(direction_index[matvec(matrix, direction)] for direction in DIRECTIONS)
            )
    assert len(result) == 24 and len(set(result)) == 24
    return tuple(result)


def rotate(word, frame):
    rotated = [0] * 6
    for old_slot, new_slot in enumerate(frame):
        rotated[new_slot] = word[old_slot]
    return tuple(rotated)


def orbit_census(frame_set):
    unseen = set(WORDS)
    census = []
    while unseen:
        representative = min(unseen)
        orbit = {rotate(representative, frame) for frame in frame_set}
        unseen -= orbit
        census.append(
            {
                "shell": sum(representative),
                "size": len(orbit),
                "representative": list(representative),
            }
        )
    census.sort(key=lambda item: (item["shell"], item["size"], item["representative"]))
    assert sum(item["size"] for item in census) == 64
    return census


def accepts(law, word):
    return int(sum(word) in LAWS[law])


def distinct_on_shells(names, shells):
    profiles = {
        tuple(int(shell in LAWS[name]) for shell in shells)
        for name in names
    }
    return len(profiles) == len(names)


def minimum_separating_sets(names, shell_pool):
    shell_pool = tuple(shell_pool)
    for size in range(len(shell_pool) + 1):
        result = [
            list(shells)
            for shells in itertools.combinations(shell_pool, size)
            if distinct_on_shells(names, shells)
        ]
        if result:
            return result
    return []


def consistent_laws(observations):
    return sorted(
        law
        for law in LAW_ORDER
        if all(accepts(law, word) == bit for word, bit in observations)
    )


def main():
    frame_set = frames()
    shell_profiles = {
        law: [int(shell in LAWS[law]) for shell in range(7)]
        for law in LAW_ORDER
    }

    pairwise = []
    for left, right in itertools.combinations(LAW_ORDER, 2):
        train = held = 0
        for word in WORDS:
            if accepts(left, word) == accepts(right, word):
                continue
            if sum(word) <= 3:
                train += 1
            else:
                held += 1
        pairwise.append(
            {"left": left, "right": right, "train": train, "held": held, "total": train + held}
        )

    shell1 = tuple(word for word in WORDS if sum(word) == 1)
    shell1_unique = consistent_laws(
        tuple((word, accepts("unique_quorum", word)) for word in shell1)
    )
    shell1_even = consistent_laws(
        tuple((word, accepts("even_nonzero", word)) for word in shell1)
    )

    train = tuple(word for word in WORDS if sum(word) <= 3)
    train_only = {
        law: consistent_laws(tuple((word, accepts(law, word)) for word in train)) == [law]
        for law in LAW_ORDER
    }

    mimic_train = mimic_held = 0
    mimic_weights = set()
    for word in WORDS:
        mimic = int(sum(word) in (1, 3))
        if mimic == accepts("odd_shells", word):
            continue
        if sum(word) <= 3:
            mimic_train += 1
        else:
            mimic_held += 1
            mimic_weights.add(sum(word))

    antipodal_pairs = {frozenset((0, 1)), frozenset((2, 3)), frozenset((4, 5))}

    def antipodal(word):
        return int(frozenset(index for index, bit in enumerate(word) if bit) in antipodal_pairs)

    by_shell = defaultdict(set)
    for word in WORDS:
        by_shell[sum(word)].add(antipodal(word))
    antipodal_orbit_constant = all(
        antipodal(rotate(word, frame)) == antipodal(word)
        for word in WORDS
        for frame in frame_set
    )
    shell2 = tuple(word for word in WORDS if sum(word) == 2)

    result = {
        "antipodal": {
            "accepted_count": sum(antipodal(word) for word in WORDS),
            "is_shell_function": all(len(values) == 1 for values in by_shell.values()),
            "orbit_constant": antipodal_orbit_constant,
            "shell2_accept_reject": [sum(antipodal(word) for word in shell2), len(shell2)],
        },
        "completing_sets_after_shell1_uq": minimum_separating_sets(
            shell1_unique, (0, 2, 3, 4, 5, 6)
        ),
        "generator_path": str(Path(__file__).resolve().relative_to(ROOT)),
        "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "mimic_odd_disagreements": {
            "train": mimic_train,
            "held": mimic_held,
            "held_witness_weights": sorted(mimic_weights),
        },
        "minimal_separating_shell_sets": minimum_separating_sets(LAW_ORDER, range(7)),
        "orbit_census": orbit_census(frame_set),
        "pairwise_separators": pairwise,
        "scenario_consistent_sets": {
            "shell1_stream_labeled_by_unique_quorum": shell1_unique,
            "shell1_stream_labeled_by_even_nonzero": shell1_even,
        },
        "shell_profiles": shell_profiles,
        "train_only_identifiable": train_only,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=1, sort_keys=True) + "\n")
    print(
        f"frames={len(frame_set)} orbits={len(result['orbit_census'])} "
        f"minimum_sets={len(result['minimal_separating_shell_sets'])} "
        f"mimic_train={mimic_train} mimic_held={mimic_held}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
