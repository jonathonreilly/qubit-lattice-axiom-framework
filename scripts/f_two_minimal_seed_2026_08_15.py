#!/usr/bin/env python3
"""Minimal occupancy seed for a nonempty f_two first wave.

The paired note is
docs/F_TWO_MINIMAL_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md.

Objects: the displayed twelve-vertex two-cube with off-patch occupancy 0,
seeds as lock sets, and f_two (form iff at least two axes unbalanced).
The predicate is displayed, not adopted. No axiom sentence is written.
No cache is written.
"""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_TWO_MINIMAL_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_TWO_MINIMAL_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

SLOTS: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
AXIS_PAIRS = ((0, 1), (2, 3), (4, 5))
OFF_PATCH = 0
SEED3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SEED2 = ((0, 0, 0), (1, 1, 0))


def normalize(text: str) -> str:
    return " ".join(text.split())


def two_cube_patch() -> frozenset[tuple[int, int, int]]:
    cube_a = product((0, 1), (0, 1), (0, 1))
    cube_b = product((1, 2), (0, 1), (0, 1))
    return frozenset(cube_a) | frozenset(cube_b)


def occupancy(
    site: tuple[int, int, int],
    locked: frozenset[tuple[int, int, int]],
    patch: frozenset[tuple[int, int, int]],
) -> int:
    if site in locked:
        return 1
    if site not in patch:
        return OFF_PATCH
    return 0


def neighbor_cell(
    site: tuple[int, int, int],
    locked: frozenset[tuple[int, int, int]],
    patch: frozenset[tuple[int, int, int]],
) -> tuple[int, ...]:
    return tuple(
        occupancy(
            (site[0] + slot[0], site[1] + slot[1], site[2] + slot[2]),
            locked,
            patch,
        )
        for slot in SLOTS
    )


def unbalanced_axis_count(cell: tuple[int, ...]) -> int:
    return sum(cell[plus] != cell[minus] for plus, minus in AXIS_PAIRS)


def f_two(cell: tuple[int, ...]) -> int:
    return int(unbalanced_axis_count(cell) >= 2)


def f_l1(cell: tuple[int, ...]) -> int:
    return int(unbalanced_axis_count(cell) >= 1)


def first_wave(
    func,
    locked: frozenset[tuple[int, int, int]],
    patch: frozenset[tuple[int, int, int]],
) -> frozenset[tuple[int, int, int]]:
    return frozenset(
        site
        for site in patch
        if site not in locked and func(neighbor_cell(site, locked, patch)) == 1
    )


def on_patch_neighbors(
    site: tuple[int, int, int],
    patch: frozenset[tuple[int, int, int]],
) -> frozenset[tuple[int, int, int]]:
    return frozenset(
        (site[0] + slot[0], site[1] + slot[1], site[2] + slot[2])
        for slot in SLOTS
        if (site[0] + slot[0], site[1] + slot[1], site[2] + slot[2]) in patch
    )


