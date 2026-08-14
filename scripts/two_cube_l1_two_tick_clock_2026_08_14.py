#!/usr/bin/env python3
"""Two-tick one-neighborhood clock on a declared two-cube carrier.

The paired note is
docs/TWO_CUBE_L1_TWO_TICK_CLOCK_BOUNDED_THEOREM_NOTE_2026-08-14.md.

The two-cube vertex set, the seed, and the one-neighborhood tick are
declared finite test objects. The runner grows the lock set and computes
formation count and cube-A occupancy from those sets. It does not embed
the census integers as the objects under test, write a cache, or edit
axioms.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/TWO_CUBE_L1_TWO_TICK_CLOCK_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_L1_TWO_TICK_CLOCK_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Site = tuple[int, int, int]
UNIT_STEPS: tuple[Site, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add_site(site: Site, step: Site) -> Site:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def cube_a_vertices() -> frozenset[Site]:
    return frozenset(
        (x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)
    )


def cube_b_vertices() -> frozenset[Site]:
    return frozenset(
        (x, y, z) for x in (1, 2) for y in (0, 1) for z in (0, 1)
    )


def neighbors_on(carrier: frozenset[Site], site: Site) -> frozenset[Site]:
    return frozenset(
        add_site(site, step)
        for step in UNIT_STEPS
        if add_site(site, step) in carrier
    )


def tick(carrier: frozenset[Site], locked: frozenset[Site]) -> frozenset[Site]:
    grown = set(locked)
    for site in locked:
        grown.update(neighbors_on(carrier, site))
    return frozenset(grown)


def grow(carrier: frozenset[Site], seed: frozenset[Site], ticks: int) -> frozenset[Site]:
    locked = seed
    for _ in range(ticks):
        locked = tick(carrier, locked)
    return locked


def manhattan(site: Site, origin: Site = (0, 0, 0)) -> int:
    return abs(site[0] - origin[0]) + abs(site[1] - origin[1]) + abs(site[2] - origin[2])


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f"  ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    cube_a = cube_a_vertices()
    cube_b = cube_b_vertices()
    carrier = cube_a | cube_b
    seed = frozenset({(0, 0, 0)})
    locks_1 = grow(carrier, seed, 1)
    locks_2 = grow(carrier, seed, 2)
    new_on_tick_2 = locks_2 - locks_1

    seed_size = len(seed)
    locks_1_count = len(locks_1)
    locks_2_count = len(locks_2)
    formation_1 = locks_1_count - seed_size
    formation_2 = locks_2_count - seed_size
    formation_tick_2 = len(new_on_tick_2)
    rho_a_1 = len(locks_1 & cube_a)
    rho_a_2 = len(locks_2 & cube_a)
    b_only_2 = locks_2 - cube_a

    print("Two-cube L1 two-tick clock")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "scope: declared two-cube carrier and supplied one-neighborhood "
        "tick; no time metric and no rate object"
    )
    print(
        f"census: seed={seed_size} "
        f"t1_locks={locks_1_count} t1_F={formation_1} t1_rhoA={rho_a_1} "
        f"t2_locks={locks_2_count} t2_F={formation_2} t2_rhoA={rho_a_2} "
        f"F_tick2={formation_tick_2}"
    )
    print(f"locks_1={tuple(sorted(locks_1))}")
    print(f"locks_2={tuple(sorted(locks_2))}")
    print(f"b_only_2={tuple(sorted(b_only_2))}")

    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "audit-input-paths-unique-normalized",
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)
    checks.check("cache-write-disabled", "cache_write: false" in note)

    lock_sentence = (
        "When present, a record locks exactly one admissible local possibility."
    )
    checks.check("source-occurrence-sentence-current", "Records form." in axiom)
    checks.check("source-lock-sentence-current", lock_sentence in normalized_axiom)
    checks.check(
        "source-permanence-and-unread-absence-current",
        "A site never carries more than one record; records are permanent."
        in normalized_axiom
        and "A site with no record cannot be read." in normalized_axiom,
    )
    checks.check(
        "source-no-time-metric-or-production-process",
        "time metric" in normalized_axiom
        and "record-production process" in normalized_axiom,
    )

    checks.check("seed-size-one", seed_size == 1 and seed <= cube_a)
    checks.check(
        "two-cube-carrier-census",
        len(cube_a) == 8
        and len(cube_b) == 8
        and len(carrier) == 12
        and cube_a & cube_b
        == frozenset((1, y, z) for y in (0, 1) for z in (0, 1)),
    )
    checks.check(
        "tick1-neighborhood-of-seed",
        locks_1 == seed | neighbors_on(carrier, (0, 0, 0)),
    )
    checks.check(
        "tick1-census",
        locks_1_count == 4 and formation_1 == 3 and rho_a_1 == 4,
        f"|locks|={locks_1_count} F={formation_1} rho(A)={rho_a_1}",
    )
    checks.check(
        "tick2-census",
        locks_2_count == 8 and formation_2 == 7 and rho_a_2 == 7,
        f"|locks|={locks_2_count} F={formation_2} rho(A)={rho_a_2}",
    )
    checks.check(
        "tick2-new-locks-are-distance-two",
        new_on_tick_2
        == frozenset({(2, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)})
        and all(manhattan(site) == 2 for site in new_on_tick_2),
    )
    checks.check(
        "corner-of-a-is-not-yet-locked",
        (1, 1, 1) in cube_a
        and (1, 1, 1) not in locks_2
        and manhattan((1, 1, 1)) == 3,
    )

    checks.check(
        "theorem1-clock-is-lock-count-minus-seed",
        formation_1 == locks_1_count - seed_size
        and formation_2 == locks_2_count - seed_size
        and formation_1 == 3
        and formation_2 == 7,
    )
    checks.check(
        "theorem2-tick1-clock-is-not-rho-a",
        formation_1 != rho_a_1 and formation_1 == 3 and rho_a_1 == 4,
    )
    checks.check(
        "theorem2-tick2-meeting-is-coincidence",
        formation_2 == rho_a_2 == 7
        and b_only_2 == frozenset({(2, 0, 0)})
        and (0, 0, 0) in locks_2 & cube_a
        and (2, 0, 0) in cube_b - cube_a
        and rho_a_2 == len(locks_2) - len(b_only_2)
        and formation_2 == rho_a_2 - seed_size + len(b_only_2),
    )
    checks.check(
        "theorem3-two-tick-additivity",
        formation_2 == formation_1 + formation_tick_2
        and formation_tick_2 == 4
        and formation_2 == 7,
        f"{formation_2}={formation_1}+{formation_tick_2}",
    )

    seed_inclusive_clock_1 = locks_1_count
    omitted_b_only = locks_2 - b_only_2
    checks.check(
        "mutation-seed-inclusive-clock-collides-with-rho-a",
        seed_inclusive_clock_1 == rho_a_1 == 4
        and seed_inclusive_clock_1 != formation_1,
    )
    checks.check(
        "mutation-dropping-b-only-breaks-tick2-meeting",
        len(omitted_b_only) - seed_size == 6
        and len(omitted_b_only & cube_a) == 7
        and (len(omitted_b_only) - seed_size) != len(omitted_b_only & cube_a),
    )

    machine_markers = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "claim_type_reason:",
        "trace_class: negative_route_pruning",
        "target_claim_id: two_cube_l1_two_tick_clock",
        "target_blocker_text:",
        "source_of_blocker_text: handoff",
        "reachability_to_target: prunes",
        "artifact_role: theorem",
        "next_trace_action:",
        "conditional_surface_status:",
        "hypothetical_axiom_status: no edit",
        "admitted_observation_status: null",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    checks.check(
        "note-machine-status-complete",
        all(marker in note for marker in machine_markers),
    )
    checks.check(
        "note-one-hop-dependency-current",
        "upstream_dependencies:\n  - minimal_axioms" in note
        and "MINIMAL_AXIOMS_2026-06-29.md" in note,
    )
    checks.check(
        "note-states-three-theorems",
        "F_t = |locks_t| − 1" in note
        and "3≠4" in note
        and "7=7" in note
        and "7=3+4" in note
        and "(2,0,0)" in note,
    )
    checks.check(
        "note-coincidence-not-identity",
        "coincidence, not identity" in normalized_note
        and "missed the B-only lock" in normalized_note
        and "already counted the seed" in normalized_note,
    )
    checks.check(
        "note-tick-is-supplied-not-time-metric",
        "supplied one-neighborhood tick" in normalized_note
        and "does not supply a time metric" in normalized_note,
    )

    n5_lines = (
        "per-element: executed — every lock after each tick is enumerated",
        "per-site: executed — the twelve two-cube vertices are the carrier",
        "per-mode: not applicable — no modal or spectral decomposition is used",
        "per-block: executed — only the declared two-tick integrated law is checked",
        "lattice-wide: not executed — no full Z^3 history or rate is claimed",
    )
    checks.check(
        "note-n5-five-line-certificate",
        all(line in note for line in n5_lines),
    )
    print("N5_CERTIFICATE:")
    for line in n5_lines:
        print(line)

    checks.check(
        "note-no-go-n1-through-n8",
        all(f"### N{index}" in note for index in range(1, 9)),
    )
    forbidden = (
        "G" + "_N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice" + "-named",
        "not a " + "TOE",
    )
    runner_text = Path(__file__).read_text(encoding="utf-8")
    checks.check(
        "note-and-runner-avoid-forbidden-phrases",
        all(phrase not in note for phrase in forbidden)
        and all(phrase not in runner_text for phrase in forbidden),
    )
    checks.check(
        "note-explicit-nonclaims",
        "No axiom, primitive, registry, or audit verdict is edited." in note
        and "The tick index is a discrete step of a supplied law, not a derived clock rate."
        in normalized_note,
    )
    return 0 if checks.finish() == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
