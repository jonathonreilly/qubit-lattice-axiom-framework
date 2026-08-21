#!/usr/bin/env python3
"""Named rank-1 PVM letters on four opposite-lock y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed is
{0, (0,1,0)} with locks +e_1 and -e_1. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. At each y-probe's formation, n is the occupancy kernel from
already-recorded six-neighbor occupancy. A is a seed: same-tick partner is
not already-recorded. If n≠0 the named rank-1 P_± letters are {+,−}. Letters
do not feed n and are not incoming {±e_i}. Uniqueness is not required.
"""

from __future__ import annotations

import ast
from collections import deque
from fractions import Fraction
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_YPROBE_PVM_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_YPROBE_PVM_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Vec3 = tuple[Fraction, Fraction, Fraction]
Cpx = tuple[Fraction, Fraction]
Mat = tuple[tuple[Cpx, Cpx], tuple[Cpx, Cpx]]
ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
MINUS_E1: Point = (-1, 0, 0)
NN: tuple[Point, ...] = (
    E1,
    MINUS_E1,
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)
AXES: tuple[Point, Point, Point] = (E1, E2, E3)
PVM_LETTERS = frozenset({"+", "-"})
ZERO_N: Vec3 = (Fraction(0), Fraction(0), Fraction(0))
BALL_SQ = 9
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, MINUS_E1),
)
PROBES = {
    "A": (0, 1, 0),
    "B": (1, 1, 1),
    "C": (0, 2, 0),
    "D": (1, 1, 0),
}
EXPECTED_N = {
    "A": (Fraction(0), Fraction(0), Fraction(0)),
    "B": (Fraction(-1, 3), Fraction(0), Fraction(0)),
    "C": (Fraction(0), Fraction(-1, 3), Fraction(0)),
    "D": (Fraction(-1, 3), Fraction(1, 3), Fraction(0)),
}
EXPECTED_K = {"A": 0, "B": 1, "C": 1, "D": 2}
FORBIDDEN_NOTE_TOKENS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "Gram",
    "L1",
    "Runner cache",
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


def cz(re: int | Fraction, im: int | Fraction = 0) -> Cpx:
    return (Fraction(re), Fraction(im))


def cadd(left: Cpx, right: Cpx) -> Cpx:
    return (left[0] + right[0], left[1] + right[1])


def cmul(left: Cpx, right: Cpx) -> Cpx:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def cscale(coeff: Fraction, value: Cpx) -> Cpx:
    return (coeff * value[0], coeff * value[1])


def madd(left: Mat, right: Mat) -> Mat:
    return (
        (cadd(left[0][0], right[0][0]), cadd(left[0][1], right[0][1])),
        (cadd(left[1][0], right[1][0]), cadd(left[1][1], right[1][1])),
    )


def mmul(left: Mat, right: Mat) -> Mat:
    return (
        (
            cadd(cmul(left[0][0], right[0][0]), cmul(left[0][1], right[1][0])),
            cadd(cmul(left[0][0], right[0][1]), cmul(left[0][1], right[1][1])),
        ),
        (
            cadd(cmul(left[1][0], right[0][0]), cmul(left[1][1], right[1][0])),
            cadd(cmul(left[1][0], right[0][1]), cmul(left[1][1], right[1][1])),
        ),
    )


def mscale(coeff: Fraction, mat: Mat) -> Mat:
    return (
        (cscale(coeff, mat[0][0]), cscale(coeff, mat[0][1])),
        (cscale(coeff, mat[1][0]), cscale(coeff, mat[1][1])),
    )


def mtrace(mat: Mat) -> Cpx:
    return cadd(mat[0][0], mat[1][1])


def I2() -> Mat:
    zero, one = cz(0), cz(1)
    return ((one, zero), (zero, one))


def SX() -> Mat:
    zero, one = cz(0), cz(1)
    return ((zero, one), (one, zero))


def SY() -> Mat:
    zero, i, mi = cz(0), cz(0, 1), cz(0, -1)
    return ((zero, mi), (i, zero))


def SZ() -> Mat:
    zero, one, mone = cz(0), cz(1), cz(-1)
    return ((one, zero), (zero, mone))


