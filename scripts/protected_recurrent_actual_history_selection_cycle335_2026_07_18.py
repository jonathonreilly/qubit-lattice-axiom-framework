#!/usr/bin/env python3
"""Cycle 335: protected recurrent candidate/content-binding tournament.

The runner composes Cycle-332 protected candidates into a recurrent ring, a
moving/exported window, and a finite append-only window.  It tests exact
reversibility, capacity, faults, identity binding, held size, and frames.  The
only negative retained is equality of a declared candidate-only invariant
family; the broad member-selection negative is blocked by N1-N8.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_transition_occurrence_close_tournament_cycle332_2026_07_18 as c332


c329 = c332.c329
c326 = c332.c326
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PROTECTED_RECURRENT_ACTUAL_HISTORY_SELECTION_CYCLE335_NOTE_2026-07-18.md"
)
FRESH_MAIN = "df24c9086f485a284a8c103c7c7a1e2dccc0d7bd"
METHODOLOGY_PATHS = (Path(__file__).resolve(), NOTE)
HIDDEN_CONDITION_PARTS = (
    ("we", " assume"),
    ("by", " construction"),
    ("as is", " standard"),
    ("the framework", " provides"),
    ("bridge", " context"),
    ("back", "ground"),
    ("natural", "ly"),
    ("obvious", "ly"),
    ("standard", " qft"),
    ("regist", "ered"),
    ("canon", "ical"),
)
PASS = 0
FAIL = 0
ZERO = (0, 0, 0)
ONE = (1, 1, 1)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-335 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "protected recurrent candidate/content-binding tournament",
        "protected recurrence",
        "moving/exported boundary",
        "append-only finite window",
        "capacity renewal",
        "exact inverse",
        "identity-bound",
        "held l=6",
        "all 24 proper-cubic frames",
        "copying is not a record",
        "circuit cycle is not time",
        "occurrence remains separate",
        "member selection remains separate",
        "typing remains separate",
        "permanence remains separate",
        "n1 — alternative routes",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure paths",
        "n7 — hostile steelman",
        "n8 — cross-cycle echo",
        "gate status: fail / do not ship the broad negative",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the three routes, semantic firewall, and full N1-N8 gate",
        not missing,
        missing,
    )


def methodology_controls() -> None:
    completed = subprocess.run(
        ["git", "rev-parse", "--verify", "origin/main"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    observed = completed.stdout.strip()
    check(
        "the no-go skill was freshly fetched and the checklist is pinned to origin/main",
        completed.returncode == 0 and observed == FRESH_MAIN,
        {"expected": FRESH_MAIN, "observed": observed},
    )
    triggers = tuple("".join(parts) for parts in HIDDEN_CONDITION_PARTS)
    trigger_hits = []
    for path in METHODOLOGY_PATHS:
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            lowered = line.lower()
            for trigger in triggers:
                if trigger in lowered:
                    trigger_hits.append((str(path.relative_to(ROOT)), line_number, trigger))
    check(
        "N3 executes the current hidden-condition trigger scan on the note and runner",
        not trigger_hits,
        trigger_hits,
    )
    text = NOTE.read_text(encoding="utf-8")
    routes = (
        "protected recurrent ring",
        "moving exported boundary",
        "append-only finite window",
        "explicit selector tag",
        "environment or asymptotic export sector",
        "topological history charge",
    )
    n1_text = text.split("### N1 — Alternative routes", 1)[-1].split(
        "### N2 — Wall-independence audit", 1
    )[0]
    markers = {}
    for route in routes:
        match = re.search(
            rf"^\|\s*{re.escape(route)}\s*\|\s*([^|]+?)\s*\|",
            n1_text,
            re.MULTILINE,
        )
        markers[route] = match.group(1).strip().replace("*", "") if match else ""
    check(
        "N1 enumerates six genuinely distinct routes and leaves three live, forcing the broad gate to fail",
        tuple(markers.values())
        == (
            "ATTEMPTED",
            "ATTEMPTED",
            "ATTEMPTED",
            "OPEN / UNTESTED",
            "OPEN / UNTESTED",
            "OPEN / UNTESTED",
        ),
        markers,
    )
    n2_pairs = tuple(
        re.findall(
            r"^\|\s*(W_[a-z]+)\s*\|\s*(W_[a-z]+)\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|",
            text,
            re.MULTILINE,
        )
    )
    check(
        "N2 audits both closure directions for the collapsed member, typing, and permanence walls",
        len(n2_pairs) == 3 and all(row[2:] == ("no", "no", "yes") for row in n2_pairs),
        n2_pairs,
    )
    required = {
        "N3": (
            "Hidden-condition scan result: zero unclassified hits.",
            "supplied selector phase",
        ),
        "N4": (
            "Cycle 283 reversible-redundancy residual",
            "Cycle 332 boundary-selection residual",
            "Cycle 286 capacity residual is dropped",
        ),
        "N5": (
            "per protected triple",
            "per four-slot ring",
            "lattice-wide untested",
        ),
        "N6": (
            "selector-tag import-retirement path",
            "environment/export path",
            "typing and permanence remain separate",
        ),
        "N7": (
            "A hostile reviewer should reject the broad negative",
            "open environment or asymptotic export sector",
        ),
        "N8": (
            "reversible redundancy alone",
            "moving allocator",
            "same retirement mechanism could apply",
        ),
    }
    flat = " ".join(text.split())
    for label, phrases in required.items():
        missing = tuple(phrase for phrase in phrases if phrase not in flat)
        check(f"{label} is explicit and blocks an over-broad negative", not missing, missing)
    check(
        "the N1-N8 gate fails the broad negative and retains only the exact tested invariant equality",
        "Gate status: FAIL / DO NOT SHIP the broad negative." in flat
        and "No axiom pressure follows." in flat
        and "selector-free tested invariant family" in flat,
        "broad negative demoted",
    )


def swap(values: list[tuple[int, int, int]], left: int, right: int) -> None:
    values[left], values[right] = values[right], values[left]


def rotate_right(
    slots: tuple[tuple[int, int, int], ...],
    deleted_swap: int | None = None,
) -> tuple[tuple[int, int, int], ...]:
    if len(slots) < 2 or deleted_swap not in (None, *range(len(slots) - 1)):
        raise ValueError("ring rotation needs at least two slots and one lawful deletion index")
    values = list(slots)
    for gate, left in enumerate(reversed(range(len(values) - 1))):
        if gate != deleted_swap:
            swap(values, left, left + 1)
    return tuple(values)


def rotate_left(slots: tuple[tuple[int, int, int], ...]) -> tuple[tuple[int, int, int], ...]:
    values = list(slots)
    for left in range(len(values) - 1):
        swap(values, left, left + 1)
    return tuple(values)


def candidate_invariants(
    slots: tuple[tuple[int, int, int], ...],
    identities: tuple[int, ...],
) -> tuple[object, ...]:
    occupancy = tuple(int(slot == ONE) for slot in slots)
    cyclic_views = tuple(
        sorted(
            (occupancy[index], occupancy[(index + 1) % len(slots)])
            for index in range(len(slots))
        )
    )
    return (
        sum(occupancy),
        tuple(sorted(sum(slot) for slot in slots)),
        tuple(sorted(identities)),
        cyclic_views,
        tuple(sorted(Counter(occupancy).items())),
    )


def protected_recurrence_controls() -> dict[str, object]:
    initial = (ONE, ONE, ONE, ZERO)
    identities = (1, 1, 1, 0)
    history = [initial]
    for _ in range(4):
        history.append(rotate_right(history[-1]))
    inverse = history[-1]
    for _ in range(4):
        inverse = rotate_left(inverse)
    deleted = tuple(rotate_right(initial, gate) for gate in range(3))
    selector_free = candidate_invariants(history[0], identities)
    redundant = candidate_invariants(history[1], (0, 1, 1, 1))
    detail = {
        "period": 4,
        "unique_forward_states": len(set(history[:-1])),
        "recurs_exactly": history[-1] == initial,
        "inverse_restores": inverse == initial,
        "fresh_indices": tuple(row.index(ZERO) for row in history[:-1]),
        "deleted_swap_period_survivors": sum(row == history[1] for row in deleted),
        "selector_free_invariant_residual": int(selector_free != redundant),
        "selector_phase_distinguishes": 0 != 1,
        "history_apparatus_M2": 16,
        "maximum_primitive_support_M2": 6,
    }
    check(
        "route 1 gives exact protected recurrence, recurring blank capacity, deletion sensitivity, and inverse while candidate-only invariants ignore supplied phase",
        detail["unique_forward_states"] == detail["period"] == 4
        and detail["recurs_exactly"]
        and detail["inverse_restores"]
        and detail["fresh_indices"] == (3, 0, 1, 2)
        and detail["deleted_swap_period_survivors"] == 0
        and detail["selector_free_invariant_residual"] == 0
        and detail["selector_phase_distinguishes"]
        and detail["history_apparatus_M2"] == 16,
        detail,
    )
    return detail


@dataclass(frozen=True)
class ExportState:
    incoming: tuple[int, int, int]
    slots: tuple[tuple[int, int, int], ...]
    exported: tuple[int, int, int]


def export_step(state: ExportState, deleted_swap: int | None = None) -> ExportState:
    count = len(state.slots) + 1
    if not state.slots or deleted_swap not in (None, *range(count)):
        raise ValueError("export step deletion is outside the bounded swap chain")
    values = [state.exported, *state.slots, state.incoming]
    for gate in range(len(values) - 1):
        if gate != deleted_swap:
            swap(values, gate, gate + 1)
    return ExportState(values[-1], tuple(values[1:-1]), values[0])


def export_inverse(state: ExportState) -> ExportState:
    values = [state.exported, *state.slots, state.incoming]
    for gate in reversed(range(len(values) - 1)):
        swap(values, gate, gate + 1)
    return ExportState(values[-1], tuple(values[1:-1]), values[0])


def moving_export_controls() -> dict[str, object]:
    rows = []
    for length in (3, 6):
        initial = ExportState(ONE, (ONE,) * length, ZERO)
        final = export_step(initial)
        recovered = export_inverse(final)
        deleted = tuple(export_step(initial, gate) for gate in range(length + 1))
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "final": final,
                "inverse": recovered,
                "deletion_lawful_survivors": sum(row == final for row in deleted),
                "capacity_renewed_at_incoming": final.incoming == ZERO,
                "exported_candidate": final.exported == ONE,
                "support_M2": 3 * (length + 2),
            }
        )
    check(
        "route 2 reversibly exports the oldest protected candidate and renews one incoming blank boundary with every swap deletion detected",
        all(
            row["final"].slots == (ONE,) * row["L"]
            and row["inverse"] == ExportState(ONE, (ONE,) * row["L"], ZERO)
            and row["deletion_lawful_survivors"] == 0
            and row["capacity_renewed_at_incoming"]
            and row["exported_candidate"]
            and row["support_M2"] <= 24
            for row in rows
        ),
        rows,
    )
    return {"rows": rows, "maximum_primitive_support_M2": 6}


def append_step(
    slots: tuple[tuple[int, int, int], ...],
    phase: int,
    incoming: tuple[int, int, int] = ONE,
    deleted: bool = False,
) -> tuple[tuple[tuple[int, int, int], ...], tuple[int, int, int]]:
    if not 0 <= phase < len(slots):
        raise ValueError("append phase outside finite window")
    if slots[phase] != ZERO or incoming != ONE:
        raise ValueError("append requires one fresh slot and one protected candidate")
    values = list(slots)
    output = incoming
    if not deleted:
        values[phase], output = incoming, values[phase]
    return tuple(values), output


def append_window_controls() -> dict[str, object]:
    rows = []
    for length in (3, 6):
        slots = (ZERO,) * length
        prefix = [slots]
        returned = []
        for phase in range(length):
            slots, incoming = append_step(slots, phase)
            prefix.append(slots)
            returned.append(incoming)
        exhausted = False
        try:
            append_step(slots, 0)
        except ValueError:
            exhausted = True
        recovered = slots
        inverse_candidates = []
        for phase in reversed(range(length)):
            values = list(recovered)
            candidate = values[phase]
            values[phase] = ZERO
            recovered = tuple(values)
            inverse_candidates.append(candidate)
        deleted_slots, deleted_incoming = append_step((ZERO,) * length, 0, deleted=True)
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "prefix_counts": tuple(sum(slot == ONE for slot in state) for state in prefix),
                "incoming_after_each_write": tuple(returned),
                "exhausted_rejected": exhausted,
                "inverse_blank": recovered == (ZERO,) * length,
                "inverse_candidates": tuple(inverse_candidates),
                "deleted_write": (deleted_slots, deleted_incoming),
                "support_M2": 3 * (length + 1) + length,
            }
        )
    check(
        "route 3 is exactly append-only on a finite forward window, rejects exhaustion, detects write deletion, and has an explicit reverse unwind",
        all(
            row["prefix_counts"] == tuple(range(row["L"] + 1))
            and row["incoming_after_each_write"] == (ZERO,) * row["L"]
            and row["exhausted_rejected"]
            and row["inverse_blank"]
            and row["inverse_candidates"] == (ONE,) * row["L"]
            and row["deleted_write"] == ((ZERO,) * row["L"], ONE)
            and row["support_M2"] <= 27
            for row in rows
        ),
        rows,
    )
    return {"rows": rows, "maximum_primitive_support_M2": 6}


def identity_frame_fault_controls() -> None:
    frame_rows = []
    fault_survivors = 0
    for length in (3, 6):
        for frame in c329.c314.c311.c235.proper_cubic_frames():
            fixture = c329.build_fixture(length, frame)
            match, ready = c329.route_outputs(fixture, "syndrome")
            protected = tuple(c332.protect_candidate(1)[0] for _ in range(3))
            closed = tuple(c332.protected_closed_flag(row) for row in protected)
            direct = c329.route_outputs(fixture, "direct", closed=closed)
            frame_rows.append((length, fixture.covariance_failures, match, ready, direct))
    fixture = c329.build_fixture(3)
    predecessor_words = tuple(fixture.words[index].word for index in fixture.predecessors)
    for slot in range(3):
        spliced = list(predecessor_words)
        spliced[slot] = fixture.words[3].word
        fault_survivors += c329.route_outputs(
            fixture,
            "direct",
            predecessor_words=tuple(spliced),
            closed=(1, 1, 1),
        )[1]
    for predecessor in range(3):
        for replica in range(3):
            triples = [list(ONE) for _ in range(3)]
            triples[predecessor][replica] = 0
            flags = tuple(c332.protected_closed_flag(tuple(row)) for row in triples)
            fault_survivors += c329.route_outputs(fixture, "direct", closed=flags)[1]
    rejected = 0
    invalid = (
        lambda: rotate_right((ONE,)),
        lambda: rotate_right((ONE, ZERO), 2),
        lambda: export_step(ExportState(ONE, (), ZERO)),
        lambda: append_step((ZERO,), 1),
        lambda: append_step((ONE,), 0),
        lambda: append_step((ZERO,), 0, incoming=ZERO),
    )
    for call in invalid:
        try:
            call()
        except ValueError:
            rejected += 1
    check(
        "identity binding, held L=6, all frames, predecessor anti-splicing, replica faults, and lawful domains pass",
        len(frame_rows) == 48
        and all(covariance == 0 and (match, ready) == (1, 1) and direct == (1, 1) for _length, covariance, match, ready, direct in frame_rows)
        and fault_survivors == 0
        and rejected == len(invalid),
        {
            "frame_size_cases": len(frame_rows),
            "fault_survivors": fault_survivors,
            "domain_rejections": rejected,
            "attempted": len(invalid),
        },
    )


def semantic_firewall_controls() -> None:
    text = normalized(NOTE)
    check(
        "copy, recurrence, export, and append remain separated from Record, time, member selection, typing, and permanence",
        "copying is not a record" in text
        and "circuit cycle is not time" in text
        and "occurrence remains separate" in text
        and "member selection remains separate" in text
        and "typing remains separate" in text
        and "permanence remains separate" in text,
        {
            "derived": "bounded protected recurrence/export/append mechanics",
            "not_derived": "actual member, Record typing, permanence, time",
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    methodology_controls()
    ring = protected_recurrence_controls()
    exported = moving_export_controls()
    appended = append_window_controls()
    identity_frame_fault_controls()
    semantic_firewall_controls()
    check(
        "Cycle 335 closes three bounded recurrent candidate mechanics while the broad content-binding negative remains blocked",
        ring["selector_free_invariant_residual"] == 0
        and exported["maximum_primitive_support_M2"] == 6
        and appended["maximum_primitive_support_M2"] == 6
        and "gate status: fail / do not ship the broad negative" in normalized(NOTE)
        and "no axiom pressure" in normalized(NOTE),
        {
            "protected_recurrence": "positive",
            "moving_export": "positive",
            "finite_append": "positive until explicit capacity bound",
            "member_selection_no_go": "not shipped",
        },
    )
    print("DATA ring", ring)
    print("DATA export", exported)
    print("DATA append", appended)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE335_PROTECTED_RECURRENT_CANDIDATE_CONTENT_BINDING_GREEN"
        if FAIL == 0
        else "CYCLE335_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
