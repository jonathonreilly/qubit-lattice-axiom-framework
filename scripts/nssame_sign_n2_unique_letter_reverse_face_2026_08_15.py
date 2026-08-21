#!/usr/bin/env python3
"""Unique letter sign(n_2) on four nssame probes.

Host Euclidean B_3(0) = {n in Z^3 : n·n <= 9}. Seed at tick 0 records the
origin and (0,1,0), both locking +e_1. Growth is the nssame perp-step
incoming-lock process. At each probe's formation tick, n is the formdraw
occupancy kernel from already-recorded six-neighbor occupancy. If n_2=0 the
unique letter is UNDEFINED; else it is sign(n_2) in {+,−}. Reverse and face
are scored on that unique letter. Not unique P_+ along n. Not unique letter
sign(n_1). Not ndot. Uniqueness is not required. Displayed, not adopted.
"""

from __future__ import annotations

import ast
from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/NSSAME_SIGN_N2_UNIQUE_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NSSAME_SIGN_N2_UNIQUE_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Vec3 = tuple[Fraction, Fraction, Fraction]
ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
STEPS: tuple[Point, ...] = (
    E1,
    (-1, 0, 0),
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)
AXES: tuple[Point, Point, Point] = (E1, E2, E3)
SIGN_LETTERS = frozenset({"+", "-"})
ZERO_N: Vec3 = (Fraction(0), Fraction(0), Fraction(0))
PROBES: dict[str, Point] = {
    "A": (1, 0, 0),
    "B": (1, 1, 1),
    "C": (2, 0, 0),
    "D": (1, 1, 0),
}
EXPECTED_N = {
    "A": (Fraction(-1, 3), Fraction(-1, 3), Fraction(0)),
    "B": (Fraction(-1, 3), Fraction(0), Fraction(0)),
    "C": (Fraction(-1, 3), Fraction(0), Fraction(0)),
    "D": (Fraction(-1, 3), Fraction(1, 3), Fraction(0)),
}
EXPECTED_TICKS = {"A": 3, "B": 2, "C": 4, "D": 3}
EXPECTED_K = {"A": 2, "B": 1, "C": 1, "D": 2}
EXPECTED_LETTERS = {
    "A": "-",
    "B": "UNDEFINED",
    "C": "UNDEFINED",
    "D": "+",
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
    "nfplus",
)
CLAIM_SCOPE = (
    "Reverse and face from unique letter sign(n_2) on the four "
    "nssame probes are reported. Displayed, not adopted."
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]


def lock_axis(lock: Point) -> Point:
    return (abs(lock[0]), abs(lock[1]), abs(lock[2]))


def euclidean_ball() -> frozenset[Point]:
    return frozenset(
        (x, y, z)
        for x, y, z in product(range(-3, 4), repeat=3)
        if x * x + y * y + z * z <= 9
    )


def apply_matrix(matrix: tuple[tuple[int, ...], ...], point: Point) -> Point:
    return tuple(
        matrix[row][0] * point[0]
        + matrix[row][1] * point[1]
        + matrix[row][2] * point[2]
        for row in range(3)
    )


