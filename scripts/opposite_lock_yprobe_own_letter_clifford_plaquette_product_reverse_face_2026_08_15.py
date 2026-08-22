#!/usr/bin/env python3
"""Own-letter Cl(3,0) cyclic plaquette product reverse/face on HOLDING #7167.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and -e_1. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters. L(q) is q's own unique incoming lock in
{±e_i} at t(q); mixed earliest steps make L(q) UNDEFINED. Identify ±e_i with
generators γ_i of Cl(3,0): γ_i^2=+1 and γ_i γ_j=-γ_j γ_i for i≠j; -e_i maps
to -γ_i. This is a displayed algebra, not a cube-Pauli Lattice action. Face
plaquette Q is the 4-cycle (0, e_1, e_1+e_2, e_2). U_Q is the Cl(3,0) product
of the four own letters, each at that site's own t, with no T_Q. Face HOLD
iff U_Q is the scalar ±1. Reverse 4-cycle R is
((0,1,0), (1,1,0), (1,1,1), (0,1,1)). U_R is the product of those four own
letters at each vertex's own t. Reverse HOLD iff U_R is the scalar ±1. Any
UNDEFINED letter or unrecorded vertex in B_3(0) makes the product UNDEFINED.
Same process as the nsopp y-probe same-tick union own display. Not leftover
of exist-opposite in S^+. Not leftover of vector-sum / opposite-vertex
holonomy. Not leftover of mixed-letter Cl(3,0) products on the z-symmetric
three-site process. Not a 6-NN star. Uniqueness of incoming locks is not
required. Occupancy n is not used. No unique P_+. No Dijkstra. No Gram. No
larger ball.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_YPROBE_OWN_LETTER_CLIFFORD_PLAQUETTE_PRODUCT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_YPROBE_OWN_LETTER_CLIFFORD_PLAQUETTE_PRODUCT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Letter = Point | str
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
NSOPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
Z_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
    (NEG_E3, NEG_E1),
)
NNSEED_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
)
A: Point = (0, 1, 0)
B: Point = (1, 1, 1)
FACE_Q: tuple[Point, ...] = (ORIGIN, E1, (1, 1, 0), E2)
REVERSE_R: tuple[Point, ...] = (E2, (1, 1, 0), B, (0, 1, 1))
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
    "Reverse and face from Cl(3,0) own-letter products "
    "on the #7167 y-probe process are reported. Displayed, not adopted."
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
        return "UNDEFINED"
    vector = next(iter(unique))
    if vector not in NN:
        return "UNDEFINED"
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
    """Cyclic Cl(3,0) product of own letters, or UNDEFINED."""
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
    seeds: tuple[tuple[Point, Point], ...] = NSOPP_SEEDS,
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
        return "UNDEFINED"
    return unique_own_incoming_letter(locks[site])


def cycle_letters(
    cycle: tuple[Point, ...],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> tuple[Letter, ...]:
    return tuple(site_letter(site, ticks, locks) for site in cycle)


def common_tick_recorded(
    cycle: tuple[Point, ...],
    ticks: dict[Point, int],
    common: int,
) -> bool:
    return all(site in ticks and ticks[site] <= common for site in cycle)


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

    print("own-letter Cl(3,0) plaquette product reverse/face on nsopp y-probe")
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
        FACE_Q == (ORIGIN, E1, (1, 1, 0), E2)
        and REVERSE_R == (E2, (1, 1, 0), B, (0, 1, 1))
        and set(FACE_Q) <= host
        and set(REVERSE_R) <= host
        and A in REVERSE_R
        and B in REVERSE_R
        and A == E2,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and add(NEG_E1, E1) == ZERO
        and add(NEG_E2, E2) == ZERO
        and add(E1, E2) == (1, 1, 0)
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(B)
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
    illegal_plus = cycle_product((E1, E2, E1, E2))
    illegal_minus = cycle_product((E1, NEG_E2, E1, E2))
    checks.check(
        "scalar-hold-identity",
        illegal_plus == SCALAR_M1
        and hold_from_product(illegal_plus) == "hold"
        and illegal_minus == SCALAR_P1
        and hold_from_product(illegal_minus) == "hold"
        and hold_from_product(mv_mul(g1, g2)) == "fail"
        and hold_from_product("UNDEFINED") == "UNDEFINED"
        and cycle_product((E1, "UNDEFINED", E1, E2)) == "UNDEFINED",
    )
    checks.check(
        "unique-own-incoming-letter-identity",
        unique_own_incoming_letter((E1,)) == E1
        and unique_own_incoming_letter((E1, E1)) == E1
        and unique_own_incoming_letter((NEG_E1,)) == NEG_E1
        and unique_own_incoming_letter((E1, E2)) == "UNDEFINED"
        and unique_own_incoming_letter((NEG_E2, E2)) == "UNDEFINED"
        and unique_own_incoming_letter((NEG_E2, NEG_E3, E3)) == "UNDEFINED"
        and unique_own_incoming_letter(()) == "UNDEFINED",
    )

    ticks, locks = form()
    nn_ticks, nn_locks = form(NNSEED_SEEDS)
    z_ticks, z_locks = form(Z_SYMMETRIC_SEEDS)
    two_ticks, two_locks = form(TWO_SITE_SEEDS)

    q_letters = cycle_letters(FACE_Q, ticks, locks)
    r_letters = cycle_letters(REVERSE_R, ticks, locks)
    u_q = cycle_product(q_letters)
    u_r = cycle_product(r_letters)
    face_status = hold_from_product(u_q)
    reverse_status = hold_from_product(u_r)
    t_q = max(ticks[site] for site in FACE_Q)
    t_r_min = min(ticks[A], ticks[B])
    opp_q = opposite_vertex_hold(q_letters)
    opp_r_at_min = (
        "UNDEFINED"
        if not common_tick_recorded(REVERSE_R, ticks, t_r_min)
        else opposite_vertex_hold(r_letters)
    )
    sum_q = vector_sum(q_letters)
    sum_r = vector_sum(r_letters)
    nn_q = cycle_letters(FACE_Q, nn_ticks, nn_locks)
    z_q = cycle_letters(FACE_Q, z_ticks, z_locks)
    z_r = cycle_letters(REVERSE_R, z_ticks, z_locks)

    for name, cycle, letters in (("Q", FACE_Q, q_letters), ("R", REVERSE_R, r_letters)):
        bits = []
        for site, letter in zip(cycle, letters):
            incoming = ",".join(
                LOCK_NAME[lock] for lock in sorted(locks[site])
            )
            bits.append(
                f"{site} t={ticks[site]} L={letter_display(letter)} incoming={incoming}"
            )
        print(f"{name}: " + " | ".join(bits))
    print(f"U_Q={clifford_display(u_q)} U_R={clifford_display(u_r)}")
    print(
        f"reverse={reverse_status} face={face_status} "
        f"T_Q={t_q} leftover_T_R_min={t_r_min} L(A)={letter_display(site_letter(A, ticks, locks))}"
    )
    print("per_element: each own incoming lock as a Cl(3,0) unit ±γ_i")
    print("per_site: scored only on face 4-cycle Q and reverse 4-cycle R in Euclidean B_3(0)")
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print("per_block: four letters and one Cl(3,0) product per cycle, hold iff scalar ±1")
    print("lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed")

    checks.check(
        "theorem1-all-cycle-vertices-recorded",
        all(site in ticks for site in FACE_Q)
        and all(site in ticks for site in REVERSE_R)
        and set(FACE_Q) <= host
        and set(REVERSE_R) <= host,
    )
    checks.check(
        "theorem1-face-letters",
        q_letters == (E1, "UNDEFINED", "UNDEFINED", NEG_E1)
        and ticks[ORIGIN] == 0
        and ticks[E1] == 3
        and ticks[(1, 1, 0)] == 3
        and ticks[E2] == 0
        and locks[ORIGIN] == {E1}
        and locks[E1] == {E2, E3, NEG_E3}
        and locks[(1, 1, 0)] == {NEG_E2, E3, NEG_E3}
        and locks[E2] == {NEG_E1},
        str((q_letters, {site: ticks[site] for site in FACE_Q})),
    )
    checks.check(
        "theorem1-reverse-letters",
        r_letters == (NEG_E1, "UNDEFINED", E1, E3)
        and ticks[A] == 0
        and ticks[(1, 1, 0)] == 3
        and ticks[B] == 2
        and ticks[(0, 1, 1)] == 1
        and locks[A] == {NEG_E1}
        and locks[(1, 1, 0)] == {NEG_E2, E3, NEG_E3}
        and locks[B] == {E1}
        and locks[(0, 1, 1)] == {E3},
        str((r_letters, {site: ticks[site] for site in REVERSE_R})),
    )
    checks.check(
        "theorem1-products-undefined",
        u_q == "UNDEFINED"
        and u_r == "UNDEFINED"
        and u_q != SCALAR_P1
        and u_q != SCALAR_M1
        and u_r != SCALAR_P1
        and u_r != SCALAR_M1,
        str((clifford_display(u_q), clifford_display(u_r))),
    )
    checks.check(
        "theorem2-reverse-undefined",
        reverse_status == "UNDEFINED"
        and reverse_status != "hold"
        and reverse_status != "fail"
        and "UNDEFINED" in r_letters,
        reverse_status,
    )
    checks.check(
        "theorem3-face-undefined",
        face_status == "UNDEFINED"
        and face_status != "hold"
        and face_status != "fail"
        and q_letters[1] == "UNDEFINED"
        and q_letters[2] == "UNDEFINED",
        face_status,
    )
    checks.check(
        "unique-L-A-does-not-define-products",
        site_letter(A, ticks, locks) == NEG_E1
        and locks[A] == {NEG_E1}
        and q_letters[3] == NEG_E1
        and r_letters[0] == NEG_E1
        and u_q == "UNDEFINED"
        and u_r == "UNDEFINED",
    )
    checks.check(
        "no-T_Q-in-letter",
        t_q == 3
        and t_q == ticks[E1]
        and t_q == ticks[(1, 1, 0)]
        and ticks[ORIGIN] != t_q
        and ticks[E2] != t_q
        and u_q == "UNDEFINED",
    )
    checks.check(
        "not-leftover-of-opposite-vertex-holonomy",
        opp_q == "UNDEFINED"
        and opp_r_at_min == "UNDEFINED"
        and not common_tick_recorded(REVERSE_R, ticks, t_r_min)
        and ticks[A] == 0
        and t_r_min == 0
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED",
    )
    checks.check(
        "not-leftover-of-vector-sum",
        sum_q == "UNDEFINED"
        and sum_r == "UNDEFINED"
        and u_q == "UNDEFINED"
        and hold_from_product is not vector_sum,
    )
    checks.check(
        "not-leftover-of-exist-opposite-S-plus",
        "S^+" not in CLAIM_SCOPE
        and "Cl(3,0) own-letter products" in CLAIM_SCOPE
        and face_status == "UNDEFINED"
        and reverse_status == "UNDEFINED"
        and unique_own_incoming_letter(locks[A]) == NEG_E1,
    )
    checks.check(
        "not-nnseed-or-z-symmetric-reprint",
        NSOPP_SEEDS != NNSEED_SEEDS
        and NSOPP_SEEDS != Z_SYMMETRIC_SEEDS
        and NSOPP_SEEDS != TWO_SITE_SEEDS
        and nn_q != q_letters
        and z_q != q_letters
        and z_r != r_letters
        and nn_ticks[E1] != ticks[E1],
        str((nn_q, z_q, q_letters)),
    )
    checks.check(
        "mutation-picking-a-mixed-letter-would-hold-or-fail-face",
        hold_from_product(cycle_product((E1, E2, NEG_E2, NEG_E1))) == "hold"
        and hold_from_product(cycle_product((E1, E2, E3, NEG_E1))) == "fail"
        and hold_from_product(cycle_product((E1, E3, E3, NEG_E1))) == "hold"
        and q_letters[1] == "UNDEFINED"
        and q_letters[2] == "UNDEFINED"
        and face_status == "UNDEFINED"
        and face_status != "hold",
    )
    checks.check(
        "mutation-picking-mixed-reverse-letters-disagrees",
        hold_from_product(cycle_product((NEG_E1, E3, E1, E3))) == "hold"
        and hold_from_product(cycle_product((NEG_E1, NEG_E3, E1, E3))) == "hold"
        and hold_from_product(cycle_product((NEG_E1, NEG_E2, E1, E3))) == "fail"
        and r_letters[1] == "UNDEFINED"
        and reverse_status == "UNDEFINED",
    )
    checks.check(
        "mixed-earliest-steps-at-e1-and-D",
        locks[E1] == {E2, E3, NEG_E3}
        and locks[(1, 1, 0)] == {NEG_E2, E3, NEG_E3}
        and unique_own_incoming_letter(locks[E1]) == "UNDEFINED"
        and unique_own_incoming_letter(locks[(1, 1, 0)]) == "UNDEFINED"
        and E1 not in {site for site, _lock in NSOPP_SEEDS},
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[E1]) == 3
        and len(locks[(1, 1, 0)]) == 3
        and len(locks[A]) == 1
        and unique_own_incoming_letter(locks[A]) == NEG_E1
        and unique_own_incoming_letter(locks[E1]) == "UNDEFINED"
        and unique_own_incoming_letter(locks[(1, 1, 0)]) == "UNDEFINED",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-letters",
        "L(0) = +e_1" in note
        and "L(e_1) = UNDEFINED" in note
        and "L(e_1+e_2) = UNDEFINED" in note
        and "L(e_2) = −e_1" in note
        and "L(0,1,0) = −e_1" in note
        and "L(1,1,0) = UNDEFINED" in note
        and "L(1,1,1) = +e_1" in note
        and "L(0,1,1) = +e_3" in note
        and "t(0)=0" in note
        and "t(e_1)=3" in note
        and "t(e_1+e_2)=3" in note
        and "t(e_2)=0" in note
        and "t(0,1,0)=0" in note
        and "t(1,1,1)=2" in note
        and "t(0,1,1)=1" in note
        and "L(A)=−e_1" in note,
    )
    checks.check(
        "note-reports-products-and-status",
        "U_Q = UNDEFINED" in note
        and "U_R = UNDEFINED" in note
        and "Reverse: UNDEFINED" in note
        and "Face: UNDEFINED" in note
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
        and "own incoming" in normalized_note
        and "no T_Q" in normalized_note,
    )
    checks.check(
        "note-not-vector-sum-or-exist-opposite",
        "not leftover of vector-sum" in normalized_note
        and "not leftover of opposite-vertex" in normalized_note
        and "not leftover of exist-opposite" in normalized_note
        and "not a 6-NN star" in normalized_note,
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
        '    "docs/OPPOSITE_LOCK_YPROBE_OWN_LETTER_CLIFFORD_PLAQUETTE_PRODUCT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def cycle_product(" in source
        and "def hold_from_product(" in source
        and "def letter_to_clifford(" in source
        and "def unique_own_incoming_letter(" in source
        and "def form(" in source
        and "def mv_mul(" in source,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[A] == 0
        and ticks[B] == 2
        and set(ticks) <= host,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "source-letter-from-own-cl30-product",
        "cycle_product" in defined_fns
        and "hold_from_product" in defined_fns
        and "letter_to_clifford" in defined_fns
        and "unique_own_incoming_letter" in defined_fns
        and "form" in defined_fns
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
