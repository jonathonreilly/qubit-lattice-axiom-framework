#!/usr/bin/env python3
"""Exist-choice Cl(3,0) 4-cycle products from S^+ on HOLDING #7188 Q and R.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,0,1), (0,0,-1)} with locks +e_1, -e_1, and -e_1. A 6-NN step is
allowed iff it is perpendicular to the parent lock axis. Newly formed sites
lock the incoming step. Seeds keep their seed letters. L(q) is q's own unique
incoming lock; mixed earliest steps make L(q) UNDEFINED. At q's own formation
tick t(q), S^+(q) is the set of locks of 6-NN of q that formed at tick <= t(q)
and are not q, union {L(q)} when L(q) is defined. Unformed sites make S^+
UNDEFINED. No global T. Identify ±e_i with generators γ_i of Cl(3,0):
γ_i^2=+1 and γ_i γ_j=-γ_j γ_i for i≠j; -e_i maps to -γ_i. This is a displayed
algebra, not a cube-Pauli Lattice action. Face plaquette Q is the 4-cycle
(0, e_1, e_1+e_2, e_2). Reverse 4-cycle R is ((1,0,0), (1,1,0), (1,1,1),
(1,0,1)). A pick is one letter from each vertex S^+ at that site's own t.
U is the Cl(3,0) product of the four picked units. Exist-choice HOLD iff some
pick has U equal to the scalar ±1. Empty or UNDEFINED S^+, or an unformed
vertex, makes the report UNDEFINED. Unique-L products are comparison only
and stay UNDEFINED from mixed vertices. Same process and x-probes as the
z-symmetric three-site same-tick union-own display. Not leftover of unique-L
Cl(3,0) products. Not leftover of exist-opposite on the four x-probes. Not
another S^+ seed reprint. Uniqueness of incoming locks is not required.
Occupancy n is not used. No unique P_+. No Dijkstra. No Gram. No larger ball.
Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from itertools import product as cartesian
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/Z_SYMMETRIC_THREE_SITE_SAMETICK_UNION_OWN_CLIFFORD_EXIST_CHOICE_PLAQUETTE_PRODUCT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/Z_SYMMETRIC_THREE_SITE_SAMETICK_UNION_OWN_CLIFFORD_EXIST_CHOICE_PLAQUETTE_PRODUCT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Letter = Point | str
PlusSet = frozenset[Point] | str
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
BALL_SQ = 9
Z_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
    (NEG_E3, NEG_E1),
)
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
)
NNSEED_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
NSOPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
A: Point = (1, 0, 0)
B: Point = (1, 1, 1)
C: Point = (2, 0, 0)
D: Point = (1, 1, 0)
PROBES = {"A": A, "B": B, "C": C, "D": D}
FACE_Q: tuple[Point, ...] = (ORIGIN, E1, D, E2)
REVERSE_R: tuple[Point, ...] = (E1, D, B, (1, 0, 1))
SCALAR_P1: Multivector = (1, 0, 0, 0, 0, 0, 0, 0)
SCALAR_M1: Multivector = (-1, 0, 0, 0, 0, 0, 0, 0)
ZERO_MV: Multivector = (0, 0, 0, 0, 0, 0, 0, 0)
UNDEFINED = "UNDEFINED"
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
    "of S⁺ on #7188 Q and R are reported. Displayed, not adopted."
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


def unique_own_incoming_letter(incoming: tuple[Point, ...] | set[Point]) -> Letter:
    """Unique letter if the site's own earliest incoming locks are a singleton in NN."""
    unique = set(incoming)
    if len(unique) != 1:
        return UNDEFINED
    vector = next(iter(unique))
    if vector not in NN:
        return UNDEFINED
    return vector


def _blade_mul(left: int, right: int) -> tuple[int, int]:
    """Euclidean Cl(3,0) product of two basis blades encoded as 3-bit masks."""
    sign = 1
    for index in range(3):
        if (left >> index) & 1:
            lower = right & ((1 << index) - 1)
            if bin(lower).count("1") % 2:
                sign = -sign
    return sign, left ^ right


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
    if letter == UNDEFINED:
        return UNDEFINED
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
    if vector == UNDEFINED:
        return UNDEFINED
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
    """Cyclic Cl(3,0) product of four units, or UNDEFINED."""
    if any(letter == UNDEFINED for letter in letters):
        return UNDEFINED
    product: Multivector = SCALAR_P1
    for letter in letters:
        unit = letter_to_clifford(letter)
        if unit == UNDEFINED or not isinstance(unit, tuple):
            return UNDEFINED
        product = mv_mul(product, unit)
    return product


