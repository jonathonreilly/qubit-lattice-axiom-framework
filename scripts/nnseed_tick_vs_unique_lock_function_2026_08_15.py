#!/usr/bin/env python3
"""Whether formation-tick is a function of unique lock on nnseed B_3(0).

Same perp-step incoming-lock process as the two-site seed on Euclidean B_3(0):
seed {0,(0,1,0)} with locks +e_1 and +e_2, a 6-NN step is allowed iff it is
perpendicular to the parent lock axis, and a newly formed site locks the
incoming step. Host is {n : n·n <= 9}. Uniqueness is not required of the
process. The domain is the unique-lock formed sites, including both seeds,
and the question is whether t is a function of the unique letter L.
"""

from __future__ import annotations

import ast
from collections import defaultdict, deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/NNSEED_TICK_VS_UNIQUE_LOCK_FUNCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NNSEED_TICK_VS_UNIQUE_LOCK_FUNCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
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
LETTER_NAME = {
    E1: "+e_1",
    (-1, 0, 0): "-e_1",
    E2: "+e_2",
    (0, -1, 0): "-e_2",
    E3: "+e_3",
    (0, 0, -1): "-e_3",
}
BALL_SQ = 9
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
ONE_SITE_SEEDS: tuple[tuple[Point, Point], ...] = ((ORIGIN, E1),)
FORBIDDEN_NOTE_TOKENS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "L1",
    "hop-cost",
    "B_57",
    "Runner cache",
    "s^2",
    "Gram",
    "|x|_1",
    "parnn",
    "k20",
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


def fmt_site(site: Point) -> str:
    return f"({site[0]},{site[1]},{site[2]})"


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
    """Earliest formation ticks and possible incoming locks on B_3(0)."""
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


def unique_letter(locks: dict[Point, set[Point]], site: Point) -> Point | None:
    letters = locks.get(site)
    if letters is None or len(letters) != 1:
        return None
    return next(iter(letters))


def unique_map_of(
    ticks: dict[Point, int], locks: dict[Point, set[Point]]
) -> dict[Point, tuple[Point, int]]:
    unique_map: dict[Point, tuple[Point, int]] = {}
    for site in ticks:
        letter = unique_letter(locks, site)
        if letter is None:
            continue
        unique_map[site] = (letter, ticks[site])
    return unique_map


