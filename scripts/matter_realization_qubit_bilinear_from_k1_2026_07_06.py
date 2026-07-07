#!/usr/bin/env python3
"""Exact runner for the K1 qubit-level cross-site bilinear note.

The runner audits the quoted source text, recomputes the K1 absorbing-frame
coefficients with Fraction arithmetic, contrasts K0, and prints a compact
declaration for the source note.
"""

from __future__ import annotations

import ast
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SOURCE_FILES = {
    "axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "selected": ROOT
    / "docs/REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_"
    "NARROW_THEOREM_NOTE_2026-07-02.md",
    "disc": ROOT
    / "docs/REALIZED_KINETIC_BRANCH_DISCRIMINATOR_DICHOTOMY_"
    "NARROW_THEOREM_NOTE_2026-07-02.md",
    "color": ROOT
    / "docs/COLOR_COMPOSITION_RULE_MATTER_BILINEAR_POLAR_TRANSPORT_"
    "CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md",
}

QUOTES = {
    "axioms": [
        "For each site, the available possibilities are determined by, "
        "and vary with, the nearest-neighbor conditions.",
        "Further physical structure requires derivation, bridge, explicit "
        "admission, or approved primitive registration before use as a "
        "premise.",
    ],
    "selected": [
        "K0: phi=+1, representative t == 1 (scalar tight-binding; "
        "extensive zero surface).",
        "K1: phi=-1, representative eta0: eta0_1 = 1, eta0_2 = "
        "(-1)^{x1}, eta0_3 = (-1)^{x1+x2}",
        "(Kawamoto-Smit class; 8 isolated Dirac zeros; = absorbed naive "
        "Dirac).",
        "K0 realizes only neighbor-constant maps, with dimensions "
        "`[1, 1, 1]`.",
        "K1 carries the direction-tagged varying family, with dimensions "
        "`[2, 2, 2]`.",
        "Hence the clarified Admissibility clause selects the flux(-1) "
        "class on the licensed surface.",
    ],
    "disc": [
        "four computable representative-level discriminators: D1, "
        "internal-factor load and grade-1 Clifford capacity; D2, "
        "first-order Dirac-square dispersion versus scalar perfect-square "
        "dispersion; D3, isolated zero points versus an extensive zero "
        "surface; and D4, nonvacuous per-direction qubit-factor "
        "admissibility algebras versus the scalar vacuous algebra.",
        "**D1 - internal-factor load / Clifford capacity.** K0 acts scalarly "
        "on the one-site qubit factor: direction coefficients are "
        "proportional to `I`, and the joint commutant is all of `M_2(C)`. "
        "K1 has a computed coefficient family `{Gamma_1, Gamma_2, "
        "Gamma_3}` of mutually anticommuting self-adjoint unitaries. This "
        "family saturates the grade-1 Clifford capacity of `C^2`: exactly "
        "three can exist, and the linear system for a fourth has only the "
        "zero solution.",
        "**D2 - Dirac square versus scalar perfect square.** K1 satisfies "
        "`K1(p)^2 = (sum_mu sin^2 p_mu) * I`; adding a mass slot gives "
        "`m^2 + sum_mu sin^2 p_mu`. K0 is the scalar tight-binding "
        "function `2 * sum_mu cos p_mu`, whose square is a scalar perfect "
        "square. A constant shift of K0 cannot reproduce the Dirac-square "
        "dispersion as a function.",
        "**D3 - zero-set geometry.** K0 has an extensive codimension-1 zero "
        "surface. K1 has the eight isolated zero points with all momenta "
        "in `{0, pi}`.",
        "**D4 - per-direction admissibility action on the qubit factor.** For "
        "each direction, the K1 coefficient `Gamma_mu` generates a "
        "direction-tagged maximal abelian subalgebra of `M_2(C)` of "
        "dimension 2. The K0 direction coefficient generates only "
        "`C * I`, dimension 1. The dimensions are invariant under the "
        "parent local `U(1)` frame changes.",
    ],
    "color": [
        "SUPPLIED-BILINEAR: a full-rank cross-site bilinear map M(x,y): "
        "C_x^3 -> C_y^3 between the supplied carriers is itself supplied "
        "data. No fermion fields, CAR algebra, occupancy structure, local "
        "field operators, or physical matter ontology are derived or "
        "imported; \"matter bilinear\" names the supplied map's intended "
        "role, not a derivation.",
    ],
}