def hold_from_product(product: Multivector | str) -> str:
    """HOLD iff the product is the scalar ±1. UNDEFINED stays UNDEFINED."""
    if product == UNDEFINED:
        return UNDEFINED
    if not isinstance(product, tuple):
        raise TypeError(f"not a Cl(3,0) element: {product!r}")
    if is_scalar_pm1(product):
        return "hold"
    return "fail"


def exist_choice(
    plus_sets: tuple[PlusSet, ...],
) -> tuple[str, int | str, int | str]:
    """Exist-choice HOLD iff some pick from the four S^+ sets has U = ±1."""
    if any(plus == UNDEFINED for plus in plus_sets):
        return UNDEFINED, UNDEFINED, UNDEFINED
    if any(not isinstance(plus, frozenset) for plus in plus_sets):
        return UNDEFINED, UNDEFINED, UNDEFINED
    concrete = tuple(plus for plus in plus_sets if isinstance(plus, frozenset))
    if any(len(plus) == 0 for plus in concrete):
        return UNDEFINED, UNDEFINED, UNDEFINED
    n_picks = 0
    n_hold = 0
    for pick in cartesian(*concrete):
        n_picks += 1
        product = cycle_product(pick)
        if hold_from_product(product) == "hold":
            n_hold += 1
    status = "hold" if n_hold > 0 else "fail"
    return status, n_picks, n_hold


def unique_l_product(letters: tuple[Letter, ...]) -> Multivector | str:
    """Leftover: unique-L Cl(3,0) product. Mixed vertex ⇒ UNDEFINED."""
    return cycle_product(letters)


def existential_opposite(left: PlusSet, right: PlusSet) -> str:
    """Leftover exist-opposite of two S^+ sets. Empty or UNDEFINED ⇒ UNDEFINED."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        return UNDEFINED
    if not left or not right:
        return UNDEFINED
    for a in left:
        for b in right:
            if add(a, b) == ZERO:
                return "hold"
    return "fail"


def letter_display(letter: Letter) -> str:
    if letter == UNDEFINED:
        return UNDEFINED
    if not isinstance(letter, tuple):
        raise TypeError(f"letter is not a lock vector: {letter!r}")
    return LOCK_NAME[letter]


def set_display(locks: PlusSet) -> str:
    if locks == UNDEFINED:
        return UNDEFINED
    if not isinstance(locks, frozenset):
        raise TypeError(f"not an S^+ set: {locks!r}")
    if not locks:
        return "{}"
    names = ", ".join(LOCK_NAME[lock] for lock in NN if lock in locks)
    return "{" + names + "}"


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
    seeds: tuple[tuple[Point, Point], ...] = Z_SYMMETRIC_SEEDS,
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


def site_letter(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> Letter:
    if site not in ticks:
        return UNDEFINED
    return unique_own_incoming_letter(locks[site])


def s_plus(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> PlusSet:
    """S^+ at the site's own t. Unformed ⇒ UNDEFINED. No global T."""
    if site not in ticks:
        return UNDEFINED
    formation = ticks[site]
    neighbors: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        if neighbor == site:
            continue
        if neighbor not in ticks:
            continue
        if ticks[neighbor] > formation:
            continue
        neighbors.update(locks[neighbor])
    letter = unique_own_incoming_letter(locks[site])
    if letter != UNDEFINED and isinstance(letter, tuple):
        neighbors.add(letter)
    return frozenset(neighbors)