def first_witness(
    unique_map: dict[Point, tuple[Point, int]],
) -> tuple[Point, Point, Point, int, int] | None:
    """Lexicographically first x<y with L(x)=L(y) and t(x)!=t(y)."""
    by_letter: dict[Point, list[Point]] = defaultdict(list)
    for site, (letter, _tick) in unique_map.items():
        by_letter[letter].append(site)
    candidates: list[tuple[Point, Point, Point, int, int]] = []
    for letter, sites in by_letter.items():
        ordered = sorted(sites)
        for i, left in enumerate(ordered):
            t_left = unique_map[left][1]
            for right in ordered[i + 1 :]:
                t_right = unique_map[right][1]
                if t_left != t_right:
                    candidates.append((left, right, letter, t_left, t_right))
    if not candidates:
        return None
    return min(candidates, key=lambda item: (item[0], item[1]))


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
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    claim_scope = (
        "Whether formation-tick is a function of unique earliest incoming "
        "lock on the nnseed unique-lock sites of B_3(0) is reported. "
        "Displayed, not adopted."
    )

    print("nnseed tick vs unique-lock function on Euclidean B_3(0)")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"claim_scope: {claim_scope}")

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
    ticks, locks = form()
    unique_map = unique_map_of(ticks, locks)

    by_letter: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    for site, (letter, tick) in unique_map.items():
        by_letter[letter].append((site, tick))
    for letter in by_letter:
        by_letter[letter].sort()

    t_is_function = all(
        len({tick for _site, tick in items}) == 1 for items in by_letter.values()
    )
    seed_sites = {ORIGIN, E2}
    seed_excluded = {
        site: pair for site, pair in unique_map.items() if site not in seed_sites
    }
    by_letter_ex: dict[Point, set[int]] = defaultdict(set)
    for _site, (letter, tick) in seed_excluded.items():
        by_letter_ex[letter].add(tick)
    t_is_function_ex_seed = all(
        len(tick_set) == 1 for tick_set in by_letter_ex.values()
    )
    witness = first_witness(unique_map)
    displayed = ((0, 1, 0), (0, 3, 0), E2, 0, 4)

    one_ticks, one_locks = form(seeds=ONE_SITE_SEEDS)
    one_unique = unique_map_of(one_ticks, one_locks)

    print(f"host={len(host)} formed={len(ticks)} unique_lock_sites={len(unique_map)}")
    print(
        "letter_counts: "
        + ", ".join(
            f"{LETTER_NAME[letter]}={len(by_letter.get(letter, ()))}"
            for letter in NN
        )
    )
    if witness is None:
        print("t_is_function_of_L=yes")
        print("witness=none")
    else:
        left, right, letter, t_left, t_right = witness
        print("t_is_function_of_L=no")
        print(
            "witness "
            f"{fmt_site(left)} {LETTER_NAME[letter]} t={t_left}; "
            f"{fmt_site(right)} {LETTER_NAME[letter]} t={t_right}"
        )
    print(
        "displayed_witness "
        f"{fmt_site(displayed[0])} {LETTER_NAME[displayed[2]]} t={displayed[3]}; "
        f"{fmt_site(displayed[1])} {LETTER_NAME[displayed[2]]} t={displayed[4]}"
    )
    print(f"locks(1,1,1)={sorted(locks.get((1, 1, 1), ()))}")

    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "host-is-euclidean-includes-nn8-site",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8,
    )
    checks.check(
        "theorem1-unique-lock-set-includes-both-seeds",
        ORIGIN in unique_map
        and unique_map[ORIGIN] == (E1, 0)
        and E2 in unique_map
        and unique_map[E2] == (E2, 0)
        and len(unique_map) == 61,
        f"N={len(unique_map)} origin={unique_map.get(ORIGIN)} e2={unique_map.get(E2)}",
    )
    checks.check(
        "theorem1-map-letters-are-unit-steps",
        all(letter in LETTER_NAME and letter in NN for letter, _tick in unique_map.values()),
    )
    checks.check(
        "theorem1-uniqueness-not-required",
        (1, 1, 1) in ticks
        and (1, 1, 1) not in unique_map
        and len(locks[(1, 1, 1)]) == 2
        and locks[(1, 1, 1)] == {E1, E3},
        str(sorted(locks.get((1, 1, 1), ()))),
    )
    checks.check(
        "theorem1-euclidean-corner-is-unique-lock",
        unique_map.get((2, 2, 0)) == (E1, 3),
        str(unique_map.get((2, 2, 0))),
    )
    checks.check(
        "theorem2-t-is-not-a-function-of-L",
        not t_is_function and witness is not None,
        "function" if t_is_function else "not-function",
    )
    checks.check(
        "theorem2-witness-pair-same-letter-different-tick",
        witness is not None
        and unique_map[witness[0]][0] == unique_map[witness[1]][0] == witness[2]
        and unique_map[witness[0]][1] == witness[3]
        and unique_map[witness[1]][1] == witness[4]
        and witness[0] != witness[1]
        and witness[3] != witness[4],
        str(witness),
    )
    checks.check(
        "theorem2-displayed-witness-010-030",
        unique_map.get((0, 1, 0)) == (E2, 0)
        and unique_map.get((0, 3, 0)) == (E2, 4),
        f"{unique_map.get((0, 1, 0))} vs {unique_map.get((0, 3, 0))}",
    )
    checks.check(
        "theorem2-not-an-artifact-of-including-seeds",
        not t_is_function_ex_seed
        and {2, 4} <= by_letter_ex[E2],
    )
    checks.check(
        "cardinality-not-one-site-clone",
        len(one_unique) == 51
        and len(unique_map) != len(one_unique)
        and unique_map != one_unique,
        f"two={len(unique_map)} one={len(one_unique)}",
    )
    checks.check(
        "seed-ticks-and-locks",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {E2}
        and perpendicular(E1, E2),
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check("formation-uses-earliest-tick-queue", "queue.popleft()" in source)
    checks.check(
        "source-host-is-euclidean-dot",
        "dot(site, site) <= BALL_SQ" in source
        and "BALL_SQ = 9" in source
        and "in_ball" in source,
    )

    map_entries_in_note = all(
        f"{fmt_site(site)}:{tick}" in note for site, (_letter, tick) in unique_map.items()
    )
    checks.check("note-claim-scope", claim_scope in note)
    checks.check(
        "note-reports-unique-map",
        "unique-lock sites N=61" in note and map_entries_in_note,
    )
    checks.check(
        "note-reports-witness",
        "x=(0,1,0)" in note
        and "y=(0,3,0)" in note
        and "L(x)=L(y)=+e_2" in note
        and "t(x)=0" in note
        and "t(y)=4" in note
        and "t is not a function of L" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in note.lower()
        and "not written into Admissibility" in note
        and "Do not write t or L into Admissibility." in note,
    )
    checks.check(
        "note-content-alone-consequence",
        "formation-tick cannot be recovered from Record content-alone" in note
        and "A readout value is determined by record content" in axiom,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in note
        and "B_3(0)" in note
        and "n·n <= 9" in note
        and "No runner cache is written." in note,
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
        and "A readout value is determined by record content" in axiom,
    )
    checks.check(
        "note-machine-status-no-axiom-edit",
        "hypothetical_axiom_status: no edit" in note
        and "claim_type: bounded_theorem" in note,
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/NNSEED_TICK_VS_UNIQUE_LOCK_FUNCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