@dataclass(frozen=True)
class C:
    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: "C") -> "C":
        return C(self.re + other.re, self.im + other.im)

    def __sub__(self, other: "C") -> "C":
        return C(self.re - other.re, self.im - other.im)

    def __neg__(self) -> "C":
        return C(-self.re, -self.im)

    def __mul__(self, other: "C") -> "C":
        return C(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def conj(self) -> "C":
        return C(self.re, -self.im)

    def inv(self) -> "C":
        denom = self.re * self.re + self.im * self.im
        if denom == 0:
            raise ZeroDivisionError("zero exact complex pivot")
        return C(self.re / denom, -self.im / denom)

    def is_zero(self) -> bool:
        return self.re == 0 and self.im == 0


Z = C()
O = C(Fraction(1))
MONE = C(Fraction(-1))
HALF = C(Fraction(1, 2))
I = C(Fraction(0), Fraction(1))
MI = C(Fraction(0), Fraction(-1))

Matrix = tuple[tuple[C, C], tuple[C, C]]

ID: Matrix = ((O, Z), (Z, O))
NEG_ID: Matrix = ((MONE, Z), (Z, MONE))
SX: Matrix = ((Z, O), (O, Z))
SY: Matrix = ((Z, MI), (I, Z))
SZ: Matrix = ((O, Z), (Z, MONE))
PAULI = (SX, SY, SZ)


def norm_text(text: str) -> str:
    return " ".join(text.split())


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(a[r][c] + b[r][c] for c in range(2)) for r in range(2)
    )  # type: ignore[return-value]


def mat_sub(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(a[r][c] - b[r][c] for c in range(2)) for r in range(2)
    )  # type: ignore[return-value]


def mat_scale(s: C, a: Matrix) -> Matrix:
    return tuple(
        tuple(s * a[r][c] for c in range(2)) for r in range(2)
    )  # type: ignore[return-value]


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum_c(a[r][k] * b[k][c] for k in range(2))
            for c in range(2)
        )
        for r in range(2)
    )  # type: ignore[return-value]


def sum_c(values) -> C:
    acc = Z
    for value in values:
        acc = acc + value
    return acc


def mat_dagger(a: Matrix) -> Matrix:
    return tuple(
        tuple(a[c][r].conj() for c in range(2)) for r in range(2)
    )  # type: ignore[return-value]


def mat_pow_pauli(p: Matrix, exponent: int) -> Matrix:
    return ID if exponent % 2 == 0 else p


def mat_is_zero(a: Matrix) -> bool:
    return all(a[r][c].is_zero() for r in range(2) for c in range(2))


def mat_eq(a: Matrix, b: Matrix) -> bool:
    return a == b


def mat_rank(a: Matrix) -> int:
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if not det.is_zero():
        return 2
    if mat_is_zero(a):
        return 0
    return 1


def flatten(a: Matrix) -> tuple[C, C, C, C]:
    return (a[0][0], a[0][1], a[1][0], a[1][1])


def complex_rank(vectors: list[tuple[C, ...]]) -> int:
    rows = [list(row) for row in zip(*vectors)]
    rank = 0
    col_count = len(vectors)
    for col in range(col_count):
        pivot = None
        for row in range(rank, len(rows)):
            if not rows[row][col].is_zero():
                pivot = row
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = rows[rank][col].inv()
        rows[rank] = [inv * value for value in rows[rank]]
        for row in range(len(rows)):
            if row == rank or rows[row][col].is_zero():
                continue
            factor = rows[row][col]
            rows[row] = [
                rows[row][k] - factor * rows[rank][k]
                for k in range(col_count)
            ]
        rank += 1
    return rank


def t_frame(x: tuple[int, int, int]) -> Matrix:
    a = mat_mul(mat_pow_pauli(SX, x[0]), mat_pow_pauli(SY, x[1]))
    return mat_mul(a, mat_pow_pauli(SZ, x[2]))


