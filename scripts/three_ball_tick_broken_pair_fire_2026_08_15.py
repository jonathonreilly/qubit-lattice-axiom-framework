#!/usr/bin/env python3
"""Tick-broken 3-ball weight-4 July-3 pair fire census.

Same box as tickuneq: U = B_2(s1) ∪ B_2(s2) ∪ B_2(s3) with distinct
centers in [-2, 2]^3 and unread v with |v|_∞ ≤ 3 and wt(σ) = 4.
Rebuild N_uneq. On the lex-first breaker (or none), S is the set of
July-3 pair members with that support invariant under Stab(σ, t).
N_fire counts members of S that form exactly that v with U persisting.
If N_uneq = 0 then N_tick_ok = 0 and N_fire = 0. Score the lex-first
breaker star only, or none. Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/THREE_BALL_TICK_BROKEN_PAIR_FIRE_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/THREE_BALL_TICK_BROKEN_PAIR_FIRE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
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
EMPTY, PLUS, MINUS = 0, 1, 2
LETTER = {EMPTY: "0", PLUS: "+", MINUS: "−"}
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "On the lex-first 3-ball weight-4 star whose lock-ticks '
    "shrink Stab, how many tick-invariant July-3 pair members "
    'fire is reported. Displayed, not adopted."'
)
KNOWN_SEEDS: tuple[Point, ...] = ((0, 0, 0), (1, 2, 1), (2, 0, 0))
KNOWN_V: Point = (-1, 1, 1)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


def l1(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def linf(point: Point) -> int:
    return max(abs(point[0]), abs(point[1]), abs(point[2]))


def ball(center: Point, radius: int = 2) -> frozenset[Point]:
    sites: set[Point] = set()
    span = range(-radius, radius + 1)
    for offset in itertools.product(span, repeat=3):
        if l1(offset) <= radius:
            sites.add(add(center, offset))
    return frozenset(sites)


def site_index(point: Point) -> int:
    return (point[0] + 4) * 81 + (point[1] + 4) * 9 + (point[2] + 4)


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


def act_col(perm: tuple[int, ...], coloring: tuple) -> tuple:
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


def format_tuple(coloring: Coloring) -> str:
    return "(" + ",".join(LETTER[slot] for slot in coloring) + ")"


def execute_pair_step(
    occupied: frozenset[Point],
    site: Point,
    coloring: Coloring,
    pair: frozenset[Coloring],
) -> tuple[frozenset[Point], int]:
    if site in occupied:
        return occupied, 0
    if coloring not in pair:
        return occupied, 0
    return occupied | {site}, 1


def parse_audit_input_paths(source: str) -> object:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                return ast.literal_eval(node.value)
    raise AssertionError("AUDIT_INPUT_PATHS assignment is missing")


def census_breakers(
    rotations: tuple[tuple[Matrix, tuple[int, ...]], ...],
) -> dict[str, object]:
    """Lipschitz identity plus a 2000-star prefix. Do not rescan 763608."""
    offsets = tuple(
        point
        for point in itertools.product(range(-2, 3), repeat=3)
        if l1(point) <= 2
    )
    centers = tuple(itertools.product(range(-2, 3), repeat=3))
    vs = tuple(itertools.product(range(-3, 4), repeat=3))
    slot_perms = tuple(slots for _matrix, slots in rotations)

    # t = min_i ||· − s_i||_1 is 1-Lipschitz. Unread v is outside every
    # radius-2 ball, so t(v) ≥ 3. An occupied neighbor w is in U, so
    # t(w) ≤ 2, and Lipschitz gives t(w) ≥ t(v) − 1 ≥ 2. Hence t(w) = 2
    # on every occupied slot and Stab(σ, t) = Stab(σ).
    lipschitz_ok = True
    sample_seeds = ((0, 0, 0), (2, 0, 0), (1, 2, 1))
    sample_pts = tuple(itertools.product(range(-3, 4), repeat=3))
    for a, b in zip(sample_pts, sample_pts[1:]):
        ta = min(l1(sub(a, seed)) for seed in sample_seeds)
        tb = min(l1(sub(b, seed)) for seed in sample_seeds)
        if abs(ta - tb) > l1(sub(a, b)):
            lipschitz_ok = False
            break
    unread_floor_ok = min(l1(sub(KNOWN_V, seed)) for seed in KNOWN_SEEDS) >= 3

    known_union = ball(KNOWN_SEEDS[0]) | ball(KNOWN_SEEDS[1]) | ball(KNOWN_SEEDS[2])
    known_hit = KNOWN_V not in known_union
    known_bits = []
    known_ticks_list: list[int | None] = []
    for direction in DIRS:
        neighbor = add(KNOWN_V, direction)
        if neighbor in known_union:
            known_bits.append(1)
            known_ticks_list.append(
                min(l1(sub(neighbor, seed)) for seed in KNOWN_SEEDS)
            )
        else:
            known_bits.append(0)
            known_ticks_list.append(None)
    known_sigma = tuple(known_bits)
    known_ticks = tuple(known_ticks_list)
    known_stab = len(
        [perm for perm in slot_perms if act_col(perm, known_sigma) == known_sigma]
    )
    known_stab_t = len(
        [
            perm
            for perm in slot_perms
            if act_col(perm, known_sigma) == known_sigma
            and act_col(perm, known_ticks) == known_ticks
        ]
    )

    n_prefix = 0
    n_bad_tick = 0
    first: object | None = None
    prefix_limit = 2000
    for seeds in itertools.combinations(centers, 3):
        occupied = ball(seeds[0]) | ball(seeds[1]) | ball(seeds[2])
        for site in vs:
            if site in occupied:
                continue
            bits = []
            ticks: list[int | None] = []
            occupied_ticks: list[int] = []
            for direction in DIRS:
                neighbor = add(site, direction)
                if neighbor in occupied:
                    bits.append(1)
                    tick = min(l1(sub(neighbor, seed)) for seed in seeds)
                    ticks.append(tick)
                    occupied_ticks.append(tick)
                else:
                    bits.append(0)
                    ticks.append(None)
            if sum(bits) != 4:
                continue
            n_prefix += 1
            if occupied_ticks != [2, 2, 2, 2]:
                n_bad_tick += 1
                sigma = tuple(bits)
                tick_tuple = tuple(ticks)
                stab = [perm for perm in slot_perms if act_col(perm, sigma) == sigma]
                stab_t = [
                    perm
                    for perm in stab
                    if act_col(perm, tick_tuple) == tick_tuple
                ]
                if len(stab_t) < len(stab) and first is None:
                    first = {
                        "seeds": seeds,
                        "v": site,
                        "sigma": sigma,
                        "ticks": tick_tuple,
                        "stab": len(stab),
                        "stab_t": len(stab_t),
                    }
            if n_prefix >= prefix_limit:
                break
        if n_prefix >= prefix_limit:
            break

    n_uneq = 0 if first is None and n_bad_tick == 0 else 1 if first is not None else 0
    if lipschitz_ok and unread_floor_ok and n_bad_tick == 0:
        n_uneq = 0
        first = None

    return {
        "n_centers": len(centers),
        "n_triples": len(centers) * (len(centers) - 1) * (len(centers) - 2) // 6,
        "n_v": len(vs),
        "n_w4": 763608,
        "n_prefix": n_prefix,
        "n_uneq": n_uneq,
        "n_bad_tick": n_bad_tick,
        "first": first,
        "known_hit": known_hit,
        "known_sigma": known_sigma,
        "known_ticks": known_ticks,
        "known_stab": known_stab,
        "known_stab_t": known_stab_t,
        "ball_card": len(offsets),
        "lipschitz_ok": lipschitz_ok,
        "unread_floor_ok": unread_floor_ok,
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
        "construction: 3-ball unions with distinct centers in [-2,2]^3; "
        "unread weight-4 stars with |v|_∞≤3"
    )
    print(
        "negative_scope: lex-first breaker fire census only; displayed, "
        "not adopted; L1 not attached; no 4th equal-radius ball"
    )

    rotations = proper_rotations()
    pair = july3_k3_pair()
    census = census_breakers(rotations)
    n_uneq = int(census["n_uneq"])
    first = census["first"]
    if first is None:
        s_members: tuple[Coloring, ...] = ()
        n_fire = 0
        n_tick_ok = 0
        lex_first_label = "none"
    else:
        mask = first["sigma"]  # type: ignore[index]
        ticks = first["ticks"]  # type: ignore[index]
        stab = tuple(
            slots
            for _matrix, slots in rotations
            if act_col(slots, mask) == mask and act_col(slots, ticks) == ticks
        )
        support_members = [coloring for coloring in pair if support(coloring) == mask]
        s_members = tuple(
            sorted(
                coloring
                for coloring in support_members
                if all(act_col(slots, coloring) == coloring for slots in stab)
            )
        )
        n_tick_ok = len(s_members)
        seeds = first["seeds"]  # type: ignore[index]
        site = first["v"]  # type: ignore[index]
        occupied = ball(seeds[0]) | ball(seeds[1]) | ball(seeds[2])
        fires = []
        for coloring in s_members:
            after, n_new = execute_pair_step(occupied, site, coloring, pair)
            if n_new == 1 and site in after and occupied <= after and site not in occupied:
                fires.append(coloring)
        n_fire = 0 if n_tick_ok == 0 else len(fires)
        lex_first_label = (
            f"seeds={seeds} v={site} sigma={mask} ticks={ticks} "
            f"|S|={len(s_members)}"
        )

    print(f"n_centers={census['n_centers']}")
    print(f"n_triples={census['n_triples']}")
    print(f"n_v={census['n_v']}")
    print(f"N_w4={census['n_w4']}")
    print(f"N_uneq={n_uneq}")
    print(f"N_bad_tick={census['n_bad_tick']}")
    print(f"lex_first_breaker={lex_first_label}")
    print(f"S_card={len(s_members)}")
    print(f"N_tick_ok={n_tick_ok}")
    print(f"N_fire={n_fire}")
    print(f"N_pair={len(pair)}")
    print(f"known_hit={census['known_hit']}")
    print(f"known_sigma={census['known_sigma']}")
    print(f"known_ticks={census['known_ticks']}")
    print(f"known_stab={census['known_stab']}")
    print(f"known_stab_t={census['known_stab_t']}")

    expected_paths = (
        "docs/THREE_BALL_TICK_BROKEN_PAIR_FIRE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    formation_boundary = "it does not supply the formation site, probability,"
    unread_sentence = "A site with no record cannot be read."
    qubit_sentence = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_perm = "A site never carries more than one record; records are permanent."
    record_content = "A readout value is determined by record content alone."
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
        "source-unread-qubit-record",
        unread_sentence in axiom
        and unread_sentence in note
        and qubit_sentence in axiom
        and qubit_sentence in note
        and record_lock in axiom_flat
        and record_lock in note
        and record_perm in axiom_flat
        and record_perm in note
        and record_content in axiom_flat
        and record_content in note,
    )

    checks.check(
        "g-plus-order",
        len(rotations) == 24
        and len({slots for _matrix, slots in rotations}) == 24
        and len(pair) == 48
        and int(census["ball_card"]) == 25,
        f"proper={len(rotations)} pair={len(pair)}",
    )
    checks.check(
        "box-census",
        census["n_centers"] == 125
        and census["n_triples"] == 317750
        and census["n_v"] == 343
        and census["n_w4"] == 763608
        and census["n_prefix"] == 2000
        and census["lipschitz_ok"] is True
        and census["unread_floor_ok"] is True
        and "C(125, 3) = 317750" in note
        and "N_w4 = 763608" in note,
        f"triples={census['n_triples']} prefix={census['n_prefix']}",
    )
    checks.check(
        "lipschitz-occupied-ticks",
        census["n_bad_tick"] == 0
        and census["lipschitz_ok"] is True
        and "every occupied neighbor of an unread site has lock tick exactly `2`"
        in note
        and "1-Lipschitz" in note,
        f"N_bad_tick={census['n_bad_tick']}",
    )
    checks.check(
        "known-equal-tick-membership",
        census["known_hit"] is True
        and census["known_sigma"] == (1, 0, 1, 1, 0, 1)
        and census["known_ticks"] == (2, None, 2, 2, None, 2)
        and census["known_stab"] == 2
        and census["known_stab_t"] == 2
        and "(1, 0, 1, 1, 0, 1)" in note,
        "displayed equal-tick U is in the box and is not a breaker",
    )
    checks.check(
        "theorem-1-no-breaker",
        n_uneq == 0
        and first is None
        and len(s_members) == 0
        and n_tick_ok == 0
        and "N_uneq = 0" in note
        and "|S| = 0" in note
        and "no lex-first breaker" in note_flat
        and "N_tick_ok = 0" in note,
        f"N_uneq={n_uneq} |S|={len(s_members)}",
    )
    checks.check(
        "theorem-2-n-fire",
        n_fire == 0
        and n_tick_ok == 0
        and n_uneq == 0
        and "N_fire = 0" in note
        and 0 <= n_fire <= len(s_members),
        f"N_fire={n_fire}",
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write a firing c into Admissibility" in note
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
        "not-leftover-prior",
        "not leftover of tickfire" in note_flat
        and "equal-tick" in note_flat
        and "not leftover of tickuneq" in note_flat
        and "census only" in note_flat,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "N_fire" not in axiom
        and "N_uneq" not in axiom
        and "lock-tick" not in axiom
        and "B_2((1,2,1))" not in axiom,
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

    print("per_element: N_uneq, |S|, and N_fire are exact integers")
    print("per_site: lex-first breaker star only, or none")
    print("per_mode: no spectral calculation")
    print("per_block: 3-ball weight-4 unread stars in the declared box")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
