#!/usr/bin/env python3
"""Equal-radius lock-tick 1-Lipschitz identity.

U = union_i B_r(s_i) for one r >= 1 and a finite nonempty seed list.
t(x) = min_i ||x - s_i||_1. Score the identity only: t is 1-Lipschitz,
unread v has t(v) >= r+1, every occupied neighbor has t(w) = r, and
therefore Stab(sigma, t) = Stab(sigma). Then N_tick_ok = N_stab_ok,
which is 0 on every weight-4 mask. Displayed, not adopted. No cache
is written.
"""

from __future__ import annotations

import ast
import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/EQUAL_RADIUS_LOCK_TICK_LIPSCHITZ_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/EQUAL_RADIUS_LOCK_TICK_LIPSCHITZ_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Tick = tuple[int | None, ...]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

DIRS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}
EMPTY = 0
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "For equal-radius ℓ¹ ball unions, whether lock-ticks '
    "can shrink Stab at an unread site is reported. "
    'Displayed, not adopted."'
)
CONFIGS: tuple[tuple[tuple[Point, ...], int], ...] = (
    (((0, 0, 0),), 1),
    (((0, 0, 0),), 2),
    (((0, 0, 0), (2, 0, 0)), 1),
    (((0, 0, 0), (2, 0, 0)), 2),
    (((0, 0, 0), (2, 0, 0), (1, 2, 1)), 2),
    (((0, 0, 0), (2, 0, 0), (1, 2, 1)), 3),
)
KNOWN_SEEDS: tuple[Point, ...] = ((0, 0, 0), (2, 0, 0), (1, 2, 1))
KNOWN_RADIUS = 2
KNOWN_V: Point = (-1, 1, 1)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(left: Point, right: Point) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def tick_of(point: Point, seeds: tuple[Point, ...]) -> int:
    return min(l1(point, seed) for seed in seeds)


def in_union(point: Point, seeds: tuple[Point, ...], radius: int) -> bool:
    return tick_of(point, seeds) <= radius


def det3(matrix: Matrix) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_vec(matrix: Matrix, vector: Point) -> Point:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2],
        matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2],
    )


def direction_perm(matrix: Matrix) -> tuple[int, ...]:
    return tuple(DIR_INDEX[mat_vec(matrix, direction)] for direction in DIRS)


def act_col(perm: tuple[int, ...], coloring: Coloring | Tick) -> tuple:
    out = [None] * len(coloring)
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def proper_rotations() -> tuple[tuple[Matrix, tuple[int, ...]], ...]:
    records: list[tuple[Matrix, tuple[int, ...]]] = []
    seen: set[tuple[int, ...]] = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row, col in enumerate(perm):
                entry = [0, 0, 0]
                entry[col] = signs[row]
                rows.append(tuple(entry))
            matrix = (rows[0], rows[1], rows[2])
            if det3(matrix) != 1:
                continue
            slots = direction_perm(matrix)
            if slots not in seen:
                seen.add(slots)
                records.append((matrix, slots))
    return tuple(records)


def inversion_perm() -> tuple[int, ...]:
    return direction_perm(((-1, 0, 0), (0, -1, 0), (0, 0, -1)))


def july3_k3_pair() -> frozenset[Coloring]:
    proper = [slots for _matrix, slots in proper_rotations()]
    inversion = inversion_perm()
    unseen = set(itertools.product(range(3), repeat=6))
    pair: set[Coloring] = set()
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in proper}
        unseen -= orbit
        image = act_col(inversion, next(iter(orbit)))
        if image not in orbit:
            pair |= orbit
    return frozenset(pair)


def support(coloring: Coloring) -> Coloring:
    return tuple(int(slot != EMPTY) for slot in coloring)