def taxicab(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(abs(left[i] - right[i]) for i in range(3))


def max_gap(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return max(abs(left[i] - right[i]) for i in range(3))


def is_face_diagonal(
    pair: tuple[tuple[int, int, int], tuple[int, int, int]],
    patch: frozenset[tuple[int, int, int]],
) -> bool:
    left, right = pair
    shared = on_patch_neighbors(left, patch) & on_patch_neighbors(right, patch)
    return taxicab(left, right) == 2 and max_gap(left, right) == 1 and len(shared) == 2


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

    print("Minimal occupancy seed for an f_two first wave")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scope: displayed f_two first-wave seed census on the two-cube; not adopted")

    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "audit-input-paths-literal",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_TWO_MINIMAL_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor "
        "adjacency, standard translations, and proper cubic rotations about each site."
    )
    covariant_rule_sentence = (
        "There is one fixed nearest-neighbor admissibility rule, covariant under lattice "
        "translations and proper cubic rotations."
    )
    formation_boundary = "it does not supply the formation site, probability, or rate"
    records_form = "Records form."

    checks.check(
        "source-lattice-current",
        lattice_sentence in normalized_axiom and lattice_sentence in normalized_note,
    )
    checks.check(
        "source-one-fixed-covariant-rule-current",
        covariant_rule_sentence in normalized_axiom
        and covariant_rule_sentence in normalized_note,
    )
    checks.check(
        "source-formation-open-current",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )
    checks.check(
        "source-records-form-current",
        records_form in axiom and records_form in note,
    )
    checks.check(
        "note-no-axiom-edit",
        "hypothetical_axiom_status: no edit" in note
        or 'hypothetical_axiom_status: "no edit"' in note,
    )

    patch = two_cube_patch()
    sites = tuple(sorted(patch))
    checks.check("two-cube-has-twelve-sites", len(patch) == 12 and len(sites) == 12)
    checks.check("off-patch-default-is-zero", OFF_PATCH == 0)

    one_site_waves = {
        seed: first_wave(f_two, frozenset({seed}), patch) for seed in sites
    }
    one_site_max_u = []
    for seed in sites:
        locked = frozenset({seed})
        for site in patch:
            if site == seed:
                continue
            one_site_max_u.append(unbalanced_axis_count(neighbor_cell(site, locked, patch)))
    checks.check(
        "thm1-all-one-site-empty",
        all(wave == frozenset() for wave in one_site_waves.values()),
        f"n={len(one_site_waves)}",
    )
    checks.check(
        "thm1-neighbors-u-leq-1",
        one_site_max_u and max(one_site_max_u) <= 1,
        f"max_u={max(one_site_max_u) if one_site_max_u else None}",
    )

    pairs = tuple(combinations(sites, 2))
    pair_waves = {
        pair: first_wave(f_two, frozenset(pair), patch) for pair in pairs
    }
    nonempty_pairs = tuple(pair for pair, wave in pair_waves.items() if wave)
    empty_pairs = tuple(pair for pair, wave in pair_waves.items() if not wave)
    face_diags = tuple(pair for pair in pairs if is_face_diagonal(pair, patch))
    face_diag_set = set(face_diags)
    nonempty_set = set(nonempty_pairs)
    print(f"pair_count={len(pairs)}")
    print(f"nonempty_pair_count={len(nonempty_pairs)}")
    print(f"face_diagonal_count={len(face_diags)}")

    checks.check("pair-count-66", len(pairs) == 66)
    checks.check(
        "thm2-face-diagonal-count-22",
        len(face_diags) == 6 * 2 + 6 * 2 - 2 == 22,
        f"count={len(face_diags)}",
    )
    checks.check(
        "thm2-nonempty-equals-face-diagonals",
        nonempty_set == face_diag_set,
        f"nonempty={len(nonempty_pairs)}",
    )
    checks.check(
        "thm2-non-face-diagonals-empty",
        len(empty_pairs) == 66 - 22
        and all(not is_face_diagonal(pair, patch) for pair in empty_pairs),
    )
    checks.check(
        "mutation-all-pairs-empty-fails",
        len(nonempty_pairs) != 0,
    )

    wave2 = pair_waves[SEED2]
    expected2 = frozenset({(1, 0, 0), (0, 1, 0)})
    print(f"explicit_pair={SEED2}")
    print(f"explicit_pair_wave={sorted(wave2)}")
    checks.check(
        "thm2-explicit-pair-wave",
        SEED2 in face_diag_set and wave2 == expected2,
    )

    locked3 = frozenset(SEED3)
    wave3 = first_wave(f_two, locked3, patch)
    expected3 = frozenset({(0, 0, 0), (1, 0, 1), (1, 1, 0), (0, 1, 1)})
    print(f"explicit_triple={SEED3}")
    print(f"explicit_triple_wave={sorted(wave3)}")
    checks.check("thm3-explicit-triple-nonempty", wave3 == expected3 and len(wave3) >= 1)
    checks.check(
        "thm3-triple-is-axis-neighbors-of-corner",
        locked3 == on_patch_neighbors((0, 0, 0), patch) and (0, 0, 0) in wave3,
    )
    checks.check(
        "minimal-cardinality-is-2",
        all(wave == frozenset() for wave in one_site_waves.values())
        and len(nonempty_pairs) >= 1
        and len(wave3) >= 1,
    )

    l1_wave = first_wave(f_l1, frozenset({(0, 0, 0)}), patch)
    checks.check(
        "l1-one-site-contrast-nonempty",
        l1_wave == on_patch_neighbors((0, 0, 0), patch) and len(l1_wave) == 3,
    )
    checks.check(
        "not-l1-identity",
        first_wave(f_two, frozenset({(0, 0, 0)}), patch) != l1_wave,
    )

    checks.check(
        "note-reports-pair-census",
        "22 of 66" in note and "S2 = {(0,0,0), (1,1,0)}" in note,
    )
    checks.check(
        "note-reports-explicit-triple",
        "S3 = {(1,0,0), (0,1,0), (0,0,1)}" in note
        and "(0,0,0), (1,0,1), (1,1,0), (0,1,1)" in note,
    )
    checks.check(
        "note-claim-scope-displayed-not-adopted",
        "Displayed, not adopted" in note and "does not adopt `f_two`" in note,
    )
    checks.check(
        "note-does-not-claim-all-pairs-empty",
        "every two-site seed has empty first wave” is therefore" in note
        or 'every two-site seed has empty first wave" is therefore' in note
        or "every two-site seed has empty first wave` is therefore" in note,
    )
    # The previous check is fragile. Also require the failed-mutation sentence.
    checks.check(
        "note-records-failed-all-pairs-empty",
        "failed mutation" in note and "minimal occupancy-seed cardinality" in note,
    )

    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE", "new axiom")
    checks.check(
        "forbidden-phrase-hygiene",
        all(phrase not in note for phrase in forbidden),
        ",".join(phrase for phrase in forbidden if phrase in note),
    )
    checks.check(
        "no-runner-cache-or-citation-manifest",
        "runner-cache" not in note
        and "citation_manifest" not in note
        and "CITATION_MANIFEST" not in note,
    )

    print("per_element: checked exactly — u and readiness at each unlocked site")
    print("per_site: checked exactly — all twelve vertices as one-site seeds")
    print("per_mode: checked exactly — all 66 pairs and the explicit triple")
    print("per_block: checked exactly — face-diagonal census versus first-wave emptiness")
    print("lattice_wide: checked and not executed — no physical formation law is selected")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
