#!/usr/bin/env python3
"""Same-tick formdraw occupancy kernel n on four nnseed x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and +e_2. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. At each x-probe's formation tick, occupancy of a 6-NN p is 1 iff p
formed at tick <= t(q) and p!=q. n_μ=(o_{+μ}−o_{−μ})/3. If n(C)=n(D), the
unique splitting-component letter is not assigned and reverse/face are
UNDEFINED. Uniqueness is not required.
"""

from __future__ import annotations

import ast
from collections import deque
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/NNSEED_XPROBE_SAMETICK_FORMDRAW_KERNEL_SPLIT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NNSEED_XPROBE_SAMETICK_FORMDRAW_KERNEL_SPLIT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
Y_PROBES = {
    "A": (0, 1, 0),
    "B": (1, 1, 1),
    "C": (0, 2, 0),
    "D": (1, 1, 0),
}
CLAIM_SCOPE = (
    "Same-tick-inclusive formdraw occupancy kernel n on the four nnseed "
    "x-probes, equality of n(C) and n(D), and reverse/face from the unique "
    "splitting-component letter when they disagree (else UNDEFINED), are "
    "reported. Displayed, not adopted."
)
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


def occupancy(site: Point, formed: frozenset[Point], letter: str | None = None) -> int:
    """Occupancy is 1 on formed-at-or-before neighbors. A letter does not feed n."""
    if letter is not None and letter not in {"+", "-"}:
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


def splitting_mu_star(n_c: Vec3, n_d: Vec3) -> int | None:
    """First axis in (e_1,e_2,e_3) with n(C)≠n(D). None if they agree."""
    for index in range(3):
        if n_c[index] != n_d[index]:
            return index
    return None


def unique_letter_from_n(n: Vec3, mu_star: int | None) -> str:
    """Unique splitting-component letter, or UNDEFINED if no split or zero."""
    if mu_star is None:
        return "UNDEFINED"
    component = n[mu_star]
    if component == 0:
        return "UNDEFINED"
    return "+" if component > 0 else "-"


def unique_plus_from_n(n: Vec3) -> str:
    """Refused unique P_+: + whenever n≠0. Not used for reverse/face."""
    if n == ZERO_N:
        return "UNDEFINED"
    return "+"


def ndot_letter_from_n(n: Vec3, direction: Point) -> str:
    """Refused ndot: unique letter sign(n·v). Not used for reverse/face."""
    contraction = n[0] * direction[0] + n[1] * direction[1] + n[2] * direction[2]
    if contraction == 0:
        return "UNDEFINED"
    return "+" if contraction > 0 else "-"


def reverse_face_report(letter_a: str, letter_b: str, letter_c: str, letter_d: str) -> tuple[str, str]:
    if letter_a == "UNDEFINED" or letter_b == "UNDEFINED":
        reverse = "UNDEFINED"
    elif letter_a == "+" and letter_b == "-":
        reverse = "hold"
    else:
        reverse = "fail"
    if letter_c == "UNDEFINED" or letter_d == "UNDEFINED":
        face = "UNDEFINED"
    elif letter_c == "+" and letter_d == "-":
        face = "hold"
    else:
        face = "fail"
    return reverse, face


def format_component(value: Fraction) -> str:
    if value == 0:
        return "0"
    sign = "−" if value < 0 else ""
    magnitude = abs(value)
    if magnitude.denominator == 1:
        return f"{sign}{magnitude.numerator}"
    return f"{sign}{magnitude.numerator}/{magnitude.denominator}"


