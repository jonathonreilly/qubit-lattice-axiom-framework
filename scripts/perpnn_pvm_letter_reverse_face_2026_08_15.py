#!/usr/bin/env python3
"""Named rank-1 PVM-letter reverse/face on four perpnn probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed lock at
the origin is +e_1. A 6-NN step is allowed iff it is perpendicular to the
parent lock axis. Newly formed sites lock the incoming step. Named rank-1
PVM letters are {+,−} names of P±, not incoming {±e_i} tags. If the process
assigns no such letter, reverse and face are UNDEFINED.
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
    "docs/PERPNN_PVM_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/PERPNN_PVM_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
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
PVM_LETTERS = frozenset({"+", "-"})
BALL_SQ = 9
PROBES = {
    "A": (1, 0, 0),
    "B": (1, 1, 1),
    "C": (2, 0, 0),
    "D": (1, 1, 0),
}
FORBIDDEN_NOTE_TOKENS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "Gram",
    "16-letter",
    "16 letterings",
    "hop-cost",
    "B_57",
    "Runner cache",
    "t(1,0,0)",
    "t(1,1,1)",
    "t(2,0,0)",
    "t(1,1,0)",
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
        raise ValueError("named construction is displayed here at k=1, b=c=0")
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
    """Occupancy is 1 on the formed set. A PVM letter does not feed n."""
    if letter is not None and letter not in PVM_LETTERS:
        raise ValueError(f"letter must be + or -, got {letter!r}")
    return 1 if site in formed else 0


def pvm_letters_from_process(incoming: set[object]) -> frozenset[str]:
    """Process-determined named PVM letters.

    Incoming perpnn locks are unit steps in NN. Named PVM letters are +/−.
    This function does not identify a named sign of {±e_i} with a PVM letter.
    """
    letters: set[str] = set()
    for lock in incoming:
        if lock in PVM_LETTERS:
            letters.add(str(lock))
    return frozenset(letters)


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
        return "hold-on-all"
    return "some"


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


def form_earliest(
    seed_lock: Point = E1,
    *,
    require_perp: bool = True,
) -> dict[Point, set[Point]]:
    """Earliest incoming locks, uniqueness not required."""
    order: dict[Point, int] = {ORIGIN: 0}
    locks: dict[Point, set[Point]] = {ORIGIN: {seed_lock}}
    queue: deque[tuple[Point, int]] = deque([(ORIGIN, 0)])
    while queue:
        parent, parent_order = queue.popleft()
        for lock in tuple(locks[parent]):
            for step in NN:
                if require_perp and not perpendicular(lock, step):
                    continue
                child = add(parent, step)
                if not in_ball(child):
                    continue
                next_order = parent_order + 1
                if child not in order:
                    order[child] = next_order
                    locks[child] = {step}
                    queue.append((child, next_order))
                elif order[child] == next_order:
                    locks[child].add(step)
    return locks


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

    print("named rank-1 PVM-letter reverse/face on four perpnn probes")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "claim_scope: Reverse and face from named rank-1 PVM letters on the "
        "four perpnn probes, or UNDEFINED if the process determines no such "
        "letter, are reported. Displayed, not adopted."
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
        and mmul(pplus, pminus) == ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0))),
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

    locks = form_earliest()
    lock_a = set(locks.get(PROBES["A"], ()))
    lock_b = set(locks.get(PROBES["B"], ()))
    lock_c = set(locks.get(PROBES["C"], ()))
    lock_d = set(locks.get(PROBES["D"], ()))
    letters_a = pvm_letters_from_process(lock_a)
    letters_b = pvm_letters_from_process(lock_b)
    letters_c = pvm_letters_from_process(lock_c)
    letters_d = pvm_letters_from_process(lock_d)

    print(f"incoming(A)={sorted(lock_a)}")
    print(f"incoming(B)={sorted(lock_b)}")
    print(f"incoming(C)={sorted(lock_c)}")
    print(f"incoming(D)={sorted(lock_d)}")
    print(
        "L(A,B,C,D)="
        f"{letter_report(letters_a)},{letter_report(letters_b)},"
        f"{letter_report(letters_c)},{letter_report(letters_d)}"
    )

    checks.check(
        "incoming-locks-are-nn-steps",
        lock_a <= set(NN)
        and lock_b <= set(NN)
        and lock_c <= set(NN)
        and lock_d <= set(NN)
        and len(lock_a) > 0
        and len(lock_b) > 0
        and len(lock_c) > 0
        and len(lock_d) > 0,
    )
    checks.check(
        "incoming-locks-are-not-pvm-letters",
        not (lock_a & PVM_LETTERS)
        and not (lock_b & PVM_LETTERS)
        and not (lock_c & PVM_LETTERS)
        and not (lock_d & PVM_LETTERS),
    )
    checks.check(
        "theorem1-A-undefined",
        letter_report(letters_a) == "UNDEFINED" and not letters_a,
    )
    checks.check(
        "theorem1-B-undefined",
        letter_report(letters_b) == "UNDEFINED" and not letters_b,
    )
    checks.check(
        "theorem1-C-undefined",
        letter_report(letters_c) == "UNDEFINED" and not letters_c,
    )
    checks.check(
        "theorem1-D-undefined",
        letter_report(letters_d) == "UNDEFINED" and not letters_d,
    )
    checks.check(
        "uniqueness-not-required",
        len(lock_a) > 1,
        f"incoming-A={len(lock_a)}",
    )

    defined_reverse = bool(letters_a) and bool(letters_b)
    defined_face = bool(letters_c) and bool(letters_d)
    combos = tuple(
        product(
            sorted(letters_a) or [None],
            sorted(letters_b) or [None],
            sorted(letters_c) or [None],
            sorted(letters_d) or [None],
        )
    )
    reverse_hits = 0
    face_hits = 0
    if defined_reverse or defined_face:
        for combo in combos:
            reverse_hits += int(combo[0] == "+" and combo[1] == "-")
            face_hits += int(combo[2] == "+" and combo[3] == "-")
    reverse_status = hold_report(
        reverse_hits, len(combos), defined=defined_reverse
    )
    face_status = hold_report(face_hits, len(combos), defined=defined_face)

    print(f"reverse={reverse_status} face={face_status}")

    checks.check(
        "theorem2-reverse-undefined",
        reverse_status == "UNDEFINED" and not defined_reverse,
        reverse_status,
    )
    checks.check(
        "theorem3-face-undefined",
        face_status == "UNDEFINED" and not defined_face,
        face_status,
    )
    checks.check(
        "not-free-occupancy-lettering-census",
        not defined_reverse
        and not defined_face
        and 2**4 != 0
        and "16 letterings" not in note
        and "16-letter" not in note,
    )
    checks.check(
        "letters-do-not-feed-occupancy",
        occupancy(PROBES["A"], frozenset(locks), "+")
        == occupancy(PROBES["A"], frozenset(locks), "-")
        == occupancy(PROBES["A"], frozenset(locks), None)
        == 1
        and occupancy((3, 3, 3), frozenset(locks), "+") == 0,
    )
    checks.check(
        "mutation-identify-incoming-sign-is-refused",
        pvm_letters_from_process(lock_a) == frozenset()
        and all(isinstance(lock, tuple) for lock in lock_a),
    )
    checks.check(
        "seed-origin-lock-plus-e1",
        locks[ORIGIN] == {E1},
    )
    checks.check(
        "formation-stays-in-host",
        set(locks) <= host,
    )
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in locks),
    )

    claim_scope = (
        "Reverse and face from named rank-1 PVM letters on the four "
        "perpnn probes, or UNDEFINED if the process determines no such "
        "letter, are reported. Displayed, not adopted."
    )
    checks.check("note-claim-scope", claim_scope in note)
    checks.check(
        "note-reports-undefined-letters",
        "L(A) = UNDEFINED" in note
        and "L(B) = UNDEFINED" in note
        and "L(C) = UNDEFINED" in note
        and "L(D) = UNDEFINED" in note,
    )
    checks.check(
        "note-reports-undefined-undefined",
        note.count("Report: `UNDEFINED`.") == 2
        and "hold-on-all" in note
        and "some" in note
        and "none" in note,
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
        "note-does-not-feed-n-or-attach-occupancy-member",
        "does not feed `n`" in note
        and "does not attach the occupancy-kernel member" in normalized_note
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
        '    "docs/PERPNN_PVM_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def pvm_probs(" in source
        and "def pvm_letters_from_process(" in source
        and "def occupancy(" in source
        and "def form_earliest(" in source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
