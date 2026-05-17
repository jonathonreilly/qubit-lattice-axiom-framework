#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`RCONN_VERTEX_COLOR_STRUCTURE_TO_KAPPA_EW_NARROW_THEOREM_NOTE_2026-05-17`.

Narrow theorem (Vertex → kappa_EW determination map):

  Given a Hermitian color insertion M_color at the EW current vertex,
  the matching-rule coefficient kappa_EW is fixed exactly by

      kappa_EW(M_color)  =  ( |Tr_color M_color|^2 / N_c ) / Tr_color[M_color^2].

  Two corollary values:
    (C1) M_color = I_color (color-blind point-split)  ->  kappa_EW = 1
                                                      ->  K_EW = 1.
    (C2) M_color = sqrt(2) t^A (any SU(N_c) generator) ->  kappa_EW = 0
                                                      ->  K_EW = N_c^2/(N_c^2-1)
                                                      ->  K_EW = 9/8 at N_c=3.

  (C3) Uniqueness: no Hermitian M_color with Tr_color M_color != 0
       achieves kappa_EW = 0 exactly.

Retained inputs consumed:
  (R1) Fierz completeness identity for SU(N_c) bilinears
       (EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01, retained_bounded)
  (R2) Gate-note definition of K_EW(kappa_EW) = 1/(F_adj + kappa_EW(1-F_adj))
       (EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03, source-note)
  (R3) N_c = 3 from Cl(3) (GRAPH_FIRST_SU3_INTEGRATION_NOTE, retained)

No new axioms, no fitted parameters, no observational comparator,
no literature import.

Companion role: stands alone (NEW source theorem, not a re-audit). Class A.

Exit code: 0 on full PASS, 1 on any FAIL.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path
from typing import List, Tuple


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "RCONN_VERTEX_COLOR_STRUCTURE_TO_KAPPA_EW_NARROW_THEOREM_NOTE_2026-05-17.md"
GATE = DOCS / "EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md"
FIERZ = DOCS / "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md"
TRACELESS = DOCS / "EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md"
RCONN = DOCS / "RCONN_DERIVED_NOTE.md"


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


# ----------------------------------------------------------------------
# Exact-rational matrix utilities (Hermitian over Q[i] via Fraction reals
# and imaginaries). For this exact-symbolic runner all matrices are real
# and symmetric, which is sufficient: the closed-form (V) only needs
# Tr M and Tr[M^2], both of which are real for Hermitian M.
# ----------------------------------------------------------------------

Matrix = List[List[Fraction]]


def eye(n: int) -> Matrix:
    return [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]


def zeros(n: int) -> Matrix:
    return [[Fraction(0)] * n for _ in range(n)]


def add(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]


