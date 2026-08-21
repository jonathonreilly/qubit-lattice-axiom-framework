#!/usr/bin/env python3
"""Exact Minkowski Gram signature of three nnseed four-event displacements.

Displayed ticks only. Four events only. Exact rationals. No path dump,
no cache write, no axiom edit, no network.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "NNSEED_FOUR_EVENT_MINKOWSKI_GRAM_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/NNSEED_FOUR_EVENT_MINKOWSKI_GRAM_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Vec4 = tuple[int, int, int, int]
Matrix3 = tuple[tuple[Fraction, ...], ...]

N5_LINES = (
    "per_element: all nine Gram entries and all three LDL pivots are evaluated as exact rationals",
    "per_site: only the four named events O, A, D, B enter; the extra seed (0,1,0) is excluded from the Gram",
    "per_mode: Minkowski versus Euclidean products are both computed; only the Minkowski product is the claim",
    "per_block: the 3x3 Gram block of (u(A),u(D),u(B)) is the sole signature carrier",
    "lattice_wide: checked and not executed — no lattice-wide metric, formation growth, or Admissibility rewrite is claimed",
)

FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE", "Dijkstra")


def normalize(text: str) -> str:
    return " ".join(text.split())


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def as_frac(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def minkowski(left: Vec4, right: Vec4) -> Fraction:
    return as_frac(
        left[0] * right[0]
        - left[1] * right[1]
        - left[2] * right[2]
        - left[3] * right[3]
    )


def euclidean(left: Vec4, right: Vec4) -> Fraction:
    return as_frac(sum(left[index] * right[index] for index in range(4)))


def gram(vectors: tuple[Vec4, Vec4, Vec4], product) -> Matrix3:
    return tuple(
        tuple(product(vectors[row], vectors[col]) for col in range(3))
        for row in range(3)
    )


def matmul(left: Matrix3, right: Matrix3) -> Matrix3:
    return tuple(
        tuple(
            sum((left[row][mid] * right[mid][col] for mid in range(3)), Fraction(0))
            for col in range(3)
        )
        for row in range(3)
    )


def transpose(matrix: Matrix3) -> Matrix3:
    return tuple(tuple(matrix[row][col] for row in range(3)) for col in range(3))


def diagonal(entries: tuple[Fraction, Fraction, Fraction]) -> Matrix3:
    return tuple(
        tuple(entries[row] if row == col else Fraction(0) for col in range(3))
        for row in range(3)
    )


def ldl(matrix: Matrix3) -> tuple[Matrix3, tuple[Fraction, Fraction, Fraction]]:
    work = [[as_frac(matrix[row][col]) for col in range(3)] for row in range(3)]
    lower = [[Fraction(row == col) for col in range(3)] for row in range(3)]
    pivots = [Fraction(0), Fraction(0), Fraction(0)]
    for col in range(3):
        acc = work[col][col]
        for prior in range(col):
            acc -= lower[col][prior] * lower[col][prior] * pivots[prior]
        pivots[col] = acc
        if pivots[col] == 0:
            for row in range(col + 1, 3):
                remainder = work[row][col]
                for prior in range(col):
                    remainder -= lower[row][prior] * lower[col][prior] * pivots[prior]
                if remainder != 0:
                    raise ValueError("zero pivot with nonzero Schur remainder")
                lower[row][col] = Fraction(0)
            continue
        for row in range(col + 1, 3):
            acc = work[row][col]
            for prior in range(col):
                acc -= lower[row][prior] * lower[col][prior] * pivots[prior]
            lower[row][col] = acc / pivots[col]
    lower_t = tuple(tuple(row) for row in lower)
    return lower_t, (pivots[0], pivots[1], pivots[2])


def signature(pivots: tuple[Fraction, Fraction, Fraction]) -> tuple[int, int, int]:
    n_plus = sum(1 for pivot in pivots if pivot > 0)
    n_minus = sum(1 for pivot in pivots if pivot < 0)
    n_zero = sum(1 for pivot in pivots if pivot == 0)
    return (n_plus, n_minus, n_zero)


def det3(matrix: Matrix3) -> Fraction:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def four_vector(tick: int, site: tuple[int, int, int]) -> Vec4:
    return (tick, site[0], site[1], site[2])


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: displayed nnseed ticks and the gram4 "
        "signature comparison triple; no fitted, observational, or literature values"
    )
    print("measure_boundary: exact integer and rational 3x3 linear algebra only")

    origin = (0, 0, 0)
    axis = (1, 0, 0)
    face = (1, 1, 0)
    body = (1, 1, 1)
    extra_seed = (0, 1, 0)
    sites = (axis, face, body)
    ticks = (2, 1, 2)
    vectors = tuple(four_vector(tick, site) for tick, site in zip(ticks, sites))

    minkowski_g = gram(vectors, minkowski)
    lower, pivots = ldl(minkowski_g)
    reconstructed = matmul(matmul(lower, diagonal(pivots)), transpose(lower))
    leading = (
        minkowski_g[0][0],
        minkowski_g[0][0] * minkowski_g[1][1] - minkowski_g[0][1] * minkowski_g[1][0],
        det3(minkowski_g),
    )
    signs = []
    previous = Fraction(1)
    for minor in leading:
        if previous == 0 or minor == 0:
            signs.append("zero")
        elif previous * minor < 0:
            signs.append("change")
        else:
            signs.append("same")
        previous = minor

    seed_ticks = (3, 2, 3)
    seed_vectors = tuple(four_vector(tick, site) for tick, site in zip(seed_ticks, sites))
    seed_g = gram(seed_vectors, minkowski)
    seed_lower, seed_pivots = ldl(seed_g)

    euclid_g = gram(vectors, euclidean)
    euclid_lower, euclid_pivots = ldl(euclid_g)

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required static string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/NNSEED_FOUR_EVENT_MINKOWSKI_GRAM_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "audit-input-paths-source",
        "the tuple is a static literal in this file",
        (
            "AUDIT_INPUT_PATHS = (\n"
            '    "docs/NNSEED_FOUR_EVENT_MINKOWSKI_GRAM_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
            '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
            ")"
        )
        in source,
    )
    checks.check(
        "four-events-only",
        "the Gram vectors are exactly axis, face, and body from the origin",
        sites == ((1, 0, 0), (1, 1, 0), (1, 1, 1))
        and origin == (0, 0, 0)
        and extra_seed not in sites
        and extra_seed != origin,
    )
    checks.check(
        "displayed-nnseed-ticks",
        "ticks are the displayed nnseed list (2,1,2), not a path dump",
        ticks == (2, 1, 2)
        and vectors
        == (
            (2, 1, 0, 0),
            (1, 1, 1, 0),
            (2, 1, 1, 1),
        )
        and "not recomputed by a path dump" in normalized_note,
    )
    checks.check(
        "gram-entries",
        "the nine Minkowski Gram entries are exactly Theorem 1",
        minkowski_g
        == (
            (Fraction(3), Fraction(1), Fraction(3)),
            (Fraction(1), Fraction(-1), Fraction(0)),
            (Fraction(3), Fraction(0), Fraction(1)),
        )
        and minkowski_g[0][1] == minkowski_g[1][0]
        and minkowski_g[0][2] == minkowski_g[2][0]
        and minkowski_g[1][2] == minkowski_g[2][1],
    )
    checks.check(
        "ldl-reconstruction",
        "exact rational LDL reconstructs G",
        reconstructed == minkowski_g
        and pivots == (Fraction(3), Fraction(-4, 3), Fraction(-5, 4))
        and lower
        == (
            (Fraction(1), Fraction(0), Fraction(0)),
            (Fraction(1, 3), Fraction(1), Fraction(0)),
            (Fraction(1), Fraction(3, 4), Fraction(1)),
        ),
    )
    checks.check(
        "signature-from-pivots",
        "LDL pivot signs give signature (1, 2, 0)",
        signature(pivots) == (1, 2, 0)
        and all(pivot != 0 for pivot in pivots)
        and pivots[0] * pivots[1] * pivots[2] == det3(minkowski_g) == Fraction(5),
    )
    checks.check(
        "principal-minor-inertia",
        "leading minors (3, -4, 5) independently give two sign changes and no zero",
        leading == (Fraction(3), Fraction(-4), Fraction(5))
        and signs == ["same", "change", "change"]
        and 0 not in leading,
    )
    checks.check(
        "versus-gram4",
        "the nnseed signature equals the displayed gram4 triple (1, 2, 0)",
        signature(pivots) == (1, 2, 0)
        and "equals the displayed gram4 comparison value `(1, 2, 0)`" in note,
    )
    checks.check(
        "not-one-seed-clone",
        "1-seed ticks (3,2,3) produce a different Gram, so this is not a clone",
        seed_g
        == (
            (Fraction(8), Fraction(5), Fraction(8)),
            (Fraction(5), Fraction(2), Fraction(4)),
            (Fraction(8), Fraction(4), Fraction(6)),
        )
        and seed_g != minkowski_g
        and signature(seed_pivots) == (1, 2, 0)
        and seed_ticks != ticks,
    )
    checks.check(
        "euclidean-mutation",
        "the Euclidean product on the same 4-vectors has signature (3, 0, 0)",
        signature(euclid_pivots) == (3, 0, 0)
        and euclid_g != minkowski_g
        and euclid_lower is not None,
    )
    checks.check(
        "no-float-signature",
        "Gram entries, pivots, and minors are exact Fraction values",
        all(isinstance(entry, Fraction) for row in minkowski_g for entry in row)
        and all(isinstance(pivot, Fraction) for pivot in pivots)
        and all(isinstance(minor, Fraction) for minor in leading),
    )
    checks.check(
        "axiom-unedited",
        "Admissibility remains the quoted nearest-neighbor rule and carries no Gram metric",
        "There is one fixed nearest-neighbor admissibility rule" in axiom
        and "Minkowski" not in axiom
        and "Gram" not in axiom
        and "u(x)" not in axiom,
    )
    checks.check(
        "note-contract",
        "the note states Theorems 1-3, displayed-not-adopted scope, and no L1",
        all(
            phrase in note
            for phrase in (
                "claim_scope: \"Minkowski Gram signature of the three nnseed displacements from origin of axis, face, and body events is reported versus gram4 (1,2,0). Displayed, not adopted.\"",
                "**Type:** bounded_theorem",
                "Displayed, not adopted",
                "not written into Admissibility",
                "L1 is not attached",
                "Uniqueness is not required",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "no-go-packet",
        "the landed note contains the complete N1-N8 discipline record",
        "## No-Go Discipline Gate" in note
        and all(f"### N{index} " in note for index in range(1, 9))
        and note.count("| ATTEMPTED |") >= 5,
    )
    checks.check(
        "n5-certificate-source",
        "the note carries the exact five forensic resolution lines",
        all(line in note for line in N5_LINES),
    )
    checks.check(
        "forbidden-phrases",
        "note and runner avoid the dispatch-forbidden phrases",
        all(phrase not in note for phrase in FORBIDDEN)
        and all(phrase not in source.split("FORBIDDEN")[0] for phrase in FORBIDDEN),
    )
    checks.check(
        "claim-type",
        "the source uses the bounded-theorem claim type without authoring an audit verdict",
        "claim_type: bounded_theorem" in note
        and "independent audit lane only" in normalized_note
        and "This note authors no audit verdict" in note,
    )

    for line in N5_LINES:
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