def hamiltonian(a: int, b: int, c: int) -> Mat:
    return madd(
        madd(mscale(Fraction(a), SX()), mscale(Fraction(b), SY())),
        mscale(Fraction(c), SZ()),
    )


def zero_mat() -> Mat:
    z = cz(0)
    return ((z, z), (z, z))


def pvm_projectors_k1(a: int, b: int, c: int) -> tuple[Mat, Mat]:
    """Named rank-1 P± for H=aσx+bσy+cσz with k=1."""
    if a * a + b * b + c * c != 1:
        raise ValueError("named k=1 projectors require a^2+b^2+c^2=1")
    ham = hamiltonian(a, b, c)
    half = Fraction(1, 2)
    pplus = mscale(half, madd(I2(), ham))
    pminus = mscale(half, madd(I2(), mscale(Fraction(-1), ham)))
    return pplus, pminus


def pvm_probs_k1(a: int, b: int, c: int) -> tuple[Fraction, Fraction]:
    """Identity gate: Tr(ρ P±) for named rank-1 projectors at k=1."""
    pplus, pminus = pvm_projectors_k1(a, b, c)
    ham = hamiltonian(a, b, c)
    half = Fraction(1, 2)
    rho = mscale(half, madd(I2(), mscale(Fraction(1, 3), ham)))
    tp = mtrace(mmul(rho, pplus))
    tm = mtrace(mmul(rho, pminus))
    if tp[1] != 0 or tm[1] != 0:
        raise ValueError("named k=1 traces left the reals")
    return tp[0], tm[0]


def occupancy(site: Point, formed: frozenset[Point], letter: str | None = None) -> int:
    """Occupancy is 1 on already-recorded sites. A PVM letter does not feed n."""
    if letter is not None and letter not in PVM_LETTERS:
        raise ValueError(f"letter must be + or -, got {letter!r}")
    return 1 if site in formed else 0


def n_vector(site: Point, formed: frozenset[Point]) -> Vec3:
    """Occupancy kernel n_μ = (o_{+μ} − o_{−μ}) / 3."""
    components = []
    for axis in AXES:
        plus = occupancy(add(site, axis), formed)
        minus = occupancy(add(site, (-axis[0], -axis[1], -axis[2])), formed)
        components.append(Fraction(plus - minus, 3))
    return (components[0], components[1], components[2])


def k_value(n: Vec3) -> int:
    squared = sum((3 * component) ** 2 for component in n)
    if squared.denominator != 1:
        raise ValueError(f"k left Q: {squared}")
    return int(squared)


def abc_from_n(n: Vec3) -> tuple[int, int, int]:
    return (int(3 * n[0]), int(3 * n[1]), int(3 * n[2]))


def pvm_letters_from_n(n: Vec3) -> frozenset[str]:
    """Named rank-1 P_± letters from occupancy kernel n. Not incoming {±e_i}."""
    if n == ZERO_N:
        return frozenset()
    return frozenset(PVM_LETTERS)


def unique_plus_from_n(n: Vec3) -> frozenset[str]:
    """Refused unique f(n): P_+ along n. Not used for reverse/face."""
    if n == ZERO_N:
        return frozenset()
    return frozenset({"+"})


def ndot_letter_from_n(n: Vec3, direction: Point) -> frozenset[str]:
    """Refused ndot: unique letter sign(n·v). Not used for reverse/face."""
    contraction = n[0] * direction[0] + n[1] * direction[1] + n[2] * direction[2]
    if contraction == 0:
        return frozenset()
    return frozenset({"+"} if contraction > 0 else {"-"})


def letter_report(letters: frozenset[str]) -> str:
    if not letters:
        return "UNDEFINED"
    if letters == PVM_LETTERS:
        return "{+,−}"
    only = next(iter(letters))
    return only


def hold_report(
    n_true: int,
    n_total: int,
    *,
    defined: bool,
) -> str:
    if not defined:
        return "UNDEFINED"
    if n_total == 0 or n_true == 0:
        return "none"
    if n_true == n_total:
        return "all"
    return "some"


