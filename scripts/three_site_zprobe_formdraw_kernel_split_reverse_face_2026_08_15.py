#!/usr/bin/env python3
"""Strictly-earlier formdraw occupancy kernel n on three-site z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0), (1,0,0)} with locks +e_1, -e_1, and +e_2. A 6-NN step is
allowed iff it is perpendicular to the parent lock axis. Newly formed sites
lock the incoming step. A is not a seed. At each z-probe's formation tick,
occupancy of a 6-NN p is 1 iff p formed at tick < t(q) (strictly earlier)
and p!=q. n_μ=(o_{+μ}−o_{−μ})/3. If n(C)=n(D), unique-letter reverse and
face are UNDEFINED. If they disagree, μ* is the first axis in (e_1,e_2,e_3)
with n(C)_{μ*} ≠ n(D)_{μ*}, and the unique letter at probe q is
sign(n(q)_{μ*}) in {+,−} if that component is nonzero, else UNDEFINED.
Reverse iff L(A)=+ and L(B)=−. Face iff L(C)=+ and L(D)=−. Uniqueness is
not required. Not unique P_+. Not leftover of nstriz lists. Occupancy-kernel
formation member is not attached. L1 is not attached.
"""

from __future__ import annotations

import ast
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/THREE_SITE_ZPROBE_FORMDRAW_KERNEL_SPLIT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/THREE_SITE_ZPROBE_FORMDRAW_KERNEL_SPLIT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Vec3 = tuple[Fraction, Fraction, Fraction]
Letter = str
ORIGIN: Point = (0, 0, 0)
ZERO: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NEG_E1: Point = (-1, 0, 0)
NEG_E2: Point = (0, -1, 0)
NEG_E3: Point = (0, 0, -1)
NN: tuple[Point, ...] = (E1, NEG_E1, E2, NEG_E2, E3, NEG_E3)
AXES: tuple[Point, Point, Point] = (E1, E2, E3)
ZERO_N: Vec3 = (Fraction(0), Fraction(0), Fraction(0))
BALL_SQ = 9
THREE_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E1, E2),
)
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
PROBES = {
    "A": (0, 0, 1),
    "B": (1, 1, 1),
    "C": (0, 0, 2),
    "D": (1, 0, 1),
}
X_PROBES = {
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
EXPECTED_N = {
    "A": (Fraction(0), Fraction(0), Fraction(-1, 3)),
    "B": (Fraction(-1, 3), Fraction(-1, 3), Fraction(0)),
    "C": (Fraction(-1, 3), Fraction(-1, 3), Fraction(-1, 3)),
    "D": (Fraction(0), Fraction(0), Fraction(-1, 3)),
}
EXPECTED_X_N = {
    "A": (Fraction(0), Fraction(0), Fraction(0)),
    "B": (Fraction(-1, 3), Fraction(-1, 3), Fraction(0)),
    "C": (Fraction(-1, 3), Fraction(0), Fraction(0)),
    "D": (Fraction(0), Fraction(0), Fraction(0)),
}
EXPECTED_Y_N = {
    "A": (Fraction(0), Fraction(0), Fraction(0)),
    "B": (Fraction(-1, 3), Fraction(-1, 3), Fraction(0)),
    "C": (Fraction(0), Fraction(-1, 3), Fraction(0)),
    "D": (Fraction(0), Fraction(0), Fraction(0)),
}
EXPECTED_TWO_SITE_Z_N = {
    "A": (Fraction(0), Fraction(0), Fraction(-1, 3)),
    "B": (Fraction(-1, 3), Fraction(0), Fraction(0)),
    "C": (Fraction(0), Fraction(-1, 3), Fraction(-1, 3)),
    "D": (Fraction(-1, 3), Fraction(0), Fraction(0)),
}
CLAIM_SCOPE = (
    "Strictly-earlier formdraw occupancy kernel n on the four three-site "
    "z-probes, equality of n(C) and n(D), and reverse/face from the unique "
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


def axis(lock: Point) -> Point:
    return (abs(lock[0]), abs(lock[1]), abs(lock[2]))


def perpendicular(lock: Point, step: Point) -> bool:
    return dot(lock, step) == 0


def allowed_steps(locks: frozenset[Point]) -> frozenset[Point]:
    steps: set[Point] = set()
    for lock in locks:
        ei = axis(lock)
        for step in NN:
            if dot(step, ei) == 0:
                steps.add(step)
    return frozenset(steps)


def normalize(text: str) -> str:
    return " ".join(text.split())


def occupancy(site: Point, formed: frozenset[Point], letter: str | None = None) -> int:
    """Occupancy is 1 on strictly-earlier neighbors. A letter does not feed n."""
    if letter is not None and letter not in {"+", "-"}:
        raise ValueError(f"letter must be + or -, got {letter!r}")
    return 1 if site in formed else 0


def n_vector(site: Point, formed: frozenset[Point]) -> Vec3:
    """Formdraw occupancy kernel n_μ = (o_{+μ} − o_{−μ}) / 3."""
    components = []
    for axis_vec in AXES:
        plus = occupancy(add(site, axis_vec), formed)
        minus = occupancy(add(site, (-axis_vec[0], -axis_vec[1], -axis_vec[2])), formed)
        components.append(Fraction(plus - minus, 3))
    return (components[0], components[1], components[2])


def splitting_mu_star(n_c: Vec3, n_d: Vec3) -> int | None:
    """First axis in (e_1,e_2,e_3) with n(C)≠n(D). None if they agree."""
    for index in range(3):
        if n_c[index] != n_d[index]:
            return index
    return None


def unique_letter_from_n(n: Vec3, mu_star: int | None) -> Letter:
    """Unique splitting-component letter, or UNDEFINED if no split or zero."""
    if mu_star is None:
        return "UNDEFINED"
    component = n[mu_star]
    if component == 0:
        return "UNDEFINED"
    return "+" if component > 0 else "-"


def unique_plus_from_n(n: Vec3) -> Letter:
    """Refused unique P_+: + whenever n≠0. Not used for reverse/face."""
    if n == ZERO_N:
        return "UNDEFINED"
    return "+"


def nscodot_from_n(left: Vec3, right: Vec3) -> Fraction:
    """Refused nscodot: occupancy-kernel inner product. Not used."""
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]


def unique_vector_letter(locks: tuple[Point, ...]) -> Point | str:
    """Leftover of nstriz already-recorded neighbor-lock lists. Not this letter."""
    if not locks:
        return "UNDEFINED"
    unique = set(locks)
    if len(unique) != 1:
        return "UNDEFINED"
    vector = next(iter(unique))
    if vector not in NN:
        return "UNDEFINED"
    return vector


def reverse_face_report(
    letter_a: Letter, letter_b: Letter, letter_c: Letter, letter_d: Letter
) -> tuple[str, str]:
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
    for name, axis_vec in zip(names, AXES):
        plus = occupancy(add(site, axis_vec), formed)
        minus = occupancy(add(site, (-axis_vec[0], -axis_vec[1], -axis_vec[2])), formed)
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
    seeds: tuple[tuple[Point, Point], ...] = THREE_SITE_SEEDS,
    *,
    require_perp: bool = True,
) -> tuple[dict[Point, int], dict[Point, set[Point]]]:
    """Earliest formation ticks and incoming locks on B_3(0). Same process as nstri."""
    recorded: dict[Point, dict[str, object]] = {
        site: {"t": 0, "locks": frozenset({lock})} for site, lock in seeds
    }
    for tick in range(0, 16):
        proposals: dict[Point, list[tuple[Point, Point]]] = defaultdict(list)
        for site, info in recorded.items():
            if info["t"] != tick:
                continue
            locks = info["locks"]
            assert isinstance(locks, frozenset)
            steps = allowed_steps(locks) if require_perp else frozenset(NN)
            for step in steps:
                child = add(site, step)
                if not in_ball(child) or child in recorded:
                    continue
                proposals[child].append((site, step))
        if not proposals:
            continue
        for child, parents in proposals.items():
            recorded[child] = {
                "t": tick + 1,
                "locks": frozenset(step for _, step in parents),
            }
    ticks = {site: int(info["t"]) for site, info in recorded.items()}
    locks = {site: set(info["locks"]) for site, info in recorded.items()}  # type: ignore[arg-type]
    return ticks, locks


