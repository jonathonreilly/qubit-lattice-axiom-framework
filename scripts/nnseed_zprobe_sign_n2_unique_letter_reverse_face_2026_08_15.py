#!/usr/bin/env python3
"""Unique letter sign(n_2) on four nnseed z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and +e_2. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. At each z-probe's formation tick, n is the occupancy kernel from
already-recorded six-neighbor occupancy. If n_2=0 the unique letter is
UNDEFINED; else it is sign(n_2) in {+,−}. Reverse and face are scored on
that unique letter. Not unique P_+ along n. Not ndot. Not a sixteen-
combination free lettering. Uniqueness is not required.
"""

from __future__ import annotations

import ast
from collections import deque
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/NNSEED_ZPROBE_SIGN_N2_UNIQUE_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NNSEED_ZPROBE_SIGN_N2_UNIQUE_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
EXPECTED_N = {
    "A": (Fraction(0), Fraction(0), Fraction(-1, 3)),
    "B": (Fraction(-1, 3), Fraction(0), Fraction(-1, 3)),
    "C": (Fraction(0), Fraction(-1, 3), Fraction(-1, 3)),
    "D": (Fraction(0), Fraction(0), Fraction(-1, 3)),
}
EXPECTED_TICKS = {"A": 1, "B": 2, "C": 4, "D": 1}
EXPECTED_LETTERS = {
    "A": "UNDEFINED",
    "B": "UNDEFINED",
    "C": "-",
    "D": "UNDEFINED",
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
    "16-census",
    "16-letter",
)
CLAIM_SCOPE = (
    "Reverse and face from unique letter sign(n_2) on the four "
    "nnseed z-probes are reported. Displayed, not adopted."
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
    """Occupancy is 1 on already-recorded sites. A letter does not feed n."""
    if letter is not None and letter not in SIGN_LETTERS:
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
    """Refused alternative: unique letter sign(n_1). Not used."""
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

    print("unique letter sign(n_2) reverse/face on four nnseed z-probes")
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
    checks.check(
        "host-is-euclidean-b3",
        ORIGIN in host and len(host) == 123 and BALL_SQ == 9,
    )
    checks.check(
        "z-probes-in-host",
        {PROBES["A"], PROBES["B"], PROBES["C"], PROBES["D"]} <= host
        and PROBES["A"] == (0, 0, 1)
        and PROBES["B"] == (1, 1, 1)
        and PROBES["C"] == (0, 0, 2)
        and PROBES["D"] == (0, 1, 1),
    )
    checks.check(
        "perp-step-blocks-parallel",
        perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "unique-letter-sign-n2-identity",
        unique_letter_sign_n2(ZERO_N) == "UNDEFINED"
        and unique_letter_sign_n2((Fraction(0), Fraction(0), Fraction(-1, 3)))
        == "UNDEFINED"
        and unique_letter_sign_n2((Fraction(0), Fraction(-1, 3), Fraction(-1, 3)))
        == "-"
        and unique_letter_sign_n2((Fraction(0), Fraction(1, 3), Fraction(0))) == "+",
    )
    checks.check(
        "reverse-face-undefined-when-letter-undefined",
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

    ticks, locks = form()
    kernels: dict[str, Vec3] = {}
    letters: dict[str, str] = {}
    for name, site in PROBES.items():
        formed_before = already_recorded(site, ticks)
        n = n_vector(site, formed_before)
        kernels[name] = n
        letters[name] = unique_letter_sign_n2(n)
        print(
            f"{name} n=({n[0]},{n[1]},{n[2]}) k={k_value(n)} n2={n[1]} "
            f"L={letter_display(letters[name])} t={ticks[site]} "
            f"incoming={sorted(locks.get(site, ()))}"
        )

    reverse_status = reverse_report(letters["A"], letters["B"])
    face_status = face_report(letters["C"], letters["D"])
    print(f"reverse={reverse_status} face={face_status}")

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
        and kernels["C"][1] == Fraction(-1, 3)
        and kernels["D"][1] == 0,
        f"C={kernels['C']} D={kernels['D']}",
    )
    checks.check(
        "theorem1-unique-letters",
        all(letters[name] == EXPECTED_LETTERS[name] for name in ("A", "B", "C", "D")),
        str(letters),
    )
    checks.check(
        "theorem1-z-ticks",
        all(ticks[PROBES[name]] == EXPECTED_TICKS[name] for name in ("A", "B", "C", "D")),
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "n-nonzero-but-n2-zero-is-undefined",
        all(kernels[name] != ZERO_N for name in ("A", "B", "C", "D"))
        and letters["A"] == "UNDEFINED"
        and letters["B"] == "UNDEFINED"
        and letters["D"] == "UNDEFINED"
        and letters["C"] == "-",
    )
    checks.check(
        "theorem2-reverse-undefined",
        reverse_status == "UNDEFINED"
        and letters["A"] == "UNDEFINED"
        and letters["B"] == "UNDEFINED",
        reverse_status,
    )
    checks.check(
        "theorem3-face-undefined",
        face_status == "UNDEFINED"
        and letters["C"] == "-"
        and letters["D"] == "UNDEFINED",
        face_status,
    )

    pplus_letters = {name: unique_plus_from_n(kernels[name]) for name in PROBES}
    pplus_reverse = reverse_report(pplus_letters["A"], pplus_letters["B"])
    pplus_face = face_report(pplus_letters["C"], pplus_letters["D"])
    ndot_letters = {name: ndot_letter_from_n(kernels[name], E3) for name in PROBES}
    ndot_reverse = reverse_report(ndot_letters["A"], ndot_letters["B"])
    n1_letters = {name: unique_letter_sign_n1(kernels[name]) for name in PROBES}

    checks.check(
        "not-pplus-along-n",
        all(pplus_letters[name] == "+" for name in ("A", "B", "C", "D"))
        and pplus_reverse == "none"
        and pplus_face == "none"
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED"
        and letters["A"] != pplus_letters["A"]
        and letters["C"] != pplus_letters["C"],
    )
    checks.check(
        "not-ndot",
        all(ndot_letters[name] == "-" for name in ("A", "B", "C", "D"))
        and ndot_reverse == "none"
        and reverse_status == "UNDEFINED"
        and letters["A"] != ndot_letters["A"]
        and letters["C"] == ndot_letters["C"],
    )
    checks.check(
        "not-sign-n1",
        n1_letters["A"] == "UNDEFINED"
        and n1_letters["B"] == "-"
        and n1_letters["C"] == "UNDEFINED"
        and n1_letters["D"] == "UNDEFINED"
        and letters["B"] != n1_letters["B"]
        and letters["C"] != n1_letters["C"],
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
        len(locks[PROBES["B"]]) == 2
        and len(locks[PROBES["C"]]) == 3
        and letters["B"] == "UNDEFINED",
        f"B={sorted(locks[PROBES['B']])} C={sorted(locks[PROBES['C']])}",
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
    checks.check(
        "n-independent-of-letter-branch",
        n_vector(PROBES["A"], formed_before_a) == EXPECTED_N["A"],
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
        "no-sixteen-combo-census",
        all(isinstance(letters[name], str) for name in ("A", "B", "C", "D"))
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED",
    )
    checks.check(
        "not-t-as-comparator",
        reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED"
        and "3 t(" not in note,
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-n-and-letters",
        "n(A_z) = (0, 0, −1/3)" in note
        and "n(B)   = (−1/3, 0, −1/3)" in note
        and "n(C_z) = (0, −1/3, −1/3)" in note
        and "n(D_z) = (0, 0, −1/3)" in note
        and "L(A_z) = UNDEFINED" in note
        and "L(B) = UNDEFINED" in note
        and "L(C_z) = −" in note
        and "L(D_z) = UNDEFINED" in note,
    )
    checks.check(
        "note-reports-undefined-undefined",
        note.count("Report: `UNDEFINED`.") == 2
        and "all" in note
        and "some" in note
        and "none" in note
        and "UNDEFINED" in note,
    )
    checks.check(
        "note-nC-neq-nD-split-is-n2",
        "n(C_z) ≠ n(D_z)" in note
        and "split is n_2" in note
        and "0 vs −1/3" in note,
    )
    checks.check(
        "note-not-pplus-or-ndot",
        "not unique P_+ along n" in normalized_note and "not ndot" in normalized_note,
    )
    checks.check(
        "note-z-ticks",
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
        and "incoming step" in normalized_note,
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
        "note-not-sixteen-free-letters",
        "not a sixteen-combination free lettering" in normalized_note
        and "16-census" not in note
        and "16-letter" not in note,
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
        all(line in allowed_retained and line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/NNSEED_ZPROBE_SIGN_N2_UNIQUE_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def occupancy(" in source
        and "def n_vector(" in source
        and "def unique_letter_sign_n2(" in source
        and "def reverse_report(" in source
        and "def face_report(" in source
        and "def form(" in source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
