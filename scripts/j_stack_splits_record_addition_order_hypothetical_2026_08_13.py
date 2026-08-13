#!/usr/bin/env python3
"""C1 follow-on: J-stack splits record-addition order; I-stack does not.

Reconstructs C1 occupancy arithmetic on W={x,y}. Histories are addition
events. J is the site map to {0} union menu; I is the occupied-site count.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "J_STACK_SPLITS_RECORD_ADDITION_ORDER_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/J_STACK_SPLITS_RECORD_ADDITION_ORDER_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

WINDOW = ("x", "y")
MENU = frozenset({"A", "B"})
VACANT = 0
LETTER_A = "A"


def file_sha256(relative_path: str) -> str:
    path = ROOT / relative_path
    return hashlib.sha256(path.read_bytes()).hexdigest()


def empty_occupancy() -> dict[str, object]:
    return {site: VACANT for site in WINDOW}


def occupy(occupancy: dict[str, object], site: str, letter: str) -> dict[str, object]:
    if site not in WINDOW:
        raise ValueError("site outside window")
    if letter not in MENU:
        raise ValueError("letter outside menu")
    if occupancy[site] != VACANT:
        raise ValueError("site already locked")
    next_map = dict(occupancy)
    next_map[site] = letter
    return next_map


def snapshots_from_additions(
    events: tuple[tuple[str, str], ...],
) -> tuple[dict[str, object], ...]:
    occupancy = empty_occupancy()
    frames = [dict(occupancy)]
    for site, letter in events:
        occupancy = occupy(occupancy, site, letter)
        frames.append(dict(occupancy))
    return tuple(frames)


def I_of(occupancy: dict[str, object]) -> int:
    return sum(1 for site in WINDOW if occupancy[site] != VACANT)


def J_of(occupancy: dict[str, object]) -> tuple[object, ...]:
    return tuple(occupancy[site] for site in WINDOW)


def content_bag(occupancy: dict[str, object]) -> tuple[object, ...]:
    locked = tuple(occupancy[site] for site in WINDOW if occupancy[site] != VACANT)
    if not locked:
        return ("empty",)
    return locked


def occupancy_nondecreasing(frames: tuple[dict[str, object], ...]) -> bool:
    for earlier, later in zip(frames, frames[1:]):
        for site in WINDOW:
            if earlier[site] != VACANT and later[site] != earlier[site]:
                return False
            if I_of(later) < I_of(earlier):
                return False
    return True


def I_stack(history: tuple[tuple[str, str], ...]) -> tuple[int, ...]:
    return tuple(I_of(frame) for frame in snapshots_from_additions(history))


def J_stack(history: tuple[tuple[str, str], ...]) -> tuple[tuple[object, ...], ...]:
    return tuple(J_of(frame) for frame in snapshots_from_additions(history))


def bag_stack(history: tuple[tuple[str, str], ...]) -> tuple[tuple[object, ...], ...]:
    return tuple(content_bag(frame) for frame in snapshots_from_additions(history))


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: current Record wording only; no observational or fitted inputs")
    print("package_local_integrity_reads: source note and axiom memo are the declared audit inputs")
    print(
        "input_sha256:",
        {path: file_sha256(path) for path in AUDIT_INPUT_PATHS},
    )

    H_xy = (("x", LETTER_A), ("y", LETTER_A))
    H_yx = (("y", LETTER_A), ("x", LETTER_A))

    i_xy = I_stack(H_xy)
    i_yx = I_stack(H_yx)
    j_xy = J_stack(H_xy)
    j_yx = J_stack(H_yx)
    bags_xy = bag_stack(H_xy)
    bags_yx = bag_stack(H_yx)
    frames_xy = snapshots_from_additions(H_xy)
    frames_yx = snapshots_from_additions(H_yx)

    expected_i = (0, 1, 2)
    expected_j_xy = ((VACANT, VACANT), (LETTER_A, VACANT), (LETTER_A, LETTER_A))
    expected_j_yx = ((VACANT, VACANT), (VACANT, LETTER_A), (LETTER_A, LETTER_A))
    expected_bags = (("empty",), (LETTER_A,), (LETTER_A, LETTER_A))

    checks.check(
        "source-records-form",
        "axiom names record occurrence",
        "Records form." in axiom,
    )
    checks.check(
        "source-permanence",
        "axiom names one-record-per-site permanence",
        "records are permanent" in axiom and "never carries more than one record" in axiom,
    )
    checks.check(
        "source-content-only",
        "axiom names content-only readout",
        "determined by record content" in axiom,
    )
    checks.check(
        "source-additive-I",
        "axiom names additive scalar I with empty zero",
        "scalar readout" in axiom and "I` is additive" in axiom and "I(empty)=0" in axiom,
    )

    checks.check(
        "identity-I-xy",
        "I_stack(H_xy) equals (0,1,2)",
        I_stack(H_xy) == expected_i and i_xy == (0, 1, 2),
    )
    checks.check(
        "identity-I-yx",
        "I_stack(H_yx) equals (0,1,2)",
        I_stack(H_yx) == expected_i and i_yx == (0, 1, 2),
    )
    checks.check(
        "identity-J-xy",
        "J_stack(H_xy) equals ((0,0),(A,0),(A,A))",
        J_stack(H_xy) == expected_j_xy and j_xy == expected_j_xy,
    )
    checks.check(
        "identity-J-yx",
        "J_stack(H_yx) equals ((0,0),(0,A),(A,A))",
        J_stack(H_yx) == expected_j_yx and j_yx == expected_j_yx,
    )

    checks.check(
        "theorem-1-I-agreement",
        "I-stacks agree so addition order is I-blind",
        i_xy == i_yx == expected_i,
    )
    checks.check(
        "theorem-1-bags",
        "site-blind content bags agree on both histories",
        bags_xy == bags_yx == expected_bags,
    )
    checks.check(
        "theorem-2-J-split",
        "J-stacks differ at the mid-step",
        j_xy != j_yx and j_xy[1] == (LETTER_A, VACANT) and j_yx[1] == (VACANT, LETTER_A),
    )
    checks.check(
        "three-snapshots",
        "each history has empty, one-lock, and two-lock frames",
        len(frames_xy) == 3 and len(frames_yx) == 3 and len(i_xy) == 3 and len(j_xy) == 3,
    )
    checks.check(
        "unit-lock-integers",
        "empty I is 0 and each unit lock adds exactly 1",
        I_of(empty_occupancy()) == 0
        and I_of(frames_xy[1]) == 1
        and I_of(frames_xy[2]) == 2
        and I_of(frames_yx[1]) == 1,
    )
    checks.check(
        "permanence-nondecreasing",
        "occupancy is nondecreasing on both legal orders",
        occupancy_nondecreasing(frames_xy) and occupancy_nondecreasing(frames_yx),
    )
    checks.check(
        "both-orders-lock-A",
        "both legal orders lock A and never B",
        all(frame[site] in (VACANT, LETTER_A) for frame in frames_xy + frames_yx for site in WINDOW)
        and J_of(frames_xy[-1]) == (LETTER_A, LETTER_A)
        and J_of(frames_yx[-1]) == (LETTER_A, LETTER_A),
    )

    i_differ = I_stack(H_xy) != I_stack(H_yx)
    j_equal = J_stack(H_xy) == J_stack(H_yx)
    checks.check(
        "mutation-I-differ-fails",
        "predicate I_stack(H_xy) differs from I_stack(H_yx) fails",
        i_differ is False,
    )
    checks.check(
        "mutation-J-equal-fails",
        "predicate J_stack(H_xy)=J_stack(H_yx) fails",
        j_equal is False,
    )

    checks.check(
        "note-displayed-stacks",
        "note displays both I-stacks and both J-stacks",
        all(
            phrase in note
            for phrase in (
                "I(H_xy)=(0,1,2)=I(H_yx)",
                "J(H_xy)=((0,0),(A,0),(A,A))",
                "((0,0),(0,A),(A,A))=J(H_yx)",
                "({∅}, {A}, {A,A})",
            )
        ),
    )
    checks.check(
        "note-theorem-3-record-quote",
        "note quotes formation, permanence, content-only readout, and additive I",
        all(
            phrase in note
            for phrase in (
                "Records form",
                "records are permanent",
                "content-only readout",
                "additive `I`",
                "“Records form” is existence, not a J-process",
            )
        ),
    )
    checks.check(
        "note-non-adoption",
        "note displays and does not adopt rate, clock, r=1/2, L_phys, or pairing on J",
        all(
            phrase in note
            for phrase in (
                "Do not adopt",
                "does not install a clock map `a`",
                "Do not force `r=1/2`",
                "Do not adopt `L_phys`",
                "Do not put a pairing on `J`",
            )
        ),
    )
    checks.check(
        "machine-status-contract",
        "required hypothetical and surface status strings are present",
        'hypothetical_axiom_status: "C1 follow-on: Record addition-order stack is J-valued, not I-valued; not adopted"'
        in note
        and "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "axiom-unedited",
        "canonical axiom memo does not contain the hypothetical J-stack rewrite",
        all(
            phrase not in axiom
            for phrase in (
                "J-stack",
                "I-stack",
                "H_xy",
                "clock map a",
                "pairing on J",
            )
        ),
    )
    checks.check(
        "identity-gates-bind-functions",
        "identity gates are live calls of I_stack and J_stack on both histories",
        callable(I_stack)
        and callable(J_stack)
        and I_stack(H_xy) == i_xy
        and I_stack(H_yx) == i_yx
        and J_stack(H_xy) == j_xy
        and J_stack(H_yx) == j_yx,
    )

    print("per_element: two addition events per history; unit lock I=1")
    print("per_site: window {x,y}; mid-step site is the only J split")
    print("per_mode: I-stack and site-blind bags are order-blind; J-stack is not")
    print("per_block: addition-order process type only; no rate, clock, L_phys, or pairing")
    print("lattice_wide: checked and not executed — two-site window only")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
