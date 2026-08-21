#!/usr/bin/env python3
"""Perpnn formation-tick arrival-speed variance on B_3(0).

Finite host: Euclidean ball of radius 3 centered at the origin. Seed lock at
the origin is +e_1. A 6-NN step is allowed iff it is perpendicular to the
parent lock axis. Newly formed sites lock the incoming step. Variance is
population var(|x|_2/t) on formed nonzero sites. Uniqueness is not required.
"""

from __future__ import annotations

import ast
from collections import Counter, defaultdict, deque
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/PERPNN_FORMATION_TICK_VAR_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/PERPNN_FORMATION_TICK_VAR_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

CLAIM_SCOPE = (
    "Arrival-speed variance of perpnn formation-tick on formed "
    "nonzero sites of B_3(0) is reported. Displayed, not adopted."
)

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NN: tuple[Point, ...] = (
    E1,
    (-1, 0, 0),
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)
BALL_SQ = 9
FORMED_NONZERO = 120
Q_EXPECTED = Fraction(22481, 54000)
VAR_DIGITS = "0.012492962195816963"
TICK_COUNTS = {1: 4, 2: 12, 3: 26, 4: 42, 5: 36}
UNFORMED = frozenset({(3, 0, 0), (-3, 0, 0)})
FORBIDDEN_NOTE_TOKENS = (
    "G_" "N",
    "1/" "r",
    "1/" "r^2",
    "Lattice-" "named",
    "not a " "TOE",
    "Dijk" "stra",
    "B_" "12",
)


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]


def in_ball(site: Point) -> bool:
    return dot(site, site) <= BALL_SQ


def ball_sites() -> frozenset[Point]:
    return frozenset(
        (x, y, z)
        for x in range(-3, 4)
        for y in range(-3, 4)
        for z in range(-3, 4)
        if in_ball((x, y, z))
    )


def perpendicular(lock: Point, step: Point) -> bool:
    return dot(lock, step) == 0


def normalize(text: str) -> str:
    return " ".join(text.split())


def assignment_string_tuple(tree: ast.AST, name: str) -> tuple[str, ...] | None:
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == name:
                try:
                    value = ast.literal_eval(node.value)
                except (ValueError, TypeError):
                    return None
                if isinstance(value, tuple) and all(
                    isinstance(item, str) for item in value
                ):
                    return value
                return None
    return None


def form(
    seed_lock: Point = E1,
    *,
    require_perp: bool = True,
) -> tuple[dict[Point, int], dict[Point, set[Point]]]:
    """Earliest formation ticks and possible incoming locks on B_3(0)."""
    ticks: dict[Point, int] = {ORIGIN: 0}
    locks: dict[Point, set[Point]] = {ORIGIN: {seed_lock}}
    queue: deque[tuple[Point, int]] = deque([(ORIGIN, 0)])
    while queue:
        parent, parent_tick = queue.popleft()
        for lock in tuple(locks[parent]):
            for step in NN:
                if require_perp and not perpendicular(lock, step):
                    continue
                child = add(parent, step)
                if not in_ball(child):
                    continue
                next_tick = parent_tick + 1
                if child not in ticks:
                    ticks[child] = next_tick
                    locks[child] = {step}
                    queue.append((child, next_tick))
                elif ticks[child] == next_tick:
                    locks[child].add(step)
    return ticks, locks


