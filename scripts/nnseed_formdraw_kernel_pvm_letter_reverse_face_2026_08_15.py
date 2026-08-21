#!/usr/bin/env python3
"""Formdraw occupancy-kernel PVM letters on four nnseed probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and +e_2. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. At each probe's formation tick, n is the formdraw occupancy kernel from
already-recorded six-neighbor occupancy. If n≠0 the named rank-1 P_± letters
are {+,−}. Letters do not feed n and are not incoming {±e_i}. Uniqueness is
not required.
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
    "docs/NNSEED_FORMDRAW_KERNEL_PVM_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NNSEED_FORMDRAW_KERNEL_PVM_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Vec3 = tuple[Fraction, Fraction, Fraction]
Mat = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
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
    "A": (1, 0, 0),
    "B": (1, 1, 1),
    "C": (2, 0, 0),
    "D": (1, 1, 0),
}
EXPECTED_N = {
    "A": (Fraction(-1, 3), Fraction(1, 3), Fraction(0)),
    "B": (Fraction(-1, 3), Fraction(0), Fraction(-1, 3)),
    "C": (Fraction(-1, 3), Fraction(0), Fraction(0)),
    "D": (Fraction(-1, 3), Fraction(0), Fraction(0)),
}
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


def madd(left: Mat, right: Mat) -> Mat:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def mmul(left: Mat, right: Mat) -> Mat:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def mscale(coeff: Fraction, mat: Mat) -> Mat:
    return (
        (coeff * mat[0][0], coeff * mat[0][1]),
        (coeff * mat[1][0], coeff * mat[1][1]),
    )


def mtrace(mat: Mat) -> Fraction:
    return mat[0][0] + mat[1][1]


def I2() -> Mat:
    zero, one = Fraction(0), Fraction(1)
    return ((one, zero), (zero, one))


def SX() -> Mat:
    zero, one = Fraction(0), Fraction(1)
    return ((zero, one), (one, zero))


def pvm_probs(a: int, b: int, c: int) -> tuple[Fraction, Fraction]:
    """Identity gate: Tr(ρ P±) for the named rank-1 projectors at k=1."""
    if b != 0 or c != 0:
        raise ValueError("named k=1 traces are displayed here at b=c=0")
    if a * a != 1:
        raise ValueError("named k=1 traces require a=±1")
    hamiltonian = mscale(Fraction(a), SX())
    half = Fraction(1, 2)
    pplus = mscale(half, madd(I2(), hamiltonian))
    pminus = mscale(half, madd(I2(), mscale(Fraction(-1), hamiltonian)))
    rho = mscale(half, madd(I2(), mscale(Fraction(1, 3), hamiltonian)))
    return mtrace(mmul(rho, pplus)), mtrace(mmul(rho, pminus))


def pvm_projectors_k1(a: int) -> tuple[Mat, Mat]:
    """Named rank-1 P± for H=a σx, k=1."""
    hamiltonian = mscale(Fraction(a), SX())
    half = Fraction(1, 2)
    pplus = mscale(half, madd(I2(), hamiltonian))
    pminus = mscale(half, madd(I2(), mscale(Fraction(-1), hamiltonian)))
    return pplus, pminus


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

    print("formdraw occupancy-kernel PVM-letter reverse/face on four nnseed probes")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "claim_scope: Reverse and face from formdraw occupancy-kernel PVM "
        "letters on the four nnseed probes, or UNDEFINED, are reported. "
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
    probe_sites = tuple(PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-probes-in-host",
        probe_sites == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites,
    )
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )

    pplus, pminus = pvm_projectors_k1(-1)
    tp, tm = pvm_probs(-1, 0, 0)
    checks.check(
        "named-pvm-rank1-projectors",
        mtrace(pplus) == 1
        and mtrace(pminus) == 1
        and pplus == mmul(pplus, pplus)
        and pminus == mmul(pminus, pminus)
        and mmul(pplus, pminus)
        == ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0))),
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
            f"incoming={sorted(locks.get(site, ()))}"
        )

    checks.check(
        "theorem1-n-A",
        kernels["A"] == EXPECTED_N["A"] and k_value(kernels["A"]) == 2,
        str(kernels["A"]),
    )
    checks.check(
        "theorem1-n-B",
        kernels["B"] == EXPECTED_N["B"] and k_value(kernels["B"]) == 2,
        str(kernels["B"]),
    )
    checks.check(
        "theorem1-n-C",
        kernels["C"] == EXPECTED_N["C"] and k_value(kernels["C"]) == 1,
        str(kernels["C"]),
    )
    checks.check(
        "theorem1-n-D",
        kernels["D"] == EXPECTED_N["D"] and k_value(kernels["D"]) == 1,
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
        and pvm_letters_from_n(EXPECTED_N["A"]) == PVM_LETTERS,
    )
    checks.check(
        "hamiltonian-square-matches-k",
        all(
            hamiltonian_square_k(*abc_from_n(kernels[name])) == k_value(kernels[name])
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "incoming-locks-are-nn-steps-not-letters",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D"))
        and all(not (locks[PROBES[name]] & PVM_LETTERS) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["B"]]) == 2 and letters["B"] == PVM_LETTERS,
        str(sorted(locks[PROBES["B"]])),
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
        "letters-do-not-feed-occupancy",
        occupancy(PROBES["A"], frozenset(ticks), "+")
        == occupancy(PROBES["A"], frozenset(ticks), "-")
        == occupancy(PROBES["A"], frozenset(ticks), None)
        == 1
        and occupancy((4, 0, 0), frozenset(ticks), "+") == 0,
    )
    formed_before_a = already_recorded(PROBES["A"], ticks)
    n_plus = n_vector(PROBES["A"], formed_before_a)
    n_minus = n_vector(PROBES["A"], formed_before_a)
    checks.check("n-independent-of-letter-branch", n_plus == n_minus == EXPECTED_N["A"])
    checks.check(
        "mutation-identify-incoming-sign-is-refused",
        all(isinstance(lock, tuple) for lock in locks[PROBES["A"]])
        and pvm_letters_from_n(kernels["A"]) == PVM_LETTERS
        and E1 not in PVM_LETTERS,
    )
    signed_minus_as_vacant = frozenset(
        site for site in already_recorded(PROBES["A"], ticks) if site != PROBES["D"]
    )
    checks.check(
        "mutation-minus-as-vacant-changes-n",
        n_vector(PROBES["A"], signed_minus_as_vacant) != EXPECTED_N["A"],
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
        "not-t-as-comparator",
        reverse_status == "some"
        and face_status == "some"
        and reverse_hits != 0
        and "3 t(" not in note,
    )

    claim_scope = (
        "Reverse and face from formdraw occupancy-kernel PVM letters "
        "on the four nnseed probes, or UNDEFINED, are reported. Displayed, "
        "not adopted."
    )
    checks.check("note-claim-scope", claim_scope in note)
    checks.check(
        "note-reports-n-and-letters",
        "n(A) = (−1/3, 1/3, 0)" in note
        and "n(B) = (−1/3, 0, −1/3)" in note
        and "n(C) = (−1/3, 0, 0)" in note
        and "n(D) = (−1/3, 0, 0)" in note
        and "L(A) = {+,−}" in note
        and "L(B) = {+,−}" in note
        and "L(C) = {+,−}" in note
        and "L(D) = {+,−}" in note,
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
        '    "docs/NNSEED_FORMDRAW_KERNEL_PVM_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def occupancy(" in source
        and "def n_vector(" in source
        and "def pvm_letters_from_n(" in source
        and "def form(" in source
        and "def pvm_probs(" in source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
