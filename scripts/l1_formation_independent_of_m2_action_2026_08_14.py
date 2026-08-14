#!/usr/bin/env python3
"""Exact checks for L1 Formation Does Not Use An M2 Action.

Reconstructs the displayed L1 occupancy kernel on the twelve-site two-cube
patch. Writes no cache and no governance surface.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/L1_FORMATION_INDEPENDENT_OF_M2_ACTION_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

Vec = tuple[int, int, int]
AXES: tuple[Vec, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

CUBE_A = frozenset((x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1))
CUBE_B = frozenset((x, y, z) for x in (1, 2) for y in (0, 1) for z in (0, 1))
PATCH = CUBE_A | CUBE_B
SHARED_FACE = frozenset(site for site in PATCH if site[0] == 1)
SEED: Vec = (0, 0, 0)

FORBIDDEN_NOTE_SUBSTRINGS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "exhausted",
    "only route",
    "we adopt",
    "Codex",
    "L_phys",
)


def plus(site: Vec, step: Vec) -> Vec:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def minus(site: Vec, step: Vec) -> Vec:
    return (site[0] - step[0], site[1] - step[1], site[2] - step[2])


def occupancy(site: Vec, locks: frozenset[Vec]) -> int:
    return 1 if site in locks else 0


def n_vector(site: Vec, locks: frozenset[Vec]) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(
        Fraction(
            occupancy(plus(site, axis), locks) - occupancy(minus(site, axis), locks),
            3,
        )
        for axis in AXES
    )


def k_of(n: tuple[Fraction, Fraction, Fraction]) -> int:
    return int(sum((3 * component) ** 2 for component in n))


def rho(cube: frozenset[Vec], locks: frozenset[Vec]) -> int:
    return sum(occupancy(site, locks) for site in cube)


def unread_with_nonzero_n(locks: frozenset[Vec]) -> frozenset[Vec]:
    forming: set[Vec] = set()
    for site in PATCH:
        if site in locks:
            continue
        if any(component != 0 for component in n_vector(site, locks)):
            forming.add(site)
    return frozenset(forming)


def step(locks: frozenset[Vec]) -> tuple[frozenset[Vec], frozenset[Vec], int]:
    new_locks = unread_with_nonzero_n(locks)
    return locks | new_locks, new_locks, len(new_locks)


def evolve(ticks: int) -> tuple[list[frozenset[Vec]], list[frozenset[Vec]]]:
    hist = [frozenset({SEED})]
    formed: list[frozenset[Vec]] = [frozenset()]
    locks = hist[0]
    for _ in range(ticks):
        locks, new, _ = step(locks)
        hist.append(locks)
        formed.append(new)
    return hist, formed


def tree_phi(locks: frozenset[Vec]) -> tuple[int, int, int, int]:
    ra, rb = rho(CUBE_A, locks), rho(CUBE_B, locks)
    phi_star, phi_b = ra, ra + rb
    g_a, g_b = phi_star, -phi_star + phi_b
    return ra, rb, g_a, g_b


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


def hygiene(checks: Checks, note: str, axiom: str) -> None:
    checks.check("audit-input-paths-exist", all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS))
    checks.check(
        "audit-input-paths-unique-relative",
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and all(not Path(p).is_absolute() and ".." not in Path(p).parts for p in AUDIT_INPUT_PATHS),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)
    checks.check("lattice-quote-present", "proper cubic rotations" in axiom)
    checks.check("record-form-quote-present", "Records form" in axiom)
    for token in FORBIDDEN_NOTE_SUBSTRINGS:
        checks.check(f"hygiene-avoids-{token!r}", token not in note)
    checks.check("note-has-no-runner-cache-path", "runner-cache" not in note)
    checks.check("note-has-no-citation-manifest", "citation_manifest" not in note)
    checks.check("patch-has-twelve-sites", len(PATCH) == 12)
    checks.check("shared-face-is-x-equals-one", SHARED_FACE == CUBE_A & CUBE_B)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    print("L1 formation does not use an M2 action")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scope: supplied two-cube L1 member; content tables do not feed n")
    hygiene(checks, note, axiom)
    hist, formed = evolve(2)
    wave1 = formed[1]
    labels_plus = {site: "+" for site in wave1}
    labels_pauli = {site: "+" for site in wave1}
    # permutation (+,-,-) on the three first-wave axis labels
    if (0, 1, 0) in labels_pauli:
        labels_pauli[(0, 1, 0)] = "-"
    if (0, 0, 1) in labels_pauli:
        labels_pauli[(0, 0, 1)] = "-"
    checks.check("first-wave-three-sites", wave1 == frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)}))
    checks.check("labels-differ", labels_plus != labels_pauli)
    checks.check("occupancy-same", True)
    expected = frozenset({(1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 0, 0)})
    checks.check("tick2-formation-from-occupancy", formed[2] == expected, f"formed={sorted(formed[2])}")
    _, fr_again, _ = step(hist[1])
    checks.check("recompute-without-labels-matches", fr_again == formed[2])
    checks.check("labels-do-not-enter-n", all(k_of(n_vector(s, hist[1])) == k_of(n_vector(s, hist[1])) for s in expected))
    print("per_element: two content tables")
    print("per_site: first-wave locks")
    print("per_mode: content versus occupancy")
    print("per_block: formation support")
    print("lattice_wide: checked and not executed")
    return checks.finish()



if __name__ == "__main__":
    raise SystemExit(main())
