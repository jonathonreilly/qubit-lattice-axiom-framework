#!/usr/bin/env python3
"""Own incoming set exist-choice Cl(3,0) reverse/face on #7175 Q and R.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0), (0,-1,0)} with locks +e_1, -e_1, and -e_1 (nsyopp #7132;
same process as nsyopinc #7175). A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters as a singleton. M(q) is the set of
earliest incoming NN steps at q. Mixed stays a set. Unformed is UNDEFINED.
Identify ±e_i with generators γ_i of displayed Cl(3,0): γ_i²=+1,
γ_i γ_j=−γ_j γ_i (i≠j); −e_i maps to −γ_i. Displayed algebra, not a
cube-Pauli Lattice action. At a 4-cycle V, a pick is one letter from each
M(vi) at that site's own t (no T_Q). U is the Cl(3,0) product of the four
picked units. Exist-choice HOLD iff some pick has U equal to the scalar ±1.
If any vertex is unformed or M UNDEFINED or empty, the report is UNDEFINED.
Else fail. Unique-L product is comparison only. Unique L is UNDEFINED when
mixed. The 6-NN star S^+ is not the letter. Occupancy n is not used.
Named-sign lettering is not used. No unique P_+. Uniqueness of incoming
locks is not required. Independent of nmclopp #7167. No larger ball.
"""

from __future__ import annotations

