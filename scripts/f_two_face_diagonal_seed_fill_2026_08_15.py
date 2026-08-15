#!/usr/bin/env python3
"""Exact f_two occupancy ticks from one face-diagonal two-site seed.

Two-cube twelve-vertex patch. Off-patch occupancy is 0. f_two is the
predicate u>=2 on unbalanced axes, not f_L1 and not Hamming parity.
No cache write, no axiom edit, no adopted formation law.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_TWO_FACE_DIAGONAL_SEED_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

AUDIT_INPUT_PATHS = (
    "docs/F_TWO_FACE_DIAGONAL_SEED_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
PATCH = tuple(sorted((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1)))
CUBE_A = frozenset((x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1))
CUBE_B = frozenset((x, y, z) for x in (1, 2) for y in (0, 1) for z in (0, 1))
SEED = frozenset(((0, 0, 0), (1, 1, 0)))
SEED_THREE = frozenset(((1, 0, 0), (0, 1, 0), (0, 0, 1)))
EXPECTED_WAVE1 = frozenset(((1, 0, 0), (0, 1, 0)))
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def _add(site: tuple[int, int, int], step: tuple[int, int, int]) -> tuple[int, int, int]:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def occupancy(locks: frozenset[tuple[int, int, int]], site: tuple[int, int, int]) -> int:
    """On-patch lock is 1; unlocked and off-patch are both 0."""
    return 1 if site in locks else 0


def neighbor_tuple(locks: frozenset[tuple[int, int, int]], site: tuple[int, int, int]) -> tuple[int, ...]:
    entries: list[int] = []
    for step in AXES:
        entries.append(occupancy(locks, _add(site, step)))
        entries.append(occupancy(locks, _add(site, (-step[0], -step[1], -step[2]))))
    return tuple(entries)


def unbalanced_axis_count(cell: tuple[int, ...]) -> int:
    return sum(cell[2 * index] != cell[2 * index + 1] for index in range(3))


def f_two(cell: tuple[int, ...]) -> int:
    return int(unbalanced_axis_count(cell) >= 2)


def f_l1(cell: tuple[int, ...]) -> int:
    """n != 0 is equivalent to at least one unbalanced axis."""
    return int(unbalanced_axis_count(cell) >= 1)


def f_hamming(cell: tuple[int, ...]) -> int:
    return sum(cell) % 2


def ready_sites(
    locks: frozenset[tuple[int, int, int]],
    predicate,
) -> tuple[tuple[int, int, int], ...]:
    found = []
    for site in PATCH:
        if site in locks:
            continue
        if predicate(neighbor_tuple(locks, site)):
            found.append(site)
    return tuple(found)


def evolve(
    seed: frozenset[tuple[int, int, int]],
    predicate,
    max_ticks: int = 12,
) -> tuple[int, frozenset[tuple[int, int, int]], tuple[tuple[tuple[int, int, int], ...], ...]]:
    locks = frozenset(seed)
    waves: list[tuple[tuple[int, int, int], ...]] = []
    for tick in range(max_ticks + 1):
        wave = ready_sites(locks, predicate)
        waves.append(wave)
        if not wave:
            return tick, locks, tuple(waves)
        locks = locks.union(wave)
    raise RuntimeError("occupancy ticks did not reach a fixed point within the bound")


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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; seed and f_two are displayed extra structure")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact integer lock counts on the twelve-vertex two-cube")
    print("negative_scope: this displayed seed does not fill the twelve-vertex patch")

    halt_tick, final_locks, waves = evolve(SEED, f_two)
    first_wave = frozenset(waves[0])
    three_tick, three_locks, three_waves = evolve(SEED_THREE, f_two)
    l1_wave = frozenset(ready_sites(SEED, f_l1))
    empty_wave = ready_sites(frozenset(), f_two)

    print(f"computed_T={halt_tick}")
    print(f"computed_locks={len(final_locks)}")
    print(f"computed_first_wave={tuple(sorted(first_wave))}")
    print(f"computed_fill={int(len(final_locks) == 12)}")
    print(f"displayed_three_site_T={three_tick}")
    print(f"displayed_three_site_locks={len(three_locks)}")

    checks.check("patch-twelve", "two-cube union has twelve vertices", len(PATCH) == 12)
    checks.check(
        "two-cubes-share-face",
        "cubes A and B have eight vertices each and share four",
        len(CUBE_A) == 8 and len(CUBE_B) == 8 and len(CUBE_A | CUBE_B) == 12 and len(CUBE_A & CUBE_B) == 4,
    )
    checks.check(
        "seed-face-diagonal",
        "S0 is the displayed on-patch face-diagonal pair",
        SEED <= frozenset(PATCH) and (1, 1, 0) in SEED and (0, 0, 0) in SEED and len(SEED) == 2,
    )

    weight_one = (1, 0, 0, 0, 0, 0)
    face_diag_cell = neighbor_tuple(SEED, (1, 0, 0))
    checks.check(
        "f-two-is-u-ge-2",
        "f_two is u>=2, so a one-axis cell is 0 and the first-wave cell is 1",
        f_two(weight_one) == 0
        and f_two(face_diag_cell) == 1
        and unbalanced_axis_count(face_diag_cell) == 2,
    )
    checks.check(
        "f-two-not-f-l1",
        "f_L1 is n!=0 / one unbalanced axis, not f_two",
        f_l1(weight_one) == 1 and f_two(weight_one) == 0,
    )
    checks.check(
        "f-two-not-hamming",
        "Hamming |c|_1 mod 2 is a different predicate on the first-wave cell",
        f_hamming(face_diag_cell) == 0 and f_two(face_diag_cell) == 1,
    )

    checks.check("thm1-nonempty", "first wave is nonempty", len(first_wave) > 0)
    checks.check(
        "thm1-expected-sites",
        "first wave is exactly (1,0,0) and (0,1,0)",
        first_wave == EXPECTED_WAVE1,
    )
    checks.check(
        "thm1-two-occupied-axes",
        "each first-wave site sees two occupied nearest neighbors on different axes",
        all(unbalanced_axis_count(neighbor_tuple(SEED, site)) == 2 for site in EXPECTED_WAVE1),
    )

    checks.check("thm2-bounded", "halt tick T is at most 12", halt_tick <= 12)
    checks.check(
        "thm2-halt-pair",
        "fixed point is reached with computed (T, |locks|)",
        halt_tick == 1 and len(final_locks) == 4 and not waves[halt_tick],
    )
    checks.check(
        "thm2-permanence",
        "seed locks remain locked at the fixed point",
        SEED <= final_locks,
    )
    checks.check(
        "thm2-face-square",
        "final locks are the z=0 face of cube A",
        final_locks == frozenset(((0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0))),
    )

    checks.check("thm3-no-fill", "fill boolean is false: |locks_T| != 12", len(final_locks) != 12)
    checks.check(
        "thm3-three-site-displayed",
        "displayed 3-site contrast recomputes as T=2, 8 locks, no fill",
        three_tick == 2
        and len(three_locks) == 8
        and len(three_locks) != 12
        and len(three_waves[0]) > 0,
    )
    checks.check(
        "contrast-not-same-residual",
        "face-diagonal halt pair differs from the displayed 3-site pair",
        (halt_tick, len(final_locks)) != (three_tick, len(three_locks)),
    )

    checks.check(
        "mutation-l1-wave-differs",
        "f_L1 first wave from the same seed is strictly larger",
        EXPECTED_WAVE1 < l1_wave,
    )
    checks.check("empty-fixed-point", "the empty occupancy is a fixed point of f_two", empty_wave == ())

    note_reports = f"(T, |locks|)=({halt_tick}, {len(final_locks)})" in note
    checks.check(
        "note-reports-computed-pair",
        "source note reports the computed halt pair",
        note_reports and f"|locks_T|={len(final_locks)}" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n    "docs/F_TWO_FACE_DIAGONAL_SEED_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in self_source,
    )
    checks.check(
        "live-parent-quotes",
        "note quotes Lattice, Admissibility, and Record without rewriting them",
        "Physical sites are the points of the cubic lattice `Z^3`" in note
        and "No site is privileged." in note
        and "one fixed nearest-neighbor admissibility rule" in note
        and "A site with no record cannot be read." in axiom
        and "A site with no record cannot be read." in note
        and "does not supply the formation site" in axiom,
    )
    checks.check(
        "machine-status-contract",
        "note is displayed bounded-support and does not adopt f_two",
        "actual_current_surface_status: bounded-support" in note
        and "Displayed, not adopted" in note
        and "hypothetical_axiom_status: \"not proposed; no axiom or approved primitive is added\""
        in note
        and "f_two is u≥2" in note,
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and a passing N1-N8 gate are source-visible",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note,
    )
    runner_body = self_source.split("FORBIDDEN =", 1)[0]
    forbidden_hit = any(token in note for token in FORBIDDEN) or any(
        token in runner_body for token in FORBIDDEN
    )
    checks.check(
        "forbidden-substrings",
        "note and runner omit the forbidden gravity and slogan tokens",
        not forbidden_hit,
    )

    print("per_element: checked exactly — each first-wave 6-tuple has two unbalanced axes")
    print("per_site: checked exactly — twelve vertices, seed pair, and four final locks")
    print("per_mode: checked exactly — one displayed f_two seed; f_L1 and Hamming are contrasts")
    print("per_block: checked exactly — halt pair (T, |locks|) and the fill boolean")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
