#!/usr/bin/env python3
"""
Q1 source-endpoint / record-measure no-go.

This runner tests the narrowed next theorem after the physical-orientation
probe:

    Does the native C3 sharp record S = C + C^2 itself select the physical
    equal-atom measure, forward oriented channel, or selected-line basepoint?

Result:
  - C3 + S forces a two-atom sharp record with ranks (1, 2).
  - Equal-atom weights (the Q=2/3 lane) and rank/Born weights (the Q=1 lane)
    are both C3-invariant completions.  C3 + S does not choose between them.
  - S is reflection-even.  The reflection swaps forward/backward channels
    C <-> C^2, so any S-only or reflection-even source law cannot select the
    forward oriented channel.
  - The three endpoints form a free C3 orbit.  No unbased C3-equivariant
    endpoint selector exists.

No PDG masses, fitted selectors, observed lepton inputs, or unmerged PR
artifacts are used.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.splitlines():
            print(f"       {line}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def read_rel(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def matrix_unit(n: int, i: int, j: int) -> sp.Matrix:
    e = sp.zeros(n)
    e[i, j] = 1
    return e


BASIS8 = [
    (0, 0, 0),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 1),
]
INDEX8 = {alpha: idx for idx, alpha in enumerate(BASIS8)}
T1 = [INDEX8[(1, 0, 0)], INDEX8[(0, 1, 0)], INDEX8[(0, 0, 1)]]


def cycle_bits(alpha: tuple[int, int, int]) -> tuple[int, int, int]:
    a, b, c = alpha
    return (c, a, b)


def reflect_yz(alpha: tuple[int, int, int]) -> tuple[int, int, int]:
    a, b, c = alpha
    return (a, c, b)


def perm_matrix(basis: list[tuple[int, int, int]], transform) -> sp.Matrix:
    index = {alpha: idx for idx, alpha in enumerate(basis)}
    out = sp.zeros(len(basis))
    for j, alpha in enumerate(basis):
        out[index[transform(alpha)], j] = 1
    return out


def compress_t1(x: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([[sp.simplify(x[i, j]) for j in T1] for i in T1])


def avg_c3(u: sp.Matrix, x: sp.Matrix) -> sp.Matrix:
    out = sp.zeros(u.rows)
    uk = sp.eye(u.rows)
    for _ in range(3):
        out += uk * x * uk.T
        uk = u * uk
    return sp.simplify(out / 3)


def q_from_block_weights(mu: sp.Rational, nu: sp.Rational) -> tuple[sp.Expr, sp.Expr]:
    """Return (r*, Q) for block weights (singlet=mu, doublet=nu)."""
    r_star = sp.simplify(nu / (2 * mu))
    q_value = sp.simplify((1 + 2 * r_star) / 3)
    return r_star, q_value


def main() -> int:
    section("A. C3 + S forces the two sharp-record atoms but not their measure")

    c = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    c2 = c**2
    eye = sp.eye(3)
    s = c + c2
    p_singlet = sp.simplify((eye + c + c2) / 3)
    p_doublet = sp.simplify(eye - p_singlet)

    record(
        "A.1 C is an order-three faithful generation cycle",
        c**3 == eye and c != eye and c2 != eye,
        f"C={c}",
    )
    record(
        "A.2 S=C+C^2 has the sharp-record decomposition 2*P0 - P1",
        sp.simplify(s - (2 * p_singlet - p_doublet)) == sp.zeros(3),
        f"P0 rank={p_singlet.rank()}, P1 rank={p_doublet.rank()}",
    )
    record(
        "A.3 record projectors are orthogonal idempotents with ranks (1,2)",
        p_singlet**2 == p_singlet
        and p_doublet**2 == p_doublet
        and p_singlet * p_doublet == sp.zeros(3)
        and p_singlet.rank() == 1
        and p_doublet.rank() == 2,
        "The sharp S-record has two atoms, but unequal Hilbert ranks.",
    )
    record(
        "A.4 S has exactly two eigenvalues with multiplicities 1 and 2",
        s.eigenvals() == {sp.Integer(2): 1, sp.Integer(-1): 2},
        f"eigenvals={s.eigenvals()}",
    )

    p = sp.symbols("p", real=True)
    rho_p = sp.simplify(p * p_singlet + ((1 - p) / 2) * p_doublet)
    tau = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    atom_0 = sp.simplify(sp.trace(p_singlet * rho_p))
    atom_1 = sp.simplify(sp.trace(p_doublet * rho_p))
    rho_eigs = rho_p.eigenvals()

    record(
        "A.5 rho_p is a normalized C3- and reflection-invariant state family",
        sp.simplify(sp.trace(rho_p) - 1) == 0
        and sp.simplify(c * rho_p - rho_p * c) == sp.zeros(3)
        and sp.simplify(tau * rho_p * tau - rho_p) == sp.zeros(3),
        "rho_p = p P0 + ((1-p)/2) P1, valid positive for 0 <= p <= 1.",
    )
    record(
        "A.6 rho_p realizes arbitrary sharp-record atom weights",
        atom_0 == p
        and atom_1 == 1 - p
        and rho_eigs == {p: 1, sp.Rational(1, 2) - p / 2: 2},
        f"weights=(Tr P0 rho, Tr P1 rho)=({atom_0}, {atom_1}); eigs={rho_eigs}",
    )
    record(
        "A.7 equal atom and rank/Born weights are both C3-invariant completions",
        sp.simplify(rho_p.subs(p, sp.Rational(1, 3)) - eye / 3) == sp.zeros(3)
        and sp.simplify(sp.trace(p_singlet * rho_p.subs(p, sp.Rational(1, 2)))) == sp.Rational(1, 2)
        and sp.simplify(sp.trace(p_doublet * rho_p.subs(p, sp.Rational(1, 2)))) == sp.Rational(1, 2),
        "p=1/2 gives equal atom weights; p=1/3 gives I/3 and rank/Born weights (1/3,2/3).",
    )

    r_count, q_count = q_from_block_weights(sp.Rational(1), sp.Rational(1))
    r_rank, q_rank = q_from_block_weights(sp.Rational(1), sp.Rational(2))
    record(
        "A.8 the block-extremum algebra maps count to Q=2/3 and rank to Q=1",
        r_count == sp.Rational(1, 2)
        and q_count == sp.Rational(2, 3)
        and r_rank == sp.Integer(1)
        and q_rank == sp.Integer(1),
        f"(1,1): r={r_count}, Q={q_count}; (1,2): r={r_rank}, Q={q_rank}",
    )

    section("B. S-only data cannot select the forward oriented channel")

    a, b = sp.symbols("a b")
    s_span = a * eye + b * s
    no_s_solution_for_c = sp.linsolve(list(s_span - c), (a, b)) == sp.EmptySet
    odd_line = sp.I * (c - c2)

    record(
        "B.1 reflection mirrors C and C^2 while fixing S",
        tau * c * tau == c2 and tau * c2 * tau == c and tau * s * tau == s,
        "tau C tau = C^2, but tau S tau = S.",
    )
    record(
        "B.2 the oriented odd line is invisible to S-only data",
        tau * odd_line * tau == -odd_line
        and sp.simplify(sp.trace(s * odd_line)) == 0
        and sp.simplify(sp.trace(eye * odd_line)) == 0,
        "i(C-C^2) is reflection-odd; span{I,S} is reflection-even.",
    )
    record(
        "B.3 no polynomial in the sharp record S selects C over C^2",
        no_s_solution_for_c,
        "No a,b solve a*I + b*S = C.",
    )

    section("C. Full taste-cube source channels have the same reflection obstruction")

    u8 = perm_matrix(BASIS8, cycle_bits)
    tau8 = perm_matrix(BASIS8, reflect_yz)
    i100 = INDEX8[(1, 0, 0)]
    i010 = INDEX8[(0, 1, 0)]
    qf = sp.simplify(3 * avg_c3(u8, matrix_unit(8, i010, i100)))
    qb = sp.simplify(3 * avg_c3(u8, matrix_unit(8, i100, i010)))
    qodd = sp.I * (qf - qb)

    record(
        "C.1 the full-cube reflection reverses the C3 orientation",
        tau8 * u8 * tau8 == u8**2,
        "On T1, this is the same C <-> C^2 mirror.",
    )
    record(
        "C.2 full-cube forward/backward orbit sources descend to C and C^2",
        compress_t1(qf) == c and compress_t1(qb) == c2,
        "P1 Qf P1 = C, P1 Qb P1 = C^2.",
    )
    record(
        "C.3 reflection swaps full-cube Qf and Qb and flips the odd channel",
        tau8 * qf * tau8 == qb
        and tau8 * qb * tau8 == qf
        and tau8 * qodd * tau8 == -qodd,
        "A reflection-even source law cannot distinguish Qf from Qb.",
    )

    section("D. C3 has no unbased endpoint selector")

    endpoint_projectors = [matrix_unit(3, i, i) for i in range(3)]
    fixed_space = (c - eye).nullspace()
    fixed_vector = sp.Matrix([1, 1, 1])
    x0, x1, x2 = sp.symbols("x0 x1 x2")
    diagonal_solution = sp.solve(
        list(c * sp.diag(x0, x1, x2) * c.T - sp.diag(x0, x1, x2)),
        (x0, x1, x2),
        dict=True,
    )

    record(
        "D.1 no coordinate endpoint projector is C3-fixed",
        all(c * proj * c.T != proj for proj in endpoint_projectors),
        "The endpoint basis is a free C3 orbit.",
    )
    record(
        "D.2 the only fixed vector line is the symmetric singlet, not an endpoint",
        len(fixed_space) == 1 and fixed_space[0].cross(fixed_vector) == sp.zeros(3, 1),
        f"fixed_space={fixed_space}",
    )
    record(
        "D.3 a C3-invariant diagonal endpoint weight must be uniform",
        diagonal_solution == [{x0: x2, x1: x2}],
        "C3 invariance gives x0=x1=x2, not a selected endpoint.",
    )

    section("E. Repo boundary checks")

    physical_orientation = read_rel(
        "docs/KOIDE_Q1_PHYSICAL_ORIENTATION_BASEPOINT_PROBE_NOTE_2026-05-31.md"
    )
    selected_line_no_go = read_rel(
        "docs/CHARGED_LEPTON_SELECTED_LINE_GENERATION_SELECTOR_NO_GO_NOTE_2026-04-27.md"
    )
    taste_descent = read_rel("docs/KOIDE_TASTE_CUBE_CYCLIC_SOURCE_DESCENT_NOTE_2026-04-18.md")
    q1_closeout = read_rel(
        "docs/KOIDE_Q1_ORIENTED_SIGN_COMPATIBILITY_CLOSEOUT_NOTE_2026-05-31.md"
    )

    record(
        "E.1 current Q1 packet already leaves P_ORIENT full closure open",
        "P_ORIENT_FULL_CURRENT_SURFACE_CLOSURE=FALSE" in physical_orientation
        and "SELECTED_LINE_ENDPOINT_BASEPOINT_DERIVED=FALSE" in physical_orientation,
    )
    record(
        "E.2 selected-line no-go still requires a based endpoint or source law",
        "BASED_ENDPOINT_OR_SOURCE_LAW_REQUIRED=TRUE" in selected_line_no_go
        and "basepoint is additional physical data" in selected_line_no_go,
    )
    record(
        "E.3 taste-cube descent still leaves the microscopic source law open",
        "microscopic full-cube source law" in taste_descent
        and "does **not** yet derive" in taste_descent,
    )
    record(
        "E.4 oriented-frame Q1 sign compatibility is conditional on the missing law",
        "delta_oriented := -coeff_g(S_Q1) = +2/9" in q1_closeout
        and "Does not derive the physical selected-line slot/Fourier orientation."
        in q1_closeout,
    )

    section("F. Verdict")

    algebra_no_go = all(
        ok
        for name, ok, _ in PASSES
        if name.startswith("A.") or name.startswith("B.") or name.startswith("D.")
    )
    full_cube_no_go = all(ok for name, ok, _ in PASSES if name.startswith("C."))
    repo_boundary = all(ok for name, ok, _ in PASSES if name.startswith("E."))

    record(
        "F.1 C3 + S alone leaves the measure bit unforced",
        algebra_no_go,
        "Two atoms are forced; count-vs-rank/Born weighting is not.",
    )
    record(
        "F.2 full-cube Qf/Qb orientation requires an orientation-odd source law",
        full_cube_no_go,
        "Reflection swaps Qf and Qb.",
    )
    record(
        "F.3 current repo surface still lacks the selected endpoint/source law",
        repo_boundary,
        "The next theorem cannot be S-only; it must add a physical source/boundary principle.",
    )

    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print()
    print("=" * 88)
    print("Summary")
    print("=" * 88)
    print(f"PASSED: {n_pass}/{n_total}")
    for name, ok, _ in PASSES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print()
    if n_pass == n_total:
        print("VERDICT: C3/S record data do not derive measure, forward channel, or basepoint.")
        print("KOIDE_Q1_SOURCE_ENDPOINT_RECORD_MEASURE_NO_GO=TRUE")
        print("C3_SHARP_RECORD_FORCES_TWO_ATOMS=TRUE")
        print("C3_SHARP_RECORD_FORCES_WEIGHT_MEASURE=FALSE")
        print("EQUAL_ATOM_Q23_AND_RANK_BORN_Q1_BOTH_C3_INVARIANT=TRUE")
        print("S_RECORD_SELECTS_FORWARD_CHANNEL=FALSE")
        print("C3_ORBIT_SELECTS_BASEPOINT=FALSE")
        print("FULL_CUBE_REFLECTION_SWAPS_QF_QB=TRUE")
        print("MICROSCOPIC_FULL_CUBE_SOURCE_LAW_DERIVED=FALSE")
        print("SELECTED_LINE_ENDPOINT_BASEPOINT_DERIVED=FALSE")
        print("P_ORIENT_FULL_CURRENT_SURFACE_CLOSURE=FALSE")
        print("NEXT_HANDLE=derive_orientation_odd_source_boundary_law_or_measure_principle")
        return 0

    print("VERDICT: source-endpoint / record-measure no-go has failing checks.")
    print("KOIDE_Q1_SOURCE_ENDPOINT_RECORD_MEASURE_NO_GO=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