import ast
from collections import deque
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/Y_SYMMETRIC_THREE_SITE_OWN_INCOMING_SET_CLIFFORD_EXIST_CHOICE_PLAQUETTE_PRODUCT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/Y_SYMMETRIC_THREE_SITE_OWN_INCOMING_SET_CLIFFORD_EXIST_CHOICE_PLAQUETTE_PRODUCT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Letter = Point | str
Incoming = frozenset[Point] | str
Clifford = tuple[int, int, int, int, int, int, int, int]
ORIGIN: Point = (0, 0, 0)
ZERO: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NEG_E1: Point = (-1, 0, 0)
NEG_E2: Point = (0, -1, 0)
NEG_E3: Point = (0, 0, -1)
NN: tuple[Point, ...] = (
    E1,
    NEG_E1,
    E2,
    NEG_E2,
    E3,
    NEG_E3,
)
POSITIVE_LOCKS = frozenset({E1, E2, E3})
NEGATIVE_LOCKS = frozenset({NEG_E1, NEG_E2, NEG_E3})
BALL_SQ = 9
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
PERP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
Z_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
    (NEG_E3, NEG_E1),
)
NSTRI_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E1, E2),
)
Y_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (NEG_E2, NEG_E1),
)
PROBES = {
    "A": (0, 1, 0),
    "B": (1, 1, 1),
    "C": (0, 2, 0),
    "D": (1, 1, 0),
}
Q_CYCLE: tuple[Point, ...] = (ORIGIN, E1, (1, 1, 0), E2)
R_CYCLE: tuple[Point, ...] = (E2, (1, 1, 0), (1, 1, 1), (0, 1, 1))
LOCK_NAME = {
    E1: "+e_1",
    NEG_E1: "−e_1",
    E2: "+e_2",
    NEG_E2: "−e_2",
    E3: "+e_3",
    NEG_E3: "−e_3",
}
CLIFFORD_NAMES = (
    "1",
    "γ_1",
    "γ_2",
    "γ_3",
    "γ_1γ_2",
    "γ_1γ_3",
    "γ_2γ_3",
    "γ_1γ_2γ_3",
)
MASK_TO_INDEX = {0: 0, 1: 1, 2: 2, 4: 3, 3: 4, 5: 5, 6: 6, 7: 7}
INDEX_TO_MASK = {0: 0, 1: 1, 2: 2, 3: 4, 4: 3, 5: 5, 6: 6, 7: 7}
SCALAR_ONE: Clifford = (1, 0, 0, 0, 0, 0, 0, 0)
SCALAR_MINUS: Clifford = (-1, 0, 0, 0, 0, 0, 0, 0)
FORBIDDEN_NOTE_TOKENS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "Gram",
    "16-census",
    "16-letter",
    "Runner cache",
    "f(n)",
    "ndot",
    "P_+",
)
CLAIM_SCOPE = (
    "Reverse and face from exist-choice Cl(3,0) 4-cycle products "
    "of own incoming sets on #7175 Q and R are reported. No S⁺. "
    "Displayed, not adopted."
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


def named_sign(lock: Point) -> str:
    """Named sign of a lock vector. Contrast only; not the scored predicate."""
    if lock in POSITIVE_LOCKS:
        return "+"
    if lock in NEGATIVE_LOCKS:
        return "-"
    raise ValueError(f"lock is not a six-neighbor step: {lock!r}")


def own_incoming_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> Incoming:
    """Earliest incoming NN steps at site. Seeds are a singleton. Unformed is UNDEFINED."""
    if site not in ticks:
        return "UNDEFINED"
    return frozenset(locks[site])


def unique_own_incoming_letter(incoming: Incoming) -> Letter:
    """Unique-L leftover: UNDEFINED when mixed. Comparison only; not this letter."""
    if incoming == "UNDEFINED":
        return "UNDEFINED"
    unique = set(incoming)
    if len(unique) != 1:
        return "UNDEFINED"
    vector = next(iter(unique))
    if vector not in NN:
        return "UNDEFINED"
    return vector


def mul_masks(sign_left: int, mask_left: int, sign_right: int, mask_right: int) -> tuple[int, int]:
    """Multiply two Cl(3,0) blades stored as (sign, generator bitmask)."""
    sign = sign_left * sign_right
    mask = mask_left
    for axis in range(3):
        bit = 1 << axis
        if mask_right & bit:
            swaps = 0
            for higher in range(axis + 1, 3):
                if mask & (1 << higher):
                    swaps += 1
            sign *= -1 if swaps % 2 else 1
            mask ^= bit
    return sign, mask


def clifford_from_blade(sign: int, mask: int) -> Clifford:
    coeffs = [0, 0, 0, 0, 0, 0, 0, 0]
    coeffs[MASK_TO_INDEX[mask]] = sign
    return (
        coeffs[0],
        coeffs[1],
        coeffs[2],
        coeffs[3],
        coeffs[4],
        coeffs[5],
        coeffs[6],
        coeffs[7],
    )


def clifford_mul(left: Clifford, right: Clifford) -> Clifford:
    out = [0, 0, 0, 0, 0, 0, 0, 0]
    for i, coeff_left in enumerate(left):
        if coeff_left == 0:
            continue
        for j, coeff_right in enumerate(right):
            if coeff_right == 0:
                continue
            sign, mask = mul_masks(
                coeff_left,
                INDEX_TO_MASK[i],
                coeff_right,
                INDEX_TO_MASK[j],
            )
            out[MASK_TO_INDEX[mask]] += sign
    return (
        out[0],
        out[1],
        out[2],
        out[3],
        out[4],
        out[5],
        out[6],
        out[7],
    )


def clifford_unit(lock: Point) -> Clifford:
    """Map ±e_i to ±γ_i in displayed Cl(3,0)."""
    if lock not in NN:
        raise ValueError(f"lock is not a six-neighbor step: {lock!r}")
    sign = 1 if lock in POSITIVE_LOCKS else -1
    axis = abs(lock[0]) * 0 + abs(lock[1]) * 1 + abs(lock[2]) * 2
    return clifford_from_blade(sign, 1 << axis)


def clifford_neg(element: Clifford) -> Clifford:
    return (
        -element[0],
        -element[1],
        -element[2],
        -element[3],
        -element[4],
        -element[5],
        -element[6],
        -element[7],
    )


def is_scalar_pm1(element: Clifford) -> bool:
    return element in (SCALAR_ONE, SCALAR_MINUS)


def clifford_display(element: Clifford) -> str:
    if element == SCALAR_ONE:
        return "+1"
    if element == SCALAR_MINUS:
        return "−1"
    parts: list[str] = []
    for coeff, name in zip(element, CLIFFORD_NAMES):
        if coeff == 0:
            continue
        if coeff == 1:
            parts.append(name)
        elif coeff == -1:
            parts.append("−" + name)
        else:
            parts.append(f"{coeff}{name}")
    return "+".join(parts).replace("+−", "−") or "0"


def product_U(pick: tuple[Point, ...]) -> Clifford:
    """Cl(3,0) product of the four picked units in cyclic order."""
    total = SCALAR_ONE
    for letter in pick:
        total = clifford_mul(total, clifford_unit(letter))
    return total


def exist_choice(
    incoming: tuple[Incoming, ...],
) -> tuple[str, int, int]:
    """Hold iff some pick has U equal to the scalar ±1.

    Unformed, UNDEFINED, or empty at any vertex is UNDEFINED. Else fail.
    Uniqueness is not required. Mixed stays a set.
    """
    if any(
        item == "UNDEFINED" or not isinstance(item, frozenset) or not item
        for item in incoming
    ):
        return "UNDEFINED", 0, 0
    n_picks = 0
    n_hold = 0
    for pick in product(*incoming):
        n_picks += 1
        if is_scalar_pm1(product_U(tuple(pick))):
            n_hold += 1
    if n_hold > 0:
        return "hold", n_picks, n_hold
    return "fail", n_picks, n_hold


def reverse_report(incoming: tuple[Incoming, ...]) -> str:
    """Reverse exist-choice on the four R vertices."""
    status, _n_picks, _n_hold = exist_choice(incoming)
    return status


def face_report(incoming: tuple[Incoming, ...]) -> str:
    """Face exist-choice on the four Q vertices."""
    status, _n_picks, _n_hold = exist_choice(incoming)
    return status


def unique_l_product(incoming: tuple[Incoming, ...]) -> Clifford | str:
    """Unique-L leftover product. Mixed vertex => UNDEFINED. Comparison only."""
    letters = tuple(unique_own_incoming_letter(item) for item in incoming)
    if any(letter == "UNDEFINED" or not isinstance(letter, tuple) for letter in letters):
        return "UNDEFINED"
    return product_U(tuple(letters))  # type: ignore[arg-type]


def set_display(locks: Incoming) -> str:
    if locks == "UNDEFINED":
        return "UNDEFINED"
    if not locks:
        return "{}"
    names = ", ".join(LOCK_NAME[lock] for lock in NN if lock in locks)
    return "{" + names + "}"


def letter_display(letter: Letter) -> str:
    if letter == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(letter, tuple):
        raise TypeError(f"letter is not a lock vector: {letter!r}")
    return LOCK_NAME[letter]


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
    seeds: tuple[tuple[Point, Point], ...] = Y_SYMMETRIC_SEEDS,
    *,
    require_perp: bool = True,
) -> tuple[dict[Point, int], dict[Point, set[Point]]]:
    """Earliest formation ticks and incoming locks on B_3(0)."""
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


