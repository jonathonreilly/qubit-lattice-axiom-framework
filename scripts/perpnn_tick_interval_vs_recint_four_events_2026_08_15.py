#!/usr/bin/env python3
"""Exact display checks for s^2 under perpnn ticks versus recint classes.

Clock is the displayed perpnn formation-tick map on the recorded set R.
Spatial quadratic is the Euclidean square. Axis versus body class is compared
with the displayed recint labels. Displayed, not adopted. No cache or
governance surface is written.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/PERPNN_TICK_INTERVAL_VS_RECINT_FOUR_EVENTS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
T_PERPNN: dict[Site, int] = {
    (0, 0, 0): 0,
    (1, 0, 0): 3,
    (1, 1, 0): 2,
    (1, 1, 1): 3,
}
AXIS: Site = (1, 0, 0)
BODY: Site = (1, 1, 1)
ORIGIN: Site = (0, 0, 0)
FACE: Site = (1, 1, 0)
RECINT_AXIS_CLASS = "null"
RECINT_BODY_CLASS = "time"


def quadratic(site: Site) -> int:
    return site[0] * site[0] + site[1] * site[1] + site[2] * site[2]


def interval(site: Site, ticks: dict[Site, int] = T_PERPNN) -> int:
    tick = ticks[site]
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
        "external_scientific_inputs: none; R and the named perpnn ticks are "
        "displayed mathematical inputs; recint axis/body classes are named "
        "displayed labels; Q is the Euclidean square"
    )
    print("score_domain: recorded set R only")
    print(
        "claim_scope: Interval s^2 under perpnn formation-ticks on four named "
        "recorded events, versus recint axis/body classes, is reported. "
        "Displayed, not adopted."
    )

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the note and current axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/PERPNN_TICK_INTERVAL_VS_RECINT_FOUR_EVENTS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
            "t": T_PERPNN[site],
            "Q": quadratic(site),
            "s2": interval(site),
            "class": interval_class(interval(site)),
        }
        for site in RECORDED
    }
    for site in RECORDED:
        row = values[site]
        print(
            f"event {site}: t={row['t']} Q={row['Q']} "
            f"s^2={row['s2']} class={row['class']}"
        )

    checks.check(
        "recorded-set-four",
        "the score domain is exactly the four named recorded events",
        RECORDED == ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1))
        and set(T_PERPNN) == set(RECORDED)
        and len(RECORDED) == 4,
    )
    checks.check(
        "displayed-perpnn-ticks",
        "perpnn ticks on R are the displayed values 0, 3, 2, 3",
        tuple(T_PERPNN[site] for site in RECORDED) == (0, 3, 2, 3)
        and "not recomputed by path dump" in note_flat,
        tuple(T_PERPNN[site] for site in RECORDED),
    )
    checks.check(
        "theorem1-quadratic",
        "Q is the Euclidean square on each recorded event",
        values[ORIGIN]["Q"] == 0
        and values[AXIS]["Q"] == 1
        and values[FACE]["Q"] == 2
        and values[BODY]["Q"] == 3
        and all(values[site]["Q"] == quadratic(site) for site in RECORDED),
        {site: values[site]["Q"] for site in RECORDED},
    )
    checks.check(
        "theorem1-interval",
        "s^2 equals t^2 minus Q on each recorded event",
        values[ORIGIN]["s2"] == 0
        and values[AXIS]["s2"] == 8
        and values[FACE]["s2"] == 2
        and values[BODY]["s2"] == 6
        and all(
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
        "sign of s^2 assigns null, time, time, time under perpnn ticks",
        origin_class == "null"
        and axis_class == "time"
        and face_class == "time"
        and body_class == "time"
        and values[ORIGIN]["s2"] == 0
        and values[AXIS]["s2"] > 0
        and values[FACE]["s2"] > 0
        and values[BODY]["s2"] > 0,
        {site: (values[site]["s2"], values[site]["class"]) for site in RECORDED},
    )
    checks.check(
        "theorem2-axis-time",
        "the axis event (1,0,0) is time",
        AXIS == (1, 0, 0) and axis_class == "time" and values[AXIS]["s2"] == 8,
        (values[AXIS]["s2"], axis_class),
    )
    checks.check(
        "theorem2-body-time",
        "the body event (1,1,1) is time",
        BODY == (1, 1, 1) and body_class == "time" and values[BODY]["s2"] == 6,
        (values[BODY]["s2"], body_class),
    )
    checks.check(
        "theorem3-recint-labels",
        "recint comparison labels are axis null and body time",
        RECINT_AXIS_CLASS == "null"
        and RECINT_BODY_CLASS == "time"
        and "recint axis class = null" in note
        and "recint body class = time" in note,
    )
    checks.check(
        "theorem3-axis-disagrees",
        "axis class under perpnn ticks disagrees with recint",
        axis_class != RECINT_AXIS_CLASS
        and axis_class == "time"
        and RECINT_AXIS_CLASS == "null",
        (axis_class, RECINT_AXIS_CLASS),
    )
    checks.check(
        "theorem3-body-agrees",
        "body class under perpnn ticks agrees with recint",
        body_class == RECINT_BODY_CLASS == "time",
        (body_class, RECINT_BODY_CLASS),
    )
    checks.check(
        "theorem3-pair-disagrees",
        "the axis/body class pair does not agree with recint",
        (axis_class, body_class) != (RECINT_AXIS_CLASS, RECINT_BODY_CLASS),
        ((axis_class, body_class), (RECINT_AXIS_CLASS, RECINT_BODY_CLASS)),
    )

    checks.check(
        "l1-not-attached",
        "Q is the Euclidean square even though L1 coincides on this R",
        all(l1_length(site) == quadratic(site) for site in RECORDED)
        and "This display does not attach L1." in note
        and "Q(x) = |x|_2^2" in note,
    )
    checks.check(
        "not-occupancy-lock-order-table",
        "the note is not a second occupancy lock-order table",
        "not a second occupancy lock-order table" in note_flat
        and "does not reprint the occupancy lock-order table" in note_flat,
    )

    mutated_ticks = dict(T_PERPNN)
    mutated_ticks[AXIS] = 1
    mutated_axis = interval_class(interval(AXIS, mutated_ticks))
    mutated_body = interval_class(interval(BODY, mutated_ticks))
    checks.check(
        "uniqueness-not-required",
        "a mutated tick assignment can make the axis class match recint",
        mutated_axis == RECINT_AXIS_CLASS == "null"
        and mutated_body == body_class == "time"
        and axis_class != RECINT_AXIS_CLASS
        and "Uniqueness of the displayed ticks is not required" in note_flat,
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
        "This display does not attach L1.",
        "not recomputed by path dump",
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
        "the note reports the displayed interval versus recint classes",
        'claim_scope: "Interval s^2 under perpnn formation-ticks on four named recorded events, versus recint axis/body classes, is reported. Displayed, not adopted."'
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
        "`3` | `1` | `8` | time",
        "`2` | `2` | `2` | time",
        "`3` | `3` | `6` | time",
    )
    checks.check(
        "note-runner-table",
        "the note table matches the computed four-event display",
        all(needle in note for needle in table_needles)
        and values[AXIS]["s2"] == T_PERPNN[AXIS] * T_PERPNN[AXIS] - quadratic(AXIS)
        and values[BODY]["s2"] == T_PERPNN[BODY] * T_PERPNN[BODY] - quadratic(BODY),
        [needle for needle in table_needles if needle not in note],
    )

    print("per_element: Q and s^2 are evaluated on each of the four recorded events")
    print("per_site: only the four named recorded events are scored")
    print("per_mode: checked and not executed — no spectral object appears")
    print("lattice_wide: checked and not executed — only R is scored")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
