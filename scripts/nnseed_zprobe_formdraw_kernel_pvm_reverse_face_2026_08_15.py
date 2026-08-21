#!/usr/bin/env python3
"""Formdraw occupancy-kernel PVM letters on four nnseed z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and +e_2. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. At each z-probe's formation tick, n is the formdraw occupancy kernel
from already-recorded six-neighbor occupancy. If n≠0 the named rank-1 P_±
letters are {+,−}. Letters do not feed n and are not incoming {±e_i}.
Uniqueness is not required. Not unique f(n) on x-probes. Not ndot.
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
    "docs/NNSEED_ZPROBE_FORMDRAW_KERNEL_PVM_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NNSEED_ZPROBE_FORMDRAW_KERNEL_PVM_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
NN: tuple[Point, ...] = (
    E1,
    (-1, 0, 0),
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
    (E2, E2),
)
PROBES = {
    "A": (0, 0, 1),
    "B": (1, 1, 1),
    "C": (0, 0, 2),
    "D": (0, 1, 1),
}
X_PROBES = {
    "A": (1, 0, 0),
    "B": (1, 1, 1),
    "C": (2, 0, 0),
    "D": (1, 1, 0),
}
EXPECTED_N = {
    "A": (Fraction(0), Fraction(0), Fraction(-1, 3)),
    "B": (Fraction(-1, 3), Fraction(0), Fraction(-1, 3)),
    "C": (Fraction(0), Fraction(-1, 3), Fraction(-1, 3)),
    "D": (Fraction(0), Fraction(0), Fraction(-1, 3)),
}
EXPECTED_TICKS = {"A": 1, "B": 2, "C": 4, "D": 1}
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
    return madd(madd(mscale(Fraction(a), SX()), mscale(Fraction(b), SY())), mscale(Fraction(c), SZ()))


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
    """Formdraw occupancy kernel n_μ = (o_{+μ} − o_{−μ}) / 3."""
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

    print("formdraw occupancy-kernel PVM-letter reverse/face on four nnseed z-probes")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "claim_scope: Reverse and face from formdraw occupancy-kernel PVM "
        "letters on the four nnseed z-probes, or UNDEFINED, are reported. "
        "Displayed, not adopted."
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
        "z-probes-in-host",
        {PROBES["A"], PROBES["B"], PROBES["C"], PROBES["D"]} <= host,
    )
    checks.check(
        "perp-step-blocks-parallel",
        perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )

    pplus, pminus = pvm_projectors_k1(0, 0, -1)
    tp, tm = pvm_probs_k1(0, 0, -1)
    ham = hamiltonian(0, 0, -1)
    checks.check(
        "named-pvm-rank1-projectors",
        mtrace(pplus) == cz(1)
        and mtrace(pminus) == cz(1)
        and pplus == mmul(pplus, pplus)
        and pminus == mmul(pminus, pminus)
        and mmul(pplus, pminus) == zero_mat()
        and mmul(ham, ham) == I2(),
    )
    checks.check(
        "named-pvm-traces-k1",
        tp == Fraction(2, 3) and tm == Fraction(1, 3) and tp + tm == 1,
    )
    checks.check(
        "named-pvm-letters-are-plus-minus",
        PVM_LETTERS == frozenset({"+", "-"})
        and E1 not in PVM_LETTERS
        and E2 not in PVM_LETTERS,
    )

    ticks, locks = form()
    kernels: dict[str, Vec3] = {}
    letters: dict[str, frozenset[str]] = {}
    for name, site in PROBES.items():
        formed_before = already_recorded(site, ticks)
        n = n_vector(site, formed_before)
        kernels[name] = n
        letters[name] = pvm_letters_from_n(n)
        a, b, c = abc_from_n(n)
        print(
            f"{name} n=({n[0]},{n[1]},{n[2]}) k={k_value(n)} "
            f"abc=({a},{b},{c}) L={letter_report(letters[name])} "
            f"t={ticks[site]} incoming={sorted(locks.get(site, ()))}"
        )

    x_kernels = {
        name: n_vector(site, already_recorded(site, ticks))
        for name, site in X_PROBES.items()
    }

    checks.check(
        "theorem1-n-A",
        kernels["A"] == EXPECTED_N["A"] and k_value(kernels["A"]) == 1,
        str(kernels["A"]),
    )
    checks.check(
        "theorem1-n-B",
        kernels["B"] == EXPECTED_N["B"] and k_value(kernels["B"]) == 2,
        str(kernels["B"]),
    )
    checks.check(
        "theorem1-n-C",
        kernels["C"] == EXPECTED_N["C"] and k_value(kernels["C"]) == 2,
        str(kernels["C"]),
    )
    checks.check(
        "theorem1-n-D",
        kernels["D"] == EXPECTED_N["D"] and k_value(kernels["D"]) == 1,
        str(kernels["D"]),
    )
    checks.check(
        "theorem1-n-C-neq-n-D",
        kernels["C"] != kernels["D"]
        and x_kernels["C"] == x_kernels["D"]
        and x_kernels["C"] == (Fraction(-1, 3), Fraction(0), Fraction(0)),
        f"zC={kernels['C']} zD={kernels['D']} xC={x_kernels['C']}",
    )
    checks.check(
        "theorem1-letters-all-plus-minus",
        all(letters[name] == PVM_LETTERS for name in ("A", "B", "C", "D"))
        and all(letter_report(letters[name]) == "{+,−}" for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "theorem1-z-ticks-match-nsiso",
        all(ticks[PROBES[name]] == EXPECTED_TICKS[name] for name in ("A", "B", "C", "D")),
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "n-nonzero-assigns-both-letters",
        pvm_letters_from_n(ZERO_N) == frozenset()
        and pvm_letters_from_n(EXPECTED_N["A"]) == PVM_LETTERS,
    )
    checks.check(
        "hamiltonian-square-matches-k",
        all(
            hamiltonian_square_k(*abc_from_n(kernels[name])) == k_value(kernels[name])
            for name in ("A", "B", "C", "D")
        )
        and mmul(hamiltonian(*abc_from_n(kernels["B"])), hamiltonian(*abc_from_n(kernels["B"])))
        == mscale(Fraction(2), I2())
        and mmul(hamiltonian(*abc_from_n(kernels["C"])), hamiltonian(*abc_from_n(kernels["C"])))
        == mscale(Fraction(2), I2()),
    )
    checks.check(
        "incoming-locks-are-nn-steps-not-letters",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D"))
        and all(not (locks[PROBES[name]] & PVM_LETTERS) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["B"]]) == 2
        and len(locks[PROBES["C"]]) == 3
        and letters["B"] == PVM_LETTERS,
        f"B={sorted(locks[PROBES['B']])} C={sorted(locks[PROBES['C']])}",
    )
    checks.check(
        "two-site-seed-locks",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {E2},
    )

    defined_reverse = bool(letters["A"]) and bool(letters["B"])
    defined_face = bool(letters["C"]) and bool(letters["D"])
    combos = tuple(
        product(
            sorted(letters["A"]),
            sorted(letters["B"]),
            sorted(letters["C"]),
            sorted(letters["D"]),
        )
    )
    reverse_hits = sum(combo[0] == "+" and combo[1] == "-" for combo in combos)
    face_hits = sum(combo[2] == "+" and combo[3] == "-" for combo in combos)
    reverse_status = hold_report(reverse_hits, len(combos), defined=defined_reverse)
    face_status = hold_report(face_hits, len(combos), defined=defined_face)
    print(f"combos={len(combos)} reverse_hits={reverse_hits} face_hits={face_hits}")
    print(f"reverse={reverse_status} face={face_status}")

    unique_plus = {name: unique_plus_from_n(kernels[name]) for name in ("A", "B", "C", "D")}
    unique_combos = tuple(
        product(
            sorted(unique_plus["A"]),
            sorted(unique_plus["B"]),
            sorted(unique_plus["C"]),
            sorted(unique_plus["D"]),
        )
    )
    unique_reverse = sum(combo[0] == "+" and combo[1] == "-" for combo in unique_combos)
    ndot_letters = {name: ndot_letter_from_n(kernels[name], E3) for name in ("A", "B", "C", "D")}
    ndot_combos = tuple(
        product(
            sorted(ndot_letters["A"]),
            sorted(ndot_letters["B"]),
            sorted(ndot_letters["C"]),
            sorted(ndot_letters["D"]),
        )
    )
    ndot_reverse = sum(combo[0] == "+" and combo[1] == "-" for combo in ndot_combos)
    ndot_defined = all(ndot_letters[name] for name in ("A", "B", "C", "D"))

    checks.check(
        "theorem2-reverse-some",
        reverse_status == "some"
        and defined_reverse
        and reverse_hits == 4
        and len(combos) == 16,
        reverse_status,
    )
    checks.check(
        "theorem3-face-some",
        face_status == "some" and defined_face and face_hits == 4,
        face_status,
    )
    checks.check(
        "not-unique-fn-on-x-probes",
        all(unique_plus[name] == frozenset({"+"}) for name in ("A", "B", "C", "D"))
        and unique_reverse == 0
        and reverse_status == "some"
        and letters["A"] != unique_plus["A"],
    )
    checks.check(
        "not-ndot",
        ndot_defined
        and all(ndot_letters[name] == frozenset({"-"}) for name in ("A", "B", "C", "D"))
        and ndot_reverse == 0
        and reverse_status == "some"
        and letters["A"] != ndot_letters["A"],
    )
    checks.check(
        "letters-do-not-feed-occupancy",
        occupancy(PROBES["A"], frozenset(ticks), "+")
        == occupancy(PROBES["A"], frozenset(ticks), "-")
        == occupancy(PROBES["A"], frozenset(ticks), None)
        == 1
        and occupancy((4, 0, 0), frozenset(ticks), "+") == 0,
    )
    formed_before_a = already_recorded(PROBES["A"], ticks)
    checks.check(
        "n-independent-of-letter-branch",
        n_vector(PROBES["A"], formed_before_a) == EXPECTED_N["A"],
    )
    checks.check(
        "mutation-identify-incoming-sign-is-refused",
        all(isinstance(lock, tuple) for lock in locks[PROBES["A"]])
        and pvm_letters_from_n(kernels["A"]) == PVM_LETTERS
        and E1 not in PVM_LETTERS
        and E3 not in PVM_LETTERS,
    )
    signed_minus_as_vacant = frozenset(site for site in formed_before_a if site != ORIGIN)
    checks.check(
        "mutation-minus-as-vacant-changes-n",
        n_vector(PROBES["A"], signed_minus_as_vacant) != EXPECTED_N["A"],
    )
    one_site_ticks, _ = form(seeds=((ORIGIN, E1),))
    one_site_n = {
        name: n_vector(PROBES[name], already_recorded(PROBES[name], one_site_ticks))
        for name in ("A", "B", "C", "D")
        if PROBES[name] in one_site_ticks
    }
    checks.check(
        "mutation-one-site-seed-changes-n",
        one_site_n != kernels,
        str(one_site_n),
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check(
        "not-t-as-comparator",
        reverse_status == "some"
        and face_status == "some"
        and reverse_hits != 0
        and "3 t(" not in note,
    )
    checks.check(
        "no-sixteen-letter-census-beyond-pm",
        len(combos) == 16
        and all(letters[name] == PVM_LETTERS for name in ("A", "B", "C", "D"))
        and "16-letter occupancy census independent of `n` is not taken"
        in normalized_note,
    )

    claim_scope = (
        "Reverse and face from formdraw occupancy-kernel PVM letters "
        "on the four nnseed z-probes, or UNDEFINED, are reported. Displayed, "
        "not adopted."
    )
    checks.check("note-claim-scope", claim_scope in note)
    checks.check(
        "note-reports-n-and-letters",
        "n(A_z) = (0, 0, −1/3)" in note
        and "n(B)   = (−1/3, 0, −1/3)" in note
        and "n(C_z) = (0, −1/3, −1/3)" in note
        and "n(D_z) = (0, 0, −1/3)" in note
        and "L(A_z) = {+,−}" in note
        and "L(B) = {+,−}" in note
        and "L(C_z) = {+,−}" in note
        and "L(D_z) = {+,−}" in note,
    )
    checks.check(
        "note-reports-some-some",
        note.count("Report: `some`.") == 2
        and "all" in note
        and "some" in note
        and "none" in note
        and "UNDEFINED" in note,
    )
    checks.check(
        "note-nC-neq-nD-not-x-fact",
        "n(C_z) ≠ n(D_z)" in note
        and "`n(C)=n(D)` is an x-probe fact" in note,
    )
    checks.check(
        "note-not-unique-fn-or-ndot",
        "not unique `f(n)` on the x-probes" in note and "not ndot" in note,
    )
    checks.check(
        "note-z-ticks-nsiso",
        "t(A_z)=t(0,0,1)=1" in note
        and "t(B)=t(1,1,1)=2" in note
        and "t(C_z)=t(0,0,2)=4" in note
        and "t(D_z)=t(0,1,1)=1" in note,
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
        '    "docs/NNSEED_ZPROBE_FORMDRAW_KERNEL_PVM_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
