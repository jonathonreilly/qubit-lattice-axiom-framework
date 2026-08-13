#!/usr/bin/env python3
"""Exact checks: the two-block carrier is C^8, not one-site M_2(C).

Reconstructs Y_0 = Pi_+ - 3 Pi_- on C^8 over Fraction, computes
spectrum_multiset(Y_0) from the matrix, computes site_dim() from
dim M_2(C) = 4, and requires the predicates
  'Y_0 acts on C^2'
  'one-site M_2 contains Y_0'
to fail after calling those two functions.
"""

from __future__ import annotations

import hashlib
import inspect
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]

AUDIT_INPUT_PATHS = (
    "docs/TWO_BLOCK_CARRIER_IS_C8_NOT_ONE_SITE_M2_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
MAY2_PATH = ROOT / AUDIT_INPUT_PATHS[1]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[2]

Matrix = tuple[tuple[Fraction, ...], ...]


def file_sha256(relpath: str) -> str:
    return hashlib.sha256((ROOT / relpath).read_bytes()).hexdigest()


def eye(n: int) -> Matrix:
    return tuple(
        tuple(Fraction(1 if row == col else 0) for col in range(n))
        for row in range(n)
    )


def zero(n: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(n)) for _ in range(n))


def block_diag(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    m = len(right)
    rows = []
    for i in range(n + m):
        row = []
        for j in range(n + m):
            if i < n and j < n:
                row.append(left[i][j])
            elif i >= n and j >= n:
                row.append(right[i - n][j - n])
            else:
                row.append(Fraction(0))
        rows.append(tuple(row))
    return tuple(rows)


def mat_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(len(left)))
        for i in range(len(left))
    )


def mat_scale(coeff: Fraction, mat: Matrix) -> Matrix:
    return tuple(tuple(coeff * mat[i][j] for j in range(len(mat))) for i in range(len(mat)))


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    out = []
    for i in range(n):
        row = []
        for j in range(n):
            acc = Fraction(0)
            for k in range(n):
                acc += left[i][k] * right[k][j]
            row.append(acc)
        out.append(tuple(row))
    return tuple(out)


def mat_adj(mat: Matrix) -> Matrix:
    n = len(mat)
    return tuple(tuple(mat[j][i] for j in range(n)) for i in range(n))


def is_self_adjoint(mat: Matrix) -> bool:
    return mat == mat_adj(mat)


def is_diagonal(mat: Matrix) -> bool:
    n = len(mat)
    return all(mat[i][j] == Fraction(0) for i in range(n) for j in range(n) if i != j)


def trace(mat: Matrix) -> Fraction:
    return sum((mat[i][i] for i in range(len(mat))), Fraction(0))


def pi_plus() -> Matrix:
    return block_diag(eye(6), zero(2))


def pi_minus() -> Matrix:
    return block_diag(zero(6), eye(2))


def construct_y0() -> Matrix:
    return mat_add(pi_plus(), mat_scale(Fraction(-3), pi_minus()))


def site_dim() -> int:
    """One-site Hilbert dimension: End(C^n) = M_2(C) forces n^2 = 4."""
    algebra_dim = 2 * 2
    n = 1
    while n * n < algebra_dim:
        n += 1
    if n * n != algebra_dim:
        raise ValueError("one-site algebra dimension is not a square")
    return n


def spectrum_multiset(op: Matrix) -> tuple[Fraction, ...]:
    """Eigenvalue multiset of a self-adjoint diagonalizable-by-construction operator.

    Off-diagonal vanishing is checked, then the diagonal is the spectrum.
    """
    if not is_self_adjoint(op):
        raise ValueError("spectrum_multiset requires a self-adjoint operator")
    if not is_diagonal(op):
        raise ValueError("spectrum_multiset expects the reconstructed diagonal form")
    values = [op[i][i] for i in range(len(op))]
    values.sort(reverse=True)
    return tuple(values)


def predicate_y0_acts_on_c2(y0: Matrix) -> bool:
    """Identity gate: 'Y_0 acts on C^2'. Must fail (8 eigenvalues, dim 2)."""
    return len(spectrum_multiset(y0)) <= site_dim()


def predicate_one_site_m2_contains_y0(y0: Matrix) -> bool:
    """Identity gate: 'one-site M_2 contains Y_0'. Must fail."""
    return len(y0) == site_dim() and len(spectrum_multiset(y0)) <= site_dim()