def matrix_det(matrix: tuple[tuple[int, ...], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def proper_cubic_rotations() -> tuple[tuple[tuple[int, ...], ...], ...]:
    rotations: list[tuple[tuple[int, ...], ...]] = []
    for perm in permutations((0, 1, 2)):
        for signs in product((1, -1), repeat=3):
            matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for col in range(3):
                matrix[perm[col]][col] = signs[col]
            packed = tuple(tuple(row) for row in matrix)
            if matrix_det(packed) == 1:
                rotations.append(packed)
    return tuple(rotations)


def grow(
    host: frozenset[Point],
    seed: tuple[tuple[Point, Point], ...],
) -> dict[Point, tuple[int, frozenset[Point]]]:
    recorded: dict[Point, tuple[int, frozenset[Point]]] = {
        site: (0, frozenset({lock})) for site, lock in seed
    }
    by_tick: dict[int, list[Point]] = defaultdict(list)
    for site, _lock in seed:
        if site not in host:
            raise ValueError("seed site outside host")
        by_tick[0].append(site)
    tick = 0
    while by_tick[tick]:
        arrivals: dict[Point, set[Point]] = defaultdict(set)
        for site in by_tick[tick]:
            _time, locks = recorded[site]
            for lock in locks:
                axis = lock_axis(lock)
                for step in STEPS:
                    if dot(step, axis) != 0:
                        continue
                    image = add(site, step)
                    if image not in host or image in recorded:
                        continue
                    arrivals[image].add(step)
        for image, incoming in arrivals.items():
            recorded[image] = (tick + 1, frozenset(incoming))
            by_tick[tick + 1].append(image)
        tick += 1
    return recorded


def occupancy(site: Point, formed: frozenset[Point], letter: str | None = None) -> int:
    """Occupancy is 1 on already-recorded sites. A letter does not feed n."""
    if letter is not None and letter not in SIGN_LETTERS:
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


def unique_letter_sign_n2(n: Vec3) -> str:
    """Unique letter sign(n_2). UNDEFINED if n_2=0. Not P_+ along n."""
    if n[1] == 0:
        return "UNDEFINED"
    return "+" if n[1] > 0 else "-"


def unique_plus_from_n(n: Vec3) -> str:
    """Refused leftover: unique P_+ along n. Identically + at n≠0."""
    if n == ZERO_N:
        return "UNDEFINED"
    return "+"


def unique_letter_sign_n1(n: Vec3) -> str:
    """Refused leftover: unique letter sign(n_1). Identically − here."""
    if n[0] == 0:
        return "UNDEFINED"
    return "+" if n[0] > 0 else "-"


def ndot_letter_from_n(n: Vec3, direction: Point) -> str:
    """Refused ndot: unique letter sign(n·v). Not used for reverse/face."""
    contraction = n[0] * direction[0] + n[1] * direction[1] + n[2] * direction[2]
    if contraction == 0:
        return "UNDEFINED"
    return "+" if contraction > 0 else "-"


def reverse_report(letter_a: str, letter_b: str) -> str:
    """Reverse iff L(A)=+ and L(B)=−. UNDEFINED if a needed letter is UNDEFINED."""
    if letter_a == "UNDEFINED" or letter_b == "UNDEFINED":
        return "UNDEFINED"
    holds = letter_a == "+" and letter_b == "-"
    return "all" if holds else "none"


def face_report(letter_c: str, letter_d: str) -> str:
    """Face iff L(C)=+ and L(D)=−. UNDEFINED if a needed letter is UNDEFINED."""
    if letter_c == "UNDEFINED" or letter_d == "UNDEFINED":
        return "UNDEFINED"
    holds = letter_c == "+" and letter_d == "-"
    return "all" if holds else "none"


def letter_display(letter: str) -> str:
    if letter == "-":
        return "−"
    return letter


def format_component(value: Fraction) -> str:
    if value == 0:
        return "0"
    sign = "−" if value < 0 else ""
    magnitude = abs(value)
    if magnitude.denominator == 1:
        return f"{sign}{magnitude.numerator}"
    return f"{sign}{magnitude.numerator}/{magnitude.denominator}"


def format_n(n: Vec3) -> str:
    return f"({format_component(n[0])}, {format_component(n[1])}, {format_component(n[2])})"


def already_recorded(
    site: Point, recorded: dict[Point, tuple[int, frozenset[Point]]]
) -> frozenset[Point]:
    formation = recorded[site][0]
    return frozenset(
        other for other, (tick, _locks) in recorded.items() if tick < formation
    )


def neighbor_occupancy(
    site: Point, formed: frozenset[Point]
) -> dict[str, tuple[int, int]]:
    bits: dict[str, tuple[int, int]] = {}
    names = ("e1", "e2", "e3")
    for name, axis in zip(names, AXES):
        plus = occupancy(add(site, axis), formed)
        minus = occupancy(add(site, (-axis[0], -axis[1], -axis[2])), formed)
        bits[name] = (plus, minus)
    return bits


def audit_paths_literal(source: str) -> tuple[str, ...] | None:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                value = ast.literal_eval(node.value)
                if isinstance(value, tuple) and all(
                    isinstance(item, str) for item in value
                ):
                    return value
                return None
    return None


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    host = euclidean_ball()
    seed_same: tuple[tuple[Point, Point], ...] = (
        (ORIGIN, E1),
        (E2, E1),
    )
    seed_mixed: tuple[tuple[Point, Point], ...] = (
        (ORIGIN, E1),
        (E2, E2),
    )

    recorded = grow(host, seed_same)
    kernels: dict[str, Vec3] = {}
    letters: dict[str, str] = {}
    for name, site in PROBES.items():
        formed = already_recorded(site, recorded)
        n = n_vector(site, formed)
        kernels[name] = n
        letters[name] = unique_letter_sign_n2(n)

    reverse_status = reverse_report(letters["A"], letters["B"])
    face_status = face_report(letters["C"], letters["D"])

    print("external_scientific_inputs: none; exact occupancy kernels and unique letters only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("host: Euclidean B_3(0) with n·n<=9")
    print(f"host_site_count: {len(host)}")
    print("seed: {0,(0,1,0)} both locking +e_1 at tick 0")
    print("process: nssame perp-step incoming-lock")
    print("kernel: formdraw n_μ=(o_{+μ}−o_{−μ})/3 from already-recorded 6-NN")
    print("unique letter: sign(n_2); UNDEFINED if n_2=0")
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        formed = already_recorded(site, recorded)
        occ = neighbor_occupancy(site, formed)
        n = kernels[name]
        print(
            f"n({name})={format_n(n)} k={k_value(n)} n2={n[1]} "
            f"L={letter_display(letters[name])} t={recorded[site][0]} "
            f"occ=+−e1{occ['e1']} +−e2{occ['e2']} +−e3{occ['e3']} "
            f"incoming={sorted(recorded[site][1])}"
        )
    print(f"n(C)=n(D): {kernels['C'] == kernels['D']}")
    print(f"reverse={reverse_status} face={face_status}")
    print("claim_boundary: displayed, not adopted; not written into Admissibility")
    print("cache_write: false")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print(f"claim_scope: {CLAIM_SCOPE}")

    declared = audit_paths_literal(self_source)
    checks.check(
        "audit-input-paths-literal",
        "AUDIT_INPUT_PATHS is the declared two-path static tuple",
        declared == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL),
    )
    checks.check(
        "audit-input-files",
        "declared review inputs exist",
        AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    wide_host = frozenset(
        (x, y, z)
        for x, y, z in product(range(-4, 5), repeat=3)
        if x * x + y * y + z * z <= 9
    )
    checks.check(
        "host-euclidean-ball",
        "host is exactly {n in Z^3 : n·n <= 9}",
        host == wide_host
        and all(dot(site, site) <= 9 for site in host)
        and len(host) == 123,
    )
    checks.check(
        "seed-two-site-same-lock",
        "tick-0 records are origin and (0,1,0), both locking +e_1",
        recorded[ORIGIN] == (0, frozenset({E1}))
        and recorded[E2] == (0, frozenset({E1}))
        and sum(time == 0 for time, _locks in recorded.values()) == 2,
    )
    checks.check(
        "identity-gates-present",
        "occupancy, n_vector, unique_letter_sign_n2, reverse, face, and grow are computed",
        "def occupancy(" in self_source
        and "def n_vector(" in self_source
        and "def unique_letter_sign_n2(" in self_source
        and "def reverse_report(" in self_source
        and "def face_report(" in self_source
        and "def grow(" in self_source
        and "n_μ = (o_{+μ} − o_{−μ}) / 3" in self_source,
    )
    checks.check(
        "unique-letter-sign-n2-identity",
        "sign(n_2) is UNDEFINED at n_2=0 and ± according to n_2",
        unique_letter_sign_n2(ZERO_N) == "UNDEFINED"
        and unique_letter_sign_n2((Fraction(-1, 3), Fraction(0), Fraction(0)))
        == "UNDEFINED"
        and unique_letter_sign_n2((Fraction(-1, 3), Fraction(-1, 3), Fraction(0)))
        == "-"
        and unique_letter_sign_n2((Fraction(-1, 3), Fraction(1, 3), Fraction(0)))
        == "+",
    )
    checks.check(
        "reverse-face-undefined-when-letter-undefined",
        "needed UNDEFINED letter makes reverse/face UNDEFINED; else all or none",
        reverse_report("UNDEFINED", "-") == "UNDEFINED"
        and reverse_report("+", "UNDEFINED") == "UNDEFINED"
        and face_report("UNDEFINED", "-") == "UNDEFINED"
        and face_report("+", "UNDEFINED") == "UNDEFINED"
        and reverse_report("+", "-") == "all"
        and reverse_report("-", "-") == "none"
        and reverse_report("+", "+") == "none"
        and face_report("+", "-") == "all"
        and face_report("-", "+") == "none"
        and face_report("-", "-") == "none",
    )
    for name in ("A", "B", "C", "D"):
        rendered = f"n({name}) = {format_n(kernels[name])}"
        letter_line = f"L({name}) = {letter_display(letters[name])}"
        checks.check(
            f"thm1-n-{name}",
            f"computed n({name}) and unique letter are recorded in the note",
            rendered in note
            and letter_line in note
            and PROBES[name] in recorded
            and kernels[name] == EXPECTED_N[name]
            and k_value(kernels[name]) == EXPECTED_K[name]
            and letters[name] == EXPECTED_LETTERS[name]
            and recorded[PROBES[name]][0] == EXPECTED_TICKS[name],
        )
    checks.check(
        "thm1-nC-not-equal-nD",
        "n(C)=n(D) fails and the split is n_2",
        kernels["C"] != kernels["D"]
        and kernels["C"][1] == 0
        and kernels["D"][1] == Fraction(1, 3)
        and "n(C) ≠ n(D)" in note
        and "split is n_2" in note,
    )
    checks.check(
        "thm1-n-nonzero-n2-zero-undefined",
        "all four n≠0, but n_2=0 at B and C is UNDEFINED",
        all(kernels[name] != ZERO_N for name in ("A", "B", "C", "D"))
        and letters["A"] == "-"
        and letters["B"] == "UNDEFINED"
        and letters["C"] == "UNDEFINED"
        and letters["D"] == "+",
    )
    checks.check(
        "theorem2-reverse-undefined",
        "reverse is UNDEFINED because L(B) is UNDEFINED",
        reverse_status == "UNDEFINED"
        and letters["A"] == "-"
        and letters["B"] == "UNDEFINED"
        and note.count("Report: `UNDEFINED`.") == 2,
    )
    checks.check(
        "theorem3-face-undefined",
        "face is UNDEFINED because L(C) is UNDEFINED",
        face_status == "UNDEFINED"
        and letters["C"] == "UNDEFINED"
        and letters["D"] == "+"
        and "all" in note
        and "some" in note
        and "none" in note,
    )
    pplus_letters = {name: unique_plus_from_n(kernels[name]) for name in PROBES}
    pplus_reverse = reverse_report(pplus_letters["A"], pplus_letters["B"])
    pplus_face = face_report(pplus_letters["C"], pplus_letters["D"])
    n1_letters = {name: unique_letter_sign_n1(kernels[name]) for name in PROBES}
    n1_reverse = reverse_report(n1_letters["A"], n1_letters["B"])
    n1_face = face_report(n1_letters["C"], n1_letters["D"])
    ndot_e1 = {name: ndot_letter_from_n(kernels[name], E1) for name in PROBES}
    ndot_e3 = {name: ndot_letter_from_n(kernels[name], E3) for name in PROBES}
    checks.check(
        "not-pplus-along-n",
        "unique P_+ along n is identically + and scores reverse/face none",
        all(pplus_letters[name] == "+" for name in ("A", "B", "C", "D"))
        and pplus_reverse == "none"
        and pplus_face == "none"
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED"
        and letters["A"] != pplus_letters["A"]
        and letters["B"] != pplus_letters["B"]
        and "not unique P_+ along n" in normalized_note,
    )
    checks.check(
        "not-sign-n1",
        "unique letter sign(n_1) is identically − because n_1 is constant",
        all(kernels[name][0] == Fraction(-1, 3) for name in ("A", "B", "C", "D"))
        and all(n1_letters[name] == "-" for name in ("A", "B", "C", "D"))
        and n1_reverse == "none"
        and n1_face == "none"
        and letters["A"] == n1_letters["A"]
        and letters["B"] != n1_letters["B"]
        and letters["D"] != n1_letters["D"]
        and "not unique letter `sign(n_1)`" in note,
    )
    checks.check(
        "not-ndot",
        "scoring is not ndot along e_1 or e_3",
        all(ndot_e1[name] == "-" for name in ("A", "B", "C", "D"))
        and all(ndot_e3[name] == "UNDEFINED" for name in ("A", "B", "C", "D"))
        and reverse_report(ndot_e1["A"], ndot_e1["B"]) == "none"
        and reverse_report(ndot_e3["A"], ndot_e3["B"]) == "UNDEFINED"
        and reverse_status == "UNDEFINED"
        and letters["D"] != ndot_e1["D"]
        and "not ndot" in normalized_note,
    )
    formed_a = already_recorded(PROBES["A"], recorded)
    formed_d = already_recorded(PROBES["D"], recorded)
    checks.check(
        "already-recorded-six-nn",
        "occupancy reads strictly earlier 6-NN, not the unread probe",
        occupancy(PROBES["A"], formed_a) == 0
        and occupancy(ORIGIN, formed_a) == 1
        and occupancy(PROBES["D"], formed_a) == 0
        and occupancy(add(PROBES["A"], (0, -1, 0)), formed_a) == 1
        and occupancy(add(PROBES["D"], E2), formed_d) == 1
        and occupancy(PROBES["A"], formed_d) == 0,
    )
    checks.check(
        "uniqueness-not-required",
        "first-arrival incoming locks at A and D need not be unique",
        len(recorded[PROBES["A"]][1]) > 1
        and len(recorded[PROBES["D"]][1]) > 1
        and "Uniqueness is not required" in note,
    )
    same_seed_locks = frozenset(seed_same)
    mixed_orbit = False
    for matrix in proper_cubic_rotations():
        image = frozenset(
            (apply_matrix(matrix, site), apply_matrix(matrix, lock))
            for site, lock in seed_mixed
        )
        if image == same_seed_locks:
            mixed_orbit = True
            break
    checks.check(
        "not-mixed-cubic-orbit",
        "same-lock seed is outside the proper cubic orbit of mixed +e_1/+e_2",
        (not mixed_orbit)
        and len(proper_cubic_rotations()) == 24
        and seed_same[0][1] == seed_same[1][1]
        and seed_mixed[0][1] != seed_mixed[1][1],
    )
    origin_parallel_blocked = all(
        recorded[ORIGIN][0] + 1
        != recorded.get(add(ORIGIN, step), (None, frozenset()))[0]
        for step in (E1, (-1, 0, 0))
    )
    checks.check(
        "perp-step-incoming-lock",
        "origin lock +e_1 blocks parallel steps and allows the four perpendicular steps",
        origin_parallel_blocked
        and recorded[(0, -1, 0)][0] == 1
        and recorded[E3][0] == 1
        and recorded[(0, 0, -1)][0] == 1
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "incoming-locks-are-nn-steps-not-letters",
        "incoming locks are unit NN steps, not {+,−} unique letters",
        all(recorded[PROBES[name]][1] <= frozenset(STEPS) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "letters-do-not-feed-occupancy",
        "occupancy is independent of a later unique letter",
        occupancy(PROBES["A"], frozenset(recorded), "+")
        == occupancy(PROBES["A"], frozenset(recorded), "-")
        == occupancy(PROBES["A"], frozenset(recorded), None)
        == 1
        and occupancy((4, 0, 0), frozenset(recorded), "+") == 0
        and "does not feed `n`" in note,
    )
    signed_minus_as_vacant = frozenset(site for site in formed_a if site != ORIGIN)
    checks.check(
        "mutation-minus-as-vacant-changes-n",
        "dropping an already-recorded neighbor changes n",
        n_vector(PROBES["A"], signed_minus_as_vacant) != EXPECTED_N["A"],
    )
    one_site = grow(host, ((ORIGIN, E1),))
    one_site_n = {
        name: n_vector(PROBES[name], already_recorded(PROBES[name], one_site))
        for name in ("A", "B", "C", "D")
        if PROBES[name] in one_site
    }
    checks.check(
        "mutation-one-site-seed-changes-n",
        "one-site seed disagrees with the nssame kernels",
        one_site_n != kernels,
    )
    checks.check(
        "note-claim-scope",
        "note claim_scope matches the unique-letter reverse/face report",
        CLAIM_SCOPE in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "display is not written into Admissibility and names no extra axiom",
        "displayed, not adopted" in normalized_note.lower()
        and "not written into Admissibility" in normalized_note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "Admissibility / Local Constraint" in axiom,
    )
    checks.check(
        "note-does-not-identify-incoming",
        "unique letters are not identified with incoming steps",
        "not identified" in normalized_note and "incoming step" in normalized_note,
    )
    checks.check(
        "note-does-not-feed-n-or-attach-formation-member",
        "letters do not feed n and the occupancy-kernel formation member is not attached",
        "does not feed `n`" in note
        and "does not attach the occupancy-kernel formation member" in normalized_note
        and "Do not attach" not in note,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "formation stays inside B_3(0) and no runner cache is written",
        all(dot(site, site) <= 9 for site in recorded)
        and set(recorded) <= host
        and "No larger host is used." in normalized_note
        and "No runner cache is written." in normalized_note,
    )
    checks.check(
        "note-ticks",
        "formation ticks of the four probes are recorded",
        "t(A)=t(1,0,0)=3" in note
        and "t(B)=t(1,1,1)=2" in note
        and "t(C)=t(2,0,0)=4" in note
        and "t(D)=t(1,1,0)=3" in note
        and "3 t(" not in note,
    )
    checks.check(
        "note-n-gates-present",
        "no-go discipline gates N1 through N8 are present",
        all(f"### N{index}" in note for index in range(1, 9)),
    )
    checks.check(
        "note-forbidden-tokens-absent",
        "note omits excluded claim language and does not attach a first-lemma tag",
        all(token not in note for token in FORBIDDEN_NOTE_TOKENS)
        and "16-census" not in note
        and "16-letter" not in note,
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
        "note authors no retained or promoted verdict",
        all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "FAIL / DO NOT SHIP" in note,
    )
    lattice_quote = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    record_quote = (
        "When present, a record locks exactly one admissible local possibility."
    )
    checks.check(
        "axiom-quotes-unedited",
        "Lattice, Qubit, and Record sentences are quoted from the live axiom memo",
        lattice_quote in normalized_axiom
        and record_quote in normalized_axiom
        and lattice_quote in normalized_note
        and record_quote in normalized_note
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in note
        and "does not supply the formation site, probability, or rate"
        in normalized_note
        and "Records form." in axiom
        and "A site with no record cannot be read." in axiom,
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS is a static two-path literal in the runner source",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/NSSAME_SIGN_N2_UNIQUE_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in self_source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
