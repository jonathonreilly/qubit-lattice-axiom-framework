#!/usr/bin/env python3
"""Named rank-1 PVM letters on four opposite-lock z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and -e_1. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. At each z-probe's formation, n is the formdraw occupancy kernel from
already-recorded six-neighbor occupancy. If n≠0 the named rank-1 P_± letters
are {+,−}. Reverse holds iff + is process-determined at A and − at B. Face
holds iff + is process-determined at C and − at D. Empty letter set on either
side is UNDEFINED. Letters do not feed n and are not incoming {±e_i}.
Uniqueness is not required. Four-probe lettering combinations are not
enumerated.
"""

from __future__ import annotations

import ast
from collections import deque
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_ZPROBE_PVM_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_ZPROBE_PVM_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
NEG_E1: Point = (-1, 0, 0)
NEG_E2: Point = (0, -1, 0)
NEG_E3: Point = (0, 0, -1)
NN: tuple[Point, ...] = (E1, NEG_E1, E2, NEG_E2, E3, NEG_E3)
AXES: tuple[Point, Point, Point] = (E1, E2, E3)
PVM_LETTERS = frozenset({"+", "-"})
ZERO_N: Vec3 = (Fraction(0), Fraction(0), Fraction(0))
BALL_SQ = 9
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
PERP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
PROBES = {
    "A": (0, 0, 1),
    "B": (1, 1, 1),
    "C": (0, 0, 2),
    "D": (1, 0, 1),
}
Y_PROBES = {
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
EXPECTED_N = {
    "A": (Fraction(0), Fraction(0), Fraction(-1, 3)),
    "B": (Fraction(-1, 3), Fraction(0), Fraction(0)),
    "C": (Fraction(0), Fraction(-1, 3), Fraction(-1, 3)),
    "D": (Fraction(-1, 3), Fraction(0), Fraction(0)),
}
EXPECTED_K = {"A": 1, "B": 1, "C": 2, "D": 1}
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
    "16 combinations",
    "L1",
    "Runner cache",
)
CLAIM_SCOPE = (
    "Reverse and face from named rank-1 PVM letters on the four "
    "nsopp z-probes are reported. Displayed, not adopted."
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


def letter_report(letters: frozenset[str]) -> str:
    if not letters:
        return "UNDEFINED"
    if letters == PVM_LETTERS:
        return "{+,−}"
    only = next(iter(letters))
    return only


def reverse_report(letters_a: frozenset[str], letters_b: frozenset[str]) -> str:
    """Reverse iff + is process-determined at A and − at B."""
    if not letters_a or not letters_b:
        return "UNDEFINED"
    if "+" in letters_a and "-" in letters_b:
        return "hold"
    return "fail"


def face_report(letters_c: frozenset[str], letters_d: frozenset[str]) -> str:
    """Face iff + is process-determined at C and − at D."""
    if not letters_c or not letters_d:
        return "UNDEFINED"
    if "+" in letters_c and "-" in letters_d:
        return "hold"
    return "fail"


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

    print("named rank-1 PVM-letter reverse/face on four opposite-lock z-probes")
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
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-probes-in-host",
        probe_sites == ((0, 0, 1), (1, 1, 1), (0, 0, 2), (1, 0, 1))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and PROBES["A"] != E2
        and PROBES["A"] != E1,
    )
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E3) == E3
        and add(NEG_E3, E3) == ORIGIN
        and dot(E1, E3) == 0
        and perpendicular(E1, E3)
        and perpendicular(NEG_E1, E3)
        and not perpendicular(E1, E1)
        and not perpendicular(E3, E3)
        and in_ball(PROBES["C"])
        and not in_ball((0, 0, 4)),
    )

    pplus_a, pminus_a = pvm_projectors_k1(0, 0, -1)
    pplus_b, pminus_b = pvm_projectors_k1(-1, 0, 0)
    tp_a, tm_a = pvm_probs_k1(0, 0, -1)
    tp_b, tm_b = pvm_probs_k1(-1, 0, 0)
    ham_a = hamiltonian(0, 0, -1)
    checks.check(
        "named-pvm-rank1-projectors",
        mtrace(pplus_a) == cz(1)
        and mtrace(pminus_a) == cz(1)
        and pplus_a == mmul(pplus_a, pplus_a)
        and pminus_a == mmul(pminus_a, pminus_a)
        and mmul(pplus_a, pminus_a) == zero_mat()
        and pplus_b == mmul(pplus_b, pplus_b)
        and pminus_b == mmul(pminus_b, pminus_b)
        and mmul(pplus_b, pminus_b) == zero_mat()
        and mmul(ham_a, ham_a) == I2(),
    )
    checks.check(
        "named-pvm-traces-k1",
        tp_a == Fraction(2, 3)
        and tm_a == Fraction(1, 3)
        and tp_b == Fraction(2, 3)
        and tm_b == Fraction(1, 3)
        and tp_a + tm_a == 1
        and tp_b + tm_b == 1,
    )
    checks.check(
        "named-pvm-letters-are-plus-minus",
        PVM_LETTERS == frozenset({"+", "-"})
        and E1 not in PVM_LETTERS
        and E2 not in PVM_LETTERS
        and E3 not in PVM_LETTERS,
    )
    checks.check(
        "reverse-face-identity",
        reverse_report(frozenset(), PVM_LETTERS) == "UNDEFINED"
        and reverse_report(PVM_LETTERS, frozenset()) == "UNDEFINED"
        and reverse_report(PVM_LETTERS, PVM_LETTERS) == "hold"
        and reverse_report(frozenset({"+"}), frozenset({"+"})) == "fail"
        and reverse_report(frozenset({"+"}), frozenset({"-"})) == "hold"
        and face_report(PVM_LETTERS, PVM_LETTERS) == "hold"
        and face_report(frozenset({"-"}), frozenset({"-"})) == "fail"
        and face_report(frozenset(), frozenset({"-"})) == "UNDEFINED"
        and face_report(frozenset({"+"}), frozenset()) == "UNDEFINED",
    )

    ticks, locks = form()
    kernels: dict[str, Vec3] = {}
    letters: dict[str, frozenset[str]] = {}
    occupancies: dict[str, dict[Point, int]] = {}
    for name, site in PROBES.items():
        formed_before = already_recorded(site, ticks)
        n = n_vector(site, formed_before)
        kernels[name] = n
        letters[name] = pvm_letters_from_n(n)
        occ = {step: occupancy(add(site, step), formed_before) for step in NN}
        occupancies[name] = occ
        a, b, c = abc_from_n(n)
        print(
            f"{name} n=({n[0]},{n[1]},{n[2]}) k={k_value(n)} "
            f"abc=({a},{b},{c}) L={letter_report(letters[name])} "
            f"incoming={sorted(locks.get(site, ()))}"
        )

    reverse_status = reverse_report(letters["A"], letters["B"])
    face_status = face_report(letters["C"], letters["D"])
    print(f"reverse={reverse_status} face={face_status}")
    print(
        "per_element: named rank-1 P_± from occupancy-kernel n, else UNDEFINED"
    )
    print(
        "per_site: scored only at z-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four {+,−} letter sets plus reverse/face as hold, fail, or UNDEFINED"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    checks.check(
        "theorem1-n-A",
        kernels["A"] == EXPECTED_N["A"]
        and k_value(kernels["A"]) == EXPECTED_K["A"]
        and occupancies["A"][NEG_E3] == 1
        and occupancies["A"][E3] == 0
        and occupancies["A"][E1] == 0
        and occupancies["A"][NEG_E1] == 0
        and occupancies["A"][E2] == 0
        and occupancies["A"][NEG_E2] == 0,
        str(kernels["A"]),
    )
    checks.check(
        "theorem1-n-B",
        kernels["B"] == EXPECTED_N["B"]
        and k_value(kernels["B"]) == EXPECTED_K["B"]
        and occupancies["B"][NEG_E1] == 1
        and occupancies["B"][E1] == 0
        and occupancies["B"][E2] == 0
        and occupancies["B"][NEG_E2] == 0
        and occupancies["B"][E3] == 0
        and occupancies["B"][NEG_E3] == 0,
        str(kernels["B"]),
    )
    checks.check(
        "theorem1-n-C",
        kernels["C"] == EXPECTED_N["C"]
        and k_value(kernels["C"]) == EXPECTED_K["C"]
        and occupancies["C"][E1] == 1
        and occupancies["C"][NEG_E1] == 1
        and occupancies["C"][NEG_E2] == 1
        and occupancies["C"][NEG_E3] == 1
        and occupancies["C"][E2] == 0
        and occupancies["C"][E3] == 0,
        str(kernels["C"]),
    )
    checks.check(
        "theorem1-n-D",
        kernels["D"] == EXPECTED_N["D"]
        and k_value(kernels["D"]) == EXPECTED_K["D"]
        and occupancies["D"][NEG_E1] == 1
        and occupancies["D"][E1] == 0
        and occupancies["D"][E2] == 0
        and occupancies["D"][NEG_E2] == 0
        and occupancies["D"][E3] == 0
        and occupancies["D"][NEG_E3] == 0,
        str(kernels["D"]),
    )
    checks.check(
        "theorem1-letters-all-plus-minus",
        all(letters[name] == PVM_LETTERS for name in ("A", "B", "C", "D"))
        and all(letter_report(letters[name]) == "{+,−}" for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "n-nonzero-assigns-both-letters",
        pvm_letters_from_n(ZERO_N) == frozenset()
        and pvm_letters_from_n(EXPECTED_N["A"]) == PVM_LETTERS
        and pvm_letters_from_n(EXPECTED_N["C"]) == PVM_LETTERS,
    )
    ham_c = hamiltonian(*abc_from_n(kernels["C"]))
    checks.check(
        "hamiltonian-square-matches-k",
        all(
            hamiltonian_square_k(*abc_from_n(kernels[name])) == k_value(kernels[name])
            for name in ("A", "B", "C", "D")
        )
        and mmul(hamiltonian(*abc_from_n(kernels["A"])), hamiltonian(*abc_from_n(kernels["A"])))
        == I2()
        and mmul(hamiltonian(*abc_from_n(kernels["B"])), hamiltonian(*abc_from_n(kernels["B"])))
        == I2()
        and mmul(ham_c, ham_c) == mscale(Fraction(2), I2()),
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse_status == "hold"
        and letters["A"] == PVM_LETTERS
        and letters["B"] == PVM_LETTERS
        and reverse_status != "fail"
        and reverse_status != "UNDEFINED",
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and letters["C"] == PVM_LETTERS
        and letters["D"] == PVM_LETTERS
        and face_status != "fail"
        and face_status != "UNDEFINED",
        face_status,
    )
    checks.check(
        "incoming-locks-are-nn-steps-not-letters",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D"))
        and all(not (locks[PROBES[name]] & PVM_LETTERS) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["C"]]) == 3
        and letters["C"] == PVM_LETTERS
        and letters["A"] == PVM_LETTERS,
        str(sorted(locks[PROBES["C"]])),
    )
    checks.check(
        "two-site-opposite-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and add(E1, NEG_E1) == ORIGIN
        and TWO_SITE_SEEDS != PERP_SEEDS
        and sum(time == 0 for time in ticks.values()) == 2,
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
        and ticks[E3] == 1
        and ticks[NEG_E3] == 1
        and ticks[(0, -1, 0)] == 1
        and ticks[(0, 2, 0)] == 1
        and locks[E3] == {E3}
        and PROBES["C"] in ticks
        and ticks[PROBES["C"]] != 2
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "letters-do-not-feed-occupancy",
        occupancy(PROBES["A"], frozenset(ticks), "+")
        == occupancy(PROBES["A"], frozenset(ticks), "-")
        == occupancy(PROBES["A"], frozenset(ticks), None)
        == 1
        and occupancy((0, 0, 4), frozenset(ticks), "+") == 0,
    )
    formed_before_a = already_recorded(PROBES["A"], ticks)
    checks.check(
        "n-independent-of-letter-branch",
        n_vector(PROBES["A"], formed_before_a)
        == n_vector(PROBES["A"], formed_before_a)
        == EXPECTED_N["A"],
    )
    checks.check(
        "mutation-identify-incoming-sign-is-refused",
        all(isinstance(lock, tuple) for lock in locks[PROBES["A"]])
        and pvm_letters_from_n(kernels["A"]) == PVM_LETTERS
        and E3 not in PVM_LETTERS
        and locks[PROBES["A"]] == {E3}
        and letters["A"] == PVM_LETTERS,
    )
    signed_minus_as_vacant = frozenset(
        site for site in already_recorded(PROBES["A"], ticks) if site != ORIGIN
    )
    checks.check(
        "mutation-minus-as-vacant-changes-n",
        n_vector(PROBES["A"], signed_minus_as_vacant) != EXPECTED_N["A"]
        and n_vector(PROBES["A"], signed_minus_as_vacant) == ZERO_N
        and pvm_letters_from_n(n_vector(PROBES["A"], signed_minus_as_vacant))
        == frozenset(),
    )
    checks.check(
        "mutation-empty-letters-undefined",
        reverse_report(frozenset(), letters["B"]) == "UNDEFINED"
        and face_report(letters["C"], frozenset()) == "UNDEFINED"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    y_a = Y_PROBES["A"]
    y_n_a = n_vector(y_a, already_recorded(y_a, ticks))
    y_letters_a = pvm_letters_from_n(y_n_a)
    y_letters_b = pvm_letters_from_n(
        n_vector(Y_PROBES["B"], already_recorded(Y_PROBES["B"], ticks))
    )
    checks.check(
        "not-leftover-of-yprobe-register",
        y_a == E2
        and y_n_a == ZERO_N
        and y_letters_a == frozenset()
        and reverse_report(y_letters_a, y_letters_b) == "UNDEFINED"
        and reverse_status == "hold"
        and PROBES["A"] != y_a,
    )
    x_a = X_PROBES["A"]
    x_n_a = n_vector(x_a, already_recorded(x_a, ticks))
    checks.check(
        "not-leftover-of-xprobe-register",
        x_a == E1
        and x_n_a != EXPECTED_N["A"]
        and PROBES["A"] != x_a
        and PROBES["C"] != X_PROBES["C"]
        and PROBES["D"] != X_PROBES["D"],
        str(x_n_a),
    )
    checks.check(
        "not-leftover-of-qlet-undefined",
        all(letters[name] != frozenset() for name in ("A", "B", "C", "D"))
        and reverse_status != "UNDEFINED"
        and face_status != "UNDEFINED",
    )
    checks.check(
        "formation-stays-in-host",
        set(ticks) <= host,
    )
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check(
        "four-probes-only-scored",
        set(PROBES) == {"A", "B", "C", "D"}
        and "E =" not in note
        and "four z-probes are the only sites" in normalized_note,
    )
    checks.check(
        "not-t-as-comparator",
        reverse_status == "hold"
        and face_status == "hold"
        and "3 t(" not in note
        and "Formation ticks are not scored." in note,
    )
    imported_names = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
        for alias in node.names
    }
    called_names = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    checks.check(
        "no-sixteen-letter-census",
        "16 combinations" not in note
        and "16-letter" not in note
        and "16-census" not in note
        and "product" not in imported_names
        and "product" not in called_names,
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-n-and-letters",
        "n(A) = (0, 0, −1/3)" in note
        and "n(B) = (−1/3, 0, 0)" in note
        and "n(C) = (0, −1/3, −1/3)" in note
        and "n(D) = (−1/3, 0, 0)" in note
        and "L(A) = {+,−}" in note
        and "L(B) = {+,−}" in note
        and "L(C) = {+,−}" in note
        and "L(D) = {+,−}" in note
        and "k(A) = 1" in note
        and "k(B) = 1" in note
        and "k(C) = 2" in note
        and "k(D) = 1" in note,
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
        '    "docs/OPPOSITE_LOCK_ZPROBE_PVM_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def occupancy(" in source
        and "def n_vector(" in source
        and "def pvm_letters_from_n(" in source
        and "def reverse_report(" in source
        and "def face_report(" in source
        and "def form(" in source
        and "def pvm_probs_k1(" in source,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "source-letter-from-occupancy-kernel-only",
        "pvm_letters_from_n" in defined_fns
        and "n_vector" in defined_fns
        and "reverse_report" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
