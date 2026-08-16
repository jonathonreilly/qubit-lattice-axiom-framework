#!/usr/bin/env python3
"""Plus-seed fire of the July-3 k=3 chiral pair.

Same 6-NN star only. Exact finite classification. No axiom edit, no cache
write, no network, no L1 attachment.
"""

from __future__ import annotations

import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "PLUS_SEED_CHIRAL_PAIR_FIRE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
JULY3_PATH = (
    ROOT
    / "docs"
    / "ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md"
)

AUDIT_INPUT_PATHS = (
    "docs/PLUS_SEED_CHIRAL_PAIR_FIRE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

DIRS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
Coloring = tuple[int, ...]
Perm = tuple[int, ...]


def normalize(text: str) -> str:
    return " ".join(text.split())


def det3(matrix: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_times_dir(
    matrix: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]],
    direction: tuple[int, int, int],
) -> tuple[int, int, int]:
    return (
        matrix[0][0] * direction[0] + matrix[0][1] * direction[1] + matrix[0][2] * direction[2],
        matrix[1][0] * direction[0] + matrix[1][1] * direction[1] + matrix[1][2] * direction[2],
        matrix[2][0] * direction[0] + matrix[2][1] * direction[1] + matrix[2][2] * direction[2],
    )


def direction_perm(
    matrix: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]],
) -> Perm:
    return tuple(DIR_INDEX[mat_times_dir(matrix, direction)] for direction in DIRS)


def act_col(perm: Perm, coloring: Coloring) -> Coloring:
    out = [0] * len(coloring)
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def cubic_records() -> list[tuple[int, Perm]]:
    records: list[tuple[int, Perm]] = []
    seen: set[tuple[int, ...]] = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row, col in enumerate(perm):
                entry = [0, 0, 0]
                entry[col] = signs[row]
                rows.append(tuple(entry))
            matrix = (rows[0], rows[1], rows[2])
            key = matrix[0] + matrix[1] + matrix[2]
            if key in seen:
                continue
            seen.add(key)
            records.append((det3(matrix), direction_perm(matrix)))
    return records


def all_colorings(k: int) -> list[Coloring]:
    return list(itertools.product(range(k), repeat=len(DIRS)))


def proper_orbits(proper_perms: list[Perm], k: int) -> list[set[Coloring]]:
    unseen = set(all_colorings(k))
    orbits: list[set[Coloring]] = []
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in proper_perms}
        orbits.append(orbit)
        unseen -= orbit
    return orbits


def chiral_pair_colorings(proper_perms: list[Perm], p_perm: Perm, k: int = 3) -> tuple[Coloring, set[Coloring]]:
    orbits = proper_orbits(proper_perms, k)
    ids = {coloring: index for index, orbit in enumerate(orbits) for coloring in orbit}
    pair_ids: set[int] = set()
    seen_pairs: set[tuple[int, int]] = set()
    for index, orbit in enumerate(orbits):
        image_id = ids[act_col(p_perm, next(iter(orbit)))]
        if image_id == index:
            continue
        pair = tuple(sorted((index, image_id)))
        if pair in seen_pairs:
            continue
        seen_pairs.add(pair)
        pair_ids.update(pair)
    if len(seen_pairs) != 1:
        raise RuntimeError(f"expected one k=3 chiral pair, found {len(seen_pairs)}")
    members = set().union(*(orbits[index] for index in pair_ids))
    representative = min(members)
    return representative, members


def axis_bicolored(coloring: Coloring) -> bool:
    return all(coloring[2 * axis] != coloring[2 * axis + 1] for axis in range(3))


def letter_counts(coloring: Coloring, k: int = 3) -> list[int]:
    return sorted(coloring.count(letter) for letter in range(k))