def hamiltonian_square_k(a: int, b: int, c: int) -> int:
    """Identity gate: Pauli H=aσx+bσy+cσz satisfies H^2 = (a^2+b^2+c^2) I."""
    return a * a + b * b + c * c


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
    """Earliest formation and incoming locks on B_3(0)."""
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


def already_recorded(site: Point, ticks: dict[Point, int]) -> frozenset[Point]:
    formation = ticks[site]
    return frozenset(other for other, tick in ticks.items() if tick < formation)


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

    print("named rank-1 PVM-letter reverse/face on four opposite-lock y-probes")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "claim_scope: Reverse and face from named rank-1 PVM letters "
        "on the four nsopp y-probes are reported. Displayed, not adopted."
    )

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
    checks.check(
        "host-is-euclidean-b3",
        ORIGIN in host and len(host) == 123 and BALL_SQ == 9,
    )
    checks.check(
        "four-y-probes-in-host",
        tuple(PROBES[name] for name in ("A", "B", "C", "D"))
        == ((0, 1, 0), (1, 1, 1), (0, 2, 0), (1, 1, 0))
        and {PROBES["A"], PROBES["B"], PROBES["C"], PROBES["D"]} <= host,
    )
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "perp-step-blocks-parallel",
        perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((0, 4, 0)),
    )

    pplus_b, pminus_b = pvm_projectors_k1(-1, 0, 0)
    pplus_c, pminus_c = pvm_projectors_k1(0, -1, 0)
    tp_b, tm_b = pvm_probs_k1(-1, 0, 0)
    tp_c, tm_c = pvm_probs_k1(0, -1, 0)
    ham_c = hamiltonian(0, -1, 0)
    checks.check(
        "named-pvm-rank1-projectors",
        mtrace(pplus_b) == cz(1)
        and mtrace(pminus_b) == cz(1)
        and pplus_b == mmul(pplus_b, pplus_b)
        and pminus_b == mmul(pminus_b, pminus_b)
        and mmul(pplus_b, pminus_b) == zero_mat()
        and pplus_c == mmul(pplus_c, pplus_c)
        and pminus_c == mmul(pminus_c, pminus_c)
        and mmul(pplus_c, pminus_c) == zero_mat()
        and mmul(ham_c, ham_c) == I2(),
    )
    checks.check(
        "named-pvm-traces-k1",
        tp_b == Fraction(2, 3)
        and tm_b == Fraction(1, 3)
        and tp_c == Fraction(2, 3)
        and tm_c == Fraction(1, 3)
        and tp_b + tm_b == 1
        and tp_c + tm_c == 1,
    )
    checks.check(
        "named-pvm-letters-are-plus-minus",
        PVM_LETTERS == frozenset({"+", "-"})
        and E1 not in PVM_LETTERS
        and MINUS_E1 not in PVM_LETTERS
        and E2 not in PVM_LETTERS,
    )

    ticks, locks = form()
    kernels: dict[str, Vec3] = {}
    letters: dict[str, frozenset[str]] = {}
    occupancies: dict[str, list[Point]] = {}
    for name, site in PROBES.items():
        formed_before = already_recorded(site, ticks)
        n = n_vector(site, formed_before)
        kernels[name] = n
        letters[name] = pvm_letters_from_n(n)
        occupied = [
            add(site, step) for step in NN if occupancy(add(site, step), formed_before)
        ]
        occupancies[name] = occupied
        a, b, c = abc_from_n(n)
        print(
            f"{name} n=({n[0]},{n[1]},{n[2]}) k={k_value(n)} "
            f"abc=({a},{b},{c}) L={letter_report(letters[name])} "
            f"incoming={sorted(locks.get(site, ()))}"
        )

    checks.check(
        "theorem1-n-A-zero-undefined",
        kernels["A"] == EXPECTED_N["A"]
        and k_value(kernels["A"]) == EXPECTED_K["A"]
        and letters["A"] == frozenset()
        and letter_report(letters["A"]) == "UNDEFINED",
        str(kernels["A"]),
    )
    checks.check(
        "theorem1-n-B",
        kernels["B"] == EXPECTED_N["B"]
        and k_value(kernels["B"]) == EXPECTED_K["B"]
        and letters["B"] == PVM_LETTERS,
        str(kernels["B"]),
    )
    checks.check(
        "theorem1-n-C",
        kernels["C"] == EXPECTED_N["C"]
        and k_value(kernels["C"]) == EXPECTED_K["C"]
        and letters["C"] == PVM_LETTERS,
        str(kernels["C"]),
    )
    checks.check(
        "theorem1-n-D",
        kernels["D"] == EXPECTED_N["D"]
        and k_value(kernels["D"]) == EXPECTED_K["D"]
        and letters["D"] == PVM_LETTERS,
        str(kernels["D"]),
    )
    checks.check(
        "theorem1-letters-A-undefined-others-pm",
        letters["A"] == frozenset()
        and all(letters[name] == PVM_LETTERS for name in ("B", "C", "D"))
        and all(letter_report(letters[name]) == "{+,−}" for name in ("B", "C", "D")),
    )
    checks.check(
        "theorem1-neighbor-occupancy",
        occupancies["A"] == []
        and occupancies["B"] == [(0, 1, 1)]
        and occupancies["C"] == [(0, 1, 0)]
        and set(occupancies["D"])
        == {(0, 1, 0), (1, 2, 0), (1, 1, 1), (1, 1, -1)},
    )
    checks.check(
        "n-nonzero-assigns-both-letters",
        pvm_letters_from_n(ZERO_N) == frozenset()
        and pvm_letters_from_n(EXPECTED_N["C"]) == PVM_LETTERS
        and pvm_letters_from_n(EXPECTED_N["A"]) == frozenset(),
    )
    ham_d = hamiltonian(*abc_from_n(kernels["D"]))
    checks.check(
        "hamiltonian-square-matches-k",
        all(
            hamiltonian_square_k(*abc_from_n(kernels[name])) == k_value(kernels[name])
            for name in ("A", "B", "C", "D")
        )
        and mmul(hamiltonian(*abc_from_n(kernels["B"])), hamiltonian(*abc_from_n(kernels["B"])))
        == I2()
        and mmul(hamiltonian(*abc_from_n(kernels["C"])), hamiltonian(*abc_from_n(kernels["C"])))
        == I2()
        and mmul(ham_d, ham_d) == mscale(Fraction(2), I2()),
    )
    checks.check(
        "incoming-locks-are-nn-steps-not-letters",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D"))
        and all(not (locks[PROBES[name]] & PVM_LETTERS) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["D"]]) == 3 and letters["D"] == PVM_LETTERS,
        str(sorted(locks[PROBES["D"]])),
    )
    checks.check(
        "two-site-opposite-seed-locks",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {MINUS_E1}
        and PROBES["A"] == E2,
    )

    formed_before_a = already_recorded(PROBES["A"], ticks)
    checks.check(
        "seed-occupancy-excludes-same-tick-partner",
        ORIGIN not in formed_before_a
        and formed_before_a == frozenset()
        and ticks[ORIGIN] == ticks[PROBES["A"]] == 0
        and occupancy(ORIGIN, formed_before_a) == 0,
    )
    checks.check(
        "a-is-seed-not-grown-incoming",
        ticks[PROBES["A"]] == 0
        and locks[PROBES["A"]] == {MINUS_E1}
        and kernels["A"] == ZERO_N,
    )
    checks.check(
        "formation-member-not-attached",
        ticks[PROBES["A"]] == 0 and kernels["A"] == ZERO_N and PROBES["A"] in ticks,
    )

    defined_reverse = bool(letters["A"]) and bool(letters["B"])
    defined_face = bool(letters["C"]) and bool(letters["D"])
    reverse_combos = tuple(product(sorted(letters["A"]), sorted(letters["B"])))
    face_combos = tuple(product(sorted(letters["C"]), sorted(letters["D"])))
    reverse_hits = sum(combo[0] == "+" and combo[1] == "-" for combo in reverse_combos)
    face_hits = sum(combo[0] == "+" and combo[1] == "-" for combo in face_combos)
    reverse_status = hold_report(
        reverse_hits, len(reverse_combos), defined=defined_reverse
    )
    face_status = hold_report(face_hits, len(face_combos), defined=defined_face)
    print(
        f"reverse_combos={len(reverse_combos)} reverse_hits={reverse_hits} "
        f"face_combos={len(face_combos)} face_hits={face_hits}"
    )
    print(f"reverse={reverse_status} face={face_status}")

    unique_plus = {
        name: unique_plus_from_n(kernels[name]) for name in ("A", "B", "C", "D")
    }
    unique_face_combos = tuple(
        product(sorted(unique_plus["C"]), sorted(unique_plus["D"]))
    )
    unique_face = sum(combo[0] == "+" and combo[1] == "-" for combo in unique_face_combos)
    unique_face_defined = bool(unique_plus["C"]) and bool(unique_plus["D"])
    unique_face_status = hold_report(
        unique_face, len(unique_face_combos), defined=unique_face_defined
    )
    ndot_letters = {
        name: ndot_letter_from_n(kernels[name], E2) for name in ("A", "B", "C", "D")
    }
    ndot_face_defined = bool(ndot_letters["C"]) and bool(ndot_letters["D"])
    ndot_face_combos = tuple(
        product(sorted(ndot_letters["C"]), sorted(ndot_letters["D"]))
    )
    ndot_face = sum(combo[0] == "+" and combo[1] == "-" for combo in ndot_face_combos)
    ndot_face_status = hold_report(
        ndot_face, len(ndot_face_combos), defined=ndot_face_defined
    )

    checks.check(
        "theorem2-reverse-undefined",
        reverse_status == "UNDEFINED"
        and not defined_reverse
        and letters["A"] == frozenset()
        and letters["B"] == PVM_LETTERS
        and len(reverse_combos) == 0,
        reverse_status,
    )
    checks.check(
        "theorem3-face-some",
        face_status == "some"
        and defined_face
        and face_hits == 1
        and len(face_combos) == 4,
        face_status,
    )
    checks.check(
        "not-unique-fn",
        unique_plus["A"] == frozenset()
        and all(unique_plus[name] == frozenset({"+"}) for name in ("B", "C", "D"))
        and unique_face_status == "none"
        and unique_face == 0
        and face_status == "some"
        and letters["C"] != unique_plus["C"],
    )
    checks.check(
        "not-ndot",
        ndot_letters["A"] == frozenset()
        and ndot_letters["B"] == frozenset()
        and ndot_letters["C"] == frozenset({"-"})
        and ndot_letters["D"] == frozenset({"+"})
        and ndot_face_status == "none"
        and face_status == "some"
        and letters["C"] != ndot_letters["C"],
    )
    checks.check(
        "no-unique-p-plus",
        unique_plus["C"] == frozenset({"+"})
        and letters["C"] == PVM_LETTERS
        and letters["C"] != unique_plus["C"]
        and "Unique `P_+` is not used." in normalized_note,
    )
    checks.check(
        "letters-do-not-feed-occupancy",
        occupancy(PROBES["A"], frozenset(ticks), "+")
        == occupancy(PROBES["A"], frozenset(ticks), "-")
        == occupancy(PROBES["A"], frozenset(ticks), None)
        == 1
        and occupancy((0, 4, 0), frozenset(ticks), "+") == 0,
    )
    checks.check(
        "n-independent-of-letter-branch",
        n_vector(PROBES["A"], formed_before_a) == EXPECTED_N["A"]
        and n_vector(PROBES["C"], already_recorded(PROBES["C"], ticks))
        == EXPECTED_N["C"],
    )
    checks.check(
        "mutation-identify-incoming-sign-is-refused",
        all(isinstance(lock, tuple) for lock in locks[PROBES["A"]])
        and pvm_letters_from_n(kernels["A"]) == frozenset()
        and pvm_letters_from_n(kernels["C"]) == PVM_LETTERS
        and MINUS_E1 not in PVM_LETTERS
        and E1 not in PVM_LETTERS,
    )
    same_tick_as_recorded = frozenset({ORIGIN})
    checks.check(
        "mutation-same-tick-partner-changes-n",
        n_vector(PROBES["A"], same_tick_as_recorded) != EXPECTED_N["A"]
        and n_vector(PROBES["A"], same_tick_as_recorded)
        == (Fraction(0), Fraction(-1, 3), Fraction(0))
        and pvm_letters_from_n(n_vector(PROBES["A"], same_tick_as_recorded))
        == PVM_LETTERS,
    )
    one_site_ticks, _ = form(seeds=((ORIGIN, E1),))
    one_site_n = {
        name: n_vector(PROBES[name], already_recorded(PROBES[name], one_site_ticks))
        for name in ("A", "B", "C", "D")
        if PROBES[name] in one_site_ticks
    }
    checks.check(
        "mutation-one-site-seed-changes-n",
        one_site_n != kernels
        and one_site_n["A"] != EXPECTED_N["A"]
        and one_site_ticks[PROBES["A"]] != 0,
        str(one_site_n),
    )
    nnseed_ticks, _ = form(seeds=((ORIGIN, E1), (E2, E2)))
    nnseed_n = {
        name: n_vector(PROBES[name], already_recorded(PROBES[name], nnseed_ticks))
        for name in ("A", "B", "C", "D")
    }
    checks.check(
        "mutation-perp-seed-changes-n-at-B-and-D",
        nnseed_n["A"] == EXPECTED_N["A"]
        and nnseed_n["B"] != EXPECTED_N["B"]
        and nnseed_n["D"] != EXPECTED_N["D"],
        str(nnseed_n),
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check(
        "four-probes-only-scored",
        set(PROBES) == {"A", "B", "C", "D"}
        and "E =" not in note
        and "four y-probes are the only sites" in normalized_note,
    )
    checks.check(
        "not-t-as-comparator",
        reverse_status == "UNDEFINED"
        and face_status == "some"
        and "3 t(" not in note
        and "t(" not in note,
    )
    checks.check(
        "no-sixteen-letter-census",
        "16" not in note and "sixteen" not in note.lower(),
    )

    claim_scope = (
        "Reverse and face from named rank-1 PVM letters on the four "
        "nsopp y-probes are reported. Displayed, not adopted."
    )
    checks.check("note-claim-scope", claim_scope in note)
    checks.check(
        "note-reports-n-and-letters",
        "n(A) = (0, 0, 0)" in note
        and "n(B) = (−1/3, 0, 0)" in note
        and "n(C) = (0, −1/3, 0)" in note
        and "n(D) = (−1/3, 1/3, 0)" in note
        and "L(A) = UNDEFINED" in note
        and "L(B) = {+,−}" in note
        and "L(C) = {+,−}" in note
        and "L(D) = {+,−}" in note,
    )
    checks.check(
        "note-reports-undefined-some",
        note.count("Report: `UNDEFINED`.") == 1
        and note.count("Report: `some`.") == 1
        and "all" in note
        and "some" in note
        and "none" in note
        and "UNDEFINED" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "not written into Admissibility" in normalized_note,
    )
    checks.check(
        "note-does-not-identify-incoming",
        "not identified" in normalized_note
        and "Identifying a named sign of an incoming step with a PVM letter is refused."
        in normalized_note,
    )
    checks.check(
        "note-does-not-feed-n-or-attach-formation-member",
        "does not feed `n`" in note
        and "does not attach the occupancy-kernel formation member" in normalized_note
        and "Do not attach" not in note,
    )
    checks.check(
        "note-same-tick-partner-rule",
        "same-tick partner is not already-recorded" in normalized_note
        and "Occupancy at a seed formation is already-recorded strictly earlier."
        in normalized_note,
    )
    checks.check(
        "note-not-unique-fn-or-ndot",
        "not unique `f(n)`" in note and "not ndot" in note,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in normalized_note
        and "B_3(0)" in note
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
        '    "docs/OPPOSITE_LOCK_YPROBE_PVM_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def occupancy(" in source
        and "def n_vector(" in source
        and "def pvm_letters_from_n(" in source
        and "def form(" in source
        and "def pvm_probs_k1(" in source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
