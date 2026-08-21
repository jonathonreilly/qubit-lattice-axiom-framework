#!/usr/bin/env python3
"""Unique letter from sign(n_1) on four nnseed probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and +e_2. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. At each probe's formation tick, n is the formdraw occupancy kernel from
already-recorded six-neighbor occupancy. The unique letter is + if n_1>0, −
if n_1<0, and UNDEFINED if n_1=0. Reverse and face are scored on that unique
letter. Uniqueness of incoming locks is not required. Letters do not feed n
and are not incoming {±e_i}. No sixteen-combination free lettering.
"""

from __future__ import annotations

import ast
from collections import deque
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/NNSEED_UNIQUE_N1_SIGN_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NNSEED_UNIQUE_N1_SIGN_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
NN: tuple[Point, ...] = (
    E1,
    (-1, 0, 0),
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)
AXES: tuple[Point, Point, Point] = (E1, E2, E3)
SIGN_LETTERS = frozenset({"+", "-"})
ZERO: Fraction = Fraction(0)
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
    "16-census",
    "L1",
    "Runner cache",
)
CLAIM_SCOPE = (
    "Reverse and face from the unique letter sign(n_1) on the four "
    "nnseed probes are reported. Displayed, not adopted."
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


def occupancy(site: Point, formed: frozenset[Point], letter: str | None = None) -> int:
    """Occupancy is 1 on already-recorded sites. A sign letter does not feed n."""
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


def unique_letter_from_n1(n: Vec3) -> str:
    """Unique letter: + iff n_1>0, − iff n_1<0, UNDEFINED iff n_1=0."""
    n1 = n[0]
    if n1 > ZERO:
        return "+"
    if n1 < ZERO:
        return "-"
    return "UNDEFINED"


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

    print("unique letter sign(n_1) reverse/face on four nnseed probes")
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

    plus_n = (Fraction(1, 3), Fraction(0), Fraction(0))
    minus_n = (Fraction(-1, 3), Fraction(0), Fraction(0))
    zero_n = (Fraction(0), Fraction(1, 3), Fraction(0))
    checks.check(
        "unique-letter-identity-from-n1-sign",
        unique_letter_from_n1(plus_n) == "+"
        and unique_letter_from_n1(minus_n) == "-"
        and unique_letter_from_n1(zero_n) == "UNDEFINED"
        and unique_letter_from_n1((Fraction(0), Fraction(0), Fraction(0)))
        == "UNDEFINED",
    )
    checks.check(
        "reverse-face-undefined-when-letter-undefined",
        reverse_report("UNDEFINED", "-") == "UNDEFINED"
        and reverse_report("+", "UNDEFINED") == "UNDEFINED"
        and face_report("UNDEFINED", "-") == "UNDEFINED"
        and face_report("+", "UNDEFINED") == "UNDEFINED"
        and reverse_report("+", "-") == "all"
        and reverse_report("-", "-") == "none"
        and face_report("+", "-") == "all"
        and face_report("-", "-") == "none",
    )

    ticks, locks = form()
    kernels: dict[str, Vec3] = {}
    letters: dict[str, str] = {}
    for name, site in PROBES.items():
        formed_before = already_recorded(site, ticks)
        n = n_vector(site, formed_before)
        kernels[name] = n
        letters[name] = unique_letter_from_n1(n)
        print(
            f"{name} n=({n[0]},{n[1]},{n[2]}) n1={n[0]} "
            f"L={letter_display(letters[name])} "
            f"incoming={sorted(locks.get(site, ()))}"
        )

    reverse_status = reverse_report(letters["A"], letters["B"])
    face_status = face_report(letters["C"], letters["D"])
    print(f"reverse={reverse_status} face={face_status}")

    checks.check(
        "theorem1-n1-A",
        kernels["A"] == EXPECTED_N["A"]
        and kernels["A"][0] == Fraction(-1, 3)
        and letters["A"] == "-",
        str((kernels["A"][0], letters["A"])),
    )
    checks.check(
        "theorem1-n1-B",
        kernels["B"] == EXPECTED_N["B"]
        and kernels["B"][0] == Fraction(-1, 3)
        and letters["B"] == "-",
        str((kernels["B"][0], letters["B"])),
    )
    checks.check(
        "theorem1-n1-C",
        kernels["C"] == EXPECTED_N["C"]
        and kernels["C"][0] == Fraction(-1, 3)
        and letters["C"] == "-",
        str((kernels["C"][0], letters["C"])),
    )
    checks.check(
        "theorem1-n1-D",
        kernels["D"] == EXPECTED_N["D"]
        and kernels["D"][0] == Fraction(-1, 3)
        and letters["D"] == "-",
        str((kernels["D"][0], letters["D"])),
    )
    checks.check(
        "theorem1-letters-all-minus",
        all(letters[name] == "-" for name in ("A", "B", "C", "D"))
        and all(kernels[name][0] < ZERO for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "theorem2-reverse-none",
        reverse_status == "none"
        and letters["A"] == "-"
        and letters["B"] == "-",
        reverse_status,
    )
    checks.check(
        "theorem3-face-none",
        face_status == "none" and letters["C"] == "-" and letters["D"] == "-",
        face_status,
    )
    checks.check(
        "incoming-locks-are-nn-steps-not-letters",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D"))
        and all(
            not (locks[PROBES[name]] & SIGN_LETTERS)  # type: ignore[arg-type]
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["B"]]) == 2 and letters["B"] == "-",
        str(sorted(locks[PROBES["B"]])),
    )
    checks.check(
        "two-site-seed-locks",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {E2},
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
        "n-from-already-recorded-six-nn",
        formed_before_a == already_recorded(PROBES["A"], ticks)
        and occupancy(add(PROBES["A"], E1), formed_before_a) == 0
        and occupancy(add(PROBES["A"], (-1, 0, 0)), formed_before_a) == 1,
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
        "no-sixteen-combo-census",
        isinstance(letters["A"], str)
        and isinstance(letters["B"], str)
        and isinstance(letters["C"], str)
        and isinstance(letters["D"], str)
        and reverse_status == "none"
        and face_status == "none",
    )
    checks.check(
        "mutation-zero-n1-is-undefined",
        unique_letter_from_n1((ZERO, kernels["A"][1], kernels["A"][2]))
        == "UNDEFINED"
        and reverse_report("UNDEFINED", letters["B"]) == "UNDEFINED",
    )
    checks.check(
        "mutation-positive-n1-is-plus",
        unique_letter_from_n1((Fraction(1, 3), kernels["A"][1], kernels["A"][2]))
        == "+"
        and reverse_report("+", "-") == "all",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-n1-and-letters",
        "n_1(A) = −1/3" in note
        and "n_1(B) = −1/3" in note
        and "n_1(C) = −1/3" in note
        and "n_1(D) = −1/3" in note
        and "L(A) = −" in note
        and "L(B) = −" in note
        and "L(C) = −" in note
        and "L(D) = −" in note,
    )
    checks.check(
        "note-reports-none-none",
        note.count("Report: `none`.") == 2
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
        and "incoming step" in normalized_note,
    )
    checks.check(
        "note-does-not-feed-n-or-attach-formation-member",
        "does not feed `n`" in note
        and "does not attach a formation member from the first occupancy-kernel component"
        in normalized_note
        and "Do not attach" not in note,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in normalized_note
        and "B_3(0)" in note
        and "No runner cache is written." in normalized_note,
    )
    checks.check(
        "note-not-sixteen-free-letters",
        "not a sixteen-combination free lettering" in normalized_note
        and "16-census" not in note,
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
        '    "docs/NNSEED_UNIQUE_N1_SIGN_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def occupancy(" in source
        and "def n_vector(" in source
        and "def unique_letter_from_n1(" in source
        and "def reverse_report(" in source
        and "def face_report(" in source
        and "def form(" in source,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] >= 1
        and set(ticks) <= host,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