def cycle_incoming(
    cycle: tuple[Point, ...],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> tuple[Incoming, ...]:
    return tuple(own_incoming_set(site, ticks, locks) for site in cycle)


def sum_of_set(locks: Incoming) -> Point | str:
    """Z^3 sum leftover of a lock set. Contrast only; not this letter."""
    if locks == "UNDEFINED":
        return "UNDEFINED"
    total = ZERO
    for lock in locks:
        total = add(total, lock)
    return total


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
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("own incoming set exist-choice Cl(3,0) reverse/face on #7175 Q and R")
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
    checks.check(
        "q-and-r-in-host",
        set(Q_CYCLE) <= host
        and set(R_CYCLE) <= host
        and Q_CYCLE == (ORIGIN, E1, (1, 1, 0), E2)
        and R_CYCLE == (E2, (1, 1, 0), (1, 1, 1), (0, 1, 1))
        and PROBES["A"] in R_CYCLE
        and PROBES["B"] in R_CYCLE
        and PROBES["A"] in Q_CYCLE
        and ORIGIN in Q_CYCLE,
    )
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and add(NEG_E1, E1) == ZERO
        and add(E1, E2) == (1, 1, 0)
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    g1 = clifford_unit(E1)
    g2 = clifford_unit(E2)
    g3 = clifford_unit(E3)
    checks.check(
        "clifford-cl30-identities",
        clifford_mul(g1, g1) == SCALAR_ONE
        and clifford_mul(g2, g2) == SCALAR_ONE
        and clifford_mul(g3, g3) == SCALAR_ONE
        and clifford_mul(clifford_unit(NEG_E1), clifford_unit(NEG_E1)) == SCALAR_ONE
        and clifford_unit(NEG_E1) == clifford_neg(g1)
        and clifford_mul(g1, g2) == clifford_neg(clifford_mul(g2, g1))
        and clifford_mul(g1, g3) == clifford_neg(clifford_mul(g3, g1))
        and clifford_mul(g2, g3) == clifford_neg(clifford_mul(g3, g2))
        and is_scalar_pm1(SCALAR_ONE)
        and is_scalar_pm1(SCALAR_MINUS)
        and not is_scalar_pm1(g1)
        and clifford_display(SCALAR_MINUS) == "−1",
    )
    four_e1 = (frozenset({E1}),) * 4
    mixed_scalar = (
        frozenset({E1}),
        frozenset({E3, NEG_E3}),
        frozenset({E3, NEG_E3}),
        frozenset({NEG_E1}),
    )
    no_scalar = (
        frozenset({E1}),
        frozenset({E2}),
        frozenset({E3}),
        frozenset({E1}),
    )
    checks.check(
        "exist-choice-identity",
        exist_choice(("UNDEFINED", frozenset({E1}), frozenset({E1}), frozenset({E1})))[0]
        == "UNDEFINED"
        and exist_choice((frozenset(), frozenset({E1}), frozenset({E1}), frozenset({E1})))[0]
        == "UNDEFINED"
        and exist_choice(four_e1) == ("hold", 1, 1)
        and exist_choice(mixed_scalar)[0] == "hold"
        and exist_choice(no_scalar) == ("fail", 1, 0)
        and unique_l_product(mixed_scalar) == "UNDEFINED"
        and unique_own_incoming_letter(frozenset({E3, NEG_E3})) == "UNDEFINED"
        and unique_own_incoming_letter(frozenset({NEG_E1})) == NEG_E1,
    )

    ticks, locks = form()
    perp_ticks, perp_locks = form(PERP_SEEDS)
    zsym_ticks, zsym_locks = form(Z_SYMMETRIC_SEEDS)
    twosite_ticks, twosite_locks = form(TWO_SITE_SEEDS)
    nstri_ticks, nstri_locks = form(NSTRI_SEEDS)

    q_sets = cycle_incoming(Q_CYCLE, ticks, locks)
    r_sets = cycle_incoming(R_CYCLE, ticks, locks)
    q_status, q_picks, q_hold = exist_choice(q_sets)
    r_status, r_picks, r_hold = exist_choice(r_sets)
    q_unique = unique_l_product(q_sets)
    r_unique = unique_l_product(r_sets)
    q_letters = tuple(unique_own_incoming_letter(item) for item in q_sets)
    r_letters = tuple(unique_own_incoming_letter(item) for item in r_sets)

    print("Q vertices:")
    for site, incoming in zip(Q_CYCLE, q_sets):
        print(
            f"  {site} t={ticks[site]} M={set_display(incoming)} "
            f"L={letter_display(unique_own_incoming_letter(incoming))}"
        )
    print(f"Q N_picks={q_picks} N_hold={q_hold} unique_L={q_unique} face={q_status}")
    print("R vertices:")
    for site, incoming in zip(R_CYCLE, r_sets):
        print(
            f"  {site} t={ticks[site]} M={set_display(incoming)} "
            f"L={letter_display(unique_own_incoming_letter(incoming))}"
        )
    print(f"R N_picks={r_picks} N_hold={r_hold} unique_L={r_unique} reverse={r_status}")
    print(
        "per_element: each lock vector in a vertex own incoming set and each 4-cycle pick"
    )
    print("per_site: scored only at Q and R vertices on Euclidean B_3(0); no other sites")
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print(
        "per_block: eight incoming sets, N_picks/N_hold, and reverse/face as hold, fail, or UNDEFINED"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    expected_q = (
        frozenset({E1}),
        frozenset({E3, NEG_E3}),
        frozenset({NEG_E2, E3, NEG_E3}),
        frozenset({NEG_E1}),
    )
    expected_r = (
        frozenset({NEG_E1}),
        frozenset({NEG_E2, E3, NEG_E3}),
        frozenset({E1}),
        frozenset({E3}),
    )
    twosite_q = cycle_incoming(Q_CYCLE, twosite_ticks, twosite_locks)
    twosite_status, twosite_picks, _twosite_hold = exist_choice(twosite_q)
    zsym_q = cycle_incoming(Q_CYCLE, zsym_ticks, zsym_locks)
    perp_q = cycle_incoming(Q_CYCLE, perp_ticks, perp_locks)
    nstri_q = cycle_incoming(Q_CYCLE, nstri_ticks, nstri_locks)

    checks.check(
        "theorem1-all-q-and-r-recorded",
        all(site in ticks for site in Q_CYCLE)
        and all(site in ticks for site in R_CYCLE),
    )
    checks.check(
        "theorem1-incoming-sets",
        q_sets == expected_q
        and r_sets == expected_r
        and ticks[Q_CYCLE[0]] == 0
        and ticks[Q_CYCLE[1]] == 3
        and ticks[Q_CYCLE[2]] == 3
        and ticks[Q_CYCLE[3]] == 0
        and ticks[R_CYCLE[0]] == 0
        and ticks[R_CYCLE[1]] == 3
        and ticks[R_CYCLE[2]] == 2
        and ticks[R_CYCLE[3]] == 1,
        str((tuple(set_display(item) for item in q_sets), tuple(set_display(item) for item in r_sets))),
    )
    checks.check(
        "theorem1-n-picks-n-hold",
        q_picks == 6
        and q_hold == 4
        and r_picks == 3
        and r_hold == 2
        and q_picks == 1 * 2 * 3 * 1
        and r_picks == 1 * 3 * 1 * 1,
        str((q_picks, q_hold, r_picks, r_hold)),
    )
    checks.check(
        "theorem1-unique-L-letters",
        q_letters == (E1, "UNDEFINED", "UNDEFINED", NEG_E1)
        and r_letters == (NEG_E1, "UNDEFINED", E1, E3)
        and q_unique == "UNDEFINED"
        and r_unique == "UNDEFINED",
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        len(q_sets[1]) == 2
        and len(q_sets[2]) == 3
        and q_sets[1] != "UNDEFINED"
        and q_sets[2] != "UNDEFINED"
        and unique_own_incoming_letter(q_sets[1]) == "UNDEFINED"
        and unique_own_incoming_letter(q_sets[2]) == "UNDEFINED",
    )
    checks.check(
        "theorem2-reverse-hold",
        r_status == "hold"
        and reverse_report(r_sets) == "hold"
        and r_hold == 2
        and r_status != "fail"
        and r_status != "UNDEFINED",
        r_status,
    )
    checks.check(
        "theorem3-face-hold",
        q_status == "hold"
        and face_report(q_sets) == "hold"
        and q_hold == 4
        and q_status != "fail"
        and q_status != "UNDEFINED",
        q_status,
    )
    checks.check(
        "holding-picks-are-scalar-pm1",
        product_U((E1, E3, E3, NEG_E1)) == SCALAR_MINUS
        and product_U((E1, E3, NEG_E3, NEG_E1)) == SCALAR_ONE
        and product_U((E1, NEG_E3, E3, NEG_E1)) == SCALAR_ONE
        and product_U((E1, NEG_E3, NEG_E3, NEG_E1)) == SCALAR_MINUS
        and product_U((NEG_E1, E3, E1, E3)) == SCALAR_ONE
        and product_U((NEG_E1, NEG_E3, E1, E3)) == SCALAR_MINUS
        and not is_scalar_pm1(product_U((E1, E3, NEG_E2, NEG_E1)))
        and not is_scalar_pm1(product_U((NEG_E1, NEG_E2, E1, E3))),
    )
    checks.check(
        "not-unique-L-leftover",
        q_unique == "UNDEFINED"
        and r_unique == "UNDEFINED"
        and q_status == "hold"
        and r_status == "hold"
        and q_status != q_unique
        and r_status != r_unique
        and q_letters[1] == "UNDEFINED"
        and r_letters[1] == "UNDEFINED",
    )
    checks.check(
        "independent-of-nmclopp-7167",
        Y_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and twosite_q[1] == frozenset({E2, E3, NEG_E3})
        and q_sets[1] == frozenset({E3, NEG_E3})
        and twosite_q[1] != q_sets[1]
        and twosite_picks == 9
        and q_picks == 6
        and twosite_picks != q_picks
        and E2 in twosite_q[1]
        and E2 not in q_sets[1],
    )
    checks.check(
        "not-x-probes-or-z-symmetric-or-perp-or-nstri",
        Y_SYMMETRIC_SEEDS != PERP_SEEDS
        and Y_SYMMETRIC_SEEDS != Z_SYMMETRIC_SEEDS
        and Y_SYMMETRIC_SEEDS != NSTRI_SEEDS
        and zsym_q != q_sets
        and perp_q != q_sets
        and nstri_q != q_sets
        and zsym_q[0] == frozenset({E1})
        and perp_q[3] == frozenset({E2})
        and q_sets[3] == frozenset({NEG_E1}),
    )
    checks.check(
        "not-nnlock-named-sign",
        q_sets[0] == frozenset({E1})
        and named_sign(E1) == "+"
        and named_sign(NEG_E1) == "-"
        and q_sets[0] != named_sign(E1)
        and r_sets[0] != named_sign(NEG_E1),
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(item <= set(NN) for item in q_sets)
        and all(item <= set(NN) for item in r_sets),
    )
    checks.check(
        "uniqueness-not-required",
        len(q_sets[0]) == 1
        and len(q_sets[1]) == 2
        and len(q_sets[2]) == 3
        and len(q_sets[3]) == 1
        and q_status == "hold"
        and r_status == "hold",
    )
    checks.check(
        "y-symmetric-three-site-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and ticks[NEG_E2] == 0
        and locks[NEG_E2] == {NEG_E1}
        and add(E1, NEG_E1) == ZERO
        and Y_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and sum(time == 0 for time in ticks.values()) == 3,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E2, step)) != 1 for step in (E1, NEG_E1)
    )
    y_mirror_parallel_blocked = all(
        ticks.get(add(NEG_E2, step)) != 1 for step in (E1, NEG_E1)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and y_mirror_parallel_blocked
        and ticks[NEG_E2] == 0
        and ticks[E3] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["D"]] == 3
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "mutation-empty-or-undefined-is-undefined",
        exist_choice(("UNDEFINED",) + q_sets[1:])[0] == "UNDEFINED"
        and exist_choice((frozenset(),) + r_sets[1:])[0] == "UNDEFINED"
        and reverse_report(("UNDEFINED",) + r_sets[1:]) == "UNDEFINED"
        and face_report((frozenset(),) + q_sets[1:]) == "UNDEFINED",
    )
    checks.check(
        "mutation-no-scalar-pick-fails",
        exist_choice(no_scalar)[0] == "fail"
        and q_status == "hold"
        and r_status == "hold",
    )
    checks.check(
        "mutation-unique-L-product-would-be-undefined",
        q_unique == "UNDEFINED"
        and r_unique == "UNDEFINED"
        and q_status == "hold"
        and r_status == "hold",
    )
    checks.check(
        "mutation-minus-e2-picks-are-not-scalar",
        not is_scalar_pm1(product_U((E1, E3, NEG_E2, NEG_E1)))
        and not is_scalar_pm1(product_U((E1, NEG_E3, NEG_E2, NEG_E1)))
        and not is_scalar_pm1(product_U((NEG_E1, NEG_E2, E1, E3)))
        and q_hold == q_picks - 2
        and r_hold == r_picks - 1,
    )
    checks.check(
        "mutation-sum-cancels-mixed-D",
        sum_of_set(q_sets[2]) == NEG_E2
        and q_sets[2] != frozenset({NEG_E2})
        and len(q_sets[2]) == 3
        and q_status == "hold",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-incoming-sets",
        "M(0) = {+e_1}" in note
        and "M(e_1) = {+e_3, −e_3}" in note
        and "M(e_1+e_2) = {−e_2, +e_3, −e_3}" in note
        and "M(e_2) = {−e_1}" in note
        and "M(A) = {−e_1}" in note
        and "M(D) = {−e_2, +e_3, −e_3}" in note
        and "M(B) = {+e_1}" in note
        and "M((0,1,1)) = {+e_3}" in note,
    )
    checks.check(
        "note-reports-n-picks-n-hold",
        "N_picks(Q) = 6" in note
        and "N_hold(Q) = 4" in note
        and "N_picks(R) = 3" in note
        and "N_hold(R) = 2" in note
        and "L(e_1) = UNDEFINED" in note
        and "L(D) = UNDEFINED" in note
        and "Unique-L product on `Q` is `UNDEFINED`" in note,
    )
    checks.check(
        "note-reports-hold-hold",
        "Reverse: hold" in note
        and "Face: hold" in note
        and "hold" in note
        and "fail" in note
        and "UNDEFINED" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-does-not-use-occupancy",
        "does not use occupancy" in normalized_note
        and "own incoming set" in normalized_note
        and "mixed stays a set" in normalized_note,
    )
    checks.check(
        "note-not-sign-lettering",
        "not named-sign lettering" in normalized_note
        and "lost the axis" in normalized_note,
    )
    checks.check(
        "note-not-ndot-or-occupancy-inner-product",
        "not an occupancy-kernel inner product" in normalized_note
        and "does not use occupancy" in normalized_note,
    )
    checks.check(
        "note-does-not-attach-formation-member",
        "does not attach a formation member from already-recorded six-neighbor locks"
        in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-unique-or-star-or-nmclopp-leftover",
        "not a unique lock-vector leftover" in normalized_note
        and "not leftover of unique-L" in normalized_note
        and "independent of nmclopp" in normalized_note
        and "No S⁺." in note
        and "Face holds." in note
        and "Reverse holds." in note
        and "Unique-L product is comparison only." in note,
    )
    checks.check(
        "note-no-six-neighbor-star-as-letter",
        "does not use a six-neighbor star" in normalized_note
        and "No S⁺." in note
        and "own incoming set" in normalized_note,
    )
    checks.check(
        "note-displayed-cl30-not-cube-pauli-lattice-action",
        "Displayed algebra, not a cube-Pauli Lattice action." in note
        or "displayed algebra, not a cube-Pauli Lattice action" in normalized_note.lower(),
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in normalized_note
        and "B_3(0)" in note
        and "{n:n·n<=9}" in note.replace(" ", "")
        and "No runner cache is written." in normalized_note,
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
        in normalized_axiom,
    )
    checks.check(
        "note-quotes-current-premises",
        "Physical sites are the points of the cubic lattice `Z^3`" in note
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in note
        and "When present, a record locks exactly one admissible local possibility."
        in note
        and "does not supply the formation site, probability, or rate"
        in normalized_note,
    )
    checks.check(
        "note-machine-status-no-axiom-edit",
        'hypothetical_axiom_status: "no edit"' in note
        and "claim_type: bounded_theorem" in note
        and "authors no audit verdict" in normalized_note
        and "FAIL / DO NOT SHIP" in note,
    )
    checks.check(
        "note-n-gates-present",
        all(f"### N{index}" in note for index in range(1, 9)),
    )
    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-no-author-retained-verdict",
        all(line in allowed_retained for line in allowed_retained)
        and all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/Y_SYMMETRIC_THREE_SITE_OWN_INCOMING_SET_CLIFFORD_EXIST_CHOICE_PLAQUETTE_PRODUCT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def own_incoming_set(" in source
        and "def exist_choice(" in source
        and "def reverse_report(" in source
        and "def face_report(" in source
        and "def clifford_unit(" in source
        and "def product_U(" in source
        and "def form(" in source,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] == 0
        and set(ticks) <= host,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "source-letter-from-own-incoming-set-exist-choice",
        "own_incoming_set" in defined_fns
        and "exist_choice" in defined_fns
        and "clifford_unit" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