def format_n(n: Vec3) -> str:
    return (
        f"({format_component(n[0])}, {format_component(n[1])}, "
        f"{format_component(n[2])})"
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


def formed_at_or_before(site: Point, ticks: dict[Point, int]) -> frozenset[Point]:
    """Sites formed at tick ≤ t(q), with q excluded."""
    formation = ticks[site]
    return frozenset(
        other for other, tick in ticks.items() if tick <= formation and other != site
    )


def strictly_earlier(site: Point, ticks: dict[Point, int]) -> frozenset[Point]:
    """Strictly-earlier leftover occupancy. Not this display."""
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

    print("same-tick formdraw n on four nnseed x-probes; split letter or UNDEFINED")
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
        "x-probes-in-host",
        {PROBES["A"], PROBES["B"], PROBES["C"], PROBES["D"]} <= host
        and PROBES["A"] == (1, 0, 0)
        and PROBES["B"] == (1, 1, 1)
        and PROBES["C"] == (2, 0, 0)
        and PROBES["D"] == (1, 1, 0)
        and PROBES["A"] != Y_PROBES["A"]
        and PROBES["C"] != Y_PROBES["C"],
    )
    checks.check(
        "perp-step-blocks-parallel",
        perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )

    ticks, locks = form()
    kernels: dict[str, Vec3] = {}
    leftover: dict[str, Vec3] = {}
    for name, site in PROBES.items():
        formed = formed_at_or_before(site, ticks)
        kernels[name] = n_vector(site, formed)
        leftover[name] = n_vector(site, strictly_earlier(site, ticks))
        occ = neighbor_occupancy(site, formed)
        print(
            f"{name} t={ticks[site]} n={format_n(kernels[name])} "
            f"occ=+−e1{occ['e1']} +−e2{occ['e2']} +−e3{occ['e3']} "
            f"incoming={sorted(locks.get(site, ()))}"
        )

    mu_star = splitting_mu_star(kernels["C"], kernels["D"])
    letters = {
        name: unique_letter_from_n(kernels[name], mu_star) for name in ("A", "B", "C", "D")
    }
    reverse_status, face_status = reverse_face_report(
        letters["A"], letters["B"], letters["C"], letters["D"]
    )
    equal_cd = kernels["C"] == kernels["D"]
    print(f"n(C)=n(D): {equal_cd}")
    print(f"mu_star={mu_star} letters={letters}")
    print(f"reverse={reverse_status} face={face_status}")

    checks.check(
        "theorem1-n-A",
        kernels["A"] == (Fraction(-1, 3), Fraction(0), Fraction(0))
        and f"n(A) = {format_n(kernels['A'])}" in note,
        format_n(kernels["A"]),
    )
    checks.check(
        "theorem1-n-B",
        kernels["B"]
        == (Fraction(-1, 3), Fraction(-1, 3), Fraction(-1, 3))
        and f"n(B) = {format_n(kernels['B'])}" in note,
        format_n(kernels["B"]),
    )
    checks.check(
        "theorem1-n-C",
        kernels["C"] == (Fraction(-1, 3), Fraction(0), Fraction(0))
        and f"n(C) = {format_n(kernels['C'])}" in note,
        format_n(kernels["C"]),
    )
    checks.check(
        "theorem1-n-D",
        kernels["D"] == (Fraction(-1, 3), Fraction(0), Fraction(0))
        and f"n(D) = {format_n(kernels['D'])}" in note,
        format_n(kernels["D"]),
    )
    checks.check(
        "theorem1-nC-equals-nD",
        equal_cd
        and kernels["C"] == kernels["D"]
        and mu_star is None
        and "n(C)=n(D)" in note,
    )
    checks.check(
        "theorem2-reverse-undefined",
        reverse_status == "UNDEFINED"
        and all(letters[name] == "UNDEFINED" for name in ("A", "B", "C", "D"))
        and "Report: `UNDEFINED`." in note,
        reverse_status,
    )
    checks.check(
        "theorem3-face-undefined",
        face_status == "UNDEFINED"
        and note.count("Report: `UNDEFINED`.") == 2,
        face_status,
    )
    checks.check(
        "splitting-axis-undefined-when-equal",
        splitting_mu_star(kernels["C"], kernels["D"]) is None
        and unique_letter_from_n(kernels["A"], None) == "UNDEFINED"
        and splitting_mu_star(
            (Fraction(-1, 3), Fraction(0), Fraction(0)),
            (Fraction(-1, 3), Fraction(1, 3), Fraction(0)),
        )
        == 1,
    )
    checks.check(
        "not-unique-pplus",
        unique_plus_from_n(kernels["A"]) == "+"
        and unique_plus_from_n(kernels["B"]) == "+"
        and unique_plus_from_n(kernels["C"]) == "+"
        and unique_plus_from_n(kernels["D"]) == "+"
        and reverse_face_report("+", "+", "+", "+") == ("fail", "fail")
        and reverse_status == "UNDEFINED"
        and "not unique `P_+`" in normalized_note,
    )
    checks.check(
        "not-ndot",
        ndot_letter_from_n(kernels["A"], E1) == "-"
        and "not ndot" in normalized_note,
    )
    checks.check(
        "not-strictly-earlier-leftover",
        leftover["A"] == (Fraction(-1, 3), Fraction(1, 3), Fraction(0))
        and leftover["B"] == (Fraction(-1, 3), Fraction(0), Fraction(-1, 3))
        and leftover["C"] == kernels["C"]
        and leftover["D"] == kernels["D"]
        and leftover["A"] != kernels["A"]
        and leftover["B"] != kernels["B"]
        and "not the strictly-earlier leftover" in normalized_note,
    )
    checks.check(
        "not-sametick-yprobe-pvm",
        PROBES["A"] != Y_PROBES["A"]
        and PROBES["C"] != Y_PROBES["C"]
        and "not the same-tick y-probe" in normalized_note
        and "PVM lettering" in note,
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["B"]]) == 2 and "Uniqueness is not required" in note,
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
        "incoming-locks-are-nn-steps",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    formed_a = formed_at_or_before(PROBES["A"], ticks)
    checks.check(
        "same-tick-excludes-probe",
        PROBES["A"] not in formed_a
        and occupancy(PROBES["A"], formed_a) == 0
        and ticks[PROBES["A"]] == 2,
    )
    checks.check(
        "same-tick-counts-partners-at-A",
        occupancy(add(PROBES["A"], (0, -1, 0)), formed_a) == 1
        and occupancy(add(PROBES["A"], E3), formed_a) == 1
        and occupancy(add(PROBES["A"], (0, 0, -1)), formed_a) == 1
        and ticks[add(PROBES["A"], (0, -1, 0))] == ticks[PROBES["A"]],
    )
    checks.check(
        "letters-do-not-feed-occupancy",
        occupancy(PROBES["A"], frozenset(ticks), "+")
        == occupancy(PROBES["A"], frozenset(ticks), "-")
        == occupancy(PROBES["A"], frozenset(ticks), None)
        == 1,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9
        and all(dot(site, site) <= 9 for site in ticks)
        and "No larger host is used." in normalized_note,
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "not written into Admissibility" in normalized_note,
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
        '    "docs/NNSEED_XPROBE_SAMETICK_FORMDRAW_KERNEL_SPLIT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def occupancy(" in source
        and "def n_vector(" in source
        and "def form(" in source
        and "def formed_at_or_before(" in source
        and "def splitting_mu_star(" in source
        and "def unique_letter_from_n(" in source
        and "n_μ = (o_{+μ} − o_{−μ}) / 3" in source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