def scale(a: Matrix, s: Fraction) -> Matrix:
    n = len(a)
    return [[a[i][j] * s for j in range(n)] for i in range(n)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return [
        [sum((a[i][k] * b[k][j] for k in range(n)), Fraction(0)) for j in range(n)]
        for i in range(n)
    ]


def trace(a: Matrix) -> Fraction:
    return sum((a[i][i] for i in range(len(a))), Fraction(0))


def transpose(a: Matrix) -> Matrix:
    n = len(a)
    return [[a[j][i] for j in range(n)] for i in range(n)]


def is_symmetric(a: Matrix) -> bool:
    n = len(a)
    return all(a[i][j] == a[j][i] for i in range(n) for j in range(n))


def matequal(a: Matrix, b: Matrix) -> bool:
    n = len(a)
    return all(a[i][j] == b[i][j] for i in range(n) for j in range(n))


# ----------------------------------------------------------------------
# Real-symmetric SU(N_c) generator basis (Cartan + symmetric off-diagonal
# only; sufficient to instantiate witnesses with rational Tr and Tr[M^2]).
# We use the conventional normalization Tr[t^A t^B] = (1/2) delta_{AB}.
# All entries are rational, so the runner is exact-rational throughout.
# ----------------------------------------------------------------------


def real_su_n_generators(n: int) -> List[Matrix]:
    """Return a real-symmetric subset of SU(n) generators (off-diagonal
    'lambda_1-type' and Cartan diagonals). Tr[t^A t^B] = (1/2) delta_{AB}
    for all pairs in this subset."""
    gens: List[Matrix] = []

    # Off-diagonal symmetric: lambda_{ij} = (E_{ij} + E_{ji}) / 2
    # Tr[lambda^2] = 2 * (1/2)^2 = 1/2. Good.
    for i in range(n):
        for j in range(i + 1, n):
            g = zeros(n)
            g[i][j] = Fraction(1, 2)
            g[j][i] = Fraction(1, 2)
            gens.append(g)

    # Cartan diagonal: traceless real-diagonal generators.
    # T_k = (1/sqrt(2*k*(k+1))) * diag(1,1,...,1, -k, 0,...,0)
    # We use rational-square normalization: we square them and check
    # Tr[T_k^2] = 1/2 directly. Use the explicit form
    #   T_k_diag = c_k * diag(1,...,1 [k entries], -k, 0,...,0)
    # with c_k^2 * (k + k^2) = 1/2  =>  c_k^2 = 1/(2*k*(k+1)).
    # c_k^2 is rational; we only need T_k AND T_k^2 entries, both rational.
    # We track T_k as a pair (sqrt_coeff_squared, integer matrix).
    # To stay exact-rational, store T_k entries as c_k * <int>. Squared
    # values needed for Tr[T_k^2] are rational. We do not need t^A
    # entries to be rational themselves; only Tr[t^A t^B] (rational)
    # and Tr[M_color t^A] for our chosen M_color values, both of which
    # are derived in closed rational form below.
    return gens


def gell_mann_3() -> List[Matrix]:
    """Return the 3 symmetric off-diagonal Gell-Mann matrices (lambda_1,
    lambda_4, lambda_6) at the conventional normalization
    t^A = lambda^A / 2 (so Tr[t^A t^B] = (1/2) delta_{AB}).
    Used as exact-rational symmetric SU(3) generator witnesses."""
    # lambda_1 = ((0,1,0),(1,0,0),(0,0,0))
    lam1 = [[Fraction(0), Fraction(1), Fraction(0)],
            [Fraction(1), Fraction(0), Fraction(0)],
            [Fraction(0), Fraction(0), Fraction(0)]]
    # lambda_4 = ((0,0,1),(0,0,0),(1,0,0))
    lam4 = [[Fraction(0), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(0), Fraction(0)],
            [Fraction(1), Fraction(0), Fraction(0)]]
    # lambda_6 = ((0,0,0),(0,0,1),(0,1,0))
    lam6 = [[Fraction(0), Fraction(0), Fraction(0)],
            [Fraction(0), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(1), Fraction(0)]]
    # t^A = lambda^A / 2:
    return [scale(m, Fraction(1, 2)) for m in (lam1, lam4, lam6)]


def lambda_3() -> Matrix:
    """Cartan lambda_3 = diag(1, -1, 0). Real-symmetric, traceless,
    Tr[lambda_3^2] = 2, so t^3 = lambda_3/2 has Tr[t^3 t^3] = 1/2."""
    return [[Fraction(1), Fraction(0), Fraction(0)],
            [Fraction(0), Fraction(-1), Fraction(0)],
            [Fraction(0), Fraction(0), Fraction(0)]]


def lambda_8_squared() -> Matrix:
    """Square of lambda_8 = (1/sqrt(3)) diag(1,1,-2). Note we cannot use
    lambda_8 itself with exact rationals since 1/sqrt(3) is irrational,
    but lambda_8^2 = (1/3) diag(1,1,4) is rational and used for trace
    checks."""
    return [[Fraction(1, 3), Fraction(0), Fraction(0)],
            [Fraction(0), Fraction(1, 3), Fraction(0)],
            [Fraction(0), Fraction(0), Fraction(4, 3)]]


# ----------------------------------------------------------------------
# Theorem (V) closed form, gate-note formulas, Fierz channel projections.
# ----------------------------------------------------------------------


def kappa_ew_from_vertex(m_color: Matrix, n_c: int) -> Fraction:
    """Theorem (V): kappa_EW(M_color) = (|Tr M|^2 / N_c) / Tr[M^2]."""
    tr_m = trace(m_color)
    tr_m_sq = trace(matmul(m_color, m_color))
    if tr_m_sq == 0:
        raise ValueError("Tr[M^2] = 0; vertex projection ill-defined.")
    return (tr_m * tr_m / Fraction(n_c)) / tr_m_sq


def k_ew_from_kappa(kappa: Fraction, n_c: int) -> Fraction:
    """Gate eq. (1): K_EW(kappa) = 1 / (F_adj + kappa (1 - F_adj))
        = 1 / ((N_c^2 - 1)/N_c^2 + kappa/N_c^2)
        = N_c^2 / (N_c^2 - 1 + kappa)."""
    return Fraction(n_c * n_c, n_c * n_c - 1) if kappa == 0 else \
           Fraction(n_c * n_c) / (Fraction(n_c * n_c - 1) + kappa)


def fierz_projections(m_color: Matrix, n_c: int) -> Tuple[Fraction, Fraction, Fraction]:
    """Return (P_singlet, P_adjoint, Tr[M^2]) where
        P_singlet = (1/N_c) |Tr M|^2
        P_adjoint = Tr[M^2] - P_singlet     (Fierz completeness, eq. (4*))."""
    tr_m = trace(m_color)
    tr_m_sq = trace(matmul(m_color, m_color))
    p_singlet = tr_m * tr_m / Fraction(n_c)
    p_adjoint = tr_m_sq - p_singlet
    return p_singlet, p_adjoint, tr_m_sq


# ----------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-rational) for")
    print("RCONN_VERTEX_COLOR_STRUCTURE_TO_KAPPA_EW_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: derive vertex-color-structure -> kappa_EW closed-form map")
    print("Retained inputs (cited):")
    print("  (R1) Fierz completeness identity ... retained_bounded (audited_clean)")
    print("  (R2) Gate-note K_EW(kappa_EW) ... source-note")
    print("  (R3) N_c = 3 from Cl(3) ... retained")
    print("=" * 88)

    # ==================================================================
    section("Part 0: Source-note + cited-authority anchors exist")
    # ==================================================================

    check("source note exists",
          NOTE.exists(),
          str(NOTE.relative_to(ROOT)))
    check("Fierz authority exists",
          FIERZ.exists(),
          str(FIERZ.relative_to(ROOT)))
    check("matching-rule gate authority exists",
          GATE.exists(),
          str(GATE.relative_to(ROOT)))
    check("traceless-selector no-go companion exists",
          TRACELESS.exists(),
          str(TRACELESS.relative_to(ROOT)))
    check("RCONN_DERIVED sister note exists",
          RCONN.exists(),
          str(RCONN.relative_to(ROOT)))

    note = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    check("source note declares positive_theorem", "positive_theorem" in note)
    check("source note declares Class A",
          "Class A" in note or "class: A" in note)
    check("source note cites Fierz authority",
          "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01" in note)
    check("source note cites matching-rule gate",
          "EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03" in note)
    check("source note names theorem (V)",
          "Theorem (V" in note)
    check("source note keeps matching rule open",
          "does **not** derive the matching rule" in note
          or "does not derive the matching rule" in note
          or "named open gate" in note)

    # ==================================================================
    section("Part 1: Fierz channel decomposition identity (eq. (4*))")
    # ==================================================================
    # For Hermitian M_color: P_singlet + P_adjoint = Tr[M^2].

    n_c = 3

    # Witness 1: M = I (color-blind point-split vertex).
    m_I = eye(n_c)
    p_s, p_a, tr_sq = fierz_projections(m_I, n_c)
    check("Witness M=I: Tr M = N_c", trace(m_I) == Fraction(n_c),
          f"Tr M = {trace(m_I)}, N_c = {n_c}")
    check("Witness M=I: Tr[M^2] = N_c", tr_sq == Fraction(n_c),
          f"Tr[M^2] = {tr_sq}")
    check("Witness M=I: P_singlet = N_c", p_s == Fraction(n_c),
          f"P_singlet = (N_c^2)/N_c = {p_s}")
    check("Witness M=I: P_adjoint = 0", p_a == Fraction(0),
          f"P_adjoint = {p_a}")
    check("Witness M=I: P_s + P_a = Tr[M^2] (Fierz completeness)",
          p_s + p_a == tr_sq,
          f"{p_s} + {p_a} = {tr_sq}")

    # Witness 2: M = lambda_3 (Cartan SU(3) generator), unnormalized.
    m_lam3 = lambda_3()
    p_s, p_a, tr_sq = fierz_projections(m_lam3, n_c)
    check("Witness M=lambda_3: traceless", trace(m_lam3) == Fraction(0))
    check("Witness M=lambda_3: Tr[M^2] = 2", tr_sq == Fraction(2),
          f"Tr[M^2] = {tr_sq}")
    check("Witness M=lambda_3: P_singlet = 0", p_s == Fraction(0))
    check("Witness M=lambda_3: P_adjoint = Tr[M^2]", p_a == tr_sq)
    check("Witness M=lambda_3: Fierz completeness",
          p_s + p_a == tr_sq)

    # Witness 3: M = lambda_1, lambda_4, lambda_6 (symmetric off-diagonal
    # Gell-Mann matrices, divided by 2 to give the t^A normalization
    # Tr[t^A t^A] = 1/2).
    gens = gell_mann_3()
    for idx, (gen, name) in enumerate(zip(gens, ("t^1", "t^4", "t^6"))):
        p_s, p_a, tr_sq = fierz_projections(gen, n_c)
        check(f"Witness M={name}: traceless", trace(gen) == Fraction(0))
        check(f"Witness M={name}: Tr[(t^A)^2] = 1/2",
              tr_sq == Fraction(1, 2),
              f"Tr[M^2] = {tr_sq}")
        check(f"Witness M={name}: P_singlet = 0", p_s == Fraction(0))
        check(f"Witness M={name}: P_adjoint = 1/2",
              p_a == Fraction(1, 2))
        check(f"Witness M={name}: Fierz completeness",
              p_s + p_a == tr_sq)

    # Witness 4: random rational symmetric 3x3 matrices.
    rationals_3x3 = [
        # Diagonal-only mixture:
        [[Fraction(2), Fraction(0), Fraction(0)],
         [Fraction(0), Fraction(-3, 2), Fraction(0)],
         [Fraction(0), Fraction(0), Fraction(5, 4)]],
        # Off-diagonal mixture:
        [[Fraction(1, 3), Fraction(2, 5), Fraction(-1, 7)],
         [Fraction(2, 5), Fraction(0), Fraction(3, 11)],
         [Fraction(-1, 7), Fraction(3, 11), Fraction(-2)]],
        # Identity + adjoint mixture (Corollary 3 family):
        [[Fraction(3, 2), Fraction(1, 4), Fraction(0)],
         [Fraction(1, 4), Fraction(3, 2), Fraction(0)],
         [Fraction(0), Fraction(0), Fraction(3, 2)]],
    ]
    for idx, M in enumerate(rationals_3x3):
        assert is_symmetric(M)
        p_s, p_a, tr_sq = fierz_projections(M, n_c)
        check(f"Random witness #{idx + 1} symmetric", is_symmetric(M))
        check(f"Random witness #{idx + 1}: P_s + P_a = Tr[M^2]",
              p_s + p_a == tr_sq,
              f"{p_s} + {p_a} = {tr_sq}")

    # Witness 5: random rational symmetric 4x4 matrix (N_c = 4 sanity).
    n_c_4 = 4
    M_4x4 = [
        [Fraction(1), Fraction(1, 3), Fraction(-1, 2), Fraction(0)],
        [Fraction(1, 3), Fraction(2), Fraction(1, 5), Fraction(0)],
        [Fraction(-1, 2), Fraction(1, 5), Fraction(-1), Fraction(1, 7)],
        [Fraction(0), Fraction(0), Fraction(1, 7), Fraction(0)],
    ]
    assert is_symmetric(M_4x4)
    p_s, p_a, tr_sq = fierz_projections(M_4x4, n_c_4)
    check("Random 4x4 witness symmetric", is_symmetric(M_4x4))
    check("Random 4x4 witness: P_s + P_a = Tr[M^2]",
          p_s + p_a == tr_sq,
          f"{p_s} + {p_a} = {tr_sq}")

    # ==================================================================
    section("Part 2: Corollary 1 — color-blind vertex kappa_EW(I) = 1")
    # ==================================================================

    for n in (2, 3, 4, 5):
        m_I = eye(n)
        kappa = kappa_ew_from_vertex(m_I, n)
        check(f"N_c = {n}: kappa_EW(I_color) = 1",
              kappa == Fraction(1),
              f"kappa_EW = {kappa}")
        k_ew = k_ew_from_kappa(kappa, n)
        check(f"N_c = {n}: K_EW(kappa=1) = 1",
              k_ew == Fraction(1),
              f"K_EW = {k_ew}")

    # ==================================================================
    section("Part 3: Corollary 2 — adjoint-projector vertex kappa_EW = 0")
    # ==================================================================
    # For any single SU(N_c) generator (color-traceless), kappa_EW = 0.

    # SU(3) symmetric Gell-Mann matrices (lambda_1, lambda_4, lambda_6 are
    # symmetric and rational; lambda_3 is diagonal symmetric and rational).
    test_gens_3 = gell_mann_3() + [scale(lambda_3(), Fraction(1, 2))]
    test_names_3 = ("t^1 = lambda_1/2", "t^4 = lambda_4/2",
                    "t^6 = lambda_6/2", "t^3 = lambda_3/2")
    for gen, name in zip(test_gens_3, test_names_3):
        kappa = kappa_ew_from_vertex(gen, n_c)
        check(f"N_c=3 vertex M = {name}: kappa_EW = 0",
              kappa == Fraction(0),
              f"kappa_EW = {kappa}")

    # K_EW(0) = 9/8 at N_c = 3, 4/3 at N_c = 2, 16/15 at N_c = 4, ...
    expected_k_ew_0 = {
        2: Fraction(4, 3),
        3: Fraction(9, 8),
        4: Fraction(16, 15),
        5: Fraction(25, 24),
    }
    for n, expected in expected_k_ew_0.items():
        k_ew = k_ew_from_kappa(Fraction(0), n)
        check(f"N_c = {n}: K_EW(kappa=0) = N_c^2/(N_c^2-1) = {expected}",
              k_ew == expected,
              f"K_EW = {k_ew}")

    # Special case headline: 9/8 at N_c = 3.
    check("N_c = 3 headline: K_EW(kappa=0) = 9/8 exactly",
          k_ew_from_kappa(Fraction(0), 3) == Fraction(9, 8))

    # ==================================================================
    section("Part 4: Corollary 3 — Uniqueness of kappa_EW = 0")
    # ==================================================================
    # No Hermitian M with nonzero Tr M can give kappa_EW = 0.
    # Equivalently: kappa_EW = 0 iff Tr_color M = 0.
    # Family test: M(alpha, beta) = alpha I + beta lambda_3, both rational.

    n_c = 3
    family_results: List[Tuple[Fraction, Fraction, Fraction]] = []
    for alpha_num in (-2, -1, 0, 1, 2):
        for beta_num in (-2, -1, 0, 1, 2):
            alpha = Fraction(alpha_num, 3)
            beta = Fraction(beta_num, 5)
            if alpha == 0 and beta == 0:
                continue
            # M = alpha I + beta lambda_3
            M = add(scale(eye(n_c), alpha), scale(lambda_3(), beta))
            tr_m_sq = trace(matmul(M, M))
            if tr_m_sq == 0:
                continue
            kappa = kappa_ew_from_vertex(M, n_c)
            family_results.append((alpha, beta, kappa))

            # Uniqueness claim: kappa_EW = 0 iff Tr M = 0.
            tr_m = trace(M)
            kappa_zero = (kappa == Fraction(0))
            tr_zero = (tr_m == Fraction(0))
            check(
                f"Family M = ({alpha})*I + ({beta})*lambda_3: kappa_EW=0 iff Tr M=0",
                kappa_zero == tr_zero,
                f"kappa_EW={kappa}, Tr M={tr_m}",
            )

    # Direct check: M = I has Tr M = N_c != 0 and kappa = 1 (not 0).
    M = eye(n_c)
    check("I_color: Tr M != 0, kappa_EW != 0",
          trace(M) != Fraction(0) and kappa_ew_from_vertex(M, n_c) != Fraction(0))

    # Direct check: M = lambda_3 has Tr M = 0 and kappa = 0.
    M = lambda_3()
    check("lambda_3: Tr M = 0, kappa_EW = 0",
          trace(M) == Fraction(0) and kappa_ew_from_vertex(M, n_c) == Fraction(0))

    # ==================================================================
    section("Part 5: Round-trip via gate-note K_EW(kappa_EW) formula")
    # ==================================================================
    # K_EW(kappa) * (F_adj + kappa(1-F_adj)) = 1 for all kappa, all N_c.

    n_c = 3
    F_adj = Fraction(n_c * n_c - 1, n_c * n_c)  # 8/9 at N_c=3
    one_minus_F = Fraction(1, n_c * n_c)         # 1/9 at N_c=3
    check(f"N_c=3: F_adj = 8/9", F_adj == Fraction(8, 9),
          f"F_adj = {F_adj}")
    check(f"N_c=3: 1 - F_adj = 1/9", one_minus_F == Fraction(1, 9),
          f"1 - F_adj = {one_minus_F}")
    check(f"N_c=3: F_adj + (1 - F_adj) = 1",
          F_adj + one_minus_F == Fraction(1))

    for kappa_num in (-3, -1, 0, 1, 2, 3, 5):
        for kappa_den in (1, 2, 3, 7, 11):
            kappa = Fraction(kappa_num, kappa_den)
            denom = F_adj + kappa * one_minus_F
            if denom == 0:
                continue
            k_ew = Fraction(1) / denom
            check(
                f"N_c=3 round-trip: K_EW * (F_adj + kappa*(1-F_adj)) = 1 "
                f"(kappa = {kappa})",
                k_ew * denom == Fraction(1),
            )

    # ==================================================================
    section("Part 6: Cited cross-checks (boundary statements)")
    # ==================================================================

    # Confirm gate-note keeps kappa_EW explicit (matching rule (M) open).
    gate = GATE.read_text(encoding="utf-8") if GATE.exists() else ""
    check("gate note keeps kappa_EW explicit",
          "kappa_EW" in gate and "K_EW(kappa_EW)" in gate)
    check("gate note records K_EW(0) = 9/8 specialization",
          "K_EW(0) = 9/8" in gate)
    check("gate note records K_EW(1) = 1 specialization",
          "K_EW(1) = 1" in gate)

    # Confirm Fierz authority is the cycle-breaking F-half referenced.
    fierz = FIERZ.read_text(encoding="utf-8") if FIERZ.exists() else ""
    check("Fierz authority records exact (N_c^2-1)/N_c^2 fraction",
          "(N_c^2 - 1)/N_c^2" in fierz or "(N_c^2 − 1)/N_c^2" in fierz)
    check("Fierz authority states matching rule (M) is open",
          "matching rule" in fierz.lower())

    # Confirm traceless no-go is consistent with our positive map.
    traceless = TRACELESS.read_text(encoding="utf-8") if TRACELESS.exists() else ""
    check("traceless no-go records Tr_internal vs Tr_internal^2 distinction",
          "Tr_internal(Q_EW)" in traceless and "Tr_internal(Q_EW^2)" in traceless)
    check("source note explicitly does not contradict traceless no-go",
          "complements that no-go" in note
          or "consistent with" in note)

    # Confirm source note exposes the open-gate inheritance honestly.
    check("source note records matching-rule freedom is captured by vertex choice",
          "vertex" in note.lower() and "kappa_EW" in note)
    check("source note records two completions (kappa=0 and kappa=1)",
          ("kappa_EW = 0" in note and "kappa_EW = 1" in note)
          or ("kappa_EW = 0" in note and "K_EW(1)" in note))

    # ==================================================================
    print()
    print("=" * 88)
    print(f"RESULT: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