def cycle_s_plus(
    cycle: tuple[Point, ...],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> tuple[PlusSet, ...]:
    return tuple(s_plus(site, ticks, locks) for site in cycle)


def cycle_letters(
    cycle: tuple[Point, ...],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> tuple[Letter, ...]:
    return tuple(site_letter(site, ticks, locks) for site in cycle)


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

    print("exist-choice Cl(3,0) plaquette product reverse/face from S^+ on z-symmetric three-site")
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
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "cycles-in-host",
        FACE_Q == (ORIGIN, E1, D, E2)
        and REVERSE_R == (E1, D, B, (1, 0, 1))
        and set(FACE_Q) <= host
        and set(REVERSE_R) <= host
        and A in REVERSE_R
        and B in REVERSE_R
        and A in FACE_Q,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and add(NEG_E1, E1) == ZERO
        and add(NEG_E2, E2) == ZERO
        and add(E1, E2) == D
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(B)
        and in_ball(C)
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
        and letter_to_clifford(UNDEFINED) == UNDEFINED,
    )
    illegal_plus = cycle_product((E1, E2, E1, E2))
    illegal_minus = cycle_product((E1, NEG_E2, E1, E2))
    hold_pick_q = cycle_product((E1, E2, E2, E1))
    hold_pick_r = cycle_product((E2, E2, E2, E2))
    checks.check(
        "scalar-hold-identity",
        illegal_plus == SCALAR_M1
        and hold_from_product(illegal_plus) == "hold"
        and illegal_minus == SCALAR_P1
        and hold_from_product(illegal_minus) == "hold"
        and hold_pick_q == SCALAR_P1
        and hold_from_product(hold_pick_q) == "hold"
        and hold_pick_r == SCALAR_P1
        and hold_from_product(hold_pick_r) == "hold"
        and hold_from_product(mv_mul(g1, g2)) == "fail"
        and hold_from_product(UNDEFINED) == UNDEFINED
        and cycle_product((E1, UNDEFINED, E1, E2)) == UNDEFINED,
    )
    checks.check(
        "exist-choice-identity",
        exist_choice((frozenset(), frozenset({E1}), frozenset({E1}), frozenset({E1})))
        == (UNDEFINED, UNDEFINED, UNDEFINED)
        and exist_choice((UNDEFINED, frozenset({E1}), frozenset({E1}), frozenset({E1})))
        == (UNDEFINED, UNDEFINED, UNDEFINED)
        and exist_choice((frozenset({E1}), frozenset({E2}), frozenset({E1}), frozenset({E2})))
        == ("hold", 1, 1)
        and exist_choice((frozenset({E1}), frozenset({E2}), frozenset({E3}), frozenset({E1})))
        == ("fail", 1, 0)
        and exist_choice(
            (
                frozenset({E1, NEG_E1}),
                frozenset({E2}),
                frozenset({E2}),
                frozenset({E1}),
            )
        )
        == ("hold", 2, 2),
    )
    checks.check(
        "unique-own-incoming-letter-identity",
        unique_own_incoming_letter((E1,)) == E1
        and unique_own_incoming_letter((E1, E1)) == E1
        and unique_own_incoming_letter((NEG_E1,)) == NEG_E1
        and unique_own_incoming_letter((E1, E2)) == UNDEFINED
        and unique_own_incoming_letter((NEG_E2, E2)) == UNDEFINED
        and unique_own_incoming_letter((NEG_E2, NEG_E3, E3)) == UNDEFINED
        and unique_own_incoming_letter(()) == UNDEFINED,
    )

    ticks, locks = form()
    nn_ticks, nn_locks = form(NNSEED_SEEDS)
    nsopp_ticks, nsopp_locks = form(NSOPP_SEEDS)
    two_ticks, two_locks = form(TWO_SITE_SEEDS)

    q_plus = cycle_s_plus(FACE_Q, ticks, locks)
    r_plus = cycle_s_plus(REVERSE_R, ticks, locks)
    q_letters = cycle_letters(FACE_Q, ticks, locks)
    r_letters = cycle_letters(REVERSE_R, ticks, locks)
    face_status, n_picks_q, n_hold_q = exist_choice(q_plus)
    reverse_status, n_picks_r, n_hold_r = exist_choice(r_plus)
    unique_u_q = unique_l_product(q_letters)
    unique_u_r = unique_l_product(r_letters)
    unique_face = hold_from_product(unique_u_q)
    unique_reverse = hold_from_product(unique_u_r)
    probe_plus = {name: s_plus(PROBES[name], ticks, locks) for name in ("A", "B", "C", "D")}
    exist_opp_reverse = existential_opposite(probe_plus["A"], probe_plus["B"])
    exist_opp_face = existential_opposite(probe_plus["C"], probe_plus["D"])
    nn_q_plus = cycle_s_plus(FACE_Q, nn_ticks, nn_locks)
    nsopp_q_plus = cycle_s_plus(FACE_Q, nsopp_ticks, nsopp_locks)
    two_q_plus = cycle_s_plus(FACE_Q, two_ticks, two_locks)

    expected_q = (
        frozenset({E1, NEG_E1}),
        frozenset({E1, E2, NEG_E2, E3, NEG_E3}),
        frozenset({E1, E2}),
        frozenset({E1, E2}),
    )
    expected_r = (
        frozenset({E1, E2, NEG_E2, E3, NEG_E3}),
        frozenset({E1, E2}),
        frozenset({E1, E2}),
        frozenset({E1, NEG_E1, E2, NEG_E2}),
    )

    for name, cycle, plus_sets, letters in (
        ("Q", FACE_Q, q_plus, q_letters),
        ("R", REVERSE_R, r_plus, r_letters),
    ):
        bits = []
        for site, plus, letter in zip(cycle, plus_sets, letters):
            incoming = ",".join(LOCK_NAME[lock] for lock in sorted(locks[site]))
            bits.append(
                f"{site} t={ticks[site]} L={letter_display(letter)} "
                f"S+={set_display(plus)} incoming={incoming}"
            )
        print(f"{name}: " + " | ".join(bits))
    print(
        f"N_picks(Q)={n_picks_q} N_hold(Q)={n_hold_q} "
        f"N_picks(R)={n_picks_r} N_hold(R)={n_hold_r}"
    )
    print(
        f"unique-L U_Q={clifford_display(unique_u_q)} "
        f"unique-L U_R={clifford_display(unique_u_r)}"
    )
    print(f"reverse={reverse_status} face={face_status}")
    print("per_element: each lock vector in S^+ as a Cl(3,0) unit ±γ_i")
    print("per_site: scored only on face 4-cycle Q and reverse 4-cycle R in Euclidean B_3(0)")
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print(
        "per_block: four S^+ sets, N_picks, N_hold, and exist-choice hold iff some pick has U=±1"
    )
    print("lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed")

    checks.check(
        "theorem1-all-cycle-vertices-recorded",
        all(site in ticks for site in FACE_Q)
        and all(site in ticks for site in REVERSE_R)
        and set(FACE_Q) <= host
        and set(REVERSE_R) <= host,
    )
    checks.check(
        "theorem1-face-s-plus",
        q_plus == expected_q
        and ticks[ORIGIN] == 0
        and ticks[E1] == 3
        and ticks[D] == 2
        and ticks[E2] == 1
        and locks[ORIGIN] == {E1}
        and locks[E1] == {E2, NEG_E2}
        and locks[D] == {E1}
        and locks[E2] == {E2},
        str((tuple(set_display(s) for s in q_plus), {site: ticks[site] for site in FACE_Q})),
    )
    checks.check(
        "theorem1-reverse-s-plus",
        r_plus == expected_r
        and ticks[A] == 3
        and ticks[D] == 2
        and ticks[B] == 2
        and ticks[(1, 0, 1)] == 3
        and locks[A] == {E2, NEG_E2}
        and locks[D] == {E1}
        and locks[B] == {E1}
        and locks[(1, 0, 1)] == {E2, NEG_E2, NEG_E3},
        str((tuple(set_display(s) for s in r_plus), {site: ticks[site] for site in REVERSE_R})),
    )
    checks.check(
        "theorem1-unique-L-letters-undefined-on-mixed",
        q_letters == (E1, UNDEFINED, E1, E2)
        and r_letters == (UNDEFINED, E1, E1, UNDEFINED)
        and unique_u_q == UNDEFINED
        and unique_u_r == UNDEFINED
        and unique_face == UNDEFINED
        and unique_reverse == UNDEFINED,
        str((q_letters, r_letters)),
    )
    checks.check(
        "theorem1-n-picks-and-n-hold",
        n_picks_q == 40
        and n_hold_q == 12
        and n_picks_r == 80
        and n_hold_r == 24
        and n_picks_q == 2 * 5 * 2 * 2
        and n_picks_r == 5 * 2 * 2 * 4
        and n_hold_q < n_picks_q
        and n_hold_r < n_picks_r
        and n_hold_q > 0
        and n_hold_r > 0,
        str((n_picks_q, n_hold_q, n_picks_r, n_hold_r)),
    )
    checks.check(
        "theorem1-holding-picks-are-scalar-pm1",
        hold_from_product(cycle_product((E1, E2, E2, E1))) == "hold"
        and cycle_product((E1, E2, E2, E1)) == SCALAR_P1
        and E1 in q_plus[0]
        and E2 in q_plus[1]
        and E2 in q_plus[2]
        and E1 in q_plus[3]
        and hold_from_product(cycle_product((E2, E2, E2, E2))) == "hold"
        and cycle_product((E2, E2, E2, E2)) == SCALAR_P1
        and E2 in r_plus[0]
        and E2 in r_plus[1]
        and E2 in r_plus[2]
        and E2 in r_plus[3],
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse_status == "hold"
        and reverse_status != "fail"
        and reverse_status != UNDEFINED
        and n_hold_r == 24
        and unique_reverse == UNDEFINED
        and unique_reverse != reverse_status,
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and face_status != "fail"
        and face_status != UNDEFINED
        and n_hold_q == 12
        and unique_face == UNDEFINED
        and unique_face != face_status,
        face_status,
    )
    checks.check(
        "no-T_Q-in-letter",
        max(ticks[site] for site in FACE_Q) == 3
        and ticks[ORIGIN] != ticks[E1]
        and ticks[E2] != ticks[E1]
        and ticks[D] != ticks[E1]
        and all(
            isinstance(plus, frozenset) and len(plus) > 0 for plus in q_plus + r_plus
        ),
    )
    checks.check(
        "not-leftover-of-unique-L-cl30-product",
        unique_u_q == UNDEFINED
        and unique_u_r == UNDEFINED
        and unique_face == UNDEFINED
        and unique_reverse == UNDEFINED
        and face_status == "hold"
        and reverse_status == "hold"
        and q_letters[1] == UNDEFINED
        and r_letters[0] == UNDEFINED
        and r_letters[3] == UNDEFINED
        and q_plus[1] != frozenset()
        and r_plus[0] != frozenset()
        and r_plus[3] != frozenset(),
    )
    checks.check(
        "not-leftover-of-exist-opposite-nszopinx",
        exist_opp_reverse == "hold"
        and exist_opp_face == "hold"
        and probe_plus["A"] == expected_q[1]
        and probe_plus["B"] == expected_r[2]
        and probe_plus["C"] == frozenset({E1, E2, NEG_E2})
        and probe_plus["D"] == expected_q[2]
        and CLAIM_SCOPE.startswith("Reverse and face from exist-choice")
        and "exist-choice Cl(3,0) 4-cycle products" in CLAIM_SCOPE
        and exist_choice is not existential_opposite,
    )
    checks.check(
        "not-another-S-plus-seed-reprint",
        Z_SYMMETRIC_SEEDS != NNSEED_SEEDS
        and Z_SYMMETRIC_SEEDS != NSOPP_SEEDS
        and Z_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and nn_q_plus != q_plus
        and nsopp_q_plus != q_plus
        and two_q_plus != q_plus
        and nn_ticks[E1] != ticks[E1]
        and exist_choice(nn_q_plus) != (face_status, n_picks_q, n_hold_q),
        str((tuple(set_display(s) for s in nn_q_plus), tuple(set_display(s) for s in q_plus))),
    )
    checks.check(
        "x-probes-match-7188",
        PROBES["A"] == (1, 0, 0)
        and PROBES["B"] == (1, 1, 1)
        and PROBES["C"] == (2, 0, 0)
        and PROBES["D"] == (1, 1, 0)
        and ticks[A] == 3
        and ticks[B] == 2
        and ticks[C] == 4
        and ticks[D] == 2
        and A in FACE_Q
        and A in REVERSE_R
        and B in REVERSE_R
        and D in FACE_Q
        and D in REVERSE_R,
    )
    checks.check(
        "mixed-earliest-steps-kept-in-S-plus",
        locks[A] == {E2, NEG_E2}
        and unique_own_incoming_letter(locks[A]) == UNDEFINED
        and E2 in q_plus[1]
        and NEG_E2 in q_plus[1]
        and E1 in q_plus[1]
        and locks[(1, 0, 1)] == {E2, NEG_E2, NEG_E3}
        and unique_own_incoming_letter(locks[(1, 0, 1)]) == UNDEFINED
        and E2 in r_plus[3]
        and NEG_E2 in r_plus[3]
        and A not in {site for site, _lock in Z_SYMMETRIC_SEEDS},
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[A]) == 2
        and len(locks[(1, 0, 1)]) == 3
        and unique_own_incoming_letter(locks[A]) == UNDEFINED
        and unique_own_incoming_letter(locks[(1, 0, 1)]) == UNDEFINED
        and face_status == "hold"
        and reverse_status == "hold",
    )
    checks.check(
        "s-plus-includes-own-lock-when-defined",
        q_letters[0] == E1
        and E1 in q_plus[0]
        and NEG_E1 in q_plus[0]
        and q_letters[3] == E2
        and E2 in q_plus[3]
        and E1 in q_plus[3]
        and q_letters[2] == E1
        and E1 in q_plus[2],
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-s-plus-and-counts",
        "S^+(0) = {+e_1, −e_1}" in note
        and "S^+(e_1) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S^+(e_1+e_2) = {+e_1, +e_2}" in note
        and "S^+(e_2) = {+e_1, +e_2}" in note
        and "S^+((1,0,0)) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S^+((1,1,0)) = {+e_1, +e_2}" in note
        and "S^+((1,1,1)) = {+e_1, +e_2}" in note
        and "S^+((1,0,1)) = {+e_1, −e_1, +e_2, −e_2}" in note
        and "N_picks(Q) = 40" in note
        and "N_hold(Q) = 12" in note
        and "N_picks(R) = 80" in note
        and "N_hold(R) = 24" in note
        and "t(0)=0" in note
        and "t(e_1)=3" in note
        and "t(e_1+e_2)=2" in note
        and "t(e_2)=1" in note
        and "t(1,0,0)=3" in note
        and "t(1,1,1)=2" in note
        and "t(1,0,1)=3" in note,
    )
    checks.check(
        "note-reports-unique-L-and-status",
        "unique-L U_Q = UNDEFINED" in note
        and "unique-L U_R = UNDEFINED" in note
        and "L(e_1) = UNDEFINED" in note
        and "L(1,0,0) = UNDEFINED" in note
        and "L(1,0,1) = UNDEFINED" in note
        and "Reverse: hold" in note
        and "Face: hold" in note
        and "scalar ±1" in note
        and "Cl(3,0)" in note
        and "(+e_1, +e_2, +e_2, +e_1)" in note
        and "(+e_2, +e_2, +e_2, +e_2)" in note,
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
        and "no T_Q" in normalized_note
        and "no global T" in normalized_note,
    )
    checks.check(
        "note-not-unique-L-or-exist-opposite-or-reprint",
        "not leftover of unique-L" in normalized_note
        and "not leftover of exist-opposite" in normalized_note
        and "not another S^+" in note.replace("`", ""),
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
        '    "docs/Z_SYMMETRIC_THREE_SITE_SAMETICK_UNION_OWN_CLIFFORD_EXIST_CHOICE_PLAQUETTE_PRODUCT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "identity-gates-present",
        "exist_choice" in defined_fns
        and "s_plus" in defined_fns
        and "cycle_product" in defined_fns
        and "hold_from_product" in defined_fns
        and "letter_to_clifford" in defined_fns
        and "unique_own_incoming_letter" in defined_fns
        and "form" in defined_fns
        and "mv_mul" in defined_fns,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[A] == 3
        and set(ticks) <= host,
    )
    checks.check(
        "source-letter-from-exist-choice-cl30",
        "exist_choice" in defined_fns
        and "s_plus" in defined_fns
        and "cycle_product" in defined_fns
        and "letter_to_clifford" in defined_fns
        and "unique_l_product" in defined_fns
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
