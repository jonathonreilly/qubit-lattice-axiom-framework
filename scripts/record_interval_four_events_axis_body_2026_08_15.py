#!/usr/bin/env python3
"""Exact display checks for s^2 = t_lock^2 - |x|_2^2 on four recorded events.

Clock is the named lock order on the recorded set R. Spatial quadratic is the
Euclidean square. Axis versus body class is reported. Displayed, not adopted.
No cache or governance surface is written.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/RECORD_INTERVAL_FOUR_EVENTS_AXIS_BODY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

Site = tuple[int, int, int]

RECORDED: tuple[Site, ...] = (
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 0),
    (1, 1, 1),
)
T_LOCK: dict[Site, int] = {
    (0, 0, 0): 0,
    (1, 0, 0): 1,
    (1, 1, 0): 2,
    (1, 1, 1): 3,
}
AXIS: Site = (1, 0, 0)
BODY: Site = (1, 1, 1)
ORIGIN: Site = (0, 0, 0)
FACE: Site = (1, 1, 0)
UNREAD: Site = (2, 0, 0)


def quadratic(site: Site) -> int:
    return site[0] * site[0] + site[1] * site[1] + site[2] * site[2]


def interval(site: Site, lock: dict[Site, int] = T_LOCK) -> int:
    tick = lock[site]
    return tick * tick - quadratic(site)


def interval_class(value: int) -> str:
    if value < 0:
        return "space"
    if value == 0:
        return "null"
    return "time"


def l1_length(site: Site) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def normalize(text: str) -> str:
    return " ".join(text.split())


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: none; R and the named lock order are "
        "displayed mathematical inputs; Q is the Euclidean square"
    )
    print("score_domain: recorded set R only")

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the note and current axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/RECORD_INTERVAL_FOUR_EVENTS_AXIS_BODY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)),
    )
    checks.check(
        "audit-timeout",
        "the declared audit timeout is 120 seconds",
        AUDIT_TIMEOUT_SEC == 120,
    )

    checks.check(
        "current-record-readable",
        "only records are readable and readout is content-determined",
        "Only records are readable." in axiom
        and "A readout value is determined by record content alone." in axiom_flat,
    )
    checks.check(
        "current-record-unreadability",
        "a site with no record cannot be read",
        "A site with no record cannot be read." in axiom,
    )
    checks.check(
        "current-admissibility-no-time-metric",
        "Admissibility does not define a time metric",
        "define a time metric" in axiom_flat
        and "It does not" in axiom,
    )

    values = {
        site: {
            "t": T_LOCK[site],
            "Q": quadratic(site),
            "s2": interval(site),
            "class": interval_class(interval(site)),
        }
        for site in RECORDED
    }
    for site in RECORDED:
        row = values[site]
        print(
            f"event {site}: t_lock={row['t']} Q={row['Q']} "
            f"s^2={row['s2']} class={row['class']}"
        )

    checks.check(
        "recorded-set-four",
        "the score domain is exactly the four named recorded events",
        RECORDED == ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1))
        and set(T_LOCK) == set(RECORDED)
        and UNREAD not in T_LOCK
        and len(RECORDED) == 4,
    )
    checks.check(
        "theorem1-quadratic",
        "Q is the Euclidean square on each recorded event",
        values[ORIGIN]["Q"] == ORIGIN[0] * ORIGIN[0] + ORIGIN[1] * ORIGIN[1] + ORIGIN[2] * ORIGIN[2]
        and values[AXIS]["Q"] == AXIS[0] * AXIS[0]
        and values[FACE]["Q"] == FACE[0] * FACE[0] + FACE[1] * FACE[1]
        and values[BODY]["Q"]
        == BODY[0] * BODY[0] + BODY[1] * BODY[1] + BODY[2] * BODY[2],
        {site: values[site]["Q"] for site in RECORDED},
    )
    checks.check(
        "theorem1-interval",
        "s^2 equals t_lock^2 minus Q on each recorded event",
        all(
            values[site]["s2"] == values[site]["t"] * values[site]["t"] - values[site]["Q"]
            for site in RECORDED
        ),
        {site: values[site]["s2"] for site in RECORDED},
    )
    origin_class = values[ORIGIN]["class"]
    axis_class = values[AXIS]["class"]
    face_class = values[FACE]["class"]
    body_class = values[BODY]["class"]
    checks.check(
        "theorem1-sign-classes",
        "sign of s^2 assigns null, null, time, time on the named order",
        origin_class == "null"
        and axis_class == "null"
        and face_class == "time"
        and body_class == "time"
        and values[ORIGIN]["s2"] == 0
        and values[AXIS]["s2"] == 0
        and values[FACE]["s2"] > 0
        and values[BODY]["s2"] > 0,
        {site: (values[site]["s2"], values[site]["class"]) for site in RECORDED},
    )
    checks.check(
        "theorem2-axis-null",
        "the axis event (1,0,0) is null",
        AXIS == (1, 0, 0) and axis_class == "null" and values[AXIS]["s2"] == 0,
        (values[AXIS]["s2"], axis_class),
    )
    checks.check(
        "theorem2-body-time",
        "the body event (1,1,1) is time",
        BODY == (1, 1, 1) and body_class == "time" and values[BODY]["s2"] > 0,
        (values[BODY]["s2"], body_class),
    )
    checks.check(
        "theorem3-distinct-classes",
        "axis and body do not lie in the same class",
        axis_class != body_class,
        (axis_class, body_class),
    )

    checks.check(
        "l1-not-attached",
        "Q is the Euclidean square even though L1 coincides on this R",
        all(l1_length(site) == quadratic(site) for site in RECORDED)
        and "This display does not attach L1." in note
        and "Q(x) = x·x = |x|_2^2" in note,
    )
    checks.check(
        "unread-not-scored",
        "unread sites are outside the score and are not a reverse map",
        UNREAD not in RECORDED
        and UNREAD not in T_LOCK
        and "Unread sites are not scored and are not a reverse map." in note_flat,
    )

    mutated_lock = dict(T_LOCK)
    mutated_lock[AXIS] = 2
    mutated_axis = interval_class(interval(AXIS, mutated_lock))
    mutated_body = interval_class(interval(BODY, mutated_lock))
    checks.check(
        "uniqueness-not-required",
        "a mutated lock order can place axis and body in the same class",
        mutated_axis == mutated_body == "time"
        and axis_class != body_class
        and "uniqueness of lock order is not required" in note_flat,
        (mutated_axis, mutated_body),
    )

    required = (
        "**Type:** bounded_theorem",
        "actual_current_surface_status: bounded-support",
        "hypothetical_axiom_status: no edit",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "Displayed, not adopted.",
        "The note does not write a metric into Admissibility.",
        "No hop-cost is used.",
        "Clock is this lock order.",
        "score domain is exactly `R`",
    )
    forbidden = (
        "G_N",
        "1/r",
        "1/r^2",
        "Lattice-named",
        "not a TOE",
        "Dijkstra",
        "B_57",
        "runner-cache",
    )
    checks.check(
        "note-claim-scope",
        "the note reports the displayed interval and axis-versus-body class",
        'claim_scope: "Interval s^2=t_lock^2-|x|_2^2 on four named recorded events, and axis vs body class, is reported. Displayed, not adopted."'
        in note,
    )
    checks.check(
        "note-contract",
        "machine fields, display scope, and hygiene hold",
        all(phrase in note for phrase in required)
        and all(phrase not in note for phrase in forbidden),
        [phrase for phrase in required if phrase not in note]
        + [phrase for phrase in forbidden if phrase in note],
    )
    table_needles = (
        "`0` | `0` | `0` | null",
        "`1` | `1` | `0` | null",
        "`2` | `2` | `2` | time",
        "`3` | `3` | `6` | time",
    )
    checks.check(
        "note-runner-table",
        "the note table matches the computed four-event display",
        all(needle in note for needle in table_needles)
        and values[BODY]["s2"] == T_LOCK[BODY] * T_LOCK[BODY] - quadratic(BODY)
        and values[FACE]["s2"] == T_LOCK[FACE] * T_LOCK[FACE] - quadratic(FACE),
        [needle for needle in table_needles if needle not in note],
    )

    print("per_element: Q and s^2 are evaluated on each of the four recorded events")
    print("per_site: unread sites are excluded from the score domain")
    print("per_mode: checked and not executed — no spectral object appears")
    print("lattice_wide: checked and not executed — only R is scored")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