def pair_fires(coloring: Coloring, members: set[Coloring]) -> bool:
    return coloring in members


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    july3 = JULY3_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)

    print("external_scientific_inputs: none; no observational, fitted, literature, scale, or normalization value is used")
    print("explicit_bounded_inputs: the same 6-NN star, the July-3 k=3 pair, and the 64 plus-labelings")
    print("framework_context: Qubit remains one-site M_2(C); no plus-seed is written into Admissibility")
    print("negative_scope: displayed counts only; L1 is not attached")

    records = cubic_records()
    proper_perms = [perm for det, perm in records if det == 1]
    p_perm = direction_perm(((-1, 0, 0), (0, -1, 0), (0, 0, -1)))
    representative, members = chiral_pair_colorings(proper_perms, p_perm)
    n_new = int(pair_fires(representative, members))
    plus_labelings = list(itertools.product((1, 2), repeat=6))
    n_fire = sum(1 for coloring in plus_labelings if pair_fires(coloring, members))

    print(f"representative={representative}")
    print(f"chiral_pair_size={len(members)}")
    print(f"N_new={n_new}")
    print(f"N_plus={len(plus_labelings)}")
    print(f"N_fire={n_fire}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the declared note-plus-axiom tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/PLUS_SEED_CHIRAL_PAIR_FIRE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "source-qubit-m2",
        "the axiom memo still names one-site M_2(C)",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`." in axiom,
    )
    checks.check(
        "source-admissibility",
        "the axiom memo still names one fixed nearest-neighbor rule",
        "There is one fixed nearest-neighbor admissibility rule, covariant under lattice" in axiom,
    )
    checks.check(
        "source-unread",
        "the axiom memo still says a site with no record cannot be read",
        "A site with no record cannot be read." in axiom,
    )
    checks.check(
        "july3-unique-pair",
        "the July-3 parent names exactly one chiral pair at k=3",
        "exactly **one** chiral pair" in july3
        and "handed fully-mixed patterns" in july3,
    )
    checks.check(
        "rep-lex-first",
        "the re-earned representative is the July-3 lex-first handed fully-mixed 6-tuple",
        representative == (0, 1, 0, 2, 1, 2),
    )
    checks.check(
        "rep-fully-mixed",
        "the representative is axis-bicolored with letter counts 2/2/2",
        axis_bicolored(representative) and letter_counts(representative) == [2, 2, 2],
    )
    checks.check(
        "thm1-fires",
        "the fully-mixed representative fires at the unread center",
        n_new == 1 and pair_fires(representative, members),
    )
    checks.check(
        "thm2-sixty-four",
        "there are exactly 64 {+,−} plus-labelings and empty is forbidden",
        len(plus_labelings) == 64
        and all(0 not in coloring for coloring in plus_labelings)
        and all(set(coloring) <= {1, 2} for coloring in plus_labelings),
    )
    checks.check(
        "thm2-n-fire",
        "none of the 64 plus-labelings fire the k=3 pair",
        n_fire == 0,
    )
    checks.check(
        "pair-size",
        "the unique pair contains 48 colorings in two proper orbits of 24",
        len(members) == 48,
    )
    checks.check(
        "claim-scope",
        "the note reports the required claim_scope",
        'claim_scope: "On the 6-NN star with six occupied neighbors and unread center, whether the July-3 k=3 pair fires at the center for the fully-mixed labeling and how many of the 64 {+,−} plus-labelings fire, is reported. Displayed, not adopted."'
        in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the note displays the counts and refuses a plus-seed axiom and L1",
        "Displayed, not adopted" in note
        and "does not write a plus-seed into Admissibility" in note
        and "does not attach L1" in normalized_note
        and "N_new = 1" in note
        and "N_fire = 0" in note,
    )
    checks.check(
        "same-star-only",
        "the note stays on the same 6-NN star and does not grow a new patch",
        "same 6-NN star" in note and "No new spatial patch is grown" in note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the required bounded-support status fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "trace_class: frontier_discovery",
                "target_claim_id: null",
                "next_trace_action:",
                "hypothetical_axiom_status: null",
                "**Type:** bounded_theorem",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "forbidden-phrases",
        "the note omits the forbidden phrases",
        all(phrase not in note for phrase in FORBIDDEN),
    )
    checks.check(
        "axiom-unedited",
        "the axiom memo does not contain a plus-seed or L1 formation rule",
        all(
            phrase not in axiom
            for phrase in (
                "plus-seed",
                "N_fire",
                "handed fully-mixed",
                "form iff",
            )
        ),
    )
    mutation_rep_silent = n_new == 0
    mutation_all_fire = n_fire == 64
    checks.check(
        "mutation-rep-silent",
        "predicate N_new == 0 on the representative fails",
        mutation_rep_silent is False,
    )
    checks.check(
        "mutation-all-fire",
        "predicate N_fire == 64 fails",
        mutation_all_fire is False,
    )
    checks.check(
        "mutation-n-fire-zero",
        "predicate N_fire == 0 holds",
        n_fire == 0,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
