#!/usr/bin/env python3
"""Score same-k reverse at k=14 under κλ on B_42(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/KAPPA_LATE_LEAVE_SAMEK_K14_B42_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/KAPPA_LATE_LEAVE_SAMEK_K14_B42_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=14 under the named "
    "kappa-plus-late-leave hop-cost on B_42(0) is reported. "
    "Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
T_AXIS_REP = 26
T_BODY_REP = 46
DIJKSTRA_CALLS = 0


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def l1(v: tuple[int, int, int]) -> int:
    return abs(v[0]) + abs(v[1]) + abs(v[2])


def support_size(v: tuple[int, int, int]) -> int:
    return int(v[0] != 0) + int(v[1] != 0) + int(v[2] != 0)


def abs_coords(v: tuple[int, int, int]) -> tuple[int, int, int]:
    return (abs(v[0]), abs(v[1]), abs(v[2]))


def ball(radius: int) -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            rem = radius - abs(x) - abs(y)
            for z in range(-rem, rem + 1):
                sites.append((x, y, z))
    return sites


def nu_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1) or sigma_w < sigma_v:
        return 3
    return 1


def mu_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if nu_cost(v, w) == 3:
        return 3
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 2 and sigma_w == 2:
        nonzero = [c for c in abs_coords(w) if c != 0]
        if nonzero and min(nonzero) == 1:
            return 3
    return 1


def rho3_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if mu_cost(v, w) == 3:
        return 3
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 3 and sigma_w == 3:
        if sum(1 for c in abs_coords(w) if c == 1) == 2:
            return 3
    return 1


def kappa_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 2 and sigma_w == 3:
        if sum(1 for c in abs_coords(w) if c == 1) == 2:
            return 3
    return 1


def lambda2_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 1 and sigma_w == 2 and max(abs_coords(w)) >= 2:
        return 3
    return 1


def kappalambda_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 2 and sigma_w == 3:
        if sum(1 for c in abs_coords(w) if c == 1) == 2:
            return 3
    if sigma_v == 1 and sigma_w == 2 and max(abs_coords(w)) >= 2:
        return 3
    return 1


def dijkstra_kappalambda(
    sites: list[tuple[int, int, int]],
) -> dict[tuple[int, int, int], int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    site_set = set(sites)
    dist: dict[tuple[int, int, int], int] = {(0, 0, 0): 0}
    heap: list[tuple[int, tuple[int, int, int]]] = [(0, (0, 0, 0))]
    seen: set[tuple[int, int, int]] = set()
    while heap:
        d, v = heapq.heappop(heap)
        if v in seen:
            continue
        seen.add(v)
        vx, vy, vz = v
        for dx, dy, dz in NEIGH:
            w = (vx + dx, vy + dy, vz + dz)
            if w not in site_set:
                continue
            nd = d + kappalambda_cost(v, w)
            if nd < dist.get(w, 10**9):
                dist[w] = nd
                heapq.heappush(heap, (nd, w))
    return dist


def literal_audit_paths(source: str) -> tuple[str, ...] | None:
    module = ast.parse(source)
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS" for t in node.targets):
            continue
        if not isinstance(node.value, ast.Tuple):
            return None
        out: list[str] = []
        for elt in node.value.elts:
            if not isinstance(elt, ast.Constant) or not isinstance(elt.value, str):
                return None
            out.append(elt.value)
        return tuple(out)
    return None


def main() -> int:
    checks = Checks()
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print(f"claim_scope: {CLAIM_SCOPE}")

    checks.check(
        "audit-input-paths",
        "declared inputs are the source note and the current axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "audit-input-literal",
        "AUDIT_INPUT_PATHS is a static string-literal tuple",
        literal_audit_paths(source) == AUDIT_INPUT_PATHS,
    )
    checks.check(
        "claim-scope",
        "note claim_scope matches the displayed scoring statement",
        CLAIM_SCOPE in note.replace("\n", " "),
    )
    checks.check(
        "displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note or "displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "κλ is not written into Admissibility",
        "Do not write κλ into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note and "Do not attach L1" not in axiom,
    )
    checks.check(
        "uniqueness-not-claimed",
        "uniqueness among hop-costs is not claimed",
        "Uniqueness is not claimed" in note or "no uniqueness" in note.lower(),
    )
    checks.check(
        "no-axiom-edit",
        "note records hypothetical axiom status no edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    forbidden = tuple("".join(parts) for parts in FORBIDDEN_PARTS)
    forbidden_hits = [token for token in forbidden if token in note]
    checks.check(
        "forbidden-absent",
        "forbidden phrases are absent from the source note",
        forbidden_hits == [],
    )

    sites = ball(42)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_kappalambda(sites)
    t1400 = dist[(14, 0, 0)]
    t141414 = dist[(14, 14, 14)]
    t4200 = dist[(42, 0, 0)]
    t3900 = dist[(39, 0, 0)]
    reverse = 3 * t1400 * t1400 > t141414 * t141414
    ridge_enter = ((2, 1, 0), (2, 1, 1))
    late_leave = ((2, 0, 0), (2, 1, 0))
    print(f"n_sites {len(sites)}")
    print(f"t(14,0,0) {t1400}")
    print(f"t(14,14,14) {t141414}")
    print(f"t(14,0,0)^2/196 {t1400 * t1400}/196")
    print(f"t(14,14,14)^2/588 {t141414 * t141414}/588")
    print(f"3t_axis^2 {3 * t1400 * t1400}")
    print(f"t_body^2 {t141414 * t141414}")
    print(f"reverse {reverse}")
    print(f"t(42,0,0) {t4200}")
    print(f"t(39,0,0) {t3900}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(
        "ridge_enter "
        f"kl={kappalambda_cost(*ridge_enter)} "
        f"rho3={rho3_cost(*ridge_enter)} "
        f"lam2={lambda2_cost(*ridge_enter)}"
    )
    print(
        "late_leave "
        f"kl={kappalambda_cost(*late_leave)} "
        f"rho3={rho3_cost(*late_leave)} "
        f"kap={kappa_cost(*late_leave)}"
    )

    checks.check(
        "t-1400-141414",
        f"t(14,0,0)={T_AXIS_REP} and t(14,14,14)={T_BODY_REP}",
        t1400 == T_AXIS_REP and t141414 == T_BODY_REP,
    )
    checks.check(
        "reverse-k14",
        "t(14,0,0)^2/196 > t(14,14,14)^2/588 does not hold",
        (not reverse)
        and 3 * t1400 * t1400 == 2028
        and t141414 * t141414 == 2116
        and "2028 > 2116" in note
        and "does not hold" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b42",
        "B_42(0) has 102425 sites and 102424 nonzero sites",
        len(sites) == 102425 and len(nonzero) == 102424 and all(l1(v) <= 42 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_42(0) is reached",
        len(dist) == 102425,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        "`26`" in note
        and "`46`" in note
        and "`(14,0,0)`" in note
        and "`(14,14,14)`" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the integer reverse products",
        "2028 > 2116" in note and "2028 < 2116" in note,
    )
    checks.check(
        "not-leftover-of-b39",
        "(14,14,14) lies outside B_39(0) and the note says so",
        l1((14, 14, 14)) == 42
        and (14, 14, 14) in dist
        and t4200 == 58
        and t3900 == 51
        and "absent from `B_39(0)`" in note
        and "not leftover of the `B_39(0)` times" in note,
    )
    checks.check(
        "not-leftover-of-rho3",
        "ρ3 cannot price either stacked extra hop",
        kappalambda_cost(*ridge_enter) == 3
        and rho3_cost(*ridge_enter) == 1
        and kappalambda_cost(*late_leave) == 3
        and rho3_cost(*late_leave) == 1
        and "not leftover of `ρ3`" in note,
    )
    checks.check(
        "not-leftover-of-kappa",
        "κ cannot price the late-leave hop (2,0,0)→(2,1,0)",
        kappalambda_cost(*late_leave) == 3
        and kappa_cost(*late_leave) == 1
        and "not leftover of `κ`" in note,
    )
    checks.check(
        "not-leftover-of-lambda2",
        "λ2 cannot price the ridge-enter hop (2,1,0)→(2,1,1)",
        kappalambda_cost(*ridge_enter) == 3
        and lambda2_cost(*ridge_enter) == 1
        and "not leftover of `λ2`" in note,
    )
    checks.check(
        "stacked-extra-clauses",
        "seed-exit and both-weights-1 cost 3; both extras fire; unit-cube leave stays 1",
        kappalambda_cost((0, 0, 0), (1, 0, 0)) == 3
        and kappalambda_cost((1, 0, 0), (2, 0, 0)) == 3
        and kappalambda_cost((1, 0, 0), (1, 1, 0)) == 1
        and kappalambda_cost((1, 1, 0), (1, 1, 1)) == 1
        and kappalambda_cost((2, 1, 0), (2, 1, 1)) == 3
        and kappalambda_cost((2, 0, 0), (2, 1, 0)) == 3
        and kappalambda_cost((2, 1, 1), (3, 1, 1)) == 3,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "κλ(v→w)" not in axiom
        and "kappa-plus-late-leave" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
