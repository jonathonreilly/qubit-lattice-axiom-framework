#!/usr/bin/env python3
"""Exact Minkowski Gram signature of three perpnn displacements.

Four events only. Ticks are the displayed perpnn values, not a path dump.
Signature is exact rational LDL inertia, not a float eigensolve.
Displayed, not adopted. No cache or governance surface is written.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/PERPNN_FOUR_EVENT_MINKOWSKI_GRAM_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

Site = tuple[int, int, int]
Four = tuple[int, int, int, int]

ORIGIN: Site = (0, 0, 0)
AXIS: Site = (1, 0, 0)
FACE: Site = (1, 1, 0)
BODY: Site = (1, 1, 1)
RECORDED: tuple[Site, ...] = (ORIGIN, AXIS, FACE, BODY)
TICKS: dict[Site, int] = {
    ORIGIN: 0,
    AXIS: 3,
    FACE: 2,
    BODY: 3,
}
ORDER: tuple[Site, ...] = (AXIS, FACE, BODY)
UNREAD: Site = (2, 0, 0)


def four_vector(site: Site, ticks: dict[Site, int] = TICKS) -> Four:
    tick = ticks[site]
    return (tick, site[0], site[1], site[2])


def minkowski(u: Four, v: Four) -> int:
    return u[0] * v[0] - u[1] * v[1] - u[2] * v[2] - u[3] * v[3]


def gram_matrix(vectors: tuple[Four, ...]) -> list[list[int]]:
    return [[minkowski(u, v) for v in vectors] for u in vectors]


def ldl(matrix: list[list[int]]) -> tuple[list[list[Fraction]], list[Fraction]]:
    n = len(matrix)
    work = [[Fraction(matrix[i][j]) for j in range(n)] for i in range(n)]
    lower = [[Fraction(i == j) for j in range(n)] for i in range(n)]
    diag = [Fraction(0)] * n
    for j in range(n):
        pivot = work[j][j]
        for k in range(j):
            pivot -= lower[j][k] * lower[j][k] * diag[k]
        diag[j] = pivot
        if diag[j] == 0:
            for i in range(j + 1, n):
                entry = work[i][j]
                for k in range(j):
                    entry -= lower[i][k] * lower[j][k] * diag[k]
                if entry != 0:
                    raise ValueError("nonzero column under a zero pivot")
                lower[i][j] = Fraction(0)
            continue
        for i in range(j + 1, n):
            entry = work[i][j]
            for k in range(j):
                entry -= lower[i][k] * lower[j][k] * diag[k]
            lower[i][j] = entry / diag[j]
    return lower, diag


def reconstruct(lower: list[list[Fraction]], diag: list[Fraction]) -> list[list[Fraction]]:
    n = len(diag)
    return [
        [
            sum(lower[i][k] * diag[k] * lower[j][k] for k in range(n))
            for j in range(n)
        ]
        for i in range(n)
    ]


def signature_from_diag(diag: list[Fraction]) -> tuple[int, int, int]:
    if any(not isinstance(entry, Fraction) for entry in diag):
        raise TypeError("signature requires exact rationals")
    n_pos = sum(1 for entry in diag if entry > 0)
    n_neg = sum(1 for entry in diag if entry < 0)
    n_zero = sum(1 for entry in diag if entry == 0)
    return (n_pos, n_neg, n_zero)


def leading_minors(matrix: list[list[int]]) -> tuple[int, int, int]:
    a00, a01, a02 = matrix[0]
    a10, a11, a12 = matrix[1]
    a20, a21, a22 = matrix[2]
    minor1 = a00
    minor2 = a00 * a11 - a01 * a10
    minor3 = (
        a00 * (a11 * a22 - a12 * a21)
        - a01 * (a10 * a22 - a12 * a20)
        + a02 * (a10 * a21 - a11 * a20)
    )
    return (minor1, minor2, minor3)


def quadratic(site: Site) -> int:
    return site[0] * site[0] + site[1] * site[1] + site[2] * site[2]


def l1_length(site: Site) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def normalize(text: str) -> str:
    return " ".join(text.split())


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: none; R and the displayed perpnn ticks "
        "are named mathematical inputs; the product is the declared Minkowski form"
    )
    print("score_domain: recorded set R only")

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the note and current axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/PERPNN_FOUR_EVENT_MINKOWSKI_GRAM_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)),
    )
    checks.check(
        "audit-timeout",
        "the declared audit timeout is 120 seconds",
        AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "current-record-readable",
        "only records are readable and readout is content-determined",
        "Only records are readable." in axiom
        and "A readout value is determined by record content alone." in axiom_flat,
    )
    checks.check(
        "current-record-unreadability",
        "a site with no record cannot be read",
        "A site with no record cannot be read." in axiom,
    )
    checks.check(
        "current-admissibility-no-time-metric",
        "Admissibility does not define a time metric",
        "define a time metric" in axiom_flat and "It does not" in axiom,
    )

    vectors = tuple(four_vector(site) for site in ORDER)
    gram = gram_matrix(vectors)
    print("4-vectors in order (A, D, B):", vectors)
    print("G =", gram)

    expected_vectors = ((3, 1, 0, 0), (2, 1, 1, 0), (3, 1, 1, 1))
    expected_gram = [[8, 5, 8], [5, 2, 4], [8, 4, 6]]
    checks.check(
        "recorded-set-four",
        "the score domain is exactly the four named recorded events",
        RECORDED == ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1))
        and set(TICKS) == set(RECORDED)
        and UNREAD not in TICKS
        and len(RECORDED) == 4
        and four_vector(ORIGIN) == (0, 0, 0, 0),
    )
    checks.check(
        "displayed-perpnn-ticks",
        "ticks are the displayed perpnn values 0,3,2,3 and are not path-dumped",
        TICKS[ORIGIN] == 0
        and TICKS[AXIS] == 3
        and TICKS[FACE] == 2
        and TICKS[BODY] == 3
        and "not recomputed by path dump" in note_flat,
    )
    checks.check(
        "theorem1-nine-entries",
        "the nine exact Gram entries are the Minkowski products in order (A,D,B)",
        vectors == expected_vectors
        and gram == expected_gram
        and gram[0][0] == minkowski(vectors[0], vectors[0])
        and gram[0][1] == minkowski(vectors[0], vectors[1])
        and gram[0][2] == minkowski(vectors[0], vectors[2])
        and gram[1][1] == minkowski(vectors[1], vectors[1])
        and gram[1][2] == minkowski(vectors[1], vectors[2])
        and gram[2][2] == minkowski(vectors[2], vectors[2])
        and all(gram[i][j] == gram[j][i] for i in range(3) for j in range(3)),
        gram,
    )
    checks.check(
        "theorem1-diagonal-squares",
        "Gram diagonal equals t^2 minus Euclidean square on axis, face, and body",
        all(
            gram[index][index]
            == TICKS[site] * TICKS[site] - quadratic(site)
            for index, site in enumerate(ORDER)
        ),
        [gram[index][index] for index in range(3)],
    )

    lower, diag = ldl(gram)
    rebuilt = reconstruct(lower, diag)
    inertia = signature_from_diag(diag)
    minors = leading_minors(gram)
    print("LDL L =", [[str(entry) for entry in row] for row in lower])
    print("LDL D =", [str(entry) for entry in diag])
    print("signature (n+, n-, n0) =", inertia)
    print("leading principal minors =", minors)

    checks.check(
        "theorem2-ldl-reconstruction",
        "exact rational LDL reconstructs G and uses no floats",
        rebuilt == [[Fraction(gram[i][j]) for j in range(3)] for i in range(3)]
        and diag == [Fraction(8), Fraction(-9, 8), Fraction(-10, 9)]
        and lower[1][0] == Fraction(5, 8)
        and lower[2][0] == Fraction(1)
        and lower[2][1] == Fraction(8, 9)
        and all(isinstance(entry, Fraction) for entry in diag)
        and all(isinstance(entry, Fraction) for row in lower for entry in row),
        (diag, rebuilt),
    )
    checks.check(
        "theorem2-signature",
        "signature of G is (1, 2, 0) from exact LDL inertia",
        inertia == (1, 2, 0)
        and diag[0] > 0
        and diag[1] < 0
        and diag[2] < 0
        and minors == (8, -9, 10)
        and (minors[0] > 0) is True
        and (minors[1] < 0) is True
        and (minors[2] > 0) is True,
        (inertia, minors),
    )

    ambient = [
        [1, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, -1],
    ]
    ambient_inertia = signature_from_diag(ldl(ambient)[1])
    checks.check(
        "theorem3-not-opposite-or-other",
        "the signature is (1,2,0), not (2,1,0) or other",
        inertia == (1, 2, 0)
        and inertia != (2, 1, 0)
        and inertia != (0, 3, 0)
        and inertia != (1, 3, 0)
        and minors[2] != 0,
        inertia,
    )
    checks.check(
        "member-vs-3plus1",
        "the three displacements are a Lorentzian 3-member of displayed 3+1",
        ambient_inertia == (1, 3, 0)
        and inertia == (1, 2, 0)
        and minors[2] == 10
        and "Lorentzian 3-member of the displayed 3+1 product" in note_flat,
        (ambient_inertia, inertia, minors[2]),
    )

    mutated_ticks = {ORIGIN: 0, AXIS: 0, FACE: 0, BODY: 0}
    mutated_vectors = tuple(four_vector(site, mutated_ticks) for site in ORDER)
    mutated_gram = gram_matrix(mutated_vectors)
    mutated_inertia = signature_from_diag(ldl(mutated_gram)[1])
    checks.check(
        "uniqueness-not-required",
        "a mutated tick assignment can change the Gram signature",
        mutated_inertia == (0, 3, 0)
        and mutated_inertia != inertia
        and "Uniqueness of the displayed perpnn ticks is not required" in note,
        (inertia, mutated_inertia, mutated_gram),
    )
    checks.check(
        "l1-not-attached",
        "spatial quadratic is Euclidean even though L1 coincides on this R",
        all(l1_length(site) == quadratic(site) for site in RECORDED)
        and "This display does not attach L1." in note
        and "does not attach L1" in note_flat,
    )
    checks.check(
        "unread-and-four-only",
        "unread sites stay outside the four-event score domain",
        UNREAD not in RECORDED
        and UNREAD not in TICKS
        and "Four events only." in note
        and "The score domain is exactly `R`." in note,
    )

    required = (
        "**Type:** bounded_theorem",
        "actual_current_surface_status: bounded-support",
        "hypothetical_axiom_status: no edit",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "Displayed, not adopted.",
        "The note does not write a metric into Admissibility.",
        "No hop-cost is used.",
        "Clock is this displayed tick assignment.",
        "score domain is exactly `R`",
    )
    forbidden = (
        "G_N",
        "1/r",
        "1/r^2",
        "Lattice-named",
        "not a TOE",
        "Dijkstra",
        "B_57",
        "runner-cache",
    )
    checks.check(
        "note-claim-scope",
        "the note reports the displayed Minkowski Gram signature",
        'claim_scope: "Minkowski Gram signature of the three perpnn displacements from origin of axis, face, and body events is reported. Displayed, not adopted."'
        in note,
    )
    checks.check(
        "note-contract",
        "machine fields, display scope, and hygiene hold",
        all(phrase in note for phrase in required)
        and all(phrase not in note for phrase in forbidden),
        [phrase for phrase in required if phrase not in note]
        + [phrase for phrase in forbidden if phrase in note],
    )
    table_needles = (
        "`8` | `5` | `8`",
        "`5` | `2` | `4`",
        "`8` | `4` | `6`",
        "(n+, n−, n0) = (1, 2, 0)",
        "D = diag(8, −9/8, −10/9)",
    )
    checks.check(
        "note-runner-table",
        "the note table matches the computed Gram and signature",
        all(needle in note for needle in table_needles)
        and gram == expected_gram
        and inertia == (1, 2, 0),
        [needle for needle in table_needles if needle not in note],
    )

    print("per_element: each of the nine Gram entries is a Minkowski product")
    print("per_site: unread sites are excluded; only R is scored")
    print("per_mode: signature is exact rational LDL inertia, not a float spectrum")
    print("lattice_wide: checked and not executed — only four events are used")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
