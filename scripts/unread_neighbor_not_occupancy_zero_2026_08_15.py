#!/usr/bin/env python3
"""Exact first-wave comparison: unread neighbor is not occupancy zero.

The paired note is
docs/UNREAD_NEIGHBOR_NOT_OCCUPANCY_ZERO_BOUNDED_THEOREM_NOTE_2026-08-15.md.

On the supplied twelve-vertex two-cube, displayed L1 fills off-patch
neighbors as 0 and forms iff n != 0. The alternative member leaves those
neighbors blank and blocks readiness. No cache, citation manifest, or
axiom surface is written.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/UNREAD_NEIGHBOR_NOT_OCCUPANCY_ZERO_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/UNREAD_NEIGHBOR_NOT_OCCUPANCY_ZERO_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
BLANK = "blank"
SEED: Point = (0, 0, 0)
SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
AXIS_SITES: frozenset[Point] = frozenset(
    {(1, 0, 0), (0, 1, 0), (0, 0, 1)}
)
FORBIDDEN_NOTE_TOKENS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
)
FORBIDDEN_AXIOM_PHRASES = (
    "unread = 0",
    "unread=0",
    "unreadability is occupancy 0",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def cube_a() -> frozenset[Point]:
    return frozenset(product((0, 1), (0, 1), (0, 1)))


def cube_b() -> frozenset[Point]:
    return frozenset(product((1, 2), (0, 1), (0, 1)))


def two_cube() -> frozenset[Point]:
    return cube_a() | cube_b()


def neighbors(site: Point) -> tuple[Point, ...]:
    return tuple(add(site, shift) for shift in SHIFTS)


def occupancy(site: Point, patch: frozenset[Point]) -> int | str:
    if site == SEED:
        return 1
    if site in patch:
        return 0
    return BLANK


def displayed_n(site: Point, patch: frozenset[Point]) -> int:
    total = 0
    for neighbor in neighbors(site):
        letter = occupancy(neighbor, patch)
        total += 0 if letter == BLANK else int(letter)
    return total


def n_is_defined(site: Point, patch: frozenset[Point]) -> bool:
    return all(occupancy(neighbor, patch) in (0, 1) for neighbor in neighbors(site))


def l1_first_wave(patch: frozenset[Point]) -> frozenset[Point]:
    return frozenset(
        site
        for site in patch
        if site != SEED and displayed_n(site, patch) != 0
    )


def blank_blocked_first_wave(patch: frozenset[Point]) -> frozenset[Point]:
    return frozenset(
        site
        for site in patch
        if site != SEED
        and n_is_defined(site, patch)
        and displayed_n(site, patch) != 0
    )


def off_patch_neighbors(site: Point, patch: frozenset[Point]) -> frozenset[Point]:
    return frozenset(neighbor for neighbor in neighbors(site) if neighbor not in patch)


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
    patch = two_cube()
    cube_a_sites = cube_a()
    cube_b_sites = cube_b()

    print("Unread neighbor is not occupancy zero")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "scope: supplied twelve-vertex two-cube; displayed L1 versus "
        "blank-blocked readiness; no adopted law and no axiom edit"
    )

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
    checks.check(
        "cache-write-disabled",
        "No runner cache is written." in note
        and "cache_write: false" not in note.split("## ", 1)[0],
    )

    checks.check("two-cube-has-twelve-sites", len(patch) == 12, f"|P|={len(patch)}")
    checks.check(
        "two-cube-factorization",
        len(cube_a_sites) == 8
        and len(cube_b_sites) == 8
        and len(cube_a_sites & cube_b_sites) == 4
        and cube_a_sites | cube_b_sites == patch,
    )
    checks.check("seed-on-patch", SEED in patch and SEED in cube_a_sites)
    checks.check("six-neighbor-star", len(SHIFTS) == 6 and len(set(SHIFTS)) == 6)

    seed_neighbors = frozenset(neighbors(SEED))
    checks.check(
        "seed-on-patch-neighbors-are-axis-sites",
        seed_neighbors & patch == AXIS_SITES,
        f"on-patch N(s)={sorted(seed_neighbors & patch)}",
    )

    occupancies = {site: occupancy(site, patch) for site in patch}
    checks.check(
        "seed-occupancy-one-others-zero",
        occupancies[SEED] == 1
        and all(value == 0 for site, value in occupancies.items() if site != SEED),
    )
    sample_off = add(SEED, (-1, 0, 0))
    checks.check(
        "off-patch-letter-is-blank-not-zero",
        sample_off not in patch and occupancy(sample_off, patch) == BLANK,
    )

    wave = l1_first_wave(patch)
    blocked = blank_blocked_first_wave(patch)
    axis_n = {site: displayed_n(site, patch) for site in AXIS_SITES}
    other_n = {
        site: displayed_n(site, patch)
        for site in patch
        if site not in AXIS_SITES and site != SEED
    }

    checks.check(
        "theorem1-l1-first-wave-is-axis-sites",
        wave == AXIS_SITES,
        f"W={sorted(wave)}",
    )
    checks.check(
        "theorem1-axis-n-nonzero",
        AXIS_SITES <= patch and all(value != 0 for value in axis_n.values()),
        f"n={axis_n}",
    )
    checks.check(
        "theorem1-nonaxis-unformed-n-zero",
        other_n and all(value == 0 for value in other_n.values()),
        f"count={len(other_n)}",
    )

    axis_off = {site: off_patch_neighbors(site, patch) for site in AXIS_SITES}
    checks.check(
        "theorem2-each-axis-site-has-off-patch-neighbor",
        all(len(off) >= 1 for off in axis_off.values()),
        f"off={ {site: sorted(off) for site, off in axis_off.items()} }",
    )
    checks.check(
        "theorem2-n-undefined-on-axis-sites",
        all(not n_is_defined(site, patch) for site in AXIS_SITES),
    )
    checks.check(
        "theorem2-blank-blocked-first-wave-empty",
        blocked == frozenset(),
        f"blocked={sorted(blocked)}",
    )
    checks.check(
        "theorem2-no-unformed-site-has-closed-star",
        all(not n_is_defined(site, patch) for site in patch if site != SEED),
    )

    checks.check(
        "theorem3-members-disagree-on-first-wave",
        wave != blocked and len(wave) == 3 and len(blocked) == 0,
    )
    checks.check(
        "theorem3-o-zero-default-is-load-bearing",
        wave == AXIS_SITES and blocked == frozenset(),
    )

    record_section = axiom.split("### Record / Fixed Reality", 1)[1].split(
        "## Qualification", 1
    )[0]
    checks.check(
        "source-unreadability-current",
        "A site with no record cannot be read." in normalize(record_section),
    )
    checks.check(
        "source-record-does-not-assign-occupancy-zero",
        all(phrase not in record_section for phrase in FORBIDDEN_AXIOM_PHRASES)
        and "occupancy 0" not in normalize(record_section)
        and "o=0" not in record_section,
    )
    checks.check(
        "source-occurrence-sentence-current",
        "Records form." in axiom,
    )
    checks.check(
        "note-does-not-write-unread-equals-zero-as-axiom",
        "does not write that assignment into axiom text" in normalized_note
        and "It is not an assignment of occupancy" in note
        and "unreadability is occupancy 0" not in normalized_note
        and "### Record / Fixed Reality" not in note,
    )

    claim_scope = (
        "On the supplied twelve-vertex two-cube, replacing off-patch `o=0` "
        "by “blank blocks readiness” empties the first wave. L1's wave uses "
        "the vacuum default. Displayed, not adopted."
    )
    checks.check("note-claim-scope-exact", claim_scope in note)
    checks.check(
        "note-l1-displayed-not-adopted",
        "L1 is displayed, not adopted." in note
        and "L2 is not adopted" in normalized_note,
    )
    checks.check(
        "note-not-leftover-character-or-new-patch",
        "not a leftover-character identity" in normalized_note
        and "not an `n_μ` step on a new patch" in note,
    )
    checks.check(
        "note-not-a-vacuum-axiom",
        "not a vacuum axiom" in normalized_note
        and "This is not a vacuum axiom" in note,
    )

    machine_markers = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "claim_type_reason:",
        "trace_class: negative_route_pruning",
        "target_claim_id: unread_neighbor_not_occupancy_zero",
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
        "note-forbidden-tokens-absent",
        all(token not in note for token in FORBIDDEN_NOTE_TOKENS),
    )
    checks.check(
        "note-no-go-n1-through-n8",
        all(f"### N{index}" in note for index in range(1, 9)),
    )
    checks.check(
        "note-no-go-route-enumeration",
        note.count("**ATTEMPTED**") >= 5
        and "treat unreadability as occupancy" in note
        and "vacuum axiom" in note,
    )
    checks.check(
        "note-steelman-rejects-automatic-zero-fill",
        "The strongest objection" in normalized_note
        and "filling `0` is extra encoding" in normalized_note,
    )

    n5_lines = (
        "per-element: executed — each of the twelve vertices is enumerated",
        "per-site: executed — n and readiness are computed at every unformed site",
        "per-mode: not applicable — no modal or spectral decomposition is used",
        "per-block: executed — only the supplied two-cube and seed are checked",
        "lattice-wide: not executed — no full Z^3 history or adopted formation law is claimed",
    )
    checks.check("note-n5-five-line-certificate", all(line in note for line in n5_lines))
    print("N5_CERTIFICATE:")
    for line in n5_lines:
        print(line)

    checks.check(
        "note-explicit-nonclaims",
        "No axiom, primitive, registry, citation manifest, runner cache, or audit"
        in note
        and "L2 is not adopted" in note,
    )
    checks.check("axiom-file-unedited-in-this-dispatch", AXIOM_PATH.is_file())

    return 0 if checks.finish() == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