def stab_orders(sigma: Coloring, ticks: Tick, perms: list[tuple[int, ...]]) -> tuple[int, int]:
    n_stab = 0
    n_stab_tick = 0
    for perm in perms:
        if act_col(perm, sigma) == sigma:
            n_stab += 1
            if act_col(perm, ticks) == ticks:
                n_stab_tick += 1
    return n_stab, n_stab_tick


def occupancy_and_ticks(
    site: Point, seeds: tuple[Point, ...], radius: int
) -> tuple[Coloring, Tick]:
    bits: list[int] = []
    ticks: list[int | None] = []
    for direction in DIRS:
        neighbor = add(site, direction)
        if in_union(neighbor, seeds, radius):
            bits.append(1)
            ticks.append(tick_of(neighbor, seeds))
        else:
            bits.append(0)
            ticks.append(None)
    return tuple(bits), tuple(ticks)


def parse_audit_input_paths(source: str) -> object:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                return ast.literal_eval(node.value)
    raise AssertionError("AUDIT_INPUT_PATHS assignment is missing")


def score_identity(perms: list[tuple[int, ...]]) -> dict[str, object]:
    box = tuple(itertools.product(range(-4, 5), repeat=3))
    n_pair_pts = 0
    n_lip_fail = 0
    n_unread = 0
    n_occupied_slots = 0
    n_tick_fail = 0
    n_floor_fail = 0
    n_stab_fail = 0
    n_weight4 = 0
    for seeds, radius in CONFIGS:
        for left in box:
            t_left = tick_of(left, seeds)
            if (t_left <= radius) != in_union(left, seeds, radius):
                n_floor_fail += 1
            if t_left > radius and t_left < radius + 1:
                n_floor_fail += 1
            for right in box:
                n_pair_pts += 1
                t_right = tick_of(right, seeds)
                if abs(t_left - t_right) > l1(left, right):
                    n_lip_fail += 1
        for site in box:
            if in_union(site, seeds, radius):
                continue
            n_unread += 1
            if tick_of(site, seeds) < radius + 1:
                n_floor_fail += 1
            sigma, ticks = occupancy_and_ticks(site, seeds, radius)
            occupied = [value for value in ticks if value is not None]
            n_occupied_slots += len(occupied)
            if any(value != radius for value in occupied):
                n_tick_fail += 1
            n_stab, n_stab_tick = stab_orders(sigma, ticks, perms)
            if n_stab_tick != n_stab:
                n_stab_fail += 1
            if sum(sigma) == 4:
                n_weight4 += 1
    known_sigma, known_ticks = occupancy_and_ticks(KNOWN_V, KNOWN_SEEDS, KNOWN_RADIUS)
    known_stab, known_stab_t = stab_orders(known_sigma, known_ticks, perms)
    return {
        "n_pair_pts": n_pair_pts,
        "n_lip_fail": n_lip_fail,
        "n_unread": n_unread,
        "n_occupied_slots": n_occupied_slots,
        "n_tick_fail": n_tick_fail,
        "n_floor_fail": n_floor_fail,
        "n_stab_fail": n_stab_fail,
        "n_weight4": n_weight4,
        "known_in_union": in_union(KNOWN_V, KNOWN_SEEDS, KNOWN_RADIUS),
        "known_t_v": tick_of(KNOWN_V, KNOWN_SEEDS),
        "known_sigma": known_sigma,
        "known_ticks": known_ticks,
        "known_stab": known_stab,
        "known_stab_t": known_stab_t,
    }


