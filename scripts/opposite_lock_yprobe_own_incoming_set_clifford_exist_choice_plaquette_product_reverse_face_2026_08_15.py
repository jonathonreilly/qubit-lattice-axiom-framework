#!/usr/bin/env python3
"""Exist-choice Cl(3,0) 4-cycle products of own incoming sets on #7167 Q and R.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and -e_1 (nsopp #7093; same process and
y-probes as nsuoyinc #7167 / nsmopp #7208). A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters as a singleton. M(q) is the set of
earliest incoming NN steps at q. Mixed stays a set. Unformed is UNDEFINED.
Identify ±e_i with generators γ_i of Cl(3,0): γ_i^2=+1 and γ_i γ_j=-γ_j γ_i
for i≠j; -e_i maps to -γ_i. This is a displayed algebra, not a cube-Pauli
Lattice action. Face plaquette Q is the 4-cycle (0, e_1, e_1+e_2, e_2).
Reverse 4-cycle R containing A=(0,1,0) and B=(1,1,1) is
((0,1,0), (1,1,0), (1,1,1), (0,1,1)). At a 4-cycle, a pick is one letter
from each vertex's own incoming set at that site's own t, with no T_Q.
U is the Cl(3,0) product of the four picked units. Exist-choice HOLD iff
some pick has U equal to the scalar ±1. If any vertex is unformed or M is
UNDEFINED or empty, the report is UNDEFINED. Else fail. Unique-L product
is comparison only: mixed vertex makes that leftover UNDEFINED. Unique-L
is not the theorem. This retires “Cl has no member because unique-L is
UNDEF” on mixed Q vertices by displaying whether some pick from HOLDING
M-sets of #7208 makes U=±1. Not leftover of unique-L. Not leftover of
exist-opposite of nsmopp. Not S^+. Occupancy n is not used. Named-sign
lettering is not used. No unique P_+. Uniqueness of incoming locks is not
required. No larger ball. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from itertools import product as cartesian
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_YPROBE_OWN_INCOMING_SET_CLIFFORD_EXIST_CHOICE_PLAQUETTE_PRODUCT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_YPROBE_OWN_INCOMING_SET_CLIFFORD_EXIST_CHOICE_PLAQUETTE_PRODUCT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Letter = Point | str
Incoming = frozenset[Point] | str
Multivector = tuple[int, int, int, int, int, int, int, int]
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
X_PROBES = {
    "A": (1, 0, 0),
    "B": (1, 1, 1),
    "C": (2, 0, 0),
    "D": (1, 1, 0),
}
FACE_Q: tuple[Point, ...] = (ORIGIN, E1, (1, 1, 0), E2)
REVERSE_R: tuple[Point, ...] = (E2, (1, 1, 0), (1, 1, 1), (0, 1, 1))
X_REVERSE_R: tuple[Point, ...] = (E1, (1, 1, 0), (1, 1, 1), (1, 0, 1))
SCALAR_P1: Multivector = (1, 0, 0, 0, 0, 0, 0, 0)
SCALAR_M1: Multivector = (-1, 0, 0, 0, 0, 0, 0, 0)
ZERO_MV: Multivector = (0, 0, 0, 0, 0, 0, 0, 0)
LOCK_NAME = {
    E1: "+e_1",
    NEG_E1: "−e_1",
    E2: "+e_2",
    NEG_E2: "−e_2",
    E3: "+e_3",
    NEG_E3: "−e_3",
}
GRADE_NAME = (
    "1",
    "γ_1",
    "γ_2",
    "γ_3",
    "γ_1γ_2",
    "γ_1γ_3",
    "γ_2γ_3",
    "γ_1γ_2γ_3",
)
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
    "of own incoming sets on #7167 Q and R are reported. No S⁺. "
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


def unique_own_incoming_letter(incoming: tuple[Point, ...] | set[Point] | Incoming) -> Letter:
    """Unique-L leftover: UNDEFINED when mixed. Not the theorem."""
    if incoming == "UNDEFINED":
        return "UNDEFINED"
    unique = set(incoming)
    if len(unique) != 1:
        return "UNDEFINED"
    vector = next(iter(unique))
    if vector not in NN:
        return "UNDEFINED"
    return vector


def ordered_letters(incoming: Incoming) -> tuple[Point, ...] | str:
    if incoming == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(incoming, frozenset):
        return "UNDEFINED"
    return tuple(step for step in NN if step in incoming)


def recorded_lock_set(pairs: tuple[tuple[Point, Point], ...]) -> frozenset[Point]:
    """Set of six-neighbor locks. Leftover comparator only."""
    return frozenset(lock for _neighbor, lock in pairs)


def own_lock_in_set(neighbors: frozenset[Point], letter: Letter) -> Incoming:
    """S^+ leftover: neighbor locks union L(q) when defined. Not this letter."""
    if letter == "UNDEFINED":
        return neighbors
    if not isinstance(letter, tuple):
        raise TypeError(f"letter is not a lock vector: {letter!r}")
    return neighbors | {letter}


def existential_opposite(left: Incoming, right: Incoming) -> str:
    """nsmopp leftover: hold iff some lock in left is opposite some lock in right."""
    if left == "UNDEFINED" or right == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        return "UNDEFINED"
    if not left or not right:
        return "UNDEFINED"
    for a in left:
        for b in right:
            if add(a, b) == ZERO:
                return "hold"
    return "fail"


def reverse_report(set_a: Incoming, set_b: Incoming) -> str:
    """Leftover exist-opposite reverse on y-probes A,B."""
    return existential_opposite(set_a, set_b)


def face_report(set_c: Incoming, set_d: Incoming) -> str:
    """Leftover exist-opposite face on y-probes C,D."""
    return existential_opposite(set_c, set_d)


def _blade_mul(left: int, right: int) -> tuple[int, int]:
    """Euclidean Cl(3,0) product of two basis blades encoded as 3-bit masks."""
    sign = 1
    for index in range(3):
        if (left >> index) & 1:
            lower = right & ((1 << index) - 1)
            if bin(lower).count("1") % 2:
                sign = -sign
    return sign, left ^ right


def mv_add(left: Multivector, right: Multivector) -> Multivector:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def mv_scale(scalar: int, vector: Multivector) -> Multivector:
    return tuple(scalar * coeff for coeff in vector)  # type: ignore[return-value]


def mv_mul(left: Multivector, right: Multivector) -> Multivector:
    total = [0] * 8
    for i, a in enumerate(left):
        if a == 0:
            continue
        for j, b in enumerate(right):
            if b == 0:
                continue
            sign, blade = _blade_mul(i, j)
            total[blade] += sign * a * b
    return tuple(total)  # type: ignore[return-value]


def basis_gamma(axis: int) -> Multivector:
    coeffs = [0] * 8
    coeffs[1 << (axis - 1)] = 1
    return tuple(coeffs)  # type: ignore[return-value]


def letter_to_clifford(letter: Letter) -> Multivector | str:
    """Map ±e_i to ±γ_i in Cl(3,0). Mixed or missing letters stay UNDEFINED."""
    if letter == "UNDEFINED":
        return "UNDEFINED"
    if letter == E1:
        return basis_gamma(1)
    if letter == NEG_E1:
        return mv_scale(-1, basis_gamma(1))
    if letter == E2:
        return basis_gamma(2)
    if letter == NEG_E2:
        return mv_scale(-1, basis_gamma(2))
    if letter == E3:
        return basis_gamma(3)
    if letter == NEG_E3:
        return mv_scale(-1, basis_gamma(3))
    raise ValueError(f"letter is not a six-neighbor step: {letter!r}")


def is_scalar_pm1(vector: Multivector) -> bool:
    return vector == SCALAR_P1 or vector == SCALAR_M1


def clifford_display(vector: Multivector | str) -> str:
    if vector == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(vector, tuple):
        raise TypeError(f"not a Cl(3,0) element: {vector!r}")
    if vector == ZERO_MV:
        return "0"
    if vector == SCALAR_P1:
        return "+1"
    if vector == SCALAR_M1:
        return "−1"
    parts: list[str] = []
    for coeff, name in zip(vector, GRADE_NAME):
        if coeff == 0:
            continue
        if name == "1":
            parts.append(f"{coeff:+d}")
            continue
        if coeff == 1:
            parts.append(f"+{name}")
        elif coeff == -1:
            parts.append(f"−{name}")
        else:
            parts.append(f"{coeff:+d}{name}")
    text = "".join(parts)
    if text.startswith("+"):
        return text[1:]
    return text


def cycle_product(letters: tuple[Letter, ...]) -> Multivector | str:
    """Cyclic Cl(3,0) product of four picked units, or UNDEFINED."""
    if any(letter == "UNDEFINED" for letter in letters):
        return "UNDEFINED"
    units = [letter_to_clifford(letter) for letter in letters]
    if any(unit == "UNDEFINED" for unit in units):
        return "UNDEFINED"
    product: Multivector = SCALAR_P1
    for unit in units:
        if not isinstance(unit, tuple):
            return "UNDEFINED"
        product = mv_mul(product, unit)
    return product


def hold_from_product(product: Multivector | str) -> str:
    """HOLD iff the product is the scalar ±1. UNDEFINED stays UNDEFINED."""
    if product == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(product, tuple):
        raise TypeError(f"not a Cl(3,0) element: {product!r}")
    if is_scalar_pm1(product):
        return "hold"
    return "fail"


def unique_letter_product(
    incoming_sets: tuple[Incoming, ...],
) -> Multivector | str:
    """Unique-L leftover product. Mixed vertex ⇒ UNDEFINED. Not the theorem."""
    letters = tuple(unique_own_incoming_letter(incoming) for incoming in incoming_sets)
    return cycle_product(letters)


def n_picks_n_hold(
    incoming_sets: tuple[Incoming, ...],
) -> tuple[int | str, int | str]:
    """Number of picks and number of picks with U=±1, or UNDEFINED."""
    ordered: list[tuple[Point, ...]] = []
    for incoming in incoming_sets:
        letters = ordered_letters(incoming)
        if letters == "UNDEFINED" or not letters:
            return "UNDEFINED", "UNDEFINED"
        ordered.append(letters)
    n_picks = 1
    for letters in ordered:
        n_picks *= len(letters)
    n_hold = 0
    for pick in cartesian(*ordered):
        if hold_from_product(cycle_product(pick)) == "hold":
            n_hold += 1
    return n_picks, n_hold


def exist_choice_hold(incoming_sets: tuple[Incoming, ...]) -> str:
    """HOLD iff some pick has U equal to the scalar ±1.

    If any vertex is unformed or M is UNDEFINED or empty ⇒ UNDEFINED.
    Else fail when no pick is the scalar ±1.
    """
    n_picks, n_hold = n_picks_n_hold(incoming_sets)
    if n_picks == "UNDEFINED" or n_hold == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(n_hold, int):
        return "UNDEFINED"
    if n_hold > 0:
        return "hold"
    return "fail"


def opposite_vertex_hold(letters: tuple[Letter, ...]) -> str:
    """Leftover: opposite vertices have opposite lock vectors."""
    if any(letter == "UNDEFINED" for letter in letters):
        return "UNDEFINED"
    if len(letters) != 4:
        return "UNDEFINED"
    a, b, c, d = letters
    if not isinstance(a, tuple) or not isinstance(c, tuple):
        return "UNDEFINED"
    if not isinstance(b, tuple) or not isinstance(d, tuple):
        return "UNDEFINED"
    if add(a, c) == ZERO and add(b, d) == ZERO:
        return "hold"
    return "fail"


def vector_sum(letters: tuple[Letter, ...]) -> Point | str:
    """Leftover Z^3 sum of four lock vectors."""
    if any(letter == "UNDEFINED" for letter in letters):
        return "UNDEFINED"
    total = ZERO
    for letter in letters:
        if not isinstance(letter, tuple):
            return "UNDEFINED"
        total = add(total, letter)
    return total


def lock_display(lock: Point) -> str:
    return LOCK_NAME[lock]


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
    seeds: tuple[tuple[Point, Point], ...] = TWO_SITE_SEEDS,
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


def own_tick_neighbor_locks(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> tuple[tuple[Point, Point], ...]:
    """Leftover #7167 S^+ neighbor list: 6-NN locks formed at tick <= t(site)."""
    formation = ticks[site]
    pairs: list[tuple[Point, Point]] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor == site:
            continue
        if neighbor not in ticks:
            continue
        if ticks[neighbor] > formation:
            continue
        for lock in sorted(locks[neighbor]):
            pairs.append((neighbor, lock))
    return tuple(pairs)


