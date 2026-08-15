#!/usr/bin/env python3
"""Face-diagonal 2-site halt dynamics of f_min versus f_L1.

On the twelve-site two-cube with off-patch occupancy 0, run the nonempty
n_both=0 map f_min and the n≠0 map f_L1 from the face-diagonal seed
{(0,0,0),(1,1,0)}. Report halt locks, tick, and lock history. Display the
comparison. Do not adopt f_min and do not write it into Admissibility.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_MIN_TWO_SITE_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_MIN_TWO_SITE_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Site = tuple[int, int, int]
Counts = tuple[int, int, int]

SITES: tuple[Site, ...] = tuple(
    (x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1)
)
SITE_SET = frozenset(SITES)
AXES: tuple[tuple[Site, Site], ...] = (
    ((1, 0, 0), (-1, 0, 0)),
    ((0, 1, 0), (0, -1, 0)),
    ((0, 0, 1), (0, 0, -1)),
)
FACE_SEED: tuple[Site, ...] = ((0, 0, 0), (1, 1, 0))
ONE_SITE: tuple[Site, ...] = ((0, 0, 0),)
LINE_SEED: tuple[Site, ...] = ((0, 0, 0), (1, 0, 0), (2, 0, 0))


def add(left: Site, right: Site) -> Site:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def occupancy(site: Site, locks: frozenset[Site], off_patch: int) -> int:
    if site in locks:
        return 1
    if site not in SITE_SET:
        return off_patch
    return 0


def axis_counts(site: Site, locks: frozenset[Site], off_patch: int) -> Counts:
    n_unbalanced = 0
    n_both = 0
    n_empty = 0
    for plus, minus in AXES:
        occupied = occupancy(add(site, plus), locks, off_patch) + occupancy(
            add(site, minus), locks, off_patch
        )
        if occupied == 0:
            n_empty += 1
        elif occupied == 2:
            n_both += 1
        else:
            n_unbalanced += 1
    return (n_unbalanced, n_both, n_empty)


def f_l1(counts: Counts) -> bool:
    """n≠0: fire iff some axis is unbalanced."""
    return counts[0] >= 1


def f_min(counts: Counts) -> bool:
    """Nonempty n_both=0: fire iff no axis is both-occupied and some axis is unbalanced."""
    return counts[1] == 0 and counts[0] >= 1


def f_two(counts: Counts) -> bool:
    return counts[0] >= 2


def f_hamming(counts: Counts) -> bool:
    """Hamming parity of the six-neighbor occupancy word: |c|_1 = n_unbalanced + 2 n_both."""
    return (counts[0] + 2 * counts[1]) % 2 == 1


def complement_counts(counts: Counts) -> Counts:
    n_unbalanced, n_both, n_empty = counts
    return (n_unbalanced, n_empty, n_both)


def run_map(
    predicate,
    seed: tuple[Site, ...],
    off_patch: int = 0,
    max_ticks: int = 12,
) -> tuple[int, int, tuple[int, ...], frozenset[Site]]:
    locks = frozenset(seed)
    history = [len(locks)]
    for tick in range(1, max_ticks + 1):
        newly = frozenset(
            site
            for site in SITES
            if site not in locks and predicate(axis_counts(site, locks, off_patch))
        )
        if not newly:
            return tick - 1, len(locks), tuple(history), locks
        locks = locks | newly
        history.append(len(locks))
    return max_ticks, len(locks), tuple(history), locks


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: current Lattice, Admissibility, and Record boundaries only; no observations or fits")
    print("integrity_reads: this runner, its note, and the live axiom memo")
    print("construction: two-cube lock dynamics from a displayed face-diagonal 2-site seed")
    print("negative_scope: f_min is displayed, not adopted, and is not written into Admissibility")

    checks.check(
        "audit-inputs",
        "the required two source-bound inputs exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_MIN_TWO_SITE_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "audit-input-literal",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        'AUDIT_INPUT_PATHS = (\n    "docs/F_MIN_TWO_SITE_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in self_source,
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    formation_boundary = "does not supply the formation site, probability, or rate"
    no_dynamics = "Admissibility is not a dynamics axiom."

    checks.check(
        "source-lattice",
        "current cubic nearest-neighbor wording is pinned",
        lattice_sentence in normalized_axiom and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        "current local-distribution wording is pinned",
        admissibility_sentence in normalized_axiom and admissibility_sentence in note,
    )
    checks.check(
        "source-record-boundary",
        "current lock/content/unreadable-at-absence wording is pinned",
        all(phrase in normalized_axiom for phrase in (record_lock, record_content, record_absence))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )
    checks.check(
        "source-no-dynamics",
        "Admissibility remains not a dynamics axiom",
        no_dynamics in axiom and no_dynamics in note,
    )

    checks.check(
        "two-cube-cardinality",
        "the two-cube is the twelve-site set {0,1,2}x{0,1}x{0,1}",
        len(SITES) == 12 and len(SITE_SET) == 12,
    )
    checks.check(
        "face-seed",
        "the seed is the displayed face-diagonal pair",
        FACE_SEED == ((0, 0, 0), (1, 1, 0))
        and sum(abs(FACE_SEED[0][i] - FACE_SEED[1][i]) for i in range(3)) == 2,
    )

    wt1: Counts = (1, 0, 2)
    opp2: Counts = (0, 1, 2)
    adj2: Counts = (2, 0, 1)
    vertex3: Counts = (3, 0, 0)
    mixed3: Counts = (1, 1, 1)
    empty: Counts = (0, 0, 3)
    full: Counts = (0, 3, 0)
    orbit_bits = tuple(int(f_min(counts)) for counts in (wt1, opp2, adj2, vertex3, mixed3))
    checks.check(
        "f-min-definition",
        "f_min is 1 iff n_both=0 and some axis is unbalanced",
        orbit_bits == (1, 0, 1, 1, 0)
        and not f_min(empty)
        and not f_min(full)
        and f_min(wt1)
        and not f_min(mixed3),
    )
    checks.check(
        "f-l1-definition",
        "f_L1 is the n≠0 map: 1 iff some axis is unbalanced",
        tuple(int(f_l1(counts)) for counts in (wt1, opp2, adj2, vertex3, mixed3))
        == (1, 0, 1, 1, 1)
        and not f_l1(empty)
        and not f_l1(full)
        and f_l1(mixed3)
        and f_min != f_l1,
    )
    checks.check(
        "f-min-not-f-cut",
        "f_min is not complement-even, so it is not in F_cut",
        f_min(empty) == f_min(full) == False
        and f_min(wt1) != f_min(complement_counts(wt1))
        and f_l1(wt1) == f_l1(complement_counts(wt1))
        and f_l1(empty) == f_l1(full) == False,
    )
    checks.check(
        "f-l1-not-hamming",
        "f_L1 is n≠0 and is not Hamming parity",
        f_l1(wt1)
        and f_hamming(wt1)
        and f_l1(adj2)
        and not f_hamming(adj2)
        and not f_l1(opp2)
        and not f_hamming(opp2),
    )

    l1_one = run_map(f_l1, ONE_SITE)
    min_one = run_map(f_min, ONE_SITE)
    l1_line = run_map(f_l1, LINE_SEED)
    min_line = run_map(f_min, LINE_SEED)
    checks.check(
        "engine-one-site",
        "the lock engine recovers the displayed 1-site L1 history",
        l1_one[0] == 4
        and l1_one[1] == 12
        and l1_one[2] == (1, 4, 8, 11, 12)
        and min_one[2] == l1_one[2],
        residual=(l1_one[2], min_one[2]),
    )
    checks.check(
        "engine-line",
        "the lock engine recovers the displayed 3-site line L1 history",
        l1_line[0] == 2
        and l1_line[1] == 12
        and l1_line[2] == (3, 9, 12)
        and min_line[2] == l1_line[2],
        residual=(l1_line[2], min_line[2]),
    )

    l1_face = run_map(f_l1, FACE_SEED)
    min_face = run_map(f_min, FACE_SEED)
    two_face = run_map(f_two, FACE_SEED)
    ham_face = run_map(f_hamming, FACE_SEED)
    l1_t, l1_halt, l1_hist, l1_locks = l1_face
    min_t, min_halt, min_hist, min_locks = min_face

    print(f"f_L1 face-diagonal: T={l1_t} halt_locks={l1_halt} history={l1_hist} fills={l1_halt == 12}")
    print(f"f_min face-diagonal: T={min_t} halt_locks={min_halt} history={min_hist} fills={min_halt == 12}")

    checks.check(
        "thm1-l1-fills",
        "f_L1 fills the two-cube from the face-diagonal seed",
        l1_halt == 12 and len(l1_locks) == 12 and l1_locks == SITE_SET,
        residual=l1_hist,
    )
    checks.check(
        "thm1-l1-history",
        "f_L1 halt tick and lock history are reported",
        l1_t >= 1 and l1_hist[0] == 2 and l1_hist[-1] == 12 and len(l1_hist) == l1_t + 1,
        residual=(l1_t, l1_hist),
    )
    checks.check(
        "thm2-fmin-fills",
        "f_min fills the two-cube from the face-diagonal seed",
        min_halt == 12 and len(min_locks) == 12 and min_locks == SITE_SET,
        residual=min_hist,
    )
    checks.check(
        "thm2-fmin-history",
        "f_min halt locks, T, and lock history are reported",
        min_t >= 1
        and min_hist[0] == 2
        and min_hist[-1] == min_halt
        and len(min_hist) == min_t + 1
        and f"T={min_t}" in note
        and str(min_hist) in note
        and f"|locks_halt|={min_halt}" in note,
        residual=(min_t, min_hist),
    )
    checks.check(
        "thm3-comparison",
        "the two maps have the same face-diagonal history; comparison is displayed",
        min_hist == l1_hist
        and min_t == l1_t
        and min_halt == l1_halt
        and "same lock history" in normalized_note
        and "does fill" in normalized_note,
        residual=(min_hist, l1_hist),
    )
    checks.check(
        "thm3-not-adopted",
        "f_min is displayed and is not written into Admissibility",
        "Displayed, not adopted" in note
        and "not written into Admissibility" in normalized_note
        and "do not adopt f_min" in normalized_note.lower(),
    )
    checks.check(
        "mutation-f-two",
        "the u≥2 map from the same seed does not fill",
        two_face[1] != 12 and two_face[1] == 4 and two_face[2] == (2, 4),
        residual=two_face[2],
    )
    checks.check(
        "mutation-hamming",
        "Hamming parity from the same seed does not match either history",
        ham_face[2] != min_hist and ham_face[1] != 12,
        residual=ham_face[2],
    )
    checks.check(
        "mutation-off-patch",
        "off-patch occupancy 1 changes the f_min run",
        run_map(f_min, FACE_SEED, off_patch=1)[2] != min_hist,
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: frontier_discovery",
        "reachability_to_target: advances",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "f_L1 is n≠0",
        "not Hamming",
    )
    forbidden = (
        "G_N",
        "1/r",
        "1/r^2",
        "Lattice-named",
        "not a TOE",
        "new axiom",
        "trace_class: direct_blocker_closure",
        "reachability_to_target: partially_closes",
    )
    checks.check(
        "note-contract",
        "machine fields, display-only scope, N1-N8, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required)
        and all(line in note for line in allowed_retained)
        and all(f"### N{i}" in note for i in range(1, 9))
        and not any(phrase in note for phrase in forbidden)
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "Block 12" not in note
        and "toe-lphys" not in note
        and "hypothetical_axiom_status: \"no edit\"" in note,
    )
    checks.check(
        "claim-scope",
        "claim_scope states that f_min does fill from the face-diagonal seed",
        "the nonempty n_both=0 map f_min does fill from the face-diagonal 2-site seed"
        in normalized_note,
    )

    print("per_element: axis-type words and six-neighbor occupancy bits are enumerated exactly")
    print("per_site: lock readiness is evaluated at each of the twelve two-cube sites")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: the face-diagonal seed run of f_min and f_L1 is executed to halt")
    print("lattice_wide: checked and not executed — no infinite-lattice or axiom edit is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