def split_square(value: int) -> tuple[int, int]:
    square = 1
    square_free = 1
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            square *= prime ** (exponent // 2)
            if exponent % 2:
                square_free *= prime
        prime += 1 if prime == 2 else 2
    if remaining > 1:
        square_free *= remaining
    return square, square_free


def second_moment_and_var_coeff(
    ticks: dict[Point, int],
) -> tuple[Fraction, dict[int, Fraction]]:
    nonzero = tuple(site for site in ticks if site != ORIGIN)
    count = len(nonzero)
    moment = Fraction(0)
    linear: dict[int, Fraction] = defaultdict(Fraction)
    for site in nonzero:
        arrival = ticks[site]
        squared = dot(site, site)
        moment += Fraction(squared, arrival * arrival)
        square, square_free = split_square(squared)
        linear[square_free] += Fraction(square, arrival)
    moment /= count
    square_coeff: dict[int, Fraction] = defaultdict(Fraction)
    keys = tuple(linear)
    for left in keys:
        for right in keys:
            square, square_free = split_square(left * right)
            square_coeff[square_free] += linear[left] * linear[right] * square
    var_coeff: dict[int, Fraction] = defaultdict(Fraction)
    var_coeff[1] += moment
    denom = count * count
    for square_free, coeff in square_coeff.items():
        var_coeff[square_free] -= coeff / denom
    return moment, {key: value for key, value in var_coeff.items() if value != 0}


def eval_coeff(coeff: dict[int, Fraction], precision: int = 50) -> Decimal:
    getcontext().prec = precision
    total = Decimal(0)
    for square_free, value in coeff.items():
        total += (Decimal(value.numerator) / Decimal(value.denominator)) * Decimal(
            square_free
        ).sqrt()
    return total


def truncated_decimal(value: Decimal, places: int = 18) -> str:
    quantized = value.quantize(Decimal(10) ** -places)
    text = format(quantized, "f")
    whole, frac = text.split(".")
    return whole + "." + frac[:places]


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
    source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("perpnn formation-tick arrival-speed variance on B_3(0)")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"claim_scope: {CLAIM_SCOPE}")

    checks.check(
        "audit-input-paths-literal",
        literal_paths == AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL),
        str(literal_paths),
    )
    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)

    host = ball_sites()
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)

    ticks, locks = form()
    formed_nonzero = frozenset(site for site in ticks if site != ORIGIN)
    unformed = host - frozenset(ticks)
    tick_hist = Counter(ticks[site] for site in formed_nonzero)

    print(f"formed_nonzero={len(formed_nonzero)} unformed={sorted(unformed)}")
    print(f"tick_histogram={dict(sorted(tick_hist.items()))}")

    checks.check(
        "theorem1-formed-nonzero-set",
        formed_nonzero == host - {ORIGIN} - UNFORMED
        and len(formed_nonzero) == FORMED_NONZERO
        and unformed == UNFORMED,
        f"n={len(formed_nonzero)} unformed={sorted(unformed)}",
    )
    checks.check(
        "theorem1-tick-histogram",
        dict(tick_hist) == TICK_COUNTS,
        str(dict(sorted(tick_hist.items()))),
    )
    checks.check(
        "theorem1-note-reports-set",
        "B_3(0) \\ { (0,0,0), (3,0,0), (-3,0,0) }" in note
        and "unformed = {(3,0,0), (-3,0,0)}" in note
        and "(t, count) = (1,4), (2,12), (3,26), (4,42), (5,36)" in note
        and "t(1,0,0)=3" in note,
    )
    checks.check(
        "theorem1-uniqueness-not-required",
        ticks[(1, 0, 0)] == 3 and len(locks[(1, 0, 0)]) == 4,
        str(sorted(locks.get((1, 0, 0), ()))),
    )
    checks.check(
        "theorem1-not-hop-count",
        ticks[(1, 0, 0)] != 1 and ticks[(2, 0, 0)] != 2,
    )

    moment, var_coeff = second_moment_and_var_coeff(ticks)
    variance = eval_coeff(var_coeff)
    var_text = truncated_decimal(variance)
    print(f"Q={moment}")
    print(f"var={var_text}")

    expected_coeff = {
        1: Fraction(347297, 1080000),
        2: Fraction(-427, 9000),
        3: Fraction(-1177, 40500),
        5: Fraction(-4771, 202500),
        6: Fraction(-149, 6000),
        10: Fraction(-13, 1125),
        15: Fraction(-26, 10125),
        30: Fraction(-13, 2250),
    }
    checks.check(
        "theorem2-second-moment",
        moment == Q_EXPECTED and "22481/54000" in note,
        str(moment),
    )
    checks.check(
        "theorem2-exact-var-coeff",
        var_coeff == expected_coeff
        and "347297/1080000" in note
        and "(427/9000) sqrt(2)" in note,
    )
    checks.check(
        "theorem2-truncated-variance",
        var_text == VAR_DIGITS and VAR_DIGITS in note,
        var_text,
    )
    occupancy = Counter((dot(site, site), ticks[site]) for site in formed_nonzero)
    checks.check(
        "theorem2-occupancy",
        dict(occupancy)
        == {
            (1, 1): 4,
            (1, 3): 2,
            (2, 2): 12,
            (3, 3): 8,
            (4, 4): 6,
            (5, 3): 16,
            (5, 5): 8,
            (6, 4): 24,
            (8, 4): 12,
            (9, 5): 28,
        }
        and "(9,5):28" in note.replace(" ", ""),
    )

    free_ticks, _ = form(require_perp=False)
    checks.check(
        "mutation-drop-perp-forms-seed-axis-radius-3",
        (3, 0, 0) in free_ticks
        and (-3, 0, 0) in free_ticks
        and free_ticks[(3, 0, 0)] == 3
        and free_ticks[(1, 0, 0)] == 1
        and len(free_ticks) == 123,
        f"free_n={len(free_ticks)} t300={free_ticks.get((3, 0, 0))}",
    )
    checks.check(
        "seed-origin-tick-zero-lock-plus-e1",
        ticks[ORIGIN] == 0 and locks[ORIGIN] == {E1},
    )
    checks.check(
        "formation-stays-in-host",
        set(ticks) <= host,
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in note.lower()
        and "Displayed, not adopted." in note
        and "Do not write the variance" in note,
    )
    checks.check(
        "no-admissibility-write",
        "Do not write the variance, the formation tick, or the perp-step incoming-lock"
        in note
        and "one fixed nearest-neighbor admissibility rule" in axiom
        and "hypothetical_axiom_status: no edit" in note,
    )
    checks.check(
        "no-l1-attach",
        "Do not attach L1." in note and "This note does not attach L1" not in axiom,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in note
        and "B_3(0)" in note
        and "No runner cache is written." in note,
    )
    checks.check(
        "note-forbidden-tokens-absent",
        all(token not in note and token not in source for token in FORBIDDEN_NOTE_TOKENS),
    )
    checks.check(
        "axiom-record-sentences-current",
        "Records form." in axiom
        and "When present, a record locks exactly one admissible local possibility."
        in axiom
        and "Physical sites are the points of the cubic lattice `Z^3`" in axiom
        and "does not supply the formation site, probability, or rate" in normalized_axiom
        and "A readout value is determined by record content alone." in normalized_axiom
        and "A site with no record cannot be read." in axiom,
    )
    checks.check(
        "note-pins-axiom-wording",
        "Physical sites are the points of the cubic lattice `Z^3`" in note
        and "does not supply the formation site, probability, or rate" in normalized_note
        and "When present, a record locks exactly one admissible local possibility."
        in note
        and "A readout value is determined by record content alone." in note
        and "A site with no record cannot be read." in note,
    )
    checks.check(
        "note-machine-status-no-axiom-edit",
        "hypothetical_axiom_status: no edit" in note
        and "claim_type: bounded_theorem" in note,
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/PERPNN_FORMATION_TICK_VAR_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
