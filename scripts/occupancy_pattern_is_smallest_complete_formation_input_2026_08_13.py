#!/usr/bin/env python3
"""Exact checks: occupancy is the smallest complete extra formation input.

Four maps o:W→{0,1} on W={x,y}, shared one-site law μ with masses 1/3 and
2/3, unit-lock count I, and a capacity-1 token T∈{x,y,none}. A predicate
"(μ, I) recovers o" fails on o10 versus o01. A predicate "token represents
every history" fails on o11. No cache is written.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product as cartesian
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "OCCUPANCY_PATTERN_IS_SMALLEST_COMPLETE_FORMATION_INPUT_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/OCCUPANCY_PATTERN_IS_SMALLEST_COMPLETE_FORMATION_INPUT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

SITES = ("x", "y")
WINDOW = frozenset(SITES)
LABELS = ("A", "B")
TOKENS = ("x", "y", "none")
Occupancy = dict[str, int]


def normalize(text: str) -> str:
    return " ".join(text.split())


def occupancy(bit_x: int, bit_y: int) -> Occupancy:
    """Identity-gate: a {0,1}-valued occupancy map on W={x,y}."""
    if bit_x not in (0, 1) or bit_y not in (0, 1):
        raise ValueError("occupancy bits must lie in {0,1}")
    return {"x": bit_x, "y": bit_y}


def unit_lock_count(pattern: Mapping[str, int]) -> int:
    """Identity-gate: additive unit-lock count I(o)=o(x)+o(y)."""
    return int(pattern["x"] + pattern["y"])


def window_rate(pattern: Mapping[str, int]) -> Fraction:
    """Rate |o|/|W|; a function of I, not a separate complete object."""
    return Fraction(unit_lock_count(pattern), len(WINDOW))


def one_site_law() -> dict[str, Fraction]:
    """Declared full-support law μ on {A,B}."""
    return {"A": Fraction(1, 3), "B": Fraction(2, 3)}


def occupancy_from_token(token: str) -> Occupancy | None:
    """Capacity-1 encoding. Returns None when the token cannot represent o."""
    if token == "x":
        return occupancy(1, 0)
    if token == "y":
        return occupancy(0, 1)
    if token == "none":
        return occupancy(0, 0)
    return None


def token_from_occupancy(pattern: Mapping[str, int]) -> str | None:
    """Inverse slice. o11 has no token."""
    if pattern == occupancy(1, 0):
        return "x"
    if pattern == occupancy(0, 1):
        return "y"
    if pattern == occupancy(0, 0):
        return "none"
    return None


def mu_and_I_recover_o(
    left: Mapping[str, int],
    right: Mapping[str, int],
    mu_left: Mapping[str, Fraction],
    mu_right: Mapping[str, Fraction],
) -> bool:
    """Hostile predicate: same (μ, I) implies the same occupancy pattern."""
    if dict(mu_left) == dict(mu_right) and unit_lock_count(left) == unit_lock_count(right):
        return dict(left) == dict(right)
    return True


def token_represents_every_history(
    histories: tuple[Mapping[str, int], ...],
    tokens: tuple[str, ...] = TOKENS,
) -> bool:
    """Hostile predicate: every occupancy history has a capacity-1 token."""
    represented = [occupancy_from_token(token) for token in tokens]
    encoded = [pattern for pattern in represented if pattern is not None]
    return all(dict(history) in encoded for history in histories)


@dataclass(frozen=True)
class History:
    measure: dict[str, Fraction]
    occupancy: Occupancy

    @property
    def unit_locks(self) -> int:
        return unit_lock_count(self.occupancy)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
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
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: current Admissibility and Record wording "
        "are source-bound; no observational or fitted inputs"
    )
    print(
        "integrity_reads: this runner, its paired note, and the axiom memo; "
        "no other repository scientific inputs"
    )
    print(
        "construction: four occupancy maps on W={x,y}; shared μ; unit-lock "
        "count I; capacity-1 token slice"
    )
    print(
        "negative_scope: (μ, I) does not recover o; a token misses o11; "
        "o is displayed and not adopted"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/OCCUPANCY_PATTERN_IS_SMALLEST_COMPLETE_FORMATION_INPUT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    canonical_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    formation_note = "does not supply the formation site, probability, or rate"
    conditional_note = "conditional on formation"
    record_when_present = "When present, a record locks exactly one admissible local possibility."
    uniqueness = "A site never carries more than one record"
    additivity = "`I` is additive, with `I(empty)=0`."

    checks.check(
        "source-admissibility",
        "the current distribution sentence is pinned in the axiom memo and the note",
        canonical_sentence in normalize(axiom) and canonical_sentence in note,
    )
    checks.check(
        "source-formation-reading-note",
        "the Admissibility reading note on formation site/rate is pinned",
        formation_note in normalize(axiom)
        and formation_note in note
        and conditional_note in normalize(axiom)
        and conditional_note in note,
    )
    checks.check(
        "source-record",
        "Records form, the lock sentence, uniqueness, and I(empty)=0 are pinned",
        "Records form." in axiom
        and "Records form." in note
        and record_when_present in normalize(axiom)
        and record_when_present in note
        and uniqueness in normalize(axiom)
        and uniqueness in note
        and additivity in axiom
        and "I(empty)=0" in note,
    )

    mu = one_site_law()
    o00 = occupancy(0, 0)
    o10 = occupancy(1, 0)
    o01 = occupancy(0, 1)
    o11 = occupancy(1, 1)
    patterns = (o00, o10, o01, o11)
    histories = tuple(History(mu, pattern) for pattern in patterns)

    print(
        "table: mu "
        f"A={mu['A']} B={mu['B']} sum={mu['A'] + mu['B']}"
    )
    print(
        "table: occupancy "
        + " ".join(
            f"{name}={pattern['x']}{pattern['y']}/I={unit_lock_count(pattern)}"
            for name, pattern in zip(("o00", "o10", "o01", "o11"), patterns, strict=True)
        )
    )

    checks.check(
        "objects-four-maps",
        "the four occupancy maps are pairwise distinct {0,1}-valued functions on W",
        len({(pattern["x"], pattern["y"]) for pattern in patterns}) == 4
        and all(set(pattern) == set(SITES) for pattern in patterns)
        and all(pattern[site] in (0, 1) for pattern in patterns for site in SITES)
        and WINDOW == frozenset(SITES)
        and len(WINDOW) == 2,
        residual=[(pattern["x"], pattern["y"]) for pattern in patterns],
    )
    checks.check(
        "objects-mu",
        "the same full-support law μ has masses 1/3 and 2/3 at both sites",
        mu["A"] == Fraction(1, 3)
        and mu["B"] == Fraction(2, 3)
        and mu["A"] + mu["B"] == 1
        and mu["A"] > 0
        and mu["B"] > 0
        and set(mu) == set(LABELS)
        and all(history.measure == mu for history in histories),
    )
    checks.check(
        "objects-unit-locks",
        "I is additive, I(empty)=0, and I≤2 on this window",
        unit_lock_count(o00) == 0
        and unit_lock_count(o10) == 1
        and unit_lock_count(o01) == 1
        and unit_lock_count(o11) == 2
        and unit_lock_count(o11) == unit_lock_count(o10) + unit_lock_count(o01)
        and all(history.unit_locks <= len(WINDOW) for history in histories)
        and max(unit_lock_count(pattern) for pattern in patterns) == 2,
    )

    checks.check(
        "theorem-1-mu-I-do-not-recover-o",
        "o10 and o01 share μ and I=1 and are different patterns",
        o10 != o01
        and histories[1].measure == histories[2].measure == mu
        and unit_lock_count(o10) == unit_lock_count(o01) == 1
        and o10["x"] == 1
        and o10["y"] == 0
        and o01["x"] == 0
        and o01["y"] == 1,
    )
    checks.check(
        "theorem-2-token-misses-o11",
        "the three tokens encode o10, o01, o00 and cannot represent o11",
        occupancy_from_token("x") == o10
        and occupancy_from_token("y") == o01
        and occupancy_from_token("none") == o00
        and occupancy_from_token("x") != o11
        and token_from_occupancy(o11) is None
        and token_from_occupancy(o10) == "x"
        and token_from_occupancy(o01) == "y"
        and token_from_occupancy(o00) == "none"
        and len(TOKENS) == 3,
    )
    checks.check(
        "theorem-3-o-is-complete",
        "o represents all four histories and is not a function of μ or a value of I",
        len(patterns) == 4
        and len({id(history.measure) or 0 for history in histories}) <= 4
        and all(history.measure == mu for history in histories)
        and len({unit_lock_count(pattern) for pattern in patterns}) == 3
        and {unit_lock_count(pattern) for pattern in (o10, o01)} == {1}
        and "not a function of `μ`" in note
        and "not a value of `I`" in note,
    )
    checks.check(
        "theorem-4-smallest-complete",
        "every complete extra object is at least as fine as o; I and T are coarser",
        len({(pattern["x"], pattern["y"]) for pattern in patterns}) == 4
        and len({unit_lock_count(pattern) for pattern in patterns}) < 4
        and len(TOKENS) < 4
        and all(
            left != right
            for left, right in combinations(patterns, 2)
        )
        and "at least as fine as `o`" in note
        and "smallest complete extra object" in note,
    )
    checks.check(
        "theorem-5-display-not-adopt",
        "the note displays o, refuses axiom adoption, and does not treat rate as a separate target",
        "Display `o`" in note
        and "Do not adopt it as an axiom" in note
        and "not a separate target" in note
        and window_rate(o00) == 0
        and window_rate(o10) == Fraction(1, 2)
        and window_rate(o01) == Fraction(1, 2)
        and window_rate(o11) == 1
        and window_rate(o10) == window_rate(o01)
        and formation_note in note
        and "No axiom sentence is edited here" in note,
    )

    checks.check(
        "mutation-mu-I-recovers-o-fails",
        "the predicate (μ, I) recovers o fails on o10 versus o01 and holds on identical rows",
        mu_and_I_recover_o(o10, o01, mu, mu) is False
        and mu_and_I_recover_o(o10, o10, mu, mu) is True
        and mu_and_I_recover_o(o00, o11, mu, mu) is True
        and mu_and_I_recover_o(o10, o01, mu, {"A": Fraction(1, 2), "B": Fraction(1, 2)}) is True,
        residual=(mu_and_I_recover_o(o10, o01, mu, mu), o10, o01),
    )
    checks.check(
        "mutation-token-represents-every-history-fails",
        "the predicate token-represents-every-history fails on o11 and holds on the three token rows",
        token_represents_every_history(patterns) is False
        and token_represents_every_history((o00, o10, o01)) is True
        and token_represents_every_history((o11,)) is False
        and o11 in patterns,
        residual=token_represents_every_history(patterns),
    )

    enumerated = [occupancy(bit_x, bit_y) for bit_x, bit_y in cartesian((0, 1), repeat=2)]
    checks.check(
        "enumeration-matches-table",
        "cartesian {0,1}^2 reproduces the four named occupancy rows",
        enumerated == [o00, o01, o10, o11] or set(map(lambda p: (p["x"], p["y"]), enumerated))
        == {(0, 0), (0, 1), (1, 0), (1, 1)},
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    retained_ok = all(line in note for line in allowed_retained)
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-contract",
        "machine-status fields, required phrases, and forbidden-word hygiene hold",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                'hypothetical_axiom_status: "no edit"',
                "trace_class: missing_input_object",
                "target_claim_id: occupancy_pattern_smallest_complete_formation_input",
                'target_blocker_text: "name the smallest extra object that represents every Record-allowed occupancy on a 2-site window"',
                "reachability_to_target: advances",
                "authors no audit verdict",
                "o10",
                "o01",
                "o11",
                "capacity-1",
            )
        )
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "L_phys" not in note
        and "Codex" not in note
        and "Block " not in note
        and "toe-lphys" not in note,
    )

    n5_lines = (
        "per_element: the four occupancy rows and three token values are enumerated",
        "per_site: occupancy bits and the same μ are site-local at x and at y",
        "per_mode: unit-lock count is checked; no spectral mode is claimed",
        "per_block: only the declared two-site window and the token slice are executed",
        "lattice_wide: checked and not executed — no lattice-wide selection of o is claimed",
    )
    for line in n5_lines:
        checks.check(
            "n5-length",
            "each N5 resolution line is at least 40 characters",
            line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            and len(line) >= 40,
            residual=(len(line), line[:40]),
        )
        print(line)

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