def cycle_incoming(
    cycle: tuple[Point, ...],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> tuple[Incoming, ...]:
    return tuple(own_incoming_set(site, ticks, locks) for site in cycle)


def cycle_unique_letters(incoming_sets: tuple[Incoming, ...]) -> tuple[Letter, ...]:
    return tuple(unique_own_incoming_letter(incoming) for incoming in incoming_sets)


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

    print("exist-choice Cl(3,0) plaquette product of own incoming sets on #7167 Q and R")
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
    probe_sites = tuple(PROBES[name] for name in ("A", "B", "C", "D"))
    x_probe_sites = tuple(X_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-y-probes-in-host",
        probe_sites == ((0, 1, 0), (1, 1, 1), (0, 2, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and probe_sites != x_probe_sites,
    )
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "cycles-in-host",
        FACE_Q == (ORIGIN, E1, (1, 1, 0), E2)
        and REVERSE_R == (E2, (1, 1, 0), (1, 1, 1), (0, 1, 1))
        and set(FACE_Q) <= host
        and set(REVERSE_R) <= host
        and PROBES["A"] in REVERSE_R
        and PROBES["B"] in REVERSE_R
        and PROBES["A"] in FACE_Q
        and PROBES["D"] in FACE_Q
        and PROBES["D"] in REVERSE_R
        and REVERSE_R != X_REVERSE_R,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and add(NEG_E1, E1) == ZERO
        and add(NEG_E2, E2) == ZERO
        and add(E2, NEG_E2) == ZERO
        and add(E1, E2) == (1, 1, 0)
        and add(E1, E1) != ZERO
        and add(E2, E2) != ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and in_ball((0, 1, 1))
        and not in_ball((4, 0, 0)),
    )

    g1 = basis_gamma(1)
    g2 = basis_gamma(2)
    g3 = basis_gamma(3)
    checks.check(
        "clifford-squares-plus-one",
        mv_mul(g1, g1) == SCALAR_P1
        and mv_mul(g2, g2) == SCALAR_P1
        and mv_mul(g3, g3) == SCALAR_P1,
    )
    checks.check(
        "clifford-anticommutators",
        mv_mul(g1, g2) == mv_scale(-1, mv_mul(g2, g1))
        and mv_mul(g1, g3) == mv_scale(-1, mv_mul(g3, g1))
        and mv_mul(g2, g3) == mv_scale(-1, mv_mul(g3, g2))
        and mv_mul(g1, g2) != SCALAR_P1
        and mv_mul(g1, g2) != SCALAR_M1,
    )
    checks.check(
        "letter-map-is-displayed-cl30",
        letter_to_clifford(E1) == g1
        and letter_to_clifford(NEG_E1) == mv_scale(-1, g1)
        and letter_to_clifford(E2) == g2
        and letter_to_clifford(NEG_E2) == mv_scale(-1, g2)
        and letter_to_clifford(E3) == g3
        and letter_to_clifford(NEG_E3) == mv_scale(-1, g3)
        and letter_to_clifford("UNDEFINED") == "UNDEFINED",
    )
    hold_pick_q = (E1, E2, NEG_E2, NEG_E1)
    hold_pick_r = (NEG_E1, E3, E1, E3)
    fail_pick_q = (E1, E2, E3, NEG_E1)
    fail_pick_r = (NEG_E1, NEG_E2, E1, E3)
    checks.check(
        "scalar-hold-identity",
        cycle_product(hold_pick_q) == SCALAR_P1
        and hold_from_product(cycle_product(hold_pick_q)) == "hold"
        and cycle_product((E1, E3, E3, NEG_E1)) == SCALAR_M1
        and hold_from_product(cycle_product((E1, E3, E3, NEG_E1))) == "hold"
        and cycle_product(hold_pick_r) == SCALAR_P1
        and hold_from_product(cycle_product(hold_pick_r)) == "hold"
        and hold_from_product(cycle_product(fail_pick_q)) == "fail"
        and hold_from_product(cycle_product(fail_pick_r)) == "fail"
        and hold_from_product(mv_mul(g1, g2)) == "fail"
        and hold_from_product("UNDEFINED") == "UNDEFINED"
        and cycle_product((E1, "UNDEFINED", E1, E2)) == "UNDEFINED",
    )
    set_a = frozenset({NEG_E1})
    set_b = frozenset({E1})
    set_c = frozenset({E2})
    set_d = frozenset({NEG_E2, E3, NEG_E3})
    set_e1 = frozenset({E2, E3, NEG_E3})
    set_origin = frozenset({E1})
    set_e2 = frozenset({NEG_E1})
    set_e2e3 = frozenset({E3})
    checks.check(
        "exist-choice-identity",
        exist_choice_hold(("UNDEFINED", set_a, set_b, set_c)) == "UNDEFINED"
        and exist_choice_hold((frozenset(), set_a, set_b, set_c)) == "UNDEFINED"
        and exist_choice_hold((set_origin, set_e1, set_d, set_e2)) == "hold"
        and exist_choice_hold((set_e2, set_d, set_b, set_e2e3)) == "hold"
        and exist_choice_hold((set_origin, frozenset({E2}), frozenset({E3}), set_e2))
        == "fail"
        and n_picks_n_hold((set_origin, set_e1, set_d, set_e2)) == (9, 5)
        and n_picks_n_hold((set_e2, set_d, set_b, set_e2e3)) == (3, 2)
        and n_picks_n_hold(("UNDEFINED", set_a, set_b, set_c))
        == ("UNDEFINED", "UNDEFINED"),
    )
    checks.check(
        "own-incoming-set-identity",
        unique_own_incoming_letter(frozenset({NEG_E1})) == NEG_E1
        and unique_own_incoming_letter(frozenset({E2, NEG_E2})) == "UNDEFINED"
        and unique_own_incoming_letter(frozenset({NEG_E2, E3, NEG_E3})) == "UNDEFINED"
        and unique_own_incoming_letter((E1, E2)) == "UNDEFINED"
        and unique_own_incoming_letter(()) == "UNDEFINED"
        and unique_own_incoming_letter("UNDEFINED") == "UNDEFINED",
    )

    ticks, locks = form()
    perp_ticks, perp_locks = form(PERP_SEEDS)
    zsym_ticks, zsym_locks = form(Z_SYMMETRIC_SEEDS)
    ysym_ticks, ysym_locks = form(Y_SYMMETRIC_SEEDS)
    checks.check(
        "theorem1-all-cycle-vertices-recorded",
        all(site in ticks for site in FACE_Q)
        and all(site in ticks for site in REVERSE_R)
        and all(PROBES[name] in ticks for name in ("A", "B", "C", "D")),
    )

    incoming_sets: dict[str, Incoming] = {}
    letters: dict[str, Letter] = {}
    plus_sets: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        incoming_sets[name] = own_incoming_set(site, ticks, locks)
        letters[name] = unique_own_incoming_letter(incoming_sets[name])
        pairs = own_tick_neighbor_locks(site, ticks, locks)
        plus_sets[name] = own_lock_in_set(recorded_lock_set(pairs), letters[name])

    q_incoming = cycle_incoming(FACE_Q, ticks, locks)
    r_incoming = cycle_incoming(REVERSE_R, ticks, locks)
    q_unique = cycle_unique_letters(q_incoming)
    r_unique = cycle_unique_letters(r_incoming)
    q_n_picks, q_n_hold = n_picks_n_hold(q_incoming)
    r_n_picks, r_n_hold = n_picks_n_hold(r_incoming)
    unique_u_q = unique_letter_product(q_incoming)
    unique_u_r = unique_letter_product(r_incoming)
    reverse_status = exist_choice_hold(r_incoming)
    face_status = exist_choice_hold(q_incoming)
    unique_reverse = hold_from_product(unique_u_r)
    unique_face = hold_from_product(unique_u_q)
    leftover_opposite_reverse = reverse_report(incoming_sets["A"], incoming_sets["B"])
    leftover_opposite_face = face_report(incoming_sets["C"], incoming_sets["D"])
    plus_reverse = reverse_report(plus_sets["A"], plus_sets["B"])
    plus_face = face_report(plus_sets["C"], plus_sets["D"])
    t_q = max(ticks[site] for site in FACE_Q)
    opp_q = opposite_vertex_hold(q_unique)
    sum_q = vector_sum(q_unique)
    sum_r = vector_sum(r_unique)

    for name, cycle, incoming in (("Q", FACE_Q, q_incoming), ("R", REVERSE_R, r_incoming)):
        bits = []
        for site, incoming_set in zip(cycle, incoming):
            bits.append(
                f"{site} t={ticks[site]} M={set_display(incoming_set)} "
                f"L={letter_display(unique_own_incoming_letter(incoming_set))}"
            )
        print(f"{name}: " + " | ".join(bits))
    print(f"N_picks(Q)={q_n_picks} N_hold(Q)={q_n_hold} N_picks(R)={r_n_picks} N_hold(R)={r_n_hold}")
    print(
        f"unique_L_U_Q={clifford_display(unique_u_q)} unique_L_U_R={clifford_display(unique_u_r)}"
    )
    print(f"reverse={reverse_status} face={face_status}")
    print(
        f"unique_L_reverse={unique_reverse} unique_L_face={unique_face} "
        f"nsmopp_exist_opposite reverse={leftover_opposite_reverse} "
        f"face={leftover_opposite_face} S+_reverse={plus_reverse} S+_face={plus_face}"
    )
    print("per_element: each picked lock vector as a Cl(3,0) unit ±γ_i")
    print(
        "per_site: scored only on face 4-cycle Q and reverse 4-cycle R in Euclidean B_3(0)"
    )
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print(
        "per_block: four incoming sets, N_picks, N_hold, and exist-choice hold iff some U=±1"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    perp_q = cycle_incoming(FACE_Q, perp_ticks, perp_locks)
    zsym_q = cycle_incoming(FACE_Q, zsym_ticks, zsym_locks)
    ysym_q = cycle_incoming(FACE_Q, ysym_ticks, ysym_locks)
    x_r = cycle_incoming(X_REVERSE_R, ticks, locks)
    x_reverse = exist_choice_hold(x_r)

    checks.check(
        "theorem1-formation-ticks",
        ticks[ORIGIN] == 0
        and ticks[E1] == 3
        and ticks[(1, 1, 0)] == 3
        and ticks[E2] == 0
        and ticks[(1, 1, 1)] == 2
        and ticks[(0, 1, 1)] == 1
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3,
        str({site: ticks[site] for site in FACE_Q + REVERSE_R}),
    )
    checks.check(
        "theorem1-incoming-sets-Q",
        q_incoming == (set_origin, set_e1, set_d, set_e2)
        and q_incoming[0] != "UNDEFINED"
        and q_incoming[1] != "UNDEFINED"
        and q_incoming[2] != "UNDEFINED"
        and q_incoming[3] != "UNDEFINED"
        and len(q_incoming[1]) == 3
        and len(q_incoming[2]) == 3,
        str(tuple(set_display(item) for item in q_incoming)),
    )
    checks.check(
        "theorem1-incoming-sets-R",
        r_incoming == (set_e2, set_d, set_b, set_e2e3)
        and r_incoming[0] == incoming_sets["A"]
        and r_incoming[1] == incoming_sets["D"]
        and r_incoming[2] == incoming_sets["B"]
        and len(r_incoming[1]) == 3
        and len(r_incoming[3]) == 1,
        str(tuple(set_display(item) for item in r_incoming)),
    )
    checks.check(
        "theorem1-n-picks-n-hold",
        q_n_picks == 9
        and q_n_hold == 5
        and r_n_picks == 3
        and r_n_hold == 2
        and q_n_hold != q_n_picks
        and r_n_hold != r_n_picks,
        str(((q_n_picks, q_n_hold), (r_n_picks, r_n_hold))),
    )
    checks.check(
        "theorem1-unique-L-letters",
        q_unique == (E1, "UNDEFINED", "UNDEFINED", NEG_E1)
        and r_unique == (NEG_E1, "UNDEFINED", E1, E3)
        and letters["A"] == NEG_E1
        and letters["B"] == E1
        and letters["C"] == E2
        and letters["D"] == "UNDEFINED"
        and unique_u_q == "UNDEFINED"
        and unique_u_r == "UNDEFINED",
        str((q_unique, r_unique)),
    )
    checks.check(
        "theorem1-A-is-seed-on-Q-and-R",
        PROBES["A"] == E2
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and incoming_sets["A"] == frozenset({NEG_E1})
        and FACE_Q[3] == PROBES["A"]
        and REVERSE_R[0] == PROBES["A"]
        and X_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        len(q_incoming[1]) == 3
        and len(q_incoming[2]) == 3
        and q_unique[1] == "UNDEFINED"
        and q_unique[2] == "UNDEFINED"
        and q_incoming[1] != "UNDEFINED"
        and q_incoming[2] != "UNDEFINED"
        and E2 in q_incoming[1]
        and E3 in q_incoming[1]
        and NEG_E3 in q_incoming[1]
        and NEG_E2 in q_incoming[2]
        and letters["D"] == "UNDEFINED"
        and incoming_sets["D"] != "UNDEFINED",
    )
    checks.check(
        "theorem2-reverse-exist-choice-hold",
        reverse_status == "hold"
        and r_n_hold == 2
        and r_n_picks == 3
        and hold_from_product(cycle_product(hold_pick_r)) == "hold"
        and reverse_status != "fail"
        and reverse_status != "UNDEFINED",
        reverse_status,
    )
    checks.check(
        "theorem3-face-exist-choice-hold",
        face_status == "hold"
        and q_n_hold == 5
        and q_n_picks == 9
        and hold_from_product(cycle_product(hold_pick_q)) == "hold"
        and face_status != "fail"
        and face_status != "UNDEFINED",
        face_status,
    )
    checks.check(
        "not-unique-L-leftover",
        unique_reverse == "UNDEFINED"
        and unique_face == "UNDEFINED"
        and reverse_status == "hold"
        and face_status == "hold"
        and reverse_status != unique_reverse
        and face_status != unique_face
        and unique_u_q == "UNDEFINED"
        and unique_u_r == "UNDEFINED"
        and q_unique[1] == "UNDEFINED"
        and r_unique[1] == "UNDEFINED",
    )
    checks.check(
        "not-leftover-of-exist-opposite-nsmopp",
        leftover_opposite_reverse == "hold"
        and leftover_opposite_face == "hold"
        and incoming_sets["A"] == set_a
        and incoming_sets["B"] == set_b
        and incoming_sets["C"] == set_c
        and incoming_sets["D"] == set_d
        and PROBES["C"] not in FACE_Q
        and PROBES["C"] not in REVERSE_R
        and reverse_status == "hold"
        and face_status == "hold"
        and exist_choice_hold is not existential_opposite,
    )
    checks.check(
        "not-leftover-of-S-plus-7167",
        plus_sets["A"] != incoming_sets["A"]
        and plus_reverse == "hold"
        and plus_face == "hold"
        and E1 in plus_sets["A"]
        and E1 not in incoming_sets["A"]
        and "No S⁺." in CLAIM_SCOPE
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "not-x-reverse-or-z-symmetric-or-perp",
        TWO_SITE_SEEDS != PERP_SEEDS
        and TWO_SITE_SEEDS != Z_SYMMETRIC_SEEDS
        and REVERSE_R != X_REVERSE_R
        and x_r != r_incoming
        and zsym_q != q_incoming
        and perp_q != q_incoming
        and ysym_q != q_incoming
        and n_picks_n_hold(zsym_q) != (q_n_picks, q_n_hold)
        and n_picks_n_hold(perp_q) != (q_n_picks, q_n_hold)
        and n_picks_n_hold(ysym_q) != (q_n_picks, q_n_hold)
        and n_picks_n_hold(x_r) != (r_n_picks, r_n_hold)
        and reverse_status == "hold"
        and face_status == "hold",
        str((n_picks_n_hold(zsym_q), n_picks_n_hold(perp_q), n_picks_n_hold(x_r))),
    )
    checks.check(
        "not-nnlock-named-sign",
        incoming_sets["A"] == frozenset({NEG_E1})
        and named_sign(NEG_E1) == "-"
        and named_sign(E1) == "+"
        and incoming_sets["C"] == frozenset({E2})
        and named_sign(E2) == "+"
        and incoming_sets["A"] != named_sign(NEG_E1)
        and incoming_sets["C"] != named_sign(E2),
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(
            incoming_sets[name] <= set(NN)
            for name in ("A", "B", "C", "D")
        )
        and all(item <= set(NN) for item in q_incoming)
        and all(item <= set(NN) for item in r_incoming),
    )
    checks.check(
        "uniqueness-not-required",
        len(q_incoming[0]) == 1
        and len(q_incoming[1]) == 3
        and len(q_incoming[2]) == 3
        and len(q_incoming[3]) == 1
        and len(r_incoming[1]) == 3
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "two-site-opposite-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and add(E1, NEG_E1) == ZERO
        and TWO_SITE_SEEDS != PERP_SEEDS
        and TWO_SITE_SEEDS != Y_SYMMETRIC_SEEDS
        and sum(time == 0 for time in ticks.values()) == 2,
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
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[E3] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["D"]] == 3
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "no-T_Q-in-letter",
        t_q == 3
        and t_q == ticks[E1]
        and t_q == ticks[(1, 1, 0)]
        and ticks[ORIGIN] != t_q
        and ticks[E2] != t_q
        and face_status == "hold"
        and unique_face == "UNDEFINED",
    )
    checks.check(
        "not-leftover-of-opposite-vertex-or-vector-sum",
        opp_q == "UNDEFINED"
        and sum_q == "UNDEFINED"
        and sum_r == "UNDEFINED"
        and face_status == "hold"
        and reverse_status == "hold"
        and exist_choice_hold is not vector_sum
        and exist_choice_hold is not opposite_vertex_hold,
    )
    checks.check(
        "mutation-empty-or-undefined-is-undefined",
        exist_choice_hold((frozenset(), q_incoming[1], q_incoming[2], q_incoming[3]))
        == "UNDEFINED"
        and exist_choice_hold(("UNDEFINED", r_incoming[1], r_incoming[2], r_incoming[3]))
        == "UNDEFINED"
        and exist_choice_hold(q_incoming) == "hold"
        and exist_choice_hold(r_incoming) == "hold",
    )
    checks.check(
        "mutation-unique-L-would-be-undefined",
        unique_face == "UNDEFINED"
        and unique_reverse == "UNDEFINED"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "mutation-no-scalar-pick-fails",
        exist_choice_hold((set_origin, frozenset({E2}), frozenset({E3}), set_e2))
        == "fail"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "some-picks-hold-some-fail",
        hold_from_product(cycle_product(hold_pick_q)) == "hold"
        and hold_from_product(cycle_product(fail_pick_q)) == "fail"
        and hold_from_product(cycle_product(hold_pick_r)) == "hold"
        and hold_from_product(cycle_product(fail_pick_r)) == "fail"
        and q_n_hold == 5
        and r_n_hold == 2,
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-incoming-sets",
        "M(0) = {+e_1}" in note
        and "M(e_1) = {+e_2, +e_3, −e_3}" in note
        and "M(e_1+e_2) = {−e_2, +e_3, −e_3}" in note
        and "M(e_2) = {−e_1}" in note
        and "M(0,1,0) = {−e_1}" in note
        and "M(1,1,0) = {−e_2, +e_3, −e_3}" in note
        and "M(1,1,1) = {+e_1}" in note
        and "M(0,1,1) = {+e_3}" in note
        and "t(0)=0" in note
        and "t(e_1)=3" in note
        and "t(e_1+e_2)=3" in note
        and "t(e_2)=0" in note
        and "t(1,1,1)=2" in note
        and "t(0,1,1)=1" in note,
    )
    checks.check(
        "note-reports-n-picks-n-hold-and-unique-L",
        "N_picks(Q)=9" in note
        and "N_hold(Q)=5" in note
        and "N_picks(R)=3" in note
        and "N_hold(R)=2" in note
        and "L(0) = +e_1" in note
        and "L(e_1) = UNDEFINED" in note
        and "L(e_1+e_2) = UNDEFINED" in note
        and "L(e_2) = −e_1" in note
        and "L(0,1,0) = −e_1" in note
        and "L(1,1,0) = UNDEFINED" in note
        and "L(1,1,1) = +e_1" in note
        and "L(0,1,1) = +e_3" in note,
    )
    checks.check(
        "note-reports-hold-hold",
        "Reverse: hold" in note
        and "Face: hold" in note
        and "hold" in note
        and "fail" in note
        and "UNDEFINED" in note
        and "scalar ±1" in note
        and "Cl(3,0)" in note,
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
        and "mixed stays a set" in normalized_note
        and "no T_Q" in normalized_note,
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
        "note-not-unique-or-sum-or-star-or-exist-opposite-leftover",
        "not leftover of unique-L" in normalized_note
        and "not leftover of exist-opposite" in normalized_note
        and "not leftover of #7208" in normalized_note
        and "not leftover of #7167" in normalized_note
        and "not a unique lock-vector leftover" in normalized_note
        and "not a sum leftover" in normalized_note
        and "does not sum" in normalized_note
        and "Face holds." in note
        and "Reverse holds." in note,
    )
    checks.check(
        "note-no-six-neighbor-star-as-letter",
        "does not use a six-neighbor star" in normalized_note
        and "No S⁺." in note
        and "own incoming set" in normalized_note,
    )
    checks.check(
        "note-not-cube-pauli-lattice-action",
        "not a cube-Pauli Lattice action" in normalized_note
        and "displayed algebra" in normalized_note
        and "Lattice-named" not in note,
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
        all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/OPPOSITE_LOCK_YPROBE_OWN_INCOMING_SET_CLIFFORD_EXIST_CHOICE_PLAQUETTE_PRODUCT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def own_incoming_set(" in source
        and "def exist_choice_hold(" in source
        and "def n_picks_n_hold(" in source
        and "def unique_letter_product(" in source
        and "def cycle_product(" in source
        and "def letter_to_clifford(" in source
        and "def form(" in source
        and "def mv_mul(" in source,
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
        "source-letter-from-exist-choice-cl30-product",
        "exist_choice_hold" in defined_fns
        and "n_picks_n_hold" in defined_fns
        and "own_incoming_set" in defined_fns
        and "cycle_product" in defined_fns
        and "letter_to_clifford" in defined_fns
        and "unique_letter_product" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns
        and "dijkstra" not in {name.lower() for name in defined_fns}
        and "gram" not in {name.lower() for name in defined_fns},
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