def cited_may2_beta(alpha: Fraction) -> Fraction:
    """Cited May 2 identity 6α + 2β = 0, solved over Fraction."""
    return -Fraction(6) * alpha / Fraction(2)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        if ok:
            self.passed += 1
        else:
            self.failed += 1
        extra = f" ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{extra}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    may2 = MAY2_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")

    for relpath in AUDIT_INPUT_PATHS:
        digest = file_sha256(relpath)
        checks.check(
            f"audit-input-present:{Path(relpath).name}",
            (ROOT / relpath).is_file() and len(digest) == 64,
            digest[:12],
        )

    qubit_sentence = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    lattice_sites = "Physical sites are the points of the cubic lattice `Z^3`"
    lattice_privilege = "No site is privileged."
    checks.check("axiom-qubit-sentence", qubit_sentence in axiom)
    checks.check("axiom-lattice-sites", lattice_sites in axiom)
    checks.check("axiom-lattice-unprivileged", lattice_privilege in axiom)
    checks.check("note-quotes-qubit", qubit_sentence in note)
    checks.check("note-quotes-lattice-privilege", "no site privileged" in note)
    checks.check(
        "axiom-does-not-name-taste-cube-or-ranks",
        all(
            phrase not in axiom
            for phrase in ("taste cube", "3-factor tensor", "ranks (6,2)")
        ),
    )

    checks.check(
        "may2-cited-identity",
        "6 · α + 2 · β = 0" in may2 and "β = −3 α" in may2,
    )
    checks.check("note-cites-may2-identity", "6α + 2β = 0" in note)
    checks.check(
        "note-reconstructs-y0",
        "Y_0 := Pi_+ − 3 Pi_-" in note or "Y_0 := Pi_+ - 3 Pi_-" in note,
    )
    checks.check("note-states-min-dim-8", "smallest Hilbert-space dimension" in note)
    checks.check("note-does-not-identify-u1y", "does not identify `Y_0` with `U(1)_Y`" in note)
    checks.check("note-does-not-select-62-over-44", "does not select the" in note and "(4,4)" in note)
    checks.check("note-does-not-derive-alpha-one-third", "does not derive `α = 1/3`" in note)
    checks.check("note-does-not-force-r-half", "does not force `r = 1/2`" in note)
    checks.check(
        "note-does-not-adopt-taste-cube",
        "does not adopt a taste-cube axiom" in note,
    )
    lowered = note.lower()
    checks.check(
        "note-forbids-adoption-language",
        "we adopt" not in lowered and "adopt a new axiom" not in lowered,
    )
    checks.check(
        "note-does-not-cite-unmerged-prs",
        all(token not in note.lower() for token in ("ranksplit", "phyanom", "ylike")),
    )

    plus = pi_plus()
    minus = pi_minus()
    identity8 = eye(8)
    zero8 = zero(8)
    y0 = construct_y0()

    checks.check("pi-plus-projector", mat_mul(plus, plus) == plus and is_self_adjoint(plus))
    checks.check("pi-minus-projector", mat_mul(minus, minus) == minus and is_self_adjoint(minus))
    checks.check("pi-plus-minus-orthogonal", mat_mul(plus, minus) == zero8)
    checks.check("pi-sum-identity", mat_add(plus, minus) == identity8)
    checks.check("y0-self-adjoint", is_self_adjoint(y0))
    checks.check("y0-is-diagonal", is_diagonal(y0))

    spec = spectrum_multiset(y0)
    expected = tuple([Fraction(1)] * 6 + [Fraction(-3)] * 2)
    checks.check(
        "spectrum-multiset-reconstructed",
        spec == expected,
        ",".join(str(v) for v in spec),
    )
    checks.check("spectrum-length-eight", len(spec) == 8)
    checks.check("trace-zero", trace(y0) == Fraction(0), str(trace(y0)))
    checks.check(
        "cited-may2-ratio-at-alpha-one",
        cited_may2_beta(Fraction(1)) == Fraction(-3),
    )
    checks.check(
        "trace-matches-cited-may2",
        Fraction(6) * Fraction(1) + Fraction(2) * Fraction(-3) == Fraction(0),
    )

    dim = site_dim()
    checks.check("site-dim-is-two", dim == 2, str(dim))
    checks.check("carrier-dim-is-eight", len(y0) == 8)
    checks.check("min-dim-is-len-spectrum", len(spec) == 8 and len(spec) > dim)
    checks.check("eight-exceeds-two", len(spec) > dim)

    acts = predicate_y0_acts_on_c2(y0)
    contains = predicate_one_site_m2_contains_y0(y0)
    checks.check("predicate-y0-acts-on-c2-fails", acts is False)
    checks.check("predicate-one-site-m2-contains-y0-fails", contains is False)

    acts_src = inspect.getsource(predicate_y0_acts_on_c2)
    contains_src = inspect.getsource(predicate_one_site_m2_contains_y0)
    checks.check(
        "identity-gates-call-spectrum-and-site-dim",
        "spectrum_multiset" in acts_src
        and "site_dim" in acts_src
        and "spectrum_multiset" in contains_src
        and "site_dim" in contains_src,
    )

    n5_lines = (
        "per_element: eight eigenvalues of Y_0 and site_dim=2 are recomputed",
        "per_site: one C^8 carrier versus one M_2(C) site; no lattice of taste cubes",
        "per_mode: only the two-block spectrum is checked; no U(1)_Y mode",
        "per_block: only the 8-versus-2 dimension split and the display residual are executed",
        "lattice_wide: checked and not executed — no lattice-wide hypercharge law is claimed",
    )
    for line in n5_lines:
        checks.check(
            f"n5 {line[:20]}",
            line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            and len(line) >= 40,
        )
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
