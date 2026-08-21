#!/usr/bin/env python3
"""Arrival-speed variance of opposite-lock formation ticks on B_3(0).

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and -e_1. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Uniqueness is not required. Variance is the population variance of
|x|_2/t on formed nonzero sites with t>0. No runner cache is written.
"""

from __future__ import annotations

import ast
from collections import defaultdict, deque
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_FORMATION_TICK_VAR_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_FORMATION_TICK_VAR_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NEG_E1: Point = (-1, 0, 0)
NN: tuple[Point, ...] = (
    E1,
    NEG_E1,
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)
BALL_SQ = 9
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
PERP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
ONE_SITE_SEEDS: tuple[tuple[Point, Point], ...] = ((ORIGIN, E1),)
UNFORMED_SITES = frozenset({(3, 0, 0), (-3, 0, 0), (0, 3, 0)})
TICK_COUNTS = {0: 1, 1: 6, 2: 16, 3: 28, 4: 41, 5: 27}
SECOND_MOMENT = Fraction(3817, 7080)
VAR_DENOM = 12531600
VAR_NUM = {
    1: 5333757,
    2: -719280,
    3: -454984,
    5: -354820,
    6: -381380,
    10: -173568,
    15: -45200,
    30: -87688,
}
MEAN_LINEAR = {
    1: Fraction(157, 708),
    2: Fraction(32, 295),
    3: Fraction(5, 177),
    5: Fraction(113, 1770),
    6: Fraction(97, 1770),
}
PERP_SECOND_MOMENT = Fraction(49223, 85680)
FORBIDDEN_NOTE_TOKENS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "B_12",
    "L1",
    "hop-cost",
    "parnn",
    "k20",
    "B_57",
)
CLAIM_SCOPE = (
    "Arrival-speed variance of nsopp formation-tick on formed nonzero "
    "sites of B_3(0) is reported. Displayed, not adopted."
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


def split_square(value: int) -> tuple[int, int]:
    """Write n = square^2 * square_free with square_free square-free."""
    square = 1
    rest = 1
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        square *= prime ** (exponent // 2)
        if exponent % 2:
            rest *= prime
        prime = prime + 1 if prime == 2 else prime + 2
    if remaining > 1:
        rest *= remaining
    return square, rest


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
    seeds: tuple[tuple[Point, Point], ...] = TWO_SITE_SEEDS,
    *,
    require_perp: bool = True,
) -> tuple[dict[Point, int], dict[Point, set[Point]]]:
    """Earliest formation ticks and possible incoming locks on B_3(0)."""
    ticks: dict[Point, int] = {site: 0 for site, _lock in seeds}
    locks: dict[Point, set[Point]] = {site: {lock} for site, lock in seeds}
    queue: deque[tuple[Point, int]] = deque((site, 0) for site, _lock in seeds)
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


def formed_nonzero(ticks: dict[Point, int]) -> dict[Point, int]:
    return {site: tick for site, tick in ticks.items() if site != ORIGIN}


def speed_sites(ticks: dict[Point, int]) -> dict[Point, int]:
    """Formed nonzero sites on which |x|_2/t is defined."""
    return {site: tick for site, tick in formed_nonzero(ticks).items() if tick > 0}


def second_moment_and_var_coeff(
    ticks: dict[Point, int],
) -> tuple[int, Fraction, dict[int, Fraction], dict[int, Fraction]]:
    """Population variance of |x|_2/t as square-free coefficients."""
    scored = speed_sites(ticks)
    count = len(scored)
    moment = Fraction(0)
    linear: dict[int, Fraction] = defaultdict(Fraction)
    for site, tick in scored.items():
        squared = dot(site, site)
        moment += Fraction(squared, tick * tick)
        square, square_free = split_square(squared)
        linear[square_free] += Fraction(square, tick)
    moment /= count
    mean_linear = {key: value / count for key, value in linear.items()}
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
    cleaned = {key: value for key, value in var_coeff.items() if value != 0}
    return count, moment, mean_linear, cleaned


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
    return f"{whole}.{frac[:places]}"


def tick_groups(nonzero: dict[Point, int]) -> dict[int, tuple[Point, ...]]:
    groups: dict[int, list[Point]] = defaultdict(list)
    for site, tick in nonzero.items():
        groups[tick].append(site)
    return {tick: tuple(sorted(sites)) for tick, sites in sorted(groups.items())}


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
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("opposite-lock formation-tick arrival-speed variance on formed B_3(0)")
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
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/OPPOSITE_LOCK_FORMATION_TICK_VAR_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )

    host = ball_sites()
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check("two-site-seed-in-host", {ORIGIN, E2} <= host)
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and add(NEG_E1, E1) == ORIGIN
        and add(ORIGIN, E2) == E2
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and perpendicular(NEG_E1, E2)
        and not perpendicular(E1, E1)
        and not perpendicular(NEG_E1, E1)
        and in_ball((1, 0, 0))
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "split-square-identity",
        split_square(1) == (1, 1)
        and split_square(2) == (1, 2)
        and split_square(4) == (2, 1)
        and split_square(8) == (2, 2)
        and split_square(9) == (3, 1)
        and split_square(12) == (2, 3),
    )

    ticks, locks = form()
    nonzero = formed_nonzero(ticks)
    scored = speed_sites(ticks)
    groups = tick_groups(nonzero)
    count, moment, mean_linear, var_coeff = second_moment_and_var_coeff(ticks)
    var_value = eval_coeff(var_coeff)
    var_text = truncated_decimal(var_value)

    print(f"N_formed_nonzero={len(nonzero)}")
    print(f"N_speed={count}")
    print(f"Q={moment}")
    print(f"var_truncated_18={var_text}")
    print(f"unformed={sorted(host - set(ticks))}")
    print(f"tick_counts={ {tick: len(sites) for tick, sites in groups.items()} }")
    print(f"locks(1,0,0)={sorted(locks.get((1, 0, 0), ()))}")

    checks.check(
        "seed-ticks-zero-locks-plus-e1-minus-e1",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and add(E1, NEG_E1) == ORIGIN
        and sum(time == 0 for time in ticks.values()) == 2,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "unformed-axis-and-plus-y-end",
        set(host) - set(ticks) == UNFORMED_SITES,
        str(sorted(set(host) - set(ticks))),
    )
    checks.check(
        "uniqueness-not-required",
        (1, 0, 0) in locks and len(locks[(1, 0, 0)]) > 1,
        str(sorted(locks.get((1, 0, 0), ()))),
    )
    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E2, step)) != 1 for step in (E1, NEG_E1)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and ticks[(0, -1, 0)] == 1
        and ticks[E3] == 1
        and ticks[(0, 0, -1)] == 1
        and ticks[(0, 2, 0)] == 1
        and locks[(0, 2, 0)] == {E2}
        and "s·e_i=0" in note.replace(" ", ""),
    )

    checks.check("theorem1-n-formed-nonzero", len(nonzero) == 119, str(len(nonzero)))
    checks.check("theorem1-origin-excluded", ORIGIN not in nonzero and ORIGIN in ticks)
    checks.check(
        "theorem1-second-seed-included-at-t0",
        E2 in nonzero and nonzero[E2] == 0,
    )
    checks.check(
        "theorem1-census-set-is-formed-nonzero",
        set(nonzero) == set(ticks) - {ORIGIN},
    )
    checks.check(
        "theorem1-tick-counts",
        {tick: len(sites) for tick, sites in groups.items()} == TICK_COUNTS
        and sum(TICK_COUNTS.values()) == 119,
        str({tick: len(sites) for tick, sites in groups.items()}),
    )
    checks.check(
        "theorem1-t0-only-second-seed",
        groups[0] == (E2,),
    )
    checks.check(
        "theorem1-axis-tick",
        nonzero[(1, 0, 0)] == 3 and nonzero[(2, 0, 0)] == 4 and nonzero[(1, 1, 0)] == 3,
    )
    checks.check(
        "theorem1-formed-plus-unformed-is-host",
        len(ticks) + len(UNFORMED_SITES) == len(host) == 123,
    )

    expected_var = {key: Fraction(num, VAR_DENOM) for key, num in VAR_NUM.items()}
    checks.check("theorem2-n-speed", count == 118, str(count))
    checks.check(
        "theorem2-second-seed-excluded-from-speed",
        E2 not in scored and ORIGIN not in scored and len(scored) == 118,
    )
    checks.check("theorem2-second-moment", moment == SECOND_MOMENT, str(moment))
    checks.check(
        "theorem2-mean-linear",
        mean_linear == MEAN_LINEAR,
        str(mean_linear),
    )
    checks.check(
        "theorem2-var-coeff",
        var_coeff == expected_var,
        str(var_coeff),
    )
    checks.check(
        "theorem2-var-not-rational",
        any(key != 1 for key in var_coeff) and 1 in var_coeff,
    )
    checks.check(
        "theorem2-truncated-18",
        var_text == "0.047614192437711682",
        var_text,
    )
    checks.check(
        "identity-var-equals-q-minus-mean-square",
        var_coeff[1] == moment - sum(
            MEAN_LINEAR[a] * MEAN_LINEAR[b] * split_square(a * b)[0]
            for a in MEAN_LINEAR
            for b in MEAN_LINEAR
            if split_square(a * b)[1] == 1
        ),
    )

    one_ticks, _ = form(seeds=ONE_SITE_SEEDS)
    one_count, one_moment, _one_mean, one_var = second_moment_and_var_coeff(one_ticks)
    checks.check(
        "cardinality-not-one-site-clone",
        len(formed_nonzero(one_ticks)) == 120
        and one_count == 120
        and one_moment != moment
        and one_var != var_coeff
        and len(nonzero) != 120,
        f"one N={one_count} Q={one_moment}",
    )

    perp_ticks, _ = form(seeds=PERP_SEEDS)
    perp_nonzero = formed_nonzero(perp_ticks)
    perp_count, perp_moment, _perp_mean, perp_var = second_moment_and_var_coeff(
        perp_ticks
    )
    checks.check(
        "not-perp-seed-variance-reprint",
        len(perp_nonzero) == 120
        and (0, 3, 0) in perp_ticks
        and perp_count == 119
        and perp_moment == PERP_SECOND_MOMENT
        and perp_var != var_coeff
        and (len(nonzero), count, moment) != (120, 119, PERP_SECOND_MOMENT),
        f"perp N_formed={len(perp_nonzero)} Q={perp_moment}",
    )

    free_ticks, _ = form(require_perp=False)
    free_n = len(formed_nonzero(free_ticks))
    checks.check(
        "mutation-drop-perp-changes-formed-count",
        free_n != len(nonzero),
        f"free N_formed_nonzero={free_n}",
    )
    checks.check(
        "q-is-euclidean-square-not-abs-sum",
        dot((2, 1, 0), (2, 1, 0)) == 5
        and (2, 1, 0) in nonzero
        and abs(2) + abs(1) + abs(0) != 5,
    )
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    two_site_var = second_moment_and_var_coeff(
        {(1, 0, 0): 1, (1, 1, 0): 1, ORIGIN: 0}
    )
    checks.check(
        "identity-two-equal-tick-speeds",
        two_site_var[0] == 2
        and two_site_var[1] == Fraction(3, 2)
        and two_site_var[2][1] == Fraction(1, 2)
        and two_site_var[2][2] == Fraction(1, 2),
        str(two_site_var[2]),
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-formed-count-and-ticks",
        "N_formed nonzero = 119" in note
        and "t=0 (1): (0,1,0)" in note
        and "t=1 (6):" in note
        and "t=5 (27):" in note
        and "1+6+16+28+41+27=119" in note,
    )
    checks.check(
        "note-reports-variance",
        "Q = 3817/7080" in note
        and "5333757 - 719280 sqrt(2)" in note
        and "12531600" in note
        and "var = 0.047614192437711682" in note
        and "157/708" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in note.lower()
        and "not written into Admissibility" in note,
    )
    checks.check(
        "note-cardinality-not-clone",
        "Cardinality-of-seed, not a 1-site clone" in note
        and "not a 1-site clone" in note,
    )
    checks.check(
        "note-not-perp-seed-reprint",
        "not a reprint of the perp two-site formation-tick variance" in note
        and "49223/85680" in note
        and "N_formed nonzero = 120" not in note.replace(
            "The perp two-site seed `+e_1/+e_2` forms 120 nonzero sites", ""
        ),
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in note
        and "B_3(0)" in note
        and "No runner cache is written." in note,
    )
    checks.check(
        "note-does-not-attach-formation-member",
        "does not attach a formation member" in note.lower()
        and "Do not attach" not in note,
    )
    checks.check(
        "note-forbidden-tokens-absent",
        all(token not in note for token in FORBIDDEN_NOTE_TOKENS),
    )
    checks.check(
        "axiom-record-sentences-current",
        "Records form." in axiom
        and "When present, a record locks exactly one admissible local possibility."
        in axiom
        and "Physical sites are the points of the cubic lattice `Z^3`" in axiom
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom
        and "does not supply the formation site, probability, or rate"
        in " ".join(axiom.split()),
    )
    checks.check(
        "note-quotes-current-premises",
        "Physical sites are the points of the cubic lattice `Z^3`" in note
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in note
        and "When present, a record locks exactly one admissible local possibility."
        in note
        and "does not supply the formation site, probability, or rate"
        in " ".join(note.split()),
    )
    checks.check(
        "note-machine-status-no-axiom-edit",
        'hypothetical_axiom_status: "no edit"' in note
        and "claim_type: bounded_theorem" in note
        and "authors no audit verdict" in note,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and "def second_moment_and_var_coeff(" in source
        and set(ticks) <= host,
    )
    print("per_element: |x|_2/t at each formed nonzero site with t>0")
    print("per_site: scored on Euclidean B_3(0) formed nonzero sites only")
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print("per_block: one population variance of arrival speed")
    print(
        "lattice_wide: checked and not executed — no lattice-wide speed law is claimed"
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
