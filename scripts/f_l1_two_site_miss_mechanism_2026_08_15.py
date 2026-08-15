#!/usr/bin/env python3
"""First refused neighborhood on the four 2-site seeds f_L1 does not fill.

Independent occupancy-to-lock runs start from each 2-site miss seed on the
twelve-vertex two-cube with off-patch occupancy 0.  The four misses of
f_L1 are recomputed; the F_cut map f1 with remaining bits (1,1,1,1,1)
fills each of them.  On the lex-first miss, the first (tick, site,
axis-type) with f_L1(nbhd)=0 and f1(nbhd)=1 is displayed, not adopted.
The other three misses share that first axis type.  opp2 is not written
into Admissibility.  f_L1 is the unbalanced-axis predicate (some n_mu
!= 0), never Hamming |c|_1 mod 2.  New object: not leftover of #6420
(that was f_min versus f_L1 on a seed f_L1 fills).
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_L1_TWO_SITE_MISS_MECHANISM_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_L1_TWO_SITE_MISS_MECHANISM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]
Seed = tuple[Site, Site]

DIRECTIONS: tuple[Direction, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
EMPTY: Config = (0, 0, 0, 0, 0, 0)
FULL: Config = (1, 1, 1, 1, 1, 1)
TWO_CUBE: tuple[Site, ...] = tuple(
    (x, y, z) for x in range(3) for y in range(2) for z in range(2)
)
TWO_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(pair) for pair in combinations(TWO_CUBE, 2)
)
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
AXIS_TYPE_NAME: dict[OrbitType, str] = {
    (0, 0, 3): "empty",
    (0, 3, 0): "full",
    (1, 0, 2): "wt1",
    (1, 2, 0): "wt1_comp",
    (0, 1, 2): "opp2",
    (0, 2, 1): "opp2_comp",
    (2, 0, 1): "adj2",
    (2, 1, 0): "adj2_comp",
    (3, 0, 0): "vertex3",
    (1, 1, 1): "mixed3",
}
L1_REMAINING: tuple[int, ...] = (1, 0, 1, 1, 1)
F1_REMAINING: tuple[int, ...] = (1, 1, 1, 1, 1)
F1_LABEL = "f1"


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


ROTATIONS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_vector(rotation: Rotation, vector: Direction) -> Direction:
    permutation, signs = rotation
    result = [0, 0, 0]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return (result[0], result[1], result[2])


def rotate_config(config: Config, rotation: Rotation) -> Config:
    occupancy = {direction: config[index] for index, direction in enumerate(DIRECTIONS)}
    forward = {direction: rotate_vector(rotation, direction) for direction in DIRECTIONS}
    inverse = {image: source for source, image in forward.items()}
    return tuple(occupancy[inverse[direction]] for direction in DIRECTIONS)  # type: ignore[return-value]


def axis_type(config: Config) -> OrbitType:
    n_unbalanced = 0
    n_both = 0
    n_empty = 0
    for axis in range(3):
        plus = config[2 * axis]
        minus = config[2 * axis + 1]
        if plus != minus:
            n_unbalanced += 1
        elif plus == 1:
            n_both += 1
        else:
            n_empty += 1
    return (n_unbalanced, n_both, n_empty)


def complement_type(orbit_type: OrbitType) -> OrbitType:
    unbalanced, both, empty = orbit_type
    return (unbalanced, empty, both)


def f_L1(config: Config) -> int:
    """1 iff some axis is unbalanced: n_mu != 0.  Not Hamming parity."""
    return int(any(config[2 * axis] != config[2 * axis + 1] for axis in range(3)))


def f_hamming(config: Config) -> int:
    return sum(config) % 2


def remaining_value(config: Config, remaining: tuple[int, ...]) -> int:
    kind = axis_type(config)
    if kind in (axis_type(EMPTY), axis_type(FULL)):
        return 0
    assignment = dict(zip(REMAINING_ORDER, remaining, strict=True))
    if kind in assignment:
        return assignment[kind]
    return assignment[complement_type(kind)]


def f1(config: Config) -> int:
    """F_cut remaining bits (1, 1, 1, 1, 1).  Displayed cov=66 map.  Not adopted."""
    return remaining_value(config, F1_REMAINING)


def build_orbits() -> dict[OrbitType, frozenset[Config]]:
    orbits: dict[OrbitType, frozenset[Config]] = {}
    seen: set[Config] = set()
    for raw in product((0, 1), repeat=6):
        config: Config = (raw[0], raw[1], raw[2], raw[3], raw[4], raw[5])
        if config in seen:
            continue
        orbit: set[Config] = set()
        stack = [config]
        while stack:
            current = stack.pop()
            if current in orbit:
                continue
            orbit.add(current)
            for rotation in ROTATIONS:
                stack.append(rotate_config(current, rotation))
        orbit_type = axis_type(config)
        if any(axis_type(member) != orbit_type for member in orbit):
            raise RuntimeError("orbit mixed axis types")
        orbits[orbit_type] = frozenset(orbit)
        seen.update(orbit)
    return orbits


def neighborhood(site: Site, locked: set[Site]) -> Config:
    values = []
    for direction in DIRECTIONS:
        neighbor = (
            site[0] + direction[0],
            site[1] + direction[1],
            site[2] + direction[2],
        )
        values.append(1 if neighbor in locked else 0)
    return (values[0], values[1], values[2], values[3], values[4], values[5])


def evolve(locked: set[Site], predicate) -> set[Site]:
    nxt = set(locked)
    for site in TWO_CUBE:
        if site in locked:
            continue
        if predicate(neighborhood(site, locked)):
            nxt.add(site)
    return nxt


def run_from_seed(predicate, seed: frozenset[Site], halt_bound: int = 13) -> dict:
    locked = set(seed)
    history = [len(locked)]
    for _tick in range(halt_bound):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            break
        locked = nxt
        history.append(len(locked))
    return {
        "fill": len(locked) == 12,
        "history": tuple(history),
        "locks": frozenset(locked),
        "halt_tick": len(history) - 1,
    }


def fills_from_seed(predicate, seed: frozenset[Site]) -> bool:
    return bool(run_from_seed(predicate, seed)["fill"])


def coverage(predicate) -> int:
    return sum(1 for seed in TWO_SITE_SEEDS if fills_from_seed(predicate, seed))


def seed_key(seed: frozenset[Site]) -> Seed:
    ordered = tuple(sorted(seed))
    return (ordered[0], ordered[1])


def seed_display(seed: frozenset[Site] | Seed) -> str:
    a, b = seed_key(frozenset(seed))
    return f"{{({a[0]},{a[1]},{a[2]}),({b[0]},{b[1]},{b[2]})}}"


def refusal_events(locked: set[Site]) -> list[dict]:
    rows: list[dict] = []
    for site in TWO_CUBE:
        if site in locked:
            continue
        config = neighborhood(site, locked)
        value_l1 = f_L1(config)
        value_f1 = f1(config)
        if value_l1 == 0 and value_f1 == 1:
            kind = axis_type(config)
            rows.append(
                {
                    "site": site,
                    "config": config,
                    "axis_type": kind,
                    "axis_name": AXIS_TYPE_NAME[kind],
                    "f_L1": value_l1,
                    "f1": value_f1,
                }
            )
    return rows


def first_refusal(seed: frozenset[Site], predicate, halt_bound: int = 13) -> dict | None:
    """Independent run: first (tick, site, axis-type) with f_L1=0 and f1=1."""
    locked = set(seed)
    for tick in range(1, halt_bound + 1):
        events = refusal_events(locked)
        if events:
            first = events[0]
            return {
                "tick": tick,
                "site": first["site"],
                "config": first["config"],
                "axis_type": first["axis_type"],
                "axis_name": first["axis_name"],
                "n_events": len(events),
                "events": tuple(events),
            }
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return None
        locked = nxt
    return None


def bits_from_predicate(
    predicate, orbit_types: tuple[OrbitType, ...], orbits: dict[OrbitType, frozenset[Config]]
) -> tuple[int, ...]:
    bits = []
    for orbit_type in orbit_types:
        sample = next(iter(orbits[orbit_type]))
        value = int(predicate(sample))
        if any(int(predicate(member)) != value for member in orbits[orbit_type]):
            raise RuntimeError("predicate is not cube-covariant")
        bits.append(value)
    return tuple(bits)


def remaining_bits_from_assignment(assignment: dict[OrbitType, int]) -> tuple[int, ...]:
    return tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)


def remaining_bits_from_full(
    bits: tuple[int, ...], orbit_types: tuple[OrbitType, ...]
) -> tuple[int, ...]:
    assignment = dict(zip(orbit_types, bits, strict=True))
    return remaining_bits_from_assignment(assignment)


def in_f_cut(
    bits: tuple[int, ...],
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> bool:
    assignment = dict(zip(orbit_types, bits, strict=True))
    if assignment[empty_type] != 0 or assignment[full_type] != 0:
        return False
    return all(
        assignment[orbit_type] == assignment[complement_type(orbit_type)]
        for orbit_type in orbit_types
    )


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("construction: independent occupancy-to-lock runs from each f_L1 2-site miss")
    print("negative_scope: opp2 is displayed, not adopted or written into Admissibility")

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    orbit_sizes = {orbit_type: len(orbits[orbit_type]) for orbit_type in orbit_types}
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    f1_bits = bits_from_predicate(f1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)
    f1_remaining = remaining_bits_from_full(f1_bits, orbit_types)

    miss_seeds = [seed for seed in TWO_SITE_SEEDS if not fills_from_seed(f_L1, seed)]
    miss_seeds.sort(key=seed_key)
    lex_first = miss_seeds[0]
    independent = []
    for seed in miss_seeds:
        run_l1 = run_from_seed(f_L1, seed)
        run_f1 = run_from_seed(f1, seed)
        first_on_f1 = first_refusal(seed, f1)
        first_on_l1 = first_refusal(seed, f_L1)
        independent.append(
            {
                "seed": seed_key(seed),
                "display": seed_display(seed),
                "l1": run_l1,
                "f1": run_f1,
                "first_f1": first_on_f1,
                "first_l1": first_on_l1,
            }
        )
    first_lex = independent[0]["first_f1"]
    cov_l1 = 66 - len(miss_seeds)
    cov_f1 = coverage(f1)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print("orbit_types_and_sizes=" + ",".join(f"{t}:{orbit_sizes[t]}" for t in orbit_types))
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"n_two_site_seeds={len(TWO_SITE_SEEDS)}")
    print(f"cov_f_L1={cov_l1}")
    print(f"cov_f1={cov_f1}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"f1_remaining={f1_remaining}")
    print(f"n_l1_miss={len(miss_seeds)}")
    print("miss_seeds_lex=" + ", ".join(row["display"] for row in independent))
    for row in independent:
        first = row["first_f1"]
        print(
            f"  {row['display']} "
            f"hist_L1={row['l1']['history']} fill_L1={row['l1']['fill']} "
            f"hist_f1={row['f1']['history']} fill_f1={row['f1']['fill']} "
            f"first=t={first['tick']} x={first['site']} type={first['axis_name']}{first['axis_type']}"
        )
    print(
        "lex_first_refusal="
        f"t={first_lex['tick']} x={first_lex['site']} "
        f"type={first_lex['axis_name']}{first_lex['axis_type']} "
        f"cfg={first_lex['config']}"
    )
    other_types = [row["first_f1"]["axis_name"] for row in independent[1:]]
    print(f"other_three_first_axis_types={other_types}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_L1_TWO_SITE_MISS_MECHANISM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_L1_TWO_SITE_MISS_MECHANISM_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )
    checks.check(
        "thm1-twenty-four-rotations",
        "exactly 24 proper cube rotations",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24,
    )
    checks.check(
        "thm1-ten-orbits",
        "exactly 10 orbits partition the 64 cells of {0,1}^6",
        len(orbit_types) == 10 and sum(orbit_sizes.values()) == 64,
    )
    expected_sizes = {
        (0, 0, 3): 1,
        (0, 1, 2): 3,
        (0, 2, 1): 3,
        (0, 3, 0): 1,
        (1, 0, 2): 6,
        (1, 1, 1): 12,
        (1, 2, 0): 6,
        (2, 0, 1): 12,
        (2, 1, 0): 12,
        (3, 0, 0): 8,
    }
    checks.check(
        "thm1-orbit-sizes",
        "orbit sizes are the axis-type class sizes",
        orbit_sizes == expected_sizes,
    )
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis has c_+ != c_-",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and l1_remaining == L1_REMAINING
        and in_f_cut(l1_bits, orbit_types, empty_type, full_type),
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-two-cube-and-sixty-six-seeds",
        "the two-cube has twelve vertices and C(12,2)=66 two-site seeds",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and len(TWO_SITE_SEEDS) == 66
        and len(set(TWO_SITE_SEEDS)) == 66
        and all(seed <= set(TWO_CUBE) and len(seed) == 2 for seed in TWO_SITE_SEEDS),
    )
    checks.check(
        "thm1-four-misses-and-f1-fills",
        "exactly four 2-site seeds miss under f_L1, and f1 fills each independently",
        len(miss_seeds) == 4
        and cov_l1 == 62
        and cov_f1 == 66
        and f1_remaining == F1_REMAINING
        and in_f_cut(f1_bits, orbit_types, empty_type, full_type)
        and all(not row["l1"]["fill"] for row in independent)
        and all(row["f1"]["fill"] for row in independent)
        and all(row["l1"]["history"] == (2, 6, 8) for row in independent)
        and all(row["f1"]["history"] == (2, 7, 11, 12) for row in independent)
        and [row["display"] for row in independent]
        == [
            "{(0,0,0),(2,0,0)}",
            "{(0,0,1),(2,0,1)}",
            "{(0,1,0),(2,1,0)}",
            "{(0,1,1),(2,1,1)}",
        ],
    )
    checks.check(
        "thm2-lex-first-refusal",
        "lex-first miss first refusal is t=1, site (1,0,0), axis type opp2",
        first_lex is not None
        and seed_display(lex_first) == "{(0,0,0),(2,0,0)}"
        and first_lex["tick"] == 1
        and first_lex["site"] == (1, 0, 0)
        and first_lex["axis_type"] == (0, 1, 2)
        and first_lex["axis_name"] == "opp2"
        and first_lex["config"] == (1, 1, 0, 0, 0, 0)
        and first_lex["n_events"] == 1
        and independent[0]["first_l1"]["tick"] == 1
        and independent[0]["first_l1"]["site"] == (1, 0, 0)
        and independent[0]["first_l1"]["axis_name"] == "opp2",
    )
    checks.check(
        "thm3-other-three-same-axis-type",
        "the other three miss seeds have the same first axis type opp2",
        len(independent) == 4
        and all(row["first_f1"]["tick"] == 1 for row in independent)
        and all(row["first_f1"]["axis_name"] == "opp2" for row in independent)
        and all(row["first_f1"]["axis_type"] == (0, 1, 2) for row in independent)
        and [row["first_f1"]["site"] for row in independent]
        == [(1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
        and all(row["first_l1"]["axis_name"] == "opp2" for row in independent),
    )
    checks.check(
        "thm3-display-not-adopt-opp2",
        "opp2 is displayed and is not adopted or written into Admissibility",
        first_lex["axis_name"] == "opp2"
        and "Do not adopt opp2" in note
        and "Do not write it into Admissibility" in note
        and "Displayed, not adopted" in note,
    )
    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = (
        "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_absence = "A site with no record cannot be read."
    checks.check(
        "lattice-and-admissibility-parents",
        "the live axiom memo supplies Z^3, proper cubic rotations, and a covariant nearest-neighbor rule",
        lattice_sentence in axiom
        and "proper cubic rotations about each site." in axiom
        and admissibility_sentence in axiom
        and record_lock in axiom
        and record_absence in axiom
        and lattice_sentence in note
        and record_absence in note,
    )
    checks.check(
        "note-contract",
        "bounded theorem, displayed-not-adopted first refusal, and machine status",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "Displayed, not adopted" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note,
    )
    checks.check(
        "claim-type-and-gate",
        "N1-N8 and a passing no-go disposition are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6
        and ("import " + "qcd") not in self_source.lower(),
    )
    forbidden = ("G_" + "N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
    checks.check(
        "forbidden-phrases-absent",
        "the note and runner omit the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in note_flat
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "note-reports-first-refusal",
        "the note reports the four misses, f1 fill, and the lex-first (t, x, axis type)",
        all(
            display in note.replace(" ", "")
            for display in (
                "{(0,0,0),(2,0,0)}",
                "{(0,0,1),(2,0,1)}",
                "{(0,1,0),(2,1,0)}",
                "{(0,1,1),(2,1,1)}",
            )
        )
        and "(1, 1, 1, 1, 1)" in note
        and "t = 1" in note
        and "(1, 0, 0)" in note
        and "`opp2`" in note
        and "(0, 1, 2)" in note
        and "same first axis type" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write it into Admissibility" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-6420",
        "the residual is the first refused neighborhood, not leftover of #6420",
        "Not leftover of #6420" in note
        and "f_min versus f_L1 on a seed f_L1 fills" in note
        and "New object" in note,
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the first refused neighborhood on the lex-first miss",
        "On the two-cube with off-patch o=0, the first neighborhood at which f_L1 refuses and the cov=66 map (1,1,1,1,1) fires, on the lex-first 2-site seed f_L1 does not fill, is reported by tick, site, and axis type."
        in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        "does not supply the formation site, probability, or rate" in axiom_flat
        and "does not supply the formation site, probability, or rate" in note_flat,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — f_L1 and f1 are run independently from each of the four miss seeds")
    print("per_block: checked exactly — the first refused neighborhood is named by tick, site, and axis type")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