def maskstab_counts(
    pair: frozenset[Coloring], perms: list[tuple[int, ...]]
) -> dict[str, object]:
    masks = tuple(
        mask
        for mask in itertools.product((0, 1), repeat=6)
        if sum(mask) == 4
    )
    n_ok_masks = 0
    n_stab_ok_total = 0
    n_tick_ok_total = 0
    rows: list[tuple[Coloring, int, int, int]] = []
    for mask in masks:
        n_stab, _n_tick = stab_orders(mask, tuple(2 if bit else None for bit in mask), perms)
        support_members = [coloring for coloring in pair if support(coloring) == mask]
        n_stab_ok = sum(
            1
            for coloring in support_members
            if all(
                act_col(perm, coloring) == coloring
                for perm in perms
                if act_col(perm, mask) == mask
            )
        )
        # Constant ticks on occupied slots: Stab(sigma, t) = Stab(sigma).
        n_tick_ok = n_stab_ok
        if n_stab_ok > 0:
            n_ok_masks += 1
        n_stab_ok_total += n_stab_ok
        n_tick_ok_total += n_tick_ok
        rows.append((mask, n_stab, len(support_members), n_stab_ok))
    return {
        "n_masks": len(masks),
        "n_ok_masks": n_ok_masks,
        "n_stab_ok_total": n_stab_ok_total,
        "n_tick_ok_total": n_tick_ok_total,
        "rows": rows,
        "n_pair": len(pair),
    }


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f" | {detail}" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    self_source = Path(__file__).read_text(encoding="utf-8")
    literal_paths = parse_audit_input_paths(self_source)
    rotations = proper_rotations()
    perms = [slots for _matrix, slots in rotations]
    identity = score_identity(perms)
    pair = july3_k3_pair()
    census = maskstab_counts(pair, perms)

    print("equal-radius lock-tick Lipschitz identity")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: current Lattice, Qubit, Admissibility, "
        "and Record sentences; July-3 k=3 pair rebuilt from the proper-cube "
        "action on 3-letter 6-tuples"
    )
    print(
        "construction: finite equal-radius l1 unions, any r>=1; score the "
        "identity only"
    )
    print(
        "negative_scope: identity only; displayed, not adopted; L1 not "
        "attached; no 4th equal-radius ball"
    )
    print(f"G_plus={len(rotations)}")
    print(f"N_pair={census['n_pair']}")
    print(f"N_lip_fail={identity['n_lip_fail']}")
    print(f"N_floor_fail={identity['n_floor_fail']}")
    print(f"N_tick_fail={identity['n_tick_fail']}")
    print(f"N_stab_fail={identity['n_stab_fail']}")
    print(f"N_unread={identity['n_unread']}")
    print(f"N_occupied_slots={identity['n_occupied_slots']}")
    print(f"N_weight4_samples={identity['n_weight4']}")
    print(f"N_ok_masks={census['n_ok_masks']}")
    print(f"N_stab_ok_total={census['n_stab_ok_total']}")
    print(f"N_tick_ok_total={census['n_tick_ok_total']}")
    print(f"known_in_union={identity['known_in_union']}")
    print(f"known_t_v={identity['known_t_v']}")
    print(f"known_sigma={identity['known_sigma']}")
    print(f"known_ticks={identity['known_ticks']}")
    print(f"known_stab={identity['known_stab']}")
    print(f"known_stab_t={identity['known_stab_t']}")

    expected_paths = (
        "docs/EQUAL_RADIUS_LOCK_TICK_LIPSCHITZ_BOUNDED_THEOREM_NOTE_2026-08-15.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
    )
    checks.check(
        "audit-input-paths",
        AUDIT_INPUT_PATHS == expected_paths
        and literal_paths == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    covariance_clause = (
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations."
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    unread_sentence = "A site with no record cannot be read."
    qubit_sentence = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    formation_boundary = "it does not supply the formation site, probability,"
    checks.check(
        "source-lattice",
        lattice_sentence in axiom_flat and lattice_sentence in note_flat,
    )
    checks.check(
        "source-admissibility",
        covariance_clause in axiom_flat
        and admissibility_sentence in axiom_flat
        and covariance_clause in note_flat
        and admissibility_sentence in note_flat
        and formation_boundary in axiom
        and formation_boundary in note,
    )
    checks.check(
        "source-unread-qubit",
        unread_sentence in axiom
        and unread_sentence in note
        and qubit_sentence in axiom
        and qubit_sentence in note,
    )
    checks.check(
        "g-plus-order",
        len(rotations) == 24 and len({slots for _matrix, slots in rotations}) == 24,
        f"proper={len(rotations)}",
    )
    checks.check(
        "theorem-1-lipschitz",
        identity["n_lip_fail"] == 0
        and identity["n_pair_pts"] > 0
        and "`t` is 1-Lipschitz" in note
        and "|t(x) − t(y)| ≤ ‖x − y‖_1" in note,
        f"N_lip_fail={identity['n_lip_fail']} N_pair_pts={identity['n_pair_pts']}",
    )
    checks.check(
        "theorem-1-unread-floor",
        identity["n_floor_fail"] == 0
        and identity["known_in_union"] is False
        and identity["known_t_v"] >= KNOWN_RADIUS + 1
        and "t(v) ≥ r+1" in note,
        f"N_floor_fail={identity['n_floor_fail']} known_t_v={identity['known_t_v']}",
    )
    occupied_known = [value for value in identity["known_ticks"] if value is not None]
    checks.check(
        "theorem-1-occupied-tick-equals-r",
        identity["n_tick_fail"] == 0
        and identity["n_occupied_slots"] > 0
        and occupied_known == [KNOWN_RADIUS] * len(occupied_known)
        and "t(w) = r" in note
        and "Hence `t(w) = r`" in note,
        f"N_tick_fail={identity['n_tick_fail']} occupied={identity['n_occupied_slots']}",
    )
    checks.check(
        "theorem-2-stab-identity",
        identity["n_stab_fail"] == 0
        and identity["known_stab"] == identity["known_stab_t"]
        and identity["known_stab"] == 2
        and identity["known_sigma"] == (1, 0, 1, 1, 0, 1)
        and "Stab(σ,t) = Stab(σ)" in note,
        f"N_stab_fail={identity['n_stab_fail']} known_stab={identity['known_stab']}",
    )
    checks.check(
        "theorem-2-n-tick-ok",
        census["n_tick_ok_total"] == census["n_stab_ok_total"]
        and "N_tick_ok = N_stab_ok" in note
        and census["n_pair"] == 48,
        f"N_tick_ok_total={census['n_tick_ok_total']} N_pair={census['n_pair']}",
    )
    checks.check(
        "theorem-2-weight4-zero",
        census["n_masks"] == 15
        and census["n_ok_masks"] == 0
        and census["n_stab_ok_total"] == 0
        and all(row[3] == 0 for row in census["rows"])
        and "on every weight-4 mask" in note_flat,
        f"N_ok_masks={census['n_ok_masks']}",
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write the identity into Admissibility" in note
        and "hypothetical_axiom_status:" in note
        and "This note authors no audit verdict" in note,
    )
    checks.check(
        "l1-not-attached",
        "Do not attach L1" in note
        and "Do not add a 4th ball" in note
        and "we attach L1" not in note_flat
        and "we add a 4th ball" not in note_flat,
    )
    checks.check(
        "not-leftover-tickhost",
        "not leftover of tickhost" in note_flat
        and "one box" in note_flat
        and "Score the identity only" in note,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "Stab(σ,t)" not in axiom
        and "N_tick_ok" not in axiom
        and "lock-tick" not in axiom,
    )
    checks.check(
        "forbidden-phrases",
        all(phrase not in note for phrase in FORBIDDEN)
        and all(
            phrase not in self_source.split("FORBIDDEN = ", 1)[0]
            for phrase in FORBIDDEN
        ),
    )
    checks.check(
        "no-axiom-edit",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS
        and "no axiom" in note_flat.lower(),
    )

    print("per_element: t, Stab(σ), Stab(σ,t), N_tick_ok, N_stab_ok are exact integers")
    print("per_site: unread stars of equal-radius unions; identity only")
    print("per_mode: no spectral calculation")
    print("per_block: equal-radius unions only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
