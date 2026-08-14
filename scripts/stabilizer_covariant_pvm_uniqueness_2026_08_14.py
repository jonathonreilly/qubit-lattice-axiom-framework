#!/usr/bin/env python3
"""Exact uniqueness checks for the stabilizer-covariant rank-1 PVM.

Integer Bloch vectors and rational projector arithmetic only.
No float, no physical menu selector, no axiom edit, no cache write.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "STABILIZER_COVARIANT_PVM_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/STABILIZER_COVARIANT_PVM_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Vec = tuple[int, int, int]
Matrix = tuple[tuple[Fraction, ...], ...]


def rot(vec: Vec) -> Vec:
    x, y, z = vec
    return (x, -z, y)


def rot_power(vec: Vec, power: int) -> Vec:
    out = vec
    for _ in range(power):
        out = rot(out)
    return out


def neg(vec: Vec) -> Vec:
    return (-vec[0], -vec[1], -vec[2])


def is_pm(left: Vec, right: Vec) -> bool:
    return left == right or left == neg(right)


def pvm_pair(vec: Vec) -> frozenset[Vec]:
    return frozenset({vec, neg(vec)})


def row_reduce(rows: list[list[Fraction]]) -> list[list[Fraction]]:
    """Return nonzero rows of the exact reduced row-echelon form."""
    if not rows:
        return []
    n_rows = len(rows)
    n_cols = len(rows[0])
    mat = [list(row) for row in rows]
    pivot_row = 0
    for col in range(n_cols):
        pivot = next(
            (row for row in range(pivot_row, n_rows) if mat[row][col] != 0),
            None,
        )
        if pivot is None:
            continue
        mat[pivot_row], mat[pivot] = mat[pivot], mat[pivot_row]
        pivot_value = mat[pivot_row][col]
        mat[pivot_row] = [entry / pivot_value for entry in mat[pivot_row]]
        for row in range(n_rows):
            if row == pivot_row or mat[row][col] == 0:
                continue
            factor = mat[row][col]
            mat[row] = [
                mat[row][j] - factor * mat[pivot_row][j] for j in range(n_cols)
            ]
        pivot_row += 1
        if pivot_row == n_rows:
            break
    return [row for row in mat if any(entry != 0 for entry in row)]


def nullspace(rows: list[list[Fraction]], n_cols: int) -> list[tuple[Fraction, ...]]:
    """Exact basis for the nullspace of a rational coefficient matrix."""
    reduced = row_reduce(rows)
    pivots: dict[int, list[Fraction]] = {}
    for row in reduced:
        pivot = next(index for index, value in enumerate(row) if value != 0)
        pivots[pivot] = row
    free_columns = [column for column in range(n_cols) if column not in pivots]
    basis: list[tuple[Fraction, ...]] = []
    for free in free_columns:
        vector = [Fraction(0)] * n_cols
        vector[free] = Fraction(1)
        for pivot, row in pivots.items():
            vector[pivot] = -row[free]
        basis.append(tuple(vector))
    return basis


def sign_eigen_system(sign: int) -> list[list[Fraction]]:
    """Rows of (R - sign I) u = 0 on coordinates (a, b, c)."""
    # R(a,b,c) = (a, -c, b)
    # plus:  (0, -b-c, b-c) = 0
    # minus: (2a, b-c, b+c) = 0
    if sign == 1:
        return [
            [Fraction(0), Fraction(0), Fraction(0)],
            [Fraction(0), Fraction(-1), Fraction(-1)],
            [Fraction(0), Fraction(1), Fraction(-1)],
        ]
    if sign == -1:
        return [
            [Fraction(2), Fraction(0), Fraction(0)],
            [Fraction(0), Fraction(1), Fraction(-1)],
            [Fraction(0), Fraction(1), Fraction(1)],
        ]
    raise ValueError("sign must be +1 or -1")


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][col] + right[row][col] for col in range(len(left)))
        for row in range(len(left))
    )


def scale(scalar: Fraction, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(scalar * matrix[row][col] for col in range(len(matrix)))
        for row in range(len(matrix))
    )


def mul(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return tuple(
        tuple(
            sum(
                (left[row][mid] * right[mid][col] for mid in range(size)),
                Fraction(0),
            )
            for col in range(size)
        )
        for row in range(size)
    )


def adj_real(matrix: Matrix) -> Matrix:
    size = len(matrix)
    return tuple(tuple(matrix[col][row] for col in range(size)) for row in range(size))


def trace(matrix: Matrix) -> Fraction:
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def eye2() -> Matrix:
    return (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )


def sigma_x() -> Matrix:
    return (
        (Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(0)),
    )


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; exact integer Bloch algebra only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact integer vectors and Fraction matrices; no floating-point inputs")
    print("claim_boundary: bounded algebraic uniqueness; no physical menu identification is asserted")

    e_x: Vec = (1, 0, 0)
    e_y: Vec = (0, 1, 0)
    e_z: Vec = (0, 0, 1)
    equator: Vec = (0, 1, 1)

    checks.check("thm1-r-ex", "R e_x = e_x", rot(e_x) == e_x)
    powers_fix_axis = all(rot_power(e_x, k) == e_x for k in (1, 2, 3, 4))
    checks.check(
        "thm1-powers-fix-axis",
        "R^k e_x = e_x for k=1,2,3,4",
        powers_fix_axis,
    )
    spectral_pairs = [pvm_pair(rot_power(e_x, k)) for k in (0, 1, 2, 3)]
    checks.check(
        "thm1-pvm-set-stable",
        "the spectral pair is invariant under R^k for k=1,2,3",
        all(pair == spectral_pairs[0] for pair in spectral_pairs),
    )

    identity = eye2()
    p_plus = scale(Fraction(1, 2), add(identity, sigma_x()))
    p_minus = scale(Fraction(1, 2), add(identity, scale(Fraction(-1), sigma_x())))
    checks.check(
        "thm1-pvm-totalize",
        "P_n + P_{-n} = I",
        add(p_plus, p_minus) == identity,
    )
    checks.check(
        "thm1-traces-k123",
        "constructed traces Tr(P_n)=Tr(P_{-n})=1 persist for k=1,2,3",
        all(
            rot_power(e_x, k) == e_x
            and trace(p_plus) == Fraction(1)
            and trace(p_minus) == Fraction(1)
            for k in (1, 2, 3)
        ),
    )
    checks.check(
        "thm1-projectors",
        "P_n and P_{-n} are complementary rank-1 orthogonal projectors",
        mul(p_plus, p_plus) == p_plus
        and mul(p_minus, p_minus) == p_minus
        and adj_real(p_plus) == p_plus
        and adj_real(p_minus) == p_minus
        and mul(p_plus, p_minus)
        == (
            (Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(0)),
        )
        and p_plus != p_minus,
    )

    checks.check("thm2-ey-fails", "R e_y = e_z is not ± e_y", rot(e_y) == e_z and not is_pm(rot(e_y), e_y))
    checks.check("thm3-ez-fails", "R e_z = -e_y is not ± e_z", rot(e_z) == neg(e_y) and not is_pm(rot(e_z), e_z))
    checks.check(
        "thm4-equator-fails",
        "R(0,1,1)=(0,-1,1) is not ±(0,1,1)",
        rot(equator) == (0, -1, 1) and not is_pm(rot(equator), equator),
    )

    plus_kernel = nullspace(sign_eigen_system(1), 3)
    minus_kernel = nullspace(sign_eigen_system(-1), 3)
    checks.check(
        "thm5-plus-kernel",
        "the plus eigenspace is the line spanned by e_x",
        plus_kernel == [(Fraction(1), Fraction(0), Fraction(0))],
    )
    checks.check(
        "thm5-minus-empty",
        "the minus eigenspace is {0}",
        minus_kernel == [],
    )
    checks.check(
        "thm5-unit-survivors",
        "the only unit rational points on the plus line are ± e_x",
        plus_kernel == [(Fraction(1), Fraction(0), Fraction(0))]
        and (1, 0, 0) != (-1, 0, 0)
        and pvm_pair((1, 0, 0)) == pvm_pair((-1, 0, 0)),
    )

    r2_ey = rot_power(e_y, 2)
    r2_ez = rot_power(e_z, 2)
    checks.check(
        "thm6-powers-on-survivors",
        "R^2 e_x = e_x and R^3 e_x = e_x",
        rot_power(e_x, 2) == e_x and rot_power(e_x, 3) == e_x,
    )
    checks.check(
        "thm6-r2-weaker",
        "R^2 fixes e_y and e_z up to sign, so the square is strictly weaker",
        r2_ey == neg(e_y) and r2_ez == neg(e_z),
    )
    checks.check(
        "mutation-r2-only-fails",
        "replacing R by R^2 would admit the e_y axis",
        is_pm(rot_power(e_y, 2), e_y) and not is_pm(rot(e_y), e_y),
    )
    checks.check("r4-identity", "R^4 is the identity on the three axes", all(
        rot_power(vec, 4) == vec for vec in (e_x, e_y, e_z, equator)
    ))

    qubit_quote = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    qubit_privilege = (
        "No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone."
    )
    adm_cov = (
        "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations."
    )
    adm_dist = (
        "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
    )
    checks.check(
        "live-parent-quotes",
        "Qubit and Admissibility sentences are quoted without rewrite",
        qubit_quote in axiom
        and qubit_privilege in note
        and adm_cov in note
        and adm_dist in note
        and qubit_quote in note
        and "No possibility is privileged." in axiom
        and "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"
        in axiom
        and "For each site, the probability distribution over the possibilities is"
        in axiom,
    )

    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    checks.check(
        "forbidden-substrings",
        "the note avoids the dispatch-forbidden substrings",
        all(token not in note for token in forbidden)
        and "we adopt" not in note.lower()
        and "Codex" not in note
        and "L_phys" not in note,
    )
    checks.check(
        "no-qubit-flip",
        "the note refuses a Qubit rewrite and keeps M_2(C)",
        "No Qubit rewrite" in note
        and qubit_quote in note
        and "does not change the Qubit statement" in note,
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "machine-status-contract",
        "bounded status, frontier trace, and next action are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "trace_class: frontier_discovery" in note
        and 'next_trace_action: "independent audit of the bounded algebraic uniqueness claim"'
        in note
        and all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "import-boundary-contract",
        "the supplied axis, Bloch chart, and absent physical bridge are disclosed",
        "## Inputs And Import Boundary" in note
        and "Explicit theorem-domain condition" in note
        and "External empirical or literature inputs:** none" in note
        and "Open physical bridge" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/STABILIZER_COVARIANT_PVM_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "claim-type-and-proof-contract",
        "the bounded type and universal proof obligation are source-visible",
        "**Type:** bounded_theorem" in note
        and "a general triple `u=(a,b,c)` is solved exactly over `Q`" in note
        and "the minus case is empty" in note
        and "### N8" not in note
        and "FAIL / DO NOT SHIP" not in note
        and "new axiom" not in note.lower()
        and ("import " + "qcd") not in self_source.lower()
        and ("from " + "qcd") not in self_source.lower()
        and ("import " + "math") not in self_source
        and ("import " + "numpy") not in self_source,
    )

    print(
        "per_element: exact identities cover e_x, e_y, e_z, (0,1,1), and the spectral pair P_n, P_{-n}."
    )
    print(
        "per_site: the theorem is evaluated only on one-site Bloch vectors for the supplied M_2(C) chart."
    )
    print(
        "per_mode: R, R^2, and R^3 are resolved; the 180-degree square is distinguished from the order-4 generator."
    )
    print(
        "per_block: the plus and minus eigen-conditions on all three rational coordinates are row-reduced."
    )
    print(
        "lattice_wide: checked and not executed — the claim asserts no multi-site or lattice-wide lift."
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
