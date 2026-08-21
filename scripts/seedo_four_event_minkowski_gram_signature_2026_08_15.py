#!/usr/bin/env python3
"""Exact Minkowski Gram signature of three displayed seedo displacements.

Ticks are the displayed seedo values, not a path dump. Signature is computed
by exact rational LDL with diagonal pivoting and by the characteristic
polynomial; no float is used. No cache is written.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SEEDO_FOUR_EVENT_MINKOWSKI_GRAM_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SEEDO_FOUR_EVENT_MINKOWSKI_GRAM_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

FORBIDDEN_PHRASES = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
GRAM4_SIGNATURE = (1, 2, 0)

Poly = tuple[Fraction, ...]
Matrix3 = tuple[tuple[Fraction, Fraction, Fraction], ...]
Vec4 = tuple[Fraction, Fraction, Fraction, Fraction]


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


def F(value: int) -> Fraction:
    return Fraction(value)


def minkowski(u: Vec4, v: Vec4) -> Fraction:
    return u[0] * v[0] - (u[1] * v[1] + u[2] * v[2] + u[3] * v[3])


def gram_of(vectors: tuple[Vec4, Vec4, Vec4]) -> Matrix3:
    return tuple(
        tuple(minkowski(left, right) for right in vectors) for left in vectors
    )


def det3(matrix: Matrix3) -> Fraction:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def principal_minors(matrix: Matrix3) -> tuple[Fraction, Fraction, Fraction]:
    m00 = matrix[0][0]
    minor2 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (m00, minor2, det3(matrix))


def ldl_inertia(matrix: Matrix3) -> tuple[int, int, int]:
    """Sylvester inertia by exact LDL with largest-|diag| pivoting."""

    size = 3
    work = [[matrix[row][col] for col in range(size)] for row in range(size)]
    remaining = [0, 1, 2]
    signs: list[int] = []
    for _ in range(size):
        pivot_at = max(
            range(len(remaining)),
            key=lambda index: abs(work[remaining[index]][remaining[index]]),
        )
        pivot = remaining.pop(pivot_at)
        diag = work[pivot][pivot]
        if diag == 0:
            leftover = all(
                work[pivot][other] == 0 and work[other][pivot] == 0
                for other in remaining
            )
            if leftover:
                signs.append(0)
                continue
            raise ValueError("nonzero off-diagonal with zero pivot")
        signs.append(1 if diag > 0 else -1)
        for row in remaining:
            multiplier = work[row][pivot] / diag
            for col in remaining:
                work[row][col] -= multiplier * work[pivot][col]
    return (signs.count(1), signs.count(-1), signs.count(0))


def trim(poly: Poly) -> Poly:
    coeffs = list(poly)
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return tuple(coeffs)


def poly_derivative(poly: Poly) -> Poly:
    if len(poly) == 1:
        return (F(0),)
    return trim(tuple(Fraction(index) * poly[index] for index in range(1, len(poly))))


def poly_divmod(numer: Poly, denom: Poly) -> tuple[Poly, Poly]:
    denom = trim(denom)
    if denom == (F(0),):
        raise ZeroDivisionError("zero polynomial")
    remainder = list(numer)
    quot_len = max(len(numer) - len(denom) + 1, 0)
    quot = [F(0)] * quot_len
    while len(remainder) >= len(denom):
        remainder = list(trim(tuple(remainder)))
        if remainder == [F(0)] or len(remainder) < len(denom):
            break
        factor = remainder[-1] / denom[-1]
        shift = len(remainder) - len(denom)
        quot[shift] = factor
        for index, coeff in enumerate(denom):
            remainder[index + shift] -= factor * coeff
    return trim(tuple(quot)), trim(tuple(remainder))


def sturm_chain(poly: Poly) -> list[Poly]:
    chain = [trim(poly), poly_derivative(poly)]
    while True:
        prev, current = chain[-2], chain[-1]
        if current == (F(0),):
            chain.pop()
            break
        if len(current) == 1:
            break
        _, remainder = poly_divmod(prev, current)
        if remainder == (F(0),):
            break
        chain.append(trim(tuple(-coeff for coeff in remainder)))
    return chain


def eval_poly(poly: Poly, value: Fraction | None, plus_infinity: bool | None) -> Fraction:
    if plus_infinity is not None:
        leading = poly[-1]
        degree = len(poly) - 1
        if plus_infinity:
            return leading
        return leading if degree % 2 == 0 else -leading
    assert value is not None
    acc = F(0)
    power = F(1)
    for coeff in poly:
        acc += coeff * power
        power *= value
    return acc


def sign_changes(chain: list[Poly], value: Fraction | None, plus_infinity: bool | None) -> int:
    signs: list[int] = []
    for poly in chain:
        sample = eval_poly(poly, value, plus_infinity)
        if sample == 0:
            continue
        signs.append(1 if sample > 0 else -1)
    return sum(left != right for left, right in zip(signs, signs[1:]))


def char_poly(matrix: Matrix3) -> Poly:
    trace = matrix[0][0] + matrix[1][1] + matrix[2][2]
    sum2 = (
        (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
        + (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0])
        + (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
    )
    determinant = det3(matrix)
    # det(lambda I - G) = lambda^3 - tr lambda^2 + (sum of 2x2 principals) lambda - det
    return ( -determinant, sum2, -trace, F(1) )


def char_inertia(matrix: Matrix3) -> tuple[int, int, int]:
    poly = char_poly(matrix)
    chain = sturm_chain(poly)
    at_minus = sign_changes(chain, None, False)
    at_zero = sign_changes(chain, F(0), None)
    at_plus = sign_changes(chain, None, True)
    n_minus = at_minus - at_zero
    n_plus = at_zero - at_plus
    n_zero = 1 if eval_poly(poly, F(0), None) == 0 else 0
    return (n_plus, n_minus, n_zero)


def euclidean_gram(vectors: tuple[tuple[Fraction, Fraction, Fraction], ...]) -> Matrix3:
    return tuple(
        tuple(
            left[0] * right[0] + left[1] * right[1] + left[2] * right[2]
            for right in vectors
        )
        for left in vectors
    )


def all_fraction_entries(matrix: Matrix3) -> bool:
    return all(
        isinstance(entry, Fraction) and not isinstance(entry, float)
        for row in matrix
        for entry in row
    )


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("external_scientific_inputs: displayed four events and displayed seedo ticks only")
    print("framework_role: Lattice supplies Z^3 sites; no metric is written into Admissibility")
    print(
        "claim_scope: Minkowski Gram signature of the three seedo displacements "
        "from origin of axis, face, and body events is reported versus gram4 (1,2,0). "
        "Displayed, not adopted."
    )

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the source note and the axiom memo",
        AUDIT_INPUT_PATHS == (
            "docs/SEEDO_FOUR_EVENT_MINKOWSKI_GRAM_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        AUDIT_INPUT_PATHS,
    )
    checks.check(
        "audit-timeout",
        "audit timeout is the standard 120s bound",
        AUDIT_TIMEOUT_SEC == 120,
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    checks.check(
        "source-lattice",
        "current axioms supply the cubic lattice Z^3",
        lattice_sentence in axiom,
    )
    admissibility_section = axiom.split("### Admissibility / Local Constraint", 1)[1].split(
        "### Record / Fixed Reality", 1
    )[0]
    checks.check(
        "axiom-admissibility-has-no-metric",
        "the live Admissibility wording contains no Minkowski Gram or metric",
        "Minkowski" not in admissibility_section
        and "Gram" not in admissibility_section
        and "metric" not in admissibility_section.lower(),
    )

    origin = (F(0), F(0), F(0))
    axis = (F(1), F(0), F(0))
    face = (F(1), F(1), F(0))
    body = (F(1), F(1), F(1))
    ticks = {
        origin: F(0),
        axis: F(1),
        face: F(2),
        body: F(3),
    }

    def four_vector(point: tuple[Fraction, Fraction, Fraction]) -> Vec4:
        return (ticks[point], point[0], point[1], point[2])

    u_a = four_vector(axis)
    u_d = four_vector(face)
    u_b = four_vector(body)
    gram = gram_of((u_a, u_d, u_b))
    expected = (
        (F(0), F(1), F(2)),
        (F(1), F(2), F(4)),
        (F(2), F(4), F(6)),
    )

    checks.check(
        "four-vectors",
        "u(A)=(1,1,0,0), u(D)=(2,1,1,0), u(B)=(3,1,1,1) from displayed ticks",
        u_a == (F(1), F(1), F(0), F(0))
        and u_d == (F(2), F(1), F(1), F(0))
        and u_b == (F(3), F(1), F(1), F(1)),
        (u_a, u_d, u_b),
    )
    checks.check(
        "nine-entries",
        "the nine exact Minkowski Gram entries are the displayed rationals",
        gram == expected and all_fraction_entries(gram),
        gram,
    )
    checks.check(
        "symmetry",
        "G is symmetric",
        all(gram[i][j] == gram[j][i] for i in range(3) for j in range(3)),
    )
    checks.check(
        "axis-null",
        "the axis displacement is Minkowski-null: G_AA=0",
        gram[0][0] == F(0),
    )
    determinant = det3(gram)
    checks.check(
        "determinant",
        "det G = 2, so the 3-plane is nondegenerate",
        determinant == F(2),
        determinant,
    )
    minors = principal_minors(gram)
    checks.check(
        "leading-minors",
        "unpivoted leading minors are 0, -1, 2, so unpivoted Sylvester is blocked",
        minors == (F(0), F(-1), F(2)),
        minors,
    )

    ldl_sig = ldl_inertia(gram)
    poly = char_poly(gram)
    char_sig = char_inertia(gram)
    checks.check(
        "char-poly",
        "det(lambda I - G) = lambda^3 - 8 lambda^2 - 9 lambda - 2",
        poly == (F(-2), F(-9), F(-8), F(1)),
        poly,
    )
    checks.check(
        "ldl-signature",
        "exact pivoted LDL inertia is (1,2,0)",
        ldl_sig == (1, 2, 0),
        ldl_sig,
    )
    checks.check(
        "char-signature",
        "exact characteristic-polynomial inertia is (1,2,0)",
        char_sig == (1, 2, 0) and eval_poly(poly, F(0), None) != 0,
        char_sig,
    )
    checks.check(
        "versus-gram4",
        "the displayed seedo signature equals gram4 (1,2,0)",
        ldl_sig == GRAM4_SIGNATURE and char_sig == GRAM4_SIGNATURE,
        (ldl_sig, char_sig),
    )

    spatial = euclidean_gram((axis, face, body))
    spatial_sig = ldl_inertia(spatial)
    checks.check(
        "euclidean-mutation",
        "the Euclidean spatial Gram of the same three vectors is not (1,2,0)",
        spatial_sig != GRAM4_SIGNATURE and spatial_sig[0] == 3,
        spatial_sig,
    )

    zero_tick_vectors = (
        (F(0), axis[0], axis[1], axis[2]),
        (F(0), face[0], face[1], face[2]),
        (F(0), body[0], body[1], body[2]),
    )
    zero_tick_sig = ldl_inertia(gram_of(zero_tick_vectors))
    checks.check(
        "zero-tick-mutation",
        "erasing the displayed ticks changes the Minkowski signature",
        zero_tick_sig != GRAM4_SIGNATURE,
        zero_tick_sig,
    )

    required_note_phrases = (
        "O=(0,0,0), A=(1,0,0), D=(1,1,0), B=(1,1,1)",
        "t(O)=0, t(A)=1, t(D)=2, t(B)=3",
        "not recomputed by path dump",
        "u(x)=(t(x), x_1, x_2, x_3)",
        "u·v = t_u t_v − x_u·x_v",
        "[[0, 1, 2], [1, 2, 4], [2, 4, 6]]",
        "(n+, n−, n0) = (1, 2, 0)",
        "equals gram4's (1,2,0)",
        "Displayed, not adopted",
        "Do not attach L1",
        "Do not write a metric into Admissibility",
        "Uniqueness is not required",
        "Four events only",
        "No Dijkstra",
        "claim_scope: Minkowski Gram signature of the three seedo displacements from origin of axis, face, and body events is reported versus gram4 (1,2,0). Displayed, not adopted.",
        "**Type:** bounded_theorem",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "hypothetical_axiom_status: no edit",
    )
    missing = [phrase for phrase in required_note_phrases if phrase not in note]
    checks.check(
        "note-contract",
        "the note states the four events, displayed ticks, Gram, signature, and bounds",
        not missing,
        missing,
    )
    checks.check(
        "four-events-only",
        "the note names only the four cube events O, A, D, B",
        "Four events only" in note
        and "O=(0,0,0)" in note
        and "E=" not in note
        and "C=(0,1,0)" not in note,
    )
    checks.check(
        "no-dijkstra",
        "ticks are displayed; Dijkstra is excluded",
        "No Dijkstra" in note
        and "Dijkstra" not in note.replace("No Dijkstra", "")
        and "path dump" in note,
    )
    checks.check(
        "no-l1",
        "the note refuses to attach L1",
        "Do not attach L1" in note and "L1 is closed" not in note,
    )
    checks.check(
        "no-admissibility-metric",
        "the note refuses to write a metric into Admissibility",
        "Do not write a metric into Admissibility" in note
        and "Admissibility metric" not in note,
    )
    checks.check(
        "uniqueness-not-required",
        "equality versus gram4 is reported without a uniqueness claim",
        "Uniqueness is not required" in note
        and "unique Lorentzian 3-plane" not in note,
    )
    forbidden_hits = [phrase for phrase in FORBIDDEN_PHRASES if phrase in note]
    checks.check(
        "forbidden-absent",
        "forbidden gravity/TOE phrases are absent from the note",
        not forbidden_hits,
        forbidden_hits,
    )
    checks.check(
        "no-runner-cache",
        "the note does not attach a runner-cache path",
        "runner-cache" not in note and "citation manifest" not in note,
    )
    checks.check(
        "no-float-signature",
        "signature objects are exact integers, not floats",
        all(isinstance(value, int) for value in ldl_sig + char_sig)
        and all_fraction_entries(gram),
        (ldl_sig, char_sig),
    )

    print("per_element: checked — all nine Gram entries and both exact inertia algorithms")
    print("per_site: checked — only the four displayed events O, A, D, B")
    print("per_mode: checked and not executed — no dynamical mode or continuum limit")
    print("per_block: checked — the 3x3 Minkowski block versus the Euclidean mutation")
    print("lattice_wide: checked and not executed — no lattice-wide metric or L1 attachment")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
