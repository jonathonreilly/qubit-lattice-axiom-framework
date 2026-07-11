#!/usr/bin/env python3
"""Y_T color-projection matching no-go runner.

Authority note:
    docs/YT_COLOR_PROJECTION_CORRECTION_NOTE.md

The runner checks the repaired claim:

    K_Y(kappa_Y) = F_adj + kappa_Y * F_singlet
                 = 8/9 + kappa_Y/9  at N_c = 3.

The cited exact Fierz/projection packet fixes F_adj and F_singlet, but it
does not select kappa_Y = 0. The runner also distinguishes two operations that
the historical argument conflated:

    rank(P_adj) / dim End(C^N) = (N^2 - 1) / N^2,
    P_adj(I) = 0.

Thus the adjoint subspace occupies an 8/9 dimension fraction at N=3 while the
specific color-singlet scalar insertion has zero adjoint projection. A scalar
LSZ residue would require an additional dynamical matching map; it is not the
rank of the color projector.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "YT_COLOR_PROJECTION_CORRECTION_NOTE.md"
FIERZ = DOCS / "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(name: str, passed: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if passed:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def f_adj(n_c: int) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def f_singlet(n_c: int) -> Fraction:
    return Fraction(1, n_c * n_c)


def k_y(n_c: int, kappa_y: Fraction) -> Fraction:
    return f_adj(n_c) + kappa_y * f_singlet(n_c)


Matrix = tuple[tuple[Fraction, ...], ...]


def zero_matrix(n: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(n)) for _ in range(n))


def identity_matrix(n: int) -> Matrix:
    return tuple(
        tuple(Fraction(1) if i == j else Fraction(0) for j in range(n))
        for i in range(n)
    )


def matrix_unit(n: int, row: int, col: int) -> Matrix:
    return tuple(
        tuple(Fraction(1) if (i, j) == (row, col) else Fraction(0) for j in range(n))
        for i in range(n)
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(len(left)))
        for i in range(len(left))
    )


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(len(left)))
        for i in range(len(left))
    )


def matrix_scale(scale: Fraction, matrix: Matrix) -> Matrix:
    return tuple(tuple(scale * entry for entry in row) for row in matrix)


def matrix_mul(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(n)) for j in range(n))
        for i in range(n)
    )


def matrix_trace(matrix: Matrix) -> Fraction:
    return sum(matrix[i][i] for i in range(len(matrix)))


def matrix_flatten(matrix: Matrix) -> tuple[Fraction, ...]:
    return tuple(entry for row in matrix for entry in row)


def hs_norm_sq(matrix: Matrix) -> Fraction:
    # All exact test matrices are real, so transpose and Hermitian norms agree.
    return sum(entry * entry for row in matrix for entry in row)


def p_singlet(matrix: Matrix) -> Matrix:
    n = len(matrix)
    return matrix_scale(matrix_trace(matrix) / n, identity_matrix(n))


def p_adjoint(matrix: Matrix) -> Matrix:
    return matrix_sub(matrix, p_singlet(matrix))


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return matrix_sub(matrix_mul(left, right), matrix_mul(right, left))


def rational_rank(rows: list[list[Fraction]]) -> int:
    """Exact Gaussian-elimination rank over Q."""
    if not rows:
        return 0
    work = [row[:] for row in rows]
    n_rows = len(work)
    n_cols = len(work[0])
    pivot_row = 0
    for col in range(n_cols):
        pivot = next((r for r in range(pivot_row, n_rows) if work[r][col] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][col]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row_index in range(n_rows):
            if row_index == pivot_row or work[row_index][col] == 0:
                continue
            factor = work[row_index][col]
            work[row_index] = [
                work[row_index][j] - factor * work[pivot_row][j]
                for j in range(n_cols)
            ]
        pivot_row += 1
        if pivot_row == n_rows:
            break
    return pivot_row


def linear_map_rank(n: int, linear_map) -> int:
    columns = [
        matrix_flatten(linear_map(matrix_unit(n, row, col)))
        for row in range(n)
        for col in range(n)
    ]
    rows = [list(row) for row in zip(*columns)]
    return rational_rank(rows)


def commutant_dimension(n: int, require_traceless: bool = False) -> int:
    """Dimension of matrices commuting with generators of sl_N.

    Off-diagonal matrix units plus adjacent traceless diagonal matrices span
    the complexified Lie algebra. Their commutant is the scalar line; adding a
    trace-zero constraint removes that line.
    """
    generators: list[Matrix] = []
    for row in range(n):
        for col in range(n):
            if row != col:
                generators.append(matrix_unit(n, row, col))
    for index in range(n - 1):
        generators.append(
            matrix_sub(matrix_unit(n, index, index), matrix_unit(n, index + 1, index + 1))
        )

    variables = [matrix_unit(n, row, col) for row in range(n) for col in range(n)]
    constraint_rows: list[list[Fraction]] = []
    for generator in generators:
        columns = [matrix_flatten(commutator(variable, generator)) for variable in variables]
        constraint_rows.extend([list(row) for row in zip(*columns)])
    if require_traceless:
        constraint_rows.append([matrix_trace(variable) for variable in variables])
    return n * n - rational_rank(constraint_rows)


@dataclass(frozen=True)
class Completion:
    n_c: int
    kappa_y: Fraction
    color_blind_scale: Fraction

    @property
    def c(self) -> Fraction:
        return f_adj(self.n_c)

    @property
    def s(self) -> Fraction:
        return f_singlet(self.n_c)

    @property
    def scaled_c(self) -> Fraction:
        return self.color_blind_scale * self.c

    @property
    def scaled_s(self) -> Fraction:
        return self.color_blind_scale * self.s

    @property
    def k_unscaled(self) -> Fraction:
        return self.c + self.kappa_y * self.s

    @property
    def k_scaled_normalized(self) -> Fraction:
        return (self.scaled_c + self.kappa_y * self.scaled_s) / self.color_blind_scale

    @property
    def primitive_signature(self) -> tuple[Fraction, Fraction, Fraction, Fraction]:
        return (
            self.c,
            self.s,
            self.scaled_c / self.c,
            self.scaled_s / self.s,
        )


def rho_singlet(matrix: Matrix) -> Fraction:
    norm = hs_norm_sq(matrix)
    if norm == 0:
        raise ValueError("singlet fraction is undefined for the zero insertion")
    return hs_norm_sq(p_singlet(matrix)) / norm


def rho_singlet_identity(n_c: int) -> Fraction:
    return rho_singlet(identity_matrix(n_c))


def rho_singlet_traceless(n_c: int) -> Fraction:
    witness = matrix_sub(matrix_unit(n_c, 0, 0), matrix_unit(n_c, 1, 1))
    return rho_singlet(witness)


def scalar_source_matrix(n_c: int, h: Fraction, vacuum_shift: Fraction) -> Matrix:
    return matrix_scale(h - vacuum_shift, identity_matrix(n_c))


def main() -> int:
    print("=" * 78)
    print("Y_T COLOR-PROJECTION MATCHING NO-GO")
    print("=" * 78)

    note = read(NOTE)
    fierz = read(FIERZ)

    print("\nPart 0: source and authority anchors")
    check("source note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    check("Fierz authority exists", FIERZ.exists(), str(FIERZ.relative_to(ROOT)))
    check("source note is typed no_go", "**Claim type:** no_go" in note)
    check("source note registers this runner", "scripts/frontier_yt_color_projection_correction.py" in note)
    check(
        "source links the load-bearing Fierz authority",
        "](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)" in note
    )
    check(
        "Fierz authority exposes the adjoint channel fraction",
        "8/9" in fierz and "adjoint-channel fraction" in fierz,
    )
    check(
        "projection guardrail is non-load-bearing context",
        "Plain-text context, not load-bearing authority" in note
        and "`RCONN_VERTEX_COLOR_SINGLET_PROJECTION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md`" in note,
    )

    print("\nPart 1: exact channel fractions")
    for n_c in (2, 3, 4, 5, 10):
        c = f_adj(n_c)
        s = f_singlet(n_c)
        check(f"N_c={n_c}: F_adj + F_singlet = 1", c + s == 1, f"{c} + {s}")
        check(f"N_c={n_c}: F_adj = (N_c^2-1)/N_c^2", c == Fraction(n_c * n_c - 1, n_c * n_c), str(c))
    check("N_c=3 gives F_adj=8/9", f_adj(3) == Fraction(8, 9), str(f_adj(3)))
    check("N_c=3 gives F_singlet=1/9", f_singlet(3) == Fraction(1, 9), str(f_singlet(3)))

    print("\nPart 2: corrected conditional family")
    check("K_Y(0)=8/9", k_y(3, Fraction(0)) == Fraction(8, 9), str(k_y(3, Fraction(0))))
    check("K_Y(1)=1", k_y(3, Fraction(1)) == Fraction(1), str(k_y(3, Fraction(1))))
    check("K_Y(1/2)=17/18", k_y(3, Fraction(1, 2)) == Fraction(17, 18), str(k_y(3, Fraction(1, 2))))
    check(
        "source states corrected K_Y formula",
        "K_Y(kappa_Y) = F_adj + kappa_Y * F_singlet" in note
        and "8/9 + kappa_Y/9" in note,
    )
    check(
        "source avoids stale reversed K_Y formula",
        "1/9 + 8 kappa_Y/9" not in note and "1/9 + kappa_Y * 8/9" not in note,
    )

    print("\nPart 3: two-completion independence witness")
    connected = Completion(n_c=3, kappa_y=Fraction(0), color_blind_scale=Fraction(77, 100))
    full_trace = Completion(n_c=3, kappa_y=Fraction(1), color_blind_scale=Fraction(77, 100))
    half_trace = Completion(n_c=3, kappa_y=Fraction(1, 2), color_blind_scale=Fraction(77, 100))
    check(
        "kappa=0 and kappa=1 share the cited channel-data signature",
        connected.primitive_signature == full_trace.primitive_signature,
        str(connected.primitive_signature),
    )
    check(
        "kappa=0 and kappa=1 disagree on K_Y",
        connected.k_unscaled != full_trace.k_unscaled,
        f"{connected.k_unscaled} != {full_trace.k_unscaled}",
    )
    for model in (connected, full_trace, half_trace):
        check(
            f"color-blind scaling cancels at kappa={model.kappa_y}",
            model.k_scaled_normalized == model.k_unscaled,
            f"scaled={model.k_scaled_normalized}, unscaled={model.k_unscaled}",
        )

    print("\nPart 4: vertex-projection guardrail")
    check("rho_singlet(I_color)=1", rho_singlet_identity(3) == Fraction(1))
    check("rho_singlet(traceless generator)=0", rho_singlet_traceless(3) == Fraction(0))
    check(
        "identity insertion would give K_Y=1 if kappa_Y=rho_singlet",
        k_y(3, rho_singlet_identity(3)) == Fraction(1),
        str(k_y(3, rho_singlet_identity(3))),
    )
    check(
        "traceless insertion would give K_Y=8/9 if kappa_Y=rho_singlet",
        k_y(3, rho_singlet_traceless(3)) == Fraction(8, 9),
        str(k_y(3, rho_singlet_traceless(3))),
    )

    print("\nPart 5: projector rank is not projector action")
    for n_c in (2, 3, 4, 5):
        ident = identity_matrix(n_c)
        singlet_rank = linear_map_rank(n_c, p_singlet)
        adjoint_rank = linear_map_rank(n_c, p_adjoint)
        check(
            f"N_c={n_c}: singlet projector has rank 1",
            singlet_rank == 1,
            f"rank={singlet_rank}",
        )
        check(
            f"N_c={n_c}: adjoint projector has rank N_c^2-1",
            adjoint_rank == n_c * n_c - 1,
            f"rank={adjoint_rank}",
        )
        check(
            f"N_c={n_c}: adjoint projector rank fraction equals F_adj",
            Fraction(adjoint_rank, n_c * n_c) == f_adj(n_c),
            f"{adjoint_rank}/{n_c*n_c}={Fraction(adjoint_rank, n_c*n_c)}",
        )
        check(
            f"N_c={n_c}: P_singlet(I)=I",
            p_singlet(ident) == ident,
        )
        check(
            f"N_c={n_c}: P_adjoint(I)=0",
            p_adjoint(ident) == zero_matrix(n_c),
        )
        matrix_units = [
            matrix_unit(n_c, row, col)
            for row in range(n_c)
            for col in range(n_c)
        ]
        check(
            f"N_c={n_c}: projector completeness on every matrix unit",
            all(matrix_add(p_singlet(basis), p_adjoint(basis)) == basis for basis in matrix_units),
        )
        check(
            f"N_c={n_c}: P_adj idempotent on every matrix unit",
            all(p_adjoint(p_adjoint(basis)) == p_adjoint(basis) for basis in matrix_units),
        )

    # The dimension fraction is also the mean adjoint projection energy of an
    # orthonormal matrix-unit basis. That average statement does not determine
    # the projection energy of the specific identity insertion.
    for n_c in (2, 3, 4, 5):
        basis_adjoint_energy = sum(
            hs_norm_sq(p_adjoint(matrix_unit(n_c, row, col)))
            for row in range(n_c)
            for col in range(n_c)
        )
        mean_adjoint_energy = basis_adjoint_energy / (n_c * n_c)
        identity_adjoint_fraction = (
            hs_norm_sq(p_adjoint(identity_matrix(n_c)))
            / hs_norm_sq(identity_matrix(n_c))
        )
        check(
            f"N_c={n_c}: isotropic basis mean gives F_adj",
            mean_adjoint_energy == f_adj(n_c),
            str(mean_adjoint_energy),
        )
        check(
            f"N_c={n_c}: identity insertion adjoint fraction is zero, not F_adj",
            identity_adjoint_fraction == 0 and identity_adjoint_fraction != f_adj(n_c),
            f"identity={identity_adjoint_fraction}, rank_fraction={f_adj(n_c)}",
        )

    print("\nPart 6: equivariant scalar-source obstruction")
    for n_c in (2, 3, 4, 5):
        invariant_dimension = commutant_dimension(n_c)
        traceless_invariant_dimension = commutant_dimension(n_c, require_traceless=True)
        check(
            f"N_c={n_c}: invariant insertion space is the scalar line",
            invariant_dimension == 1,
            f"dimension={invariant_dimension}",
        )
        check(
            f"N_c={n_c}: no nonzero invariant traceless insertion",
            traceless_invariant_dimension == 0,
            f"dimension={traceless_invariant_dimension}",
        )
        h = Fraction(7, 5)
        delta = Fraction(1, 11)
        vacuum_shift = Fraction(2, 3)
        source_tangent = matrix_scale(
            Fraction(1, 1) / delta,
            matrix_sub(
                scalar_source_matrix(n_c, h + delta, vacuum_shift),
                scalar_source_matrix(n_c, h, vacuum_shift),
            ),
        )
        check(
            f"N_c={n_c}: shifted scalar source has identity finite-difference tangent",
            source_tangent == identity_matrix(n_c)
            and p_adjoint(source_tangent) == zero_matrix(n_c)
            and p_singlet(source_tangent) == source_tangent,
        )

    check(
        "source states rank-versus-action obstruction",
        "rank fraction of the adjoint projector" in note
        and "P_adj(I_color) = 0" in note,
    )
    check(
        "source states scalar-to-adjoint equivariant-map obstruction",
        "Hom_SU(N_c)(1, adj) = 0" in note,
    )
    check(
        "source distinguishes connected cumulant from traceless color projection",
        "connected cumulant" in note and "source tangent" in note,
    )

    print("\nPart 7: overclaim guards")
    forbidden = [
        "The framework derives the `sqrt(8/9)` correction",
        "ALL CHECKS PASSED",
        "m_t(pole, 2-loop) within",
        "Z_phi = Sigma_connected / Sigma_total = R_conn",
    ]
    for phrase in forbidden:
        check(f"source avoids overclaim phrase {phrase!r}", phrase not in note)
    required = [
        "not a derived theorem",
        "conditional support only",
        "derive kappa_Y = 0",
        "No-Go Discipline Gate",
        "Status:** PASS",
        "rank fraction of the adjoint projector",
        "specific scalar insertion",
        "dynamical scalar two-point",
    ]
    for phrase in required:
        check(f"source contains boundary phrase {phrase!r}", phrase in note)

    print()
    print("=" * 78)
    print(f"RESULT: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
