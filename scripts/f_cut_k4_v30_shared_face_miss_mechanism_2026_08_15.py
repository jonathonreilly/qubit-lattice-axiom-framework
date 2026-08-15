#!/usr/bin/env python3
"""First refused neighborhood on the four shared-face 1-site miss seeds.

Independent occupancy-to-lock runs start from each of the four x=1
shared-face one-site seeds on the twelve-vertex two-cube with off-patch
occupancy 0.  The vertex3=0 k=4 map f00=(1,1,1,0,0) misses each of those
seeds; the F_cut map f11 with remaining bits (1,1,1,1,1) fills each of
them.  On seed (1,0,0), the first (tick, site, axis-type) with f00(nbhd)=0
and f11(nbhd)=1 is displayed, not adopted.  The other three shared-face
seeds share that first axis type.  vertex3 is not written into
Admissibility.  f_L1 is the unbalanced-axis predicate (some n_mu != 0),
never Hamming |c|_1 mod 2.  New object: not leftover of #6448 (that only
listed the missed sites).
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_K4_V30_SHARED_FACE_MISS_MECHANISM_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_K4_V30_SHARED_FACE_MISS_MECHANISM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]

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
ONE_SITE_SEEDS: tuple[Site, ...] = TWO_CUBE
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
F00: tuple[int, ...] = (1, 1, 1, 0, 0)
F11: tuple[int, ...] = (1, 1, 1, 1, 1)
SHARED_FACE: tuple[Site, ...] = (
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1),
)
LEX_SEED: Site = (1, 0, 0)


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


def f00(config: Config) -> int:
    """F_cut remaining bits (1, 1, 1, 0, 0).  Displayed vertex3=0 k=4 map."""
    return remaining_value(config, F00)


def f11(config: Config) -> int:
    """F_cut remaining bits (1, 1, 1, 1, 1).  Displayed, not adopted."""
    return remaining_value(config, F11)


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


def run_from_seed(predicate, seed: Site, halt_bound: int = 13) -> dict:
    locked = {seed}
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


def fills_from_seed(predicate, seed: Site) -> bool:
    return bool(run_from_seed(predicate, seed)["fill"])


def miss_tuple(predicate) -> tuple[Site, ...]:
    return tuple(site for site in ONE_SITE_SEEDS if not fills_from_seed(predicate, site))


def coverage(predicate) -> int:
    return sum(1 for site in ONE_SITE_SEEDS if fills_from_seed(predicate, site))


def refusal_events(locked: set[Site]) -> list[dict]:
    rows: list[dict] = []
    for site in TWO_CUBE:
        if site in locked:
            continue
        config = neighborhood(site, locked)
        value_00 = f00(config)
        value_11 = f11(config)
        if value_00 == 0 and value_11 == 1:
            kind = axis_type(config)
            rows.append(
                {
                    "site": site,
                    "config": config,
                    "axis_type": kind,
                    "axis_name": AXIS_TYPE_NAME[kind],
                    "f00": value_00,
                    "f11": value_11,
                }
            )
    return rows


def first_refusal(seed: Site, predicate, halt_bound: int = 13) -> dict | None:
    """Independent run: first (tick, site, axis-type) with f00=0 and f11=1."""
    locked = {seed}
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
    print("construction: independent occupancy-to-lock runs from each shared-face 1-site miss")
    print("negative_scope: vertex3 is displayed, not adopted or written into Admissibility")

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    orbit_sizes = {orbit_type: len(orbits[orbit_type]) for orbit_type in orbit_types}
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    f00_bits = bits_from_predicate(f00, orbit_types, orbits)
    f11_bits = bits_from_predicate(f11, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)
    f00_remaining = remaining_bits_from_full(f00_bits, orbit_types)
    f11_remaining = remaining_bits_from_full(f11_bits, orbit_types)

    miss00 = miss_tuple(f00)
    miss11 = miss_tuple(f11)
    cov00 = coverage(f00)
    cov11 = coverage(f11)

    independent = []
    for seed in SHARED_FACE:
        run_00 = run_from_seed(f00, seed)
        run_11 = run_from_seed(f11, seed)
        first_on_11 = first_refusal(seed, f11)
        first_on_00 = first_refusal(seed, f00)
        independent.append(
            {
                "seed": seed,
                "f00": run_00,
                "f11": run_11,
                "first_f11": first_on_11,
                "first_f00": first_on_00,
            }
        )
    first_lex = independent[0]["first_f11"]

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print("orbit_types_and_sizes=" + ",".join(f"{t}:{orbit_sizes[t]}" for t in orbit_types))
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"n_one_site_seeds={len(ONE_SITE_SEEDS)}")
    print(f"f00={F00}")
    print(f"f11={F11}")
    print(f"cov1_f00={cov00}")
    print(f"cov1_f11={cov11}")
    print(f"miss_f00={miss00}")
    print(f"miss_f11={miss11}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"f00_remaining={f00_remaining}")
    print(f"f11_remaining={f11_remaining}")
    print(f"f_hamming_bits={ham_bits}")
    for row in independent:
        first = row["first_f11"]
        seed = row["seed"]
        print(
            f"  seed={seed} "
            f"hist_f00={row['f00']['history']} fill_f00={row['f00']['fill']} "
            f"hist_f11={row['f11']['history']} fill_f11={row['f11']['fill']} "
            f"first=t={first['tick']} x={first['site']} type={first['axis_name']}{first['axis_type']}"
        )
    print(
        "lex_first_refusal="
        f"t={first_lex['tick']} x={first_lex['site']} "
        f"type={first_lex['axis_name']}{first_lex['axis_type']} "
        f"cfg={first_lex['config']}"
    )
    other_types = [row["first_f11"]["axis_name"] for row in independent[1:]]
    print(f"other_three_first_axis_types={other_types}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_K4_V30_SHARED_FACE_MISS_MECHANISM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_K4_V30_SHARED_FACE_MISS_MECHANISM_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        "thm1-f-L1-not-hamming",
        "f_L1 is unbalanced-axis and is not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and l1_remaining == L1_REMAINING
        and l1_remaining not in (F00, F11)
        and all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-two-cube-and-twelve-seeds",
        "the two-cube has twelve vertices in lex order and twelve one-site seeds",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and TWO_CUBE == tuple(sorted(TWO_CUBE))
        and ONE_SITE_SEEDS == TWO_CUBE
        and set(SHARED_FACE) <= set(TWO_CUBE)
        and len(SHARED_FACE) == 4
        and SHARED_FACE == tuple(sorted(SHARED_FACE)),
    )
    checks.check(
        "thm1-maps-in-f-cut",
        "f00 and f11 are F_cut maps; f00 has vertex3=0 and f11 has remaining bits (1,1,1,1,1)",
        in_f_cut(f00_bits, orbit_types, empty_type, full_type)
        and in_f_cut(f11_bits, orbit_types, empty_type, full_type)
        and f00_remaining == F00
        and f11_remaining == F11
        and F00[3] == 0
        and F11[3] == 1
        and F00 == (1, 1, 1, 0, 0)
        and F11 == (1, 1, 1, 1, 1),
    )
    checks.check(
        "thm1-f00-miss-f11-fill",
        "f11 fills from (1,0,0); f00 does not, and the four shared-face seeds are the f00 misses",
        not independent[0]["f00"]["fill"]
        and independent[0]["f11"]["fill"]
        and independent[0]["seed"] == LEX_SEED
        and miss00 == SHARED_FACE
        and cov00 == 8
        and all(not row["f00"]["fill"] for row in independent)
        and all(row["f11"]["fill"] for row in independent)
        and all(row["f00"]["history"] == (1, 5, 10) for row in independent)
        and all(row["f11"]["history"] == (1, 5, 10, 12) for row in independent)
        and "f11 fills from (1,0,0); f00 does not" in note_flat,
    )
    checks.check(
        "thm2-first-refusal",
        "first refusal on seed (1,0,0) is t=3, site (0,1,1), axis type vertex3",
        first_lex is not None
        and first_lex["tick"] == 3
        and first_lex["site"] == (0, 1, 1)
        and first_lex["axis_type"] == (3, 0, 0)
        and first_lex["axis_name"] == "vertex3"
        and first_lex["config"] == (1, 0, 0, 1, 0, 1)
        and first_lex["n_events"] == 2
        and independent[0]["first_f00"]["tick"] == 3
        and independent[0]["first_f00"]["site"] == (0, 1, 1)
        and independent[0]["first_f00"]["axis_name"] == "vertex3"
        and independent[0]["first_f00"]["config"] == (1, 0, 0, 1, 0, 1),
    )
    checks.check(
        "thm3-other-three-same-axis-type",
        "the other three shared-face seeds have the same first axis type vertex3",
        len(independent) == 4
        and all(row["first_f11"]["tick"] == 3 for row in independent)
        and all(row["first_f11"]["axis_name"] == "vertex3" for row in independent)
        and all(row["first_f11"]["axis_type"] == (3, 0, 0) for row in independent)
        and all(row["first_f00"]["axis_name"] == "vertex3" for row in independent)
        and [row["first_f11"]["site"] for row in independent]
        == [(0, 1, 1), (0, 1, 0), (0, 0, 1), (0, 0, 0)],
    )
    checks.check(
        "thm3-display-not-adopt-vertex3",
        "vertex3 is displayed and is not adopted or written into Admissibility",
        first_lex["axis_name"] == "vertex3"
        and "Do not adopt vertex3" in note
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
        "no-axiom-edit",
        "the theorem proposes no axiom change and does not adopt vertex3",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write it into Admissibility" in note
        and "Do not adopt vertex3" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-6448",
        "the residual is the first refused neighborhood, not leftover of #6448",
        "Not leftover of #6448" in note
        and "that only listed sites" in note
        and "New mechanism" in note,
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the first refused neighborhood on seed (1,0,0)",
        "On the two-cube with off-patch o=0 and 1-site seed (1,0,0), the first neighborhood at which F_cut (1,1,1,0,0) refuses and (1,1,1,1,1) fires is reported by tick, site, and axis type."
        in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        "does not supply the formation site, probability, or rate" in axiom_flat
        and "does not supply the formation site, probability, or rate" in note_flat,
    )
    checks.check(
        "note-reports-first-refusal",
        "the note reports f00 miss, f11 fill, and the first (t, x, axis type)",
        "t = 3" in note
        and "(0, 1, 1)" in note
        and "`vertex3`" in note
        and "(3, 0, 0)" in note
        and "(1, 0, 0, 1, 0, 1)" in note
        and "same first axis type" in note
        and "3-axis contrast" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — f00 and f11 are run independently from each shared-face 1-site seed")
    print("per_block: checked exactly — the first refused neighborhood is named by tick, site, and axis type")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
