#!/usr/bin/env python3
"""Exact Q(i) checks: trivial vs Pauli-adjoint cube action is extra.

One-site M_2. Two displayed maps of the body-diagonal cube 3-fold.
No QCD, no G_N, no axiom edit, no cache write, no network.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TRIVIAL_VS_PAULI_ADJOINT_CUBE_ACTION_IS_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TRIVIAL_VS_PAULI_ADJOINT_CUBE_ACTION_IS_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


class Qi:
    """a + b i with i^2 = -1 and a, b in Q."""

    __slots__ = ("a", "b")

    def __init__(self, a: Fraction | int, b: Fraction | int = 0) -> None:
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other: Qi) -> Qi:
        return Qi(self.a + other.a, self.b + other.b)

    def __sub__(self, other: Qi) -> Qi:
        return Qi(self.a - other.a, self.b - other.b)

    def __mul__(self, other: Qi) -> Qi:
        return Qi(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Qi):
            return NotImplemented
        return self.a == other.a and self.b == other.b

    def __neg__(self) -> Qi:
        return Qi(-self.a, -self.b)

    def conj(self) -> Qi:
        return Qi(self.a, -self.b)

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0


I_UNIT = Qi(1, 0)
ZERO = Qi(0, 0)
IMAG = Qi(0, 1)

Matrix = tuple[tuple[Qi, Qi], tuple[Qi, Qi]]


def mat_add(left: Matrix, right: Matrix) -> Matrix:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def mat_sub(left: Matrix, right: Matrix) -> Matrix:
    return (
        (left[0][0] - right[0][0], left[0][1] - right[0][1]),
        (left[1][0] - right[1][0], left[1][1] - right[1][1]),
    )


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def mat_scale(coeff: Qi, matrix: Matrix) -> Matrix:
    return (
        (coeff * matrix[0][0], coeff * matrix[0][1]),
        (coeff * matrix[1][0], coeff * matrix[1][1]),
    )


def mat_adj(matrix: Matrix) -> Matrix:
    return (
        (matrix[0][0].conj(), matrix[1][0].conj()),
        (matrix[0][1].conj(), matrix[1][1].conj()),
    )


def flatten(matrix: Matrix) -> tuple[Qi, ...]:
    return (matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1])


def span_rank(matrices: tuple[Matrix, ...]) -> int:
    """Exact row rank over Q(i)."""
    rows = [list(flatten(matrix)) for matrix in matrices]
    rank = 0
    col = 0
    n_rows = len(rows)
    n_cols = 4
    while rank < n_rows and col < n_cols:
        pivot = None
        for i in range(rank, n_rows):
            if not rows[i][col].is_zero():
                pivot = i
                break
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_entry = rows[rank][col]
        # Inverse of a+bi is (a-bi)/(a^2+b^2).
        denom = pivot_entry.a * pivot_entry.a + pivot_entry.b * pivot_entry.b
        pivot_inv = Qi(pivot_entry.a / denom, -pivot_entry.b / denom)
        rows[rank] = [entry * pivot_inv for entry in rows[rank]]
        for i in range(n_rows):
            if i == rank or rows[i][col].is_zero():
                continue
            factor = rows[i][col]
            rows[i] = [rows[i][j] - factor * rows[rank][j] for j in range(n_cols)]
        rank += 1
        col += 1
    return rank


def identity2() -> Matrix:
    return ((I_UNIT, ZERO), (ZERO, I_UNIT))


def sigma_x() -> Matrix:
    return ((ZERO, I_UNIT), (I_UNIT, ZERO))


def sigma_y() -> Matrix:
    return ((ZERO, Qi(0, -1)), (IMAG, ZERO))


def sigma_z() -> Matrix:
    return ((I_UNIT, ZERO), (ZERO, Qi(-1, 0)))


def phi0(matrix: Matrix) -> Matrix:
    return matrix


def phi_ad(matrix: Matrix) -> Matrix:
    """Unique unital linear extension of σx↦σy, σy↦σz, σz↦σx."""
    # M_2 basis expansion: X = a I + b σx + c σy + d σz,
    # a = Tr(X)/2, b = Tr(X σx)/2, and cyclic.
    sx, sy, sz, unit = sigma_x(), sigma_y(), sigma_z(), identity2()
    half = Qi(Fraction(1, 2), 0)
    coeff_i = half * (matrix[0][0] + matrix[1][1])
    xs = mat_mul(matrix, sx)
    ys = mat_mul(matrix, sy)
    zs = mat_mul(matrix, sz)
    coeff_x = half * (xs[0][0] + xs[1][1])
    coeff_y = half * (ys[0][0] + ys[1][1])
    coeff_z = half * (zs[0][0] + zs[1][1])
    return mat_add(
        mat_add(mat_scale(coeff_i, unit), mat_scale(coeff_x, sy)),
        mat_add(mat_scale(coeff_y, sz), mat_scale(coeff_z, sx)),
    )


def displayed_u() -> Matrix:
    sx, sy, sz, unit = sigma_x(), sigma_y(), sigma_z(), identity2()
    summed = mat_add(mat_add(sx, sy), sz)
    minus_i_sum = mat_scale(Qi(0, -1), summed)
    return mat_scale(Qi(Fraction(1, 2), 0), mat_add(unit, minus_i_sum))


def ad_u(matrix: Matrix) -> Matrix:
    unitary = displayed_u()
    return mat_mul(unitary, mat_mul(matrix, mat_adj(unitary)))


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

    print("external_scientific_inputs: none; displayed φ0, φAd, and U are theorem objects")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact Q(i); no fitted, QCD, or G_N input")
    print("negative_scope: the two displayed maps disagree on σx; neither is axiom-named")

    checks.check("field-i-square", "i^2 = -1", IMAG * IMAG == Qi(-1, 0))

    sx, sy, sz, unit = sigma_x(), sigma_y(), sigma_z(), identity2()
    checks.check("pauli-x-formula", "σx = ((0,1),(1,0))", sx == ((ZERO, I_UNIT), (I_UNIT, ZERO)))
    checks.check(
        "pauli-y-formula",
        "σy = ((0,-i),(i,0))",
        sy == ((ZERO, Qi(0, -1)), (IMAG, ZERO)),
    )
    checks.check(
        "pauli-z-formula",
        "σz = ((1,0),(0,-1))",
        sz == ((I_UNIT, ZERO), (ZERO, Qi(-1, 0))),
    )
    checks.check("pauli-x-square", "σx^2 = I", mat_mul(sx, sx) == unit)
    checks.check("pauli-y-square", "σy^2 = I", mat_mul(sy, sy) == unit)
    checks.check("pauli-z-square", "σz^2 = I", mat_mul(sz, sz) == unit)
    checks.check(
        "pauli-basis-rank-4",
        "{I,σx,σy,σz} has Q(i)-rank 4",
        span_rank((unit, sx, sy, sz)) == 4,
    )
    checks.check("star-x", "σx* = σx", mat_adj(sx) == sx)
    checks.check("star-y", "σy* = σy", mat_adj(sy) == sy)
    checks.check("star-z", "σz* = σz", mat_adj(sz) == sz)

    checks.check("phi0-x", "φ0(σx) = σx", phi0(sx) == sx)
    checks.check("phi0-y", "φ0(σy) = σy", phi0(sy) == sy)
    checks.check("phi0-z", "φ0(σz) = σz", phi0(sz) == sz)
    checks.check("phi0-unital", "φ0(I) = I", phi0(unit) == unit)

    checks.check("phiad-x", "φAd(σx) = σy", phi_ad(sx) == sy)
    checks.check("phiad-y", "φAd(σy) = σz", phi_ad(sy) == sz)
    checks.check("phiad-z", "φAd(σz) = σx", phi_ad(sz) == sx)
    checks.check("phiad-unital", "φAd(I) = I", phi_ad(unit) == unit)
    checks.check("phiad-star-x", "φAd(σx)* = φAd(σx*)", mat_adj(phi_ad(sx)) == phi_ad(mat_adj(sx)))

    checks.check(
        "thm1-disagreement",
        "φ0(σx) = σx ≠ σy = φAd(σx)",
        phi0(sx) == sx and phi_ad(sx) == sy and sx != sy,
    )
    checks.check(
        "mutation-images-equal-fails",
        "predicate φ0(σx) == φAd(σx) fails",
        phi0(sx) != phi_ad(sx),
    )

    composed_once = phi_ad
    composed_twice = lambda m: phi_ad(phi_ad(m))
    composed_thrice = lambda m: phi_ad(phi_ad(phi_ad(m)))
    checks.check(
        "control-phiad-order-three",
        "φAd³ = id on {I,σx,σy,σz}",
        all(composed_thrice(m) == m for m in (unit, sx, sy, sz)),
    )
    checks.check("control-phiad-not-id", "φAd ≠ id", composed_once(sx) != sx)
    checks.check(
        "control-phi0-order-three",
        "φ0³ = id",
        all(phi0(phi0(phi0(m))) == m for m in (unit, sx, sy, sz)),
    )
    checks.check(
        "control-twice-not-id",
        "φAd² ≠ id (disagreement is the image, not the order)",
        composed_twice(sx) != sx,
    )

    unitary = displayed_u()
    checks.check("exhibit-u-unitary", "U* U = I", mat_mul(mat_adj(unitary), unitary) == unit)
    checks.check("exhibit-ad-x", "Ad_U(σx) = σy", ad_u(sx) == sy)
    checks.check("exhibit-ad-y", "Ad_U(σy) = σz", ad_u(sy) == sz)
    checks.check("exhibit-ad-z", "Ad_U(σz) = σx", ad_u(sz) == sx)
    checks.check(
        "exhibit-matches-phiad",
        "Ad_U agrees with φAd on the Pauli basis",
        all(ad_u(m) == phi_ad(m) for m in (unit, sx, sy, sz)),
    )

    lattice_quote = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    qubit_quote = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    checks.check(
        "thm2-live-lattice-quote",
        "live Lattice names proper cubic rotations about each site",
        lattice_quote in axiom
        and "proper cubic rotations about each site" in axiom,
    )
    checks.check(
        "thm2-live-qubit-quote",
        "live Qubit names one-site M_2(C)",
        qubit_quote in axiom,
    )
    checks.check(
        "thm2-note-quotes-parents",
        "note quotes the live Lattice and Qubit sentences",
        lattice_quote in note and qubit_quote in note,
    )
    checks.check(
        "mutation-memo-names-adu-or-pauli-adjoint-fails",
        "predicate live memo names Ad_U or Pauli-adjoint fails",
        "Ad_U" not in axiom
        and "Pauli-adjoint" not in axiom
        and "pauli-adjoint" not in axiom.lower()
        and "φAd" not in axiom,
    )
    checks.check(
        "mutation-memo-lattice-named-fails",
        "predicate live memo contains Lattice-named fails",
        "Lattice-named" not in axiom,
    )
    checks.check(
        "thm3-both-extras-displayed",
        "note displays both maps as extras and does not adopt φAd",
        "Both maps are extras" in note
        and "It does not adopt `φAd`" in note
        and "lawful reading of Lattice+Qubit" in note,
    )
    checks.check(
        "boundary-no-qubit-flip",
        "note does not flip Qubit to M_3",
        "Qubit remains `M_2(C)`" in note
        and "not flipped to `M_3`" in note
        and "Do not flip Qubit" not in axiom,
    )
    checks.check(
        "boundary-no-unmerged-pr",
        "note reconstructs locally and does not cite #6268",
        "#6268" not in note and "PR #" not in note,
    )
    note_flat = " ".join(note.split())
    checks.check(
        "machine-status-contract",
        "note carries bounded-support status and no axiom adoption",
        "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and "This note authors no audit verdict" in note_flat,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TRIVIAL_VS_PAULI_ADJOINT_CUBE_ACTION_IS_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