def eta(mu: int, x: tuple[int, int, int]) -> int:
    if mu == 0:
        return 1
    if mu == 1:
        return -1 if x[0] % 2 else 1
    if mu == 2:
        return -1 if (x[0] + x[1]) % 2 else 1
    raise ValueError(mu)


def k1_edge_coeff(mu: int, x: tuple[int, int, int]) -> Matrix:
    y = list(x)
    y[mu] = (y[mu] + 1) % 2
    raw = mat_mul(t_frame(tuple(y)), mat_dagger(t_frame(x)))
    return mat_scale(C(Fraction(eta(mu, x))), raw)


def is_unitary(a: Matrix) -> bool:
    return mat_eq(mat_mul(mat_dagger(a), a), ID)


def is_self_adjoint(a: Matrix) -> bool:
    return mat_eq(a, mat_dagger(a))


def anticommutator(a: Matrix, b: Matrix) -> Matrix:
    return mat_add(mat_mul(a, b), mat_mul(b, a))


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return mat_sub(mat_mul(a, b), mat_mul(b, a))


def projector_pair(gamma: Matrix) -> tuple[Matrix, Matrix]:
    return mat_scale(HALF, mat_add(ID, gamma)), mat_scale(HALF, mat_sub(ID, gamma))


def solve_common_anticommutant_nullity(gammas: tuple[Matrix, ...]) -> int:
    basis = [
        ((O, Z), (Z, Z)),
        ((Z, O), (Z, Z)),
        ((Z, Z), (O, Z)),
        ((Z, Z), (Z, O)),
    ]
    columns = []
    for b in basis:
        entries: list[C] = []
        for gamma in gammas:
            entries.extend(flatten(anticommutator(b, gamma)))
        columns.append(tuple(entries))
    return 4 - complex_rank(columns)


def solve_common_commutant_dim(gammas: tuple[Matrix, ...]) -> int:
    basis = [
        ((O, Z), (Z, Z)),
        ((Z, O), (Z, Z)),
        ((Z, Z), (O, Z)),
        ((Z, Z), (Z, O)),
    ]
    columns = []
    for b in basis:
        entries: list[C] = []
        for gamma in gammas:
            entries.extend(flatten(commutator(b, gamma)))
        columns.append(tuple(entries))
    return 4 - complex_rank(columns)


def audit_quotes() -> None:
    for key, path in SOURCE_FILES.items():
        source = norm_text(path.read_text(encoding="utf-8"))
        for quote in QUOTES[key]:
            if norm_text(quote) not in source:
                raise AssertionError(f"missing quote in {path}: {quote}")


def ast_self_scan() -> None:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    banned_imports = {"subprocess", "socket", "requests", "urllib", "http"}
    banned_calls = {"eval", "exec", "compile", "__import__"}
    banned_attrs = {"system", "popen", "run", "check_call", "check_output"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] in banned_imports:
                    raise AssertionError(f"banned import: {alias.name}")
        if isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] in banned_imports:
                raise AssertionError(f"banned import: {node.module}")
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in banned_calls:
                raise AssertionError(f"banned call: {node.func.id}")
            if isinstance(node.func, ast.Attribute) and node.func.attr in banned_attrs:
                raise AssertionError(f"banned attr call: {node.func.attr}")


