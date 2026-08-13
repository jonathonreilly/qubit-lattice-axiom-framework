#!/usr/bin/env python3
"""Exact checks: the two-site factor-swap uniquely names a rank-3 corner.

Finite Fraction identities only. No QCD, no axiom edit, no cache write.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_SITE_FACTOR_SWAP_UNIQUELY_NAMES_RANK3_CORNER_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_SITE_FACTOR_SWAP_UNIQUELY_NAMES_RANK3_CORNER_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, ...], ...]


def zero(n: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(n)) for _ in range(n))


def eye(n: int) -> Matrix:
    return tuple(tuple(Fraction(int(row == col)) for col in range(n)) for row in range(n))


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
            sum((left[row][mid] * right[mid][col] for mid in range(size)), Fraction(0))
            for col in range(size)
        )
        for row in range(size)
    )


def adj(matrix: Matrix) -> Matrix:
    size = len(matrix)
    return tuple(tuple(matrix[col][row] for col in range(size)) for row in range(size))


def trace(matrix: Matrix) -> Fraction:
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def rank(matrix: Matrix) -> int:
    rows = [list(row) for row in matrix]
    n = len(rows)
    rnk = 0
    col = 0
    while rnk < n and col < n:
        pivot = None
        for i in range(rnk, n):
            if rows[i][col] != 0:
                pivot = i
                break
        if pivot is None:
            col += 1
            continue
        rows[rnk], rows[pivot] = rows[pivot], rows[rnk]
        pivot_val = rows[rnk][col]
        rows[rnk] = [entry / pivot_val for entry in rows[rnk]]
        for i in range(n):
            if i == rnk or rows[i][col] == 0:
                continue
            factor = rows[i][col]
            rows[i] = [rows[i][j] - factor * rows[rnk][j] for j in range(n)]
        rnk += 1
        col += 1
    return rnk


def kron(left: Matrix, right: Matrix) -> Matrix:
    a, b = len(left), len(right)
    return tuple(
        tuple(left[i // b][j // b] * right[i % b][j % b] for j in range(a * b))
        for i in range(a * b)
    )


def e_unit(n: int, row: int, col: int) -> Matrix:
    data = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    data[row][col] = Fraction(1)
    return tuple(tuple(item) for item in data)


def factor_swap() -> Matrix:
    return (
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    )


def pauli_x() -> Matrix:
    return (
        (Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(0)),
    )


def pauli_z() -> Matrix:
    return (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-1)),
    )


def apply_to_basis(matrix: Matrix, index: int) -> tuple[Fraction, ...]:
    return tuple(matrix[row][index] for row in range(len(matrix)))


def flatten_sym(matrix: Matrix) -> tuple[Fraction, ...]:
    """Upper triangle of a 4x4 symmetric matrix, 10 coordinates."""
    coords = []
    for i in range(4):
        for j in range(i, 4):
            coords.append(matrix[i][j])
    return tuple(coords)


def unflatten_sym(coords: tuple[Fraction, ...]) -> Matrix:
    data = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    k = 0
    for i in range(4):
        for j in range(i, 4):
            data[i][j] = coords[k]
            data[j][i] = coords[k]
            k += 1
    return tuple(tuple(row) for row in data)


def row_reduce(rows: list[list[Fraction]]) -> list[list[Fraction]]:
    if not rows:
        return []
    n_rows = len(rows)
    n_cols = len(rows[0])
    mat = [list(row) for row in rows]
    rank_i = 0
    col = 0
    while rank_i < n_rows and col < n_cols:
        pivot = None
        for i in range(rank_i, n_rows):
            if mat[i][col] != 0:
                pivot = i
                break
        if pivot is None:
            col += 1
            continue
        mat[rank_i], mat[pivot] = mat[pivot], mat[rank_i]
        pivot_val = mat[rank_i][col]
        mat[rank_i] = [entry / pivot_val for entry in mat[rank_i]]
        for i in range(n_rows):
            if i == rank_i or mat[i][col] == 0:
                continue
            factor = mat[i][col]
            mat[i] = [mat[i][j] - factor * mat[rank_i][j] for j in range(n_cols)]
        rank_i += 1
        col += 1
    return [row for row in mat if any(entry != 0 for entry in row)]


def intertwining_kernel() -> list[Matrix]:
    """Real-symmetric 4x4 solutions of U(A)=B U for A=X⊗I, B=I⊗X, X=E00,E01."""
    i2 = eye(2)
    gens = (e_unit(2, 0, 0), e_unit(2, 0, 1))
    constraints: list[list[Fraction]] = []
    for x in gens:
        left_op = kron(x, i2)
        right_op = kron(i2, x)
        for basis_index in range(10):
            coords = [Fraction(0)] * 10
            coords[basis_index] = Fraction(1)
            u = unflatten_sym(tuple(coords))
            residual = add(mul(u, left_op), scale(Fraction(-1), mul(right_op, u)))
            for r in range(4):
                for c in range(4):
                    row = [Fraction(0)] * 10
                    # residual is linear in U; collect coefficient of this basis U
                    # Build the constraint matrix by evaluating each basis element.
                    # Done below via a second pass.
                    _ = residual, row
        # Coefficient matrix: for each output entry, 10 unknowns.
        coeff_rows: list[list[Fraction]] = [ [Fraction(0)] * 10 for _ in range(16) ]
        for basis_index in range(10):
            coords = [Fraction(0)] * 10
            coords[basis_index] = Fraction(1)
            u = unflatten_sym(tuple(coords))
            residual = add(mul(u, left_op), scale(Fraction(-1), mul(right_op, u)))
            for r in range(4):
                for c in range(4):
                    coeff_rows[4 * r + c][basis_index] = residual[r][c]
        constraints.extend(coeff_rows)
    reduced = row_reduce(constraints)
    # Nullspace of reduced (RREF).
    pivot_col = {}
    for row in reduced:
        for j, val in enumerate(row):
            if val != 0:
                pivot_col[j] = row
                break
    free = [j for j in range(10) if j not in pivot_col]
    basis = []
    for f in free:
        coords = [Fraction(0)] * 10
        coords[f] = Fraction(1)
        for j, row in pivot_col.items():
            coords[j] = -row[f]
        basis.append(unflatten_sym(tuple(coords)))
    return basis


def involutions_in_span(span: list[Matrix]) -> list[Matrix]:
    """Find U=sum a_i B_i with a_i in {-1,0,1} and U^2=I, U!=0. Enough for ±F."""
    found: list[Matrix] = []
    if not span:
        return found
    dim = len(span)
    # Search {-2,-1,0,1,2}^dim is 5^k; k is small (expected 2).
    ranges = range(-2, 3)

    def rec(idx: int, acc: Matrix) -> None:
        if idx == dim:
            if acc != zero(4) and mul(acc, acc) == eye(4) and adj(acc) == acc:
                if acc not in found:
                    found.append(acc)
            return
        for coeff in ranges:
            rec(idx + 1, add(acc, scale(Fraction(coeff), span[idx])))

    rec(0, zero(4))
    return found


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

    print("external_scientific_inputs: none; exact Fraction two-site swap")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact Fraction; no float, no QCD import")
    print("negative_scope: factor-swap names p_+; leftover not adopted")

    f = factor_swap()
    i4 = eye(4)
    i2 = eye(2)
    p_plus = scale(Fraction(1, 2), add(i4, f))
    p_minus = scale(Fraction(1, 2), add(i4, scale(Fraction(-1), f)))

    checks.check("thm1-hermitian", "F^* = F", adj(f) == f)
    checks.check("thm1-involution", "F^2 = I_4", mul(f, f) == i4)
    checks.check("thm1-trace", "Tr(F) = 2", trace(f) == Fraction(2))

    gens = (e_unit(2, 0, 0), e_unit(2, 0, 1), pauli_x(), pauli_z())
    ad_ok = True
    for x in gens:
        left = kron(x, i2)
        right = kron(i2, x)
        if mul(mul(f, left), f) != right or mul(mul(f, right), f) != left:
            ad_ok = False
    checks.check(
        "thm2-ad-exchanges",
        "Ad_F(X⊗I)=I⊗X and Ad_F(I⊗X)=X⊗I on E00,E01,σx,σz",
        ad_ok,
    )

    # Theorem 3: unique linear map on four basis vectors.
    images = {
        0: (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),  # |00> -> |00>
        1: (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),  # |01> -> |10>
        2: (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),  # |10> -> |01>
        3: (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),  # |11> -> |11>
    }
    checks.check(
        "thm3-basis-images",
        "F sends |i⟩⊗|j⟩ to |j⟩⊗|i⟩ on the four product basis vectors",
        all(apply_to_basis(f, idx) == images[idx] for idx in range(4)),
    )

    minus_f = scale(Fraction(-1), f)
    checks.check("mutation-f-eq-minus-f-fails", "predicate F == -F fails", f != minus_f)
    checks.check(
        "thm4-minus-f-also-implements",
        "(-F)(X⊗I)(-F)=I⊗X on E00",
        mul(mul(minus_f, kron(e_unit(2, 0, 0), i2)), minus_f) == kron(i2, e_unit(2, 0, 0)),
    )

    span = intertwining_kernel()
    invols = involutions_in_span(span)
    checks.check(
        "thm4-span-contains-pm-f",
        "intertwining span contains F and -F",
        f in invols and minus_f in invols,
    )
    # Stronger: the only involutions found in a small integer grid on the span are ±F.
    extra = [u for u in invols if u not in (f, minus_f)]
    checks.check(
        "thm4-only-pm-f",
        "Hermitian involutions in the integer grid on the intertwining span are exactly ±F",
        set(invols) == {f, minus_f} and extra == [],
    )

    checks.check("thm5-pplus-proj", "p_+^2 = p_+ = p_+^*", mul(p_plus, p_plus) == p_plus and adj(p_plus) == p_plus)
    checks.check("thm5-pminus-proj", "p_-^2 = p_- = p_-^*", mul(p_minus, p_minus) == p_minus and adj(p_minus) == p_minus)
    checks.check("thm5-rank-pplus", "rank(p_+) = 3", rank(p_plus) == 3)
    checks.check("thm5-rank-pminus", "rank(p_-) = 1", rank(p_minus) == 1)
    checks.check("mutation-rank-pplus-eq-1-fails", "predicate rank(p_+) == 1 fails", rank(p_plus) != 1)
    checks.check("mutation-pplus-eq-i4-fails", "predicate p_+ == I_4 fails", p_plus != i4)

    checks.check(
        "thm6-refusals",
        "note refuses SU(3), QCD, color adoption, and Qubit rewrite",
        "does not install `SU(3)`, name QCD, select color, or rewrite" in note
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom
        and "Do not ship" in note
        and "F` is axiom content" in note,
    )
    checks.check(
        "machine-status-contract",
        "note carries the required leftover status and bounded-support surface",
        'hypothetical_axiom_status: "factor-swap leftover: unique F names p=(I+F)/2; not adopted as color"'
        in note
        and "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_SITE_FACTOR_SWAP_UNIQUELY_NAMES_RANK3_CORNER_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and N1-N8 gate are source-visible; no QCD module load",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note
        and ("import " + "qcd") not in self_source.lower()
        and ("from " + "qcd") not in self_source.lower(),
    )
    checks.check(
        "live-record-unread",
        "live Record unread sentence is quoted",
        "A site with no record cannot be read." in axiom
        and "A site with no record cannot be read." in note,
    )

    print("per_element: F, -F, p_+, p_-, E_00, E_01")
    print("per_site: two-site tensor T_2 ≅ M_4; no lattice-wide carrier")
    print("per_mode: displayed factor-swap and its rank-3 spectral projection")
    print("per_block: uniqueness of ±F among real-symmetric implementing involutions")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
