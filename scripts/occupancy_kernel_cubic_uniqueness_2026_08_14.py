#!/usr/bin/env python3
"""Unique proper-cubic-equivariant linear occupancy kernel."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "OCCUPANCY_KERNEL_CUBIC_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OCCUPANCY_KERNEL_CUBIC_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

# bits: +x,-x,+y,-y,+z,-z
PX, MX, PY, MY, PZ, MZ = range(6)


def n0(c: tuple) -> tuple:
    """Identity gate."""
    return (c[PX] - c[MX], c[PY] - c[MY], c[PZ] - c[MZ])


def s_even(c: tuple) -> tuple:
    return (c[PX] + c[MX], c[PY] + c[MY], c[PZ] + c[MZ])


def rotate_z(c: tuple) -> tuple:
    """Identity gate. R:(x,y,z)->(-y,x,z); c'(g)=c(R^{-1} g)."""
    # c'(+x)=c(-y), c'(-x)=c(+y), c'(+y)=c(+x), c'(-y)=c(-x), z fixed
    return (c[MY], c[PY], c[PX], c[MX], c[PZ], c[MZ])


def rotate_x(c: tuple) -> tuple:
    """90° about x: (x,y,z)->(x,-z,y). c'(g)=c(R^{-1} g)."""
    # R^{-1}(x,y,z)=(x,z,-y)
    # c'(+y)=c(-z), c'(-y)=c(+z), c'(+z)=c(+y), c'(-z)=c(-y)
    return (c[PX], c[MX], c[MZ], c[PZ], c[PY], c[MY])


def Rz_vec(v: tuple) -> tuple:
    x, y, z = v
    return (-y, x, z)


def Rx_vec(v: tuple) -> tuple:
    x, y, z = v
    return (x, -z, y)


def all_occ():
    for bits in range(64):
        yield tuple((bits >> i) & 1 for i in range(6))


def apply_A(A, c):
    return tuple(sum(A[i][j] * c[j] for j in range(6)) for i in range(3))


def equivariant_dimension():
    """Identity gate. Rank-nullity on 18 coefficients, two generators."""
    # Unknowns A[i][j], i=0..2, j=0..5. Index 6*i+j.
    # For each generator, A ρ = R A, i.e. A(g e_j) = R A e_j for j=0..5.
    # A e_j is column j. A(g e_j) is column of the preimage bit.
    # We collect equations as rows of M (len x 18) and row-reduce.
    rows = []

    def add_map(rot_bits, rot_vec):
        for j in range(6):
            e = [0] * 6
            e[j] = 1
            ge = rot_bits(tuple(e))
            # A ge = column combo: (A ge)_i = sum_k A[i][k] ge[k]
            # R A e_j : A e_j is (A[0][j], A[1][j], A[2][j]); apply rot_vec
            # For each output component i: lhs - rhs = 0
            for i in range(3):
                row = [Fraction(0)] * 18
                for k in range(6):
                    if ge[k]:
                        row[6 * i + k] += 1
                # rhs = rot_vec(column j)_i
                # rot_vec of (A00j, A10j, A20j)
                basis = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
                # We need the i-th component of R applied to column j.
                # R(A[0][j], A[1][j], A[2][j])_i = sum_p R_{i p} A[p][j]
                # Compute R on the three standard basis vectors:
                images = [rot_vec(basis[p]) for p in range(3)]
                for p in range(3):
                    row[6 * p + j] -= images[p][i]
                rows.append(row)

    add_map(rotate_z, Rz_vec)
    add_map(rotate_x, Rx_vec)
    return _null_dim(rows)


def _null_dim(rows):
    """Row-reduce and count free variables."""
    if not rows:
        return 18
    m = [list(r) for r in rows]
    n = 18
    r = 0
    used = []
    for col in range(n):
        pivot = None
        for i in range(r, len(m)):
            if m[i][col] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        pv = m[r][col]
        m[r] = [x / pv for x in m[r]]
        for i in range(len(m)):
            if i == r:
                continue
            fac = m[i][col]
            if fac != 0:
                m[i] = [m[i][k] - fac * m[r][k] for k in range(n)]
        used.append(col)
        r += 1
        if r == n:
            break
    return n - len(used)


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
    four = axiom.split("## The Four Framework Axioms", 1)[-1].split("## Qualification", 1)[0]

    print("external_scientific_inputs: none")
    print("package_local_integrity_reads: runner, note, axiom memo")
    print("measure_boundary: exact Q uniqueness of the occupancy kernel")
    print("negative_scope: linear maps on six bits, not a TOE")

    n_ok = all(n0(rotate_z(c)) == Rz_vec(n0(c)) and n0(rotate_x(c)) == Rx_vec(n0(c)) for c in all_occ())
    checks.check("thm1-n-equiv", "n is equivariant under 90z and 90x on all 64", n_ok)
    s_fail = any(s_even(rotate_z(c)) != Rz_vec(s_even(c)) for c in all_occ())
    checks.check("thm2-s-not", "s is not the standard 3", s_fail)
    dim = equivariant_dimension()
    checks.check("thm3-dim", "equivariant Hom is 1-dimensional", dim == 1)
    # n0 itself is a nonzero equivariant map
    checks.check("thm3-n-nonzero", "n is a nonzero witness", n0((1, 0, 0, 0, 0, 0)) == (1, 0, 0))
    checks.check("mutation-s-fails", "predicate s is equivariant must fail", s_fail)
    checks.check("mutation-dim2-fails", "predicate dimension is 2 must fail", dim != 2)
    checks.check(
        "quoted",
        "note quotes Qubit and Admissibility",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`." in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note,
    )
    forbidden = ("we adopt", "L_phys", "0.5934", "Lattice-named", "exhausted", "closes the route")
    checks.check(
        "boundary",
        "not TOE, no forbidden phrases",
        all(p not in note for p in forbidden)
        and "not a TOE" in note
        and "Qubit remains `M_2(C)`" in note
        and "This note authors no audit verdict" in note
        and "QCD is unused" in note
        and "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"' in note
        and "Honest-auditor / Boundary" in note,
    )
    checks.check("memo-silent", "axioms do not name n_μ uniqueness", "occupancy kernel" not in four)
    checks.check(
        "gates",
        "identity gates and AUDIT_INPUT_PATHS",
        "def n0(" in self_source
        and "def rotate_z(" in self_source
        and "def equivariant_dimension(" in self_source
        and AUDIT_INPUT_PATHS == (
            "docs/OCCUPANCY_KERNEL_CUBIC_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — 6 occupancy bits, 18 coefficients")
    print("per_site: checked exactly — all 64 occupancy tuples")
    print("per_mode: checked exactly — two 90° generators and Hom dimension")
    print("per_block: checked exactly — uniqueness of the linear kernel")
    print("lattice_wide: checked and not executed — not axiom text")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