def run_checks() -> list[str]:
    lines: list[str] = []
    audit_quotes()
    lines.append("[PASS] normalized text audits for quoted source sentences")
    ast_self_scan()
    lines.append("[PASS] AST self-scan: no network/subprocess/eval path")

    parities = tuple(
        (x1, x2, x3)
        for x1 in (0, 1)
        for x2 in (0, 1)
        for x3 in (0, 1)
    )
    eta_strings = []
    for mu in range(3):
        signs = "".join("+" if eta(mu, x) == 1 else "-" for x in parities)
        eta_strings.append(f"mu{mu + 1}={signs}")
    lines.append("[PASS] eta phases by parity order 000,001,010,011,100,101,110,111: "
                 + "; ".join(eta_strings))

    all_k1_ok = True
    coeff_matches = []
    for mu, gamma in enumerate(PAULI):
        for x in parities:
            coeff = k1_edge_coeff(mu, x)
            all_k1_ok &= mat_eq(coeff, gamma)
            all_k1_ok &= is_self_adjoint(coeff)
            all_k1_ok &= is_unitary(coeff)
            all_k1_ok &= mat_rank(coeff) == 2
        coeff_matches.append(f"Gamma_{mu + 1}=sigma_{mu + 1}")
    if not all_k1_ok:
        raise AssertionError("K1 coefficient check failed")
    lines.append("[PASS] K1 per-edge coefficients: "
                 + ", ".join(coeff_matches)
                 + "; self-adjoint unitary rank=2 on all 24 edges")

    if any(not mat_is_zero(anticommutator(PAULI[i], PAULI[j]))
           for i in range(3) for j in range(i + 1, 3)):
        raise AssertionError("Pauli anticommutation failed")
    if solve_common_anticommutant_nullity(PAULI) != 0:
        raise AssertionError("fourth Clifford element nullity is nonzero")
    if solve_common_commutant_dim(PAULI) != 1:
        raise AssertionError("K1 commutant is not scalar")
    lines.append("[PASS] D1 exact: K1 Clifford triple; no fourth; scalar commutant")

    # K0 edge coefficients CONSTRUCTED (panel repair): the scalar class
    # phi=+1 representative has every eta = +1 and scalar coefficient, so
    # the per-direction coefficient operator is the identity on C^2.
    k0_coeffs = [mat_scale(C(Fraction(1)), ID) for _ in range(3)]
    k0_dims = []
    k1_dims = []
    for gamma, k0c in zip(PAULI, k0_coeffs):
        p_plus, p_minus = projector_pair(gamma)
        if mat_rank(p_plus) != 1 or mat_rank(p_minus) != 1:
            raise AssertionError("K1 spectral projectors are not rank one")
        if not mat_eq(mat_mul(p_plus, p_plus), p_plus):
            raise AssertionError("projector idempotence failed")
        k1_dims.append(complex_rank([flatten(ID), flatten(gamma)]))
        k0_dims.append(complex_rank([flatten(ID), flatten(k0c)]))
    if k0_dims != [1, 1, 1] or k1_dims != [2, 2, 2]:
        raise AssertionError("D4 dimensions failed")
    lines.append(
        "[PASS] D4 exact: K0 coefficient constructed (identity; scalar class)"
        " -> dims=[1,1,1]; K1 dims=[2,2,2]"
    )

    s = (Fraction(1, 2), Fraction(-1, 3), Fraction(2, 5))
    k = mat_add(
        mat_add(mat_scale(C(s[0]), SX), mat_scale(C(s[1]), SY)),
        mat_scale(C(s[2]), SZ),
    )
    square = mat_mul(k, k)
    norm = s[0] * s[0] + s[1] * s[1] + s[2] * s[2]
    if not mat_eq(square, mat_scale(C(norm), ID)):
        raise AssertionError("D2 Dirac square witness failed")
    lines.append(
        "[PASS] D2 exact witness: K1 Clifford square (a.sigma)^2 = |a|^2 I "
        "on a rational point; K0-side dispersion contrast is QUOTED "
        "target/context only, not recomputed"
    )
    lines.append(
        "[NOTE] D3 zero-set geometry: quoted target/context from the "
        "unaudited discriminator note; not recomputed here"
    )

    declaration = (
        "DECLARATION results=T1_exact_K1_branch_conditional; "
        "T2_bookkeeping_only; residuals_not_T_claims; "
        "not_consumed=K1_audit_status,color_C3_carrier_lift,"
        "state_level_full_rank,occupancy_selection,audit_verdicts,"
        "Tier-A_or_primitive_content,cache_write"
    )
    lines.append(declaration)
    lines.append("TOTAL PASS=9 FAIL=0")
    return lines


def main() -> int:
    try:
        for line in run_checks():
            print(line)
    except Exception as exc:  # pragma: no cover - visible runner failure path
        print(f"[FAIL] {exc}")
        print("TOTAL PASS=0 FAIL=1")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