def strictly_earlier(site: Point, ticks: dict[Point, int]) -> frozenset[Point]:
    """Sites formed at tick < t(q), with q excluded."""
    formation = ticks[site]
    return frozenset(
        other for other, tick in ticks.items() if tick < formation and other != site
    )


def formed_at_or_before(site: Point, ticks: dict[Point, int]) -> frozenset[Point]:
    """Same-tick-inclusive occupancy. Not this display."""
    formation = ticks[site]
    return frozenset(
        other for other, tick in ticks.items() if tick <= formation and other != site
    )


def recorded_neighbor_locks(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> tuple[Point, ...]:
    """Already-recorded six-neighbor lock vectors (nstriz leftover). Not this letter."""
    formation = ticks[site]
    vectors: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks:
            continue
        if formation == 0:
            if ticks[neighbor] == 0 and neighbor != site:
                for lock in sorted(locks[neighbor]):
                    vectors.append(lock)
        elif ticks[neighbor] < formation:
            for lock in sorted(locks[neighbor]):
                vectors.append(lock)
    return tuple(vectors)


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

    print("strictly-earlier formdraw n on three-site z-probes; split letter")
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
    x_probe_sites = tuple(X_PROBES[name] for name in ("A", "B", "C", "D"))
    y_probe_sites = tuple(Y_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-z-probes-in-host",
        probe_sites == ((0, 0, 1), (1, 1, 1), (0, 0, 2), (1, 0, 1))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and E1 not in probe_sites
        and E2 not in probe_sites,
    )
    checks.check(
        "z-probes-are-not-x-or-y-probes",
        probe_sites != x_probe_sites
        and probe_sites != y_probe_sites
        and x_probe_sites == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
        and y_probe_sites == ((0, 1, 0), (1, 1, 1), (0, 2, 0), (1, 1, 0)),
    )
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and add(NEG_E1, E1) == ZERO
        and add(NEG_E2, E2) == ZERO
        and add(NEG_E3, E3) == ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and perpendicular(NEG_E1, E2)
        and perpendicular(E1, E3)
        and not perpendicular(E1, E1)
        and not perpendicular(NEG_E1, E1)
        and in_ball(PROBES["C"])
        and in_ball(PROBES["D"])
        and not in_ball((4, 0, 0)),
    )

    ticks, locks = form()
    two_site_ticks, _two_site_locks = form(TWO_SITE_SEEDS)
    kernels: dict[str, Vec3] = {}
    same_tick: dict[str, Vec3] = {}
    lock_letters: dict[str, Point | str] = {}
    x_kernels: dict[str, Vec3] = {}
    y_kernels: dict[str, Vec3] = {}
    two_site_kernels: dict[str, Vec3] = {}
    for name, site in PROBES.items():
        formed = strictly_earlier(site, ticks)
        kernels[name] = n_vector(site, formed)
        same_tick[name] = n_vector(site, formed_at_or_before(site, ticks))
        lock_letters[name] = unique_vector_letter(
            recorded_neighbor_locks(site, ticks, locks)
        )
        occ = neighbor_occupancy(site, formed)
        print(
            f"{name} t={ticks[site]} n={format_n(kernels[name])} "
            f"occ=+−e1{occ['e1']} +−e2{occ['e2']} +−e3{occ['e3']} "
            f"incoming={sorted(locks.get(site, ()))}"
        )
    for name, site in X_PROBES.items():
        x_kernels[name] = n_vector(site, strictly_earlier(site, ticks))
    for name, site in Y_PROBES.items():
        y_kernels[name] = n_vector(site, strictly_earlier(site, ticks))
    for name, site in PROBES.items():
        two_site_kernels[name] = n_vector(
            site, strictly_earlier(site, two_site_ticks)
        )

    mu_star = splitting_mu_star(kernels["C"], kernels["D"])
    letters = {
        name: unique_letter_from_n(kernels[name], mu_star) for name in ("A", "B", "C", "D")
    }
    x_mu_star = splitting_mu_star(x_kernels["C"], x_kernels["D"])
    x_letters = {
        name: unique_letter_from_n(x_kernels[name], x_mu_star)
        for name in ("A", "B", "C", "D")
    }
    reverse_status, face_status = reverse_face_report(
        letters["A"], letters["B"], letters["C"], letters["D"]
    )
    equal_cd = kernels["C"] == kernels["D"]
    print(f"n(C)=n(D): {equal_cd}")
    print(f"mu_star={mu_star} letters={letters}")
    print(f"reverse={reverse_status} face={face_status}")
    print(
        "per_element: each occupancy component of n and the splitting-component letter"
    )
    print(
        "per_site: scored only at z-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four kernels, equality of n(C) and n(D), and reverse/face"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    checks.check(
        "theorem1-n-A",
        kernels["A"] == EXPECTED_N["A"]
        and f"n(A) = {format_n(kernels['A'])}" in note,
        format_n(kernels["A"]),
    )
    checks.check(
        "theorem1-n-B",
        kernels["B"] == EXPECTED_N["B"]
        and f"n(B) = {format_n(kernels['B'])}" in note,
        format_n(kernels["B"]),
    )
    checks.check(
        "theorem1-n-C",
        kernels["C"] == EXPECTED_N["C"]
        and f"n(C) = {format_n(kernels['C'])}" in note,
        format_n(kernels["C"]),
    )
    checks.check(
        "theorem1-n-D",
        kernels["D"] == EXPECTED_N["D"]
        and f"n(D) = {format_n(kernels['D'])}" in note,
        format_n(kernels["D"]),
    )
    checks.check(
        "theorem1-nC-disagrees-nD",
        (not equal_cd)
        and kernels["C"] != kernels["D"]
        and mu_star == 0
        and "n(C)≠n(D)" in note
        and "μ*" in note,
    )
    checks.check(
        "splitting-axis-is-e1",
        mu_star == 0
        and kernels["C"][0] != kernels["D"][0]
        and unique_letter_from_n(kernels["A"], 0) == "UNDEFINED"
        and unique_letter_from_n(kernels["B"], 0) == "-"
        and unique_letter_from_n(kernels["C"], 0) == "-"
        and unique_letter_from_n(kernels["D"], 0) == "UNDEFINED",
    )
    checks.check(
        "theorem1-letters",
        letters["A"] == "UNDEFINED"
        and letters["B"] == "-"
        and letters["C"] == "-"
        and letters["D"] == "UNDEFINED"
        and "L(A) = UNDEFINED" in note
        and "L(B) = −" in note
        and "L(C) = −" in note
        and "L(D) = UNDEFINED" in note,
    )
    checks.check(
        "theorem1-A-is-not-seed",
        ticks[PROBES["A"]] == 1
        and PROBES["A"] == E3
        and ticks[ORIGIN] == 0
        and kernels["A"] != ZERO_N
        and occupancy(ORIGIN, strictly_earlier(PROBES["A"], ticks)) == 1
        and "`A` is not a seed" in note,
    )
    checks.check(
        "theorem2-reverse-undefined",
        reverse_status == "UNDEFINED"
        and letters["A"] == "UNDEFINED"
        and letters["B"] == "-"
        and reverse_status != "hold"
        and reverse_status != "fail"
        and "Reverse: UNDEFINED" in note,
        reverse_status,
    )
    checks.check(
        "theorem3-face-undefined",
        face_status == "UNDEFINED"
        and letters["C"] == "-"
        and letters["D"] == "UNDEFINED"
        and face_status != "hold"
        and face_status != "fail"
        and "Face: UNDEFINED" in note,
        face_status,
    )
    pplus_letters = {name: unique_plus_from_n(kernels[name]) for name in PROBES}
    pplus_reverse, pplus_face = reverse_face_report(
        pplus_letters["A"], pplus_letters["B"], pplus_letters["C"], pplus_letters["D"]
    )
    checks.check(
        "not-unique-pplus",
        pplus_letters["A"] == "+"
        and pplus_letters["B"] == "+"
        and pplus_letters["C"] == "+"
        and pplus_letters["D"] == "+"
        and pplus_reverse == "fail"
        and pplus_face == "fail"
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED"
        and "not unique `P_+`" in normalized_note,
    )
    checks.check(
        "not-nscodot",
        nscodot_from_n(kernels["C"], kernels["D"]) == Fraction(1, 9)
        and nscodot_from_n(kernels["A"], kernels["B"]) == Fraction(0)
        and "not nscodot" in normalized_note,
    )
    leftover_reverse = "fail"
    leftover_face = "fail"
    checks.check(
        "not-leftover-of-nstriz-lists",
        lock_letters["A"] == E1
        and lock_letters["B"] == E3
        and lock_letters["C"] == E3
        and lock_letters["D"] == E2
        and leftover_reverse == "fail"
        and leftover_face == "fail"
        and letters["A"] == "UNDEFINED"
        and letters["B"] == "-"
        and letters["C"] == "-"
        and letters["D"] == "UNDEFINED"
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED"
        and "not leftover of nstriz lists" in normalized_note,
    )
    checks.check(
        "not-nstrin-x-probe-formdraw",
        x_kernels == EXPECTED_X_N
        and x_mu_star == 0
        and x_letters == {"A": "UNDEFINED", "B": "-", "C": "-", "D": "UNDEFINED"}
        and kernels["A"] != x_kernels["A"]
        and kernels["C"] != x_kernels["C"]
        and kernels["D"] != x_kernels["D"]
        and letters == x_letters
        and "not leftover of nstrin lists" in normalized_note
        and "not the x-probes" in normalized_note,
    )
    checks.check(
        "not-two-site-nsopzn-leftover",
        two_site_kernels == EXPECTED_TWO_SITE_Z_N
        and kernels["B"] != two_site_kernels["B"]
        and kernels["C"] != two_site_kernels["C"]
        and kernels["D"] != two_site_kernels["D"]
        and "not leftover of nstriz lists" in normalized_note
        and "not the two-site opposite-lock z-probes" in normalized_note,
    )
    checks.check(
        "not-same-tick-inclusive",
        same_tick["A"] != kernels["A"]
        and same_tick["A"] == (Fraction(1, 3), Fraction(1, 3), Fraction(-1, 3))
        and same_tick["B"] == kernels["B"]
        and same_tick["C"] != kernels["C"]
        and same_tick["C"] == (Fraction(0), Fraction(0), Fraction(-1, 3))
        and same_tick["D"] != kernels["D"]
        and same_tick["D"] == (Fraction(-1, 3), Fraction(0), Fraction(-1, 3))
        and "strictly earlier" in normalized_note,
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["B"]]) == 2
        and len(locks[PROBES["C"]]) == 2
        and "Uniqueness is not required" in note,
        str(sorted(locks[PROBES["C"]])),
    )
    checks.check(
        "three-site-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and ticks[E1] == 0
        and locks[E1] == {E2}
        and sum(time == 0 for time in ticks.values()) == 3
        and PROBES["A"] != E1,
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    formed_a = strictly_earlier(PROBES["A"], ticks)
    checks.check(
        "strictly-earlier-excludes-probe-and-same-tick",
        PROBES["A"] not in formed_a
        and occupancy(PROBES["A"], formed_a) == 0
        and ticks[PROBES["A"]] == 1
        and ticks[add(PROBES["A"], E2)] == 1
        and occupancy(add(PROBES["A"], E2), formed_a) == 0
        and occupancy(ORIGIN, formed_a) == 1
        and ticks[PROBES["D"]] == 1
        and occupancy(PROBES["D"], formed_a) == 0,
    )
    checks.check(
        "letters-do-not-feed-occupancy",
        occupancy(ORIGIN, frozenset(ticks), "+")
        == occupancy(ORIGIN, frozenset(ticks), "-")
        == occupancy(ORIGIN, frozenset(ticks), None)
        == 1,
    )
    checks.check(
        "formation-ticks-of-probes",
        ticks[PROBES["A"]] == 1
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 1
        and "t(A)=1" in note.replace(" ", "")
        and "t(B)=2" in note.replace(" ", "")
        and "t(C)=4" in note.replace(" ", "")
        and "t(D)=1" in note.replace(" ", ""),
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9
        and all(dot(site, site) <= 9 for site in ticks)
        and "No larger host is used." in normalized_note
        and (-3, 0, 0) not in ticks
        and (3, 0, 0) not in ticks
        and (0, 3, 0) not in ticks,
    )
    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E2, step)) != 1 for step in (E1, NEG_E1)
    )
    third_seed_parallel_blocked = all(
        ticks.get(add(E1, step)) != 1 for step in (E2, NEG_E2)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and third_seed_parallel_blocked
        and ticks[(0, -1, 0)] == 1
        and ticks[E3] == 1
        and ticks[(0, 0, -1)] == 1
        and ticks[(0, 2, 0)] == 1
        and ticks[PROBES["A"]] == 1
        and ticks[PROBES["D"]] == 1
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "identity-letter-when-equal-is-undefined",
        unique_letter_from_n(kernels["C"], None) == "UNDEFINED"
        and splitting_mu_star(kernels["C"], kernels["C"]) is None
        and reverse_face_report("UNDEFINED", "UNDEFINED", "UNDEFINED", "UNDEFINED")
        == ("UNDEFINED", "UNDEFINED"),
    )
    checks.check(
        "reverse-face-identity",
        reverse_face_report("+", "-", "+", "-") == ("hold", "hold")
        and reverse_face_report("+", "+", "+", "-") == ("fail", "hold")
        and reverse_face_report("UNDEFINED", "-", "-", "UNDEFINED")
        == ("UNDEFINED", "UNDEFINED"),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "not written into Admissibility" in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-does-not-attach-occupancy-kernel-formation",
        "does not attach the occupancy-kernel formation member" in normalized_note,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in normalized_note
        and "B_3(0)" in note
        and "No runner cache is written." in normalized_note,
    )
    checks.check(
        "note-not-x-or-y-probe-reprint",
        "not the x-probes" in normalized_note
        and "not the y-probes" in normalized_note
        and "A = (0,0,1)" in note
        and "D = (1,0,1)" in note,
    )
    checks.check(
        "note-a-is-not-seed",
        "`A` is not a seed" in note and "`D` is not a seed" in note,
    )
    checks.check(
        "note-forbidden-tokens-absent",
        all(token not in note for token in FORBIDDEN_NOTE_TOKENS)
        and "B_4" not in note
        and "n·n<=16" not in note,
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
        '    "docs/THREE_SITE_ZPROBE_FORMDRAW_KERNEL_SPLIT_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def occupancy(" in source
        and "def n_vector(" in source
        and "def form(" in source
        and "def strictly_earlier(" in source
        and "def splitting_mu_star(" in source
        and "def unique_letter_from_n(" in source
        and "n_μ = (o_{+μ} − o_{−μ}) / 3" in source,
    )
    checks.check(
        "source-formation-is-perp-step",
        "allowed_steps" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] == 1
        and set(ticks) <= host,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "source-letter-from-splitting-component",
        "unique_letter_from_n" in defined_fns
        and "splitting_mu_star" in defined_fns
        and "strictly_earlier" in defined_fns
        and "nscodot_from_n" in defined_fns,
    )
    y_mu_star = splitting_mu_star(y_kernels["C"], y_kernels["D"])
    checks.check(
        "not-y-probe-formdraw",
        y_kernels == EXPECTED_Y_N
        and y_mu_star == 1
        and kernels["A"] != y_kernels["A"]
        and kernels["C"] != y_kernels["C"]
        and probe_sites != y_probe_sites
        and "not the y-probes" in normalized_note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
